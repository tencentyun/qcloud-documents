## 现场采集功能概述

在 Oceanus 平台上，Flink 的 JobManager 和 TaskManager 运行在独立的容器（Pod）中。当 TaskManager 或 JobManager 的 Pod 遇到问题退出后，崩溃现场随时也会被即时清理，给故障定位带来了困难。

目前作业运行期间所有 JobManager、TaskManager 的日志都会采集到用户日志服务（CLS），并支持在控制台 [查看和检索日志](https://cloud.tencent.com/document/product/849/48288)。但除了日志外，现场还包括了 OOM Dump 文件、JVM 崩溃日志、程序在运行期间写入的其他文件等等，这些都对问题的定位非常有用。

因此，我们提供了 Pod 现场采集功能，用户为某个作业开启该功能后，每当该作业的 Flink TaskManager 和 JobManager 正常或异常结束，其日志目录（`/opt/flink/log`）下的所有文件都会被打包上传到集群绑定的 COS 存储桶中，以供用户分析。

> ! 注意
>
> 部分旧集群暂不支持此特性。如果您对该特性有需求，请提工单或等待后续系统自动升级。



## 开启方式

Pod 现场采集会将每个 TaskManager 和 JobManager 退出后的现场上传到集群绑定的 COS 桶中。为了避免带来过多的存储开销，默认并未启用该功能。

用户可以在作业的 [高级参数](https://cloud.tencent.com/document/product/849/53391) 中，增加如下内容，以启用 Pod 现场采集特性：

```yaml
flink.kubernetes.diagnosis-collection-enabled: true
```

> ! 注意
>
> 该功能启用后，任何写入 `/opt/flink/log` 目录下的文件，都会被采集并上传。

如果您需要在 Flink TaskManager 发生 OOM（内存溢出）错误时，能将堆内存 Dump 采集并进行后续分析，可以在高级参数中增加如下内容：

```yaml
env.java.taskmanager.opts: -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/opt/flink/log/taskmanager.hprof -XX:ErrorFile=/opt/flink/log/taskmanager.err
```



## 查看采集文件

所有采集的 Pod 现场文件，会自动打包并上传到集群绑定的 COS 存储桶的 `/oceanus-diagnosis/` 目录下，目录结构为 

- JobManager：`/oceanus-diagnosis/集群ID/作业ID/运行ID/jobmanager-时间戳.tgz`

- TaskManager：`/oceanus-diagnosis/集群ID/作业ID/运行ID/taskmanager-1-TaskManager的ID.tgz`

如下图所示

![](https://main.qcloudimg.com/raw/85c98925e6bc9e8502004d095d2f5d88.png)