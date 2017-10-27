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

从[github](https://github.com/tencentyun/cos-java-sdk-v5)下载源码, 通过maven导入。比如eclipse，选择File->Import->maven->Existing Maven Projects

## 卸载SDK

删除pom依赖或源码

# 快速入手

```java
// 1 初始化身份信息
COSCredentials cred = new BasicCOSCredentials("1250000", "AKIDXXXXXXXX", "1A2Z3YYYYYYYYYY");
// 2 设置bucket的区域, COS地域的简称请参照 https://www.qcloud.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
// 3 生成cos客户端
COSClient cosClient = new COSClient(cred, clientConfig);
// 操作API， 每一种API详情请参照JAVA SDK API文档.
// 或者参照Demo(https://github.com/tencentyun/cos-java-sdk-v5/blob/master/src/main/java/com/qcloud/cos/demo/Demo.java)

String bucketName = "mybucket";

// 上传object, 建议20M以下的文件使用该接口
File localFile = new File("src/test/resources/len5M.txt");
String key = "/upload_single_demo.txt";
PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, key, localFile);
PutObjectResult putObjectResult = cosClient.putObject(putObjectRequest);

// 下载object
File downFile = new File("src/test/resources/len5M_down.txt");
GetObjectRequest getObjectRequest = new GetObjectRequest(bucketName, key);
ObjectMetadata downObjectMeta = cosClient.getObject(getObjectRequest, downFile);

// 获取object属性
GetObjectMetadataRequest getObjectMetadataRequest =
        new GetObjectMetadataRequest(bucketName, key);
ObjectMetadata statObjectMeta = cosClient.getObjectMetadata(getObjectMetadataRequest);

// 删除object
DeleteObjectRequest deleteObjectRequest = new DeleteObjectRequest(bucketName, key);
cosClient.deleteObject(deleteObjectRequest);

// 上传文件(推荐), 支持根据文件的大小自动选择单文件上传或者分块上传
// 同时支持同时上传不同的文件
TransferManager transferManager = new TransferManager(cosClient);
localFile = new File("src/test/resources/len30M.txt");
// transfermanger upload是异步上传
key = "/upload_transfer_manager_demo.txt";
Upload upload = transferManager.upload(bucketName, key, localFile);
// 等待传输结束
upload.waitForCompletion();
transferManager.shutdownNow();

// list bucket下的成员
ObjectListing objectListing = cosClient.listObjects(bucketName);
List<COSObjectSummary> objectListSummary = objectListing.getObjectSummaries();

// 删除刚上传的文件
deleteObjectRequest = new DeleteObjectRequest(bucketName, key);
cosClient.deleteObject(deleteObjectRequest);

// 删除空bucket, bucket需要为空，不包含任何object
DeleteBucketRequest deleteBucketRequest = new DeleteBucketRequest(bucketName);
cosClient.deleteBucket(deleteBucketRequest);

// 关闭客户端(关闭后台线程)
cosClient.shutdown();
```

# 