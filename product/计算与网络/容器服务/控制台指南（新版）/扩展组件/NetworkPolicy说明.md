## 简介
### 组件介绍

Network Policy 是 Kubernetes 提供的一种资源，用于定义基于 Pod 的网络隔离策略。它描述了一组 Pod 是否可以与其他组 Pod，以及其他 Network Entities 进行通信。本组件提供了针对该资源的 Controller 实现。如果您希望在 IP 地址或端口层面（OSI 第3层或第4层）控制特定应用的网络流量，则可考虑使用本组件。

### 部署在集群内的 Kubernetes 对象

| Kubernetes 对象名称 | 类型               |             请求资源             | 所属 Namespace |
| :---------------- | :----------------- | :------------------------------ | ------------- |
| networkpolicy     | DaemonSet          | 每个实例CPU:250m，Memory:250Mi | kube-system   |
| networkpolicy     | ClusterRole        |               -                  | kube-system   |
| networkpolicy     | ClusterRoleBinding |              -                  | kube-system   |
| networkpolicy     | ServiceAccount     |              -                  | kube-system   |


## 操作步骤


1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)，在左侧导航栏中选择**集群**。
2. 在“集群管理”页面单击目标集群 ID，进入集群详情页。
3. 选择左侧菜单栏中的**组件管理**，进入 “组件列表” 页面。
4. 在“组件列表”页面中选择**新建**，并在“新建组件”页面中勾选 NetworkPolicy。NetworkPolicy 详细配置可参见 [Network Policy 最佳实践](https://cloud.tencent.com/document/product/457/19793)。
5. 单击**完成**即可创建组件。


