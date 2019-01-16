## 功能说明
HADOOP cosn 插件实现了以腾讯云 COS 作为底层存储文件系统运行上层计算任务的功能，使用 Hadoop 大数据处理引擎，如 MapReduce，Hive、Spark、Tez 等，可以处理存储在腾讯云对象存储 COS 上的数据。

## 使用环境
### 系统环境
Linux 或 Windows 系统。

### 软件依赖
Hadoop-2.6.0及以上版本。

## 下载与安装

### 获取 hadoop-cos 插件
下载地址：[hadoop-cos 插件](https://github.com/tencentyun/hadoop-cos)。


### 安装 hadoop-cos 插件

1. 将 dep 目录下的cos_hadoop_api-5.2.6.jar 和 hadoop-cos-2.X.X.jar 拷贝到 `$HADOOP_HOME/share/hadoop/tools/lib`下。
>?根据 hadoop 的具体版本选择对应的 jar 包，若 dep 目录中没有提供匹配版本的 jar 包，可自行通过修改 pom 文件中 hadoop 版本号，重新编译生成。 

2. 修改 hadoop_env.sh
在 `$HADOOP_HOME/etc/hadoop`目录下，进入 hadoop_env.sh，增加以下内容，将 cosn 相关 jar 包加入 Hadoop 环境变量：
```shell
for f in $HADOOP_HOME/share/hadoop/tools/lib/*.jar; do
  if [ "$HADOOP_CLASSPATH" ]; then
    export HADOOP_CLASSPATH=$HADOOP_CLASSPATH:$f
  else
    export HADOOP_CLASSPATH=$f
  fi
done
```

## 使用方法

### HADOOP 配置

修改 $HADOOP_HOME/etc/hadoop/core-site.xml，增加 COS 相关用户和实现类信息，例如：

```xml
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>cosn://<bucket-appid></value>
    </property>
      
    <property>
        <name>hadoop.tmp.dir</name>
        <value>${HADOOP_PATH}/tmp</value>
    </property>
      
    <property>
        <name>dfs.name.dir</name>
        <value>${HADOOP_PATH}/name</value>
    </property>
  
    <property>
        <name>fs.cosn.credentials.provider</name>
        <value>org.apache.hadoop.fs.auth.SimpleCredentialProvider</value>
        <description>

            This option allows the user to specify how to get the credentials.
            Comma-separated class names of credential provider classes which implement
            com.qcloud.cos.auth.COSCredentialsProvider:

            1.org.apache.hadoop.fs.auth.SimpleCredentialProvider: Obtain the secret id and secret key
            from fs.cosn.userinfo.secretId and fs.cosn.userinfo.secretKey in core-site.xml
            2.org.apache.hadoop.fs.auth.EnvironmentVariableCredentialProvider: Obtain the secret id and secret key
            from system environment variables named COS_SECRET_ID and COS_SECRET_KEY

            If unspecified, the default order of credential providers is:
            1. org.apache.hadoop.fs.auth.SimpleCredentialProvider
            2. org.apache.hadoop.fs.auth.EnvironmentVariableCredentialProvider

        </description>
    </property>
  
    <property>
        <name>fs.cosn.userinfo.secretId</name>
        <value>xxxxxxxxxxxxxxxxxxxxxxxxx</value>
        <description>Tencent Cloud Secret Id </description>
    </property>
      
    <property>
        <name>fs.cosn.userinfo.secretKey</name>
        <value>xxxxxxxxxxxxxxxxxxxxxxxx</value>
        <description>Tencent Cloud Secret Key</description>
    </property>
      
    <property>
        <name>fs.cosn.userinfo.region</name>
        <value>ap-xxx</value>
        <description>The region where the bucket is located</description>
    </property>
      
    <property>
        <name>fs.cosn.userinfo.endpoint_suffix</name>
        <value>cos.ap-xxx.myqcloud.com</value>
        <description>
          COS endpoint to connect to. 
          For public cloud users, it is recommended not to set this option, and only the correct area field is required.
        </description>
    </property>
      
    <property>
        <name>fs.cosn.impl</name>
        <value>org.apache.hadoop.fs.CosFileSystem</value>
        <description>The implementation class of the CosN Filesystem</description>
    </property>
      
    <property>
        <name>fs.AbstractFileSystem.cosn.impl</name>
        <value>org.apache.hadoop.fs.CosN</value>
        <description>The implementation class of the CosN AbstractFileSystem.</description>
    </property>

    <property>
        <name>fs.cosn.tmp.dir</name>
        <value>/tmp/hadoop_cos</value>
        <description>Temporary files will be placed here.</description>
    </property>
      
    <property>
    	<name>fs.cosn.buffer.size</name>
        <value>33554432</value>
        <description>The total size of the buffer pool</description>
    </property>
      
    <property>
    	<name>fs.cosn.block.size</name>
        <value>8388608</value>
        <description>Block size to use cosn filesysten, which is the part size for MultipartUpload.
        Considering the COS supports up to 10000 blocks, user should estimate the maximum size of a single file.
        for example, 8MB part size can allow  writing a 78GB single file.</description>
    </property>
      
    <property>
    	<name>fs.cosn.maxRetries</name>
      <value>3</value>
      <description>
        The maximum number of retries for reading or writing files to
        COS, before we signal failure to the application.
      </description>
    </property>
      
    <property>
    	<name>fs.cosn.retry.interval.seconds</name>
      <value>3</value>
      <description>The number of seconds to sleep between each COS retry.</description>
    </property>
      
</configuration>
```

### 配置项说明


| 属性键                             | 说明                |默认值|必填项|
|:-----------------------------------:|:----------------------|:-----:|:-----:|
|fs.cosn.userinfo.secretId/secretKey| 填写您账户的 API 密钥信息。可登录 [控制台](https://console.cloud.tencent.com/capi) 查看云 API 密钥 | 无  | 是|
|fs.cosn.credentials.provider|配置 secret id 和 secret key 的获取方式。当前支持两种获取方式：1.org.apache.hadoop.fs.auth.SimpleCredentialProvider：从 core-site.xml 配置文件中读取 fs.cosn.userinfo.secretId和 fs.cosn.userinfo.secretKey 来获取 secret id 和 secret key 2.org.apache.hadoop.fs.auth.EnvironmentVariableCredentialProvider：从系统环境变量 COS_SECRET_ID 和COS_SECRET_KEY 中获取|如果不指定改配置项，默认会按照以下顺序读取：1.org.apache.hadoop.fs.auth.SimpleCredentialProvider；2.org.apache.hadoop.fs.auth.EnvironmentVariableCredentialProvider。|否|
|fs.cosn.impl                      | cosn 对 FileSystem 的实现类，固定为 org.apache.hadoop.fs.CosFileSystem| 无 |是|
|fs.AbstractFileSystem.cosn.impl   | cosn 对 AbstractFileSystem 的实现类，固定为 org.apache.hadoop.fs.CosN | 无 |是|
|fs.cosn.userinfo.region           | 请填写您的地域信息，枚举值为 [可用地域](https://cloud.tencent.com/document/product/436/6224) 中的地域简称，如	ap-beijing、ap-guangzhou 等 | 无 | 是|
|fs.cosn.userinfo.endpoint_suffix | 指定要连接的 COS endpoint，该项为非必填项目。对于公有云 COS 用户而言，只需要正确填写上述的region配置即可。|无|否|
|fs.cosn.tmp.dir                | 请设置一个实际存在的本地目录，运行过程中产生的临时文件会暂时放于此处。| /tmp/hadoop_cos | 否|
|fs.cosn.buffer.size        | 向 COS 流式上传文件时，本地使用的内存缓冲区的大小。要求至少大于等于一个 block 的大小 | 33554432（32MB）|否|
|fs.cosn.block.size                | CosN 文件系统每个 block 的大小，也是分块上传的每个 part size 的大小。由于 COS 的分块上传最多只能支持10000块，因此需要预估最大可能使用到的单文件大小。例如，block size 为8MB 时，最大能够支持78GB 的单文件上传。 block size 最大可以支持到2GB，即单文件最大可支持19TB| 8388608（8MB） | 否 |
|fs.cosn.upload_thread_pool        | 文件流式上传到 COS 时，并发上传的线程数目 | CPU核心数*5 | 否 |
|fs.cosn.copy_thread_pool          |目录拷贝操作时，可用于并发拷贝文件的线程数目 | CPU核心数目*3 | 否 |
|fs.cosn.read.ahead.block.size     | 预读块的大小                                 | 524288（512KB） |  否 |
|fs.cosn.read.ahead.queue.size     | 预读队列的长度                               | 10              | 否  |
|fs.cosn.maxRetries				   | 访问 COS 出现错误时，最多重试的次数 | 3 | 否 |
|fs.cosn.retry.interval.seconds    | 每次重试的时间间隔 | 3 | 否 |


### 使用示例

命令格式为：`hadoop fs -ls -R cosn://bucket-appid/<路径>` 或 `hadoop fs -ls -R /<路径>`（需要配置 fs.defaultFS 选项为 cosn://bucket-appid），下例中以名称为 hdfs-test-1252681929 的 bucket 为例，可在其后面加上具体路径。

```shell
hadoop fs -ls -R cosn://hdfs-test-1252681929/
-rw-rw-rw-   1 root root       1087 2018-06-11 07:49 cosn://hdfs-test-1252681929/LICENSE
drwxrwxrwx   - root root          0 1970-01-01 00:00 cosn://hdfs-test-1252681929/hdfs
drwxrwxrwx   - root root          0 1970-01-01 00:00 cosn://hdfs-test-1252681929/hdfs/2018
-rw-rw-rw-   1 root root       1087 2018-06-12 03:26 cosn://hdfs-test-1252681929/hdfs/2018/LICENSE
-rw-rw-rw-   1 root root       2386 2018-06-12 03:26 cosn://hdfs-test-1252681929/hdfs/2018/ReadMe
drwxrwxrwx   - root root          0 1970-01-01 00:00 cosn://hdfs-test-1252681929/hdfs/test
-rw-rw-rw-   1 root root       1087 2018-06-11 07:32 cosn://hdfs-test-1252681929/hdfs/test/LICENSE
-rw-rw-rw-   1 root root       2386 2018-06-11 07:29 cosn://hdfs-test-1252681929/hdfs/test/ReadMe
```

运行 MapReduce 自带的 wordcount，执行以下命令。
>!以下命令中 hadoop-mapreduce-examples-2.7.2.jar 是以2.7.2版本为例，若版本不同，请修改成对应的版本号。

```shell
bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.2.jar wordcount cosn://example/mr/input cosn://example/mr/output3
```

执行成功会返回统计信息，示例如下：
```
File System Counters
COSN: Number of bytes read=72
COSN: Number of bytes written=40
COSN: Number of read operations=0
COSN: Number of large read operations=0
COSN: Number of write operations=0
FILE: Number of bytes read=547350
FILE: Number of bytes written=1155616
FILE: Number of read operations=0
FILE: Number of large read operations=0
FILE: Number of write operations=0
HDFS: Number of bytes read=0
HDFS: Number of bytes written=0
HDFS: Number of read operations=0
HDFS: Number of large read operations=0
HDFS: Number of write operations=0
Map-Reduce Framework
Map input records=5
Map output records=7
Map output bytes=59
Map output materialized bytes=70
Input split bytes=99
Combine input records=7
Combine output records=6
Reduce input groups=6
Reduce shuffle bytes=70
Reduce input records=6
Reduce output records=6
Spilled Records=12
Shuffled Maps =1
Failed Shuffles=0
Merged Map outputs=1
GC time elapsed (ms)=0
Total committed heap usage (bytes)=653262848
Shuffle Errors
BAD_ID=0
CONNECTION=0
IO_ERROR=0
WRONG_LENGTH=0
WRONG_MAP=0
WRONG_REDUCE=0
File Input Format Counters
Bytes Read=36
File Output Format Counters
Bytes Written=40
```
