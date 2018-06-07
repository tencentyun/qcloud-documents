## 概述

通过在 Kubernetes 集群中部署 virtual kubelet 后即可通过该集群的 APIServer 调度管理 CIS 实例。

## 操作步骤

以在 [腾讯云容器服务](https://cloud.tencent.com/product/ccs) 的 Kubernetes 集群中使用 CIS 调度部署 Deployment 为例。

1. 登录任一和腾讯云网络互通的 Kubernetes 节点，比如 [CCS](https://console.cloud.tencent.com/ccs) 集群、用户使用 CVM 自建的 Kubernetes 集群、用户使用专线和腾讯云互通的 IDC 自建的 Kubernetes 集群。

2. 使用 Kubectl 或调用 Kubernetes API 在集群的节点上部署 virtual kubelet，详情请参考 [virtual-kubelet 部署指导](https://console.cloud.tencent.com/ccs)。

3. 完成 virtual kubelet 部署后会在集群中看到新增一个 pod （virtual-kubelet）和虚拟节点（virtual-kubelet）。

  ![][1]

4. 部署 Deployment ，并指定 nodeName 为 virtual-kubelet 。

  ![][2]

   则会把该 Deployment 的 pod 调度到虚拟节点 virtual-kubelet 上。

  ![][3]

5. 完成部署后，在 [CCS 控制台](https://console.cloud.tencent.com/ccs) 的【服务】中可以看到刚刚创建的 Deployment 。
   
	![][4]

  但 Deployment 并没有使用 CCS 集群节点的资源，而是把 Pod 创建到了 CIS 中，所以其 Pod 可以在 [CIS控制台](https://console.cloud.tencent.com/cis) 的【容器实例】中看到。

  ![][5]

[1]:https://main.qcloudimg.com/raw/e26ab86e8de97abf36380482703b932f.png
[2]:https://main.qcloudimg.com/raw/c1406a0b424a94a04fd90d19eec83c55.png
[3]:https://main.qcloudimg.com/raw/8e4c0d95784dee3700c783f8bd911a60.png
[4]:https://main.qcloudimg.com/raw/8066e7a39d8686f9ca226dd606000e1a.png
[5]:https://main.qcloudimg.com/raw/d49e91a8c69dcf3e44253e262a4cbaef.png
