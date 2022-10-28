
## 使用场景

Kubernetes 使用事件（Event）反馈集群中资源对象的状态，它通常表示系统中的一些状态变化。例如在安装或修改工作负载时，您可以通过事件信息判断当前资源对象是否存在异常，以及查看导致异常的原因。事件的保留时间有限，在 TKE 集群中事件可保留1小时。

如果事件信息包含异常，则需要集群管理员及时关注。TKE 支持为您的所有集群配置事件持久化功能，开启该功能后，TKE 会将您的集群事件实时导出至配置的存储端。更多请参考 [事件存储](https://cloud.tencent.com/document/product/457/32091)。

Service/Ingress 作为 Kubernetes 中接入层的资源对象，其质量事关业务服务稳定性，因此，对 Service/Ingress 异常事件的监控告警成为了常见诉求。为此，TKE 也定义了常见了 Service/Ingress 异常事件错误码信息、异常原因和解决办法，更多请参考 [Service&Ingress 常见报错和处理](https://cloud.tencent.com/document/product/457/81004)。本文提供集群里 Service/Ingress 异常事件的告警实践。


[](id:step1)
## 步骤1：打开集群的事件采集
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在集群管理页，单击集群 ID，进入集群信息页。
3. 在集群详情页，为集群开启事件采集。操作详情见 [开启事件存储](https://cloud.tencent.com/document/product/457/32091)。
>! 若您在同一个地域有多个 Kubernetes 集群，建议您可以打开多个集群的事件存储功能，并选择相同的日志主题和日志集。

[](id:step2)
## 步骤2：确定事件是否采集
1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls/overview)，进入**检索分析**页。
2. 在“检索分析”页，选择地域、已开启事件采集的集群日志集、日志主题。	
3. 在“原始数据”中，查找字段`event.message`，该字段为集群中资源对象产生的事件信息。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/ff9b9da5f168361f18f077d6ce03e598.png)  

## 步骤3：新建告警策略

以告警 Ingress 的事件为例，Service 类似。


1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls/overview)。选择**监控告警 > 告警策略**。
2. 在“告警策略”页，单击**新建**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/cd57e8ac185f823166c2a32dda48e3c1.png)
3. 在“新建告警策略”页，参考以下主要信息进行设置：
	- **日志主题**：选择您在 [步骤1](#step1) 中创建的主题。
	- **执行语句**：添加执行语句`(event.message:"Ingress Sync ClientError." OR event.message:"Ingress Sync DependencyError." OR event.message:"IngressError. ErrorCode:") | SELECT count(*) as ErrCount`。
>? 表示获取所有的 Ingress 的事件信息
>
	- **触发条件**：添加触发条件`$1.ErrCount > 0`。
>? 表示一有时间信息就触发告警。
>
	- **多维分析**：选择**自定义检索分析**。
     - **名称**：您可以自定义名称。
     - **检索分析语句**：添加检索分析语句`(event.message:"Ingress Sync ClientError." OR event.message:"Ingress Sync DependencyError." OR event.message:"IngressError. ErrorCode:") | SELECT clusterId, event.involvedObject.namespace, event.involvedObject.name, split(split(event.message, 'ErrorCode: ')[2], ' ')[1] as ErrorCode, count(*) as ErrCount group by (clusterId, event.involvedObject.namespace, event.involvedObject.name, ErrorCode)`。
	- **通知内容**：添加通知内容“Ingress 使用告警，以下集群资源同步出现异常：”

完整参数配置方式请参考 [配置告警策略](https://cloud.tencent.com/document/product/614/51742)。

## 步骤4：查看告警

确保 [步骤2](#step2) 中有新的事件产生，且 [步骤2](#step2) 中告警策略的执行周期、告警通知频率合适（例如测试时可以设置为1分钟一次），就可以查看告警通知渠道中的告警内容了。本文示例设置为通过邮件进行告警，因此可参考邮件的告警内容，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/a966f365ed18cfc8438e511fc32c5fbd.png)
