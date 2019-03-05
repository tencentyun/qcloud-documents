## 开发准备

### SDK 获取
人脸核身 SDK 的 Android SDK-1.0.0下载地址：[Android SDK](https://mc.qcloudimg.com/static/archive/9f5229f0bb019f5fe5b9f6b7bc6134af/faceid-1.0.0.zip)。
更多示例可以参考Demo：[Android SDK Demo](https://mc.qcloudimg.com/static/archive/6e5c11cd423409f50804410e47b04e9a/FaceIdDemo+.zip)。

### 开发准备
- 开发者使用人脸识别功能前，需要先进行 [腾讯云账号注册](https://cloud.tencent.com/register)（详细指引请参考 [注册腾讯云](https://cloud.tencent.com/document/product/378/9603)），并 [创建存储桶](https://cloud.tencent.com/document/product/460/10637)，从而获得 APPID 、SecretId 和 SecretKey 等（获取 APPID 可参考 [域名管理](https://cloud.tencent.com/document/product/460/6937)）；
- 手机必须要有网络（GPRS、3G 或 Wifi 等）；
- 支持Android 4.0及其以上版本；

### SDK 配置
1.导入下列 jar 包
- faceid-1.0.0.jar
- okhttp-3.2.0.jar
- okio-1.6.0.jar
- slf4j-android-1.6.1-RC1.jar

2.在AndroidManifest.xml中增加如下权限
```
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
<uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS"/>
```
<span id="1"></span>
## 快速入门
### 初始化 FaceIdClient
```
Context context = getApplicationContext();
String appid = "your appid";

final FaceIdClient faceIdClient = new FaceIdClient(context, appid);
```
### 人脸对比
**通过上传本地图像进行对比**
```
String bucket = "your bucket"; // bucket名称
String idCardNumber = "your id card number"; // 身份证号码
String idCardName = "your idCard name"; // 身份证姓名
File image = new File("your image path"); // 本地图片文件
String seq = "seq";

String sign = "多次有效签名"; // 测试时可以利用CredentialProvider类来生成签名

// 初始化人脸对比请求
final ImageIdCardCompareRequest imageIdCardCompareRequest = new ImageIdCardCompareRequest(bucket, idCardNumber, idCardName, image, seq);

// 设置签名
imageIdCardCompareRequest.setSign(sign);

// 发送请求（注意：所有发送请求的方法均是同步的，因此请不要直接在主线程中调用）
new Thread(new Runnable() {
    @Override
    public void run() {
        try {
            ImageIdCardCompareResult imageIdCardCompareResult = faceIdClient.imageIdCardCompare(imageIdCardCompareRequest);
        } catch (ClientException e) {
            e.printStackTrace();
        } catch (ServerException e) {
            e.printStackTrace();
        }
    }
}).start();
```
**通过上传图像 url 进行对比**

```
String bucket = "your bucket"; // bucket名称
String idCardNumber = "your id card number"; // 身份证号码
String idCardName = "your idCard name"; // 本地图片文件
String url = "your image url"; // 图片的url路径
String seq = "seq";

String sign = "多次有效签名"; // 测试时可以利用CredentialProvider类来生成签名

// 初始化请求
final ImageIdCardCompareRequest imageIdCardCompareRequest = new ImageIdCardCompareRequest(bucket, idCardNumber, idCardName, url, seq);
// 设置签名
imageIdCardCompareRequest.setSign(sign);

// 发送请求（注意：所有发送请求的方法均是同步的，因此请不要直接在主线程中调用）
new Thread(new Runnable() {
    @Override
    public void run() {
        try {
            ImageIdCardCompareResult imageIdCardCompareResult = faceIdClient.imageIdCardCompare(imageIdCardCompareRequest);
        } catch (ClientException e) {
            e.printStackTrace();
        } catch (ServerException e) {
            e.printStackTrace();
        }
    }
}).start();
```
<span id="2"></span>
### 获取唇语
```
String bucket = "your bucket"; // bucket名称
String seq = "seq";

String sign = "多次有效签名";

// 初始化请求
final GetLipLanguageRequest getLipLanguageRequest = new GetLipLanguageRequest(bucket, seq);
// 设置签名
getLipLanguageRequest.setSign(sign);

// 发送请求（注意：所有发送请求的方法均是同步的，因此请不要直接在主线程中调用）
new Thread(new Runnable() {
    @Override
    public void run() {
        try {
            GetLipLanguageResult getLipLanguageResult = faceIdClient.getLipLanguage(getLipLanguageRequest);
        } catch (ClientException e) {
            e.printStackTrace();
        } catch (ServerException e) {
            e.printStackTrace();
        }
    }
}).start();
```
<span id="3"></span>
### 人脸核身
**根据用户上传的照片和视频，进行人脸核身验证**
```
String bucket = "your bucket"; // bucket名称
String validateData = "your validate data"; // 唇语
String videoPath = "your local video path"; // 本地视频路径
String imagePath = "your local image path"; // 本地图片路径
boolean compare = true; // 上传的图片和视频是否进行对比
String seq = "seq";

String sign = "sign"; // 测试时可以利用CredentialProvider类来生成签名

// 初始化请求
final VideoImageIdentityRequest videoImageIdentityRequest = new 
VideoImageIdentityRequest(bucket, validateData, videoPath, imagePath, compare, seq);
// 设置签名
videoImageIdentityRequest.setSign(sign);

// 发送请求（注意：所有发送请求的方法均是同步的，因此请不要直接在主线程中调用）
new Thread(new Runnable() {
	@Override
    public void run() {
        try {
        	VideoImageIdentityResult videoImageIdentityResult = faceIdClient.videoImageIdentity(videoImageIdentityRequest);
        } catch (ClientException e) {
        	e.printStackTrace();            
        } catch (ServerException e) {
            e.printStackTrace();
        }
    }
}).start();
```
**根据用户的身份证号、姓名，与用户上传的图像进行人脸相似度对比**
```
String bucket = "your bucket"; // bucket名称
String validateData = "your validate data"; // 唇语
String videoPath = "your local video path"; // 本地视频路径
String idcardNumber = "your id card number"; // 身份证号码
String idcardName = "your id card name";  // 身份证姓名
String seq = "seq";

String sign = "sign"; // 测试时可以利用CredentialProvider类来生成签名

// 初始化请求
final VideoIdCardIdentityRequest videoIdCardIdentityRequest = new VideoIdCardIdentityRequest(bucket, validateData, videoPath, idcardNumber, idcardName, seq);
// 设置签名
videoIdCardIdentityRequest.setSign(sign);

// 发送请求（注意：所有发送请求的方法均是同步的，因此请不要直接在主线程中调用）
new Thread(new Runnable() {
	@Override
    public void run() {
        try {
        	VideoIdCardIdentityResult videoIdCardIdentityResult = faceIdClient.videoIdCardIdentity(videoIdCardIdentityRequest);
        } catch (ClientException e) {
        	e.printStackTrace();            
        } catch (ServerException e) {
            e.printStackTrace();
        }
    }
}).start();
```
## SDK 详细说明
### 用户配置
用户调用 ClientConfiguration 类的静态方法来修改全局配置。

| 方法                         | 方法描述       | 默认值        |
| -------------------------- | ---------- | ---------- |
| setMaxTaskConcurrentNumber | 设置最大任务并发数  | 5          |
| setHttpConnectTimeout      | HTTP 连接超时时间 | 30*1000ms  |
| setHttpReadTimeout         | HTTP 读超时时间  | 160*1000ms |
| setHttpWriteTimeout        | HTTP 写超时时间  | 160*1000ms |

示例
```
ClientConfiguration.setMaxTaskConcurrentNumber(4);
ClientConfiguration.setHttpConnectTimeout(20 * 1000)；
ClientConfiguration.setHttpReadTimeout(100 * 1000);
ClientConfiguration.setHttpWriteTimeout(100 * 1000);
```
### 签名获取
所有请求均需要多次有效签名。为了方便用户测试，SDK 中提供了本地生成签名的方法，调用 CredentialProvider 对象的getMultipleSign方法即可获得有效签名。但是为了不暴露用户的 SecretKey，正式环境下请在第三方服务器上进行签名。具体签名算法可参考 [签名与鉴权](/document/product/460/6968)。
本地生成签名示例：
```
String appid = "your appid"; 
String secretId = "your secretId";
String secretKey = "your secretKey";
String bucket = "your bucket";
long duration = 3600; //签名有效期为3600秒

CredentialProvider credentialProvider = new CredentialProvider(appid, secretId, secretKey);
String sign = credentialProvider.getMultipleSign(bucket, duration); // 生成签名
```

### 实例化 FaceIdClient
调用构造函数`FaceIdClient(Context context, String appid)`来初始化 FaceIdClient 对象，该对象可以用于发送和取消请求。

| 参数名称    | 类型      | 是否必填 | 参数描述        |
| ------- | ------- | ---- | ----------- |
| context | Context | 是    | 上下文         |
| appid   | String  | 是    | 腾讯云注册的 APPID |
初始化示例：
```
FaceIdClient faceIdClient = new FaceIdClient(context, appid);
```
取消单个任务：
```
int requestId = request.getRequestId(); // 获取请求任务的ID号
boolean success = faceIdClient.cancel(requestId); // 通过请求ID号取消任务
```
如果 FaceIdClient 不再需要使用，请调用 release() 方法释放资源：
```
faceIdClient.release();
```
><font color="#0000cc">**注意：** </font>
发送任务示例请参见 [快速入门](#1)。

### 人脸对比
自带人脸识别数据库，可实时为国内公民提供真实身份信息核验。根据用户的身份证号、姓名，与用户上传的图像进行人脸相似度对比。
#### 通过上传本地图像进行对比
人脸对比请求初始化函数：
```
public ImageIdCardCompareRequest(String bucket, String idCardNumber, String idCardName, File image, String seq);
```
参数说明：

| 参数名称         | 类型     | 是否必填 | 参数描述          |
| ------------ | ------ | ---- | ------------- |
| bucket       | String | 是    | 用户创建的存储桶名称 |
| idCardNumber | String | 是    | 身份证号码         |
| idCardName   | String | 是    | 身份证名称         |
| image        | File   | 是    | 本地图片          |
| seq          | String | 否    | 用于日志查询        |

#### 通过上传图像 url 进行对比
人脸对比请求初始化函数：
```
public static ImageIdCardCompareRequest getInstanceByUrl(String bucket, String idCardNumber, String idCardName, String url, String seq);
```
参数说明：

| 参数名称         | 类型     | 是否必填 | 参数描述          |
| ------------ | ------ | ---- | ------------- |
| bucket       | String | 是    | 用户创建的存储桶名称 |
| idCardNumber | String | 是    | 身份证号码         |
| idCardName   | String | 是    | 身份证名称         |
| url          | String | 是    | 图片的 url 路径      |
| seq          | String | 否    | 用于日志查询        |

返回结果 ImageIdCardCompareResult ：

| 参数名称       | 类型     | 参数描述       |
| ---------- | ------ | ---------- |
| code       | int    | 状态码        |
| message    | String | 结果信息       |
| similarity | float  | 图像和身份证的相似度 |
| seq        | String | 用于日志查询     |
><font color="#0000cc">**注意：** </font>
人脸对比示例代码请参见 [快速入门](#1)。

### 获取唇语
获取一个唇语验证字符串，用于用户录制视频时使用。获取唇语构造函数：
```
public GetLipLanguageRequest(String bucket, String seq);
```
参数说明：

| 参数名称   | 类型     | 是否必填 | 参数描述          |
| ------ | ------ | ---- | ------------- |
| bucket | String | 是    | 用户创建的存储桶名称 |
| seq    | String | 否    | 用于日志查询        |

返回结果 GetLipLanguageResult ：

| 参数名称         | 类型     | 参数描述 |
| ------------ | ------ | ---- |
| code         | int    | 状态码  |
| message      | String | 结果信息 |
| validateData | String | 唇语   |
><font color="#0000cc">**注意：** </font>
获取唇语示例代码请参见 [快速入门](#2)。

### 人脸核身---活体检测视频与用户照片的比对
根据用户提前上传的照片与在线录制的活体视频，通过人脸识别进行匹配验证。人脸核身构造函数：
```
public VideoImageIdentityRequest(String bucket, String validateData, String videoPath, String imagePath, boolean compare, String seq);
```
参数说明

| 参数名称         | 类型      | 是否必填 | 参数描述                  |
| ------------ | ------- | ---- | --------------------- |
| bucket       | String  | 是    | 用户创建的存储桶名称         |
| validateData | String  | 是    | 唇语字符串                 |
| videoPath    | String  | 是    | 本地视频路径                |
| imagePath    | String  | 否    | 本地图片路径                |
| compare      | boolean | 否    |  video 中的照片和 image 是否做对比， |
| seq          | String  | 否    | 用于日志查询                |

返回结果 VideoImageIdentityResult ：

| 参数名称           | 类型     | 参数描述          |
| -------------- | ------ | ------------- |
| code           | int    | 状态码           |
| message        | String | 结果信息          |
| liveStatus     | int    | 活体检测错误码       |
| liveMessage    | String | 活体检测错误描述      |
| compareStatus  | int    | 人脸对比检测错误码     |
| compareMessage | String | 人脸对比检测错误描述    |
| similarity     | int    | 人脸对比检测的相似度    |
| photo          | String | 人脸检测中相似度最高的图像 |

><font color="#0000cc">**注意：** </font>
人脸核身示例代码请参见 [快速入门](#3)。

### 人脸核身---活体检测视频身份信息核验

自带人脸识别数据库，可实时为国内公民提供真实身份信息核验。根据用户的身份证号、姓名，与用户上传的图像进行人脸相似度对比。人脸核身构造函数：

```
VideoIdCardIdentityRequest(String bucket, String validateData, String videoPath, String idCardNumber, String idCardName, String seq);
```
**参数说明**

| 参数名称         | 类型     | 是否必填 | 参数描述          |
| ------------ | ------ | ---- | ------------- |
| bucket       | String | 是    | 用户创建的存储桶名称 |
| validateData | String | 是    | 唇语字符串         |
| videoPath    | String | 是    | 本地视频路径        |
| idCardNumber | String | 是    | 身份证号码         |
| idCardName   | String | 是    | 身份证姓名         |
| seq          | String | 否    | 用于日志查询        |

返回结果 VideoIdCardIdentityResult ：

| 参数名称           | 类型     | 参数描述          |
| -------------- | ------ | ------------- |
| code           | int    | 状态码           |
| message        | String | 结果信息          |
| liveStatus     | int    | 活体检测错误码       |
| liveMessage    | String | 活体检测错误描述      |
| compareStatus  | int    | 人脸对比检测错误码     |
| compareMessage | String | 人脸对比检测错误描述    |
| similarity     | int    | 人脸对比检测的相似度    |
| photo          | String | 人脸检测中相似度最高的图像 |

><font color="#0000cc">**注意：** </font>
人脸核身示例代码请参见 [快速入门](#3)。

