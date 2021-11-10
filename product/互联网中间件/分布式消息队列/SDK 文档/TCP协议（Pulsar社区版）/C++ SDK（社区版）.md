## 操作场景

TDMQ Pulsar 版2.7.1及以上版本的集群已支持 Pulsar 社区版 C++ SDK。本文介绍如何使用 Pulsar 社区版 C++ SDK 完成接入。

## 前提条件

- 获取接入地址
  在 TDMQ Pulsar 版控制台 **[集群管理](https://console.cloud.tencent.com/tdmq/cluster)** 页面复制接入地址。

- 获取密钥
  已参考 [角色与鉴权](https://cloud.tencent.com/document/product/1179/47543) 文档配置好了角色与权限，并获取到了对应角色的密钥（Token）。


## 操作步骤

1. 按照 [Pulsar 官方文档](http://pulsar.apache.org/docs/en/client-libraries-cpp/) 在您客户端所在的环境中安装 pulsar C++ 的库。
   ```sh
   brew install libpulsar
   ```

2. 在创建 client 的代码中，配置准备好的接入地址和密钥，下面展示一个生产消息的示例。
<dx-codeblock>
::: c++
  
#include <pulsar/Client.h>

//新建一个Client
pulsar::ClientConfiguration config;
config.setAuth(pulsar::AuthToken::createWithToken("eyJh****"));

pulsar::Client client("http://***", config); //替换成接入地址
   
//新增一个生产者（单个client下可以创建多个生产者，请尽量复用）
Producer producer;
Result result = client.createProducer("persistent://pulsar-****/default/mytopic", producer);
if (result != ResultOk) {
				LOG_ERROR("Error creating producer: " << result);
				return -1;
}

//发送消息
for (int i = 0; i < 10; i++){
				Message msg = MessageBuilder().setContent("my-message").build();
				Result res = producer.send(msg);
				LOG_INFO("Message sent: " << res);
}

//关闭客户端（长时间不使用一定要记得关闭客户端，及时回收连接池资源）
client.close();
:::
</dx-codeblock>


关于 Pulsar 社区版 C++ SDK 各种功能的使用方式，请参考 [Pulsar 官方文档](http://pulsar.apache.org/docs/en/client-libraries-cpp/)。

