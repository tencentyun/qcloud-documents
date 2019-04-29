日志支持通过客户端或通过 API/SDK 的方式采集日志。采集至 CLS 平台上的日志将根据一定规则进行结构化。

## 采集方式

### 通过 API/SDK 采集日志

您可以通过调用 [日志服务API](https://cloud.tencent.com/document/product/614/12445) 上传结构化日志至日志服务。相关文档参考：[上传日志接口](https://cloud.tencent.com/document/product/614/12406)

### 通过 LogListener 客户端实时采集

LogListener 是腾讯云日志服务提供的日志采集 Agent，您可以在您的服务器上安装 LogListener 实时采集指定路径上的日志，并对日志原始数据进行结构化。只需以下三个步骤您就可以使用 LogListener 采集：

第一步：在机器上安装 Loglistener；

第二步：在腾讯云日志服务控制台上创建机器组；

第三步：在日志主题处关联机器组并完成相关配置。

相关文档参考：[使用 LogListener 采集日志](https://cloud.tencent.com/document/product/614/14541)

## 日志结构化

日志的结构化是指您的日志数据将以 key-value 的形式存储在 CLS 平台上。日志结构化后，您可以下载结构化的日志，指定键值进行检索，或者对日志进行结构化的投递。

- 采集 API 允许您直接上传结构化的日志数据。
- LogListener 采集 Agent 允许您指定日志数据的结构化方式，将您的非结构化日志原始数据进行结构化解析。例如：您的一条日志原始数据为 `10002345987;write;error;topic does not exist`，您可以指定日志的解析方式是分隔符方式，分隔符为分号，所有的键值（key）为 eventid action status msg。那么该条日志将被结构化为四个键值对，即 `eventid:10002345987 action:write status error msg:topic does not exist`。