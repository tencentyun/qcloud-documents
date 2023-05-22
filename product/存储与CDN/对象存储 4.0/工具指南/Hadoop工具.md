## 功能说明

Hadoop-COS 基于腾讯云对象存储（Cloud Object Storage，COS）实现了标准的 Hadoop 文件系统，可以为 Hadoop、Spark 以及 Tez 等大数据计算框架集成 COS 提供支持，使其能够跟访问 HDFS 文件系统时相同，读写存储在 COS 上的数据。

Hadoop-COS 使用 cosn 作为 URI 的 scheme，因此也称为 Hadoop-COS 为 CosN 文件系统。


## 使用环境

#### 系统环境

支持 Linux、Windows 和 macOS 系统。

#### 软件依赖

Hadoop-2.6.0及以上版本。

>?
- 目前 Hadoop-COS 已经正式被 Apache Hadoop-3.3.0 [官方集成](https://hadoop.apache.org/docs/r3.3.0/hadoop-cos/cloud-storage/index.html)。
- 在 Apache Hadoop-3.3.0 之前版本或 CDH 集成 Hadoop-cos jar 包后，需要重启 NodeManager 才能加载到 jar 包。
-  需要编译具体 Hadoop 版本的 jar 包时，可更改 pom 文件中 hadoop.version 进行编译。



## 下载与安装

#### 获取 Hadoop-COS 分发包及其依赖

下载地址：[Hadoop-COS release](https://github.com/tencentyun/hadoop-cos/releases)。

#### 安装 Hadoop-COS 插件

1. 将 `hadoop-cos-{hadoop.version}-{version}.jar` 和 `cos_api-bundle-{version}.jar` 拷贝到 `$HADOOP_HOME/share/hadoop/tools/lib`下。
>? 根据 Hadoop 的具体版本选择对应的 jar 包，若 release 中没有提供匹配版本的 jar 包，可自行通过修改 pom 文件中 Hadoop 版本号，重新编译生成。
>
2. 修改 hadoop-env.sh 文件。进入 `$HADOOP_HOME/etc/hadoop` 目录，编辑 hadoop-env.sh 文件，增加以下内容，将 cosn 相关 jar 包加入 Hadoop 环境变量：
```shell
for f in $HADOOP_HOME/share/hadoop/tools/lib/*.jar; do
  if [ "$HADOOP_CLASSPATH" ]; then
    export HADOOP_CLASSPATH=$HADOOP_CLASSPATH:$f
  else
    export HADOOP_CLASSPATH=$f
  fi
done
```

## 配置方法


### Hadoop 配置


修改 `$HADOOP_HOME/etc/hadoop/core-site.xml`，增加 COS 相关用户和实现类信息，例如：

```xml
<configuration>
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
            4. org.apache.hadoop.fs.auth.SessionTokenCredentialProvider
            5. org.apache.hadoop.fs.auth.CVMInstanceCredentialsProvider
            6. org.apache.hadoop.fs.auth.CPMInstanceCredentialsProvider
            7. org.apache.hadoop.fs.auth.EMRInstanceCredentialsProvider
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
        <name>fs.cosn.upload.buffer</name>
        <value>mapped_disk</value>
        <description>The type of upload buffer. Available values: non_direct_memory, direct_memory, mapped_disk</description>
    </property>

    <property>
        <name>fs.cosn.upload.buffer.size</name>
        <value>134217728</value>
        <description>The total size of the upload buffer pool. -1 means unlimited.</description>
    </property>
	
    <property>
    	<name>fs.cosn.upload.part.size</name>
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
  
    <property>
        <name>fs.cosn.client-side-encryption.enabled</name>
        <value></value>
        <description>Enable or disable the client encryption function</description>
    </property>
  
    <property>
        <name>fs.cosn.client-side-encryption.public.key.path</name>
        <value>/xxx/xxx.key</value>
        <description>The direct path to the public key</description>
    </property>
  
     <property>
        <name>fs.cosn.client-side-encryption.private.key.path</name>
        <value>/xxx/xxx.key</value>
        <description>The direct path to the private key</description>
    </property>
      
</configuration>
```

其中 fs.defaultFS 不建议在生产环境进行配置，若您需要用于部分测试场景（例如 hive-testbench 等），可添加如下配置信息：

```
<property>
          <name>fs.defaultFS</name>
          <value>cosn://examplebucket-1250000000</value>
        <description>
             This option is not advice to config, this only used for some special test cases.
        </description>
</property>
```



### 配置项说明

|                     属性键                      | 说明                                                         |                            默认值                            | 必填项 |
| :---------------------------------------------: | :----------------------------------------------------------- | :----------------------------------------------------------: | :----: |
|     fs.cosn.userinfo.secretId/secretKey     | 填写您账户的 API 密钥信息。可登录 [访问管理控制台](https://console.cloud.tencent.com/capi) 查看云 API 密钥。 |                              无                              |   是   |
|        fs.cosn.credentials.provider         | 配置 SecretId 和 SecretKey 的获取方式。当前支持如下获取方式：<ol  style="margin: 0;"><li>org.apache.hadoop.fs.auth.SessionCredentialProvider：从请求 URI 中获取 secret id 和 secret key。其格式为：`cosn://{secretId}:{secretKey}@examplebucket-1250000000/`。</li><li>org.apache.hadoop.fs.auth.SimpleCredentialProvider：从 core-site.xml 配置文件中读取 fs.cosn.userinfo.secretId 和 fs.cosn.userinfo.secretKey 来获取 SecretId 和 SecretKey。</li><li>org.apache.hadoop.fs.auth.EnvironmentVariableCredentialProvider：从系统环境变量 COS_SECRET_ID 和 COS_SECRET_KEY 中获取。</li><li>org.apache.hadoop.fs.auth.SessionTokenCredentialProvider：使用 [临时密钥形式](https://cloud.tencent.com/document/product/436/14048) 访问。</li><li>org.apache.hadoop.fs.auth.CVMInstanceCredentialsProvider：利用腾讯云云服务器（CVM）绑定的角色，获取访问 COS 的临时密钥。</li><li>org.apache.hadoop.fs.auth.CPMInstanceCredentialsProvider：利用腾讯云黑石物理机（CPM）绑定的角色，获取访问 COS 的临时密钥。</li><li>org.apache.hadoop.fs.auth.EMRInstanceCredentialsProvider：利用腾讯云 EMR 实例绑定的角色，获取访问 COS 的临时密钥。</li><li>org.apache.hadoop.fs.auth.RangerCredentialsProvider 使用 ranger 进行获取密钥。</li></ol> | 如果不指定该配置项，默认会按照<br>以下顺序读取：<ol  style="margin: 0;"><li>org.apache.hadoop.fs.auth.SessionCredentialProvider</li><li>org.apache.hadoop.fs.auth.SimpleCredentialProvider</li><li>org.apache.hadoop.fs.auth.EnvironmentVariableCredentialProvider</li><li>org.apache.hadoop.fs.auth.SessionTokenCredentialProvider</li><li>org.apache.hadoop.fs.auth.CVMInstanceCredentialsProvider</li><li>org.apache.hadoop.fs.auth.CPMInstanceCredentialsProvider</li><li>org.apache.hadoop.fs.auth.EMRInstanceCredentialsProvider</li></ol> |   否   |
|                fs.cosn.useHttps                 | 配置是否使用 HTTPS 作为与 COS 后端的传输协议。               |                             true                             |   否   |
|                  fs.cosn.impl                   | cosn 对 FileSystem 的实现类，固定为 org.apache.hadoop.fs.CosFileSystem。 |                              无                              |   是   |
|       fs.AbstractFileSystem.cosn.impl       | cosn 对 AbstractFileSystem 的实现类，固定为 org.apache.hadoop.fs.CosN。 |                              无                              |   是   |
|              fs.cosn.bucket.region              | 请填写待访问存储桶的地域信息，枚举值请参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224) 中的地域简称，<br>例如：ap-beijing、ap-guangzhou 等。兼容原有配置：fs.cosn.userinfo.region。 |                              无                              |   是   |
|       fs.cosn.bucket.endpoint_suffix        | 指定要连接的 COS endpoint，该项为非必填项目。对于公有云 COS 用户而言，<br>只需要正确填写上述的 region 配置即可。兼容原有配置：fs.cosn.userinfo.endpoint_suffix。配置该项时请删除 fs.cosn.bucket.region 配置项 endpoint 才能生效。 |                              无                              |   否   |
|                 fs.cosn.tmp.dir                 | 请设置一个实际存在的本地目录，运行过程中产生的临时文件会暂时放于此处。 |                       /tmp/hadoop_cos                        |   否   |
|          fs.cosn.upload.part.size           | CosN 文件系统每个 block 的大小，也是分块上传的每个 part size 的大小。由于 COS 的分块上传最多只能支持10000块，因此需要预估最大可能使用到的单文件大小。<br>例如，part size 为8MB时，最大能够支持78GB的单文件上传。 part size 最大可以支持到2GB，即单文件最大可支持19TB。 |                        8388608（8MB）                        |   否   |
|            fs.cosn.upload.buffer            | CosN 文件系统上传时依赖的缓冲区类型。当前支持三种类型的缓冲区：非直接内存缓冲区（non_direct_memory），<br>直接内存缓冲区（direct_memory），磁盘映射缓冲区（mapped_disk）。非直接内存缓冲<br>区使用的是 JVM 堆内存，直接内存缓冲区使用的是堆外内存，而磁盘映射缓冲区则是基于内存文件映射得到的缓冲区。 |                         mapped_disk                          |   否   |
|         fs.cosn.upload.buffer.size          | CosN 文件系统上传时依赖的缓冲区大小，如果指定为-1，则表示不限制缓冲区。若不<br>限制缓冲区大小，则缓冲区的类型必须为 mapped_disk。如果指定大小大于0，则要求该值至少大于等于一个 block 的大小。兼容原有配置 fs.cosn.buffer.size。 |                              -1                              |   否   |
|               fs.cosn.block.size                | CosN 文件系统 block size。                                   |                      134217728（128MB）                      |   否   |
|         fs.cosn.upload_thread_pool          | 文件流式上传到 COS 时，并发上传的线程数目。                  |                              10                              |   否   |
|          fs.cosn.copy_thread_pool           | 目录拷贝操作时，可用于并发拷贝和删除文件的线程数目。         |                              3                               |   否   |
|        fs.cosn.read.ahead.block.size        | 预读块的大小。                                               |                        1048576（1MB）                        |   否   |
|        fs.cosn.read.ahead.queue.size        | 预读队列的长度。                                             |                              8                               |   否   |
|               fs.cosn.maxRetries                | 访问 COS 出现错误时，最多重试的次数。                        |                             200                              |   否   |
|       fs.cosn.retry.interval.seconds        | 每次重试的时间间隔。                                         |                              3                               |   否   |
|  fs.cosn.server-side-encryption.algorithm   | 配置 COS 服务端加密算法，支持 SSE-C 和 SSE-COS，默认为空，不加密。 |                              无                              |   否   |
|     fs.cosn.server-side-encryption.key      | 当开启 COS 的 SSE-C 服务端加密算法时，必须配置 SSE-C 的密钥，<br>密钥格式为 base64 编码的 AES-256 密钥，默认为空，不加密。 |                              无                              |   否   |
|     fs.cosn.client-side-encryption.enabled      | 是否开启客户端加密，默认不开启。开启后必须配置客户端加密的公钥和私钥。此时无法使用 append、truncate 接口。 |                            false                             |   否   |
| fs.cosn.client-side-encryption.public.key.path  | 客户端加密公钥文件的绝对路径                                 |                              无                              |   否   |
| fs.cosn.client-side-encryption.private.key.path | 客户端加密私钥文件的绝对路径                                 |                              无                              |   否   |
|       fs.cosn.crc64.checksum.enabled        | 是否开启 CRC64 校验。默认不开启，此时无法使用 hadoop fs -checksum 命令获取文件的 CRC64 校验值。 |                            false                             |   否   |
|       fs.cosn.crc32c.checksum.enabled       | 是否开启 CRC32C 校验。默认不开启，此时无法使用 hadoop fs -checksum 命令获取文件的 CRC32C 校验值，只能开启一种校验方式：crc32c 或 crc64。 |                            false                             |   否   |
|              fs.cosn.traffic.limit              | 上传带宽的控制选项，819200 - 838860800 bits/s，默认值为-1，默认表示不限制。 |                              无                              |   否   |


#### Bucket 独立配置项

背景：跨地域访问不同的 bucket，每个 bucket 的配置项不同，为此支持了一次配置，访问多个 bucket 的需求。
核心：单独设置 bucket 维度的配置优先使用独立配置项，如果没有设置独立配置项则使用原配置，如果原配置没有设置则使用默认配置。

下面示例是给 examplebucket-1250000000 单独设置 fs.cosn.upload.buffer 的配置项：
```shell
fs.cosn.bucket.examplebucket-1250000000.upload.buffer  ***
```

>?
>这里 fs.cosn.upload.buffer 的 subkey（trim fs.cosn.) 是 upload.buffer， 则 bucket 的独立配置项是 `fs.cosn.bucket.<bucket-appid>.<subkey>`。

使用方式：
```shell
hadoop fs -ls cosn://examplebucket-1250000000/ 
```
	
##### 简化 Bucket 独立配置项（适用于普通存储桶）

通过 `cosn://<bucket>/` 方式进行访问。

下面示例是给 examplebucket-1250000000 单独设置 fs.cosn.upload.buffer 的配置项：
```shell
fs.cosn.userinfo.appid 123456
fs.cosn.bucket.testbucket.upload.buffer  ***
```

>?
>这里 fs.cosn.upload.buffer 的 subkey（trim fs.cosn.)是 upload.buffer，但由于已经设置了 appid，则 bucket 的独立配置项可以简化为 `fs.cosn.bucket.<bucket>.<subkey>`。

使用方式：
```shell
hadoop fs -ls cosn://testbucket/ 
```
	
##### 简化 Bucket 独立配置项（适用于元数据加速存储桶）

通过 `cosn://<bucket>/` 方式进行访问。

下面示例是给 examplebucket-1250000000 单独设置 fs.cosn.upload.buffer 的配置项：

```shell
fs.cosn.userinfo.appid 123456
fs.cosn.trsf.fs.ofs.use.short.bucketname true
fs.cosn.bucket.testbucket.upload.buffer  ***
```

>?
这里 fs.cosn.upload.buffer 的 subkey（trim fs.cosn.) 是 upload.buffer，但由于已经设置了 appid，则 bucket 的独立配置项可以简化为 `fs.cosn.bucket.<bucket>.<subkey>`。

由于旧版本 OFS Java SDK 对挂载点格式进行了访问限制，只支持`<bucket-appid>`方式访问，所以需要更新依赖插件至最新版本才可使用。

依赖插件版本信息：
```shell
ofs java sdk >= 1.1.8
hadoop cos >= 8.3.0
```
使用方式：
```shell
hadoop fs -ls cosn://testbucket/ 
```


### 服务端加密

Hadoop-COS 支持服务端加密，目前提供两种加密方式：COS 托管密钥方式（SSE-COS）和用户自定义密钥方式（SSE-C），Hadoop-COS 的加密功能默认为关闭状态，用户可以选择开启，通过以下方式进行配置。

#### SSE-COS 加密

SSE-COS 加密即 COS 托管密钥的服务端加密，由腾讯云 COS 托管主密钥和管理数据。当使用 Hadoop-COS 时，用户可以在 `$HADOOP_HOME/etc/hadoop/core-site.xml` 文件中，增加以下配置来进行实现 SSE-COS 加密。

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

>!
>- Hadoop-COS 的 SSE-C 服务端加密依赖于 COS 的 SSE-C 服务端加密。因此，Hadoop-COS 不存储用户提供的加密密钥。同时需要值得注意的是，COS 的 SSE-C 服务端加密方式不存储用户提供的加密密钥，而是存储加密密钥添加了随机数据的 HMAC 值，该值用于验证用户访问对象的请求。COS 无法使用随机数据的 HMAC 值来推导出加密密钥的值或解密加密对象的内容。因此，如果用户丢失了加密密钥，则无法再次获取到该对象。
>- Hadoop-COS 配置了 SSE-C 服务端加密算法时，必须在 fs.cosn.server-side-encryption.key 配置项中配置 SSE-C 的密钥，密钥格式为 base64 编码的 AES-256 密钥。
>

### 客户端加密

COSN 客户端加密采用 RSA 加密方式，密钥分为公钥和私钥，其中公钥用于文件加密过程，私钥用于文件解密过程。在上传文件时，COSN 会生成一个随机密钥，并用该密钥对文件进行对称加密。公钥会对该密钥进行加密，并将加密后的信息保存在文件元数据中。在下载文件时，COSN 会使用私钥从文件元数据中得到加密随机密钥进行解密，再使用解密后的随机密钥对文件进行对此解密。公钥和私钥只参与客户端本地计算，不会在网络上进行传输或保存在服务端，以保证主密钥的数据安全。

- 使用客户端加密功能时，您需要对主密钥的完整性和正确性负责。在对加密数据进行复制或者迁移时，您需要对加密元信息的完整性和正确性负责。因您维护不当导致主密钥用错或丢失，加密元信息出错或丢失，从而导致加密数据无法解密所引起的一切损失和后果均由您自行承担。
- 开启客户端加密后，不再支持 append、truncate 接口。
- 使用关闭了客户端加密功能的客户端对加密文件进行 `hadoop fs -cp` 命令，会丢失加密信息。
- 开启客户端加密后，默认关闭 CRC 文件校验，默认关闭异步文件分块上传。

当使用 Hadoop-COS 时，用户可以在`$HADOOP_HOME/etc/hadoop/core-site.xml`文件中，增加以下配置来进行实现 SSE-COS 加密。

```shell
 <property>
        <name>fs.cosn.client-side-encryption.enabled</name>
        <value>true</value>
        <description>Enable or disable the client encryption function</description>
    </property>
  
    <property>
        <name>fs.cosn.client-side-encryption.public.key.path</name>
        <value>/xxx/xxx.key</value>
        <description>The direct path to the public key</description>
    </property>
  
     <property>
        <name>fs.cosn.client-side-encryption.private.key.path</name>
        <value>/xxx/xxx.key</value>
        <description>The direct path to the private key</description>
    </property>
```

可使用以下代码生成密钥：

```java
import java.io.FileOutputStream;
import java.io.IOException;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.NoSuchAlgorithmException;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.security.SecureRandom;
import java.security.spec.PKCS8EncodedKeySpec;
import java.security.spec.X509EncodedKeySpec;

// 使用非对称秘钥 RSA 加密每次生成的随机对称秘钥
public class BuildKey {
    private static final SecureRandom srand = new SecureRandom();
    private static void buildAndSaveAsymKeyPair(String pubKeyPath, String priKeyPath) throws IOException, NoSuchAlgorithmException {
        KeyPairGenerator keyGenerator = KeyPairGenerator.getInstance("RSA");
        keyGenerator.initialize(1024, srand);
        KeyPair keyPair = keyGenerator.generateKeyPair();
        PrivateKey privateKey = keyPair.getPrivate();
        PublicKey publicKey = keyPair.getPublic();

        X509EncodedKeySpec x509EncodedKeySpec = new X509EncodedKeySpec(publicKey.getEncoded());
        FileOutputStream fos = new FileOutputStream(pubKeyPath);
        fos.write(x509EncodedKeySpec.getEncoded());
        fos.close();

        PKCS8EncodedKeySpec pkcs8EncodedKeySpec = new PKCS8EncodedKeySpec(privateKey.getEncoded());
        fos = new FileOutputStream(priKeyPath);
        fos.write(pkcs8EncodedKeySpec.getEncoded());
        fos.close();
    }


    public static void main(String[] args) throws Exception {

        String pubKeyPath = "pub.key";
        String priKeyPath = "pri.key";
        buildAndSaveAsymKeyPair(pubKeyPath, priKeyPath);
    }
}

```

## 使用方法


### 使用示例

命令格式为 `hadoop fs -ls -R cosn://<BucketName-APPID>/<路径>`，或 `hadoop fs -ls -R /<路径>`（需要配置 `fs.defaultFS` 选项为 `cosn://BucketName-APPID`），下例中以名称为 examplebucket-1250000000 的 bucket 为例，可在其后面加上具体路径。

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

>! 以下命令中 hadoop-mapreduce-examples-2.7.2.jar 是以2.7.2版本为例，若版本不同，请修改成对应的版本号。
>

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

### 通过 Java 代码访问 COSN

```
package com.qcloud.chdfs.demo;

import org.apache.commons.io.IOUtils;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FSDataOutputStream;
import org.apache.hadoop.fs.FileChecksum;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

import java.io.IOException;
import java.net.URI;
import java.nio.ByteBuffer;

public class Demo {
    private static FileSystem initFS() throws IOException {
        Configuration conf = new Configuration();
        // COSN 的配置项可参见 https://cloud.tencent.com/document/product/436/6884#hadoop-.E9.85.8D.E7.BD.AE
        // 以下配置是必填项
        conf.set("fs.cosn.impl", "org.apache.hadoop.fs.CosFileSystem");
        conf.set("fs.AbstractFileSystem.cosn.impl", "org.apache.hadoop.fs.CosN");
        conf.set("fs.cosn.tmp.dir", "/tmp/hadoop_cos");
        conf.set("fs.cosn.bucket.region", "ap-guangzhou");
        conf.set("fs.cosn.userinfo.secretId", "AKXXXXXXXXXXXXXXXXX");
        conf.set("fs.cosn.userinfo.secretKey", "XXXXXXXXXXXXXXXXXX");
        conf.set("fs.ofs.user.appid", "XXXXXXXXXXX");
        // 其他配置参考官网文档 https://cloud.tencent.com/document/product/436/6884#hadoop-.E9.85.8D.E7.BD.AE
        // 是否开启 CRC64 校验。默认不开启，此时无法使用 hadoop fs -checksum 命令获取文件的 CRC64 校验值
        conf.set("fs.cosn.crc64.checksum.enabled", "true");
        String cosnUrl = "cosn://f4mxxxxxxxx-125xxxxxxx";
        return FileSystem.get(URI.create(cosnUrl), conf);
    }

    private static void mkdir(FileSystem fs, Path filePath) throws IOException {
        fs.mkdirs(filePath);
    }

    private static void createFile(FileSystem fs, Path filePath) throws IOException {
        // 创建一个文件（如果存在则将其覆盖）
        // if the parent dir does not exist, fs will create it!
        FSDataOutputStream out = fs.create(filePath, true);
        try {
            // 写入一个文件
            String content = "test write file";
            out.write(content.getBytes());
        } finally {
            IOUtils.closeQuietly(out);
        }
    }

    private static void readFile(FileSystem fs, Path filePath) throws IOException {
        FSDataInputStream in = fs.open(filePath);
        try {
            byte[] buf = new byte[4096];
            int readLen = -1;
            do {
                readLen = in.read(buf);
            } while (readLen >= 0);
        } finally {
            IOUtils.closeQuietly(in);
        }
    }

    private static void queryFileOrDirStatus(FileSystem fs, Path path) throws IOException {
        FileStatus fileStatus = fs.getFileStatus(path);
        if (fileStatus.isDirectory()) {
            System.out.printf("path %s is dir\n", path);
            return;
        }
        long fileLen = fileStatus.getLen();
        long accessTime = fileStatus.getAccessTime();
        long modifyTime = fileStatus.getModificationTime();
        String owner = fileStatus.getOwner();
        String group = fileStatus.getGroup();

        System.out.printf("path %s is file, fileLen: %d, accessTime: %d, modifyTime: %d, owner: %s, group: %s\n",
                path, fileLen, accessTime, modifyTime, owner, group);
    }
    
    private static void getFileCheckSum(FileSystem fs, Path path) throws IOException {
        FileChecksum checksum = fs.getFileChecksum(path);
        System.out.printf("path %s, checkSumType: %s, checkSumCrcVal: %d\n",
                path, checksum.getAlgorithmName(), ByteBuffer.wrap(checksum.getBytes()).getInt());
    }

    private static void copyFileFromLocal(FileSystem fs, Path cosnPath, Path localPath) throws IOException {
        fs.copyFromLocalFile(localPath, cosnPath);
    }

    private static void copyFileToLocal(FileSystem fs, Path cosnPath, Path localPath) throws IOException {
        fs.copyToLocalFile(cosnPath, localPath);
    }

    private static void renamePath(FileSystem fs, Path oldPath, Path newPath) throws IOException {
        fs.rename(oldPath, newPath);
    }

    private static void listDirPath(FileSystem fs, Path dirPath) throws IOException {
        FileStatus[] dirMemberArray = fs.listStatus(dirPath);

        for (FileStatus dirMember : dirMemberArray) {
            System.out.printf("dirMember path %s, fileLen: %d\n", dirMember.getPath(), dirMember.getLen());
        }
    }

    // 递归删除标志用于删除目录
    // 如果递归为 false 并且 dir 不为空，则操作将失败
    private static void deleteFileOrDir(FileSystem fs, Path path, boolean recursive) throws IOException {
        fs.delete(path, recursive);
    }

    private static void closeFileSystem(FileSystem fs) throws IOException {
        fs.close();
    }

    public static void main(String[] args) throws IOException {
        // 初始化文件
        FileSystem fs = initFS();

        // 创建文件
        Path cosnFilePath = new Path("/folder/exampleobject.txt");
        createFile(fs, cosnFilePath);

        // 读取文件
        readFile(fs, cosnFilePath);

        // 查询文件或目录
        queryFileOrDirStatus(fs, cosnFilePath);

        // 获取文件校验和
        getFileCheckSum(fs, cosnFilePath);

        // 从本地复制文件
        Path localFilePath = new Path("file:///home/hadoop/ofs_demo/data/exampleobject.txt");
        copyFileFromLocal(fs, cosnFilePath, localFilePath);

        // 获取文件到本地
        Path localDownFilePath = new Path("file:///home/hadoop/ofs_demo/data/exampleobject.txt");
        copyFileToLocal(fs, cosnFilePath, localDownFilePath);

        listDirPath(fs, cosnFilePath);
        // 重命名
        mkdir(fs, new Path("/doc"));
        Path newPath = new Path("/doc/example.txt");
        renamePath(fs, cosnFilePath, newPath);

        // 删除文件
        deleteFileOrDir(fs, newPath, false);

        // 创建目录
        Path dirPath = new Path("/folder");
        mkdir(fs, dirPath);

        // 在目录中创建文件
        Path subFilePath = new Path("/folder/exampleobject.txt");
        createFile(fs, subFilePath);

        // 列出目录
        listDirPath(fs, dirPath);

        // 删除目录
        deleteFileOrDir(fs, dirPath, true);
        deleteFileOrDir(fs, new Path("/doc"), true);

        // 关闭文件系统
        closeFileSystem(fs);
    }
}
```

## 常见问题


如果您在使用 Hadoop 工具过程中，有相关的疑问，请参见 [Hadoop 工具类常见问题](https://cloud.tencent.com/document/product/436/36897)。

