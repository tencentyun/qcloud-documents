如果您细心对比过 JSON Java SDK 和 XML Java SDK 的文档，您会发现并不是一个简单的增量更新。XML Java SDK 在架构、可用性和安全性上有了非常大的提升，而且在易用性、健壮性和性能上也做了非常大的改进。如果您想要升级到 XML Java SDK，请参考下面的指引，完成 Java SDK 的升级工作。

## 功能对比

| 功能       | XML Java SDK         | JSON Java SDK                         |
| -------- | :------------: | :------------------:    |
| 文件上传 | 支持本地文件、字节流、输入流上传<br>默认覆盖上传<br>智能判断上传模式：简单上传最大支持5GB<br>分块上传最大支持48.82TB（50,000GB）| 只支持本地文件上传<br>可选择是否覆盖<br>需要手动选择是简单还是分片上传。<br>简单上传最大支持20MB<br>分片上传最大支持64GB |
| 文件删除 | 支持批量删除 | 只支持单文件删除 |
| 存储桶基本操作 | 创建存储桶<br>获取存储桶<br>删除存储桶   | 不支持 |
| 存储桶 ACL操作 | 设置存储桶 ACL<br>获取设置存储桶 ACL<br>删除设置存储桶 ACL   | 不支持 |
| 存储桶生命周期 | 创建存储桶生命周期<br>获取存储桶生命周期<br>删除存储桶生命周期 | 不支持 |
| 目录操作 | 不单独提供接口   | 创建目录<br>查询目录<br>删除目录 |

## 升级步骤
请按照以下步骤升级 Java SDK。

**1. 更新 Java SDK**

XML Java SDK 发布在 [maven](https://mvnrepository.com/artifact/com.qcloud/cos_api) 中央仓库，推荐您使用 maven 自动管理依赖方式引入。

在 maven 项目的 pom.xml 文件中添加如下依赖：

```xml
<!-- https://mvnrepository.com/artifact/com.qcloud/cos_api -->
<dependency>
    <groupId>com.qcloud</groupId>
    <artifactId>cos_api</artifactId>
    <version>5.x.x</version>
</dependency>

```

当然您也可以在 [maven](https://mvnrepository.com/artifact/com.qcloud/cos_api) 中央仓库中直接下载对应版本的 jar 包，手动加入到您的项目当中。


**2. 更改存储桶名称和可用区域简称**

XML Java SDK 的存储桶名称和可用区域简称与 JSON Java SDK 的不同，需要您进行相应的更改。

**存储桶 Bucket**

XML SDK 存储桶名称由两部分组成：用户自定义字符串和 APPID，两者以中划线“-”相连。
例如 `examplebucket-1250000000`，其中 `examplebucket` 为用户自定义字符串，`1250000000` 为 APPID。

>?APPID 是腾讯云账户的账户标识之一，用于关联云资源。在用户成功申请腾讯云账户后，系统自动为用户分配一个 APPID。可通过 [腾讯云控制台](https://console.cloud.tencent.com/)【账号信息】查看 APPID。

设置 Bucket，请参考以下示例代码：

```java
COSCredentials cred = new BasicCOSCredentials("COS_SECRETID", "COS_SECRETKEY");
// 采用了新的region名字，可用region的列表可以在官网文档中获取，也可以参考下面的XML SDK和JSON SDK的地域对照表
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
COSClient cosclient = new COSClient(cred, clientConfig);
// bucket的名字需要的包含appid
String bucketName = "examplebucket-1250000000";

// 以下是向这个存储桶上传一个文件的示例
String key = "docs/exampleobject.doc";
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

**存储桶可用区域简称 Region**
XML SDK 的存储桶可用区域简称发生了变化，不同区域在 JSON SDK 和 XML SDK 中的对应关系请查看下表：

| 地域       | XML SDK 地域简称         | JSON SDK 地域简称                         |
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

**3. 更改 API**
升级到 XML SDK 之后，一些操作的 API 发生了变化，请您根据实际需求进行相应的更改。同时我们做了封装让 SDK 更加易用，具体请参考我们的示例和 [接口文档](https://cloud.tencent.com/document/product/436/12263)。

API 主要有以下变化：

**1）没有单独的目录接口**

在 XML SDK 中，不再提供单独的目录接口。对象存储中本身是没有文件夹和目录的概念的，对象存储不会因为上传对象`project/a.txt` 而创建一个 project 文件夹。为了满足用户使用习惯，对象存储在控制台、COS browser 等图形化工具中模拟了「文件夹」或「目录」的展示方式，具体实现是通过创建一个键值为`project/`，内容为空的对象，在展示方式上模拟了传统文件夹。

例如：上传对象`project/doc/a.txt`，分隔符`/`会模拟「文件夹」的展示方式，于是可以看到控制台上出现「文件夹」project 和 doc，其中 doc 是 project 下一级「文件夹」，并包含 a.txt 文件。

因此，如果您的应用场景只是上传文件，可以直接上传即可，不需要先创建文件夹。使用场景里面有文件夹的概念，则需要提供创建文件夹的功能，您可以上传一个路径以`/`结尾的0KB 文件。这样在您调用 GetBucket 接口时，就可以将该文件当做文件夹。

**2）TransferManager**

在 XML Java SDK 中，我们封装了上传、下载和复制操作，命名为`TransferManager`，优化了 API 设计和传输性能，建议您直接使用。

`TransferManager`的主要特性有：

- 支持上传下载过程的暂停和恢复；
- 支持根据文件大小只能选择简单上传还是分片上传，您可以设置该判断临界；
- 支持任务状态的监听。

使用`TransferManager`上传的示例代码：

```java
TransferManager transferManager = new TransferManager(cosclient, threadPool);

String key = "docs/exampleobject.doc";
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

**3）签名算法不同**

通常您不需要手动计算签名，但如果您将 SDK 的签名返回给前端使用，请注意我们的签名算法发生了改变。签名不再区分单次和多次签名，而是通过设置签名的有效期来保证安全性。具体的算法请参考 [XML 请求签名](https://cloud.tencent.com/document/product/436/7778) 文档。

**4）新增 API**

XML Java SDK 新增 API，您可根据需求进行调用。包括：

* 存储桶的操作，如 createBucket、GetBucket（List Objects）、ListBuckets 等。
* 存储桶 ACL 的操作，如 getBucketAcl、setBucketAcl 等。
* 存储桶生命周期的操作，如 setBucketLifecycleConfiguration、getBucketLifecycleConfiguration、 deleteBucketLifecycleConfiguration 等。

了解更多请查看 [Java SDK 接口文档](https://cloud.tencent.com/document/product/436/12263)。
