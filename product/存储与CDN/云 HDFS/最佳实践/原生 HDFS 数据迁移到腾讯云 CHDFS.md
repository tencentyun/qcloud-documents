## 准备工作

1. 在腾讯云官网创建 CHDFS 文件系统和 CHDFS 挂载点，配置好权限信息。
2. 通过腾讯云 VPC 环境的 CVM 机器访问创建好的 CHDFS，详情请参见 [创建 CHDFS](https://cloud.tencent.com/document/product/1105/37234)。
3. 当挂载成功后，打开 hadoop 命令行工具，执行以下命令，验证 CHDFS 功能是否正常。
```bash
hadoop fs -ls ofs://f4xxxxxxxxxxxxxxx.chdfs.ap-beijing.myqcloud.com/
```
如果能看到以下类似的输出，则表明云 HDFS 功能一切正常。
![](https://main.qcloudimg.com/raw/3be9476976dd7da027ea6e634652c00b.png)

## 迁移

当准备工作就绪后，就可以使用 hadoop 社区标准的 Distcp 工具实现全量或者增量的 HDFS 数据迁移，详情请参见 [Distcp 官方指引文档](https://hadoop.apache.org/docs/r1.0.4/cn/distcp.html)。

#### 注意事项

在 hadoop distcp 工具中，提供了一些 CHDFS 不兼容的参数。如果指定如下表格中的一些参数，则不生效。

| 参数| 描述                                        | 状态 |
| -------- | ----------------------------------------------- | -------- |
| -p[rbax] | r：replication，b：block-size，a：ACL，x：XATTR | 不生效   |

#### 示例说明

1. 当 CHDFS 准备就绪后，执行以下 hadoop 命令进行数据迁移。
```bash
hadoop distcp hdfs://10.0.1.11:4007/testcp ofs://f4xxxxxxxx-xxxx.chdfs.ap-beijing.myqcloud.com/
```
其中`f4xxxxxxxx-xxxx.chdfs.ap-beijing.myqcloud.com`为挂载点域名，需要根据实际申请的挂载点信息进行替换。
2. Hadoop 命令执行完毕后，会在日志中打印出本次迁移的具体详情。如下示例所示：
```plaintext
2019-12-31 10:59:31 [INFO ] [main:13300] [org.apache.hadoop.mapreduce.Job:] [Job.java:1385]
 Counters: 38
    File System Counters
        FILE: Number of bytes read=0
        FILE: Number of bytes written=387932
        FILE: Number of read operations=0
        FILE: Number of large read operations=0
        FILE: Number of write operations=0
        HDFS: Number of bytes read=1380
        HDFS: Number of bytes written=74
        HDFS: Number of read operations=21
        HDFS: Number of large read operations=0
        HDFS: Number of write operations=6
        OFS: Number of bytes read=0
        OFS: Number of bytes written=0
        OFS: Number of read operations=0
        OFS: Number of large read operations=0
        OFS: Number of write operations=0
    Job Counters
        Launched map tasks=3
        Other local map tasks=3
        Total time spent by all maps in occupied slots (ms)=419904
        Total time spent by all reduces in occupied slots (ms)=0
        Total time spent by all map tasks (ms)=6561
        Total vcore-milliseconds taken by all map tasks=6561
        Total megabyte-milliseconds taken by all map tasks=6718464
    Map-Reduce Framework
        Map input records=3
        Map output records=2
        Input split bytes=408
        Spilled Records=0
        Failed Shuffles=0
        Merged Map outputs=0
        GC time elapsed (ms)=179
        CPU time spent (ms)=4830
        Physical memory (bytes) snapshot=1051619328
        Virtual memory (bytes) snapshot=12525191168
        Total committed heap usage (bytes)=1383071744
    File Input Format Counters
        Bytes Read=972
File Output Format Counters
        Bytes Written=74
    org.apache.hadoop.tools.mapred.CopyMapper$Counter
        BYTESSKIPPED=5
        COPY=1
        SKIP=2
```

