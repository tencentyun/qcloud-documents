## 操作场景

本文以调用 C++ SDK 为例介绍通过开源 SDK 实现消息收发的操作过程，帮助您更好地理解消息收发的完整过程。

## 前提条件

- [安装 GCC](https://gcc.gnu.org/install/)
- [下载 Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-rocketmq-demo/tdmq-rocketmq-cpp-sdk-demo.zip)

## 操作步骤

1. 准备环境。

   1. 需要在客户端环境安装 RocketMQ-Client-CPP库，根据官方文档进行安装即可 [安装CPP动态库](https://github.com/apache/rocketmq-client-cpp)，**推荐使用 master 分支构建**。
   2. 在项目中引入RocketMQ-Client-CPP相关头文件及动态库。

2. 初始化消息生产者。

   ```c++
   // 设置生产组名称
   DefaultMQProducer producer(groupName);
   // 设置服务接入地址
   producer.setNamesrvAddr(nameserver);
   // 设置用户权限
   producer.setSessionCredentials(
       accessKey,  // 角色密钥
       secretKey, // 角色名称
       "");
   // 设置命名空间(命名空间全称)
   producer.setNameSpace(nameserver);
   // 请确保参数设置完成在启动之前
   producer.start();
   ```

   | 参数       | 说明                                                         |
   | :--------- | :----------------------------------------------------------- |
   | groupName  | 生产者组名称，在控制台集群管理中`Group` tab中获取。          |
   | nameserver | 集群接入地址，在控制台**集群管理**页面操作列的**获取接入地址**获取。![](https://qcloudimg.tencent-cloud.cn/raw/45b3582e4d089041cae7030797bc447e.png) |
   | secretKey  | 角色名称，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制。 |
   | accessKey  | 角色密钥，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制**密钥**列复制。![img](https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png) |
   | namespace  | 命名空间全称在控制台集群管理中`Topic` 页签中页面复制，格式是**集群 ID +｜+命名空间**。![](https://qcloudimg.tencent-cloud.cn/raw/9251db01de6d447bbba7d3ca7f3591ef.png) |

3. 发送消息

   ```c++
   // 初始化消息内容
   MQMessage msg(
       topicName,  // topic名称
       TAGS,		// 消息tag
       KEYS,		// 消息业务key
       "Hello cpp client, this is a message."  // 消息内容
   );
   
   try {
       // 发送消息
       SendResult sendResult = producer.send(msg);
       std::cout << "SendResult:" << sendResult.getSendStatus() << ", Message ID: " << sendResult.getMsgId()
           << std::endl;
   } catch (MQException e) {
       std::cout << "ErrorCode: " << e.GetError() << " Exception:" << e.what() << std::endl;
   }
   ```

   | 参数      | 说明                                                         |
   | :-------- | :----------------------------------------------------------- |
   | topicName | Topic 名称在控制台集群管理中`Topic`页签中复制具体 Topic 名称。![](https://qcloudimg.tencent-cloud.cn/raw/f27fdecdf352468ef411cfdafc096d86.png) |
   | TAGS      | 用来设置消息的TAG。                                          |
   | KEYS      | 设置消息业务key。                                            |

4. 资源释放

   ```c++
   // 释放资源
   producer.shutdown();
   ```

5. 初始化消费者

   ```c++
   // 消息监听
   class ExampleMessageListener : public MessageListenerConcurrently {
   public:
       ConsumeStatus consumeMessage(const std::vector<MQMessageExt> &msgs) {
           for (auto item = msgs.begin(); item != msgs.end(); item++) {
               // 业务
               std::cout << "Received Message Topic:" << item->getTopic() << ", MsgId:" << item->getMsgId() << ", TAGS:"
                         << item->getTags() << ", KEYS:" << item->getKeys() << ", Body:" << item->getBody() << std::endl;
           }
           // 消费成功返回CONSUME_SUCCESS
           return CONSUME_SUCCESS;
           // 消费失败返回RECONSUME_LATER，该消息将会被重新消费
           // return RECONSUME_LATER;
       }
   };
   
   // 初始化消费者
   DefaultMQPushConsumer *consumer = new DefaultMQPushConsumer(groupName);
   // 设置服务地址
   consumer->setNamesrvAddr(nameserver);
   // 设置用户权限
   consumer->setSessionCredentials(
       accessKey,
       secretKey, 
       "");
   // 设置命名空间
   consumer->setNameSpace(namespace);
   // 设置实例名称
   consumer->setInstanceName("CppClient");
   
   // 请注册自定义侦听函数用来处理接收到的消息，并返回响应的处理结果。
   ExampleMessageListener *messageListener = new ExampleMessageListener();
   // 订阅消息
   consumer->subscribe(topicName, TAGS);
   // 设置消息监听
   consumer->registerMessageListener(messageListener);
   
   // 准备工作完成，必须调用启动函数，才可以正常工作。
   consumer->start();
   ```

   | 参数       | 说明                                                         |
   | :--------- | :----------------------------------------------------------- |
   | groupName  | 消费者组名称。在控制台集群管理中`Group` 页签中获取。         |
   | nameserver | 集群接入地址，在**集群管理**页面操作列的**获取接入地址**获取。![](https://qcloudimg.tencent-cloud.cn/raw/45b3582e4d089041cae7030797bc447e.png) |
   | secretKey  | 角色名称，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制。 |
   | accessKey  | 角色密钥，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制**密钥**列复制。![img](https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png) |
   | namespace  | 命名空间全称在控制台集群管理中`Topic` 页签中页面复制，格式是**集群 ID +｜+命名空间**。![](https://qcloudimg.tencent-cloud.cn/raw/9251db01de6d447bbba7d3ca7f3591ef.png) |
   | topicName  | Topic 名称在控制台集群管理中`Topic`页签中复制具体 Topic 名称。![](https://qcloudimg.tencent-cloud.cn/raw/f27fdecdf352468ef411cfdafc096d86.png) |
   | TAGS       | 用来设置订阅消息的TAG。                                      |

6. 资源释放。

   ```c++
   // 资源释放
   consumer->shutdown();
   ```

7. 查看消费详情。登录 [TDMQ 控制台](https://console.cloud.tencent.com/tdmq)，在**集群管理** > **Group** 页面，可查看与 Group 连接的客户端列表，单击操作列的**查看详情**，可查看消费者详情。
   ![img](https://main.qcloudimg.com/raw/7187da67219534d767206553e2a383ab.png)





上述是对消息的发布和订阅方式的简单介绍。更多操作可参考 [Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-rocketmq-demo/tdmq-rocketmq-cpp-sdk-demo.zip) 或 [RocketMQ-Client-CPP示例](https://github.com/apache/rocketmq-client-cpp/tree/master/example) 。
