## tencentcloud-cloud-controller-manager
tencentcloud-cloud-controller-manager 是腾讯云容器服务的 Cloud Controller Manager 的实现。使用该组件，可以在通过腾讯云云服务器自建的 Kubenrentes 集群上实现以下功能：
- nodecontroller：更新 Kubernetes node 相关的 addresses 信息。
- routecontroller：负责创建 VPC 内 pod 网段内的路由。
- servicecontroller：当集群中创建了类型为 LoadBalancer 的 service 的时候，创建相应的 LoadBalancers。

更多安装使用说明，可查看 GitHub [详细介绍](https://github.com/tencentcloud/tencentcloud-cloud-controller-manager/blob/master/README_zhCN.md)。

## kubernetes-csi-tencentcloud
kubernetes-csi-tencentcloud 是腾讯云 Cloud Block Storage 服务的一个满足 CSI 标准实现的插件。使用该组件，可以在通过腾讯云云服务器自建的 Kubenrentes 集群使用 Cloud Block Storage。 
该插件适用与自建 kubernetes 集群的时候使用cbs的插件，与TKE集群自带的 provisioner: cloud.tencent.com/qcloud-cbs 不相同。

更多安装使用说明，可查看 GitHub [详细介绍](https://github.com/tencentcloud/kubernetes-csi-tencentcloud/blob/master/README_zhCN.md)。

## ingress-tke-bm
ingress-tke-bm 是腾讯云 TKE 黑石集群的 ingress controller。该 controller 会监听 ingress 资源，创建黑石 lb 并绑定到对应 service。
更多安装使用说明，可查看 Github [详细介绍](https://github.com/TencentCloud/ingress-tke-bm)
