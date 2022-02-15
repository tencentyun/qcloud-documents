## 操作场景

本文以调用 Python SDK 为例介绍通过开源 SDK 实现消息收发的操作过程，帮助您更好地理解消息收发的完整过程。

## 前提条件

- [完成资源创建与准备](https://cloud.tencent.com/document/product/1179/44814)
- [安装 Python](https://www.python.org/downloads/)
- [安装 pip](https://pip-cn.readthedocs.io/en/latest/installing.html)
- [下载 Demo](https://tdmq-document-1306598660.cos.ap-nanjing.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91demo/pulsar/tcp/tdmq-pulsar-python-sdk-demo.zip)

## 操作步骤

1. 准备环境。
   在客户端环境安装 pulsar-client 库，可以使用 pip 进行安装，也可以使用其他方式，参见 [Pulsar Python client](https://pulsar.apache.org/docs/en/client-libraries-python/)。
<dx-codeblock>
:::  shell
   pip install pulsar-client==2.8.1
:::
</dx-codeblock>
2. 创建客户端。
<dx-codeblock>
:::  python
   # 创建客户端
   client = pulsar.Client(
       authentication=pulsar.AuthenticationToken(
           # 已授权角色密钥
           AUTHENTICATION),
       # 服务接入地址
       service_url=SERVICE_URL)
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
:::  python
   # 创建生产者
   producer = client.create_producer(
       # topic完整路径，格式为persistent://集群（租户）ID/命名空间/Topic名称，从【Topic管理】处复制
       topic='pulsar-xxx/sdk_python/topic1'
   )
:::
</dx-codeblock>
<dx-alert infotype="explain" title="">
Topic 名称需要填入完整路径，即 `persistent://clusterid/namespace/Topic`，`clusterid/namespace/topic` 的部分可以从控制台上 **[Topic管理](https://console.cloud.tencent.com/tdmq/topic)** 页面直接复制。
</dx-alert>
4. 发送消息。
<dx-codeblock>
:::  python
   # 发送消息
   producer.send(
       # 消息内容
       'Hello python client, this is a msg.'.encode('utf-8'),
       # 消息参数
       properties={'k': 'v'},
       # 业务key
       partition_key='yourKey'
   )
:::
</dx-codeblock>
   还可以使用异步方式发送消息。
<dx-codeblock>
:::  python
   # 异步发送回调
   def send_callback(send_result, msg_id):
       print('Message published: result:{}  msg_id:{}'.format(send_result, msg_id))
   
   # 发送消息
   producer.send_async(
       # 消息内容
       'Hello python client, this is a async msg.'.encode('utf-8'),
       # 异步回调
       callback=send_callback,
       # 消息配置
       properties={'k': 'v'},
       # 业务key
       partition_key='yourKey'
   )
:::
</dx-codeblock>
5. 创建消费者。
<dx-codeblock>
:::  python
   # 订阅消息
   consumer = client.subscribe(
       # topic完整路径，格式为persistent://集群（租户）ID/命名空间/Topic名称，从【Topic管理】处复制
       topic='pulsar-xxx/sdk_python/topic1',
       # 订阅名称
       subscription_name='sub_topic1'
   )
:::
</dx-codeblock>
> ?
>
> - Topic 名称需要填入完整路径，即 `persistent://clusterid/namespace/Topic`，`clusterid/namespace/topic` 的部分可以从控制台上 **[Topic管理](https://console.cloud.tencent.com/tdmq/topic)** 页面直接复制。
>   ![img](https://qcloudimg.tencent-cloud.cn/raw/dc1bc50c434546755565c6dcb8d3e7f0.png)
> - subscriptionName 需要写入订阅名，可在**消费管理**界面查看。
6. 消费消息。
<dx-codeblock>
:::  python
   # 获取消息
   msg = consumer.receive()
   try:
       # 模拟业务
       print("Received message '{}' id='{}'".format(msg.data(), msg.message_id()))
       # 消费成功，回复ack
       consumer.acknowledge(msg)
   except:
       # 消费失败，消息将会重新投递
       consumer.negative_acknowledge(msg)
:::
</dx-codeblock>
7. 登录 [TDMQ Pulsar 版控制台](https://console.cloud.tencent.com/tdmq)，依次点击 **Topic 管理** > **Topic 名称**进入消费管理页面，点开订阅名下方右三角号，可查看生产消费记录。
   ![img](https://main.qcloudimg.com/raw/3bee532dab55b7cab1167416aac95f4d.png)

>?上述是对消息的发布和订阅方式的简单介绍。更多操作可参见 [Demo](https://tdmq-document-1306598660.cos.ap-nanjing.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91demo/pulsar/tcp/tdmq-pulsar-python-sdk-demo.zip) 或 [Pulsar 官方文档](https://pulsar.apache.org/docs/en/client-libraries-python/)。
