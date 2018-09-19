流连接提供一个 Flume 的 Sink 插件，通过该插件，能够将 Flume 中数据上报到流连接中。 

首先需要安装标准版本的 Flume（需 1.7.0 版本以上），然后在 Flume 的根目录下新建 plugins.d 目录，解压 Sink 插件到新建的 plugins.d 目录下面即可。解压后在 plugins.d 目录下有 flume-datapipeline-sink 这个目录，该目录下是 lib 和 libext。

流连接的 Flume Sink 组件特殊配置说明如下：
type：必	须	配	置	为 com.tencent.cloud.datapipeline.flume.sink.DataPipelineSink
datapipeline.appID：腾讯云里面的 appid
datapipeline.secretID：腾讯云里面的 asecretId
datapipeline.secretKey：腾讯云里面的 asecretKey
datapipeline.endPoint：上传数据的 url 地址
Datapipeline.project：项目名称
Datapipeline.topic：上传的 topic 名称
batchSize：每次上传多少条数据

下面是一个完整的 Flume 的配置示例（第三段为插件特有的配置）：
```
agent-1.channels.ch-1.type = memory
agent-1.channels.ch-1.capacity = 100000
agent-1.channels.ch-1.transactionCapacity = 100000
	
agent-1.sources.avro-source1.channels = ch-1
agent-1.sources.avro-source1.type = avro
agent-1.sources.avro-source1.bind = 0.0.0.0
agent-1.sources.avro-source1.port = 41414
agent-1.sources.avro-source1.threads = 50

//插件特有的配置
agent-1.sinks.log-sink1.channel = ch-1
agent-1.sinks.log-sink1.type = com.tencent.cloud.datapipeline.flume.sink.DataPipelineSink
agent-1.sinks.log-sink1.datapipeline.appID = 1251966477
agent-1.sinks.log-sink1.datapipeline.secretID = sfhwu4545654634n3nf3f34t4g
agent-1.sinks.log-sink1.datapipeline.secretKey = fegreghgrfbrj5u7674wh4h54hg
agent-1.sinks.log-sink1.datapipeline.endPoint = http://10.66.89.217
agent-1.sinks.log-sink1.datapipeline.project = internal_test
agent-1.sinks.log-sink1.datapipeline.topic = internal
agent-1.sinks.log-sink1.batchSize = 5000
　　
agent-1.channels = ch-1
agent-1.sources = avro-source1
agent-1.sinks = log-sink1
```	

将数据传递到流连接，除了使用上面介绍 Flume 方式外，还可以通过调用提供的 SDK 来实现。 
