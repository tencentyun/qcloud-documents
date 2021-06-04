GooseFS 会采集 Master 和 Worker 节点运行的时候产生的日志；上层计算应用在发起作业时，GooseFS 也会记录各类请求的日志。GooseFS 日志能力基于 [log4j](https://logging.apache.org/log4j/2.x/) 实现，可以通过修改 log4j.properties 配置来调整日志能力，例如日志存储路径，日志级别，是否记录 RPC 调用情况等。用户可以到 GooseFS 的配置文件目录下打开并修改 log4j.properties 文件：

```plaintext
$ cd /usr/local/service/goosefs/conf
$ cat log4j.properties

# May get overridden by System Property

log4j.rootLogger=INFO, ${goosefs.logger.type}, ${goosefs.remote.logger.type}

log4j.category.goosefs.logserver=INFO, ${goosefs.logserver.logger.type}
log4j.additivity.goosefs.logserver=false

log4j.logger.AUDIT_LOG=INFO, ${goosefs.master.audit.logger.type}
log4j.additivity.AUDIT_LOG=false

...
```



下文将详细介绍 GooseFS 的日志配置：

## 1. **日志存储位置**

GooseFS 采集的日志默认存储在 ${GOOSEFS}/logs 目录下。其中，Master 采集的日志存储在 /logs/master.log 中，Worker 采集的日志存储在 /logs/worker.log 中。需要注意的是， 节点进程异常抛出的日志会记录在 master.out 或者 worker.out 中，正常情况下这两类文件均为空文件，系统有异常时会记录异常信息以便追溯。

以 Master 节点的日志存储配置为例，以下为常用的几项配置：

```plaintext
# Appender for Master
log4j.appender.MASTER_LOGGER=org.apache.log4j.RollingFileAppender
log4j.appender.MASTER_LOGGER.File=${goosefs.logs.dir}/master.log
log4j.appender.MASTER_LOGGER.MaxFileSize=10MB
log4j.appender.MASTER_LOGGER.MaxBackupIndex=100
log4j.appender.MASTER_LOGGER.layout=org.apache.log4j.PatternLayout
log4j.appender.MASTER_LOGGER.layout.ConversionPattern=%d{ISO8601} %-5p %c{1} - %m%n
```


配置参数介绍如下：

- MASTER_LOGGER：指定采集日志组件。
- MASTER_LOGGER.File：指定日志存储路径，可以通过修改路径来自定义日志存储位置。
- MASTER_LOGGER.MaxFileSize：指定单个日志文件大小的上限。
- MASTER_LOGGER.MaxBackupIndex：指定日志文件数上限。
- MASTER_LOGGER.layout：指定日志输出格式模板。
- MASTER_LOGGER.layout.ConversionPattern：指定日志输出的具体格式。

>!
- .log 文件是滚动存储的，可以将其备份到 UFS 如对象存储 COS 中指定的存储桶以便持久化存储；.out 文件不滚动存储，如果需要清理 .out 文件需要手动发起删除操作。
- 更多 log4j 的参数配置可以参考 [log4j configuration 文档](https://logging.apache.org/log4j/2.x/manual/configuration.html)。
- GooseFS 仅存储本身产生的日志，上层计算应用产生的日志可以根据计算应用的日志配置，查看日志存储位置。常见计算应用的日志配置信息可见：[Apache Hadoop](https://docs.alluxio.io/os/user/stable/en/compute/Hadoop-MapReduce.html#logging-configuration), [Apache HBase](https://docs.alluxio.io/os/user/stable/en/compute/HBase.html#logging-configuration), [Apache Hive](https://docs.alluxio.io/os/user/stable/en/compute/Hive.html#logging-configuration), [Apache Spark](https://docs.alluxio.io/os/user/stable/en/compute/Spark.html#logging-configuration)。

## 2. **日志级别**

GooseFS 提供了以下 5 种级别的日志：

- TRACE: 详细的调用日志，适用于调试方法和类的调用。
- DEBUG: 较详细的调用日志，适用于 DEBUG 过程中排查问题。
- INFO: 概括进程状态的信息。
- WARN: 警告类信息，任务进程可以继续执行但客户需要了解潜在的影响。
- ERROR: 系统报错信息，影响任务进行。

上述 5 种级别日志的详细程度从高到低，配置高等级的日志级别会一并记录低等级的日志信息。默认情况下 GooseFS 配置 INFO 级别的日志，记录 INFO、WARN、ERROR三个级别的日志。

一般而言，**推荐到日志配置文件中修改日志级别**，可以到 GooseFS 的配置文件目录下打开并修改 log4j.properties 文件。如下示例展示了将所有 GooseFS 的日志级别修改为 DEBUG 级别：

```plaintext
log4j.rootLogger=DEBUG, ${goosefs.logger.type}, ${goosefs.remote.logger.type}
```


如果需要指定某些类的日志级别，可以在配置文件中添加声明，如下示例展示指定 GooseFSFileInStream 这个类的日志级别为 DEBUG：

```plaintext
log4j.logger.goosefs.client.file.GooseFSFileInStream=DEBUG
```

在一些特定的场景下，用户可能需要在集群运行过程中修改日志参数，此时可以通过在命令行中输入 logLevel 相关的指令进行调整。如下为 logLevl 支持的配置：

```plaintext
$ goosefs logLevel
Unable to parse input args: Missing required option: logName
usage: logLevel [--level <arg>] --logName <arg> [--target <arg>]
    --level <arg>     The log level to be set.
    --logName <arg>   The logger's name(e.g. goosefs.master.file.DefaultFileSystemMaster) you want to get or set level.
    --target <arg>    <master|workers|host:webPort>. A list of targets separated by, can be specified. host:webPort pair must be one of workers. Default target is master and all workers
```


各项配置的详细说明如下：

- level：日志级别，支持TRACE、DEBUG、INFO、WARN、ERROR五种级别。
- logName：需要采集日志的组件，如goosefs.underfs.hdfs.HdfsUnderFileSystem等。
- target：日志采集范围，可以设置为指定的 Master 或者 Worker 节点（通过 IP：PORT 方式指定），默认为 Master 和所有 Worker 节点。

用户可以按需在系统运行过程中调整日志级别，以便排查系统运行过程中的问题。如以下示例展示了在运行过程中将所有 Worker 节点上 goosefs.underfs.hdfs.HdfsUnderFileSystem 这个类的日志级别调整为 DEBUG 级别，并在调试完成后调整回 INFO 级别：

```plaintext
$  goosefs logLevel --logName=goosefs.underfs.hdfs.HdfsUnderFileSystem --target=workers --level=DEBUG # 调整为 DEBUG 模式

$  goosefs logLevel --logName=goosefs.underfs.hdfs.HdfsUnderFileSystem --target=workers --level=INFO # 调整为 INFO 模式
```

## 3. **高级配置**

GooseFS 还支持 GC 事件日志，FUSE 接口日志，RPC 调用日志，UFS 操作日志，日志分割等高级配置。以下会介绍部分常用高级配置的使用方式。

- **GC 事件日志**

将 GC 事件日志记录在 .out 文件， 可以通过在 conf/allulxio-env.sh 中添加如下配置：

```plaintext
GOOSEFS_JAVA_OPTS+=" -XX:+PrintGCDetails -XX:+PrintTenuringDistribution -XX:+PrintGCTimeStamps"
```

GOOSEFS_JAVA_OPTS 代表收集所有 GooseFS 节点的 GC 事件日志，也可以通过指定 GOOSEFS_Master_JAVA_OPTS 和 GOOSEFS_Worker_JAVA_OPTS 来分别指定收集 Master 和 Worker上的日志。

- **FUSE 接口日志**

可以在 conf/log4j.properties 文件中启用记录 FUSE 日志：

```plaintext
goosefs.logger.goosefs.fuse.GoosefsFuseFileSystem=DEBUG
```

启用后 FUSE 接口日志可以在 /logs/fuse.log 查看。 

- **启用 RPC 调用日志**

可以在 conf/log4j.properties 文件中启用记录 RPC 调用日志，RPC 调用日志有两种日志类型，其一是客户端发送的 RPC 请求日志，其二为 Master节点发送的请求日志，两种类型日志的配置方式存在差别。

log4j.properties 文件中记录客户端发送的 RPC 请求日志的配置如下：


```plaintext
log4j.logger.goosefs.client.file.FileSystemMasterClient=DEBUG # 文件级别的 RPC 请求日志
log34j.logger.goosefs.client.block.BlockSystemMasterClient=DEBUG # Block 级别的 RPC 请求日志
```


可以通过 logLevel 指令来配置日志 Master 节点发送的 RPC 请求日志：

```plaintext
$ goosefs logLevel \--logName=goosefs.master.file.FileSystemMasterClientServiceHandler \--target master --level=DEBUG # 文件级别的 RPC 请求日志
$ goosefs logLevel \--logName=goosefs.master.block.BlockSystemMasterClientServiceHandler \--target master --level=DEBUG # 文件级别的 RPC 请求日志
```


- **UFS 操作日志**

GooseFS 也支持采集对底层存储系统 UFS 的操作日志。启用 UFS 操作日志收集可以通过在 log4j.properties 文件中添加配置项或者通过 logLevel 指令进行操作。以 logLevel 指令为例：

```plaintext
$ goosefs logLevel \--logName=goosefs.underfs.UnderFileSystemWithLogging \--target master --level=DEBUG # 记录 master 节点对 UFS的操作日志
$ goosefs logLevel \--logName=goosefs.underfs.UnderFileSystemWithLogging \--target workers --level=DEBUG # 记录 worker 节点对 UFS的操作日志
```


- **分割日志**

GooseFS 支持将指定类型日志存储在指定存储路径，如果将所有日志都记录在 .log 文件，可能存在以下问题：

- 当集群规模大，吞吐量较多时，master.log 或者 worker.log 文件可能变得异常庞大，或者触发日志滚存产生大量日志文件。
- 日志信息较多，不利于针对性分析某些类型日志。
- 大量日志存储在本地节点，占用空间。

因此业务可以根据需要在 log4j.properties 文件中添加配置项对日志进行分割，将指定类型日志存储至指定文件路径，如下示例展示了将 StateLockManager 这类型的日志存储在 statelock.log 中：

```plaintext
log4j.category.goosefs.master.StateLockManager=DEBUG, State_LOCK_LOGGER
log4j.additivity.goosefs.master.StateLockManager=false
log4j.appender.State_LOCK_LOGGER=org.apache.log4j.RollingFileAppender
log4j.appender.State_LOCK_LOGGER.File=<GOOSEFS_HOME>/logs/statelock.log
log4j.appender.State_LOCK_LOGGER.MaxFileSize=10MB
log4j.appender.State_LOCK_LOGGER.MaxBackupIndex=100
log4j.appender.State_LOCK_LOGGER.layout=org.apache.log4j.PatternLayout
log4j.appender.State_LOCK_LOGGER.layout.ConversionPattern=%d{ISO8601} %-5p %c{1} - %m%
```


- **筛选日志**

GooseFS 支持按照一定的条件筛选并记录日志，而不是全量记录所有日志。比如在进行性能测试时需要记录 RPC 调用日志，但业务侧并不需要记录所有 RPC 调用日志，只需要记录某些延迟较高的日志即可，此时可以通过在 log4j.properties 文件中添加配置项添加日志筛选条件即可，如下示例分别展示了筛选 RPC 调用延迟超过 200ms 的请求和 FUSE 调用超过 1s 的请求：

```plaintext
goosefs.user.logging.threshold=200ms
goosefs.fuse.logging.threshold=1s
```