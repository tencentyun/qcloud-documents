## 概述

透明加速能力用于加速 CosN 访问 COS 的性能。[CosN 工具](https://cloud.tencent.com/document/product/436/6884) 是基于腾讯云对象存储（Cloud Object Storage，COS）提供的标准的 Hadoop 文件系统实现，可以为 Hadoop、Spark 以及 Tez 等大数据计算框架集成 COS 提供支持。用户可使用实现了 Hadoop 文件系统接口的 CosN 插件，读写存储在 COS 上的数据。对于已经使用 CosN 工具访问 COS 的用户，GooseFS 提供了一种客户端路径映射方式，让用户可以在不修改当前 Hive table 定义的前提下，仍然能够使用 CosN scheme 访问 GooseFS，该特性方便用户在不修改已有表定义的前提下，对 GooseFS 的功能和性能进行对比测试。对于云 HDFS 用户（CHDFS），也可以通过修改配置，实现使用 OFS Scheme 访问 GooseFS 的目的。

CosN Schema 和 GooseFS Schema 的映射说明如下：

假设 Namespace warehouse 对应的 UFS 路径为 `cosn://examplebucket-1250000000/data/warehouse/`，则 CosN 到 GooseFS 的路径映射关系如下：
```plaintext
cosn://examplebucket-1250000000/data/warehouse -> /warehouse/
cosn://examplebucket-1250000000/data/warehouse/folder/test.txt ->/warehouse/folder/test.txt
```
GooseFS 到 CosN 的路径映射关系如下：
```plaintext
/warehouse ->cosn://examplebucket-1250000000/data/warehouse/
/warehouse/ -> cosn://examplebucket-1250000000/data/warehouse/
/warehouse/folder/test.txt -> cosn://examplebucket-1250000000/data/warehouse/folder/test.txt
```

CosN Scheme 访问 GooseFS 特性，通过在客户端维持 GooseFS 路径和底层文件系统 CosN 路径之间的映射关系，并将 CosN 路径的请求转换为 GooseFS 的请求。映射关系周期性刷新，您可以通过修改 GooseFS 配置文件 goosefs-site.properties 中的配置项 goosefs.user.client.namespace.refresh.interval 调整刷新间隔，默认值为60s。

>! 如果访问的 CosN 路径无法转换为 GooseFS 路径，对应的 Hadoop API 调用会抛出异常。

## 操作示例

该示例演示了 Hadoop 命令行以及 Hive 中，如何使用 gfs://、 cosn://、ofs:// 三种 Schema 访问 GooseFS。操作流程如下：

### 1. 准备数据和计算集群

- 参考 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 文档，创建一个测试用途的存储桶。
- 参考 [创建文件夹](https://cloud.tencent.com/document/product/436/13329) 文档，在存储桶根路径下创建一个名为 ml-100k 的文件夹。
- 从 [Grouplens](https://grouplens.org/datasets/movielens/100k/) 下载 ml-100k 数据集，并将文件 u.user 上传到 `<存储桶根路径>/ml-100k`下。
- 参考 EMR 指引文档，购买一个 EMR 集群并配置 HIVE 组件。

### 2. 环境配置

i. 将 GooseFS 的客户端 jar 包（goosefs-1.0.0-client.jar）放入 share/hadoop/common/lib/ 目录下：
```plaintext
 cp goosefs-1.0.0-client.jar  hadoop/share/hadoop/common/lib/
```
<dx-alert infotype="notice" title="">
配置变更和添加 jar 包，需同步到集群上所有节点。
</dx-alert>
ii. 修改 Hadoop 配置文件 etc/hadoop/core-site.xml，指定 GooseFS 的实现类：
```plaintext
<property>
  <name>fs.AbstractFileSystem.gfs.impl</name>
  <value>com.qcloud.cos.goosefs.hadoop.GooseFileSystem</value>
</property>
<property>
  <name>fs.gfs.impl</name>
  <value>com.qcloud.cos.goosefs.hadoop.FileSystem</value>
</property>
```
iii. 执行如下 Hadoop 命令，检查是否能够通过 gfs:// Scheme 访问 GooseFS，其中 &lt;MASTER_IP> 为 Master 节点的 IP：
```plaintext
hadoop fs -ls gfs://<MASTER_IP>:9200/
```
iv. 将 GooseFS 的客户端 jar 包放到 Hive 的 auxlib 目录下，使得 Hive 能加载到 GooseFS Client 包：
```plaintext
cp goosefs-1.0.0-client.jar  hive/auxlib/
```
v. 执行如下命令，创建 UFS Scheme 为 CosN 的 Namespace，并列出 Namespace。您可将该命令中的 examplebucket-1250000000 替换为你的 COS 存储桶，SecretId 和 SecretKey 替换为您的密钥信息：
```plaintext
goosefs ns create ml-100k cosn://examplebucket-1250000000/ml-100k  --secret fs.cosn.userinfo.secretId=SecretId --secret fs.cosn.userinfo.secretKey=SecretKey--attribute fs.cosn.bucket.region=ap-guangzhou --attribute fs.cosn.credentials.provider=org.apache.hadoop.fs.auth.SimpleCredentialProvider
goosefs ns ls
```
vi. 执行命令，创建 UFS Scheme 为 OFS 的 Namespace，并列出 Namespace。您可将该命令中的 instance-id 替换为您的 CHDFS 实例，1250000000 替换为您的 APPID：
```plaintext
goosefs ns create ofs-test  ofs://instance-id.chdfs.ap-guangzhou.myqcloud.com/ofs-test --attribute fs.ofs.userinfo.appid=1250000000
goosefs ns ls
```

### 3. 创建 GooseFS Schema 表和查询数据

通过如下指令执行：

```plaintext
create database goosefs_test;

use goosefs_test;
CREATE TABLE u_user_gfs (
userid INT,
age INT,
gender CHAR(1),
occupation STRING,
zipcode STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '|'
STORED AS TEXTFILE
LOCATION 'gfs://<MASTER_IP>:<MASTER_PORT>/ml-100k';

select sum(age) from u_user_gfs;
```


### 4. 创建 CosN Schema 表和查询数据

通过如下指令执行：

```plaintext
CREATE TABLE u_user_cosn (
userid INT,
age INT,
gender CHAR(1),
occupation STRING,
zipcode STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '|'
STORED AS TEXTFILE
LOCATION 'cosn://examplebucket-1250000000/ml-100k';

select sum(age) from u_user_cosn;
```

### 5. 修改 CosN 的实现为 GooseFS 的兼容实现

修改 hadoop/etc/hadoop/core-site.xml：

```plaintext
 <property>
     <name>fs.AbstractFileSystem.cosn.impl</name>
     <value>com.qcloud.cos.goosefs.hadoop.CosN</value>
</property>
<property>
     <name>fs.cosn.impl</name>
     <value>com.qcloud.cos.goosefs.hadoop.CosNFileSystem</value>
</property>
```

执行 Hadoop 命令，如果路径无法转换为 GooseFS 中的路径，命令的输出中会包含报错信息：

```plaintext
hadoop fs -ls  cosn://examplebucket-1250000000/ml-100k/

Found 1 items
-rw-rw-rw-   0 hadoop hadoop      22628 2021-07-02 15:27 cosn://examplebucket-1250000000/ml-100k/u.user
 
hadoop fs -ls cosn://examplebucket-1250000000/unknow-path
ls: Failed to convert ufs path cosn://examplebucket-1250000000/unknow-path to GooseFs path, check if namespace mounted 
```

重新执行 Hive 查询语句：

```plaintext
select sum(age) from u_user_cosn;
```

### 6. 创建 OFS Schema 表和查询数据

通过如下命令执行：

```plaintext
CREATE TABLE u_user_ofs (
userid INT,
age INT,
gender CHAR(1),
occupation STRING,
zipcode STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '|'
STORED AS TEXTFILE
LOCATION 'ofs://instance-id.chdfs.ap-guangzhou.myqcloud.com/ofs-test/';

select sum(age) from u_user_ofs;
```

### 7. 修改 OFS 的实现为 GooseFS 的兼容实现

修改 hadoop/etc/hadoop/core-site.xml：

```plaintext
<property>
     <name>fs.AbstractFileSystem.ofs.impl</name>
     <value>com.qcloud.cos.goosefs.hadoop.CHDFSDelegateFS</value>
</property>
<property>
     <name>fs.ofs.impl</name>
     <value>com.qcloud.cos.goosefs.hadoop.CHDFSHadoopFileSystem</value>
</property>
```

执行 Hadoop 命令，如果路径无法转换为 GooseFS 中的路径，则输出结果中会包含报错信息：

```plaintext
hadoop fs -ls  ofs://instance-id.chdfs.ap-guangzhou.myqcloud.com/ofs-test/

Found 1 items
-rw-r--r--   0 hadoop hadoop      22628 2021-07-15 15:56 ofs://instance-id.chdfs.ap-guangzhou.myqcloud.com/ofs-test/u.user
 
hadoop fs -ls  ofs://instance-id.chdfs.ap-guangzhou.myqcloud.com/unknown-path
ls: Failed to convert ufs path ofs://instance-id.chdfs.ap-guangzhou.myqcloud.com/unknown-path to GooseFs path, check if namespace mounted
```

重新执行 Hive 查询语句：

```plaintext
select sum(age) from u_user_ofs;
```
