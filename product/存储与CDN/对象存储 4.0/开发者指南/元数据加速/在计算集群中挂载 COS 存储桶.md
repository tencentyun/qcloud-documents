## 简介

对象存储（Cloud Object Storage，COS）可以通过开启元数据加速能力，拥有 HDFS 协议访问的能力。开启元数据加速能力后，COS 会为存储桶生成一个挂载点，您可以通过下载 [HDFS 客户端](https://github.com/tencentyun/chdfs-hadoop-plugin/tree/master/jar)，在客户端中输入该挂载点挂载 COS。本文将详细介绍如何在计算集群中挂载开启元数据加速的存储桶。

>! 
>- Hadoop-cos 自8.1.1版本开始支持`cosn://bucketname-appid/`方式访问元数据加速桶。
>- 元数据加速功能只能在创建存储桶时开启，开启后不支持关闭，请结合您的业务情况**慎重考虑**是否开启，同时注意旧版本的 Hadoop-cos 包不能正常访问已开启元数据加速功能的存储桶。

## 前提条件

- 确保计算集群中需要挂载的机器或者容器内已安装 [Java 1.8](https://www.oracle.com/java/technologies/downloads/)。
- 确保计算集群中需要挂载的机器或者容器已授权访问，您需要在 HDFS 权限配置里指定可访问的 VPC 网络和 IP 地址。
- 依赖 JAR 包说明：
1. [chdfs_hadoop_plugin_network-2.8.jar](https://github.com/tencentyun/chdfs-hadoop-plugin/tree/master/jar) verison>=2.7;
2. [cos_api-bundle.jar](https://search.maven.org/artifact/com.qcloud/cos_api-bundle/5.6.69/jar) version>=5.6.69;
3. [Hadoop-cos](https://github.com/tencentyun/hadoop-cos/releases) version>=8.1.3
4. ofs-java-sdk.jar (version >=1.0.4) 自动拉取无需安装，运行 hadoop fs ls 成功后可以在 fs.cosn.trsf.fs.ofs.tmp.cache.dir 配置的目录下查看对应版本是否符合预期;

## 操作步骤

1. 下载 [Hadoop 客户端工具安装包](https://github.com/tencentyun/chdfs-hadoop-plugin/tree/master/jar) 。
2. 将安装包放到各节点 classpath 下保证任务启动能正常加载，例如`$HADOOP_HOME/share/hadoop/common/lib/`下。
>! EMR 环境下自带依赖 jar 包，无需安装，可直接通过 POSIX 语义访问元数据加速桶，如需使用 s3 协议访问则更改 fs.cosn.posix_bucket.fs.impl 配置项，详见下文。
3. 编辑 `core-site.xml`文件，新增以下基本配置：
```
<!--chdfs 的实现类-->
<property>
		 <name>fs.AbstractFileSystem.ofs.impl</name>
		 <value>com.qcloud.chdfs.fs.CHDFSDelegateFSAdapter</value>
</property>

<!--chdfs 的实现类-->
<property>
		 <name>fs.ofs.impl</name>
		 <value>com.qcloud.chdfs.fs.CHDFSHadoopFileSystemAdapter</value>
</property>

<!--本地 cache 的临时目录, 对于读写数据, 当内存 cache 不足时会写入本地硬盘, 这个路径若不存在会自动创建-->
<property>
		 <name>fs.ofs.tmp.cache.dir</name>
		 <value>/data/chdfs_tmp_cache</value>
</property>

<!--用户的appId, 可登录腾讯云控制台(https://console.cloud.tencent.com/developer)查看-->      
<property>
		 <name>fs.ofs.user.appid</name>
		 <value>1250000000</value>
</property>

<!--flush语义, 默认false(异步刷盘), 请参考下图数据可见性与持久化详细说明 -->      
<property>
		 <name>fs.ofs.upload.flush.flag</name>
		 <value>false</value>
</property>

```
4. 将 `core-site.xml`同步到所有`hadoop`节点上。
>?对于 EMR 集群，以上步骤3、4可在 EMR 控制台的组件管理中，修改 HDFS 配置即可。
>
5. 使用 `hadoop fs` 命令行工具，运行`hadoop fs -ls cosn://${bucketname-appid}/`命令，这里 `bucketname-appid` 为挂载地址，即存储桶名称。如果正常列出文件列表，则说明已经成功挂载 COS 存储桶。
6. 用户也可使用 `hadoop` 其他配置项，或者 `mr` 任务在开启了元数据加速能力的 COS 存储桶上运行数据任务。对于 `mr` 任务，可以通过`-Dfs.defaultFS=ofs://${bucketname-appid}/`将本次任务的默认输入输出 `FS` 改为对应的存储桶。

## 配置项说明

### 1. 通用必填配置项

| 配置项                              | 配置项内容                         | 说明                                                         |
| ----------------------------------- | ---------------------------------- | ------------------------------------------------------------ |
| fs.cosn.userinfo.secretId/secretKey |                                    | 填写您账户的 API 密钥信息。可登录 [访问管理控制台](https://console.cloud.tencent.com/capi) 查看云 API 密钥。 |
| fs.cosn.impl                        | org.apache.hadoop.fs.CosFileSystem | cosn 对 FileSystem 的实现类，固定。                          |
| fs.AbstractFileSystem.cosn.impl     | org.apache.hadoop.fs.CosN          | cosn 对 AbstractFileSystem 的实现类，固定为。                |
| fs.cosn.bucket.region               |                                    | 请填写待访问存储桶的地域信息，枚举值请参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224) 中的地域简称，例如：ap-beijing、ap-guangzhou 等。兼容原有配置：fs.cosn.userinfo.region。 |
| fs.cosn.tmp.dir                     | 默认/tmp/hadoop_cos                | 请设置一个实际存在的本地目录，运行过程中产生的临时文件会暂时放于此处。同时建议配置各节点该目录足够的空间和权限 |



### 2. POSIX 访问方式必填配置项

| 配置项                 | 配置项内容     | 说明 |
| ------------------------ | ------------------ | ---------------- |
| fs.cosn.posix_bucket.fs.impl         | com.qcloud.chdfs.fs.CHDFSHadoopFileSystemAdapter                |      POSIX 方式访问配置为 com.qcloud.chdfs.fs.CHDFSHadoopFileSystemAdapter S3 协议方式访问配置为 org.apache.hadoop.fs.CosNFileSystem， 默认 POSIX 方式访问。               |
| fs.cosn.trsf.fs.AbstractFileSystem.ofs.impl | com.qcloud.chdfs.fs.CHDFSDelegateFSAdapter                      |      元数据桶访问实现类                                           |
| fs.cosn.trsf.fs.ofs.impl                    | com.qcloud.chdfs.fs.CHDFSHadoopFileSystemAdapter                |     元数据桶访问实现类                                                          |
| fs.cosn.trsf.fs.ofs.tmp.cache.dir           |  |请设置一个实际存在的本地目录，运行过程中产生的临时文件会暂时放于此处。同时建议配置各节点该目录足够的空间和权限，例如"/data/emr/hdfs/tmp/posix-cosn/"                                                                      |
| fs.cosn.trsf.fs.ofs.user.appid              |                                                  | 必填。用户 appid |
| fs.cosn.trsf.fs.ofs.bucket.region           |                                       | 必填。用户 bucket 对应 region |


### 3. S3 协议访问方式必填配置项

| 配置项                 | 配置项内容     | 说明 |
| ------------------------ | ------------------ | ---------------- |
| fs.cosn.posix_bucket.fs.impl         | org.apache.hadoop.fs.CosNFileSystem |      POSIX 方式访问配置为 com.qcloud.chdfs.fs.CHDFSHadoopFileSystemAdapter S3 协议方式访问配置为 org.apache.hadoop.fs.CosNFileSystem， 默认 POSIX 方式访问。                                        |

### 4. 其他配置项

- [其他 Hadoop-cos 配置项](https://cloud.tencent.com/document/product/436/6884)
- [其他 POSIX 方式配置项](https://cloud.tencent.com/document/product/1105/36368)，其他 POSIX 方式配置项添加“fs.cosn.trsf.”前缀即可用于访问元数据加速桶。
