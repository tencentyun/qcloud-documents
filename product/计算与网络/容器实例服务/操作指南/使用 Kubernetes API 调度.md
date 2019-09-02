## 概述
在 Kubernetes 集群中部署 Virtual Kubelet 后，即可通过该集群的 apiserver 组件调度管理 CIS 实例。

## 操作步骤
以在腾讯云容器服务的 Kubernetes 集群中使用 CIS 调度部署 Deployment 为例。
1. 登录任一和腾讯云网络互通的 Kubernetes 节点，例如 TKE 集群、您使用 CVM 自建的 Kubernetes 集群、您使用专线和腾讯云互通的 IDC 自建的 Kubernetes 集群等。

2. 使用 Kubectl 或调用 Kubernetes API 在集群的节点上部署 Virtual Kubelet，详情请参考 [virtual-kubelet 部署指南](https://cloud.tencent.com/document/product/858/17680)。

3. 完成 Virtual Kubelet 部署后，查看节点和 Pod。
```
kubectl get nodes -o wide
```
```
kubectl get pods -o wide
```
会发现集群中会新增一个 Pod 和虚拟节点，名称相同：virtual-kubelet。
![][1]

4. 部署 Deployment ，并指定 nodeName 为 virtual-kubelet，把该 Deployment 的 Pod 调度到虚拟节点 virtual-kubelet 上。
```
kubectl create -f service-nginx.yaml
```
![][2]
查看 Pod 状态，示例如下：
![][3]

5. 完成部署后，在 [TKE 控制台](https://console.cloud.tencent.com/ccs) 的【服务】中可以看到刚刚创建的 Deployment 。
![](https://main.qcloudimg.com/raw/1f2783348ab6bd50de2fdca33a2b1aa9.png)
但 Deployment 并没有使用 TKE 集群节点的资源，而是把 Pod 创建到了 CIS 中，所以其 Pod 可以在 [CIS控制台](https://console.cloud.tencent.com/cis) 的【容器实例】中看到。
![][5]

[1]:https://main.qcloudimg.com/raw/e26ab86e8de97abf36380482703b932f.png
[2]:https://main.qcloudimg.com/raw/c1406a0b424a94a04fd90d19eec83c55.png
[3]:https://main.qcloudimg.com/raw/8e4c0d95784dee3700c783f8bd911a60.png
[4]:https://main.qcloudimg.com/raw/8066e7a39d8686f9ca226dd606000e1a.png
[5]:https://main.qcloudimg.com/raw/d49e91a8c69dcf3e44253e262a4cbaef.png
