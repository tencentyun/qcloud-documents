## 操作场景

本文以调用 C++ SDK 为例介绍通过开源 SDK 实现消息收发的操作过程，帮助您更好地理解消息收发的完整过程。

## 前提条件

- [完成资源创建与准备](https://cloud.tencent.com/document/product/1179/44814)
- [安装 GCC](https://gcc.gnu.org/install/)
- [下载 Demo](https://tdmq-document-1306598660.cos.ap-nanjing.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91demo/pulsar/tcp/tdmq-pulsar-cpp-sdk-demo.zip)

## 操作步骤

1. 准备环境。
   1. 在客户端环境安装 Pulsar C++ client，安装过程可参考官方教程 [Pulsar C++ client](https://pulsar.apache.org/docs/en/client-libraries-cpp/)。
   2. 在项目中引入 Pulsar C++ client 相关头文件及动态库。
2. 创建客户端。
<dx-codeblock>
:::  c++
   // 客户端配置信息
   ClientConfiguration config;
   // 设置授权角色密钥
   AuthenticationPtr auth = pulsar::AuthToken::createWithToken(AUTHENTICATION);
   config.setAuth(auth);
   // 创建客户端
   Client client(SERVICE_URL, config);
:::
</dx-codeblock>
<table>
    <thead>
    <tr>
        <th style='text-align:left;'>参数</th>
        <th style='text-align:left;'>说明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td style='text-align:left;'>SERVICE_URL</td>
        <td style='text-align:left;'>集群接入地址，可以在控制台 <a
                href='https://console.cloud.tencent.com/tdmq/cluster'><strong>集群管理</strong></a> 页面查看并复制。<br><img
                src="https://qcloudimg.tencent-cloud.cn/raw/1221f6b1be8ad150a6544a3f9394a8eb.png"
                referrerpolicy="no-referrer" alt="img"></td>
    </tr>
    <tr>
        <td style='text-align:left;'>AUTHENTICATION</td>
        <td style='text-align:left;'>角色密钥，在 <strong><a
                href='https://console.cloud.tencent.com/tdmq/role'>角色管理</a></strong> 页面复制<strong>密钥</strong>列复制。<img
                src="https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png" referrerpolicy="no-referrer"
                alt="img"></td>
    </tr>
    </tbody>
</table>
3. 创建生产者。
<dx-codeblock>
:::  c++
// 生产者配置
ProducerConfiguration producerConf;
producerConf.setBlockIfQueueFull(true);
producerConf.setSendTimeout(5000);
// 生产者
Producer producer;
// 创建生产者
Result result = client.createProducer(
    // topic完整路径，格式为persistent://集群（租户）ID/命名空间/Topic名称
    "persistent://pulsar-xxx/sdk_cpp/topic1",
    producerConf,
    producer);
if (result != ResultOk) {
    std::cout << "Error creating producer: " << result << std::endl;
    return -1;
}
:::
</dx-codeblock>
<dx-alert infotype="explain" title="">
Topic 名称需要填入完整路径，即 `persistent://clusterid/namespace/Topic`，`clusterid/namespace/topic` 的部分可以从控制台上 **[Topic管理](https://console.cloud.tencent.com/tdmq/topic)** 页面直接复制。
</dx-alert>
4. 发送消息。
<dx-codeblock>
:::  c++
   // 消息内容
   std::string content = "hello cpp client, this is a msg";
   // 构建消息对象
   Message msg = MessageBuilder().setContent(content)
       .setPartitionKey("mykey")  // 业务key
       .setProperty("x", "1")   // 设置消息参数
       .build();
   // 发送消息
   Result result = producer.send(msg);
   if (result != ResultOk) {
       // 发送失败
       std::cout << "The message " << content << " could not be sent, received code: " << result << std::endl;
   } else {
       // 发送成功
       std::cout << "The message " << content << " sent successfully" << std::endl;
   }
:::
</dx-codeblock>
5. 创建消费者。
<dx-codeblock>
:::  c++
   // 消费者配置信息
   ConsumerConfiguration consumerConfiguration;
   consumerConfiguration.setSubscriptionInitialPosition(pulsar::InitialPositionEarliest);
   // 消费者
   Consumer consumer;
   // 订阅topic
   Result result = client.subscribe(
       // topic完整路径，格式为persistent://集群（租户）ID/命名空间/Topic名称
       "persistent://pulsar-xxx/sdk_cpp/topic1",
       // 订阅名称
       "sub_topic1",
       consumerConfiguration,
       consumer);
   
   if (result != ResultOk) {
       std::cout << "Failed to subscribe: " << result << std::endl;
       return -1;
   }
:::
</dx-codeblock>
> ?
>
> - Topic 名称需要填入完整路径，即 `persistent://clusterid/namespace/Topic`，`clusterid/namespace/topic` 的部分可以从控制台上 **[Topic管理](https://console.cloud.tencent.com/tdmq/topic)** 页面直接复制。
>   ![img](https://qcloudimg.tencent-cloud.cn/raw/dc1bc50c434546755565c6dcb8d3e7f0.png)
> - subscriptionName 需要写入订阅名，可在**消费管理**界面查看。
6. 消费消息。
<dx-codeblock>
:::  c++
   Message msg;
   // 获取消息
   consumer.receive(msg);
   // 模拟业务
   std::cout << "Received: " << msg << "  with payload '" << msg.getDataAsString() << "'" << std::endl;
   // 回复ack
   consumer.acknowledge(msg);
   // 消费失败回复nack, 消息将会重新投递
   // consumer.negativeAcknowledge(msg);
:::
</dx-codeblock>
7. 登录 [TDMQ Pulsar 版控制台](https://console.cloud.tencent.com/tdmq)，依次点击 **Topic 管理** > **Topic 名称**进入消费管理页面，点开订阅名下方右三角号，可查看生产消费记录。
   ![img](https://main.qcloudimg.com/raw/3bee532dab55b7cab1167416aac95f4d.png)

>?上述是对消息的发布和订阅方式的简单介绍。更多操作可参见 [Demo](https://tdmq-document-1306598660.cos.ap-nanjing.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91demo/pulsar/tcp/tdmq-pulsar-cpp-sdk-demo.zip) 或 [Pulsar 官方文档](https://pulsar.apache.org/docs/en/client-libraries-cpp/)。
