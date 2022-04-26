## 操作场景

本文以调用 C++ SDK 为例介绍通过开源 SDK 实现消息收发的操作过程，帮助您更好地理解消息收发的完整过程。

## 前提条件

- [完成资源创建与准备](https://cloud.tencent.com/document/product/1495/61829)
- [下载 Demo](https://tdmq-document-1306598660.cos.ap-nanjing.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91demo/rabbitmq/tdmq-rabbitmq-cpp-sdk-demo.zip)

## 操作步骤

### 步骤1：环境准备

1. 安装客户端相关的库 [C and C++ 库](https://www.rabbitmq.com/devtools.html?spm=a2c4g.11186623.0.0.22d166975jyVxo#c-dev)， 本文以 AMQP-CPP 为例。
2. 导入动态库和头文件。

### 步骤2：生产消息

1. 建立连接。
<dx-codeblock>
:::  c++
   auto evbase = event_base_new();
   LibEventHandlerMyError hndl(evbase);
   
   // 建立连接
   AMQP::TcpConnection connection(&hndl, AMQP::Address(
       "amqp://admin:eyJrZXlJZC...@amqp-xxx.rabbitmq.ap-sh.public.tencenttdmq.com:5672/amqp-xxx|vhost-cpp"));
   	// 服务地址格式为  amqp://username:password@host:port/vhost
   // 建立通道
   AMQP::TcpChannel channel(&connection);
   channel.onError([&evbase](const char *message) {
       std::cout << "Channel error: " << message << std::endl;
       event_base_loopbreak(evbase);
   });
:::
</dx-codeblock>
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left">host</td>
<td align="left">集群接入地址，在<strong>集群管理</strong>页面操作列的<strong>获取接入地址</strong>获取。<img src="https://main.qcloudimg.com/raw/e5b19ca7c6b2724fe3545d99874f4ce9.png" alt="img"></td>
</tr>
<tr>
<td align="left">port</td>
<td align="left">集群接入地址中的端口号。</td>
</tr>
<tr>
<td align="left">username</td>
<td align="left">角色名称，在 <strong><a href="https://console.cloud.tencent.com/tdmq/role">角色管理</a></strong> 页面复制。</td>
</tr>
<tr>
<td align="left">password</td>
<td align="left">角色密钥，在 <strong><a href="https://console.cloud.tencent.com/tdmq/role">角色管理</a></strong> 页面复制<strong>密钥</strong>列复制。<img src="https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png" alt="img"></td>
</tr>
<tr>
<td align="left">vhost</td>
<td align="left">Vhost 名称，在控制台 Vhost 页面复制，格式是<strong>“集群 ID + | + vhost 名称”</strong>。<img src="https://main.qcloudimg.com/raw/ae6ec1a5a94c9befea289ad7f5b46aed.png" alt="img"></td>
</tr>
</tbody></table>
2. 发送消息。
<dx-codeblock>
:::  c++
   // 声明交换机
   channel.declareExchange(exchange_name, AMQP::ExchangeType::direct);
   
   // 发送消息到交换机
   channel.publish(exchange_name, routing_key, "Hello client this is a info message");
   
   event_base_dispatch(evbase);
   event_base_free(evbase);
:::
</dx-codeblock>
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left">exchange_name</td>
<td align="left">Exchange 名称，可在控制台 Exchange 列表获取。</td>
</tr>
<tr>
<td align="left">routing_key</td>
<td align="left">消息队列支持的routing key</td>
</tr>
</tbody></table>

### 步骤3：消费消息

1. 建立连接。
<dx-codeblock>
:::  c++
ConnHandler handler;
// 建立连接
AMQP::TcpConnection connection(handler, AMQP::Address(host, part, AMQP::Login(username, password), vhost));
// 建立通道
AMQP::TcpChannel channel(&connection);
channel.onError([&handler](const char *message) {
		std::cout << "Channel error: " << message << std::endl;
		handler.Stop();
});
:::
</dx-codeblock>
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left">host</td>
<td align="left">集群接入地址，在<strong>集群管理</strong>页面操作列的<strong>获取接入地址</strong>获取。<img src="https://main.qcloudimg.com/raw/a0417f57f7f1c8498eec9d56e05924b4.png" alt="img"></td>
</tr>
<tr>
<td align="left">port</td>
<td align="left">集群接入地址中的端口号。</td>
</tr>
<tr>
<td align="left">username</td>
<td align="left">角色名称，在 <strong><a href="https://console.cloud.tencent.com/tdmq/role">角色管理</a></strong> 页面复制。</td>
</tr>
<tr>
<td align="left">password</td>
<td align="left">角色密钥，在 <strong><a href="https://console.cloud.tencent.com/tdmq/role">角色管理</a></strong> 页面复制<strong>密钥</strong>列复制。<img src="https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png" alt="img"></td>
</tr>
<tr>
<td align="left">vhost</td>
<td align="left">Vhost 名称，在控制台 Vhost 页面复制，格式是<strong>“集群 ID + | + vhost 名称”</strong>。<img src="https://main.qcloudimg.com/raw/ae6ec1a5a94c9befea289ad7f5b46aed.png" alt="img"></td>
</tr>
</tbody></table>
2. 声明交换机、消息队列，并将消息队列绑定到交换机
<dx-codeblock>
:::  c++
// 声明交换机
channel.declareExchange(exchange_name, AMQP::ExchangeType::direct);
// 声明消息队列
channel.declareQueue(queue_name, AMQP::durable);
// 绑定消息队列到交换机
channel.bindQueue(exchange_name, queue_name, routing_key);
:::
</dx-codeblock>
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left">exchange_name</td>
<td align="left">Exchange 名称，可在控制台 Exchange 列表获取。</td>
</tr>
<tr>
<td align="left">queue_name</td>
<td align="left">消息队列名称，可在控制台 Queue 列表获取。</td>
</tr>
<tr>
<td align="left">routing_key</td>
<td align="left">消息队列支持的routing key</td>
</tr>
</tbody></table>
3. 订阅消息。
<dx-codeblock>
:::  c++
// 订阅消息
channel.consume(queue_name)
		.onReceived
		(
		[&channel](const AMQP::Message &msg, uint64_t tag, bool redelivered) {
				// 处理消息
				std::cout << "Received: " << msg.body() << std::endl;
				// 回复ack，  消费失败可回复reject
				channel.ack(tag);
		}
);
handler.Start();
:::
</dx-codeblock>
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left">queue_name</td>
<td align="left">消息队列名称，可在控制台 Queue 列表获取。</td>
</tr>
</tbody></table>


>?完整示例或其他使用可参考 [Demo](https://tdmq-document-1306598660.cos.ap-nanjing.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91demo/rabbitmq/tdmq-rabbitmq-cpp-sdk-demo.zip) 或者 [AMQP-CPP ](https://github.com/CopernicaMarketingSoftware/AMQP-CPP)和 [AMQP-CPP 示例](https://github.com/hoxnox/examples.amqp-cpp)

