## 功能说明

COSDistcp 是一款基于 MapReduce 的分布式文件拷贝工具，主要用于 HDFS 和 COS 之间的数据拷贝，COSDistcp 提供文件过滤、压缩和文件聚合等实用拷贝功能，同时基于 COS 支持的特性，COSDistcp 工具还可提供 CRC 增量拷贝、数据实时检验功能。

## 使用环境

#### 系统环境

支持 Linux 系统。

#### 软件依赖

Hadoop-2.6.0及以上版本、Hadoop-COS 插件 5.8.7 及以上版本。

## 下载与安装

#### 获取 COSDistcp jar 包

下载 [cos-distcp-1.0.jar 包](https://cos-sdk-archive-1253960454.file.myqcloud.com/cos-distcp/cos-distcp-1.0.jar) 。

#### 安装说明

在 Hadoop 环境下，安装 [Hadoop-COS](https://cloud.tencent.com/document/product/436/6884?!preview&!editLang=zh#.E4.B8.8B.E8.BD.BD.E4.B8.8E.E5.AE.89.E8.A3.85) 后，即可直接运行 COSDistcp 工具。


## 原理说明

COSDistcp 基于 MapReduce 框架实现，在 Mapper 中对文件进行分组，在 Reducer 进程中使用多线程对文件进行拷贝、压缩和数据校验等工作。当文件迁移或校验失败的时候，任务可能会执行失败。当迁移失败时，您可使用 diff 模式，通过对比文件的 CRC 校验值，实现文件的增量迁移。


## 参数说明

您可使用命令 `hadoop jar cos-distcp-1.0.jar --help` 查看 COSDistcp 支持的参数选项，以下为 COSDistcp 参数说明：


|                  属性键                  | 说明                                                         |                            默认值                            | 必填项 |
| :--------------------------------------: | :----------------------------------------------------------- | :----------------------------------------------------------: | :----: |
|          --help          | 输出 COSDistcp 支持的参数选项<br> 示例：--help |                              无                              |   否   |
|          --src=LOCATION          | 指定拷贝的源目录，可以是 HDFS 或者 COS 路径<br> 示例：--src=hdfs://user/logs/ |                              无                              |   是   |
|         --dest=LOCATION          | 指定拷贝的目标目录，可以是 HDFS 或者 COS 路径<br> 示例：--dest=cosn://examplebucket-1250000000/user/logs |       无       |   是   |
|       --srcPattern=PATTERN       | 指定正则表达式对源目录中的文件进行过滤<br>示例：`--srcPattern='.*.log'`<br>**注意：您需要将参数使用单引号包围，以避免符号`*`被 shell 解释**。 | 无 | 否 |
|       --reducerNumber=VALUE       | 指定 reducer 进程数目<br>示例：--reducerNumber=10 |                             10                             |   否   |
|       --workerNumber=VALUE       | 指定每个 reducer 中的拷贝线程数，COSDistcp 在每个 reducer 中创建该参数大小的拷贝线程池<br>示例：--workerNumber=10 |                             10                             |   否   |
|      --filesPerMapper=VALUE      | 指定每个 Mapper 输入文件的行数<br>示例：--filesPerMapper=10000 |                              500000                              |   否   |
|         --groupBy=PATTERN   | 指定正则表达式对文件进行聚合<br>示例：--groupBy='.\*group-input/(\d+)-(\d+).*'                              |                              无                              |   否   |
|        --targetSize=VALUE        | 指定目标文件的大小，单位:MB，与--groupBy一起使用<br>示例：--targetSize=10              |                              无                              |   否   |
|       --outputCodec=VALUE        | 指定输出文件的压缩方式，可选 gzip、lzo、snappy、none 和 keep, 其中：<br> 1. keep 保持原有文件的压缩方式<br>2. none 则根据文件后缀对文件进行解压<br>示例：--outputCodec=gzip | keep | 否 |
|        --deleteOnSuccess         | 指定源文件拷贝到目标目录成功时，立即删除源文件<br>示例：--deleteOnSuccess | false | 否 |
| --multipartUploadChunkSize=VALUE | 指定 Hadoop-COS 插件传输文件到 COS 时分块的大小，COS 支持的最大分块数为 10000，您可根据文件大小，调整分块大小，单位：MB，默认为8MB<br>示例：--multipartUploadChunkSize=20 | 8MB |   否   |
|    --cosServerSideEncryption     | 指定文件上传到 COS 时，使用 SSE-COS 作为加解密算法<br />示例：--cosServerSideEncryption | false | 否 |
|      --outputManifest=VALUE      | 指定拷贝完成的时候，在目标目录下生成本次拷贝到目标文件信息列表（GZIP 压缩）<br>示例：--outputManifest=manifest.gz | 无 | 否 |
|    --requirePreviousManifest     | 要求指定 --previousManifest=VALUE 参数，以进行增量拷贝<br>示例：--requirePreviousManifest |     false      | 否 |
|     --previousManifest=LOCATION     | 前一次拷贝生成的目标文件信息<br>示例：--previousManifest=cosn://examplebucket-1250000000/big-data/manifest.gz |                        无                        |   否   |
|        --copyFromManifest        | 和 --previousManifest=LOCATION 一起使用，可将 --previousManifest 中的文件，拷贝到目标文件系统<br>示例：--copyFromManifest |                   false                   |   否   |
| --storageClass=VALUE | 指定对象存储类型，可选值为 STANDARD、STANDARD_IA、ARCHIVE、DEEP_ARCHIVE、INTELLIGENT_TIERING，关于更多支持的存储类型和介绍，请参见 [存储类型概述](https://cloud.tencent.com/document/product/436/33417)  |                        无                        |   否   |
|        --srcPrefixesFile=LOCATION        | 指定本地文件，该文件中每行包含一个需要拷贝的源目录<br/>示例：--srcPrefixesFile=file:///data/migrate-folders.txt |                              无                              |   否   |
|         --enableCrcCheck         | 当文件拷贝完成的时候，校验源文件和目的文件的 CRC 是否相同，注意：除拷贝到 COS 外，源文件系统和目标文件系统支持相同 CRC 算法，该参数才生效<br/>示例：--enableCrcCheck |       false   |    否   |    
|      --skipCopySameCrcFile       | 指定跳过源和目的具有相同 CRC 值和相同大小的文件，以进行增量拷贝<br>注意：源和目的支持相同 CRC 算法时，该参数才生效<br>示例：--skipCopySameCrcFile |                              无                              |   否   |
|         --diffMode=MODE         | 指定获取差异文件列表的准则，可选 length （长度）和 length-checksum（长度 + CRC 值）<br/>示例：--diffMode=length-checksum |                              无                              |   否   |
|      --diffOutput=LOCATION       | 指定差异文件列表的输出目录，该输出目录必须为空<br/>示例：--diffOutput=/diff-output            |     无     |   否   |
|     --cosChecksumType=TYPE     | 指定 Hadoop-COS 插件使用的 CRC 算法，可选值为 CRC32C 和 CRC64<br/>示例：--cosChecksumType=CRC32C | CRC32C | 否 |


## 使用示例

### 查看 help 选项

以参数`--help`执行命令，查看 COSDistcp 支持的参数，示例如下：

```plaintext
hadoop jar cos-distcp-1.0.jar --help
```

### 指定待迁移文件的源目录和目标目录

以参数`--src` 和 `--dest`执行命令，示例如下：

```plaintext
hadoop jar cos-distcp-1.0.jar --src /data/warehouse --dest cosn://examplebucket-1250000000/data/warehouse
```

### 对输入文件进行正则表达式过滤

以参数`--srcPattern`执行命令，只同步 `/data/warehouse/logs` 目录下，以 .log 结尾的日志文件，示例如下：

```plaintext
hadoop jar cos-distcp-1.0.jar  --src /data/warehouse/logs --dest cosn://examplebucket-1250000000/data/warehouse --srcPattern='.*/logs/.*\.log'
```

### 指定 reducer 数目以及每个 reducer 进程内拷贝线程数

以参数`--reducerNumber`和`--workersNumber`执行命令，COSDistcp 采用多进程+多线程的拷贝架构，您可以：
- 通过 `--reducerNumber` 指定 reducer 进程数目
- 通过 `--workerNumber` 指定每个 reducer 内的拷贝线程数

```plaintext
hadoop jar cos-distcp-1.0.jar --src /data/warehouse/ --dest cosn://examplebucket-1250000000/data/warehouse --reducerNumber=10 --workerNumber=10
```

### 删除源文件

以参数`--deleteOnSuccess`执行命令，将 `/data/warehouse`目录下文件从 HDFS 同步到 COS 后，立即删除源目录中的对应文件：

```plaintext
hadoop jar cos-distcp-1.0.jar --src /data/warehouse --dest cosn://examplebucket-1250000000/data/warehouse --deleteOnSuccess
```

>!指定该选项后每迁移完一个文件，立即删除对应的源文件，并非整个迁移完成后，再删除源文件，请谨慎使用。

### 限制单文件读取带宽

以参数`--bandWidth`执行命令，数值单位为MB。限制每个迁移文件的读取带宽为 10MB/s，示例如下：

```plaintext
hadoop jar cos-distcp-1.0.jar  --src /data/warehouse --dest cosn://examplebucket-1250000000/data/warehouse --bandWidth=10
```

### 指定 Hadoop-COS 的文件检验和类型

以参数`--cosChecksumType`执行命令，默认 CRC32C，可选 CRC32C 和 CRC64。

```plaintext
hadoop jar cos-distcp-1.0.jar  --src /data/warehouse --dest cosn://examplebucket-1250000000/data/warehouse --cosChecksumType=CRC32C
```

### 跳过具有相同 CRC 的文件

以参数`--skipCopySameCrcFile`执行命令。该选项仅在源和目标文件系统具有相同 CRC 算法实现时生效，否则仍然会拷贝文件。如果您的源是 HDFS，您可以通过如下方式，确定 HDFS 源是否支持 COMPOSITE-CRC32C 校验算法：

```plaintext
hadoop fs  -Ddfs.checksum.combine.mode=COMPOSITE_CRC -checksum /data/test.txt
/data/test.txt  COMPOSITE-CRC32C        6a732798
```

当您的 HDFS 源支持 COMPOSITE-CRC32C 算法，则您可以通过 `--skipCopySameCrcFile` 参数跳过 COS 中，具有相同 CRC32C 的文件，示例如下：

```plaintext
hadoop jar cos-distcp-1.0.jar  --src /data/warehouse --dest cosn://examplebucket-1250000000/data/warehouse  --skipCopySameCrcFile
```

### 校验源文件和目标文件是否具有相同 CRC

以参数`--enableCrcCheck`执行命令，文件拷贝完成时，校验源文件和目标文件是否具有相同 CRC。

从非 COS 文件系统同步到 COS 时，如果源的 CRC  算法和 Hadoop-COS 的 CRC 算法不一致，则拷贝的同时，将实时计算 CRC，并在拷贝完成后，获取目的 COS 文件的 CRC，和计算得到的 CRC 对比校验。拷贝目标为非 COS 的文件系统，仅在源文件系统和目标文件系统，具有相同 CRC 算法实现时，该选项会生效，否则校验失败。示例如下：

```plaintext
hadoop jar cos-distcp-1.0.jar   --src /data/warehouse --dest cosn://examplebucket-1250000000/data/warehouse --enableCrcCheck
```

### 指定目标文件的压缩类型

以参数`--outputCodec`执行命令，您可通过该参数，将 HDFS 中的数据实时压缩备份到 COS，节省存储成本。参数可选值为：keep、none、gzip、lzop、snappy，none 选项保存的目标文件为未压缩状态，keep 保持原来文件的压缩状态。示例如下：

```plaintext
hadoop jar cos-distcp-1.0.jar --src /data/warehouse/logs --dest cosn://examplebucket-1250000000/data/warehouse/logs-gzip --outputCodec=gzip
```

>!其中除 keep 选项外，皆会先对文件先解压，随后转换为目的压缩类型，因此，除 keep 选项外，可能会由于压缩参数等不一致，导致目标文件和源文件不一致，但解压后的文件一致。

### 多目录同步

新建一个本地文件（例如 srcPrefixes.txt），在该文件中添加需要迁移的多个目录，添加之后，可通过 cat 命令查看，示例如下：

```plaintext
cat srcPrefixes.txt 
/data/warehouse/20181121/
/data/warehouse/20181122/
```

使用 `--srcPrefixesFile` 参数指定该文件，执行迁移命令：

```plaintext
hadoop jar  cos-distcp-1.0.jar --src /data/warehouse  --srcPrefixesFile file:///usr/local/service/hadoop/srcPrefixes.txt --dest  cosn://examplebucket-1250000000/data/warehouse/ --reducerNumber=20
```

### 生成目的清单文件和指定上一次清单输出文件

以参数`--outputManifest` 和`--previousManifest`执行命令。

- `--outputManifest` 该选项首先会在本地生成一个 gzip 压缩的 manifest.gz，并在迁移成功时，移动到 `--dest` 所指定的目录下。
- `--previousManifest` 指定上一次 `--outputManifest` 输出文件，COSDistcp 会跳过相同长度大小的文件：

```plaintext
hadoop jar cos-distcp-1.0.jar --src /data/warehouse --dest  cosn://examplebucket-1250000000/data/warehouse/ --outputManifest=manifest.gz --previousManifest= cosn://examplebucket-1250000000/data/warehouse/manifest-2020-01-10.gz
```

>!上述命令的增量迁移，只能同步文件大小变化的文件，无法同步文件内容发生变化的文件。如果文件内容可能发生变化，请参考 --diffMode 使用示例，根据文件的 CRC 确定文件发生变化的文件列表。

### 根据 CRC 获取差异文件列表和增量迁移

以参数`--diffMode`和`--diffOutput`执行命令：
- `--diffMode` 可选值为 length 和 length-checksum。
 - `--diffMode=length`表示根据文件大小是否相同，获取差异文件列表。
 - `--diffMode=length-checksum`，根据文件大小和 CRC 检验和是否相同，获取差异文件列表。
- `--diffOutput` 指定 diff 操作的输出目录。

以下示例中，根据文件大小和 CRC 值校验源和目的文件是否相同， 指定 mapred.max.split.size 为 100KB：

```plaintext
hadoop jar cos-distcp-1.0.jar -Dmapred.max.split.size=102400  --src /data/warehouse --dest cosn://examplebucket-1250000000/data/warehouse/ --diffMode=length-checksum --diffOutput=/tmp/diff-output
```

>!如果目的文件系统为 COS，且源文件系统的 CRC 算法与之不同，则 COSDistcp 会拉取源文件计算新的 CRC，以进行相同 CRC 算法值的对比。

以上命令执行成功后，会在 HDFS 的 `/tmp/diff-output` 目录下，生成差异文件列表，以下类型的源文件信息包含在输出中：

1. 源文件系统存在，目标文件系统不存在
2. 源文件系统和目标文件系统大小不同
3. 源文件系统和目标文件系统 CRC 算法或值不同

您可以通过如下命令，合并差异文件列表：

```plaintext
hadoop fs -getmerge /tmp/diff-output diff-manifest
gzip diff-manifest
```

执行如下命令，根据差异文件列表进行增量迁移：

```plaintext
hadoop  jar cos-distcp-1.0.jar --reducerNumber=20 --src /data/warehouse --dest cosn://examplebucket-1250000000/data/warehouse/ --previousManifest=file:///usr/local/service/hadoop/diff-manifest.gz –copyFromManifest
```

### 指定 COS 文件的存储类型

以参数`--storageClass`执行命令，示例如下：

```plaintext
hadoop jar cos-distcp-1.0.jar --src /data/warehouse --dest cosn://examplebucket-1250000000/data/warehouse/ --outputManifest=manifest-2020-01-10.gz --storageClass=STANDARD_IA
```
