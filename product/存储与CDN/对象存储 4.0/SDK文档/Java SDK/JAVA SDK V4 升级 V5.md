# 升级到 Java SDK V5

如果您细心对比过Java SDK V4 和 V5的文档，您会发现并不是一个简单的增量更新。COS V5 在架构、可用性和安全性上有了非常大的提升。我们的SDK在易用性、健壮性和性能上也做了非常大的改进。如果您想要升级到Java SDK V5，请参考下面的指引。

## 功能对比

| 功能       | V5         | V4                         |
| -------- | :------------: | :------------------:    |
| 文件上传 | 支持本地文件、字节流、输入流上传<br>默认覆盖上传<br>智能判断上传模式 | 只支持本地文件上传<br>可选择是否覆盖<br>需要手动选择是简单还是分片上传 |
| 文件下载 | 支持断点续传 | 不支持断点续传 |
| 文件删除 | 支持批量删除 | 只支持单文件删除 |
| 存储桶基本操作 | 创建存储桶<br>获取存储桶<br>删除存储桶   | 不支持 |
| 存储桶ACL操作 | 设置存储桶ACL<br>获取设置存储桶ACL<br>删除设置存储桶ACL   | 不支持 |
| 存储桶生命周期 | 创建存储桶生命周期<br>获取存储桶生命周期<br>删除存储桶生命周期 | 不支持 |
| 目录操作 | 不支持   | 创建目录<br>查询目录<br>删除目录 |

### 总览

1. 更新您的Java SDK
2. 根据指引修改SDK的初始化方式
3. 我们的`存储桶名称`和`可用区域简称`有了更新，请对应修改
4. 一些操作的 API 发生了变化，我们了封装让 SDK 更加易用，具体参考我们的示例和 [接口文档](https://cloud.tencent.com/document/product/436/12263)

### 更新SDK

COS V5 Java SDK 发布在maven中央仓库中，推荐使用maven自动管理依赖方式引入:

在您的maven项目的pom.xml文件中添加如下依赖：

```xml
<!-- https://mvnrepository.com/artifact/com.qcloud/cos_api -->
<dependency>
    <groupId>com.qcloud</groupId>
    <artifactId>cos_api</artifactId>
    <version>5.x.x</version>
</dependency>

```

maven仓库的版本列表：[https://mvnrepository.com/artifact/com.qcloud/cos_api](https://mvnrepository.com/artifact/com.qcloud/cos_api)

当然您也可以在maven中央仓库中直接下载对应版本的jar包，手动加入到您的项目当中。下载地址：[https://mvnrepository.com/artifact/com.qcloud/cos_api](https://mvnrepository.com/artifact/com.qcloud/cos_api)



### Bucket和Region的变化

V5 的存储桶名称发生了变化，在 V5 中，存储桶名称由两部分组成：用户自定义字符串 和 APPID，两者以中划线“-”相连。例如 `mybucket1-1250000000`，其中 `mybucket1` 为用户自定义字符串，`1250000000` 为 APPID。APPID 是腾讯云账户的账户标识之一，用于关联云资源。在用户成功申请腾讯云账户后，系统自动为用户分配一个 APPID。可通过 腾讯云控制台 【账号信息】查看 APPID。

在设置 Bucket 时，请参考下面的示例代码：

```java
COSCredentials cred = new BasicCOSCredentials("AKIDXXXXXXXX", "1A2Z3YYYYYYYYYY");
// 采用了新的region名字，可用region的列表可以在官网文档中获取，也可以参考下面的V5和V4的地域对照表
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
COSClient cosclient = new COSClient(cred, clientConfig);
// bucket的名字需要的包含appid
String bucketName = "mybucket-1251668577";

// 以下是向这个存储桶上传一个文件的示例
String key = "aaa/bbb.txt";
File localFile = new File("src/test/resources/len10M.txt");
PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, key, localFile);
// 设置存储类型, 默认是标准(Standard), 低频(standard_ia)
putObjectRequest.setStorageClass(StorageClass.Standard_IA);
try {
	PutObjectResult putObjectResult = cosclient.putObject(putObjectRequest);
	// putobjectResult会返回文件的etag
    String etag = putObjectResult.getETag();
} catch (CosServiceException e) {
	e.printStackTrace();
} catch (CosClientException e) {
	e.printStackTrace();
}

// 关闭客户端
cosclient.shutdown();

```

V5的存储桶可用区域简称发生了变化，下面列出了不同区域在V4和V5中的对应关系：

| 地域       | V5 地域简称         | V4 地域简称                         |
| -------- | ------------ | ---------------------------------------- |
| 北京一区（华北） | ap-beijing-1 | tj |
| 北京       | ap-beijing   | bj |
| 上海（华东）   | ap-shanghai  | sh |
| 广州（华南）   | ap-guangzhou | gz |
| 成都（西南）   | ap-chengdu   | cd |
| 重庆       | ap-chongqing | 无 |
| 新加坡      | ap-singapore | sgp |
| 香港       | ap-hongkong  | hk |
| 多伦多      | na-toronto   | ca |
| 法兰克福     | eu-frankfurt | ger |
| 孟买       | ap-mumbai    | 无 |
| 首尔       | ap-seoul     | 无 |
| 硅谷       | na-siliconvalley     | 无 |
| 弗吉尼亚       | na-ashburn     | 无 |
| 曼谷       | ap-bangkok     | 无 |
| 莫斯科       | eu-moscow     | 无 |

在初始化`COSClient`的时候，将存储桶所在区域的简称设置到`ClientConfig`中：

```java
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
COSClient cosclient = new COSClient(cred, clientConfig);

```

### API变化

#### 不再支持目录操作

由于对象存储本身是没有目录和文件夹的概念的，所以COS不会因为上传对象`project/a.txt`而创建一个名为`project`的目录。为了满足文件系统用户的使用习惯，COS在控制台、COS browser等图形化工具中模拟了「文件夹」或「目录」的展示方式，于是可以看到控制台上出现`project`的文件夹，其中包含了`a.txt`

因此，如果您的应用场景只是上传文件，可以直接上传即可，不需要先创建文件夹。

如果您的使用场景里面有文件夹的概念，需要提供创建文件夹的功能，您可以上传一个路径以 '/' 结尾的 0KB 文件。这样在您调用 `GetBucket` 接口时，就可以将这样的文件当做文件夹。

#### TransferManager

在 COS V5 SDK中，我们封装了上传、下载和复制操作，命名为`TransferManager`，对 API 设计和传输性能都能做了优化，建议您直接使用。

`TransferManager`的主要特性有：

- 支持断点下载
- 支持根据文件大小只能选择简单上传还是分片上传，您可以设置该判断临界。
- 支持任务状态的监听

使用`TransferManager`上传的示例代码：

```java
TransferManager transferManager = new TransferManager(cosclient, threadPool);

String key = "aaa/bbb.txt";
File localFile = new File("src/test/resources/len30M.txt");
PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, key, localFile);
try {
    // 返回一个异步结果Upload, 可同步的调用waitForUploadResult等待upload结束, 成功返回UploadResult, 失败抛出异常.
    Upload upload = transferManager.upload(putObjectRequest);
    Thread.sleep(10000);
    // 暂停任务
    PersistableUpload persistableUpload = upload.pause();
    // 恢复上传
    upload = transferManager.resumeUpload(persistableUpload);
    // 可以显示上传进度
    showTransferProgress(upload);
    // 等待上传任务完成
    UploadResult uploadResult = upload.waitForUploadResult();
    System.out.println(uploadResult.getETag());

    // 另外也支持取消上传任务
    transferManager.cancel();
} catch (CosServiceException e) {
    e.printStackTrace();
} catch (CosClientException e) {
    e.printStackTrace();
} catch (InterruptedException e) {
    e.printStackTrace();
}

ransferManager.shutdownNow();
cosclient.shutdown();

```

#### 新增的API

V5增加了很多新的API，包括：

* 存储桶的操作，如 createBucket, GetBucket(List Objects), ListBuckets 等
* 存储桶ACL的操作，如 getBucketAcl，setBucketAcl 等
* 存储桶生命周期的操作，如 setBucketLifecycleConfiguration, getBucketLifecycleConfiguration, deleteBucketLifecycleConfiguration 等

具体可以参考文件的[Java SDK 接口文档](https://cloud.tencent.com/document/product/436/12263)