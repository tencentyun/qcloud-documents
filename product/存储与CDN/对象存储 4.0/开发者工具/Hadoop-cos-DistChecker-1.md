## 功能说明

Hadoop-cos-DistChecker 是一个校验迁移目录完整性的工具。用户在使用`hadoop distcp`命令从 HDFS 迁移数据到 COS 上后，基于 MapReduce 的并行能力，Hadoop-cos-DistChecker 工具可以快速地进行**源目录**和**目标目录**的校验比对。

## 使用环境

- Hadoop-cos v5.8.2以上，详见 [hadoop-cos release](https://github.com/tencentyun/hadoop-cos/releases)。
- Hadooop MapReduce 的运行环境。

> !
> - 如果是自建 Hadoop 集群，则 Hadoop-cos 依赖需要选择最新版本（GitHub release 版本为5.8.2以上）才能支持 CRC64校验码的获取。
> - 如果是使用腾讯云 EMR 套件，则2020年5月8日后创建的集群才包含该 Hadoop-cos 版本，早于这个时间创建的集群，需要 [提交工单](https://console.cloud.tencent.com/workorder/category) 处理。

## 使用说明

由于 Hadoop-cos-distchecker 需要获取 Hadoop-cos（CosN 文件系统）中的文件 CRC64校验值，因此，在运行该工具以前，需要将配置项fs.cosn.crc64.checksum.enabled置为true以支持获取 Hadoop-cos文件的 CRC64校验和，待工具运行完成后，再将该选项置回false以关闭 CRC64校验和的获取。

> !由于 Hadoop-COS 支持的 CRC64校验和与 HDFS 文件系统的 CRC32C 校验和无法兼容，因此在使用完该工具以后，务必将上述配置项恢复为关闭状态，否则可能会导致 Hadoop-cos 在某些调用文件系统 getFileChecksum 接口的场景下运行失败。

### 参数概念

- **源文件列表**
  源文件路径列表是用户执行以下命令，导出的待检查的子目录和文件列表。

```plaintext
hadoop fs -ls -R hdfs://host:port/{source_dir} | awk '{print $8}' > check_list.txt
```

示例格式如下：

```plaintext
/benchmarks/TestDFSIO
/benchmarks/TestDFSIO/io_control
/benchmarks/TestDFSIO/io_control/in_file_test_io_0
/benchmarks/TestDFSIO/io_control/in_file_test_io_1
/benchmarks/TestDFSIO/io_data
/benchmarks/TestDFSIO/io_data/test_io_0
/benchmarks/TestDFSIO/io_data/test_io_1
/benchmarks/TestDFSIO/io_write
/benchmarks/TestDFSIO/io_write/_SUCCESS
/benchmarks/TestDFSIO/io_write/part-00000
```

- **源目录**：指源文件列表所在的目录，这个目录通常也是`distcp`命令进行数据迁移时的源路径。如下所示，`hdfs://host:port/source_dir`为源目录。

```plaintext
hadoop distcp hdfs://host:port/source_dir cosn://examplebucket-appid/dest_dir
```

此外，这个路径也是**源文件路径列表**中公共父目录，例如上述的源文件列表的公共父目录就是：`/benchmarks`。

- **目标目录**：待比较的目标目录。

### 命令行格式

Hadoop-cos-DistChecker 是一个 MapReduce 作业程序，按照 MapReduce 作业的提交流程即可：

```plaintext
hadoop jar hadoop-cos-distchecker-2.8.5-1.0-SNAPSHOT.jar com.qcloud.cos.hadoop.distchecker.App <源文件列表的绝对路径> <源目录的绝对路径表示> <目标目录的绝对路径表示> [optional parameters]
```

> ? Optional parameters 表示 Hadoop 可选参数。

### 使用步骤

下面以校验` hdfs://10.0.0.3:9000/benchmarks`和`cosn://hdfs-test-1250000000/benchmarks`为例，介绍工具的使用步骤。

首先，执行以下命令。

```plaintext
hadoop fs -ls -R hdfs://10.0.0.3:9000/benchmarks | awk '{print $8}' > check_list.txt
```

![](https://main.qcloudimg.com/raw/a2a853be2646b6558983303de805c04e.png)
将待检查源路径导出到一个 check_list.txt 的文件中，这个文件里面保存的就是源文件路径列表，如下所示：
![](https://main.qcloudimg.com/raw/216d90b20d383e233e50f497e83c24c3.png)

然后，将 check_list.txt 放入到 HDFS 中，执行如下。

```plaintext
hadoop fs -put check_list.txt hdfs://10.0.0.3:9000/
```

![](https://main.qcloudimg.com/raw/e5b79519dfeac808b64f29e04c35e9a4.png)

最后，执行 Hadoop-cos-DistChecker，将`hdfs://10.0.0.3:9000/benchmarks`和`cosn://hdfs-test-1250000000/benchmarks`进行对比，然后输出结果保存到`cosn://hdfs-test-1250000000/check_result`路径下，命令格式如下：

```shell
hadoop jar hadoop-cos-distchecker-2.8.5-1.0-SNAPSHOT.jar com.qcloud.cos.hadoop.distchecker.App hdfs://10.0.0.3:9000/check_list.txt hdfs://10.0.0.3:9000/benchmarks cosn://hdfs-test-1250000000/benchmarks cosn://hdfs-test-1250000000/check_result
```

![](https://main.qcloudimg.com/raw/8356bebae88dae96aaecf03ea202df0d.png)

Hadoop-cos-DistChecker 会读取源文件列表和源目录执行 MapReduce 作业，进行分布式检查，最后的检查报告会输出到`cosn://examplebucket-appid/check_result`路径下。

![](https://main.qcloudimg.com/raw/b49000f8613e41a659df31c19bdab2fa.png)

检查报告如下：

```plaintext
hdfs://10.0.0.3:9000/benchmarks/TestDFSIO       hdfs://10.0.0.3:9000/benchmarks/TestDFSIO,cosn://hdfs-test-1250000000/benchmarks/TestDFSIO,None,None,None,SUCCESS,'The source file and the target file are the same.'
hdfs://10.0.0.3:9000/benchmarks/TestDFSIO/io_control    hdfs://10.0.0.3:9000/benchmarks/TestDFSIO/io_control,cosn://hdfs-test-1250000000/benchmarks/TestDFSIO/io_control,None,None,None,SUCCESS,'The source file and the target file are the same.'
hdfs://10.0.0.3:9000/benchmarks/TestDFSIO/io_control/in_file_test_io_0  hdfs://10.0.0.3:9000/benchmarks/TestDFSIO/io_control/in_file_test_io_0,cosn://hdfs-test-1250000000/benchmarks/TestDFSIO/io_control/in_file_test_io_0,CRC64,1566310986176587838,1566310986176587838,SUCCESS,'The source file and the target file are the same.'
hdfs://10.0.0.3:9000/benchmarks/TestDFSIO/io_control/in_file_test_io_1  hdfs://10.0.0.3:9000/benchmarks/TestDFSIO/io_control/in_file_test_io_1,cosn://hdfs-test-1250000000/benchmarks/TestDFSIO/io_control/in_file_test_io_1,CRC64,-6584441696534676125,-6584441696534676125,SUCCESS,'The source file and the target file are the same.'
hdfs://10.0.0.3:9000/benchmarks/TestDFSIO/io_data       hdfs://10.0.0.3:9000/benchmarks/TestDFSIO/io_data,cosn://hdfs-test-1250000000/benchmarks/TestDFSIO/io_data,None,None,None,SUCCESS,'The source file and the target file are the same.'
hdfs://10.0.0.3:9000/benchmarks/TestDFSIO/io_data/test_io_0     hdfs://10.0.0.3:9000/benchmarks/TestDFSIO/io_data/test_io_0,cosn://hdfs-test-1250000000/benchmarks/TestDFSIO/io_data/test_io_0,CRC64,3534425600523290380,3534425600523290380,SUCCESS,'The source file and the target file are the same.'
hdfs://10.0.0.3:9000/benchmarks/TestDFSIO/io_data/test_io_1     hdfs://10.0.0.3:9000/benchmarks/TestDFSIO/io_data/test_io_1,cosn://hdfs-test-1250000000/benchmarks/TestDFSIO/io_data/test_io_1,CRC64,3534425600523290380,3534425600523290380,SUCCESS,'The source file and the target file are the same.'
hdfs://10.0.0.3:9000/benchmarks/TestDFSIO/io_write      hdfs://10.0.0.3:9000/benchmarks/TestDFSIO/io_write,cosn://hdfs-test-1250000000/benchmarks/TestDFSIO/io_write,None,None,None,SUCCESS,'The source file and the target file are the same.'
hdfs://10.0.0.3:9000/benchmarks/TestDFSIO/io_write/_SUCCESS     hdfs://10.0.0.3:9000/benchmarks/TestDFSIO/io_write/_SUCCESS,cosn://hdfs-test-1250000000/benchmarks/TestDFSIO/io_write/_SUCCESS,CRC64,0,0,SUCCESS,'The source file and the target file are the same.'
hdfs://10.0.0.3:9000/benchmarks/TestDFSIO/io_write/part-00000   hdfs://10.0.0.3:9000/benchmarks/TestDFSIO/io_write/part-00000,cosn://hdfs-test-1250000000/benchmarks/TestDFSIO/io_write/part-00000,CRC64,-4804567387993776854,-4804567387993776854,SUCCESS,'The source file and the target file are the same.'
```



## 检查报告格式

检查报告是以如下格式展示：

```plaintext
check_list.txt中的源文件路径 源文件绝对路径,目标文件绝对路径,Checksum算法,源文件的checksum值,目标文件的checksum值,检查结果,检查结果描述
```

其中检查结果分为以下7种：

- SUCCESS：表示源文件和目标文件都存在，且一致。
- MISMATCH：表示源文件和目标文件都存在，但不一致。
- UNCONFIRM：无法确认源文件和目标文件是否一致，这种状态主要是由于 COS 上的文件可能是 CRC64 校验码特性上线前就存在的文件，无法获取到其 CRC64 的校验值。
- UNCHECKED：未检查。这种状态主要是由于源文件无法读取或无法源文件的checksum值。
- SOURCE_FILE_MISSING：源文件不存在。
- TARGET_FILE_MISSING：目标文件不存在。
- TARGET_FILESYSTEM_ERROR：目标文件系统不是 CosN 文件系统。



## 常见问题

#### 为什么检查报告的 CRC64 值出现负数？

因为 CRC64 值，有可能是20位的值，此时已超过 Java long 型的表示范围，但是其底层字节是一致的，而打印 long 型时，会出现负数表示。

