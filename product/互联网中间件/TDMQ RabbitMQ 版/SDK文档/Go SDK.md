## 操作场景

本文以调用 Go SDK 为例介绍通过开源 SDK 实现消息收发的操作过程，帮助您更好地理解消息收发的完整过程。

## 前提条件

- [完成资源创建与准备](https://cloud.tencent.com/document/product/1495/61829)
- [安装 Go](https://golang.org/dl/)
- [下载 Demo](https://tdmq-document-1306598660.cos.ap-nanjing.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91demo/rabbitmq/tdmq-rabbitmq-go-sdk-demo.zip)

## 操作步骤

1. 执行如下命令在客户端环境安装所需包。
<dx-codeblock>
:::  shell
go get "github.com/rabbitmq/amqp091-go"
:::
</dx-codeblock>
2. 安装完成后，即可引入到您的 GO 工程文件中。
<dx-codeblock>
:::  go
import (amqp "github.com/rabbitmq/amqp091-go")
:::
</dx-codeblock>
3. 引入之后即可在您的项目中使用客户端。


## 使用示例

1. 建立连接和通信信道。
<dx-codeblock>
:::  go
   // 所需参数
   const (
   	host     = "amqp-xx.rabbitmq.x.tencenttdmq.com" // 服务接入地址
   	username = "roleName" // 角色控制台对应的角色名称
   	password = "eyJrZX..." // 角色对应的密钥
   	vhost    = "amqp-xx|Vhost" // 要使用的Vhost全称
   )
   // 创建连接
   conn, err := amqp.Dial("amqp://" + username + ":" + password + "@" + host + ":5672/" + vhost)
   failOnError(err, "Failed to connect to RabbitMQ")
   defer func(conn *amqp.Connection) {
   	err := conn.Close()
   	if err != nil {
   	}
   }(conn)
   
   // 建立通道
   ch, err := conn.Channel()
   failOnError(err, "Failed to open a channel")
   defer func(ch *amqp.Channel) {
   	err := ch.Close()
   	if err != nil {
   	}
   }(ch)
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
<td align="left">集群接入地址，在<strong>集群管理</strong>页面操作列的<strong>获取接入地址</strong>获取。<img src="https://main.qcloudimg.com/raw/fa643204f9da225cbee264b12154349d.png" alt="img"></td>
</tr>
<tr>
<td align="left">username</td>
<td align="left">角色名称，在 <strong><a href="https://console.cloud.tencent.com/tdmq/role">角色管理</a></strong> 页面复制。</td>
</tr>
<tr>
<td align="left">password</td>
<td align="left">角色密钥，在 <strong><a href="https://console.cloud.tencent.com/tdmq/role">角色管理</a></strong> 页面复制<strong>密钥</strong>列复制。<img src="https://main.qcloudimg.com/raw/65ef236aaaa1b664dfe7fd7bdcbd3576.png" alt=""></td>
</tr>
<tr>
<td align="left">vhost</td>
<td align="left">Vhost 名称，在控制台 Vhost 页面复制，格式是<strong>“集群 ID + | + vhost 名称”</strong>。<img src="https://main.qcloudimg.com/raw/56d10e77bb2af1b70385d47ff29e5f44.png" alt="img"></td>
</tr>
</tbody></table>
2. 声明交换机。
<dx-codeblock>
:::  go
   // 声明交换机 （名称和类型需要与存在的交换机保持一致）
   	err = ch.ExchangeDeclare(
   		"logs-exchange",   // 交换机名称
   		"fanout", // 交换机类型
   		true,     // durable
   		false,    // auto-deleted
   		false,    // internal
   		false,    // no-wait
   		nil,      // arguments
   	)
   	failOnError(err, "Failed to declare a exchange")
:::
</dx-codeblock>
3. 发布消息。
   消息可发给交换机，也可以直接发到指定队列 ( hello world 和 work queues 消息模型)。
 - 发布消息到交换机：
<dx-codeblock>
:::  go
   // 消息内容
   body := "this is new message."
   // 发布消息到交换机   
   err = ch.Publish(
   	"logs-exchange",         // exchange
   	"", // routing key   （根据使用的交换机类型可选择的是否需要routing key），如果不选择交换机，该参数为消息队列名称
   	false,      // mandatory
   	false,      // immediate
   	amqp.Publishing{
   		ContentType: "text/plain",
   		Body:        []byte(body),
   	})
   failOnError(err, "Failed to publish a message")
:::
</dx-codeblock>
 - 发布消息到指定队列：
<dx-codeblock>
:::  go
 // 发布消息到指定的消息队列
 err = ch.Publish(
	"",         // exchange
	queue.Name, // routing key
	false,      // mandatory
	false,      // immediate
	amqp.Publishing{
		ContentType: "text/plain",
		Body:        []byte(body),
	})
 failOnError(err, "Failed to publish a message")
:::
</dx-codeblock>
4. 订阅消息。
<dx-codeblock>
:::  go
   // 创建消费者并消费指定消息队列中的消息
   msgs, err := ch.Consume(
   	"message-queue", // message-queue
   	"",           // consumer
   	false,        // 设置为非自动确认(可根据需求自己选择)
   	false,        // exclusive
   	false,        // no-local
   	false,        // no-wait
   	nil,          // args
   )
   failOnError(err, "Failed to register a consumer")
   
   // 获取消息队列中的消息
   forever := make(chan bool)
   go func() {
   	for d := range msgs {
   		log.Printf("Received a message: %s", d.Body)
   		t := time.Duration(1)
   		time.Sleep(t * time.Second)
   		// 手动回复ack
   		d.Ack(false)
   	}
   }()
   log.Printf(" [Consumer] Waiting for messages.")
   <-forever
:::
</dx-codeblock>
5. 消费者使用 routing key。
<dx-codeblock>
:::  go
   // 需要在消息队列中指定 交换机 和 routing key
   err = ch.QueueBind(
   	q.Name, // queue name
   	"routing_key",     // routing key
   	"topic_demo", // exchange
   	false,
   	nil,
   )
   failOnError(err, "Failed to bind a queue")
:::
</dx-codeblock>


>?详细使用示例可参见 [Demo](https://tdmq-document-1306598660.cos.ap-nanjing.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91demo/rabbitmq/tdmq-rabbitmq-go-sdk-demo.zip) 或 [RabbitMQ 官网](https://www.rabbitmq.com/getstarted.html)。

