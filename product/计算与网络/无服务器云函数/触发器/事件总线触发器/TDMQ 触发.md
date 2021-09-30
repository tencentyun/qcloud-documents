



通过 [EventBridge 事件总线](https://cloud.tencent.com/document/product/1359/56077)，用户可以编写云函数来处理 TDMQ 消息队列中收取到的消息。云函数后台模块可以作为消费者消费 TDMQ 中的消息，并将消息传递给云函数，本篇文档将为您指导，云函数如何通过 EventBridge 事件总线触发器，接收并消费来自 TDMQ 的产品事件。

## 创建步骤

### 步骤1：创建函数
登录 [Serverless控制台](https://console.cloud.tencent.com/scf/list-create?rid=1&ns=default)，在新建函数页面，完成您的函数代码上传与部署。详情可参见 [使用控制台创建一个事件函数](https://cloud.tencent.com/document/product/583/37509)。

>! 目前 TDMQ 只支持北京、上海、广州地域。



此处以 helloworld 模版为例，创建空函数项目：
![](https://main.qcloudimg.com/raw/6332a17c6782b4774801ebefa4348b49.png)

### 步骤2：配置触发器
选择**TDMQ 触发**后，按照指引，依次选择您的 TDMQ 集群、主题等信息，指定触发事件源，消费位置：
![](https://main.qcloudimg.com/raw/73295485d347e1a169c04378f62b0f47.png)

### 步骤3：管理触发器
创建完成后，在“触发器管理”页面可以看到创建的触发器信息，点击进入事件总线控制台，即可完成事件集、事件源等信息管理，详情请参考 [事件总线产品文档](https://cloud.tencent.com/document/product/1359/56077)。
![](https://main.qcloudimg.com/raw/067b4b46ad9cfee9bfe43d839506398a.png)

给指定 TDMQ 消息队列发送信息，即可看到函数被正常调用：
![](https://main.qcloudimg.com/raw/d63a450acc3931ef2d35125b882e3e9c.png)

## 事件结构
<dx-codeblock>
:::  json
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
					"TopicType": 0,
					"subscriptionName": "xxxxxx",
					"toTimestamp": "1603352765001",
            "partitions": "0",
					"msgId": "123345346",
					"msgBody": "Hello from TDMQ!"
    }
}
:::
</dx-codeblock>


参数说明如下：

| 参数             | 描述                                                         |
| ---------------- | ------------------------------------------------------------ |
| topic            | Topic 完整路径 `persistent://appid/namespace/topic-1`。      |
| subscriptionName | 订阅名称。                                                   |
| timestamp        | 时间戳，精确到毫秒。                                         |
| tags             | TDMQ 标签。                                                  |
| msgId            | TDMQ 消息 ID。                                               |
| msgBody          | TDMQ 消息体。                                                |
| topictype        | topic 类型描述：<br><li>0：普通消息。<br><li>1：全局顺序消息。<br><li>2：局部顺序消息。<br><li>3：重试队列。<br><li>4：死信队列。 |
