# 开发准备

## 相关资源

COS JAVA SDK GitHub地址 [github项目](https://github.com/tencentyun/cos-java-sdk-v5)

## 环境依赖

JDK 1.7, 1.8. 

JDK安装方式请参考 [JAVA安装与配置](https://cloud.tencent.com/document/product/436/10865)

## 安装SDK

- maven安装

pom.xml 添加依赖

```xml
<dependency>
            <groupId>com.qcloud</groupId>
            <artifactId>cos_api</artifactId>
            <version>5.2.0</version>
</dependency>
```

- 源码安装

从[github](https://github.com/tencentyun/cos-java-sdk-v5)下载源码, 通过maven导入。比如eclipse，依次选择File->Import->maven->Existing Maven Projects

## 卸载SDK

删除pom依赖或源码

# 快速入手

## 初始化客户端cosclient

设置用户的身份信息, appid, bucket所在的园区以及bucket名

```java
// 1 初始化身份信息(appid, secretId, secretKey)
COSCredentials cred = new BasicCOSCredentials("1250000", "AKIDXXXXXXXX", "1A2Z3YYYYYYYYYY");
// 2 设置bucket的区域, COS地域的简称请参照 https://www.qcloud.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
// 3 生成cos客户端
COSClient cosClient = new COSClient(cred, clientConfig);
// 设置bucket名
String bucketName = "mybucket";
```

## 上传文件

将本地文件或者已知长度的输入流内容上传到COS. 适用于图片类小文件上传(20MB以下), 最大支持5GB(含), 5GB以上请使用分块上传或高级API上传。请参照API文档put object

```java
// 简单文件上传, 最大支持5GB, 适用于小文件上传, 建议20M以下的文件使用该接口
// 大文件上传请参照API文档高级API上传
File localFile = new File("src/test/resources/len5M.txt");
// 指定要上传到COS上的路径
String key = "/upload_single_demo.txt";
PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, key, localFile);
PutObjectResult putObjectResult = cosClient.putObject(putObjectRequest);
```

## 下载文件

文件下载到本地或者获取下载文件下载输入流.

```java
// 指定要下载到的本地路径
File downFile = new File("src/test/resources/mydown.txt");
// 指定要下载的文件所在的bucket和路径
GetObjectRequest getObjectRequest = new GetObjectRequest(bucketName, key);
ObjectMetadata downObjectMeta = cosClient.getObject(getObjectRequest, downFile);
```

## 删除文件

删除COS上指定路径的文件.

```java
// 指定要删除的bucket和路径
cosClient.deleteObject(bucketName, key);
```

## 关闭客户端

关闭cosclient, 并释放后台线程(http连接的管理线程)

```
// 关闭客户端(关闭后台线程)
cosClient.shutdown();
```

