## 腾讯云容器服务TKE开源组件

### 1.tencentcloud-cloud-controller-manager
tencentcloud-cloud-controller-manager 是腾讯云容器服务的 cloud controller manager 的实现。通过该组件可以在腾讯云通过云主机自建的Kubenrentes集群上实现以下功能：

- nodecontroller - 更新 kubernetes node 相关的 addresses 信息。
- routecontroller - 负责创建 vpc 内 pod 网段内的路由。
- servicecontroller - 当集群中创建了类型为 LoadBalancer 的 service 的时候，创建相应的LoadBalancers。

更多安装使用说明可[查看详情](https://github.com/tencentcloud/tencentcloud-cloud-controller-manager/blob/master/README_zhCN.md).

### 2.kubernetes-csi-tencentcloud
kubernetes-csi-tencentloud 是腾讯云 Cloud Block Storage 服务的一个满足 CSI 标准实现的插件。通过该插件可以在腾讯云通过云主机自建的Kubenrentes集群 使用Cloud Block Storage。 

更多安装使用说明可[查看详情](https://github.com/tencentcloud/kubernetes-csi-tencentcloud/blob/master/README_zhCN.md).