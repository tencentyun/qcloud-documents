欢迎使用消息队列 CKafka。

消息队列 CKafka 运行在腾讯数据中心，它提供了可以弹性伸缩的消息队列服务。

消息队列 CKafka 向用户提供弹性的存储和网络资源。用户可以使用本文档介绍的 API，并参照相应的示例，对消息队列 CKafka 进行相关操作：如创建、销毁、升配等；支持的全部操作可参见 [API 概览](https://cloud.tencent.com/document/api/597/10076)。

请确保在使用这些接口前，已充分了解了 [消息队列 CKafka 概述](https://cloud.tencent.com/document/product/597/10066)。

## 术语表
本文档涉及的一些常用术语如下：

| 术语 | 全称  | 中文 | 说明 |
|---------|---------|---------|---------|
| Instance | Instance |服务器实例 | 指代一台消息队列服务器。这里的一台消息队列服务器是逻辑上的概念，物理上是由多台物理机提供服务。|
| Region | Region |[地域](https://cloud.tencent.com/doc/product/213/6091) | 表示资源所在的地域，每个地域包含一个或多个可用区。|
| Zone | Zone | [可用区](https://cloud.tencent.com/doc/product/213/6091) | 指腾讯云在同一 [地域](https://cloud.tencent.com/doc/product/213/6091) 内电力和网络互相独立的物理数据中心。目标是能够保证可用区之间故障相互隔离，不出现故障扩散，使得用户的业务持续在线服务。 |
|包年包月 | 包年包月 | 包年包月 |	一种计费模式，参看 [计费模式说明](https://cloud.tencent.com/doc/product/213/2180#1.-.E5.8C.85.E5.B9.B4.E5.8C.85.E6.9C.88)。|
|包年包月| 包年包月| 按量计费 |	一种计费模式，参看 [计费模式说明](https://cloud.tencent.com/doc/product/213/2180#2.-.E6.8C.89.E9.87.8F.E8.AE.A1.E8.B4.B9)。|

#### 输入参数与返回参数释义
* Limit 和 Offset
用来控制分页的参数；Limit 为单次返回的最多条目数量，Offset 为偏移量。当相应结果是列表形式时，如果数量超过了 Limit 所限定的值，那么只返回 Limit 个值。
例如，参数 Offset=0&Limit=20返回第0到19项，Offset=20&Limit=20返回第20到39项，Offset=40&Limit=20返回第40到59项，以此类推。
	
* topic.N
同时输入多个参数的格式。当遇到形如这样的格式时，那么该输入参数可以同时传多个，即该参数为数组参数，数组参数入参如下所示：
topic.0=test1&topic.1=test2&topic.2=test3，以此类推（以下标0开始）。


## API 快速入门
这里针对几个典型的使用场景对消息队列 CKafka  API 的使用方式进行说明：
- 通过使用 [创建主题](https://cloud.tencent.com/document/product/597/10096) API，提供实例 ID、主题名称、分区个数，副本个数等一些必要的信息，即可立刻创建出一个 Topic。
- 如需修改主题配置，可以使用 [修改主题属性接口](https://cloud.tencent.com/document/product/597/10098) API 调整主题的配置。

## 使用限制 
* 消息队列 CKafka  API 调用配额为：100次/分钟，且单一 API 不超过100次/分钟。
* 更具体的限制请参考对应 API 接口文档或产品文档。
