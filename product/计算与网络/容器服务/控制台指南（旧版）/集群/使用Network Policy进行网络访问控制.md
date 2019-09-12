## Network Policy

[Network Policy](https://kubernetes.io/docs/concepts/services-networking/network-policies/) 是 k8s 提供的一种资源，用于定义基于 pod 的网络隔离策略。它描述了一组 pod 是否可以与其它组 pod，以及其它 network endpoints 进行通信。

## Kube-router

- 官网:  [https://www.kube-router.io](https://www.kube-router.io)
- 项目地址:  [https://github.com/cloudnativelabs/kube-router](https://github.com/cloudnativelabs/kube-router)

目前 kube-router 最新版本为 0.2.0

kube-router 的三大功能：

- Pod Networking
- IPVS/LVS based service proxy  
- Network Policy Controller 

在腾讯云 TKE 上，Pod Networking 的功能由基于 IAAS 层 VPC 的高性能容器网络实现，service proxy 功能由 kube-proxy 所支持的 ipvs/iptalbes 两种模式来提供。建议在 TKE 上，只使用 kube-router 的 Network Policy 功能。

## 在 TKE 上部署 kube-router

### 腾讯云提供的 kube-router 版本

下面提供的 yaml 文件中使用的 kube-router 镜像`ccr.ccs.tencentyun.com/library/kube-router:v1` 是由腾讯云 PAAS 团队提供的。 这个镜像是基于社区 2018-07-29 的 commit "e2ee6a76"， 加上腾讯云 PAAS 团队的两个 bugfix（均已被社区合并）：

- [https://github.com/cloudnativelabs/kube-router/pull/488](https://github.com/cloudnativelabs/kube-router/pull/488)
- [https://github.com/cloudnativelabs/kube-router/pull/498](https://github.com/cloudnativelabs/kube-router/pull/498)

我们会跟踪社区进展，提供版本升级。

### 部署 kube-router

Daemonset yaml 文件：[#kube-router-firewall-daemonset.yaml.zip#](https://ask.qcloudimg.com/draft/982360/90i1a7pucf.zip)

在 **能访问公网**，也能访问 TKE 集群 apiserver 的机器上，执行以下命令即可完成 kube-router 部署。

如果集群节点开通了公网 IP，则可以直接在集群节点上执行以下命令。

如果集群节点没有开通公网 IP，则可以手动下载和粘贴 yaml 文件内容到节点, 保存为 kube-router-firewall-daemonset.yaml，再执行最后的 kubectl create 命令。

```
wget https://ask.qcloudimg.com/draft/982360/90i1a7pucf.zip
unzip 90i1a7pucf.zip
kubectl create -f kube-router-firewall-daemonset.yaml
```

### yaml 文件内容和参数说明

kube-router-firewall-daemonset.yaml 文件内容：

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: kube-router-cfg
  namespace: kube-system
  labels:
    tier: node
    k8s-app: kube-router
data:
  cni-conf.json: |
    {
      "name":"kubernetes",
      "type":"bridge",
      "bridge":"kube-bridge",
      "isDefaultGateway":true,
      "ipam": {
        "type":"host-local"
      }
    }
---
apiVersion: extensions/v1beta1
kind: DaemonSet
metadata:
  name: kube-router
  namespace: kube-system
  labels:
    k8s-app: kube-router
spec:
  template:
    metadata:
      labels:
        k8s-app: kube-router
      annotations:
        scheduler.alpha.kubernetes.io/critical-pod: ''
    spec:
      containers:
      - name: kube-router
        image: ccr.ccs.tencentyun.com/library/kube-router:v1
        args: ["--run-router=false", "--run-firewall=true", "--run-service-proxy=false", "--kubeconfig=/var/lib/kube-router/kubeconfig", "--iptables-sync-period=1s", "--cache-sync-timeout=5m"]
        securityContext:
          privileged: true
        imagePullPolicy: Always
        env:
        - name: NODE_NAME
          valueFrom:
            fieldRef:
              fieldPath: spec.nodeName
        livenessProbe:
          httpGet:
            path: /healthz
            port: 20244
          initialDelaySeconds: 10
          periodSeconds: 3
        volumeMounts:
        - name: lib-modules
          mountPath: /lib/modules
          readOnly: true
        - name: cni-conf-dir
          mountPath: /etc/cni/net.d
        - name: kubeconfig
          mountPath: /var/lib/kube-router/kubeconfig
          readOnly: true
      initContainers:
      - name: install-cni
        image: busybox
        imagePullPolicy: Always
        command:
        - /bin/sh
        - -c
        - set -e -x;
          if [ ! -f /etc/cni/net.d/10-kuberouter.conf ]; then
            TMP=/etc/cni/net.d/.tmp-kuberouter-cfg;
            cp /etc/kube-router/cni-conf.json ${TMP};
            mv ${TMP} /etc/cni/net.d/10-kuberouter.conf;
          fi
        volumeMounts:
        - name: cni-conf-dir
          mountPath: /etc/cni/net.d
        - name: kube-router-cfg
          mountPath: /etc/kube-router
      hostNetwork: true
      tolerations:
      - key: CriticalAddonsOnly
        operator: Exists
      - effect: NoSchedule
        key: node-role.kubernetes.io/master
        operator: Exists
      volumes:
      - name: lib-modules
        hostPath:
          path: /lib/modules
      - name: cni-conf-dir
        hostPath:
          path: /etc/cni/net.d
      - name: kube-router-cfg
        configMap:
          name: kube-router-cfg
      - name: kubeconfig
        hostPath:
          path: /root/.kube/config
```

args 说明：

1. "--run-router=false", "--run-firewall=true", "--run-service-proxy=false"：只加载 firewall 模块；
2. kubeconfig：用于指定 master 信息，映射到主机上的 kubectl 配置目录`/root/.kube/config`；
3. --iptables-sync-period=1s：指定同步 iptables 规则的间隔时间，根据实时性的要求设置，默认 5 m；
4. --cache-sync-timeout=5m：指定启动时将 k8s 资源做缓存的超时时间，默认 5 m；

## NetworkPolicy 配置示例

1. nsa namespace 下的 pod 可互相访问，而不能被其它任何 pod 访问。
```
apiVersion: extensions/v1beta1
kind: NetworkPolicy
metadata:
  name: npa
  namespace: nsa
spec:
  ingress: 
  - from:
    - podSelector: {} 
  podSelector: {} 
  policyTypes:
  - Ingress
```

2. nsa namespace 下的 pod 不能被任何 pod 访问。
```
apiVersion: extensions/v1beta1
kind: NetworkPolicy
metadata:
  name: npa
  namespace: nsa
spec:
  podSelector: {}
  policyTypes:
  - Ingress
```

3. nsa namespace 下的 pod 只在 6379/TCP 端口可以被带有标签 app: nsb 的 namespac e 下的 pod 访问，而不能被其它任何 pod 访问。
```
apiVersion: extensions/v1beta1
kind: NetworkPolicy
metadata:
  name: npa
  namespace: nsa
spec:
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          app: nsb
    ports:
    - protocol: TCP
      port: 6379
  podSelector: {}
  policyTypes:
  - Ingress
```

4. nsa namespace 下的 pod 可以访问 CIDR 为 14.215.0.0/16 的 network endpoint 的5978/TCP 端口，而不能访问其它任何 network endpoints（此方式可以用来为集群内的服务开访问外部 network endpoints 的白名单）。
```
apiVersion: extensions/v1beta1
kind: NetworkPolicy
metadata:
  name: npa
  namespace: nsa
spec:
  egress:
  - to:
    - ipBlock:
        cidr: 14.215.0.0/16
    ports:
    - protocol: TCP
      port: 5978
  podSelector: {}
  policyTypes:
  - Egress
```

5. default namespace 下的 pod 只在 80/TCP 端口可以被 CIDR 为 14.215.0.0/16 的 network endpoint 访问，而不能被其它任何 network endpoints 访问。
```
apiVersion: extensions/v1beta1
kind: NetworkPolicy
metadata:
  name: npd
  namespace: default
spec:
  ingress:
  - from:
    - ipBlock:
        cidr: 14.215.0.0/16
    ports:
    - protocol: TCP
      port: 80
  podSelector: {}
  policyTypes:
  - Ingress
```

### 附: 测试情况

| 用例名称 | 测试结果 |
|:----|:----|
| 不同 namespace 的 pod 互相隔离，同一 namespace 的 pod 互通 | 通过 |
| 不同 namespace 的 pod 互相隔离，同一 namespace 的 pod 隔离 | 通过 |
| 不同 namespace 的 pod 互相隔离，白名单指定 namespace B 可以访问 namespace A | 通过 |
| 允许某个 namespace 访问集群外某个 CIDR，其他外部 IP 全部隔离 | 通过 |
| 不同 namespace 的 pod 互相隔离，白名单指定 namespace B 可以访问 namespace A 中对应的 pod 以及端口 | 通过 |
| 以上用例，当 source pod 和 destination pod 在一个 node 上时，隔离生效 | 不通过 |

功能测试用例请参见 [#kube-router 测试用例.xlsx.zip#](https://ask.qcloudimg.com/draft/982360/dgs7x4hcly.zip)。




## 性能测试方案

在 k8s 集群中部署大量的 Nginx 服务，通过 ApacheBench 工具压测固定的一个服务，对比开启和不开启 kube-router 场景下的 QPS，衡量 kube-router 带来的性能损耗。

### 测试环境

VM 数量: 100

VM 配置: 2 核 4 G

VM OS: ubuntu

k8s: 1.10.5

kube-router version: 0.2.0 

### 测试流程

1. 部署 1 个 service，对应两个 pod（Nginx），作为测试组；

2. 部署 1000 个 service，每个分别对应 2/6/8 个 pod（Nginx），作为干扰组；

3. 部署 NetworkPolicy 规则，使得所有 pod 都被选中，以便产生足够数量的 iptables 规则：
```
apiVersion: extensions/v1beta1
kind: NetworkPolicy
metadata:
  name: npd
  namespace: default
spec:
  ingress:
  - from:
    - ipBlock:
        cidr: 14.215.0.0/16
    ports:
    - protocol: TCP
      port: 9090
  - from:
    - ipBlock:
        cidr: 14.215.0.0/16
    ports:
    - protocol: TCP
      port: 8080
  - from:
    - ipBlock:
        cidr: 14.215.0.0/16
    ports:
    - protocol: TCP
      port: 80
  podSelector: {}
  policyTypes:
  - Ingress
```

4. 使用 ab 压测测试组的服务，记录 QPS.

### 性能曲线

![kube-router.png](https://ask.qcloudimg.com/draft/982360/c2dvr6rprd.png)

X轴：ab 并发数

Y轴：QPS

### 测试结论

pod 数量从 2000 到 8000，开启 kube-router 时的性能比不开启时要下降 10%-20%。
