## 操作场景
TDMQ 提供了 Go 语言的 SDK 来调用服务，进行消息队列的生产和消费。

本文主要介绍 Go SDK 的使用方式，提供 Demo 工程的安装、下载、配置及运行示例，帮助工程师快速搭建 TDMQ 测试工程。

## 操作步骤

### 准备 Demo 环境

1. 安装 IDE
您可以 [安装 GoLand](https://www.jetbrains.com/zh-cn/go/promo) 或其它的 Go IDE 来运行这个 Demo，本文以 Go Land 为例。

2. 下载 TDMQ 的 [Demo 工程](https://github.com/apache/pulsar-client-go) 到本地。

### 配置 Demo工程

使用 IDE 打开 Demo 项目，如下：
![](https://main.qcloudimg.com/raw/2baca719f9cf4e56b9ba0d2f6561680d.png)

需要关注的是其中的 example 包中的 Demo工程。
![](https://main.qcloudimg.com/raw/e8d04b09e65f7781dc230180b93a5561.png)


Demo 基础的版本，只需要成功启动了 pulsar 的集群即可，无需配置其它认证数据。

需要在 Producer 和 Consumer 中配置 TDMQ 的 broker 地址，如下所示：

在 consumer.go 文件中配置，替换这部分的地址：
![](https://main.qcloudimg.com/raw/d055c9e4e5b339c29f3da9a3dc83342d.png)

在 producer.go 中也要进行类似配置：
![](https://main.qcloudimg.com/raw/d6e35344b08612843df526cb292f28fc.png)

之后先启动 consumer.go，再启动 producer.go，之后观察控制台消息：

在 producer 的控制台可以看到消息发送成功：
![](https://main.qcloudimg.com/raw/e021cf6b299ea35ef55c66ab2450cca3.png)

在 consumer 的控制台可以看到消息被成功接收：
![](https://main.qcloudimg.com/raw/a06c89f3d03ca28af53c14cc471d2d4e.png)

则 Go 版本的 SDK Demo 运行成功。

### 配置 Token 认证

在生产环境中我们绝大多数情况下需要认证用户操作，即需要在pulsar集群中启用 authentication，具体的认证配置这里不展开说明。

我们在 pulsar 集群中启用了 authentication 的认证之后会得到一个 jason web token 串，在使用时需要将其配置在客户端选项中，如下所示部分：
![](https://main.qcloudimg.com/raw/39b3001c69c58c72ba3d814b7dd471a4.png)

若是配置正确，会如上文所示，消息的发送和消费会成功。

若是配置错误的话，消息控制台会显示如下信息：
![](https://main.qcloudimg.com/raw/8994db9e3ee7a538270dc8ca361fc6c8.png)

