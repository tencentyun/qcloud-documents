## 操作场景


您可以通过配置 Ckafka 连接器来消费 Ckafka 消息队列的内容。Ckafka 连接器实现方式为 **Pull 模型**，事件连接器会主动拉取 Ckafka 内容，并将相关事件通过事件规则路由到更多服务。本文为您介绍如何创建 Ckafka 连接器和介绍 Ckafka 连接器数据结构。


## 前提条件

已 [创建事件集](https://cloud.tencent.com/document/product/1359/56080)。



## 操作步骤


1. 登录 [事件总线控制台](https://console.cloud.tencent.com/eb/)，选择左侧导航栏中的**事件集**。
2. 在“事件集”列表，选择期望配置 Ckafka 连接器的事件集。
3. 在“事件集详情”页事件连接器配置项中单击**添加**，如下图所示：
![](https://main.qcloudimg.com/raw/becfdcc055c2eb05638e662454f9d2cb.jpg)
4. 根据页面提示填写相关信息，如下图所示：
![](https://main.qcloudimg.com/raw/78a2510dc65b8dbf435e18a9dad9bf2d.png)
  其中**连接器类型**选择**消息队列（Kafka）**连接器，其余配置项按照提示填写。
<dx-alert infotype="notice" title="">
目前只支持云上 Ckafka 实例投递，请确认您的 Ckafka 实例没有配置用户名密码等信息，否则连接器可能无法成功获取消息。
</dx-alert>
5. 单击**确定**完成创建。
6. 选择左侧导航栏中的**事件规则**。
7. 在“事件规则”顶部选框，选择与之前创建一致的事件集信息，并单击**新建事件规则**，如下图所示：
  ![](https://main.qcloudimg.com/raw/722e3a30a77d81c606a929d20191e349.jpg)
8. 根据页面提示填写相关信息，如下图所示：
![](https://main.qcloudimg.com/raw/b7f78b1c1862305f1075b3569d1376fc.png)
   其中**云服务类型**选择**消息队列（Kafka）**，并配置触发目标端。
9. 单击**确定**即可创建 Ckafka 连接器。

     


#### Ckafka 连接器的数据结构说明

```json
 {       
        "specversion":"0",       
        "id":"13a3f42d-7258-4ada-da6d-023a333b4662",    
        "type":"connector:kafka",   
        "source":"ckafka.cloud.tencent",   
        "subjuect": "qcs::ckafka:ap-guangzhou:uin/1250000000:ckafkaId/uin/1250000000/ckafka-123456",     
        "time":"1615430559146",   
        "region":"ap-guangzhou",       
        "datacontenttype":"application/json;charset=utf-8",   
        "data":{             
             "topic":"test-topic",         
             "Partition":1,         
             "offset":37,         
             "msgKey":"test",         
             "msgBody":"Hello from Ckafka again!"      
           }
}
```

参数说明如下：

| 参数             | 描述                                                         |
| ---------------- | ------------------------------------------------------------ |
| topic            | Ckafka 投递 Topic。     |
| Partition | 事件源所在分区，一个 Topic 可以包含一个或者多个 Partition，CKafka 以 Partition 作为分配单位。                                                   |
| offset        | 消费分组，指定消费区域。                                      |
| msgKey            | Ckafka 消息 Key。                                               |
| msgBody          | Ckafka 消息体。                                                |









