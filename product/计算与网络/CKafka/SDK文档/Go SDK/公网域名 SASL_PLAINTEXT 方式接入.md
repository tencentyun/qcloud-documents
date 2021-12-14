## 操作场景

本文介绍 Go 客户端如何在公网环境下，使用 SASL_PLAINTEXT 方式接入消息队列 CKafka 收发消息。

## 前提条件

- [安装 Go](https://golang.org/dl)
- [配置 ACL 策略](https://cloud.tencent.com/document/product/597/31528)
- [下载 Demo](https://github.com/TencentCloud/ckafka-sdk-demo/tree/main/gokafkademo/PUBLIC_SASL)

## 操作步骤

### 步骤一：准备 Go 依赖库

下载 Demo 后，进入 gokafkademo 目录，执行以下命令安装。

```bash
go get -v gopkg.in/confluentinc/confluent-kafka-go.v1/kafka
```

### 步骤二：准备配置

创建配置文件 kafka.json。

```json
{
  "topic": [
      "xxxx"
  ],
  "sasl": {
      "username": "yourUserName",
      "password": "yourPassword",
      "instanceId":"instanceId"
  },
  "bootstrapServers": [
      "xxx.ap-changsha-ec.ckafka.tencentcloudmq.com:6000"
  ],
  "consumerGroupId": "yourConsumerId"
 }  

```

| 参数             | 描述                                                         |
| :--------------- | :----------------------------------------------------------- |
| topic            | Topic 名称，您可以在控制台上【topic管理】页面复制。<br/>![img](https://main.qcloudimg.com/raw/e7d353c89bbb204303501e8366f59d2c.png) |
| sasl.username    | 用户名，在控制台【用户管理】页面创建用户时设置。             |
| sasl.password    | 用户密码，在控制台【用户管理】页面创建用户时设置。           |
| sasl.instanceId  | 实例 ID，在控制台的实例详情页面的基本信息获取。<br/>![](https://main.qcloudimg.com/raw/9c417da4953669372fa4c13973096d3b.png) |
| bootstrapServers | 接入网络，在控制台的实例详情页面【接入方式】模块的网络列复制。<br/>![img](https://main.qcloudimg.com/raw/c5cf200a66f6dcf627d2ca6f1c747ecf.png) |
| consumerGroupId  | 您可以自定义设置，Demo 运行成功后可以在【Consumer Group】页面看到该消费者。 |

### 步骤三：发送消息

1. 编写生产消息程序。

```go
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
          // username 是实例 ID + # + 配置的用户名，password 是配置的用户密码。
          "sasl.username": fmt.Sprintf("%s#%s", cfg.SASL.InstanceId, cfg.SASL.Username),
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
```

2. 编译并运行程序发送消息。

```bash
go run main.go
```

3. 查看运行结果，示例如下。

```bash
Delivered message to test[0]@628
Delivered message to test[0]@629
```

4. 在 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 的【topic管理】页面，选择对应的 Topic ， 单击【更多】>【消息查询】，查看刚刚发送的消息。
   ![](https://main.qcloudimg.com/raw/ec5fbf218cf50ff3d760be15f6331867.png)

### 步骤四：消费消息

1. 编写消费消息程序。

```go
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
          // username 是实例 ID + # + 配置的用户名，password 是配置的用户密码。
          "sasl.username": fmt.Sprintf("%s#%s", cfg.SASL.InstanceId, cfg.SASL.Username),
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
```

2. 编译并运行程序消费消息。

```bash
go run main.go
```

3. 查看运行结果，示例如下。

```bash
Message on test[0]@628: Confluent-Kafka
Message on test[0]@629: Golang Client Message
```

4. 在 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 的【Consumer Group】页面，选择对应的消费组名称，在主题名称输入 Topic 名称，单击【查询详情】，查看消费详情。
   ![](https://main.qcloudimg.com/raw/27775267907600f4ff759e6a197195ee.png)
