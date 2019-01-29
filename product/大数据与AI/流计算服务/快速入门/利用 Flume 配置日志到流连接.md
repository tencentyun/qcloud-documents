## 准备工作

### 1.	获取用户信息

登录腾讯云的官网，进入“控制台”，在账号信息栏获取用户的appId（如图1）；然后“访问管理”, “云API秘钥管理”获取用户的secretId和secretKey（如图2）。

![](https://main.qcloudimg.com/raw/9483fd26fbc864873f9e9b1e2094000c.png)
<center><sup>图1 获取用户 appId</sup></center>
<br>

 ![](https://main.qcloudimg.com/raw/d324813aa2112d622a089f4763d1f129.png)
 <center><sub>图2 获取 secretId 和 secretKey </sub></center>
 
### 2. 创建流连接Topic

请参考 [创建新的流连接](https://cloud.tencent.com/document/product/849/17857) 的操作步骤。

## 运行 Flume 插件

流连接（CDP）提供一个 Flume 的 Sink 插件，通过该插件，能够将 Flume 中数据上报到流连接（CDP）中。 

### 1.	配置Flume sink插件

首先需要安装标准版本的 Flume（需 1.7.0 版本以上），然后在 Flume 的根目录下新建 plugins.d 目录，解压 Sink 插件到新建的 plugins.d 目录下面即可。解压后在 plugins.d 目录下有 flume-datapipeline-sink 这个目录，该目录下是 lib 和 libext；然后在Flume的conf目录下新建一个flume-conf.properties文件，进行数据源和数据目的的配置，首先配置数据管道如下：

&nbsp;&nbsp;agent-1.channels.ch-1.type = memory
&nbsp;&nbsp;agent-1.channels.ch-1.capacity = 100000
&nbsp;&nbsp;agent-1.channels.ch-1.transactionCapacity = 100000

根据业务数据量，设置数据管道的capacity，以及transactionCapacity；

### 2.	配置数据源

可使用本地文件，或者kafka作为数据源；如果使用kafka作为数据源，则配置如下：

&nbsp;&nbsp;agent-1.sources.avro-source1.channels = ch-1
&nbsp;&nbsp;agent-1.sources.avro-source1.type = org.apache.flume.source.kafka.KafkaSource
&nbsp;&nbsp;agent-1.sources.avro-source1.threads = 1
&nbsp;&nbsp;agent-1.sources.avro-source1.kafka.bootstrap.servers=
&nbsp;&nbsp;agent-1.sources.avro-source1.kafka.topics=
&nbsp;&nbsp;agent-1.sources.avro-source1.kafka.consumer.group.id=
&nbsp;&nbsp;如果使用本地的文件作为数据源，则配置如下：
&nbsp;&nbsp;agent-1.sources.avro-source1.type = TAILDIR
&nbsp;&nbsp;agent-1.sources.avro-source1.channels = ch-1
&nbsp;&nbsp;agent-1.sources.avro-source1.positionFile = ./position.json
&nbsp;&nbsp;agent-1.sources.avro-source1.skipToEnd = false
&nbsp;&nbsp;agent-1.sources.avro-source1.filegroups = f1
&nbsp;&nbsp;agent-1.sources.avro-source1.filegroups.f1 =

如果使用kafka作为数据源，则需要指定对应的bootstrap.servers，以及对应的topics，以及对应的消费者的group.id；如果使用本地文件作为数据源，需要指定本地文件的路径，在如上图的agent-1.sources.avro-source1.filegroup.f1 处指定；

### 3.	配置数据目的

配置数据目的到流连接（CDP），使用如下配置

&nbsp;&nbsp;agent-1.sinks.log-sink1.channel = ch-1
&nbsp;&nbsp;agent-1.sinks.log-sink1.type = com.tencent.cloud.datapipeline.flume.sink.DataPipelineSink
&nbsp;&nbsp;agent-1.sinks.log-sink1.appId =
&nbsp;&nbsp;agent-1.sinks.log-sink1.secretId =
&nbsp;&nbsp;agent-1.sinks.log-sink1.secretKey =
&nbsp;&nbsp;agent-1.sinks.log-sink1.endpoint =
&nbsp;&nbsp;agent-1.sinks.log-sink1.project =
&nbsp;&nbsp;agent-1.sinks.log-sink1.topic =
&nbsp;&nbsp;agent-1.sinks.log-sink1.batchSize =5000
&nbsp;&nbsp;agent-1.sinks.log-sink1.csv.delimiter =,
&nbsp;&nbsp;agent-1.sinks.log-sink1.partitionid =-1
&nbsp;&nbsp;agent-1.sinks.log-sink1.key =0
&nbsp;&nbsp;agent-1.sinks.log-sink1.dataType =csv
&nbsp;&nbsp;agent-1.sinks.log-sink1.addHost=false
&nbsp;&nbsp;agent-1.sinks.log-sink1.addTimestamp=false
&nbsp;&nbsp;agent-1.channels = ch-1
&nbsp;&nbsp;agent-1.sources = avro-source1
&nbsp;&nbsp;agent-1.sinks = log-sink1

设置用户的appId，用户的secretId，secretKey，以及CDP的上报地址，上报的CDP的Project名字，Topic的名字，上报的格式（dataType），以及分割符（delimiter），上报的批量大小（batchsize）等。

### 4.	启动Flume
以上都配置完成后，在Flume的安装目录下执行以下命令

&nbsp;&nbsp;nohup bin/flume-ng agent --conf conf -f ./conf/flume-conf.properties -n agent-1 &

启动 Flume 后，就可以观察数据是否导入成功了。

## 查看数据导入结果

返回流连接的界面，选择对应的Project，对应的Topic，进入“Partitions” 页签，可以进行数据预览，选择对应的时间点进行数据抽样预览，如下：

 ![](https://main.qcloudimg.com/raw/22b185a7d47274edae739cc223eba9a6.png)
 
可以看到，数据已经导入。
