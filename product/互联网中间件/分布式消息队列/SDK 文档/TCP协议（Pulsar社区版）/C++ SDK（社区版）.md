## 操作场景

TDMQ 2.7.1及以上版本的集群已支持 Pulsar 社区版 C++ SDK。本文介绍如何使用 Pulsar 社区版 C++ SDK 完成接入。

## 前提条件

- 获取接入地址
  在 TDMQ 控制台【[集群管理](https://console.cloud.tencent.com/tdmq/cluster)】页面复制接入地址。

- 获取密钥
  已参考 [角色与鉴权](https://cloud.tencent.com/document/product/1179/47543) 文档配置好了角色与权限，并获取到了对应角色的密钥（Token）。


## 操作步骤

1. 按照 [Pulsar 官方文档](http://pulsar.apache.org/docs/en/client-libraries-cpp/) 在您客户端所在的环境中安装  Go Client。
   ```sh
   brew install libpulsar
   ```

2. 在创建 consumer 或 producer 的代码中，配置准备好的接入地址和密钥。
<dx-codeblock>
:::  go
   Client client("http://*",'pulsar.NewAuthenticationToken("eyJh**")');//更换为接入地址（控制台集群管理页完整复制）和密钥
   
   Consumer consumer;
   Result result = client.subscribe("my-topic", "my-subscription-name", consumer);
   if (result != ResultOk) {
       LOG_ERROR("Failed to subscribe: " << result);
       return -1;
   }
   
   Message msg;
   
   while (true) {
       consumer.receive(msg);
       LOG_INFO("Received: " << msg
               << "  with payload '" << msg.getDataAsString() << "'");
   
       consumer.acknowledge(msg);
   }
   
   client.close();
:::
</dx-codeblock>


关于 Pulsar 社区版 C++ SDK 各种功能的使用方式，请参考 [Pulsar 官方文档](http://pulsar.apache.org/docs/en/client-libraries-cpp/)。

