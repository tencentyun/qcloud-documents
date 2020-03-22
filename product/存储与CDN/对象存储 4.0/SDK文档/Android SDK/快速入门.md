## 下载与安装

#### 相关资源

#### 源码和示例工程

- COS Android SDK 相关源码请参见 [COS Android SDK Github](https://github.com/tencentyun/qcloud-sdk-android)。
- 示例 demo 请参见 [COS Android SDK 示例工程](https://github.com/tencentyun/qcloud-sdk-android-samples)。

#### 更新日志

COS Android SDK 更新日志请参见 [COS Android SDK 更新日志](https://github.com/tencentyun/qcloud-sdk-android/blob/master/CHANGELOG.md)。

#### 环境依赖

1. SDK 支持 Android 2.2及以上版本的手机系统。
2. 手机必须要有网络（GPRS、3G 、4G 或 Wi-Fi 网络等）。
3. 手机存储空间不足会使部分功能无法正常工作，请预留一定的手机存储空间。
4. 从访问管理控制台中的 [API 密钥管理](https://console.cloud.tencent.com/capi) 页面获取 SecretId、SecretKey、APPID 信息。


>?
>- 关于文章中出现的 SecretId、SecretKey、Bucket 等名称的含义和获取方式请参见 [COS 术语信息](https://cloud.tencent.com/document/product/436/7751)。
>- SDK 中常用的包有：`com.tencent.cos.xml.*; com.tencent.cos.xml.exception.*; com.tencent.cos.xml.model.*; com.tencent.cos.xml.model.bucket.*; com.tencent.cos.xml.model.object.*; com.tencent.cos.xml.transfer.*; com.tencent.cos.xml.listener.*;com.tencent.qcloud.core.auth.*.`

#### 安装 SDK

#### 配置权限

使用该 SDK 需要网络、存储等相关的一些访问权限，可在 AndroidManifest.xml 中添加如下权限声明（Android 5.0 以上还需要动态获取权限）：
```
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
```

#### 集成 SDK

您可以通过两个方式集成 SDK：[自动集成](#step1) 和 [手动集成](#step2)。

<span id="step1"></span>
#### 自动集成（推荐）

1. 在应用的根目录下的 build.gradle 中添加依赖：
```
dependencies {
	...
    // 增加这行
    compile 'com.tencent.qcloud:cosxml:5.4.31'
}
```
2. 若您只使用上传、下载和复制功能，则可以使用简化版的 SDK ：
首先在根目录下的 build.gradle 中添加 maven 仓库：
```
allprojects {
    repositories {
        // 添加 maven 仓库
        maven {
            url "https://dl.bintray.com/tencentqcloudterminal/maven"
        }
        google()
        jcenter()
    }
}
```
>?暂时需要额外添加 maven 仓库地址，后续会尽快同步到 jcenter 仓库中。

	然后将上述步骤1的依赖改成如下依赖：
	```
	dependencies {
	 ...
	 // 增加这行
	 compile 'com.tencent.qcloud:cosxml-lite:5.4.31'
	}
	```
3. 为了持续跟踪和优化 SDK 的质量，给您带来更好的使用体验，我们在 SDK 中引入了腾讯移动分析（mta），若是想关闭该功能，则在应用的根目录下的 build.gradle 中添加依赖：
```
dependencies {
	...
    // 增加这行
   compile ('com.tencent.qcloud:cosxml:5.4.30'){
        exclude group:'com.tencent.qcloud', module: 'mtaUtils' //关闭 mta 上报功能
    }
}
```
简化版 SDK 代码如下：
```
dependencies {
	...
    // 增加这行
    compile ('com.tencent.qcloud:cosxml-lite:5.4.30'){
        exclude group:'com.tencent.qcloud', module: 'mtaUtils' //关闭 mta上报功能
    }
}
```

<span id="step2"></span>
#### 手动集成
需要在工程项目中导入下列 jar 包，存放在 libs 文件夹下：
- cos-android-sdk.jar
- qcloud-foundation.jar
- bolts-tasks.jar
- okhttp.jar（3.9及以上版本）
- okio.jar（1.13.0及以上版本）
- mtaUtils.jar
- mid-sdk.jar
- mta-android-sdk.jar
- LogUtils.aar

您可以在这里 [COS XML Android SDK-release](https://github.com/tencentyun/qcloud-sdk-android/releases) 下载所有的 jar 包，建议您使用最新的 release 包。

## 开始使用

下面为您介绍如何使用 COS Android SDK 完成一个基础操作，如初始化客户端、创建存储桶、查询存储桶列表、上传对象、查询对象列表、下载对象和删除对象。

### 初始化服务

#### 方式一：通过临时密钥进行授权（推荐）

在终端直接通过永久密钥来进行身份认证会存在泄漏密钥的风险，COS 终端 SDK（Android/IOS）均支持通过临时密钥来授权请求，您只需要搭建一个返回临时密钥的服务，即可给终端 COS 请求进行授权，我们强烈建议您使用这种方式，具体请参见 [移动应用直传实践](https://cloud.tencent.com/document/product/436/9068)。

如果您已经搭建临时密钥服务，并直接将 STS SDK 中得到的 JSON 数据作为临时密钥服务的响应体，那么您可以使用如下代码来创建 COS SDK 中的授权类。

[//]: # (.cssg-snippet-global-init)
```java
String region = "COS_REGION";

CosXmlServiceConfig serviceConfig = new CosXmlServiceConfig.Builder()
        .setRegion(region)
        .isHttps(true) // 使用 HTTPS 请求，默认为 HTTP 请求
        .builder();

URL url = null;
try {
    // URL 是后台临时密钥服务的地址，如何搭建服务请参考（https://cloud.tencent.com/document/product/436/14048）
    url = new URL("https://your_auth_server_url");
} catch (MalformedURLException e) {
    e.printStackTrace();
    return;
}

/**
 * 初始化 {@link QCloudCredentialProvider} 对象，来给 SDK 提供临时密钥
 */
QCloudCredentialProvider credentialProvider = new SessionCredentialProvider(new HttpRequest.Builder<String>()
        .url(url)
        .method("GET")
        .build());

CosXmlService cosXmlService = new CosXmlService(context, serviceConfig, credentialProvider);
```

#### 方式二：自定义响应体授权

如果您想获得更大的灵活性，例如，自定义临时密钥服务的 HTTP 响应体，给终端返回服务器时间作为签名的开始时间，用来避免由于用户手机本地时间偏差过大导致的签名不正确，或者使用其他的协议来进行终端和服务端之间的通信，那么您可以继承 BasicLifecycleCredentialProvider 类，并实现其 fetchNewCredentials()：

首先定义一个 MyCredentialProvider 类：

[//]: # (.cssg-snippet-global-init-custom-provider)
```java
public static class MyCredentialProvider extends BasicLifecycleCredentialProvider {

    @Override
    protected QCloudLifecycleCredentials fetchNewCredentials() throws QCloudClientException {

        // 首先从您的临时密钥服务器获取包含了签名信息的响应

        // 然后解析响应，获取密钥信息
        String tmpSecretId = "COS_SECRETID"; //临时密钥 secretId
        String tmpSecretKey = "COS_SECRETKEY"; //临时密钥 secretKey
        String sessionToken = "TOKEN"; //临时密钥 Token
        long expiredTime = 1556183496L;//临时密钥有效截止时间戳，单位是秒

        /*强烈建议返回服务器时间作为签名的开始时间，用来避免由于用户手机本地时间偏差过大导致的签名不正确 */
        // 返回服务器时间作为签名的起始时间
        long startTime = 1556182000L; //临时密钥有效起始时间，单位是秒

        // todo something you want

        // 最后返回临时密钥信息对象
        return new SessionQCloudCredentials(tmpSecretId, tmpSecretKey, sessionToken, startTime, expiredTime);
    }
}
```

然后利用您定义的 MyCredentialProvider 实例来授权请求：

[//]: # (.cssg-snippet-global-init-custom)
```java
String region = "COS_REGION";

// 创建 CosXmlServiceConfig 对象，根据需要修改默认的配置参数
CosXmlServiceConfig serviceConfig = new CosXmlServiceConfig.Builder()
        .setRegion(region)
        .isHttps(true) // 使用 HTTPS 请求, 默认为 HTTP 请求
        .builder();

/**
 * 初始化 {@link QCloudCredentialProvider} 对象，来给 SDK 提供临时密钥
 */
QCloudCredentialProvider credentialProvider = new MyCredentialProvider();

CosXmlService cosXmlService = new CosXmlService(context, serviceConfig, credentialProvider);
```

#### 方式三：通过永久密钥进行授权（不推荐）

如果您没有搭建临时密钥服务，则可以使用永久密钥来初始化授权类。由于该方式会存在泄漏密钥的风险，我们强烈不推荐您使用这种方式，建议您仅在安全的环境下临时测试时使用。

[//]: # (.cssg-snippet-global-init-secret)
```java
String region = "COS_REGION";

// 创建 CosXmlServiceConfig 对象，根据需要修改默认的配置参数
CosXmlServiceConfig serviceConfig = new CosXmlServiceConfig.Builder()
        .setRegion(region)
        .isHttps(true) // 使用 HTTPS 请求, 默认为 HTTP 请求
        .builder();

String secretId = "COS_SECRETID"; //永久密钥 secretId
String secretKey = "COS_SECRETKEY"; //永久密钥 secretKey

/**
 * 初始化 {@link QCloudCredentialProvider} 对象，来给 SDK 提供临时密钥
 * @parma secretId 永久密钥 secretId
 * @param secretKey 永久密钥 secretKey
 * @param keyDuration 密钥有效期，单位为秒
 */
QCloudCredentialProvider credentialProvider = new ShortTimeCredentialProvider(secretId, secretKey, 300);

CosXmlService cosXmlService = new CosXmlService(context, serviceConfig, credentialProvider);
```

### 创建存储桶

[//]: # (.cssg-snippet-put-bucket)
```java
String bucket = "examplebucket-1250000000";
PutBucketRequest putBucketRequest = new PutBucketRequest(bucket);

// 定义存储桶的 ACL 属性。有效值：private，public-read-write，public-read；默认值：private
putBucketRequest.setXCOSACL("private");

// 赋予被授权者读的权限
ACLAccount readACLS = new ACLAccount();
readACLS.addAccount("100000000001", "100000000001");
putBucketRequest.setXCOSGrantRead(readACLS);

// 赋予被授权者写的权限
ACLAccount writeACLS = new ACLAccount();
writeACLS.addAccount("100000000001", "100000000001");
putBucketRequest.setXCOSGrantWrite(writeACLS);

// 赋予被授权者读写的权限
ACLAccount writeandReadACLS = new ACLAccount();
writeandReadACLS.addAccount("100000000001", "100000000001");
putBucketRequest.setXCOSReadWrite(writeandReadACLS);
// 设置签名校验 Host，默认校验所有 Header
Set<String> headerKeys = new HashSet<>();
headerKeys.add("Host");
putBucketRequest.setSignParamsAndHeaders(null, headerKeys);
// 使用同步方法
try {
    PutBucketResult putBucketResult = cosXmlService.putBucket(putBucketRequest);
} catch (CosXmlClientException e) {
    e.printStackTrace();
} catch (CosXmlServiceException e) {
    e.printStackTrace();
}

// 使用异步回调请求
cosXmlService.putBucketAsync(putBucketRequest, new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest request, CosXmlResult result) {
        PutBucketResult putBucketResult = (PutBucketResult) result;
    }

    @Override
    public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException serviceException) {
        // todo Put Bucket failed because of CosXmlClientException or CosXmlServiceException...
    }
});
```

### 查询存储桶列表
[//]: # (.cssg-snippet-get-service)
```java
GetServiceRequest getServiceRequest = new GetServiceRequest();
// 设置签名校验 Host，默认校验所有 Header
Set<String> headerKeys = new HashSet<>();
headerKeys.add("Host");
getServiceRequest.setSignParamsAndHeaders(null, headerKeys);
// 使用同步方法
try {
    GetServiceResult result = cosXmlService.getService(getServiceRequest);
} catch (CosXmlClientException e) {
    e.printStackTrace();
} catch (CosXmlServiceException e) {
    e.printStackTrace();
}

// 使用异步回调请求
cosXmlService.getServiceAsync(getServiceRequest, new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest request, CosXmlResult result) {
        GetServiceResult getServiceResult = (GetServiceResult) result;
    }

    @Override
    public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException serviceException) {
        // todo Put Bucket Lifecycle failed because of CosXmlClientException or CosXmlServiceException...
    }
});
```

### 上传对象

**TransferManager**、**COSXMLUploadTask** 封装了简单上传、分块上传接口的异步请求，并支持暂停、恢复以及取消上传请求，同时支持续传功能。我们推荐使用这种方式来上传对象，示例代码如下。

[//]: # (.cssg-snippet-transfer-upload-object)
```java
// 初始化 TransferConfig
TransferConfig transferConfig = new TransferConfig.Builder().build();

/*若有特殊要求，则可以如下进行初始化定制。例如限定当对象 >= 2M 时，启用分块上传，且分块上传的分块大小为1M，当源对象大于5M时启用分块复制，且分块复制的大小为5M。*/
transferConfig = new TransferConfig.Builder()
        .setDividsionForCopy(5 * 1024 * 1024) // 是否启用分块复制的最小对象大小
        .setSliceSizeForCopy(5 * 1024 * 1024) // 分块复制时的分块大小
        .setDivisionForUpload(2 * 1024 * 1024) // 是否启用分块上传的最小对象大小
        .setSliceSizeForUpload(1024 * 1024) // 分块上传时的分块大小
        .build();

// 初始化 TransferManager
TransferManager transferManager = new TransferManager(cosXmlService, transferConfig);

String bucket = "examplebucket-1250000000"; //存储桶，格式：BucketName-APPID
String cosPath = "exampleobject"; //对象在存储桶中的位置标识符，即称对象键
String srcPath = new File(context.getExternalCacheDir(), "exampleobject").toString(); //本地文件的绝对路径
String uploadId = null; //若存在初始化分块上传的 UploadId，则赋值对应的 uploadId 值用于续传；否则，赋值 null
// 上传对象
COSXMLUploadTask cosxmlUploadTask = transferManager.upload(bucket, cosPath, srcPath, uploadId);

/**
 * 若是上传字节数组，则可调用 TransferManager 的 upload(string, string, byte[]) 方法实现;
 * byte[] bytes = "this is a test".getBytes(Charset.forName("UTF-8"));
 * cosxmlUploadTask = transferManager.upload(bucket, cosPath, bytes);
 */

/**
 * 若是上传字节流，则可调用 TransferManager 的 upload(String, String, InputStream) 方法实现；
 * InputStream inputStream = new ByteArrayInputStream("this is a test".getBytes(Charset.forName("UTF-8")));
 * cosxmlUploadTask = transferManager.upload(bucket, cosPath, inputStream);
 */

//设置上传进度回调
cosxmlUploadTask.setCosXmlProgressListener(new CosXmlProgressListener() {
    @Override
    public void onProgress(long complete, long target) {
        // todo Do something to update progress...
    }
});
//设置返回结果回调
cosxmlUploadTask.setCosXmlResultListener(new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest request, CosXmlResult result) {
        COSXMLUploadTask.COSXMLUploadTaskResult cOSXMLUploadTaskResult = (COSXMLUploadTask.COSXMLUploadTaskResult) result;
    }

    @Override
    public void onFail(CosXmlRequest request, CosXmlClientException exception, CosXmlServiceException serviceException) {
        // todo Upload failed because of CosXmlClientException or CosXmlServiceException...
    }
});
//设置任务状态回调, 可以查看任务过程
cosxmlUploadTask.setTransferStateListener(new TransferStateListener() {
    @Override
    public void onStateChanged(TransferState state) {
        // todo notify transfer state
    }
});

/**
 若有特殊要求，则可以如下操作：
 PutObjectRequest putObjectRequest = new PutObjectRequest(bucket, cosPath, srcPath);
 putObjectRequest.setRegion(region); //设置存储桶所在的地域
 putObjectRequest.setNeedMD5(true); //是否启用 Md5 校验
 COSXMLUploadTask cosxmlUploadTask = transferManager.upload(putObjectRequest, uploadId);
 */

//取消上传
cosxmlUploadTask.cancel();


//暂停上传
cosxmlUploadTask.pause();

//恢复上传
cosxmlUploadTask.resume();
```

### 查询对象列表

[//]: # (.cssg-snippet-get-bucket)
```java
String bucketName = "examplebucket-1250000000"; //格式：BucketName-APPID;
GetBucketRequest getBucketRequest = new GetBucketRequest(bucketName);

// 前缀匹配，用来规定返回的对象前缀地址
getBucketRequest.setPrefix("prefix");

// 如果是第一次调用，您无需设置 marker 参数，COS 会从头开始列出对象
// 如果需列出下一页对象，则需要将 marker 设置为上次列出对象时返回的 GetBucketResult.listBucket.nextMarker 值
// 如果返回的 GetBucketResult.listBucket.isTruncated 为 false，则说明您已经列出了所有满足条件的对象
// getBucketRequest.setMarker(marker);

// 单次返回最大的条目数量，默认1000
getBucketRequest.setMaxKeys(100);

// 定界符为一个符号，如果有 Prefix，
// 则将 Prefix 到 delimiter 之间的相同路径归为一类，定义为 Common Prefix，
// 然后列出所有 Common Prefix。如果没有 Prefix，则从路径起点开始
getBucketRequest.setDelimiter('/');

// 设置签名校验 Host, 默认校验所有 Header
Set<String> headerKeys = new HashSet<>();
headerKeys.add("Host");
getBucketRequest.setSignParamsAndHeaders(null, headerKeys);
// 使用同步方法
try {
    GetBucketResult getBucketResult = cosXmlService.getBucket(getBucketRequest);
} catch (CosXmlClientException e) {
    e.printStackTrace();
} catch (CosXmlServiceException e) {
    e.printStackTrace();
}

// 使用异步回调请求
cosXmlService.getBucketAsync(getBucketRequest, new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest request, CosXmlResult result) {
        GetBucketResult getBucketResult = (GetBucketResult) result;
    }

    @Override
    public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException serviceException) {
        // todo Get Bucket failed because of CosXmlClientException or CosXmlServiceException...
    }
});

// 如果您需列出所有的对象，可以参考如下代码：

bucketName = "examplebucket-1250000000";
getBucketRequest = new GetBucketRequest(bucketName);

// prefix 表示列出的 object 的 key 以 prefix 开始
getBucketRequest.setPrefix("images/");
// delimiter 表示分隔符，设置为 / 表示列出当前目录下的 object, 设置为空表示列出所有的 object
getBucketRequest.setDelimiter("/");
// 设置最大遍历出多少个对象，一次 listobject 最大支持1000
getBucketRequest.setMaxKeys(100);
GetBucketResult getBucketResult = null;
do {
    try {
        getBucketResult = cosXmlService.getBucket(getBucketRequest);
    } catch (CosXmlClientException e) {
        e.printStackTrace();
        return;
    } catch (CosXmlServiceException e) {
        e.printStackTrace();
        return;
    }
    // commonPrefixs 表示表示被 delimiter 截断的路径，例如 delimter 设置为 /，commonPrefixs 则表示子目录的路径
    List<ListBucket.CommonPrefixes> commonPrefixs = getBucketResult.listBucket.commonPrefixesList;

    // contents 表示列出的 object 列表
    List<ListBucket.Contents> contents = getBucketResult.listBucket.contentsList;

    String nextMarker = getBucketResult.listBucket.nextMarker;
    getBucketRequest.setMarker(nextMarker);
} while (getBucketResult.listBucket.isTruncated);
```

### 下载对象

**TransferManager**、**COSXMLDownloadTask** 封装了下载接口的异步请求，并支持暂停、恢复以及取消下载请求，同时支断点下载功能。我们推荐使用这种方式来下载对象，示例代码如下。

[//]: # (.cssg-snippet-transfer-download-object)
```java
Context applicationContext = context.getApplicationContext(); // application context
String bucket = "examplebucket-1250000000"; //存储桶，格式：BucketName-APPID
String cosPath = "exampleobject"; //对象在存储桶中的位置标识符，即称对象键
String savePathDir = context.getExternalCacheDir().toString(); //本地目录路径
String savedFileName = "exampleobject";//本地保存的文件名，若不填（null），则与 COS 上的文件名一样
//下载对象
TransferConfig transferConfig = new TransferConfig.Builder().build();
//初始化 TransferManager
TransferManager transferManager = new TransferManager(cosXmlService, transferConfig);
COSXMLDownloadTask cosxmlDownloadTask = transferManager.download(applicationContext, bucket, cosPath, savePathDir, savedFileName);
//设置下载进度回调
cosxmlDownloadTask.setCosXmlProgressListener(new CosXmlProgressListener() {
    @Override
    public void onProgress(long complete, long target) {
        // todo Do something to update progress...
    }
});
//设置返回结果回调
cosxmlDownloadTask.setCosXmlResultListener(new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest request, CosXmlResult result) {
        COSXMLDownloadTask.COSXMLDownloadTaskResult cOSXMLDownloadTaskResult = (COSXMLDownloadTask.COSXMLDownloadTaskResult) result;
    }

    @Override
    public void onFail(CosXmlRequest request, CosXmlClientException exception, CosXmlServiceException serviceException) {
        // todo Download failed because of CosXmlClientException or CosXmlServiceException...
    }
});
//设置任务状态回调，可以查看任务过程
cosxmlDownloadTask.setTransferStateListener(new TransferStateListener() {
    @Override
    public void onStateChanged(TransferState state) {
        // todo notify transfer state
    }
});

/**
 若有特殊要求，则可以如下操作：
 GetObjectRequest getObjectRequest = new GetObjectRequest(bucket, cosPath, localDir, localFileName);
 getObjectRequest.setRegion(region); //设置存储桶所在的地域
 COSXMLDownloadTask cosxmlDownloadTask = transferManager.download(context, getObjectRequest);
 */

//取消下载
cosxmlDownloadTask.cancel();

//暂停下载
cosxmlDownloadTask.pause();

//恢复下载
cosxmlDownloadTask.resume();
```

>?高级下载接口支持断点续传，所以会在下载前先发起 HEAD 请求获取文件信息。如果您使用的是临时密钥或者使用子账号访问，请确保权限列表中包含 HeadObject 的权限。

### 删除对象

[//]: # (.cssg-snippet-delete-object)
```java
String bucket = "examplebucket-1250000000"; //存储桶名称，格式：BucketName-APPID
String cosPath = "exampleobject"; //对象在存储桶中的位置标识符，即对象键

DeleteObjectRequest deleteObjectRequest = new DeleteObjectRequest(bucket, cosPath);
// 设置签名校验 Host，默认校验所有 Header
Set<String> headerKeys = new HashSet<>();
headerKeys.add("Host");
deleteObjectRequest.setSignParamsAndHeaders(null, headerKeys);
// 使用同步方法删除
try {
    DeleteObjectResult deleteObjectResult = cosXmlService.deleteObject(deleteObjectRequest);
} catch (CosXmlClientException e) {
    e.printStackTrace();
} catch (CosXmlServiceException e) {
    e.printStackTrace();
}

// 使用异步回调请求
cosXmlService.deleteObjectAsync(deleteObjectRequest, new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest cosXmlRequest, CosXmlResult result) {
        DeleteObjectResult deleteObjectResult = (DeleteObjectResult) result;
    }

    @Override
    public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException serviceException) {
        // todo Delete Object failed because of CosXmlClientException or CosXmlServiceException...
    }
});
```
