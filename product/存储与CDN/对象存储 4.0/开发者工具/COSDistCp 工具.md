## 功能说明

COSDistCp 是一款基于 MapReduce 的分布式文件拷贝工具，主要用于 HDFS 和 COS 之间的数据拷贝，它主要具有以下功能点：
- 根据长度、CRC 校验和，进行文件的增量迁移、数据校验
- 对源目录中的文件进行正则表达式过滤
- 对源目录中的文件进行解压缩 ，并转换为预期的压缩格式
- 基于正则表达式，对文本文件进行聚合
- 保留源文件和源目录的用户、组、扩展属性和时间
- 配置告警和 Prometheus 监控
- 统计文件大小分布
- 对读取带宽进行限速

## 使用环境

#### 系统环境

支持 Linux 系统。

#### 软件依赖

Hadoop-2.6.0及以上版本、Hadoop-COS 插件 5.9.3 及以上版本。

## 下载与安装

#### 获取 COSDistCp jar 包

- Hadoop 2.x 用户可下载 [cos-distcp-1.9-2.8.5.jar 包](https://cos-sdk-archive-1253960454.file.myqcloud.com/cos-distcp/cos-distcp-1.9-2.8.5.jar)，根据 jar 包的 [MD5 校验值](https://cos-sdk-archive-1253960454.file.myqcloud.com/cos-distcp/cos-distcp-1.9-2.8.5-md5.txt) 确认下载的 jar 包是否完整。
- Hadoop 3.x 用户可下载 [cos-distcp-1.9-3.1.0.jar 包](https://cos-sdk-archive-1253960454.file.myqcloud.com/cos-distcp/cos-distcp-1.9-3.1.0.jar)，根据 jar 包的 [MD5 校验值](https://cos-sdk-archive-1253960454.file.myqcloud.com/cos-distcp/cos-distcp-1.9-3.1.0-md5.txt) 确认下载的 jar 包是否完整。

#### 安装说明

在 Hadoop 环境下，安装 [Hadoop-COS](https://cloud.tencent.com/document/product/436/6884#.E4.B8.8B.E8.BD.BD.E4.B8.8E.E5.AE.89.E8.A3.85) 后，即可直接运行 COSDistCp 工具。


## 原理说明

COSDistCp 基于 MapReduce 框架实现，为多进程+多线程的架构，可以对文件进行拷贝、数据校验、压缩、文件属性保留以及拷贝重试等工作。COSDistCp 默认会覆盖目标端已经存在的同名文件，当文件迁移或校验失败的时候，对应的文件会拷贝失败，并会在临时目录下记录迁移失败的文件信息。当您的源目录有文件新增或文件内容发生变化时，您可通过 skipMode 或 diffMode 模式，通过对比文件的长度或 CRC 校验值，进行数据校验和进行文件的增量迁移。


## 参数说明

您可使用命令 `hadoop jar cos-distcp-${version}.jar --help` 查看 COSDistCp 支持的参数选项，其中`${version}`为版本号，以下为当前版本 COSDistCp 的参数说明：


|              属性键              | 说明                                                         | 默认值 | 是否必填 |
| :------------------------------: | :----------------------------------------------------------- | :----: | :------: |
|              --help              | 输出 COSDistCp 支持的参数选项<br> 示例：--help               |   无   |    否    |
|          --src=LOCATION          | 指定拷贝的源目录，可以是 HDFS 或者 COS 路径<br> 示例：--src=hdfs://user/logs/ |   无   |    是    |
|         --dest=LOCATION          | 指定拷贝的目标目录，可以是 HDFS 或者 COS 路径<br> 示例：--dest=cosn://examplebucket-1250000000/user/logs |   无   |    是 |
|       --srcPattern=PATTERN       | 指定正则表达式对源目录中的文件进行过滤<br>示例：`--srcPattern='.*.log'`<br>**注意：您需要将参数使用单引号包围，以避免符号`*`被 shell 解释** |   无   |    否    |
|       --taskNumber=VALUE       | 指定拷贝进程数，示例：--taskNumber=10 |   10   |    否    |
|       --workerNumber=VALUE       | 指定拷贝线程数，COSDistCp 在每个拷贝进程中创建该参数大小的拷贝线程池<br>示例：--workerNumber=4 |   4    |    否    |
|      --filesPerMapper=VALUE      | 指定每个 Mapper 输入文件的行数<br>示例：--filesPerMapper=10000 | 500000 |    否    |
|        --groupBy=PATTERN         | 指定正则表达式对文本文件进行聚合</br>示例：--groupBy='.\*group-input/(\d+)-(\d+).\*' |   无   |    否    |
|        --targetSize=VALUE        | 指定目标文件的大小，单位：MB，与 --groupBy 一起使用</br>示例：--targetSize=10 |   无   |    否    |
|       --outputCodec=VALUE        | 指定输出文件的压缩方式，可选 gzip、lzo、snappy、none 和 keep，其中：</br> 1. keep 保持原有文件的压缩方式<br>2. none 则根据文件后缀对文件进行解压， </br>示例：--outputCodec=gzip </br>**注意：如果存在文件 /dir/test.gzip 和 /dir/test.gz，指定输出格式为 lzo，最终只会保留一个文件 /dir/test.lzo** |  keep  |    否    |
|        --deleteOnSuccess         | 指定源文件拷贝到目标目录成功时，立即删除源文件</br>示例：--deleteOnSuccess，</br>**注意：1.7 及以上版本不再提供该参数，建议数据迁移成功并使用 --diffMode 校验后，再删除源文件系统的数据** | false  |    否    |
| --multipartUploadChunkSize=VALUE | 指定 Hadoop-COS 插件传输文件到 COS 时分块的大小，COS 支持的最大分块数为 10000，您可根据文件大小，调整分块大小，单位：MB，默认为8MB</br>示例：--multipartUploadChunkSize=20 |  8MB   |    否    |
|    --cosServerSideEncryption     | 指定文件上传到 COS 时，使用 SSE-COS 作为加解密算法</br>示例：--cosServerSideEncryption | false  |    否    |
|      --outputManifest=VALUE      | 指定拷贝完成的时候，在目标目录下生成本次拷贝的目标文件信息列表（GZIP 压缩）</br>示例：--outputManifest=manifest.gz |   无   |    否    |
|    --requirePreviousManifest     | 要求指定 --previousManifest=VALUE 参数，以进行增量拷贝</br>示例：--requirePreviousManifest | false  |    否    |
|   --previousManifest=LOCATION    | 前一次拷贝生成的目标文件信息<br>示例：--previousManifest=cosn://examplebucket-1250000000/big-data/manifest.gz |   无   |    否    |
|        --copyFromManifest        | 和 --previousManifest=LOCATION 一起使用，可将 --previousManifest 中的文件，拷贝到目标文件系统<br>示例：--copyFromManifest | false  |    否    |
|       --storageClass=VALUE       | 指定对象存储类型，可选值为 STANDARD、STANDARD_IA、ARCHIVE、DEEP_ARCHIVE、INTELLIGENT_TIERING，关于更多支持的存储类型和介绍，请参见 [存储类型概述](https://cloud.tencent.com/document/product/436/33417) |   无   |    否    |
|    --srcPrefixesFile=LOCATION    | 指定本地文件，该文件中每行包含一个需要拷贝的源目录</br>示例：--srcPrefixesFile=file:///data/migrate-folders.txt |   无   |    否    |
|         --skipMode=MODE          | 拷贝文件前，校验源文件和目标文件是否相同，相同则跳过，可选 none（不校验）、length （长度）、checksum（CRC值）和 length-checksum（长度 + CRC 值）</br>示例：--skipMode=length |  length-checksum  |    否    |
|         --checkMode=MODE         | 当文件拷贝完成的时候，校验源文件和目标文件是否相同，可选 none（不校验）、 length （长度）、checksum（CRC值）和 length-checksum（长度 + CRC 值）<br/>示例：--checkMode=length-checksum |  length-checksum  |    否    |
|         --diffMode=MODE          | 指定获取源和目的目录的差异文件列表，可选 length （长度）、checksum（CRC 值）和 length-checksum（长度 + CRC 值）</br>示例：--diffMode=length-checksum |   无   |    否    |
|      --diffOutput=LOCATION       | 指定差异文件列表的 HDFS 输出目录，该输出目录必须为空<br/>示例：--diffOutput=/diff-output |   无   |    否    |
|      --cosChecksumType=TYPE      | 指定 Hadoop-COS 插件使用的 CRC 算法，可选值为 CRC32C 和 CRC64<br/>示例：--cosChecksumType=CRC32C | CRC32C |    否    |
|      --preserveStatus=VALUE      | 指定是否将源文件的 user、group、permission、xattr 和 timestamps 元信息拷贝到目标文件，可选值为 ugpxt（即为 user、group、permission、xattr 和 timestamps 的英文首字母）<br/>示例：--preserveStatus=ugpt |   无   |    否    |
|      --ignoreSrcMiss      | 忽略存在于文件清单中，但拷贝时不存在的文件 |   false   | 否       |
|      --promGatewayAddress=VALUE      | 指定 MapReduce 任务运行的 Counter 数据推送到的 Prometheus PushGateway 的地址和端口 |   无   |    否    |
|      --promGatewayDeleteOnFinish=VALUE   | 指定任务完成时，删除 Prometheus PushGateway 中 JobName 的指标集合</br>示例：--promGatewayDeleteOnFinish=true | true    |    否   |
|      --promGatewayJobName=VALUE      | 指定上报给 Prometheus PushGateway 的 JobName </br>示例：--promGatewayJobName=cos-distcp-hive-backup           |   无   |    否    |
|      --promCollectInterval=VALUE      | 指定收集 MapReduce 任务 Counter 信息的间隔，单位：ms </br>示例：--promCollectInterval=5000            |   5000   |    否    |
|      --promPort=VALUE      | 指定将 Prometheus 指标暴露给外部的 Server 端口 <br>示例：--promPort=9028            |   无   |    否    |
|      --enableDynamicStrategy      | 指定开启任务动态分配策略，使迁移速度快的任务迁移更多的文件。</br>**注意：该模式存在一定局限性，例如任务计数器在进程异常的情况下计数不准确，请迁移完成后用 --diffMode 进行数据校验** </br>示例：--enableDynamicStrategy            |   false   |    否    |
|      --splitRatio=VALUE      | 指定 Dynamic Strategy 的切分比例，splitRatio 值越大，则任务粒度越小</br>示例：--splitRatio=8            |   8   |    否    |
|      --localTemp=VALUE      | 指定 Dynamic Strategy 生成的任务信息文件所在的本地文件夹</br>示例：--localTemp=/tmp            |   /tmp   |    否    |
|      --taskFilesCopyThreadNum=VALUE      | 指定 Dynamic Strategy 任务信息文件拷贝到 HDFS 上的并发度 </br>示例：--taskFilesCopyThreadNum=32            |   32   |    否    |
|      --statsRange=VALUE      | 指定统计的区间范围</br>示例：---statsRange=0,1mb,10mb,100mb,1gb,10gb,inf   |   0,1mb,10mb,100mb,1gb,10gb,inf   |    否    |
|      --printStatsOnly      | 只统计待迁移文件大小的分布信息，不迁移数据</br>示例：--printStatsOnly            |   无   |    否    |
|      --bandWidth      | 限制读取每个迁移文件的带宽，单位为：MB/s，默认-1，不限制读取带宽。</br>示例：--bandWidth=10            |   无   |    否    |
|      --jobName      | 指定迁移任务的名称。</br>示例：--jobName=cosdistcp-to-warehouse            |   无   |    否    |
|      --compareWithCompatibleSuffix  | 使用 --skipMode 和 --diffMode 参数时，是否将源文件的后缀 gzip 转换为 gz，lzop 文件后缀转换为 lzo，进行判断。</br>示例：--compareWithCompatibleSuffix |   无   |    否    |

## 使用示例

### 查看 help 选项

以参数`--help`执行命令，查看 COSDistCp 支持的参数，示例如下：

```plaintext
hadoop jar cos-distcp-${version}.jar --help
```
以上命令中， `${version}` 为 COSDistCp 版本号，例如 1.0 版本的 COSDistCp jar 包名为 cos-distcp-1.0.jar。

### 统计待迁移的文件大小分布信息

以参数 `--printStatsOnly` 和 `--statsRange=VALUE` 执行命令，输出待迁移文件的大小分布信息：

```plaintext
hadoop jar cos-distcp-${version}.jar --src /wookie/data --dest cosn://examplebucket-1250000000/wookie/data --printStatsOnly  --statsRange=0,1mb,10mb,100mb,1gb,10gb,inf

Copy File Distribution Statistics:
Total File Count: 4
Total File Size: 1190133760
| SizeRange         | TotalCount          | TotalSize           |
| 0MB ~ 1MB         | 0(0.00%)            | 0(0.00%)            |
| 1MB ~ 10MB        | 1(25.00%)           | 1048576(0.09%)      |
| 10MB ~ 100MB      | 1(25.00%)           | 10485760(0.88%)     |
| 100MB ~ 1024MB    | 1(25.00%)           | 104857600(8.81%)    |
| 1024MB ~ 10240MB  | 1(25.00%)           | 1073741824(90.22%)  |
| 10240MB ~ LONG_MAX| 0(0.00%)            | 0(0.00%)            |
```

### 指定待迁移文件的源目录和目标目录

以参数`--src` 和 `--dest`执行命令，示例如下：

```plaintext
hadoop jar cos-distcp-${version}.jar --src /data/warehouse --dest cosn://examplebucket-1250000000/data/warehouse
```


COSDistCp 默认会对拷贝失败的文件重试5次，如果仍然失败，则会将失败文件信息写入 /tmp/${randomUUID}/output/failed/ 目录下，其中，${randomUUID} 为随机字符串。记录失败文件信息后，COSDistcp 会继续迁移剩余文件，迁移任务并不会因为部分文件迁移失败而失败。在迁移任务完成的时候，COSDistcp 会输出计数器信息，并判断是否存在文件迁移失败，如果存在，则在提交任务的客户端抛出异常。

以下类型的源文件信息包含在输出文件中：
1. 存在源文件的清单中，但拷贝时源文件不存在，记录为 SRC_MISS
2. 其他原因导致的拷贝失败，统一记录为 COPY_FAILED

您可以重新运行拷贝命令实现增量迁移，通过如下命令，获取 MapReduce 任务的日志，确定文件拷贝失败的原因，其中 application_1610615435237_0021 为应用 ID：
```plaintext
yarn logs -applicationId application_1610615435237_0021 > application_1610615435237_0021.log
```

### 查看 Counters 

在拷贝任务结束时，会输出文件拷贝的统计信息，相关计数器如下：

```plaintext
CosDistCp Counters
        BYTES_EXPECTED=10198247
        BYTES_SKIPPED=10196880
        FILES_COPIED=1
        FILES_EXPECTED=7
        FILES_FAILED=1
        FILES_SKIPPED=5
```

文件拷贝的统计信息说明如下：

|  统计项   |  说明  |
| -----|-----|
|  BYTES_EXPECTED  | 根据源目录统计的需拷贝的文件总大小，单位：字节   |
|  FILES_EXPECTED  | 根据源目录统计的需拷贝文件数，包含目录文件   |
|  BYTES_SKIPPED  | 长度或校验和值相等，不拷贝的文件总大小，单位：字节  |
|  FILES_SKIPPED  | 长度或校验和值相等，不拷贝的源文件数  |
|  FILES_COPIED  | 拷贝成功的源文件数   |
|  FILES_FAILED  | 拷贝失败的源文件数   |
|  FOLDERS_COPIED  | 拷贝成功的目录数   |
|  FOLDERS_SKIPPED  | 跳过的目录数   |


### 指定拷贝进程数以及每个拷贝进程内的拷贝线程数

以参数`--taskNumber`和`--workersNumber`执行命令，COSDistCp 采用多进程+多线程的拷贝架构，您可以：
- 通过 `--taskNumber` 指定拷贝进程数目
- 通过 `--workerNumber` 指定每个拷贝进程内的拷贝线程数

```plaintext
hadoop jar cos-distcp-${version}.jar --src /data/warehouse/ --dest cosn://examplebucket-1250000000/data/warehouse --taskNumber=10 --workerNumber=5
```

### 跳过具有相同校验值文件，进行增量迁移

以参数`--skipMode`执行命令。跳过源和目标具有相同长度和校验和文件的拷贝，默认值 length-checksum：
```plaintext
hadoop jar cos-distcp-${version}.jar  --src /data/warehouse --dest cosn://examplebucket-1250000000/data/warehouse  --skipMode=length-checksum
```

`--skipMode`选项用于在拷贝文件前，校验源文件和目标文件是否相同，若相同则跳过，可选 none（不校验）、length（长度）、checksum（CRC 值）和 length-checksum（长度 + CRC 值）。

如果源和目标文件系统的校验和算法不同，则会读取源端文件计算新的校验和。如果您的源是 HDFS，您可以通过如下方式，确定 HDFS 源是否支持 COMPOSITE-CRC32C 校验算法：

```plaintext
hadoop fs  -Ddfs.checksum.combine.mode=COMPOSITE_CRC -checksum /data/test.txt
/data/test.txt  COMPOSITE-CRC32C        6a732798
```

### 迁移完成后的数据校验及增量迁移

以参数`--diffMode`和`--diffOutput`执行命令：
- `--diffMode` 可选值为 length 和 length-checksum。
 - `--diffMode=length`表示根据文件大小是否相同，获取差异文件列表。
 - `--diffMode=length-checksum`，根据文件大小和 CRC 检验和是否相同，获取差异文件列表。
- `--diffOutput` 指定 diff 操作的输出目录。

如果目标文件系统为 COS，且源文件系统的 CRC 算法与之不同，则 COSDistCp 会拉取源文件计算目的文件系统的 CRC，以进行相同 CRC 算法值的对比。以下示例中，在迁移完成后，使用 --diffMode 参数，根据文件大小和 CRC 值，校验源和目标文件是否相同：

```plaintext
hadoop jar cos-distcp-${version}.jar --src /data/warehouse --dest cosn://examplebucket-1250000000/data/warehouse/ --diffMode=length-checksum --diffOutput=/tmp/diff-output
```

以上命令执行成功后，会输出以源文件系统文件列表为基准的计数器信息，您可以根据计数器信息，分析源和目的是否相同，计数器信息说明如下：

1. 源和目的文件相同，记录为 SUCCESS
2. 目标文件不存在，记录为 DEST_MISS
3. 存在源目录的清单中，但是校验时源文件不存在，记录为 SRC_MISS
4. 源文件和目标文件大小不同，记录为：LENGTH_DIFF
5. 源文件和目标文件 CRC 算法值不同，记录为：CHECKSUM_DIFF
6. 由于读取权限不够等因素导致 diff 操作失败，记录为：DIFF_FAILED
7. 源为目录，目的为文件，记录为：TYPE_DIFF

此外，COSDistcp 会在 HDFS 的 `/tmp/diff-output/failed` 目录下（低版本为 /tmp/diff-output），生成差异文件列表，您可以通过如下命令，获取除 SRC_MISS 以外的差异文件列表：

```plaintext
hadoop fs -getmerge /tmp/diff-output/failed diff-manifest
grep -v '"comment":"SRC_MISS"' diff-manifest |gzip > diff-manifest.gz
```

执行如下命令，根据差异文件列表进行增量迁移：

```plaintext
hadoop  jar cos-distcp-${version}.jar --taskNumber=20 --src /data/warehouse --dest cosn://examplebucket-1250000000/data/warehouse/ --previousManifest=file:///usr/local/service/hadoop/diff-manifest.gz --copyFromManifest
```
增量迁移完成后，再次运行带 --diffMode 参数的命令，校验文件是否完全一致。

### 校验源文件和目标文件是否具有相同 CRC

以参数`--checkMode`执行命令，文件拷贝完成时，校验源文件和目标文件长度及校验和是否一致，默认值 length-checksum。

从非 COS 文件系统同步到 COS 时，如果源的 CRC 算法和 Hadoop-COS 的 CRC 算法不一致，则拷贝时计算 CRC，并在拷贝完成后，获取目标 COS 文件的 CRC，和计算得到的源文件 CRC 对比校验：

```plaintext
hadoop jar cos-distcp-${version}.jar   --src /data/warehouse --dest cosn://examplebucket-1250000000/data/warehouse --checkMode=length-checksum
```
>! 在未指定 --groupBy，且 --outputCodec 为默认值时生效。


### 限制单文件读取带宽

以参数`--bandWidth`执行命令，数值单位为MB。限制每个迁移文件的读取带宽为10MB/s，示例如下：

```plaintext
hadoop jar cos-distcp-${version}.jar  --src /data/warehouse --dest cosn://examplebucket-1250000000/data/warehouse --bandWidth=10
```

### 多目录同步

新建一个本地文件（例如 srcPrefixes.txt），在该文件中添加需要迁移的多个目录的绝对路径，这些目录之间需要不存在父子关系，添加之后，可通过 cat 命令查看，示例如下：

```plaintext
cat srcPrefixes.txt 
/data/warehouse/20181121/
/data/warehouse/20181122/
```

使用 `--srcPrefixesFile` 参数指定该文件，执行迁移命令：

```plaintext
hadoop jar  cos-distcp-${version}.jar --src /data/warehouse  --srcPrefixesFile file:///usr/local/service/hadoop/srcPrefixes.txt --dest  cosn://examplebucket-1250000000/data/warehouse/ --taskNumber=20
```

### 对输入文件进行正则表达式过滤

以参数`--srcPattern`执行命令，只同步 `/data/warehouse/logs` 目录下，以 .log 结尾的日志文件，示例如下：

```plaintext
hadoop jar cos-distcp-${version}.jar  --src /data/warehouse/logs --dest cosn://examplebucket-1250000000/data/warehouse --srcPattern='.*/logs/.*\.log'
```

### 指定 Hadoop-COS 的文件检验和类型

以参数`--cosChecksumType`执行命令，默认 CRC32C，可选 CRC32C 和 CRC64。

```plaintext
hadoop jar cos-distcp-${version}.jar  --src /data/warehouse --dest cosn://examplebucket-1250000000/data/warehouse --cosChecksumType=CRC32C
```

### 指定 COS 文件的存储类型

以参数`--storageClass`执行命令，示例如下：

```plaintext
hadoop jar cos-distcp-${version}.jar --src /data/warehouse --dest cosn://examplebucket-1250000000/data/warehouse/ --outputManifest=manifest-2020-01-10.gz --storageClass=STANDARD_IA
```


### 指定目标文件的压缩类型

以参数`--outputCodec`执行命令，您可通过该参数，将 HDFS 中的数据实时压缩备份到 COS，节省存储成本。参数可选值为：keep、none、gzip、lzop、snappy，none 选项保存的目标文件为未压缩状态，keep 保持原来文件的压缩状态。示例如下：

```plaintext
hadoop jar cos-distcp-${version}.jar --src /data/warehouse/logs --dest cosn://examplebucket-1250000000/data/warehouse/logs-gzip --outputCodec=gzip
```

>! 其中除 keep 选项外，皆会先对文件先解压，随后转换为目标压缩类型。因此，除 keep 选项外，可能会由于压缩参数等不一致，导致目标文件和源文件不一致，但解压后的文件一致；在未指定 --groupBy，且 --outputCodec 为默认值时，可通过 --checkMode 进行数据校验。
>

### 删除源文件

以参数`--deleteOnSuccess`执行命令，将 `/data/warehouse`目录下文件从 HDFS 同步到 COS 后，立即删除源目录中的对应文件：

```plaintext
hadoop jar cos-distcp-${version}.jar --src /data/warehouse --dest cosn://examplebucket-1250000000/data/warehouse --deleteOnSuccess
```

>! 指定该选项后每迁移完一个文件，立即删除对应的源文件，并非整个迁移完成后，再删除源文件，请谨慎使用，1.7 及其以后版本不再提供该参数。
>

### 生成目标清单文件和指定上一次清单输出文件

以参数`--outputManifest` 和`--previousManifest`执行命令。

- `--outputManifest` 该选项首先会在本地生成一个 gzip 压缩的 manifest.gz，并在迁移成功时，移动到 `--dest` 所指定的目录下。
- `--previousManifest` 指定上一次 `--outputManifest` 输出文件，COSDistCp 会跳过相同长度大小的文件：

```plaintext
hadoop jar cos-distcp-${version}.jar --src /data/warehouse --dest  cosn://examplebucket-1250000000/data/warehouse/ --outputManifest=manifest.gz --previousManifest= cosn://examplebucket-1250000000/data/warehouse/manifest-2020-01-10.gz
```

>! 上述命令的增量迁移，只能同步文件大小变化的文件，无法同步文件内容发生变化的文件。如果文件内容可能发生变化，请参考 --diffMode 使用示例，根据文件的 CRC 确定文件发生变化的文件列表。
>


### 指定迁移任务分配策略为动态分配

如果您的文件分布情况是文件大小分化剧烈，例如极少量超大文件，大量小文件或者迁移机器负载不一。您可以通过 `--enableDynamicStrategy` 开启任务动态分配策略，使执行速度快的任务，迁移更多的文件，从而减少任务的执行时间：

```plaintext
hadoop jar cos-distcp-${version}.jar --src /data/warehouse    --dest  cosn://examplebucket-1250000000/data/warehouse --enableDynamicStrategy
```
迁移完成后对迁移的数据进行校验：
```
hadoop jar cos-distcp-${version}.jar --src /data/warehouse --dest cosn://examplebucket-1250000000/data/warehouse/ --diffMode=length-checksum --diffOutput=/tmp/diff-output
```

>! 该模式存在一定局限性，例如任务计数器在进程异常的情况下，可能计数不准确，请迁移完成后用 --diffMode 对数据进行校验。
>

### 拷贝文件的元信息

以参数`--preserveStatus`执行命令，将源文件或源目录的 user、group、permission 和 timestamps（modification time 和 access time）拷贝到目标文件或目标目录，该参数在将文件从 HDFS 拷贝到 CHDFS 时生效。
示例如下：
```plaintext
hadoop jar cos-distcp-${version}.jar --src /data/warehouse --dest cosn://examplebucket-1250000000/data/warehouse/ --preserveStatus=ugpt
```


### 配置 Prometheus 监控

您可以在 Yarn 的管理页面，查看 COSDistcp 迁移任务的计数器，包括当前已经迁移完成的文件数、字节数等信息。为了更方便地查看迁移任务计数器的曲线变化，您只需要简单的配置，即可将 COSDistcp 迁移任务的计数器展示在 Prometheus + Grafana 监控体系中，配置 prometheus.yml，添加抓取任务：

```plaintext
- job_name: 'cos-distcp-hive-backup'
    static_configs:
      - targets: ['172.16.16.139:9028']
```

以参数 `--promPort=VALUE` 执行命令，将当前 MapReduce 任务的计数器暴露到外部：

```plaintext
hadoop jar cos-distcp-${version}.jar  --src /data/warehouse --dest cosn://examplebucket-1250000000/data/warehouse --promPort=9028
```

下载示例 [Grafana Dashboard](https://cos-sdk-archive-1253960454.file.myqcloud.com/cos-distcp/COSDistcp-Grafana-Dashboard.json) 并导入，Grafana 展示如下：
![COSDistcp-Grafana](https://main.qcloudimg.com/raw/a5eb4c66c52b3fb09cafc5d4196e9d22.png)


### 拷贝文件失败时告警
以参数`--completionCallbackClass`指定回调类路径执行命令，COSDistCp 会在拷贝任务完成的时候， 将收集的任务信息作为参数执行回调函数。用户自定义的回调函数，需要实现如下接口，前往 [下载回调示例代码](https://cos-sdk-archive-1253960454.file.myqcloud.com/cos-distcp/cos-distcp-alarm-1.0.jar)：

```plaintext
package com.qcloud.cos.distcp;
import java.util.Map;
public interface TaskCompletionCallback {
/**
 * @description: When the task is completed, the callback function is executed
 * @param jobType Copy or Diff
 * @param jobStartTime  the job start time
 * @param errorMsg  the exception error msg
 * @param applicationId the MapReduce application id
 * @param: cosDistCpCounters the job 
*/

void doTaskCompletionCallback(String jobType, long jobStartTime, String errorMsg, String applicationId, Map<String, Long> cosDistCpCounters);

/**
 *  @description: init callback config before execute
 */
void init() throws Exception;
}
```

COSDistCp 内部集成了云监控的告警，在任务出现异常及存在文件拷贝失败的时候，执行告警：

```plaintext
export alarmSecretId=SECRET-ID
export alarmSecretKey=SECRET-KEY
export alarmRegion=ap-guangzhou
export alarmModule=module
export alarmPolicyId=cm-xxx
hadoop jar cos-distcp-1.4-2.8.5.jar \
-Dfs.cosn.credentials.provider=org.apache.hadoop.fs.auth.SimpleCredentialProvider \
-Dfs.cosn.userinfo.secretId=SECRET-ID \
-Dfs.cosn.userinfo.secretKey=SECRET-KEY \
-Dfs.cosn.bucket.region=ap-guangzhou \
-Dfs.cosn.impl=org.apache.hadoop.fs.CosFileSystem \
-Dfs.AbstractFileSystem.cosn.impl=org.apache.hadoop.fs.CosN \
--src /data/warehouse \
--dest cosn://examplebucket-1250000000/data/warehouse/ \
--checkMode=checksum \
--completionCallbackClass=com.qcloud.cos.distcp.DefaultTaskCompletionCallback
```

以上命令中 alarmPolicyId 为云监控告警策略，可进入云监控控制台进行创建和配置（告警管理 > 告警配置 > 自定义消息）。



## 常见问题
### 使用 COSDistcp 迁移 HDFS 数据包含哪些阶段，如何调整迁移性能和保障数据的正确性？
您可以执行如下两个阶段的命令，以保障数据的准确性，首先执行如下的命令进行迁移：
```
hadoop jar cos-distcp-${version}.jar --src /data/warehouse --dest cosn://examplebucket-1250000000/data/warehouse --taskNumber=20
```
迁移完成后，执行如下的命令，查看源和目的的差异文件列表：
```
hadoop jar cos-distcp-${version}.jar --src /data/warehouse --dest cosn://examplebucket-1250000000/data/warehouse/ --diffMode=length-checksum --diffOutput=/tmp/diff-output
```

### 环境中未配置 Hadoop-COS, 如何运行 COSDistCp?

对于环境中未配置 Hadoop-COS 插件的用户，根据 Hadoop 版本，下载对应版本的 COSDistCp jar 包后，指定 Hadoop-COS 相关参数执行拷贝任务：

```plaintext
hadoop jar cos-distcp-${version}.jar \
-Dfs.cosn.credentials.provider=org.apache.hadoop.fs.auth.SimpleCredentialProvider \
-Dfs.cosn.userinfo.secretId=COS_SECRETID \
-Dfs.cosn.userinfo.secretKey=COS_SECRETKEY \
-Dfs.cosn.bucket.region=ap-guangzhou \
-Dfs.cosn.impl=org.apache.hadoop.fs.CosFileSystem \
-Dfs.AbstractFileSystem.cosn.impl=org.apache.hadoop.fs.CosN \
--src /data/warehouse \
--dest cosn://examplebucket-1250000000/warehouse
```

### 拷贝结果显示部分文件拷贝失败，如何处理？

COSDistCp 会对文件拷贝过程中出现的 IOException 重试五次，五次拷贝仍然失败，会将失败的文件信息写入 `/tmp/${randomUUID}/output/failed/` 目录下，其中，${randomUUID} 为随机字符串。常见的拷贝失败原因包括：
1. 源文件存在拷贝清单中，但是拷贝时源文件不存在，记录为 SRC_MISS。
2. 任务发起的用户，不具备读取源文件或写入目标文件的权限，以及其他原因，记录为 COPY_FAILED。

如果日志信息记录源文件不存在，且源文件确实可以忽略，您可以通过如下命令，获取除 SRC_MISS 以外的差异文件列表：
```plaintext
hadoop fs -getmerge /tmp/${randomUUID}/output/failed/ failed-manifest
grep -v '"comment":"SRC_MISS"' failed-manifest |gzip > failed-manifest.gz
```
如果存在除 SRC_MISS 以外的失败文件，您可以根据汇总在  `/tmp/${randomUUID}/output/logs/` 目录下的异常日志信息和拉取应用日志诊断原因，例如拉取 yarn 应用的日志，可使用如下命令：
```plaintext
yarn logs -applicationId application_1610615435237_0021 > application_1610615435237_0021.log
```
其中 application_1610615435237_0021 为应用 ID。

### COSDistCp 是否会在网络等异常情况下，拷贝生成不完整文件？

在网络异常、源文件缺失和权限不足等情况下，COSDistCp 无法在目标端生成和源端同样大小的文件。
- 对于 COSDistCp 1.5 以下版本，COSDistCp 会尝试删除生成在目标端文件。如果删除失败，则需要您重新执行拷贝任务覆盖这些文件，或者手动删除这些不完整的文件。
- 对于 COSDistCp 1.5 及以上版本，且运行环境的 Hadoop COS 插件版本在 5.9.3 及以上版本时，如果拷贝到 COS 拷贝失败，COSDistCp 会调用 abort 接口终止正在上传的请求。因此，即使遇到异常情况，也不会生成不完整的文件。
- 对于 COSDistCp 1.5 及以上版本，如果运行环境的 Hadoop COS 插件版本低于 5.9.3，建议升级到 5.9.3 及其以上版本。
- 对于非 COS 的目标端，COSDistCp 会尝试删除目标端文件。

### COS 存储桶中存在一些看不见的未完成上传文件，占用存储空间，如何处理？
由于机器异常、进程被 Kill 等因素，可能导致 COS 存储桶中存在一些碎片文件占用存储空间，您可参考官网 [生命周期文档](https://cloud.tencent.com/document/product/436/14605) 配置碎片删除规则，进行清理。
