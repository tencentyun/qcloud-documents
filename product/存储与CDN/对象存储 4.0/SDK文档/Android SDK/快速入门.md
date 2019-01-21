## 快速接入

### 接入准备

1. SDK 支持 Android 2.2及以上版本的手机系统。
2. 手机必须要有网络（GPRS、3G 或 WIFI 网络等）。
3. 手机可以没有存储空间，但会使部分功能无法正常工作。
4. 从 [COS 控制台](https://console.cloud.tencent.com/cos4/secret) 获取 APPID、SecretId、SecretKey。

>?关于文章中出现的 SecretId、SecretKey、Bucket 等名称的含义和获取方式请参考：[COS 术语信息](https://cloud.tencent.com/document/product/436/7751)。

### 集成 SDK

#### 自动集成（**推荐**）

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
    compile 'com.tencent.qcloud:cosxml:5.4.19'
}
```

3、若您只使用上传、下载和复制功能，则可以使用简化版的 SDK 将上述步骤2的依赖改成如下依赖：

```
dependencies {
	...
    // 增加这行
    compile 'com.tencent.qcloud:cosxml-lite:5.4.19'
}
```

4、为了持续跟踪和优化 SDK 的质量，给您带来更好的使用体验，我们在 SDK 中引入了腾讯移动分析（mta），若是想关闭该功能，则在应用的根目录下的 build.gradle 中添加依赖：

```
dependencies {
	...
    // 增加这行
   compile ('com.tencent.qcloud:cosxml:5.4.19'){
        exclude group:'com.tencent.qcloud', module: 'mtaUtils' //关闭mta上报功能
    }
}
```

简化版 SDK 代码如下：
```
dependencies {
	...
    // 增加这行
    compile ('com.tencent.qcloud:cosxml-lite:5.4.19'){
        exclude group:'com.tencent.qcloud', module: 'mtaUtils' //关闭mta上报功能
    }
}
```
#### 手动集成

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

### 配置权限

使用该 SDK 需要网络、存储等相关的一些访问权限，可在 AndroidManifest.xml 中增加如下权限声明（Android 5.0 以上还需要动态获取权限）：
```html
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
```

### 更多资源

**源码和示例工程**

COS Android SDK 相关源码请参见 [COS Android SDK Github 地址](https://github.com/tencentyun/qcloud-sdk-android)。
示例 demo 请参见 [COS Android SDK 示例工程](https://github.com/tencentyun/qcloud-sdk-android-samples)。

**更新日志**

COS Android SDK 更新日志请参见 [COS Android SDK 更新日志](https://github.com/tencentyun/qcloud-sdk-android/blob/master/CHANGELOG.md)。

## 快速入门

### 初始化 

在执行任何和 COS 服务相关请求之前，都需要先实例化 CosXmlService 对象，具体可分为如下几步。

#### 初始化配置类

**CosXmlServiceConfig** 是 COS 服务的配置类，您可以使用如下代码来初始化：

```
String appid = "对象存储的服务 APPID";
String region = "存储桶所在的地域"; 

//创建 CosXmlServiceConfig 对象，根据需要修改默认的配置参数
CosXmlServiceConfig serviceConfig = new CosXmlServiceConfig.Builder()
       .setAppidAndRegion(appid, region)
       .setDebuggable(true)
       .builder();
```

#### 初始化授权类

在终端直接通过永久密钥来进行身份认证会存在泄漏密钥的风险，COS 终端 SDK（Android/IOS）均支持通过临时密钥来授权请求，您只需要搭建一个返回临时密钥的服务，即可给终端 COS 请求进行授权，我们强烈建议您使用这种方式，具体请参考 [移动应用直传实践](https://cloud.tencent.com/document/product/436/9068)。

#### 通过临时密钥进行授权（推荐）

- 标准响应体授权

如果您已经搭建临时密钥服务，并直接将 STS SDK 中得到的 JSON 数据作为临时密钥服务的响应体（cossign 即采用了这种方式），那么您可以使用如下代码来创建 COS SDK 中的授权类。
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
>!标准响应体授权方式下签名的开始时间为手机本地时间，因此如果手机本地时间偏差较大（十分钟以上），可能会导致签名出错，这种情况可以使用下述的自定义响应体授权。

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
        String tmpSecretId = ...;
        String tmpSecretKey = ...;
        String sessionToken = ...;
        long expiredTime = ...;
        
        // 返回服务器时间作为签名的起始时间
        long beginTime = ...;
         
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

#### 通过永久密钥进行授权

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


#### 初始化 COS 服务类

**CosXmlService** 是 COS 服务类，可用来操作各种 COS 服务，当您实例化配置类和授权类后，您可以很方便的实例化一个 COS 服务类，具体代码如下。

````java
CosXmlService cosXmlService = new CosXmlService(context, serviceConfig, qCloudCredentialProvider);
````

### 上传文件

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
        .setSliceSizeForCopy(1024 * 1024) //分片上传时的分片大小
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
                Log.d("TEST",  "Success: " + result.printResult());
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
 putObjectRequest.setRegion(region); //设置存储桶所在的园区
 putObjectRequest.setNeedMD5(true); //是否启用Md5校验
 COSXMLUploadTask cosxmlUploadTask = transferManager.upload(putObjectRequest, uploadId);
*/

//取消上传
cosxmlUploadTask.cancel();


//暂停上传
cosxmlUploadTask.pause();

//恢复上传
cosxmlUploadTask.resume();

```
### 下载文件
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
                Log.d("TEST",  "Success: " + result.printResult());
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
### 复制文件
**TransferManager**、**COSXMLCopyTask** 封装了简单复制、分片复制接口的异步请求，并支持暂停、恢复以及取消复制请求。我们推荐使用这种方式来复制文件，示例代码如下。
```java
String bucket = "存储桶名称"; //目标文件的存储桶
String cosPath = "对象键"; //即目标文件存储到 COS 上的绝对路径, 格式如 cosPath = "test.txt";
CopyObjectRequest.CopySourceStruct copySourceStruct = new CopyObjectRequest.CopySourceStruct(
                "源文件存储桶所在的appid", "源文件存储桶", "源文件存储桶所在的园区", "源文件的对象键");// 源文件所在 cos 的位置描述
//复制文件
COSXMLCopyTask cosxmlCopyTask = transferManager.copy(bucket, cosPath, copySourceStruct);
//设置返回结果回调
cosxmlCopyTask.setCosXmlResultListener(new CosXmlResultListener() {
            @Override
            public void onSuccess(CosXmlRequest request, CosXmlResult result) {
                Log.d("TEST",  "Success: " + result.printResult());
            }

            @Override
            public void onFail(CosXmlRequest request, CosXmlClientException exception, CosXmlServiceException serviceException) {
                Log.d("TEST",  "Failed: " + (exception == null ? serviceException.getMessage() : exception.toString()));
            }
        });
//设置任务状态回调, 可以查看任务过程
cosxmlCopyTask.setTransferStateListener(new TransferStateListener() {
            @Override
            public void onStateChanged(TransferState state) {
                Log.d("TEST", "Task state:" + state.name());
            }
        });
/**
若有特殊要求，则可以如下操作：
CopyObjectRequest copyObjectRequest = new CopyObjectRequest(bucket, cosPath, copySourceStruct);
copyObjectRequest.setRegion(region); //设置存储桶所在的园区
COSXMLCopyTask cosxmlCopyTask = transferManager.copy(copyObjectRequest);
*/

//取消复制
cosxmlCopyTask.cancel();


//暂停复制
cosxmlCopyTask.pause();

//恢复复制
cosxmlCopyTask.resume();
```
