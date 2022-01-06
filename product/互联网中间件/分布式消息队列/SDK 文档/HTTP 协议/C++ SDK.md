## 操作场景

本文以  C++ 语言为例介绍通过 HTTP 协议接入 TDMQ Pulsar 版并收发消息的操作方法。

## 前提条件

- [完成资源创建与准备](https://cloud.tencent.com/document/product/1179/44814)
- [安装 GCC](https://gcc.gnu.org/install/)
- [下载 Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-pulsar-demo/http/tdmq-pulsar-cpp-http-demo.zip)



## 操作步骤

1. 准备环境。
 1. 依赖及编译安装参考 [C++ SDK 编译安装](https://cloud.tencent.com/document/sdk/C++)。
 2. 项目如引入相关头文件及依赖库。
2. 创建 TDMQ 客户端。
<dx-codeblock>
:::  c++
   // 认证信息
   Credential cred = Credential(SECRET_ID, SECRET_KEY);
   
   HttpProfile httpProfile = HttpProfile();
   httpProfile.SetEndpoint(ENDPOINT);
   
   ClientProfile clientProfile = ClientProfile();
   clientProfile.SetHttpProfile(httpProfile);
   // 创建tdmq客户端
   TdmqClient client = TdmqClient(cred, REGION, clientProfile);
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
        <td style='text-align:left;'>SECRET_ID、SECRET_KEY</td>
        <td style='text-align:left;'><img src="https://main.qcloudimg.com/raw/8ec140474be0ced1352695b372b2934d.png"
                                          referrerpolicy="no-referrer" alt="img"></td>
    </tr>
    <tr>
        <td style='text-align:left;'>ENDPOINT</td>
        <td style='text-align:left;'>接口请求域名： tdmq.tencentcloudapi.com。</td>
    </tr>
    <tr>
        <td style='text-align:left;'>REGION</td>
        <td style='text-align:left;'>集群所属地域，详见产品支持的 <a
                href='https://cloud.tencent.com/document/api/1179/46067#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8'>地域列表</a>。
        </td>
    </tr>
    </tbody>
</table>
3. 发送消息。
<dx-codeblock>
:::  c++
   SendMessagesRequest req = SendMessagesRequest();
   // 设置已授权角色密钥
   req.SetStringToken(token);
   // 设置已授权角色名称
   req.SetProducerName(userName);
   // 设置topic名称, 格式为: 集群（租户）ID/命名空间/Topic名称
   req.SetTopic(topicName);
   // 消息内容
   req.SetPayload("this is a new message.");
   // 设置发送消息超时时间
   req.SetSendTimeout(3000);
   // 发送消息
   auto outcome = client.SendMessages(req);
   if (!outcome.IsSuccess()) {
       cout << outcome.GetError().PrintAll() << endl;
       return -1;
   }
   // 获取结果
   SendMessagesResponse resp = outcome.GetResult();
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
        <td style='text-align:left;'>token</td>
        <td style='text-align:left;'>角色密钥，在 <strong><a
                href='https://console.cloud.tencent.com/tdmq/role'>角色管理</a></strong> 页面复制<strong>密钥</strong>列复制。<img
                src="https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png" referrerpolicy="no-referrer"
                alt="img"></td>
    </tr>
    <tr>
        <td style='text-align:left;'>userName</td>
        <td style='text-align:left;'>角色名称，在 <strong><a
                href='https://console.cloud.tencent.com/tdmq/role'>角色管理</a></strong> 页面复制<strong>名称</strong>列复制。
        </td>
    </tr>
    <tr>
        <td style='text-align:left;'>topicName</td>
        <td style='text-align:left;'>Topic 名称，格式为：集群（租户）ID/命名空间/Topic名称，示例：pulsar-xxx/sdk_http/topic1。可以从控制台上
            <strong><a href='https://console.cloud.tencent.com/tdmq/topic'>Topic 管理</a></strong> 页面直接复制。
        </td>
    </tr>
    </tbody>
</table>
4. 消费消息。
<dx-codeblock>
:::  c++
   ReceiveMessageRequest req = ReceiveMessageRequest();
   // 设置topic名称, 格式为：集群（租户）ID/命名空间/Topic名称
   req.SetTopic(topicName);
   // 设置订阅名称
   req.SetSubscriptionName(subName);
   // consumer接收的消息会首先存储到receiverQueueSize这个队列中，用作调优接收消息的速率
   req.SetReceiverQueueSize(10);
   // 设置consumer初始接收消息的位置，可选参数为：Earliest, Latest
   req.SetSubInitialPosition("Latest");
   
   // 接收消息
   auto outcome = client.ReceiveMessage(req);
   if (!outcome.IsSuccess()) {
       cout << outcome.GetError().PrintAll() << endl;
       return -1;
   }
   // 获取结果
   ReceiveMessageResponse resp = outcome.GetResult();
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
        <td style='text-align:left;'>topicName</td>
        <td style='text-align:left;'>Topic 名称，格式为：集群（租户）ID/命名空间/Topic名称，示例：pulsar-xxx/sdk_http/topic1。可以从控制台上
            <strong><a href='https://console.cloud.tencent.com/tdmq/topic'>Topic 管理</a></strong> 页面直接复制。
        </td>
    </tr>
    <tr>
        <td style='text-align:left;'>subName</td>
        <td style='text-align:left;'>订阅名称，可在控制台<strong>集群管理 </strong>&gt; <strong>消费者</strong>tab页面复制。</td>
    </tr>
    </tbody>
</table>
5. 确认消息。
<dx-codeblock>
:::  c++
   AcknowledgeMessageRequest req = AcknowledgeMessageRequest();
   // 确认消息的id
   req.SetMessageId(messageId);
   // 设置topic名称, 格式为：集群（租户）ID/命名空间/Topic名称
   req.SetAckTopic(topicName);
   // 设置订阅信息
   req.SetSubName(subName);
   // 确认消息
   auto outcome = client.AcknowledgeMessage(req);
   if (!outcome.IsSuccess()) {
       cout << outcome.GetError().PrintAll() << endl;
       return -1;
   }
   // 获取结果
   AcknowledgeMessageResponse resp = outcome.GetResult();
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
        <td style='text-align:left;'>messageId</td>
        <td style='text-align:left;'>消费消息获取导的消息 ID。</td>
    </tr>
    <tr>
        <td style='text-align:left;'>topicName</td>
        <td style='text-align:left;'>Topic 名称，格式为: 集群（租户）ID/命名空间/Topic名称，示例：pulsar-xxx/sdk_http/topic1。可以从控制台上
            <strong><a href='https://console.cloud.tencent.com/tdmq/topic'>Topic 管理</a></strong> 页面直接复制。
        </td>
    </tr>
    <tr>
        <td style='text-align:left;'>subName</td>
        <td style='text-align:left;'>订阅名称，可在控制台<strong>集群管理 </strong>&gt; <strong>消费者</strong>tab页面复制。</td>
    </tr>
    </tbody>
</table>


上述是对消息收发操作的简单介绍，完整实例可参考[ Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-pulsar-demo/http/tdmq-pulsar-cpp-http-demo.zip) 或 [云 API Explorer](https://console.cloud.tencent.com/api/explorer?Product=tdmq&Version=2020-02-17&Action=ModifyCluster&SignVersion=)。

