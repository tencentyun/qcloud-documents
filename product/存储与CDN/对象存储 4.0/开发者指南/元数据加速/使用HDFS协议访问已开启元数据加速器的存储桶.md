## 元数据加速器概述

元数据加速器是由腾讯云对象存储（Cloud Object Storage，COS）服务提供的高性能文件系统功能。元数据加速器底层采用了云 HDFS 卓越的元数据管理功能，支持用户通过文件系统语义访问对象存储服务，系统设计指标可以达到2.4Gb/s带宽、10万级 QPS 以及 ms 级延迟。存储桶在开启元数据加速器后，可以广泛应用于大数据、高性能计算、机器学习、AI 等场景。有关元数据加速器的详细介绍，请参见 [元数据加速器](https://cloud.tencent.com/document/product/436/56971)。

## 使用 HDFS 协议访问的优势

以往基于 COS 的大数据访问主要使用 Hadoop-COS 工具来访问。Hadoop-COS 工具内部将 HCFS 接口适配为 COS 的 Restful 接口，从而对 COS 上的数据进行访问。由于 COS 和文件系统在元数据组织方式上的差异，导致元数据操作性能上存在性能差异，从而影响了大数据分析性能。开启元数据加速器的 Bucket，完全兼容 HCFS 协议，可以采用原生的 HDFS 接口直接访问，除了省去了 HDFS 协议到对象协议的转换开销外，更能提供原生 HDFS 的一些功能，例如目录原子高效 Rename、文件 Atime、Mtime 更新、高效目录 DU 统计、Posix ACL 权限支持等原生特性。

<span id="1"></span>
## 创建存储桶并配置 HDFS 协议

1. 创建 COS 存储桶，并且开启元数据加速器。如下图所示：
![开启元数据加速能力](https://qcloudimg.tencent-cloud.cn/raw/148ce1336e35c53d3f7ef4cd95e2a35c.png)
当存储桶创建完成后，进入存储桶的**文件列表**页面，您可在该页面进行文件上传和下载操作。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/bc79bd567aa0c59aa1c2ad9090470247.png)
2. 在左侧菜单栏中，单击**性能配置 > 元数据加速能力**，可以看到元数据加速能力已开启。
如果是第一次创建**需开启元数据加速**的存储桶，需要按照提示进行相应的**授权**操作，单击授权完成后，将自动开启 HDFS 协议，并且看到默认的存储桶挂载点信息。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/8911a046375d13102a5d7faf8084f931.png)
>?如果提示未找到对应的 HDFS 文件系统，请单击 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系我们获取帮助。
>
3. 在 HDFS 权限配置栏中，单击**新增权限配置**。
![](https://qcloudimg.tencent-cloud.cn/raw/b1708a946fae9c4722e1c809770ee26b.png)
4. 在 VPC 网络名称列选择计算集群所在的 VPC 网络地址，在节点 IP 地址列填写 VPC 网段下需要放通的 IP 地址或者 IP 段，访问类型选择读写或者只读，配置完成后，单击**保存**即可。
>? HDFS 权限配置与原生 COS 权限体系存在差异。当您使用 HDFS 协议访问时，推荐通过配置 HDFS 权限授权指定 VPC 内机器访问 COS 存储桶，以便获取和原生 HDFS 一致的权限体验。


## 配置计算集群访问 COS

### 腾讯云 EMR 环境

腾讯云 EMR 环境已经无缝集成 COS，您只需要完成以下几个步骤：
1. 找到一台 EMR 机器，并在该机器上执行以下命令， 检查 EMR 环境下 HDFS 协议的客户端包版本，确保客户端 jar 包的版本在 2.7及其以上。
```
find / -name "chdfs*"
```
查看搜索结果里 chdfs 包的版本后缀是否为2.7或者以上。
2. 如果客户端版本的包需要更新，则执行以下步骤进行更新：
 1. 下载更新 jar 包的脚本文件，下载地址如下：
    - [update_cos_jar.sh](https://hadoop-jar-beijing-1259378398.cos.ap-beijing.myqcloud.com/hadoop_plugin_network/2.7/update_cos_jar.sh)
    - [update_cos_jar_common.sh](https://hadoop-jar-beijing-1259378398.cos.ap-beijing.myqcloud.com/hadoop_plugin_network/2.7/update_cos_jar_common.sh)
 2. 把这两个脚本放到服务器 /root 目录下，为 update_cos_jar.sh 添加执行权限，执行以下命令：
```
sh update_cos_jar.sh  https://hadoop-jar-beijing-1259378398.cos.ap-beijing.myqcloud.com/hadoop_plugin_network/2.7  
```
参数替换为对应地域的存储桶，例如广州地域，则替换为`https://hadoop-jar-guangzhou-1259378398.cos.ap-guangzhou.myqcloud.com/hadoop_plugin_network/2.7`。
在每一台 EMR 节点上执行以上步骤，直到机器上的 jar 包都替换完成。
3. 在 EMR 控制台配置 core-site.xml，新增配置项`fs.ofs.bucket.region` ，该参数用于指定存储桶所在的 COS 地域，例如 `ap-shanghai`。
>!`fs.ofs.bucket.region` 必须配置，该参数用于指定存储桶所在的 COS 地域，例如 `ap-shanghai`。
>
4. 重启 Yarn、Hive、Presto、Impala 等一些常驻服务。


### 自建 Hadoop/CDH 等环境
1. 下载 HDFS 协议访问的 [客户端安装包](https://github.com/tencentyun/chdfs-hadoop-plugin/tree/master/jar)，请确保安装包的版本在 2.7及其以上。
2. 下载后，将安装包正确放置到 Hadoop 集群中每台服务器的 `classpath` 路径下，例如 `/usr/local/service/hadoop/share/hadoop/common/lib/`（根据实际情况放置，不同组件可能放置的位置也不一样）。
2. 在计算集群配置 `core-site.xml`，具体配置指引请参见 [挂载 CHDFS](https://cloud.tencent.com/document/product/1105/36368)。
3. 重启 Yarn、Hive、Presto、Impala 等一些常驻服务。

>!`fs.ofs.bucket.region` 必须配置，该参数用于指定存储桶所在的 COS 地域，例如 `ap-shanghai`。
>

### 验证环境

所有环境配置完成后，您可以通过如下操作进行验证。
- 在客户端使用 Hadoop 命令行查看是否挂载成功。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/90264cdfe35753b95d48db5ab6675629.png)
- 登录 [COS 控制台](https://console.cloud.tencent.com/cos)，查看存储桶文件列表，明确文件和目录是否一致。如下图所示：
![查看文件列表](https://qcloudimg.tencent-cloud.cn/raw/120bcf98091204f99e7aa868beadb217.png)


## Ranger 权限配置

HDFS 协议默认采用原生 POSIX ACL 方式进行鉴权，如果需要使用 Ranger 鉴权，可参考如下流程配置。

### EMR 环境

1. EMR 环境集成了 COSRanger 服务，在 EMR 集群购买时勾选 COSRanger 服务。
2. 在 HDFS 协议的 HDFS 鉴权模式下，选择 Ranger 鉴权模式，配置上 Ranger 相应的地址信息即可。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/c73328e1b15dba214d75a07fe3cdbc36.png)
 - 如果是 CHDFS，在 core-site.xml 中新增配置项：fs.ofs.ranger.enable.flag，设置为：true。
 - 如果是 COSN，在 core-site.xml 中新增配置项：fs.cosn.credentials.provider，设置为：org.apache.hadoop.fs.auth.RangerCredentialsProvider。
 - 如果遇到 Ranger 相关问题，可参见 [CHDFS 常见问题](https://cloud.tencent.com/document/product/1105/36366)。

### 自建 Hadoop/CDH 等环境

1. 配置 Ranger 服务，通过 Ranger 服务以 HDFS 协议访问 COS，详情请参见 [CHDFS Ranger 权限体系解决方案](https://cloud.tencent.com/document/product/1105/53307) 文档。
2. 在 HDFS 协议的 HDFS 鉴权模式下，选择 Ranger 鉴权模式，配置上 Ranger 相应的地址信息即可。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/c73328e1b15dba214d75a07fe3cdbc36.png)
 - 如果是 CHDFS，在 core-site.xml 中新增配置项：fs.ofs.ranger.enable.flag，设置为：true。
 - 如果是 COSN，在 core-site.xml 中新增配置项：fs.cosn.credentials.provider，设置为：org.apache.hadoop.fs.auth.RangerCredentialsProvider。
 - 如果遇到 Ranger 相关问题，可参见 [CHDFS 常见问题](https://cloud.tencent.com/document/product/1105/36366)。

## 其他

大数据场景下，您可参考以下步骤以 HDFS 协议访问开启元数据加速能力的存储桶：

1. 在 `core-stie.xml` 中配置 HDFS 协议相关挂载点信息，如 [创建存储桶并配置 HDFS 协议](#1) 所示。
2. 通过 Hive、MR、Spark 等组件访问存储桶，请参见 [在计算集群中挂载 COS 存储桶](https://cloud.tencent.com/document/product/436/71550)。
3. 默认情况下，采用原生 `POSIX ACL` 方式进行鉴权，如果需要使用 `Ranger 鉴权`，可参考 [Ranger 相关原理和实践访问](https://cloud.tencent.com/document/product/1105/53307)。



