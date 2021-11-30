## 操作场景


您可以通过配置 TDMQ 连接器来消费 TDMQ 消息队列的内容。TDMQ 连接器实现方式为 **Pull 模型**，事件连接器会主动拉取 TDMQ 内容，并将相关事件通过事件规则路由到更多服务。本文为您介绍如何创建 TDMQ 连接器和介绍 TDMQ 连接器数据结构。


## 前提条件

已 [创建事件集](https://cloud.tencent.com/document/product/1359/56080)。



## 操作步骤


1. 登录 [事件总线控制台](https://console.cloud.tencent.com/eb/)，选择左侧导航栏中的**事件集**。
2. 在“事件集”列表，选择期望配置 TDMQ 连接器的事件集。
3. 在“事件集详情”页事件连接器配置项中单击**添加**，如下图所示：
![](https://main.qcloudimg.com/raw/becfdcc055c2eb05638e662454f9d2cb.jpg)
4. 根据页面提示填写相关信息，如下图所示：
	![](https://main.qcloudimg.com/raw/ab46965a9f2ed3f7d977e37fa0d80acd.jpg)
  其中**连接器类型**选择**消息队列（TDMQ）**连接器，其余配置项按照提示填写。
5. 单击**确定**完成创建。
6. 选择左侧导航栏中的**事件规则**。
7. 在“事件规则”顶部选框，选择与之前创建一致的事件集信息，并单击**新建事件规则**，如下图所示：
  ![](https://main.qcloudimg.com/raw/722e3a30a77d81c606a929d20191e349.jpg)
8. 根据页面提示填写相关信息，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/0894ccd23860b71196fb868282e8c9c7.png)
   其中**云服务类型**选择**消息队列（TDMQ）**，并配置触发目标端。
9. 单击**确定**即可创建 TDMQ 连接器。

     


#### TDMQ 连接器的数据结构说明

```json
{
   {
    "specversion": "0",
    "id": "13a3f42d-7258-4ada-da6d-023a333b4662",
    "type": "connector:tdmq",
    "source": "tdmq.cloud.tencent",
    "subjuect": "qcs::tdmq:$region:$account:topicName/$topicSets.clusterId/$topicSets.environmentId/$topicSets.topicName/$topicSets.subscriptionName",
    "time": "1615430559146",
    "region": "ap-guangzhou",
    "datacontenttype": "application/json;charset=utf-8",
    "data": {
					"topic":  "persistent://appid/namespace/topic-1",
            "tags": "testtopic",
					"TopicType": "0",
					"subscriptionName": "xxxxxx",
					"toTimestamp": "1603352765001",
            "partitions": "0",
					"msgId": "123345346",
					"msgBody": "Hello from TDMQ!"
    }
}
```

参数说明如下：

| 参数             | 描述                                                         |
| ---------------- | ------------------------------------------------------------ |
| topic            | Topic 完整路径 `persistent://appid/namespace/topic-1`。      |
| tags             | TDMQ 标签。                                                  |
| topictype        | topic 类型描述：<br><li>0：普通消息。<br><li>1：全局顺序消息。<br><li>2：局部顺序消息。<br><li>3：重试队列。<br><li>4：死信队列。 |
| subscriptionName | 订阅名称。                                                   |
| timestamp        | 时间戳，精确到毫秒。                                         |
|partitions|TMDQ 队列消费的 partition。|
| msgId            | TDMQ 消息 ID。                                               |
| msgBody          | TDMQ 消息体。                                                |









