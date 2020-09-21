## 操作场景

在腾讯云容器服务 TKE 中，Pod Networking 的功能是由基于 IaaS 层私有网络 VPC 的高性能容器网络实现，而 service proxy 功能是由 kube-proxy 所支持的 ipvs/iptables 两种模式提供。因此建议在集群上，只使用 kube-router 的 Network Policy 功能进行网络访问控制。

>! 在 TKE 环境中，kube-router 仅作为 kube-proxy 功能的补充，不能完全把 kube-proxy 替换为 kube-router。


## 相关概念

### Network Policy

[Network Policy ](https://kubernetes.io/docs/concepts/services-networking/network-policies/) 是 Kubernetes 提供的一种资源，用于定义基于 Pod 的网络隔离策略。描述了一组 Pod 是否可以与其他组 Pod，以及其他 network endpoints 进行通信。

### Kube-router

Kube-router 是专为简化操作和提升性能而打造的一个交钥匙型 Kubernetes 网络解决方案。目前最新版本为0.2.0，主要具备以下三大功能点：
- Pod Networking
- IPVS/LVS based service proxy  
- Network Policy Controller 

更多详细信息请前往[ Kube-router 官网 ](https://www.kube-router.io)或[ Kube-router 项目地址 ](https://github.com/cloudnativelabs/kube-router)进行查看。

## 操作步骤

### 在 TKE 上部署 kube-router

#### 腾讯云提供的 kube-router 版本

腾讯云 PaaS 团队基于官方镜像最新版本`v0.2.1`，提供了镜像 `ccr.ccs.tencentyun.com/library/kube-router:v1`。在该项目的开发过程中，腾讯云 PaaS 团队积极建设社区，持续贡献了一些 feature support 及 bug fix，提交 PR 均已被社区合并，列表如下：

- [processing k8s version for NPC #488](https://github.com/cloudnativelabs/kube-router/pull/488)
- [Improve health check for cache synchronization #498](https://github.com/cloudnativelabs/kube-router/pull/498)
- [Make the comments of the iptables rules in NWPLCY chains more accurate and reasonable #527](https://github.com/cloudnativelabs/kube-router/pull/527)
- [Use ipset to manage multiple CIDRs in a network policy rule #529](https://github.com/cloudnativelabs/kube-router/pull/529)
- [Add support for 'except' feature of network policy rule#543](https://github.com/cloudnativelabs/kube-router/pull/543)
- [Avoid duplicate peer pods in npc rules variables #634](https://github.com/cloudnativelabs/kube-router/pull/634)
- [Support named port of network policy #679](https://github.com/cloudnativelabs/kube-router/pull/679)

接下来我们会继续为社区贡献，并提供腾讯云镜像的版本升级。

#### 部署 kube-router
在能够访问公网、能够访问容器服务集群 apiserver 的机器上，依次执行以下命令，完成 kube-router 部署：
> ? 
> - 如果集群节点开通了公网 IP，则可直接在集群节点上执行以下命令。
> - 如果集群节点没有开通公网 IP，则可以手动下载和粘贴 [yaml 文件](https://ask.qcloudimg.com/draft/4495365/4srd9nlfla.zip) 内容到节点, 保存为 `kube-router-firewall-daemonset.yaml`，再执行最后的 `kubectl create` 命令。
> 
```
wget https://ask.qcloudimg.com/draft/4495365/4srd9nlfla.zip
```
```
unzip 4srd9nlfla.zip
```
```
kubectl create -f kube-router-firewall-daemonset.yaml
```




#### yaml 文件内容和参数说明

`kube-router-firewall-daemonset.yaml` 文件内容如下：
```yaml
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
apiVersion: v1
kind: ServiceAccount
metadata:
  name: kube-router
  namespace: kube-system
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: kube-router
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: ServiceAccount
  name: kube-router
  namespace: kube-system
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
      serviceAccountName: kube-router
      containers:
      - name: kube-router
        image: ccr.ccs.tencentyun.com/library/kube-router:v1
        args: ["--run-router=false", "--run-firewall=true", "--run-service-proxy=false", "--iptables-sync-period=5m", "--cache-sync-timeout=3m"]
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
```

args 说明：
- "--run-router=false"，"--run-firewall=true"，"--run-service-proxy=false"：只加载 firewall 模块。
- --iptables-sync-period=5m：指定定期同步 iptables 规则的间隔时间，根据准确性的要求设置，默认5m。
- --cache-sync-timeout=3m：指定启动时将 k8s 资源做缓存的超时时间，默认1m。鉴于一些资源对象较多的集群缓存同步时间可能较长，该值推荐设置为3m。



### NetworkPolicy 配置示例
- nsa namespace 下的 Pod 可互相访问，而不能被其它任何 Pod 访问。
```yaml
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
- nsa namespace 下的 Pod 不能被任何 Pod 访问。
 ```yaml
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
- nsa namespace 下的 Pod 只在 6379/TCP 端口可以被带有标签 app: nsb 的 namespace 下的 Pod 访问，而不能被其它任何 Pod 访问。
```yaml
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
- nsa namespace 下的 pod 可以访问 CIDR 为14.215.0.0/16的 network endpoint 的5978/TCP 端口，而不能访问其它任何 network endpoints（此方式可以用来为集群内的服务开访问外部 network endpoints 的白名单）。
```yaml
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
- default namespace 下的 Pod 只在80/TCP 端口可以被 CIDR 为14.215.0.0/16的 network endpoint 访问，而不能被其它任何 network endpoints 访问。
```yaml
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

#### 附: 测试情况

| 用例名称 | 测试结果 |
| -------- | -------- |
| 不同 namespace 的 Pod 互相隔离，同一 namespace 的 Pod 互通 | 通过 |
| 不同 namespace 的 Pod 互相隔离，同一 namespace 的 Pod 隔离 | 通过 |
| 不同 namespace 的 Pod 互相隔离，白名单指定 namespace B 可以访问 namespace A | 通过 |
| 允许某个 namespace 访问集群外某个 CIDR，其他外部 IP 全部隔离 | 通过 |
| 不同 namespace 的 Pod 互相隔离，白名单指定 namespace B 可以访问 namespace A 中对应的 Pod 以及端口 | 通过 |
| 以上用例，当 source Pod 和 destination Pod 在一个 Node 上时，隔离生效 | 通过 |

功能测试用例请参见 [#kube-router 测试用例.xlsx.zip#](https://ask.qcloudimg.com/draft/982360/dgs7x4hcly.zip)。

## 性能测试方案

在 k8s 集群中部署大量的 Nginx 服务，通过 ApacheBench 工具压测固定的一个服务，对比开启和不开启 kube-router 场景下的 QPS，衡量 kube-router 带来的性能损耗。

### 测试环境

- VM 数量：100
- VM 配置：2核4G
- VM OS：Ubuntu
- k8s：1.10.5
- kube-router version：0.2.0 

### 测试流程
1. 部署1个 service，对应两个 Pod（Nginx），作为测试组。
2. 部署1000个 service，每个分别对应 2/6/8 个 Pod（Nginx），作为干扰组。
3. 部署 NetworkPolicy 规则，使得所有 Pod 都被选中，以便产生足够数量的 iptables 规则：
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
4. 使用 ab 压测测试组的服务，记录 QPS。
得出性能曲线如下：
![](https://main.qcloudimg.com/raw/29f9a28f68844e497cf08c8bd72cbffe.png)
	- X轴：ab 并发数
	- Y轴：QPS

### 测试结论

Pod 数量从2000增长到8000，开启 kube-router 时的性能比不开启时要下降10% - 20%。
