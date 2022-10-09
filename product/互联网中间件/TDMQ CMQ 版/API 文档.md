TDMQ CMQ 版资源管控相关接口如下表所示。

>? 以下 API 仅适用于对队列和主题的管理类操作，例如新增、查询、修改、删除等，如需查看和收发消息相关的 API 请参见[HTTP 数据流 SDK](https://cloud.tencent.com/document/product/1496/61039)。


<style>
table th:nth-of-type(1) {
width: 300px;        
}
</style>


## 管理相关接口

| 接口名称                                                     | 接口功能              |
| :----------------------------------------------------------- | :-------------------- |
| [CreateCmqQueue](https://cloud.tencent.com/document/api/1179/55917) | 创建 TDMQ CMQ 版队列接口       |
| [CreateCmqSubscribe](https://cloud.tencent.com/document/api/1179/55916) | 创建 TDMQ CMQ 版订阅接口       |
| [CreateCmqTopic](https://cloud.tencent.com/document/api/1179/55915) | 创建 TDMQ CMQ 版主题           |
| [DeleteCmqQueue](https://cloud.tencent.com/document/api/1179/55914) | 删除 TDMQ CMQ 版队列           |
| [DeleteCmqSubscribe](https://cloud.tencent.com/document/api/1179/55913) | 删除 TDMQ CMQ 版订阅           |
| [DeleteCmqTopic](https://cloud.tencent.com/document/api/1179/55912) | 删除 TDMQ CMQ 版主题           |
| [DescribeCmqDeadLetterSourceQueues](https://cloud.tencent.com/document/api/1179/55911) | 枚举 TDMQ CMQ 版死信队列源队列 |
| [DescribeCmqQueueDetail](https://cloud.tencent.com/document/api/1179/55910) | 查询 TDMQ CMQ 版队列详情       |
| [DescribeCmqQueues](https://cloud.tencent.com/document/api/1179/55909) | 查询 TDMQ CMQ 版全量队列       |
| [DescribeCmqSubscriptionDetail](https://cloud.tencent.com/document/api/1179/55908) | 查询 TDMQ CMQ 版订阅详情       |
| [DescribeCmqTopicDetail](https://cloud.tencent.com/document/api/1179/55907) | 查询 TDMQ CMQ 版主题详情       |
| [DescribeCmqTopics](https://cloud.tencent.com/document/api/1179/55906) | 枚举 TDMQ CMQ 版全量主题       |
| [ModifyCmqQueueAttribute](https://cloud.tencent.com/document/api/1179/55905) | 修改 TDMQ CMQ 版队列属性       |
| [ModifyCmqSubscriptionAttribute](https://cloud.tencent.com/document/api/1179/55904) | 修改 TDMQ CMQ 版订阅属性       |
| [ModifyCmqTopicAttribute](https://cloud.tencent.com/document/api/1179/55903) | 修改 TDMQ CMQ 版主题属性       |
| [RewindCmqQueue](https://cloud.tencent.com/document/api/1179/55902) | 回溯 TDMQ CMQ 版队列           |
| [UnbindCmqDeadLetter](https://cloud.tencent.com/document/api/1179/55901) | 解绑 TDMQ CMQ 版死信队列       |
