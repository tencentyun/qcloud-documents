## 下载与安装

### 相关资源
**源码和示例工程**

- COS Android SDK 相关源码请参见 [COS Android SDK Github 地址](https://github.com/tencentyun/qcloud-sdk-android)。
- 示例 demo 请参见 [COS Android SDK 示例工程](https://github.com/tencentyun/qcloud-sdk-android-samples)。

**更新日志**

COS Android SDK 更新日志请参阅 [COS Android SDK 更新日志](https://github.com/tencentyun/qcloud-sdk-android/blob/master/CHANGELOG.md)。

### 环境依赖

1. SDK 支持 Android 2.2及以上版本的手机系统。
2. 手机必须要有网络（GPRS、3G 或 WIFI 网络等）。
3. 手机存储空间不足会使部分功能无法正常工作，请预留一定的手机存储空间。
4. 从访问管理控制台中的 [API 密钥管理](https://console.cloud.tencent.com/capi) 页面获取 SecretId、SecretKey，以及在 [账号设置](https://console.cloud.tencent.com/developer) 中获取 APPID 信息。

>?关于文章中出现的 SecretId、SecretKey、Bucket 等名称的含义和获取方式请参阅 [COS 术语信息](https://cloud.tencent.com/document/product/436/7751)。

### 安装 SDK

#### 配置权限

使用该 SDK 需要网络、存储等相关的一些访问权限，可在 AndroidManifest.xml 中添加如下权限声明（Android 5.0 以上还需要动态获取权限）：
```html
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
```

#### 集成 SDK
您可以通过两个方式集成 SDK：自动集成和手动集成。

**自动集成（推荐）**

1、在您的项目根目录下的 build.gradle 文件中添加 maven 仓库：

```
allprojects {

    repositories {
        ...
        // 添加如下 maven 仓库地址
        maven {
            url "https://dl.bintray.com/tencentqcloudterminal/maven"
        }
    }
}
```

2、在应用的根目录下的 build.gradle 中添加依赖：
```
dependencies {
	...
    // 增加这行
    compile 'com.tencent.qcloud:cosxml:5.4.23'
}
```

3、若您只使用上传、下载和复制功能，则可以使用简化版的 SDK 将上述步骤2的依赖改成如下依赖：

```
dependencies {
	...
    // 增加这行
    compile 'com.tencent.qcloud:cosxml-lite:5.4.23'
}
```

4、为了持续跟踪和优化 SDK 的质量，给您带来更好的使用体验，我们在 SDK 中引入了腾讯移动分析（mta），若是想关闭该功能，则在应用的根目录下的 build.gradle 中添加依赖：

```
dependencies {
	...
    // 增加这行
   compile ('com.tencent.qcloud:cosxml:5.4.23'){
        exclude group:'com.tencent.qcloud', module: 'mtaUtils' //关闭 mta 上报功能
    }
}
```

简化版 SDK 代码如下：
```
dependencies {
	...
    // 增加这行
    compile ('com.tencent.qcloud:cosxml-lite:5.4.23'){
        exclude group:'com.tencent.qcloud', module: 'mtaUtils' //关闭 mta上报功能
    }
}
```

**手动集成**

需要在工程项目中导入下列 jar 包，存放在 libs 文件夹下：

- cos-android-sdk.jar
- qcloud-foundation.jar
- bolts-tasks.jar
- okhttp.jar (3.9及以上版本)
- okio.jar(1.13.0及以上版本)
- mtaUtils.jar
- mid-sdk.jar
- mta-android-sdk.jar
- logUtils.aar

您可以在这里 [COS XML Android SDK-release](https://github.com/tencentyun/qcloud-sdk-android/releases) 下载所有的 jar 包，建议您使用最新的 release 包。

## 开始使用
下面为您介绍如何使用 COS Android SDK 完成一个基础操作，如初始化客户端、创建存储桶、查询存储桶列表、上传对象、查询对象列表、下载对象和删除对象。

### 初始化 

在执行任何和 COS 服务相关请求之前，都需要先实例化 CosXmlService 对象，具体可分为如下几步：
1. 初始化配置类 CosXmlServiceConfig；
2. 初始化授权类 QCloudCredentialProvider；
3. 初始化 COS 服务类 CosXmlService.

#### 初始化配置类

**CosXmlServiceConfig** 是 COS 服务的配置类，您可以使用如下代码来初始化：

```
String region = "存储桶所在的地域"; 

//创建 CosXmlServiceConfig 对象，根据需要修改默认的配置参数
CosXmlServiceConfig serviceConfig = new CosXmlServiceConfig.Builder()
       .setRegion(region)
       .setDebuggable(true)
       .builder();
```

#### 初始化授权类

在终端直接通过永久密钥来进行身份认证会存在泄漏密钥的风险，COS 终端 SDK（Android/IOS）均支持通过临时密钥来授权请求，您只需要搭建一个返回临时密钥的服务，即可给终端 COS 请求进行授权，我们强烈建议您使用这种方式，具体请参阅 [移动应用直传实践](https://cloud.tencent.com/document/product/436/9068)。

##### 通过临时密钥进行授权（推荐）

- 标准响应体授权

如果您已经搭建临时密钥服务，并直接将 STS SDK 中得到的 JSON 数据作为临时密钥服务的响应体，那么您可以使用如下代码来创建 COS SDK 中的授权类。
```
/**
 * 获取授权服务的 url 地址
 */
URL url = null; // 后台授权服务的 url 地址
try {
    url = new URL("your_auth_server_url");
} catch (MalformedURLException e) {
    e.printStackTrace();
}

/**
 * 初始化 {@link QCloudCredentialProvider} 对象，来给 SDK 提供临时密钥。
 */
QCloudCredentialProvider credentialProvider = new SessionCredentialProvider(new HttpRequest.Builder<String>()
                .url(url)
                .method("GET")
                .build());
```
>!标准响应体授权方式下，签名的开始时间为手机本地时间，因此如果手机本地时间偏差较大（十分钟以上），可能会导致签名出错，这种情况可以使用下述的自定义响应体授权。

- 自定义响应体授权

如果您想获得更大的灵活性，比如自定义临时密钥服务的 HTTP 响应体，给终端返回服务器时间作为签名的开始时间，用来避免由于用户手机本地时间偏差过大导致的签名不正确，或者使用其他的协议来进行终端和服务端之间的通信，那么您可以继承 `BasicLifecycleCredentialProvider` 类，并实现其 `fetchNewCredentials()`：

首先定义一个 `MyCredentialProvider` 类：

```java
public class MyCredentialProvider extends BasicLifecycleCredentialProvider {

    @Override
    protected QCloudLifecycleCredentials fetchNewCredentials() throws QCloudClientException {
       
        // 首先从您的临时密钥服务器获取包含了签名信息的响应
        ....
        
        // 然后解析响应，获取密钥信息
        String tmpSecretId = "COS_SECRETID"; //临时密钥 secretId
        String tmpSecretKey = "COS_SECRETKEY"; //临时密钥 secretKey
        String sessionToken = "TOKEN"; //临时密钥 Token
        long expiredTime = 1556183496L;//临时密钥有效截止时间
        
        // 返回服务器时间作为签名的起始时间
        long beginTime = 1556182000L; //临时密钥有效起始时间
         
        // todo something you want
         
        // 最后返回临时密钥信息对象 
        return new SessionQCloudCredentials(tmpSecretId, tmpSecretKey, sessionToken, beginTime, expiredTime);
    }
}
```

然后利用您定义的 `MyCredentialProvider` 实例来授权请求：

```
/**
 * 初始化 {@link QCloudCredentialProvider} 对象，来给 SDK 提供临时密钥。
 */
QCloudCredentialProvider credentialProvider = new MyCredentialProvider();
```

##### 通过永久密钥进行授权

如果您没有搭建临时密钥服务，则可以使用永久密钥来初始化授权类。由于该方式会存在泄漏密钥的风险，我们**强烈不推荐您使用这种方式**，建议您仅在安全的环境下临时测试时使用，代码如下。

```
String secretId = "云 API 密钥 SecretId";
String secretKey ="云 API 密钥 SecretKey";

/**
 * 初始化 {@link QCloudCredentialProvider} 对象，来给 SDK 提供临时密钥。
 */
QCloudCredentialProvider credentialProvider = new ShortTimeCredentialProvider(secretId,
                secretKey, 300);
```


#### 初始化 CosXmlService 服务类

**CosXmlService** 是 COS 服务类，可用来操作各种 COS 服务，当您实例化配置类和授权类后，您可以很方便的实例化一个 COS 服务类，具体代码如下。

```java
CosXmlService cosXmlService = new CosXmlService(context, serviceConfig, credentialProvider);
```

### 创建存储桶
```java
String bucket = "examplebucket-1250000000"; //格式：BucketName-APPID
PutBucketRequest putBucketRequest = new PutBucketRequest(bucket);
//发送请求
cosXmlService.putBucketAsync(putBucketRequest, new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest request, CosXmlResult result) {
        // todo Put Bucket success
		PutBucketResult putBucketResult = (putBucketResult)result;
    }
    
    @Override
    public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException serviceException)  {
        // todo Put Bucket failed because of CosXmlClientException or CosXmlServiceException...
    }
});
```

### 查询存储桶列表
```java
GetServiceRequest getServiceRequest = new GetServiceRequest();
//发送请求
cosXmlService.getServiceAsync(getServiceRequest, new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest request, CosXmlResult result) {
        // todo Put Bucket Lifecycle success
		GetServiceResult getServiceResult = (GetServiceResult)result;
    }
    
    @Override
    public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException serviceException)  {
        // todo Put Bucket Lifecycle failed because of CosXmlClientException or CosXmlServiceException...
    }
});
```

### 上传对象

**TransferManager**、**COSXMLUploadTask** 封装了简单上传、分片上传接口的异步请求，并支持暂停、恢复以及取消上传请求，同时支持续传功能。我们推荐使用这种方式来上传文件，示例代码如下。

```java

// 初始化 TransferConfig
TransferConfig transferConfig = new TransferConfig.Builder().build();
/**
若有特殊要求，则可以如下进行初始化定制。如限定当文件 >= 2M 时，启用分片上传，且分片上传的分片大小为 1M, 当源文件大于 5M 时启用分片复制，且分片复制的大小为 5M。
TransferConfig transferConfig = new TransferConfig.Builder()
        .setDividsionForCopy(5 * 1024 * 1024) // 是否启用分片复制的文件最小大小
        .setSliceSizeForCopy(5 * 1024 * 1024) //分片复制时的分片大小
        .setDivisionForUpload(2 * 1024 * 1024) // 是否启用分片上传的文件最小大小
        .setSliceSizeForUpload(1024 * 1024) //分片上传时的分片大小
        .build();
*/

//初始化 TransferManager
TransferManager transferManager = new TransferManager(cosXml, transferConfig);

String bucket = "存储桶名称";
String cosPath = "对象键"; //即存储到 COS 上的绝对路径, 格式如 cosPath = "test.txt";
String srcPath = "本地文件的绝对路径"; // 如 srcPath=Environment.getExternalStorageDirectory().getPath() + "/test.txt";
String uploadId = null; //若存在初始化分片上传的 UploadId，则赋值对应uploadId值用于续传，否则，赋值null。
//上传文件
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
                float progress = 1.0f * complete / target * 100;
                Log.d("TEST",  String.format("progress = %d%%", (int)progress));
            }
        });
//设置返回结果回调
cosxmlUploadTask.setCosXmlResultListener(new CosXmlResultListener() {
            @Override
            public void onSuccess(CosXmlRequest request, CosXmlResult result) {
				COSXMLUploadTaskResult cOSXMLUploadTaskResult = (COSXMLUploadTaskResult)result;
                Log.d("TEST",  "Success: " + cOSXMLUploadTaskResult.printResult());
            }

            @Override
            public void onFail(CosXmlRequest request, CosXmlClientException exception, CosXmlServiceException serviceException) {
                Log.d("TEST",  "Failed: " + (exception == null ? serviceException.getMessage() : exception.toString()));
            }
        });
//设置任务状态回调, 可以查看任务过程
cosxmlUploadTask.setTransferStateListener(new TransferStateListener() {
            @Override
            public void onStateChanged(TransferState state) {
                Log.d("TEST", "Task state:" + state.name());
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
```java
String bucket = "examplebucket-1250000000"; //格式：BucketName-APPID;  
GetBucketRequest getBucketRequest = new GetBucketRequest(bucket);

//前缀匹配，用来规定返回的文件前缀地址
getBucketRequest.setPrefix("prefix");

//单次返回最大的条目数量，默认 1000
getBucketRequest.setMaxKeys(100);

//定界符为一个符号，如果有 Prefix，
//则将 Prefix 到 delimiter 之间的相同路径归为一类，定义为 Common Prefix，
//然后列出所有 Common Prefix。如果没有 Prefix，则从路径起点开始
getBucketRequest.setDelimiter('/');

//发送请求
cosXmlService.getBucketAsync(getBucketRequest, new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest request, CosXmlResult result) {
        // todo Get Bucket success
		GetBucketResult getBucketResult = (GetBucketResult)result;
    }
    
    @Override
    public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException serviceException)  {
        // todo Get Bucket failed because of CosXmlClientException or CosXmlServiceException...
    }
});
```

### 下载对象
**TransferManager**、**COSXMLDownloadTask** 封装了下载接口的异步请求，并支持暂停、恢复以及取消下载请求，同时支断点下载功能。我们推荐使用这种方式来下载文件，示例代码如下。
```java
Context applicationContext = "application 上下文"； // getApplicationContext()
String bucket = "存储桶名称"; //文件所在的存储桶
String cosPath = "对象键"; //即文件存储到 COS 上的绝对路径,格式如 cosPath = "test.txt";
String savedDirPath = "文件下载到本地的文件夹路径"；
String savedFileName = "文件下载本地的文件名"；//若不填（null）,则与 cos 上的文件名一样
//下载文件
COSXMLDownloadTask cosxmlDownloadTask = transferManager.download(applicationContext, bucket, cosPath, savedDirPath, savedFileName);
//设置下载进度回调
cosxmlDownloadTask.setCosXmlProgressListener(new CosXmlProgressListener() {
            @Override
            public void onProgress(long complete, long target) {
                float progress = 1.0f * complete / target * 100;
                Log.d("TEST",  String.format("progress = %d%%", (int)progress));
            }
        });
//设置返回结果回调
cosxmlDownloadTask.setCosXmlResultListener(new CosXmlResultListener() {
            @Override
            public void onSuccess(CosXmlRequest request, CosXmlResult result) {
				COSXMLDownloadTaskResult cOSXMLDownloadTaskResult = (COSXMLDownloadTaskResult)result;
                Log.d("TEST",  "Success: " + cOSXMLDownloadTaskResult.printResult());
            }

            @Override
            public void onFail(CosXmlRequest request, CosXmlClientException exception, CosXmlServiceException serviceException) {
                Log.d("TEST",  "Failed: " + (exception == null ? serviceException.getMessage() : exception.toString()));
            }
        });
//设置任务状态回调, 可以查看任务过程
cosxmlDownloadTask.setTransferStateListener(new TransferStateListener() {
            @Override
            public void onStateChanged(TransferState state) {
                Log.d("TEST", "Task state:" + state.name());
            }
        });

/**
若有特殊要求，则可以如下操作：
GetObjectRequest getObjectRequest = new GetObjectRequest(bucket, cosPath, localDir, localFileName);
getObjectRequest.setRegion(region); //设置存储桶所在的园区
COSXMLDownloadTask cosxmlDownloadTask = transferManager.download(context, getObjectRequest);
*/

//取消下载
cosxmlDownloadTask.cancel();

//暂停下载
cosxmlDownloadTask.pause();

//恢复下载
cosxmlDownloadTask.resume();

```

### 删除对象
```java
String bucket = "examplebucket-1250000000"; //存储桶，格式：BucketName-APPID
String cosPath = "exampleobject"; //对象在存储桶中的位置，即称对象键.

DeleteObjectRequest deleteObjectRequest = new DeleteObjectRequest(bucket, cosPath);
//发送请求 
cosXmlService.deleteObjectAsync(deleteObjectRequest, new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest cosXmlRequest, CosXmlResult cosXmlResult) {
        // todo Delete Object success...
		DeleteObjectResult deleteObjectResult  = (DeleteObjectResult)result;
    }
    
    @Override
    public void onFail(CosXmlRequest cosXmlRequest, CosXmlClientException clientException, CosXmlServiceException serviceException)  {
        // todo Delete Object failed because of CosXmlClientException or CosXmlServiceException...
    }
});
```