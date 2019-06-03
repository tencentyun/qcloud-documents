## 操作场景

VPC-CNI 模式是腾讯云容器服务支持的扩展网络模式，利用腾讯云的多弹性网卡能力，为集群内的 Pod 分配 VPC 中的 IP 地址。 由腾讯云 VPC 功能负责路由，可实现 Pod 和 Node 的控制面和数据面完全在同一网络层面，该模式下的 Pod能够复用腾讯云 VPC 所有产品特性。
集群开启 VPC-CNI 模式后，创建工作负载时可以使用 VPC-CNI 模式，在 VPC-CNI 模式下能够支持：
- StatefulSet 支持固定 IP 类型的 Pod。
- 该类型的 Pod 重启和迁移保持 IP 不变。适用于需要对 IP 来源做访问限制、通过 IP 查询日志等场景。

>!VPC-CNI 模式存在使用限制，建议您提前考虑是否适配您的业务场景。
- 仅支持 k8s1.10，k8s1.12集群。
- 集群需要开启 CNI 支持。
- 目前 VPC-CNI 模式仅支持单一子网，因此该模式下的 Pod 不可跨可用区调度。
- 目前 VPC-CNI 模式的子网不能与其他云上资源共用（如 CVM、CLB 等）。
- 与子网处于相同可用区的节点才支持创建 VPC-CNI 模式的 Pod，请提前规划 VPC-CNI 模式子网。
- 您需要指定单节点下 VPC-CNI 模式的 Pod 数量上限， 创建后不可修改。建议集群中节点配置相同。

## 前提条件

已登录 [容器服务控制台](https://console.qcloud.com/tke2)，并进入【[集群](https://console.qcloud.com/tke2/cluster?rid=1)】的管理页面。

## 操作步骤

### 开启 VPC-CNI
1. 选择需要查看的集群ID/名称，进入该集群的管理页面。并单击【基本信息】。
2. 在【VPC-CNI 模式】中单击<img src="https://main.qcloudimg.com/raw/5d18cae0914f64405b15a710d633fba3.png" style="margin-bottom: -5px;"></img>，弹出【编辑 VPC-CNI 模式】窗口。如下图所示：
 ![open][1]
  - 子网：选择可用区的子网。
 - Node 上最大 Pod 数量：确认使用数量。

### 关闭 VPC-CNI
 >!仅支持在集群内不存在任何 VPC-CNI 模式的 Pod 时关闭。
 >
1. 选择需要查看的集群ID/名称，进入该集群的管理页面。并单击【基本信息】。
2. 在【VPC-CNI 模式】中单击<img src="https://main.qcloudimg.com/raw/942a8819f581e4f43871baa2190b9776.png" style="margin-bottom: -5px;;"></img>，弹出【关闭 VPC-CNI 模式】窗口。如下图所示：
 ![close][2]
集群名称：输入集群名称进行确认并提交。
[1]: https://main.qcloudimg.com/raw/2fb53bed77df80d2859ea213cdaee7c6.png

[2]:https://main.qcloudimg.com/raw/25bf97e355533a5e8678567567c5aefd.png
