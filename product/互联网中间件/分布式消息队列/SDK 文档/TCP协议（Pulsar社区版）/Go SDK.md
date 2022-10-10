## 操作场景

本文以调用 Go SDK 为例介绍通过开源 SDK 实现消息收发的操作过程，帮助您更好地理解消息收发的完整过程。

## 前提条件

- [完成资源创建与准备](https://cloud.tencent.com/document/product/1179/44814)
- [安装 Go](https://golang.org/dl/)
- [下载 Demo](https://tdmq-document-1306598660.cos.ap-nanjing.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91demo/pulsar/tcp/tdmq-pulsar-go-sdk-demo.zip)

## 操作步骤

1. 在客户端环境引入 `pulsar-client-go` 库。

   1. 在客户端环境执行如下命令下载 Pulsar 客户端相关的依赖包。
      <dx-codeblock>
      :::  shell
      go get -u "github.com/apache/pulsar-client-go/pulsar"
      :::
      </dx-codeblock>
   2. 安装完成后，即可通过以下代码引用到您的 Go 工程文件中。
      <dx-codeblock>
      :::  go
      import "github.com/apache/pulsar-client-go/pulsar"
      :::
      </dx-codeblock>

2. 创建 Pulsar Client。
   <dx-codeblock>
   :::  go
   // 创建pulsar客户端
   client, err := pulsar.NewClient(pulsar.ClientOptions{
       // 服务接入地址
       URL: serviceUrl,
       // 授权角色密钥
       Authentication:    pulsar.NewAuthenticationToken(authentication),
       OperationTimeout:  30 * time.Second,
       ConnectionTimeout: 30 * time.Second,
   })

   if err != nil {
       log.Fatalf("Could not instantiate Pulsar client: %v", err)
   }

   defer client.Close()
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
        <td style='text-align:left;'>serviceUrl</td>
        <td style='text-align:left;'>集群接入地址，可以在控制台 <a
                href='https://console.cloud.tencent.com/tdmq/cluster'><strong>集群管理</strong></a> 页面查看并复制。<br><img
                src="https://qcloudimg.tencent-cloud.cn/raw/1221f6b1be8ad150a6544a3f9394a8eb.png"
                referrerpolicy="no-referrer" alt="img"></td>
    </tr>
    <tr>
        <td style='text-align:left;'>Authentication</td>
        <td style='text-align:left;'>角色密钥，在 <strong><a
                href='https://console.cloud.tencent.com/tdmq/role'>角色管理</a></strong> 页面复制<strong>密钥</strong>列复制。<img
                src="https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png" referrerpolicy="no-referrer"
                alt="img"></td>
    </tr>
    </tbody>
</table>

3. 创建生产者。
   <dx-codeblock>
   :::  go
   // 使用客户端创建生产者
   producer, err := client.CreateProducer(pulsar.ProducerOptions{
       // topic完整路径，格式为persistent://集群（租户）ID/命名空间/Topic名称
       Topic: "persistent://pulsar-mmqwr5xx9n7g/sdk_go/topic1",
   })

   if err != nil {
       log.Fatal(err)
   }
   defer producer.Close()
   :::
   </dx-codeblock>
   <dx-alert infotype="explain" title="">
   Topic 名称需要填入完整路径，即 `persistent://clusterid/namespace/Topic`，`clusterid/namespace/topic` 的部分可以从控制台上 **[Topic管理](https://console.cloud.tencent.com/tdmq/topic)** 页面直接复制。
   </dx-alert>

4. 发送消息。
   <dx-codeblock>
   :::  go
   // 发送消息
   _, err = producer.Send(context.Background(), &pulsar.ProducerMessage{
       // 消息内容
       Payload: []byte("hello go client, this is a message."),
       // 业务key
       Key: "yourKey",
       // 业务参数
       Properties: map[string]string{"key": "value"},
   })
   :::
   </dx-codeblock>

5. 创建消费者。
   <dx-codeblock>
   :::  go
   // 使用客户端创建消费者
   consumer, err := client.Subscribe(pulsar.ConsumerOptions{
       // topic完整路径，格式为persistent://集群（租户）ID/命名空间/Topic名称
       Topic:            "persistent://pulsar-mmqwr5xx9n7g/sdk_go/topic1",
       // 订阅名称
       SubscriptionName: "topic1_sub",
       // 订阅模式
       Type:             pulsar.Shared,
   })
   if err != nil {
       log.Fatal(err)
   }
   defer consumer.Close()
   :::
   </dx-codeblock>

> ?
>
> - Topic 名称需要填入完整路径，即 `persistent://clusterid/namespace/Topic`，`clusterid/namespace/topic` 的部分可以从控制台上 **[Topic管理](https://console.cloud.tencent.com/tdmq/topic)** 页面直接复制。
>   ![img](https://qcloudimg.tencent-cloud.cn/raw/dc1bc50c434546755565c6dcb8d3e7f0.png)
> - subscriptionName 需要写入订阅名，可在**消费管理**界面查看。

6. 消费消息。
   <dx-codeblock>
   :::  go
   // 获取消息
   msg, err := consumer.Receive(context.Background())
   if err != nil {
       log.Fatal(err)
   }
   // 模拟业务处理
   fmt.Printf("Received message msgId: %#v -- content: '%s'\n",
              msg.ID(), string(msg.Payload()))

   // 消费成功，回复ack，消费失败根据业务需要选择回复nack或ReconsumeLater
   consumer.Ack(msg)
   :::
   </dx-codeblock>

7. 登录 [TDMQ Pulsar 版控制台](https://console.cloud.tencent.com/tdmq)，依次点击 **Topic 管理** > **Topic 名称**进入消费管理页面，点开订阅名下方右三角号，可查看生产消费记录。
   ![img](https://main.qcloudimg.com/raw/3bee532dab55b7cab1167416aac95f4d.png)

>?上述是对消息的发布和订阅方式的简单介绍。更多操作可参见 [Demo](https://tdmq-document-1306598660.cos.ap-nanjing.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91demo/pulsar/tcp/tdmq-pulsar-go-sdk-demo.zip) 或 [Pulsar 官方文档](https://pulsar.apache.org/docs/en/client-libraries-go/)。


## 自定义日志文件输出

### 使用场景

很多用户在使用 Pulsar Go SDK 时，未能自定义指定日志输出，Go SDK 默认将日志输出到了 os.Stderr 中去，具体如下：

<dx-codeblock>
:::  go

// It's recommended to make this a global instance called `log`.
func New() *Logger {
	return &Logger{
		Out:          os.Stderr, // 默认输出
		Formatter:    new(TextFormatter),
		Hooks:        make(LevelHooks),
		Level:        InfoLevel,
		ExitFunc:     os.Exit,
		ReportCaller: false,
	}
}

:::
</dx-codeblock>

由于日志信息的默认输出大都为 `os.Stderr`，如果用户没有自定义日志 lib 的话，Go SDK 的日志就会和业务日志混淆到一起，增加了问题定位的难度。


### 解决方案

Go SDK 在 Client 侧暴露了一个 logger 的接口，可以支持用户自定义自己的 log 输出的格式以及位置等功能，同时也支持使用 logrus 以及 zab 等不同的日志 lib，具体参数如下：

1. 自定义 log lib 实现 Pulsar Go SDK 提供的 log.Logger 的接口：
<dx-codeblock>
:::  go

// ClientOptions is used to construct a Pulsar Client instance.
type ClientOptions struct {
	// Configure the logger used by the client.
	// By default, a wrapped logrus.StandardLogger will be used, namely,
	// log.NewLoggerWithLogrus(logrus.StandardLogger())
	// FIXME: use `logger` as internal field name instead of `log` as it's more idiomatic
	Logger log.Logger
}

:::
</dx-codeblock>
所以用户在使用 Go SDK 时，可以通过自定义 `logger` 接口的形式，自定义 `log lib`，来达到将日志重定向到指定位置的目的。下面以 `logrus` 为例，自定义一个 `log lib`，将 Go SDK 的日志输出到指定文件：
<dx-codeblock>
:::  go

package main

import (
	"fmt"
	"io"
	"os"

	"github.com/apache/pulsar-client-go/pulsar/log"
	"github.com/sirupsen/logrus"

)

// logrusWrapper implements Logger interface
// based on underlying logrus.FieldLogger
type logrusWrapper struct {
	l logrus.FieldLogger
}

// NewLoggerWithLogrus creates a new logger which wraps
// the given logrus.Logger
func NewLoggerWithLogrus(logger *logrus.Logger, outputPath string) log.Logger {
	writer1 := os.Stdout
	writer2, err := os.OpenFile(outputPath, os.O_WRONLY|os.O_CREATE, 0755)
	if err != nil {
		logrus.Error("create file log.txt failed: %v", err)
	}
	logger.SetOutput(io.MultiWriter(writer1, writer2))
	return &logrusWrapper{
		l: logger,
	}
}

func (l *logrusWrapper) SubLogger(fs log.Fields) log.Logger {
	return &logrusWrapper{
		l: l.l.WithFields(logrus.Fields(fs)),
	}
}

func (l *logrusWrapper) WithFields(fs log.Fields) log.Entry {
	return logrusEntry{
		e: l.l.WithFields(logrus.Fields(fs)),
	}
}

func (l *logrusWrapper) WithField(name string, value interface{}) log.Entry {
	return logrusEntry{
		e: l.l.WithField(name, value),
	}
}

func (l *logrusWrapper) WithError(err error) log.Entry {
	return logrusEntry{
		e: l.l.WithError(err),
	}
}

func (l *logrusWrapper) Debug(args ...interface{}) {
	l.l.Debug(args...)
}

func (l *logrusWrapper) Info(args ...interface{}) {
	l.l.Info(args...)
}

func (l *logrusWrapper) Warn(args ...interface{}) {
	l.l.Warn(args...)
}

func (l *logrusWrapper) Error(args ...interface{}) {
	l.l.Error(args...)
}

func (l *logrusWrapper) Debugf(format string, args ...interface{}) {
	l.l.Debugf(format, args...)
}

func (l *logrusWrapper) Infof(format string, args ...interface{}) {
	l.l.Infof(format, args...)
}

func (l *logrusWrapper) Warnf(format string, args ...interface{}) {
	l.l.Warnf(format, args...)
}

func (l *logrusWrapper) Errorf(format string, args ...interface{}) {
	l.l.Errorf(format, args...)
}

type logrusEntry struct {
	e logrus.FieldLogger
}

func (l logrusEntry) WithFields(fs log.Fields) log.Entry {
	return logrusEntry{
		e: l.e.WithFields(logrus.Fields(fs)),
	}
}

func (l logrusEntry) WithField(name string, value interface{}) log.Entry {
	return logrusEntry{
		e: l.e.WithField(name, value),
	}
}

func (l logrusEntry) Debug(args ...interface{}) {
	l.e.Debug(args...)
}

func (l logrusEntry) Info(args ...interface{}) {
	l.e.Info(args...)
}

func (l logrusEntry) Warn(args ...interface{}) {
	l.e.Warn(args...)
}

func (l logrusEntry) Error(args ...interface{}) {
	l.e.Error(args...)
}

func (l logrusEntry) Debugf(format string, args ...interface{}) {
	l.e.Debugf(format, args...)
}

func (l logrusEntry) Infof(format string, args ...interface{}) {
	l.e.Infof(format, args...)
}

func (l logrusEntry) Warnf(format string, args ...interface{}) {
	l.e.Warnf(format, args...)
}

func (l logrusEntry) Errorf(format string, args ...interface{}) {
	l.e.Errorf(format, args...)
}

:::
</dx-codeblock>
2. 在创建 client 的时候，指定自定义的 log lib。
<dx-codeblock>
:::  go

	client, err := pulsar.NewClient(pulsar.ClientOptions{
		URL:    "pulsar://localhost:6650",
		Logger: NewLoggerWithLogrus(log.StandardLogger(), "test.log"),
	})


:::
</dx-codeblock>
通过上述 Demo 示例，即可将 Pulsar Go SDK 的日志文件重定向到了当前目录的 test.log 的文件中，用户可以根据自己的需要将日志文件重定向到指定的位置。

