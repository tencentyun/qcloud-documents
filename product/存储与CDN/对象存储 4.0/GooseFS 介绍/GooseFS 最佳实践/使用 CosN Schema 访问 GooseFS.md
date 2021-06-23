## 概述

[CosN 工具](https://cloud.tencent.com/document/product/436/6884) 是目前腾讯云对象存储 COS 提供的标准的 Hadoop 文件系统，可以为 Hadoop、Spark 以及 Tez 等大数据计算框架集成 COS 提供支持，使其能够跟访问 HDFS 文件系统时相同，读写存储在 COS 上的数据。对于已经使用 COSN 工具的用户，GooseFS 提供了一种途径，让用户可以在不修改当前 Hive table 定义的前提下，仍然能够使用 CosN scheme 访问 GooseFs，该特性方便用户在不修改已有表定义的前提下，对 GooseFs 的功能和性能进行对比测试。

CosN Schema 和 GooseFS Schema 的映射说明如下：

假设 Namespace 为：

```plaintext
/cos/data/warehouse/ 挂载的 cosn 路径为 cosn://examplebucket-1250000000/data/warehouse/
```

CosN 到 GooseFS 的路径映射关系如下：

```plaintext
cosn://examplebucket-1250000000/data/warehouse -> /cos/data/warehouse/
cosn://examplebucket-1250000000/data/warehouse/folder/test.txt ->/cos/data/warehouse/folder/test.txt
```

GooseFS 到 CosN 的路径映射关系如下：

```plaintext
/cos/data/warehouse ->cosn://examplebucket-1250000000/data/warehouse/
/cos/data/warehouse/ -> cosn://examplebucket-1250000000/data/warehouse/
/cos/data/warehouse/folder/test.txt -> cosn://examplebucket-1250000000/data/warehouse/folder/test.txt
```


## **操作示例**

该示例演示了如何使用CosN Schema 访问 GooseFS。操作流程如下：

### 1. **准备数据和计算集群**

- 参考 [对象存储指引文档](https://cloud.tencent.com/document/product/436/13309) 创建一个存储桶 examplebucket-1250000000；
- 参考 [创建文件夹文档](https://cloud.tencent.com/document/product/436/13329)，在存储桶根目录下创建一个 /ml-100k 的文件夹；
- 从 [Grouplens](https://grouplens.org/datasets/movielens/100k/) 下载 ml-100k 数据集，并将数据集上传到存储桶目录 /ml-100k 下；
- 参考 EMR 指引文档，购买一个 EMR 集群并配置 HIVE 组件。

### 2. **环境配置**

- 修改 etc/hadoop/hadoop-env.sh，将 client 包路径添加到 hadoop classpath 中，以便让 hadoop 识别 GooseFS 的 scheme 'gfs'：

```plaintext
export HADOOP_CLASSPATH=/usr/local/service/goosefs-centos/client/goosefs-1.0.0-SNAPSHOT-client.jar:$HADOOP_CLASSPATH
```


- 修改 etc/hadoop/core-site.xml，指定 GooseFS 的实现：

```plaintext
<property>
<name>fs.AbstractFileSystem.gfs.impl</name>
<value>com.qcloud.cos.goosefs.hadoop.GooseFileSystem</value>
</property>
<property>
<name>fs.gfs.impl</name>       <value>com.qcloud.cos.goosefs.hadoop.FileSystem</value>
</property>
```


- 执行如下命令，使得当前用户执行 hdfs 命令时，能加载 GooseFS 的默认配置：

```plaintext
ln -s /usr/local/service/goosefs-centos/conf/ ~/.goosefs
```


执行如下命令，检查能否 hadoop ls gfs ：

```plaintext
hadoop fs -ls gfs:///
```


- 将 GooseFS 的client jar包放到 HIVE 的 auxlib 目录下，使得 HIVE 能加载到 GooseFS client包：

```plaintext
goosefs-1.0.0-SNAPSHOT-client.jar
```

- 执行如下命令，查看是否能创建 namespace，挂载 CosN 路径：

```plaintext
goosefs ns create ml-100k cosn://examplebucket-1250000000/ml-100k --option fs.cosn.userinfo.secretId=xxx --option fs.cosn.userinfo.secretKey=yyy --option fs.cosn.bucket.region=ap-guangzhou --option fs.cosn.impl=org.apache.hadoop.fs.CosFileSystem -option fs.AbstractFileSystem.cosn.impl=org.apache.hadoop.fs.CosN --option fs.cosn.credentials.provider=org.apache.hadoop.fs.auth.SimpleCredentialProvider
goosefs ns list
```





### 3. **创建 GooseFS Schema 表和查询数据**

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


### 4. **创建 CosN Schema 表和查询数据**

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

### 5. **修改 CosN 的实现为 GooseFS 的兼容实现**

修改 hadoop/etc/hadoop/core-site.xml，将 fs.cosn.impl 修改为：

```plaintext
com.qcloud.cos.goosefs.hadoop.CosNFileSystem
```

执行如下命令，查看输出的 info 日志中是否有路径转换：

```plaintext
 hadoop fs -ls  cosn://examplebucket-1250000000/ml-100k/

convert cosPath:cosn://examplebucket-1250000000/ml-100k to gooseFsPath:/ml-100k/
```

重新执行查询语句：

```plaintext
select sum(age) from u_user_cosn;
```

此时可以发现检索性能有了明显提升。
