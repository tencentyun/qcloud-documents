## 操作场景
通过在集群节点上以 Daemonset 的形式运行 [NodeLocal DNS Cache](https://github.com/kubernetes/kubernetes/tree/master/cluster/addons/dns/nodelocaldns?spm=a2c6h.12873639.0.0.b8e3669eIhJqEN)，能够大幅提升集群内 DNS 解析性能，以及有效避免[ conntrack 冲突引发的 DNS 五秒延迟](https://www.weave.works/blog/racy-conntrack-and-dns-lookup-timeouts)。

本文接下来将详细介绍如何在 TKE 集群中使用 NodeLocal DNS Cache。

## 操作原理

通过 DaemonSet 在集群的每个节点上部署一个 hostNetwork 的 Pod，该 Pod 是 node-cache，可以缓存本节点上 Pod 的 DNS 请求。如果存在 cache misses ，该 Pod 将会通过 TCP 请求上游 kube-dns 服务进行获取。原理图如下所示：
<p style="text-align:center;"><img src="https://main.qcloudimg.com/raw/fafa6d3cccb18bcb4752eda667fa9d3b.png" style="box-shadow:0 0 0"></p>

>?NodeLocal DNS Cache 没有高可用性（High Availability，HA），会存在单点 nodelocal dns cache 故障（Pod Evicted/ OOMKilled/ConfigMap error/DaemonSet Upgrade），但是该现象其实是任何的单点代理（例如 kube-proxy，cni pod）都会存在的常见故障问题。

## 前提条件
已通过 [TKE 控制台](https://console.cloud.tencent.com/tke2/cluster) 创建了 Kubernetes 版本为 1.14 及以上的集群，且该集群中存在节点。



## 操作步骤

1. <span ID="StepOne"></span>一键部署 NodeLocal DNS Cache。YAML 示例如下：

	```
	---
apiVersion: v1
kind: ServiceAccount
metadata:
     name: node-local-dns
     namespace: kube-system
     labels:
		   kubernetes.io/cluster-service: "true"
       addonmanager.kubernetes.io/mode: Reconcile
	---
apiVersion: v1
kind: ConfigMap
metadata:
     name: node-local-dns
     namespace: kube-system
data:
     Corefile: |
       cluster.local:53 {
           errors
           cache {
                   success 9984 30
                   denial 9984 5
           }
           reload
           loop
           bind 169.254.20.10
           forward . __PILLAR__CLUSTER__DNS__ {
                   force_tcp
           }
           prometheus :9253
           health 169.254.20.10:8080
           }
       in-addr.arpa:53 {
           errors
           cache 30
           reload
           loop
           bind 169.254.20.10
           forward . __PILLAR__CLUSTER__DNS__ {
                   force_tcp
           }
           prometheus :9253
           }
       ip6.arpa:53 {
           errors
           cache 30
           reload
           loop
           bind 169.254.20.10
           forward . __PILLAR__CLUSTER__DNS__ {
                   force_tcp
           }
           prometheus :9253
           }
       .:53 {
           errors
           cache 30
           reload
           loop
           bind 169.254.20.10
           forward . /etc/resolv.conf 
           prometheus :9253
           }
	---
apiVersion: apps/v1
kind: DaemonSet
metadata:
	 name: node-local-dns
	 namespace: kube-system
	 labels:
	   k8s-app: node-local-dns
spec:
	 updateStrategy:
	   rollingUpdate:
	     maxUnavailable: 10%
	 selector:
	   matchLabels:
	     k8s-app: node-local-dns
	 template:
	   metadata:
	     labels:
           k8s-app: node-local-dns
			 annotations:
           prometheus.io/port: "9253"
           prometheus.io/scrape: "true"
	   spec:
	     serviceAccountName: node-local-dns
			 priorityClassName: system-node-critical
	     hostNetwork: true
	     dnsPolicy: Default  # Don't use cluster DNS.
	     tolerations:
	     - key: "CriticalAddonsOnly"
	       operator: "Exists"
	 	 	- effect: "NoExecute"
        operator: "Exists"
       - effect: "NoSchedule"
        operator: "Exists"
	     containers:
	     - name: node-cache
	       image: ccr.ccs.tencentyun.com/hale/k8s-dns-node-cache:1.15.13
	       resources:
	         requests:
	           cpu: 25m
	           memory: 5Mi
	       args: [ "-localip", "169.254.20.10", "-conf", "/etc/Corefile", "-setupiptables=true" ]
	       securityContext:
	         privileged: true
	       ports:
	       - containerPort: 53
	         name: dns
	         protocol: UDP
	       - containerPort: 53
	         name: dns-tcp
	         protocol: TCP
	       - containerPort: 9253
	         name: metrics
	         protocol: TCP
	       livenessProbe:
	         httpGet:
	           host: 169.254.20.10
	           path: /health
	           port: 8080
	         initialDelaySeconds: 60
	         timeoutSeconds: 5
	       volumeMounts:
	       - mountPath: /run/xtables.lock
	         name: xtables-lock
	         readOnly: false
	       - name: config-volume
	         mountPath: /etc/coredns
	       - name: kube-dns-config
	         mountPath: /etc/kube-dns
	     volumes:
	     - name: xtables-lock
	       hostPath:
	         path: /run/xtables.lock
	         type: FileOrCreate
	     - name: kube-dns-config
	       configMap:
	         name: kube-dns
	         optional: true
	     - name: config-volume
	       configMap:
	         name: node-local-dns
	         items:
	           - key: Corefile
	             path: Corefile.base
	```
2. 将 kubelet 的指定 dns 解析访问地址设置为[ 步骤1 ](#StepOne)中创建的 lcoal dns cache。本文提供以下两种配置方法，请根据实际情况进行选择：
 -  依次执行以下命令，修改 kubelet 启动参数并重启。
```
sed -i '/CLUSTER_DNS/c\CLUSTER_DNS="--cluster-dns=169.254.20.10"' /etc/kubernetes/kubelet
```
```
systemctl restart kubelet
```
 - 根据需求配置单个 Pod 的 dnsconfig 后重启。YAML 核心部分参考如下：
    - 需要将 nameserver 配置为169.254.20.10。
    - 为确保集群内部域名能够被正常解析，需要配置 searches。
    - 适当降低 ndots 值有利于加速集群外部域名访问。
    - 当 Pod 没有使用带有多个 dots 的集群内部域名的情况下，建议将值设为2。
	```
	dnsConfig:
	  nameservers: ["169.254.20.10"]
	  searches: 
		- default.svc.cluster.local
		- svc.cluster.local
		- cluster.local
	  options:
		- name: ndots
	      value: "2" 
	```
	
## 配置验证
本次测试集群为 Kubernetes 1.14 版本集群。在通过上述步骤完成 NodeLocal DNSCache 组件部署之后，可以参照以下方法进行验证：
1. 选择一个 debug pod，调整 kubelet 参数或者配置 dnsConfig 后重启。
2. Dig 外网域名，尝试在 coredns pod 上抓包。
3. 显示169.254.20.10正常工作即可证明 NodeLocal DNSCache 组件部署成功。如下图所示：
![](https://main.qcloudimg.com/raw/8990eecaa4497f006da9878c8b736e62.png)





