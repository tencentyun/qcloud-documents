本身 Prometheus 是 [Cloud Native Computing Foundation（CNCF）](https://cncf.io/)  下衍生的第2个项目，所以与 Kubernetes 有着深度的集成，但是还是有一定的学习成本， Prometheus 监控服务为了降低用户的学习及使用成本，与腾讯云上的容器服务 TKE 做了深度的集成，可一键安装 Agent 的同时提供原生的 Prometheus 服务。

## 准备工作

- 在 [腾讯云容器服务](https://console.cloud.tencent.com/tke2/cluster) 中创建 Kubernetes 集群，具体操作请参见 [托管版集群](https://cloud.tencent.com/document/product/457/32189#TemplateCreation)。
- 服务角色授权：集成过程中需要用户授权之后来操作腾讯云容器服务 (TKE)，具体的授权操作请参见 [服务授权相关角色权限说明](https://cloud.tencent.com/document/product/1416/56023)。
- 已经进入到集成容器服务管理页面。

## 操作步骤

### 安装 Agent[](id:install_agent)

1. 用户成功授权服务角色之后，可以列出当前地域与 Prometheus 服务相同私有网络 VPC 下的容器服务 TKE 集群列表信息。
 >?由于网络的原因，不在同一私有网络 VPC 下的容器服务 TKE 集群不会显示在列表中。
2. 在集群列表中选择对应的容器集群 > 单击**安装**来进行自动化集成，在安装弹框中可以选择需要集成的 [基础监控](https://cloud.tencent.com/document/product/1416/56002) 组件，整个集成安装操作为异步操作，大概需要2 - 3分钟左右，监控状态显示“已安装”即装成功。
![](https://main.qcloudimg.com/raw/6c858ad4866adda3eec7f78c3838a8cb.png)

### 卸载监控组件

如需停止对容器服务的 Kubernetes 集群监控，请按照以下步骤卸载 Prometheus Agent 及其监控组件。

集群列表中选择对应的容器集群，单击**卸载**来进行自动化卸载操作，在弹框中确认卸载即可，整个卸载操作为异步操作，大概需要2 - 3分钟左右。
