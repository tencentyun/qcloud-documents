## 操作场景

在离线数据处理等场景下，有时需要对 offset 进行重置，用于消费前一时间段的消息。

## 操作步骤

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 。
2. 在左侧导航栏单击【实例列表】，单击目标实例的“ID/名称”，进入实例详情页。
3. 在实例详情页，点击【Consumer Group】标签页，单击操作列的【offset 设置】。
4. 在 offset 设置窗口，选择以 Topic 或者 Partition 为维度进行设置，单击【下一步】。
5. 选择需要重置 offset 的 Topic 信息（不选则默认全部 Topic 的 offset 均重置）或者 Partition 信息，单击【下一步】。
6. 对 offset 进行指定。
   ![](https://main.qcloudimg.com/raw/dae2ecebbdbf07712be90f3882df892d.png)

>!
>- offset 设置范围要在最小 offset 和最大 offset 之间。在配置时，如果小于最小 offset 会从最小 offset 进行消费，如果大于最大 offset 会从最大 offset 进行消费。
>- 重置消费分组时，需保证没有消费者在消费分组内才能进行重置，否则不能进行重置。
