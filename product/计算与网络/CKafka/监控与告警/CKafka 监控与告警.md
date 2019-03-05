腾讯云默认为所有用户提供云监控功能，无需用户手动开通。用户必须在使用了腾讯云某个产品后，云监控才可以开始收集监控数据。

## 获取监控数据
### 获取方式
CKafka 控制台提供改了单独的监控数据读取选项卡。
CKafka 控制台提供两种维度的数据监控：实例维度和 Topic 维度。您可以通过控制台查看 CKafka 实例和 Topic 的生产流量、消费流量、消息堆积量等监控数据，并可任意调整查看的时间段。查看方法如下：

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka)  。
2. 在实例列表中，单击需要要查看的实例 ID/Topic ID，进入实例详情页。
3. 在实例详情页顶部，单击【本实例监控】选项卡，可查看监控数据。

### CKafka 监控指标说明
详情参见文档 [CKafka 监控指标](https://cloud.tencent.com/document/product/248/12154)。

### CKafka 监控 API 文档
CKafka 监控 API 详情可参见如下文档：
- [主题监控](https://cloud.tencent.com/document/product/248/17296)
- [实例监控](https://cloud.tencent.com/document/product/248/17297) 
- [消费分组监控](https://cloud.tencent.com/document/product/248/17298)

## CKafka 告警策略
### 创建告警
在 CKafka 状态改变时，可以创建告警来及时通知您采取措施。创建的告警会将一定周期内监控的指标与给定阈值的情况进行比对，从而判断是否需要触发相关通知。
状态改变而导致告警触发后，您可以及时进行相应的预防或补救措施。合理地创建告警能帮助您提高应用程序的健壮性和可靠性。有关告警的更多信息，请参考 [云监控创建告警](https://cloud.tencent.com/document/product/248/1073) 。
