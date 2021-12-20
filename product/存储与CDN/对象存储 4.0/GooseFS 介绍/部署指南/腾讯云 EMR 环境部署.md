目前 GooseFS 已经集成到了腾讯云 EMR 环境中，将会在最新的 EMR 版本中发布。届时，用户无需针对腾讯云 EMR 环境单独部署，可以像使用其他 EMR 组件一样直接使用 GooseFS。

下文将针对未集成 GooseFS 的腾讯云 EMR 存量集群，介绍如何部署配置 GooseFS 的 EMR 环境。

首先，参照 [集群模式部署运行](https://cloud.tencent.com/document/product/436/57224#.E9.9B.86.E7.BE.A4.E6.A8.A1.E5.BC.8F.E9.83.A8.E7.BD.B2.E8.BF.90.E8.A1.8C) 章节的内容，选择生产环境合适的部署架构，完成集群部署。
其次，针对 EMR 支持组件进行配置，本文以 Hadoop MapReduce、Spark 以及 Flink 对 GooseFS 的支持来讲解。

## Hadoop MapReduce 支持

为了使得 Hadoop 的 MapReduce 作业能够读写 GooseFS 中的数据，需要在 hadoop-env.sh 中将 GooseFS Client 的依赖路径添加到 HADOOP_CLASSPATH，这个操作可以在 EMR 的控制台上完成，如下所示：

![](https://main.qcloudimg.com/raw/dd28fc42063509d5a43dc219ab4637b1.png)

同时，还需要配置在 core-site.xml 中配置 GooseFS 的 HCFS 实现，同样这个操作也可以在 EMR 的控制台上完成：

配置 fs.AbstractFileSystem.gfs.impl 为如下：
```
com.qcloud.cos.goosefs.hadoop.GooseFileSystem
```

![](https://main.qcloudimg.com/raw/4475c860359ad9a6b2305c2100b399a6.png)

配置 fs.gfs.impl 为如下：
```
com.qcloud.cos.goosefs.hadoop.FileSystem
```

![](https://main.qcloudimg.com/raw/53adde8f2bbd97d17b10dc277b2395b4.png)


下发配置后，重启 YARN 相关组件即可生效。


## Spark 支持

为了使得 Spark 能够访问goosefs，同样需要配置 GooseFS 的 client 依赖包到 spark 的 executor classpath 中，同时在 spark-defaults.conf 中指定：

```conf
...
spark.driver.extraClassPath ${GOOSEFS_HOME}/client/goosefs-x.x.x-client.jar
spark.executor.extraClassPath ${GOOSEFS_HOME}/client/goosefs-x.x.x-client.jar
spark.hadoop.fs.gfs.impl com.qcloud.cos.goosefs.hadoop.FileSystem
spark.hadoop.fs.AbstractFileSystem.gfs.impl com.qcloud.cos.goosefs.hadoop.GooseFileSystem
...
```

同样，该操作也可以在 EMR 控制台上 Spark 组件中配置和下发：

![](https://main.qcloudimg.com/raw/6bf4295b7bbddf2e11108e2cec52e4ee.png)

## Flink 支持

腾讯云 EMR 的 Flink 采用的是 Flink on YARN 的部署模式，因此原则上只要确保 ${FLINK_HOME}/flink-conf.yaml 中正确设置 `fs.hdfs.hadoopconf` 到 hadoop 的配置路径下即可，腾讯云 EMR 集群中一般为 `/usr/local/service/hadoop/etc/hadoop`。

无需设置其他配置项，直接使用 Flink on YARN 的方式提交 Flink 作业即可，作业中需要访问 GooseFS 的路径为 `gfs://master:port/<path>`。


>! Flink 访问 GooseFS 时，必须指定 master 和 port。
>

## Hive、Impala、HBase、Sqoop 以及 Oozie 支持

当配置 Hadoop MapReduce 的环境支持以后，Hive、Impala、HBase 等组件无需单独配置支持，即可正常使用。
  
