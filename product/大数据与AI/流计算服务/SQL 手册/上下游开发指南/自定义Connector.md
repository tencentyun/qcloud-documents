## 介绍
若内置的 Connector 无法满足需求，可以考虑**自定义 Connector** 功能，即用户可以自行上传实现了相应 Source 和 Sink 接口的类实现，然后作业在运行时会动态加载并调用。

## 选择合适的 Connector
用户可以选择第三方提供的 Connector 实现包（例如下面介绍的 Bahir），或者自行通过编程的方式实现。

### Apache Bahir 第三方包
[Apache Bahir](https://bahir.apache.org/) 为 Flink 提供了常见的数据源和数据目的的扩展包。

目前 Bahir 支持如下的第三方组件：
- [ActiveMQ](https://bahir.apache.org/docs/flink/current/flink-streaming-activemq/)
- [Akka](https://bahir.apache.org/docs/flink/current/flink-streaming-akka)
- [Flume](https://bahir.apache.org/docs/flink/current/flink-streaming-flume/)
- [InfluxDB](https://bahir.apache.org/docs/flink/current/flink-streaming-influxdb/)
- [Kudu](https://bahir.apache.org/docs/flink/current/flink-streaming-kudu/)
- [Redis](https://bahir.apache.org/docs/flink/current/flink-streaming-redis/)
- [Netty](https://bahir.apache.org/docs/flink/current/flink-streaming-netty/)

### 自行编程实现
#### 使用新版 Connector API
Flink 1.11 引入了 Source 和 Sink 接口的 [新版 API](https://ci.apache.org/projects/flink/flink-docs-release-1.11/zh/dev/table/sourceSinks.html)，简化了接口定义逻辑（合并 Upsert、Retract、Append Sink 接口），数据源也支持 Upsert 流了，同时也解耦了对 DataStream 和 Planner 等包的依赖关系。

#### 使用旧版 Connector API
新版 API 仍然有一些无法支持的特性，例如过滤条件或者分区下推等。如果发现新版 API 无法实现功能，请参考 [旧版 API](https://ci.apache.org/projects/flink/flink-docs-release-1.11/zh/dev/table/legacySourceSinks.html)。

## 构建并上传 Connector 包
### 步骤一：源码构建
建议参考现有的 Connector 的项目，修改其 `pom.xml` 配置文件，引入相关的依赖包，然后通过 Maven 构建一个 JAR 包。
>!尽量使用 `maven-shade-plugin` 将常见的依赖（例如 Apache Commons、Guava 等相关的包）进行 shade 化，以避免引入的库与流计算平台本身的类发生冲突。

### 步骤二：上传程序包
可以在流计算的 [程序包管理](https://console.cloud.tencent.com/oceanus/resource) 界面，上传 Connector 的程序包。首次上传是 V1 版本，以此类推。

### 步骤三：分析开发页引用程序包
在 SQL 作业的【分析开发】页，可以选择引用之前上传的程序包和版本。
> ! 请务必确认程序包的版本是否符合预期，避免出现各种不可预知的错误。

### 步骤四：保存并发布
选择程序包后，可以单击【保存】，也可以选择直接发布并启动运行。
