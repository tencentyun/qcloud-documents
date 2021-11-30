## Flume 简介
Apache Flume 是可以收集例如日志、事件等数据资源，并将这些数量庞大的数据从各项数据资源中集中起来存储的工具/服务。Flume 具有高可用、分布式、配置工具等特性，其设计原理也是将数据流（例如日志数据）从各种网站服务器上汇集起来存储到 HDFS、HBase 等集中存储器中。

## Flume 架构
一个 Flume 事件被定义为一个数据流单元。Flume agent 其实是一个 JVM 进程，该进程中包含完成任务所需要的各个组件，其中最核心的三个组件是 Source、Channel 以及 Sink。
![](https://main.qcloudimg.com/raw/b09b330fba73733c011b36ed1d914962.png)
- **Source**
消费外部源（例如 Web 服务器或者其他 Source）传递给它的事件，并将其保存到 Channel（一个或多个）中。
- **Channel**
Channel 位于 Source 和 Sink 之间，用于缓存进来的 events，当 Sink 成功的将 events 发送到下一跳的 Channel 或最终目的，events 从 Channel 移除。
- **Sink**
Sink 负责将 events 传输到下一跳或最终目的，成功完成后将 events 从 Channel 移除。

## 使用指南
### 使用准备
- 已创建一个 EMR 集群。[创建 EMR 集群](https://cloud.tencent.com/document/product/589/10981) 时需要在软件配置界面选择 flume 组件。
- flume 安装在 EMR 云服务器（core 节点和 task 节点）的 `/usr/local/service/flume` 路径下；master 节点的安装路径是  `/usr/local/service/apps/`。

### 配置 Flume 
进入 `/usr/local/service/flume` 文件夹，并创建 example.conf 文件。
![](https://main.qcloudimg.com/raw/ac14a7fa53ba406cbc48e6c2b1c0a201.png)
```
 # example.conf: A single-node Flume configuration
 
 # Name the components on this agent
 a1.sources = r1
 a1.sinks = k1
 a1.channels = c1
 
 # Describe/configure the source
 a1.sources.r1.type = netcat
 a1.sources.r1.bind = localhost
 a1.sources.r1.port = 44444
 
 # Describe the sink
 a1.sinks.k1.type = logger
 
 # Use a channel which buffers events in memory
 a1.channels.c1.type = memory
 a1.channels.c1.capacity = 1000
 a1.channels.c1.transactionCapacity = 100
 
 # Bind the source and sink to the channel
 a1.sources.r1.channels = c1
 a1.sinks.k1.channel = c1
```

### 启动 Flume
```bash
bin/flume-ng agent --conf conf --conf-file example.conf --name a1 -Dflume.root.logger=INFO,console
```

### 配置测试样例
配置后将会看到之前启动的 Flume Agent 向终端打印。
```bash
telnet localhost 44444
Trying 127.0.0.1...
Connected to localhost.localdomain (127.0.0.1).
Escape character is '^]'.
Hello world! <ENTER>
OK
```

