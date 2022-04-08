
## 元数据加速器概述

元数据加速器是由腾讯云对象存储（Cloud Object Storage，COS）服务提供的高性能文件系统功能。元数据加速器底层采用了云 HDFS 卓越的元数据管理功能，支持用户通过文件系统语义访问对象存储服务，系统设计指标可以达到2.4Gb/s带宽、10万级 QPS 以及 ms 级延迟。存储桶在开启元数据加速器后，可以广泛应用于大数据、高性能计算、机器学习、AI 等场景。有关元数据加速器的详细介绍，请参见 [元数据加速器](https://cloud.tencent.com/document/product/436/56971)。

## 使用 HDFS 协议访问的优势

以往基于对象存储 COS 的大数据访问主要使用 Hadoop-COS 工具来访问。Hadoop-COS 工具内部将 HCFS 接口适配为对象存储的 Restful 接口，从而对对象存储上的数据进行访问。由于对象存储和文件系统在元数据组织方式上的差异，导致元数据操作性能上存在性能差异，从而影响了大数据分析性能。开启元数据加速器的 Bucket，完全兼容 HCFS 协议，可以采用原生的 HDFS 接口直接访问，除了省去了 HDFS 协议到对象协议的转换开销外，更能提供原生 HDFS 的一些功能，例如目录原子高效 Rename、文件 Atime、Mtime 更新、高效目录 DU 统计、Posix ACL 权限支持等原生特性。


## 准备工作

1. 创建 COS 存储桶，并且开启元数据加速器。如下图所示：
![开启元数据加速能力](https://qcloudimg.tencent-cloud.cn/raw/148ce1336e35c53d3f7ef4cd95e2a35c.png)
2. 当 Bucket 创建完成后，进入存储桶的**文件列表**页面，可在控制台进行文件上传和下载操作。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/bc79bd567aa0c59aa1c2ad9090470247.png)
3. 单击左侧菜单栏中的**性能配置 > 元数据加速能力**，可以看到元数据加速能力已开启。如果是第一次创建**需开启元数据加速**的存储桶，则需要按照提示进行相应的授权操作，单击授权完成后，将自动开启 HDFS 协议，并且看到默认的 Bucket 挂载点信息，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/8911a046375d13102a5d7faf8084f931.png)
>?如果提示未找到对应的 HDFS 文件系统，请单击 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系我们获取帮助。
>
4. 开启 HDFS 协议开关后，需要配置 VPC 访问权限。在 HDFS 权限配置标签页，单击新增权限配置按钮，在 VPC 网络名称列选择计算集群所在的 VPC 网络地址，在节点 IP 地址列，填写 VPC 网段下需要放通的 IP 地址或者 IP 段。访问类型可以选择读写或者只读，配置完成后，单击保存即可，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/b1708a946fae9c4722e1c809770ee26b.png)
>? HDFS 权限配置与原生 COS 权限体系存在差异。当您使用 HDFS 协议访问时，推荐通过配置 HDFS 权限授权指定 VPC 内机器访问 COS 存储桶，以便获取和原生 HDFS 一致的权限体验。
5. HDFS 协议默认采用原生 POSIX ACL 方式进行鉴权，如果需要使用 Ranger 鉴权，可以在 HDFS 鉴权模式下，选择 Ranger 鉴权模式，配置上 Ranger 相应的地址信息即可。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/c73328e1b15dba214d75a07fe3cdbc36.png)
>?您可以参见 [HDFSranger 鉴权](https://cloud.tencent.com/document/product/1105/53307) 文档，配置 Ranger 服务，通过Ranger 服务以 HDFS 协议访问 COS。
>
6. 创建环境后，需要在计算集群配置 `core-site.xml`，具体参考文档配置 [HDFS协议配置](https://cloud.tencent.com/document/product/1105/36368)，如果您使用的是腾讯云  EMR，则可以直接使用 EMR 的默认配置，无需额外配置。
>!`fs.ofs.bucket.region` 必须配置，该参数用于指定存储桶所在的 COS 地域，例如 `ap-shanghai`。
>
7. 下载 HDFS 协议访问的 [客户端安装包](https://github.com/tencentyun/chdfs-hadoop-plugin/tree/master/jar)，请确保安装包的版本在 2.7及其以上。下载后，讲安装包放置到 Hadoop 集群中每台服务器正确的 `classpath` 路径下，例如 `/usr/local/service/hadoop/share/hadoop/common/lib/`（根据实际情况防止，不同组件可能放置的位置也不一样），然后重启 `Yarn`，`Hive`，`Presto`，`Impala` 等一些常驻服务。
8. 所有环境配置完成后，可以在客户端使用 Hadoop 命令行来查看是否挂载成功，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/90264cdfe35753b95d48db5ab6675629.png)
9. 您也可以登录 [COS 控制台](https://console.cloud.tencent.com/cos)，查看存储桶文件列表，明确文件和目录是否一致，如下图所示：
![查看文件列表](https://qcloudimg.tencent-cloud.cn/raw/120bcf98091204f99e7aa868beadb217.png)

## 通过 HDFS 协议访问 COS

大数据场景下，您可以参考如下步骤以 HDFS 协议访问开启元数据加速能力的存储桶：

1. 在 `core-stie.xml` 中配置 HDFS 协议相关挂载点信息，如准备工作中所示。
2. 通过 Hive、MR、Spark 等组件访问存储桶，请参见 [在计算集群中挂载 COS 存储桶](https://cloud.tencent.com/document/product/436/71550)。
3. 默认情况下，采用原生 `POSIX ACL` 方式进行鉴权，如果需要使用 `Ranger1鉴权`，可以参考 `Ranger` 相关原理和实践访问，可参见 [在 CDH 集群上通过 HDFS 协议访问 COS](https://cloud.tencent.com/document/product/436/71551)。


