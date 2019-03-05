## 开发前准备
### 相关资源
对象存储服务的 XML JAVA SDK 资源下载地址：[XML JAVA SDK](https://github.com/tencentyun/cos-java-sdk-v5)。
### 环境依赖

- SDK 支持 JDK 1.7, 1.8 及以上版本。
- JDK安装方式请参考 [JAVA 安装与配置](https://cloud.tencent.com/document/product/436/10865)

> 关于文章中出现的 SecretId、SecretKey、Bucket 等名称的含义和获取方式请参考：[COS 术语信息](https://cloud.tencent.com/document/product/436/7751)

###  安装 SDK
安装 SDK 的方式有两种：maven 安装和源码安装。

- maven安装
在 maven 工程中使用 pom.xml 添加相关依赖，内容如下：

```xml
<dependency>
            <groupId>com.qcloud</groupId>
            <artifactId>cos_api</artifactId>
            <version>5.2.0</version>
</dependency>
```

- 源码安装
从 [XML JAVA SDK](https://github.com/tencentyun/cos-java-sdk-v5) 下载源码，通过 maven 导入。比如 eclipse，依次选择 File->Import->maven->Existing Maven Projects。

###  卸载 SDK
卸载 SDK 的方式即删除 pom 依赖或源码。

## 快速入门

### 初始化客户端 cosclient

设置用户的身份信息， appid， bucket 所在的区域以及 bucket 名

```java
// 1 初始化身份信息(appid, secretId, secretKey)
COSCredentials cred = new BasicCOSCredentials("1250000", "AKIDXXXXXXXX", "1A2Z3YYYYYYYYYY");
// 2 设置 bucket 的区域, COS 地域的简称请参照 https://www.qcloud.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
// 3 生成 cos 客户端
COSClient cosClient = new COSClient(cred, clientConfig);
// 设置 bucket 名
String bucketName = "mybucket";
```

### 上传文件

将本地文件或者已知长度的输入流内容上传到 COS. 适用于图片类小文件上传（20 MB 以下），最大支持 5 GB （含）， 5 GB 以上请使用分块上传或高级 API 上传。请参照 API 文档 put object。

```java
// 简单文件上传, 最大支持 5 GB, 适用于小文件上传, 建议 20 M 以下的文件使用该接口
// 大文件上传请参照 API 文档高级 API 上传
File localFile = new File("src/test/resources/len5M.txt");
// 指定要上传到 COS 上的路径
String key = "/upload_single_demo.txt";
PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, key, localFile);
PutObjectResult putObjectResult = cosClient.putObject(putObjectRequest);
```

###  下载文件

文件下载到本地或者获取下载文件下载输入流。

```java
// 指定要下载到的本地路径
File downFile = new File("src/test/resources/mydown.txt");
// 指定要下载的文件所在的 bucket 和路径
GetObjectRequest getObjectRequest = new GetObjectRequest(bucketName, key);
ObjectMetadata downObjectMeta = cosClient.getObject(getObjectRequest, downFile);
```

###  删除文件

删除 COS 上指定路径的文件。

```java
// 指定要删除的 bucket 和路径
cosClient.deleteObject(bucketName, key);
```

###  关闭客户端

关闭 cosclient，并释放后台线程（http 连接的管理线程）。

```
// 关闭客户端(关闭后台线程)
cosClient.shutdown();
```

