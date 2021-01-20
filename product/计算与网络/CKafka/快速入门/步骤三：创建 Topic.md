## 操作场景

该任务指导您通过 CKafka 控制台，在已有实例下创建 Topic。

Topic（主题）是某一种分类的名字，消息在 Topic 中可以被存储和发布。生产者往 Topic 中写消息，消费者从 Topic 中读消息。

一个 Topic 实际是由多个 [Partition（分区）](https://cloud.tencent.com/document/product/597/32544#F)组成，遇到瓶颈时，可以通过增加 Partition 的数量进行横向扩容。

## 前提条件

已完成 [创建实例](https://cloud.tencent.com/document/product/597/30931)。

## 操作步骤

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 。
2. 在左侧导航树点击【实例列表】，单击目标实例的“ID/名称”，进入实例详情页。
3. 在实例详情页，单击页面顶部的【Topic 管理】，点击【新建】。
4. 在编辑 Topic 窗口中，选择分区数和副本数等信息。

- 名称：Topic 名称，输入后无法更改，名称只能包含字母、数字、下划线、“-”和“.”。
- 分区数：一个物理上分区的概念，一个 Topic 可以包含一个或者多个 partition，CKafka 以 partition 作为分配单位。
- 副本数：partition 的副本个数，用于保障 partition 的高可用，为保障数据可靠性，当前不支持创建单副本 Topic，默认开启2副本。
- 白名单： 开启白名单后，只有白名单中的 IP 才可访问该 Topic，有效保证数据安全（在新建 Topic 和编辑 Topic 页面均可以开启白名单）。

5. 单击【提交】完成 Topic 创建。

> ?副本数也算分区个数，例如客户创建了1个 Topic、6个分区、2个副本，那么分区额度一共用了1 * 6 * 2 = 12个。 如果超过了购买的最大分区个数，单击【提交】时会有如下提示：  
>
> [![img](https://camo.githubusercontent.com/db9afe4687450032ac197e6498a7c7a3244f5321e6cad513720f420894aea5be/68747470733a2f2f6d61696e2e71636c6f7564696d672e636f6d2f7261772f65656233623961613136656637623561653633373064353661666665643836352e706e67)](https://camo.githubusercontent.com/db9afe4687450032ac197e6498a7c7a3244f5321e6cad513720f420894aea5be/68747470733a2f2f6d61696e2e71636c6f7564696d672e636f6d2f7261772f65656233623961613136656637623561653633373064353661666665643836352e706e67)

