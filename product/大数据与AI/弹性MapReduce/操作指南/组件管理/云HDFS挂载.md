云 HDFS 是标准 HDFS 访问协议和分层命名空间的高性能分布式文件系统，EMR 支持读写云 HDFS 上的数据，本文为您介绍如何将云 HDFS 挂载到 EMR 集群。

## 操作步骤
### 场景一：新集群，2019年12月31日后创建的集群
1. 云 HDFS 与 EMR 集群连通性设置：EMR 集群已自动适配云 HDFS，可参考云 HDFS 官方文档 [创建 CHDFS](https://cloud.tencent.com/document/product/1105/37234) 并合理设置权限，使云 HDFS 与 EMR 集群网络互通。
2. 云 HDFS 与 EMR 集群连通性检查：在 EMR 集群上，使用 `hadoop fs` 命令行工具，运行`hadoop fs –ls ofs://${mountpoint}/`命令，这里 mountpoint 为挂载地址。如果正常列出文件列表，则说明已经成功挂载云 HDFS。


### 场景二：存量集群，2019年12月31日前已创建的集群
可参考云 HDFS 提供的官方文档 [挂载 CHDFS](https://cloud.tencent.com/document/product/1105/36368)，将云 HDFS 挂载到 EMR 集群上 。


