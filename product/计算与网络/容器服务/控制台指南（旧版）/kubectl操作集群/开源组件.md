## tencentcloud-cloud-controller-manager
tencentcloud-cloud-controller-manager 是腾讯云容器服务的 Cloud Controller Manager 的实现。使用该组件，可以在通过腾讯云云服务器自建的 Kubenrentes 集群上实现以下功能：
- nodecontroller：更新 Kubernetes node 相关的 addresses 信息。
- routecontroller：负责创建私有网络内 pod 网段内的路由。
- servicecontroller：当集群中创建了类型为负载均衡的 service 的时候，创建相应的负载均衡。

更多安装使用说明，可查看 [GitHub tencentcloud-cloud-controller-manager](https://github.com/tencentcloud/tencentcloud-cloud-controller-manager/blob/master/README_zhCN.md)。

## kubernetes-csi-tencentcloud
kubernetes-csi-tencentcloud 是腾讯云云硬盘服务的一个满足 CSI 标准实现的插件。使用该组件，可以在通过腾讯云云服务器自建的 Kubenrentes 集群使用云硬盘。 
该插件适用与自建 Kubernetes 集群的时候使用云硬盘的插件，与容器服务集群自带的 `provisioner cloud.tencent.com/qcloud-cbs` 不相同。

更多安装使用说明，可查看 [GitHub kubernetes-csi-tencentcloud](https://github.com/TencentCloud/kubernetes-csi-tencentcloud)。


