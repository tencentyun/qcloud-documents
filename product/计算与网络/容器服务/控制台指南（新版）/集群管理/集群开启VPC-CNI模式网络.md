## 集群开启VPC-CNI模式网络

### VPC-CNI模式说明

VPC-CNI模式是腾讯云容器服务支持的扩展网络模式，利用腾讯云的多弹性网卡能力，为集群内的Pod分配VPC内的IP地址。 由腾讯云VPC功能负责路由，可实现Pod和Node的控制面和数据面完全在同一网络层面，该模式下的Pod能够复用腾讯云VPC所有产品特性。

VPC-CNI模式存在使用限制，建议您提前考虑是否适配您的业务场景。

### VPC-CNI模式应用场景

集群开启VPC-CNI模式后，创建工作负载时可以选择工作负载使用VPC-CNI模式，在VPC-CNI模式下能够支持：

1. StatefulSet支持固定IP类型的Pod - 该类型的Pod重启和迁移保持IP不变。适用于需要对IP来源做访问限制、通过IP查询日志等场景。

### VPC-CNI模式使用限制

1. 仅支持k8s 1.10，1.12集群

2. 集群需要开启cni支持。

3. 当前VPC-CNI模式仅支持单一子网，因此该模式下的Pod不可跨可用区调度。

4. 当前VPC-CNI模式的子网不能与其他云上资源共用（如CVM、CLB等）。

5. 和子网处于相同可用区的节点才支持创建VPC-CNI模式的Pod，请提前规划VPC-CNI模式子网。

6. 您需要指定单节点下VPC-CNI模式的Pod数量上限， 创建后不可修改。建议集群中节点配置相同

### VPC-CNI模式使用方法

#### 开启VPC-CNI

1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)。

2. 在左侧导航栏中，单击【集群】，进入集群管理页面。点击【基本信息】。

3. 在VPC-CNI字段中点击开启，选择子网，并确认使用限制。如下图示

![open][1]

#### 关闭VPC-CNI

1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)。

2. 在左侧导航栏中，单击【集群】，进入集群管理页面。点击【基本信息】。

3. 在VPC-CNI字段中点击关闭。（仅支持在集群内不存在任何VPC-CNI模式的Pod时关闭）

![close][2]

[1]: https://main.qcloudimg.com/raw/2fb53bed77df80d2859ea213cdaee7c6.png

[2]:https://main.qcloudimg.com/raw/25bf97e355533a5e8678567567c5aefd.png
