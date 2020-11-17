## 准备工作
### 1.	获取用户信息
登录腾讯云 [账号中心](https://console.cloud.tencent.com/developer)，在【账号信息】页获取用户的 APPID；选择【访问管理】>【云API密钥】>【API密钥管理】获取用户的 SecretId 和 SecretKey。
![](https://main.qcloudimg.com/raw/e577edac94f63b6afc1218a56b31291c.png)
![](https://main.qcloudimg.com/raw/8703f7da8eb323a76182ed7ea8158d62.png)
 
### 2. 创建流连接 Topic
请参见 [创建新的流连接](https://cloud.tencent.com/document/product/849/17857) 来创建 Topic。

## 运行 Flume 插件
流连接（CDP）提供一个 Flume 的 Sink 插件，通过该插件，能够将 Flume 中数据上报到流连接（CDP）中。 

### 1.	配置 Flume sink 插件
首先需要安装标准版本的 Flume（需1.7.0版本以上），然后在 Flume 的根目录下新建 plugins.d 目录，解压 Sink 插件到新建的 plugins.d 目录下面即可。
解压后在 plugins.d 目录下有 flume-datapipeline-sink 目录，该目录下是 lib 和 libext；然后在 Flume 的 conf 目录下新建一个 flume-conf.properties 文件，进行数据源和数据目的的配置，首先配置数据管道如下：
```
agent-1.channels.ch-1.type = memory
agent-1.channels.ch-1.capacity = 100000
agent-1.channels.ch-1.transactionCapacity = 100000
```

根据业务数据量，设置数据管道的 capacity 和 transactionCapacity。

### 2.	配置数据源
可使用本地文件，或者 kafka 作为数据源。
- 如果使用 kafka 作为数据源，需要指定对应的 bootstrap.servers、对应的 topics，以及对应的消费者的group.id，配置如下：
```
agent-1.sources.avro-source1.channels = ch-1
agent-1.sources.avro-source1.type = org.apache.flume.source.kafka.KafkaSource
agent-1.sources.avro-source1.threads = 1
agent-1.sources.avro-source1.kafka.bootstrap.servers=
agent-1.sources.avro-source1.kafka.topics=
agent-1.sources.avro-source1.kafka.consumer.group.id=
```

- 如果使用本地文件作为数据源，需要指定本地文件的路径，在以下 agent-1.sources.avro-source1.filegroup.f1 处指定，配置如下：
```
agent-1.sources.avro-source1.type = TAILDIR
agent-1.sources.avro-source1.channels = ch-1
agent-1.sources.avro-source1.positionFile = ./position.json
agent-1.sources.avro-source1.skipToEnd = false
agent-1.sources.avro-source1.filegroups = f1
agent-1.sources.avro-source1.filegroups.f1 =
```


### 3.	配置数据目的
配置数据目的到流连接（CDP），配置如下：
```
agent-1.sinks.log-sink1.channel = ch-1
agent-1.sinks.log-sink1.type = com.tencent.cloud.datapipeline.flume.sink.DataPipelineSink
agent-1.sinks.log-sink1.appId =
agent-1.sinks.log-sink1.secretId =
agent-1.sinks.log-sink1.secretKey =
agent-1.sinks.log-sink1.endpoint =
agent-1.sinks.log-sink1.project =
agent-1.sinks.log-sink1.topic =
agent-1.sinks.log-sink1.batchSize =5000
agent-1.sinks.log-sink1.csv.delimiter =,
agent-1.sinks.log-sink1.partitionid =-1
agent-1.sinks.log-sink1.key =0
agent-1.sinks.log-sink1.dataType =csv
agent-1.sinks.log-sink1.addHost=false
agent-1.sinks.log-sink1.addTimestamp=false
agent-1.channels = ch-1
agent-1.sources = avro-source1
agent-1.sinks = log-sink1
```

设置用户的 APPID、用户的 SecretId、SecretKey、CDP 的上报地址、上报的 CDP 的 Project 名字、Topic 的名字、上报的格式（dataType）、分割符（delimiter）、上报的批量大小（batchsize）等。

### 4.	启动 Flume
以上都配置完成后，在 Flume 的安装目录下执行以下命令：
```
nohup bin/flume-ng agent --conf conf -f ./conf/flume-conf.properties -n agent-1 &
```
启动 Flume 后，就可以观察数据是否导入成功了。

## 查看数据导入结果
返回流连接页面，选择对应的 Project、对应的 Topic，进入【Partitions】页，可以进行数据预览，选择对应的时间点进行数据抽样预览，如下图可以看到，数据已经导入。
 ![](https://main.qcloudimg.com/raw/22b185a7d47274edae739cc223eba9a6.png)
 

