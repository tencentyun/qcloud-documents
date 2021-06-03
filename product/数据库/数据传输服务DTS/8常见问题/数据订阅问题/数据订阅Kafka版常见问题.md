### 为什么我消费不到数据？
- 排查网络问题，Kafka 服务器地址为腾讯云内网地址，只能在腾讯云与订阅实例相同地域的私有网络内访问。
- 排查订阅 topic、内网地址、消费组名称、帐号、密码等是否正确。可在 [数据订阅控制台](https://console.cloud.tencent.com/dts/dss) 单击订阅名进入订阅详情页和消费管理页查看。
- 排查加密参数是否正确，参见 [Kafka 使用何种认证机制](#faq3)。

### 数据格式是怎么样的?
数据订阅 Kafka 版使用 Protobuf 进行序列化。Protobuf 协议文件可在 [此处](https://subscribesdk-1254408587.cos.ap-beijing.myqcloud.com/subscribe.proto) 下载，Demo 工程中也包含了协议文件，具体请参考 [生产和消费逻辑讲解](https://cloud.tencent.com/document/product/571/52381#dgxljjj)。

### [Kafka 使用何种认证机制？](id:faq3)
如下所示：
![](https://main.qcloudimg.com/raw/83aa8f6122ee106f57568b6f25a1bd08.png)

### 何时进行 Kafka commit?
首先请将 Kafka 的 enable_auto_commit 参数设置为 false，以关闭自动 commit。生产者会在消息序列中的合适位置插入 Checkpoint 消息，消费者消费到 Checkpoint 消息后进行 commit，这样有利于保证消息的完整性。

### 服务端消息保留多久，如何设置消费 offset？
服务端消息保留1天。可以根据需要配置 Kafka 的 auto_offset_reset 参数为 earliest 或者 latest。如果需要从具体的 offset 开始消费，则可以利用 Kafka Client 提供的 seek 功能，重新设置消费 offset。
