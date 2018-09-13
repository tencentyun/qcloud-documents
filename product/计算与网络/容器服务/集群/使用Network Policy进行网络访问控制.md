## 使用Network Policy进行网络访问控制

### Network Policy

[Network Policy](https://kubernetes.io/docs/concepts/services-networking/network-policies/)是k8s提供的一种资源，用于定义基于pod的网络隔离策略。它描述了一组pod是否可以与其它组pod，以及其它network endpoints进行通信。

### Kube-router

- 官网:  [https://www.kube-router.io](https://www.kube-router.io)
- 项目地址:  [https://github.com/cloudnativelabs/kube-router](https://github.com/cloudnativelabs/kube-router)

目前kube-router最新版本为0.2.0

kube-router的三大功能：

- Pod Networking
- IPVS/LVS based service proxy  
- Network Policy Controller 

在腾讯云TKE上，Pod Networking的功能由基于IAAS层VPC的高性能容器网络实现，service proxy功能由kube-proxy所支持的ipvs/iptalbes两种模式来提供。建议在TKE上，只使用kube-router的Network Policy功能。

### 在TKE上部署kube-router

#### 腾讯云提供的kube-router版本

下面提供的yaml文件中使用的kube-router镜像"ccr.ccs.tencentyun.com/library/kube-router:v1"是由腾讯云PAAS团队提供的。 这个镜像是基于社区2018-07-29的commit "e2ee6a76"， 加上腾讯云PAAS团队的两个bugfix（均已被社区合并）：

- [https://github.com/cloudnativelabs/kube-router/pull/488](https://github.com/cloudnativelabs/kube-router/pull/488)
- [https://github.com/cloudnativelabs/kube-router/pull/498](https://github.com/cloudnativelabs/kube-router/pull/498)

我们会跟踪社区进展， 提供版本升级。

#### 部署kube-router

Daemonset yaml文件：  [#kube-router-firewall-daemonset.yaml.zip#](https://ask.qcloudimg.com/draft/982360/90i1a7pucf.zip)

在**能访问公网**，也能访问TKE集群apiserver的机器上，执行以下命令即可完成kube-router部署。

如果集群节点开通了公网IP，则可以直接在集群节点上执行以下命令。

如果集群节点没有开通公网IP, 则可以手动下载和粘贴yaml文件内容到节点, 保存为kube-router-firewall-daemonset.yaml，再执行最后的kubectl create命令。

```
wget https://ask.qcloudimg.com/draft/982360/90i1a7pucf.zip
unzip 90i1a7pucf.zip
kuebectl create -f kube-router-firewall-daemonset.yaml
```

#### yaml文件内容和参数说明

kube-router-firewall-daemonset.yaml文件内容：

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

args说明：

1. "--run-router=false", "--run-firewall=true", "--run-service-proxy=false"：只加载firewall模块；
2. kubeconfig：用于指定master信息，映射到主机上的kubectl配置目录/root/.kube/config；
3. --iptables-sync-period=1s：指定同步iptables规则的间隔时间，根据实时性的要求设置，默认5m；
4. --cache-sync-timeout=5m：指定启动时将k8s资源做缓存的超时时间，默认5m；

### NetworkPolicy配置示例

#### 1.nsa namespace下的pod可互相访问，而不能被其它任何pod访问

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

#### 2.nsa namespace下的pod不能被任何pod访问

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

#### 3.nsa namespace下的pod只在6379/TCP端口可以被带有标签app: nsb的namespace下的pod访问，而不能被其它任何pod访问

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

#### 4.nsa namespace下的pod可以访问CIDR为14.215.0.0/16的network endpoint的5978/TCP端口，而不能访问其它任何network endpoints（此方式可以用来为集群内的服务开访问外部network endpoints的白名单）

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

#### 5.default namespace下的pod只在80/TCP端口可以被CIDR为14.215.0.0/16的network endpoint访问，而不能被其它任何network endpoints访问

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
| 不同namespace的pod互相隔离，同一namespace的pod互通 | 通过 |
| 不同namespace的pod互相隔离，同一namespace的pod隔离 | 通过 |
| 不同namespace的pod互相隔离，白名单指定B可以访问A | 通过 |
| 允许某个namespace访问集群外某个CIDR，其他外部IP全部隔离 | 通过 |
| 不同namespace的pod互相隔离，白名单指定B可以访问A中对应的pod以及端口 | 通过 |
| 以上用例，当source pod 和 destination pod在一个node上时，隔离是否生效 | 不通过 |


功能测试用例

> [#kube-router测试用例.xlsx.zip#](https://ask.qcloudimg.com/draft/982360/dgs7x4hcly.zip)




### 性能测试方案

在k8s集群中部署大量的Nginx服务，通过ApacheBench工具压测固定的一个服务，对比开启和不开启kube-router场景下的QPS，衡量kube-router带来的性能损耗。

### 测试环境

VM数量: 100

VM配置: 2核4G

VM OS: ubuntu

k8s: 1.10.5

kube-router version: 0.2.0 

# 测试流程

1.部署1个service，对应两个pod（Nginx），作为测试组；

2.部署1000个service，每个分别对应2/6/8个pod（Nginx），作为干扰组；

3.部署NetworkPolicy规则，使得所有pod都被选中，以便产生足够数量的iptables规则：

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

4.使用ab压测测试组的服务，记录QPS.

### 性能曲线

![kube-router.png](https://ask.qcloudimg.com/draft/982360/c2dvr6rprd.png)

X轴：ab并发数

Y轴：QPS

### 测试结论

pod数量从2000到8000，开启kube-router时的性能比不开启时要下降10%-20%。