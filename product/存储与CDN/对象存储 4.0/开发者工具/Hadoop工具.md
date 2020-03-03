## 功能说明

Hadoop-COS 基于腾讯云对象存储 COS 实现了标准的 Hadoop 文件系统，可以为 Hadoop、Spark 以及 Tez 等大数据计算框架集成 COS 提供支持，使其能够跟访问 HDFS 文件系统时相同，读写存储在 COS 上的数据。

Hadoop-COS 使用 cosn 作为 URI 的 scheme，因此也称为 Hadoop-COS 为 CosN 文件系统。

## 使用环境

#### 系统环境

支持 Linux、Windows 和 macOS 系统。

#### 软件依赖

Hadoop-2.6.0及以上版本。

## 下载与安装

#### 获取 Hadoop-COS 插件

下载地址：[Hadoop-COS 插件](https://github.com/tencentyun/hadoop-cos)。

#### 安装 Hadoop-COS 插件

1. 将 dep 目录下的`hadoop-cos-X.X.X-shaded.jar*`， 拷贝到`$HADOOP_HOME/share/hadoop/tools/lib`下。

> ?根据 Hadoop 的具体版本选择对应的 jar 包，若 dep 目录中没有提供匹配版本的 jar 包，可自行通过修改 pom 文件中 Hadoop 版本号，重新编译生成。 

2. 修改 hadoop_env.sh 文件。
   进入`$HADOOP_HOME/etc/hadoop`目录，编辑 hadoop_env.sh 文件，增加以下内容，将 cosn 相关 jar 包加入 Hadoop 环境变量：

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

### 配置项说明

|                  属性键                  | 说明                                                         |                            默认值                            | 必填项 |
| :--------------------------------------: | :----------------------------------------------------------- | :----------------------------------------------------------: | :----: |
|   fs.cosn.userinfo.secretId/secretKey    | 填写您账户的 API 密钥信息。可登录 [访问管理控制台](https://console.cloud.tencent.com/capi) 查看云 API 密钥。 |                              无                              |   是   |
|       fs.cosn.credentials.provider       | 配置 SecretId 和 SecretKey 的获取方式。当前支持三种获取方式：<br>1.org.apache.hadoop.fs.auth.SessionCredentialProvider：从请求 URI 中获取 secret id 和 secret key。<br>其格式为：`cosn://{secretId}:{secretKey}@examplebucket-1250000000/`。<br>2.org.apache.hadoop.fs.auth.SimpleCredentialProvider：<br>从 core-site.xml 配置文件中读取 fs.cosn.userinfo.secretId 和 fs.cosn.userinfo.secretKey 来获取 SecretId 和 SecretKey。<br>3.org.apache.hadoop.fs.auth.EnvironmentVariableCredentialProvider：从系统环境变量 COS_SECRET_ID 和 COS_SECRET_KEY 中获取。 | 如果不指定改配置项，默认会按照以下顺序读取：<br>1.org.apache.hadoop.fs.auth.SessionCredentialProvider<br>2.org.apache.hadoop.fs.auth.SimpleCredentialProvider <br>3.org.apache.hadoop.fs.auth.EnvironmentVariableCredentialProvider |   否   |
|               fs.cosn.impl               | cosn 对 FileSystem 的实现类，固定为 org.apache.hadoop.fs.CosFileSystem。 |                              无                              |   是   |
|     fs.AbstractFileSystem.cosn.impl      | cosn 对 AbstractFileSystem 的实现类，固定为 org.apache.hadoop.fs.CosN。 |                              无                              |   是   |
|          fs.cosn.bucket.region           | 请填写待访问 bucket 的地域信息，枚举值请参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224) 中的地域简称，例如	ap-beijing、ap-guangzhou 等。兼容原有配置：fs.cosn.userinfo.region。 |                              无                              |   是   |
|      fs.cosn.bucket.endpoint_suffix      | 指定要连接的 COS endpoint，该项为非必填项目。对于公有云 COS 用户而言，只需要正确填写上述的 region 配置即可。兼容原有配置：fs.cosn.userinfo.endpoint_suffix。 |                              无                              |   否   |
|             fs.cosn.tmp.dir              | 请设置一个实际存在的本地目录，运行过程中产生的临时文件会暂时放于此处。 |                       /tmp/hadoop_cos                        |   否   |
|            fs.cosn.block.size            | CosN 文件系统每个 block 的大小，也是分块上传的每个 part size 的大小。由于 COS 的分块上传最多只能支持10000块，因此需要预估最大可能使用到的单文件大小。例如，block size 为8MB时，最大能够支持78GB的单文件上传。 block size 最大可以支持到2GB，即单文件最大可支持19TB。 |                        8388608（8MB）                        |   否   |
|        fs.cosn.upload_thread_pool        | 文件流式上传到 COS 时，并发上传的线程数目。                  |                        CPU核心数 X 5                         |   否   |
|         fs.cosn.copy_thread_pool         | 目录拷贝操作时，可用于并发拷贝文件的线程数目。               |                       CPU核心数目 X 3                        |   否   |
|      fs.cosn.read.ahead.block.size       | 预读块的大小。                                               |                        1048576（1MB）                        |   否   |
|      fs.cosn.read.ahead.queue.size       | 预读队列的长度。                                             |                              8                               |   否   |
|            fs.cosn.maxRetries            | 访问 COS 出现错误时，最多重试的次数。                        |                             200                              |   否   |
|      fs.cosn.retry.interval.seconds      | 每次重试的时间间隔。                                         |                              3                               |   否   |
| fs.cosn.server-side-encryption.algorithm | 配置 COS 服务端加密算法，支持 SSE-C 和 SSE-COS，默认为空，不加密 |                              无                              |   否   |
|    fs.cosn.server-side-encryption.key    | 当开启 COS 的 SSE-C 服务端加密算法时，必须配置 SSE-C 的密钥，密钥格式为 base64 编码的 AES-256 密钥，默认为空，不加密 |                              无                              |   否   |

### Hadoop 配置

修改`$HADOOP_HOME/etc/hadoop/core-site.xml`，增加 COS 相关用户和实现类信息，例如：

```xml
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>cosn://examplebucket-1250000000</value>
    </property>
  
    <property>
        <name>fs.cosn.credentials.provider</name>
        <value>org.apache.hadoop.fs.auth.SimpleCredentialProvider</value>
        <description>

            This option allows the user to specify how to get the credentials.
            Comma-separated class names of credential provider classes which implement
            com.qcloud.cos.auth.COSCredentialsProvider:

            1.org.apache.hadoop.fs.auth.SessionCredentialProvider: Obtain the secret id and secret key from the URI: cosn://secretId:secretKey@examplebucket-1250000000/;
            2.org.apache.hadoop.fs.auth.SimpleCredentialProvider: Obtain the secret id and secret key
            from fs.cosn.userinfo.secretId and fs.cosn.userinfo.secretKey in core-site.xml;
            3.org.apache.hadoop.fs.auth.EnvironmentVariableCredentialProvider: Obtain the secret id and secret key
            from system environment variables named COS_SECRET_ID and COS_SECRET_KEY.

            If unspecified, the default order of credential providers is:
            1. org.apache.hadoop.fs.auth.SessionCredentialProvider
            2. org.apache.hadoop.fs.auth.SimpleCredentialProvider
            3. org.apache.hadoop.fs.auth.EnvironmentVariableCredentialProvider

        </description>
    </property>
  
    <property>
        <name>fs.cosn.userinfo.secretId</name>
        <value>xxxxxxxxxxxxxxxxxxxxxxxxx</value>
        <description>Tencent Cloud Secret Id</description>
    </property>
      
    <property>
        <name>fs.cosn.userinfo.secretKey</name>
        <value>xxxxxxxxxxxxxxxxxxxxxxxx</value>
        <description>Tencent Cloud Secret Key</description>
    </property>
      
    <property>
        <name>fs.cosn.bucket.region</name>
        <value>ap-xxx</value>
        <description>The region where the bucket is located.</description>
    </property>
      
    <property>
        <name>fs.cosn.bucket.endpoint_suffix</name>
        <value>cos.ap-xxx.myqcloud.com</value>
        <description>
          COS endpoint to connect to. 
          For public cloud users, it is recommended not to set this option, and only the correct area field is required.
        </description>
    </property>
      
    <property>
        <name>fs.cosn.impl</name>
        <value>org.apache.hadoop.fs.CosFileSystem</value>
        <description>The implementation class of the CosN Filesystem.</description>
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
    	<name>fs.cosn.block.size</name>
        <value>8388608</value>
        <description>Block size to use cosn filesysten, which is the part size for MultipartUpload.
        Considering the COS supports up to 10000 blocks, user should estimate the maximum size of a single file.
        For example, 8MB part size can allow  writing a 78GB single file.</description>
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
   
    <property>
    	<name>fs.cosn.server-side-encryption.algorithm</name>
        <value></value>
        <description>The server side encryption algorithm.</description>
    </property>	
	
     <property>
    	<name>fs.cosn.server-side-encryption.key</name>
        <value></value>
        <description>The SSE-C server side encryption key.</description>
    </property> 
      
</configuration>
```

### 服务端加密

Hadoop-COS 支持服务端加密，目前提供两种加密方式：COS 托管密钥方式（SSE-COS）和用户自定义密钥方式（SSE-C），Hadoop-COS 的加密功能默认为关闭状态，用户可以选择开启，通过以下方式进行配置。

#### SSE-COS 加密

SSE-COS 加密即 COS 托管密钥的服务端加密，由腾讯云 COS 托管主密钥和管理数据。当使用 Hadoop-COS 时，用户可以在`$HADOOP_HOME/etc/hadoop/core-site.xml`文件中，增加以下配置来进行实现 SSE-COS 加密。

```shell
<property>
    	<name>fs.cosn.server-side-encryption.algorithm</name>
        <value>SSE-COS</value>
        <description>The server side encryption algorithm.</description>
</property>
```

#### SSE-C 加密

SSE-C 加密即用户自定义密钥的服务端加密。加密密钥由用户自己提供，用户在上传对象时，COS 将使用用户提供的加密密钥对用户的数据进行 AES-256 加密。当使用 Hadoop-COS 时，用户可以在`$HADOOP_HOME/etc/hadoop/core-site.xml`文件中，增加以下配置来进行实现 SSE-C 加密。

```shell
<property>
        <name>fs.cosn.server-side-encryption.algorithm</name>
        <value>SSE-C</value>
        <description>The server side encryption algorithm.</description>
 </property>		
 <property>
  	<name>fs.cosn.server-side-encryption.key</name>
        <value>MDEyMzQ1Njc4OUFCQ0RFRjAxMjM0NTY3ODlBQkNERUY=</value> #用户需要自行配置 SSE-C 的密钥，密钥格式为 base64 编码的 AES-256 密钥。
        <description>The SSE-C server side encryption key.</description>
 </property> 
```

> !
>
> - Hadoop-COS 的 SSE-C 服务端加密依赖于 COS 的 SSE-C 服务端加密。因此，Hadoop-COS 不存储用户提供的加密密钥。同时需要值得注意的是，COS 的 SSE-C 服务端加密方式不存储用户提供的加密密钥，而是存储加密密钥添加了随机数据的 HMAC 值，该值用于验证用户访问对象的请求。COS 无法使用随机数据的 HMAC 值来推导出加密密钥的值或解密加密对象的内容。因此，如果用户丢失了加密密钥，则无法再次获取到该对象。
> - Hadoop-COS 配置了 SSE-C 服务端加密算法时，必须在 fs.cosn.server-side-encryption.key 配置项中配置 SSE-C 的密钥，密钥格式为 base64 编码的 AES-256 密钥。

### 使用示例

命令格式为`hadoop fs -ls -R cosn://<BucketName-APPID>/<路径>`，或`hadoop fs -ls -R /<路径>`（需要配置`fs.defaultFS`选项为`cosn://BucketName-APPID`），下例中以名称为 examplebucket-1250000000 的 bucket 为例，可在其后面加上具体路径。

```shell
hadoop fs -ls -R cosn://examplebucket-1250000000/
-rw-rw-rw-   1 root root       1087 2018-06-11 07:49 cosn://examplebucket-1250000000/LICENSE
drwxrwxrwx   - root root          0 1970-01-01 00:00 cosn://examplebucket-1250000000/hdfs
drwxrwxrwx   - root root          0 1970-01-01 00:00 cosn://examplebucket-1250000000/hdfs/2018
-rw-rw-rw-   1 root root       1087 2018-06-12 03:26 cosn://examplebucket-1250000000/hdfs/2018/LICENSE
-rw-rw-rw-   1 root root       2386 2018-06-12 03:26 cosn://examplebucket-1250000000/hdfs/2018/ReadMe
drwxrwxrwx   - root root          0 1970-01-01 00:00 cosn://examplebucket-1250000000/hdfs/test
-rw-rw-rw-   1 root root       1087 2018-06-11 07:32 cosn://examplebucket-1250000000/hdfs/test/LICENSE
-rw-rw-rw-   1 root root       2386 2018-06-11 07:29 cosn://examplebucket-1250000000/hdfs/test/ReadMe
```

运行 MapReduce 自带的 wordcount，执行以下命令。

> !以下命令中 hadoop-mapreduce-examples-2.7.2.jar 是以2.7.2版本为例，若版本不同，请修改成对应的版本号。

```shell
bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.2.jar wordcount cosn://example/mr/input cosn://example/mr/output3
```

执行成功会返回统计信息，示例如下：

```shell
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
