## 操作场景
CHDFS 是标准 HDFS 访问协议和分层命名空间的高性能分布式文件系统，EMR 支持读写 CHDFS 上的数据，本文主要介绍了如何将 CHDFS 挂载到 EMR 集群。

## 操作步骤

### 场景一：新集群挂载 CHDFS
>?新集群：2019年12月31日当日及之后创建的集群，EMR 默认 CHDFS 挂载地址为 `/data/emr/hdfs/tmp/chdfs`。

EMR 集群已自动适配 CHDFS，创建 CHDFS 并合理设置权限，使 CHDFS 与 EMR 集群网络互通，配置步骤如下：
1. 创建与 EMR 集群同地域的 CHDFS，可参考 [创建 CHDFS](https://cloud.tencent.com/document/product/1105/37234)。
2. 按需创建权限组，可参考 [创建权限组](https://cloud.tencent.com/document/product/1105/37235)。
3. 按需创建权限规则，可参考 [创建权限规则](https://cloud.tencent.com/document/product/1105/37236)。
4. 创建与 EMR 集群同网络下的挂载点，可参考 [创建挂载点](https://cloud.tencent.com/document/product/1105/37237)。
5. 检查 CHDFS 与 EMR 集群连通性，使用 `hadoop fs` 命令行工具，运行 `hadoop fs –ls ofs://${mountpoint}/` 命令，这里 mountpoint 为挂载地址。若文件列表可正常列出，则表示已成功挂在 CHDFS。

### 场景二：存量集群挂载 CHDFS
>?存量集群：2019年12月31日前已创建的集群。

存量 EMR 集群挂载 CHDFS，可参考 [挂载 CHDFS](https://cloud.tencent.com/document/product/1105/36368)。
