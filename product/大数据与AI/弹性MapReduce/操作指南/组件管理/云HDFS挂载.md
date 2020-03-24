## 操作场景
云 HDFS 是标准 HDFS 访问协议和分层命名空间的高性能分布式文件系统，EMR 支持读写云 HDFS 上的数据，本文主要介绍了如何将云 HDFS 挂载到 EMR 集群。

## 操作步骤
### 场景一：新集群挂载云 HDFS
>?新集群：2019年12月31日当日及之后创建的集群，EMR 默认 chdfs 挂载地址为`/data/emr/chdfs`。

1. 设置云 HDFS 与 EMR 集群连通性
EMR 集群已自动适配云 HDFS，[创建云 HDFS](https://cloud.tencent.com/document/product/1105/37234) 并合理设置权限，使云 HDFS 与 EMR 集群网络互通。
2. 检查云 HDFS 与 EMR 集群连通性
在 EMR 集群上，使用 `hadoop fs` 命令行工具，运行`hadoop fs –ls ofs://${mountpoint}/`命令，这里 mountpoint 为挂载地址。若文件列表可正常列出，则表示已成功挂在云 HDFS。

### 场景二：存量集群挂载云 HDFS
>?存量集群：2019年12月31日前已创建的集群。

存量 EMR 集群挂载云 HDFS，可参考 [挂载云 HDFS](https://cloud.tencent.com/document/product/1105/36368)。

