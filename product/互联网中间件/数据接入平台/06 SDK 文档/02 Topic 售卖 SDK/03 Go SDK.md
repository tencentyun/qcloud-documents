## 操作场景
本文介绍使用  Go 客户端连接数据接入平台 Topic 并收发消息的操作步骤。

## 前提条件
[安装 Go](https://golang.org/dl)

## 操作步骤

### 步骤1：准备环境

安装 kafka 依赖。
<dx-codeblock>
:::  bash
go get -v gopkg.in/confluentinc/confluent-kafka-go.v1/kafka
:::
</dx-codeblock>



### 步骤2：创建 Topic 和订阅关系

1. 在 DIP 控制台的 [Topic 列表](https://console.cloud.tencent.com/ckafka/datahub-topic) 页面创建一个 Topic。
![](https://qcloudimg.tencent-cloud.cn/raw/5f26dfc66930683c95c45e6d614d7a01.png)
2. 单击 Topic 的 “ID” 进入基本信息页面，获取用户名、密码和地址信息。
![](https://qcloudimg.tencent-cloud.cn/raw/3e2cde1cfd74193d4c78a89f98a8a613.png)
3. 在**订阅关系**页签，新建一个订阅关系（消费组）。
   ![](https://qcloudimg.tencent-cloud.cn/raw/ea08126a23715f24c50936d564421655.png)



### 步骤3：添加配置文件

创建配置文件 kafka.json。
<dx-codeblock>
:::  json
{
  "topic": [
      "xxxx"
  ],
  "sasl": {
      "username": "yourUserName",
      "password": "yourPassword",
  },
  "bootstrapServers": [
      "xx.xx.xx.xx:port"
  ],
  "consumerGroupId": "yourConsumerId"
 }  
:::
</dx-codeblock>
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left"><code>bootstrapServers</code></td>
<td align="left">接入地址，在 DIP 控制台的 Topic 基本信息页面获取。<img src="https://qcloudimg.tencent-cloud.cn/raw/e493ab1980da1b90d07b60251b30222a.png" alt=""></td>
</tr>
<tr>
<td align="left"><code>username</code></td>
<td align="left">用户名，在 DIP 控制台的 Topic 基本信息页面获取。</td>
</tr>
<tr>
<td align="left"><code>password</code></td>
<td align="left">用户密码，在 DIP 控制台的 Topic 基本信息页面获取。</td>
</tr>
<tr>
<td align="left"><code>topic</code></td>
<td align="left">Topic 名称，在 DIP 控制台的 Topic 基本信息页面获取。</td>
</tr>
<tr>
<td align="left"><code>consumerGroupId</code></td>
<td align="left">消费组名称，在 DIP 控制台的 <strong>订阅关系</strong>列表获取。<br><img src="https://qcloudimg.tencent-cloud.cn/raw/a5e47dc885da62e742286a6210cdfeea.png" alt=""></td>
</tr>
</tbody></table>



### 步骤3：生产消息

1. 编写生产消息程序。
<dx-codeblock>
:::  go
  package main
  
  import (
      "fmt"
      "gokafkademo/config"
      "log"
      "strings"
  
      "github.com/confluentinc/confluent-kafka-go/kafka"
  )
  
  func main() {
  
      cfg, err := config.ParseConfig("../config/kafka.json")
      if err != nil {
          log.Fatal(err)
      }
  
      p, err := kafka.NewProducer(&kafka.ConfigMap{
          // 设置接入点，请通过控制台获取对应Topic的接入点。
          "bootstrap.servers": strings.Join(cfg.Servers, ","),
          // SASL 验证机制类型默认选用 PLAIN
          "sasl.mechanism": "PLAIN",
          // 在本地配置 ACL 策略。
          "security.protocol": "SASL_PLAINTEXT",
          // username 是配置的用户名，password 是配置的用户密码。
          "sasl.username": cfg.SASL.Username,
          "sasl.password": cfg.SASL.Password,
  
          // Kafka producer 的 ack 有 3 种机制，分别说明如下：
          // -1 或 all：Broker 在 leader 收到数据并同步给所有 ISR 中的 follower 后，才应答给 Producer 继续发送下一条（批）消息。
          // 这种配置提供了最高的数据可靠性，只要有一个已同步的副本存活就不会有消息丢失。注意：这种配置不能确保所有的副本读写入该数据才返回，
          // 可以配合 Topic 级别参数 min.insync.replicas 使用。
          // 0：生产者不等待来自 broker 同步完成的确认，继续发送下一条（批）消息。这种配置生产性能最高，但数据可靠性最低（当服务器故障时可能会有数据丢失，如果 leader 已死但是 producer 不知情，则 broker 收不到消息）
          // 1： 生产者在 leader 已成功收到的数据并得到确认后再发送下一条（批）消息。这种配置是在生产吞吐和数据可靠性之间的权衡（如果leader已死但是尚未复制，则消息可能丢失）
          // 用户不显示配置时，默认值为1。用户根据自己的业务情况进行设置
          "acks": 1,
          // 请求发生错误时重试次数，建议将该值设置为大于0，失败重试最大程度保证消息不丢失
          "retries": 0,
          // 发送请求失败时到下一次重试请求之间的时间
          "retry.backoff.ms": 100,
          // producer 网络请求的超时时间。
          "socket.timeout.ms": 6000,
          // 设置客户端内部重试间隔。
          "reconnect.backoff.max.ms": 3000,
      })
      if err != nil {
          log.Fatal(err)
      }
  
      defer p.Close()
  
      // 产生的消息 传递至报告处理程序
      go func() {
          for e := range p.Events() {
              switch ev := e.(type) {
              case *kafka.Message:
                  if ev.TopicPartition.Error != nil {
                      fmt.Printf("Delivery failed: %v\n", ev.TopicPartition)
                  } else {
                      fmt.Printf("Delivered message to %v\n", ev.TopicPartition)
                  }
              }
          }
      }()
  
      // 异步发送消息
      topic := cfg.Topic
      for _, word := range []string{"Confluent-Kafka", "Golang Client Message"} {
          _ = p.Produce(&kafka.Message{
              TopicPartition: kafka.TopicPartition{Topic: &topic, Partition: kafka.PartitionAny},
              Value:          []byte(word),
          }, nil)
      }
  
      // 等待消息传递
      p.Flush(10 * 1000)
:::
</dx-codeblock>
2. 编译并运行程序发送消息。
<dx-codeblock>
:::  bash
go run main.go
:::
</dx-codeblock>
3. 查看运行结果，示例如下。
<dx-codeblock>
:::  bash
Delivered message to test[0]@628
Delivered message to test[0]@629
:::
</dx-codeblock>


### 步骤4：消费消息

1. 编写消费消息程序。
<dx-codeblock>
:::  go
  package main
  
  import (
      "fmt"
      "gokafkademo/config"
      "log"
      "strings"
  
      "github.com/confluentinc/confluent-kafka-go/kafka"
  )
  
  func main() {
  
      cfg, err := config.ParseConfig("../config/kafka.json")
      if err != nil {
          log.Fatal(err)
      }
  
      c, err := kafka.NewConsumer(&kafka.ConfigMap{
          // 设置接入点，请通过控制台获取对应Topic的接入点。
          "bootstrap.servers": strings.Join(cfg.Servers, ","),
          // SASL 验证机制类型默认选用 PLAIN
          "sasl.mechanism": "PLAIN",
          // 在本地配置 ACL 策略。
          "security.protocol": "SASL_PLAINTEXT",
          // username 是配置的用户名，password 是配置的用户密码。
          "sasl.username": cfg.SASL.Username,
          "sasl.password": cfg.SASL.Password,
          // 设置的消息消费组
          "group.id":          cfg.ConsumerGroupId,
          "auto.offset.reset": "earliest",
  
          // 使用 Kafka 消费分组机制时，消费者超时时间。当 Broker 在该时间内没有收到消费者的心跳时，认为该消费者故障失败，Broker
          // 发起重新 Rebalance 过程。目前该值的配置必须在 Broker 配置group.min.session.timeout.ms=6000和group.max.session.timeout.ms=300000 之间
          "session.timeout.ms": 10000,
      })
  
      if err != nil {
          log.Fatal(err)
      }
      // 订阅的消息topic 列表
      err = c.SubscribeTopics([]string{"test", "test-topic"}, nil)
      if err != nil {
          log.Fatal(err)
      }
  
      for {
          msg, err := c.ReadMessage(-1)
          if err == nil {
              fmt.Printf("Message on %s: %s\n", msg.TopicPartition, string(msg.Value))
          } else {
              // 客户端将自动尝试恢复所有的 error
              fmt.Printf("Consumer error: %v (%v)\n", err, msg)
          }
      }
  
      c.Close()
  }
:::
</dx-codeblock>
2. 编译并运行程序消费消息。
<dx-codeblock>
:::  bash
go run main.go
:::
</dx-codeblock>
3. 查看运行结果，示例如下。
<dx-codeblock>
:::  bash
Message on test[0]@628: Confluent-Kafka
Message on test[0]@629: Golang Client Message
:::
</dx-codeblock>

