## 1. 开发准备

### 1.1 SDK获取
人脸核身sdk的Android SDK-1.0.0下载地址：[Android SDK](https://mc.qcloudimg.com/static/archive/9f5229f0bb019f5fe5b9f6b7bc6134af/faceid-1.0.0.zip)
更多示例可以参考Demo：[Android SDK Demo](https://mc.qcloudimg.com/static/archive/6e5c11cd423409f50804410e47b04e9a/FaceIdDemo+.zip)

### 1.2 开发准备
1. 开发者使用人脸识别功能前，需要先在腾讯云-万象优图控制台注册账号，并获得appid、SecretId和SecretKey等；
2. 手机必须要有网络（GPRS、3G或Wifi等）；
3. 支持Android 4.0及其以上版本；

### SDK配置

1、导入下列jar包
- faceid-1.0.0.jar
- okhttp-3.2.0.jar
- okio-1.6.0.jar
- slf4j-android-1.6.1-RC1.jar

2、在AndroidManifest.xml中增加如下权限
```
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
<uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS"/>
```
## 2. 快速入门
### 初始化FaceIdClient
```
Context context = getApplicationContext();
String appid = "your appid";

final FaceIdClient faceIdClient = new FaceIdClient(context, appid);
```
### 人脸对比
**1、通过上传本地图像进行对比**
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
**2、通过上传图像url进行对比**

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
### 人脸核身
**1、根据用户上传的照片和视频，进行人脸核身验证**
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
**2、根据用户的身份证号、姓名，与用户上传的图像进行人脸相似度对比。**
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
## SDK详细说明
### 用户配置
用户调用ClientConfiguration类的静态方法来修改全局配置。

| 方法                         | 方法描述       | 默认值        |
| -------------------------- | ---------- | ---------- |
| setMaxTaskConcurrentNumber | 设置最大任务并发数  | 5          |
| setHttpConnectTimeout      | HTTP连接超时时间 | 30*1000ms  |
| setHttpReadTimeout         | HTTP读超时时间  | 160*1000ms |
| setHttpWriteTimeout        | HTTP写超时时间  | 160*1000ms |

示例
```
ClientConfiguration.setMaxTaskConcurrentNumber(4);
ClientConfiguration.setHttpConnectTimeout(20 * 1000)；
ClientConfiguration.setHttpReadTimeout(100 * 1000);
ClientConfiguration.setHttpWriteTimeout(100 * 1000);
```
### 签名
所有请求均需要多次有效签名。为了方便用户测试，sdk中提供了本地生成签名的方法，调用CredentialProvider对象的getMultipleSign方法即可获得有效签名。但是为了不暴露用户的secretKey，正式环境下请在第三方服务器上进行签名。[具体签名算法](https://www.qcloud.com/doc/product/275/3805)
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

### 实例化FaceIdClient
调用构造函数```FaceIdClient(Context context, String appid)```来初始化FaceIdClient对象，该对象可以用于发送和取消请求。

| 参数名称    | 类型      | 是否必填 | 参数描述        |
| ------- | ------- | ---- | ----------- |
| context | Context | 是    | 上下文         |
| appid   | String  | 是    | 腾讯云注册的appid |
初始化示例：
```
FaceIdClient faceIdClient = new FaceIdClient(context, appid);
```
取消单个任务：
```
int requestId = request.getRequestId(); // 获取请求任务的ID号
boolean success = faceIdClient.cancel(requestId); // 通过请求ID号取消任务
```
如果FaceIdClient不再需要使用，请调用release()方法释放资源：
```
faceIdClient.release();
```
> 发送任务示例请参见快速入门

### 人脸对比
自带人脸识别数据库，可实时为国内公民提供真实身份信息核验。根据用户的身份证号、姓名，与用户上传的图像进行人脸相似度对比。
1、通过上传本地图像进行对比。人脸对比请求初始化函数：

```
public ImageIdCardCompareRequest(String bucket, String idCardNumber, String idCardName, File image, String seq);
```

参数说明：

| 参数名称         | 类型     | 是否必填 | 参数描述          |
| ------------ | ------ | ---- | ------------- |
| bucket       | String | 是    | 用户创建的bucket名称 |
| idCardNumber | String | 是    | 身份证号码         |
| idCardName   | String | 是    | 身份证名称         |
| image        | File   | 是    | 本地图片          |
| seq          | String | 否    | 用于日志查询        |

2、通过上传图像url进行对比。人脸对比请求初始化函数：
```
public static ImageIdCardCompareRequest getInstanceByUrl(String bucket, String idCardNumber, String idCardName, String url, String seq);
```
参数说明：

| 参数名称         | 类型     | 是否必填 | 参数描述          |
| ------------ | ------ | ---- | ------------- |
| bucket       | String | 是    | 用户创建的bucket名称 |
| idCardNumber | String | 是    | 身份证号码         |
| idCardName   | String | 是    | 身份证名称         |
| url          | String | 是    | 图片的url路径      |
| seq          | String | 否    | 用于日志查询        |

返回结果ImageIdCardCompareResult：

| 参数名称       | 类型     | 参数描述       |
| ---------- | ------ | ---------- |
| code       | int    | 状态码        |
| message    | String | 结果信息       |
| similarity | float  | 图像和身份证的相似度 |
| seq        | String | 用于日志查询     |
>**人脸对比示例代码请参见*快速入门***

### 获取唇语
获取一个唇语验证字符串，用于用户录制视频时使用。获取唇语构造函数：
```
public GetLipLanguageRequest(String bucket, String seq);
```
参数说明：

| 参数名称   | 类型     | 是否必填 | 参数描述          |
| ------ | ------ | ---- | ------------- |
| bucket | String | 是    | 用户创建的bucket名称 |
| seq    | String | 否    | 用于日志查询        |

返回结果GetLipLanguageResult：

| 参数名称         | 类型     | 参数描述 |
| ------------ | ------ | ---- |
| code         | int    | 状态码  |
| message      | String | 结果信息 |
| validateData | String | 唇语   |
>**获取唇语示例代码请参见*快速入门***

### 人脸核身---活体检测视频与用户照片的比对

根据用户提前上传的照片与在线录制的活体视频，通过人脸识别进行匹配验证。人脸核身构造函数：

```
public VideoImageIdentityRequest(String bucket, String validateData, String videoPath, String imagePath, boolean compare, String seq);
```
参数说明

| 参数名称         | 类型      | 是否必填 | 参数描述                  |
| ------------ | ------- | ---- | --------------------- |
| bucket       | String  | 是    | 用户创建的bucket名称         |
| validateData | String  | 是    | 唇语字符串                 |
| videoPath    | String  | 是    | 本地视频路径                |
| imagePath    | String  | 否    | 本地图片路径                |
| compare      | boolean | 否    | video中的照片和image是否做对比， |
| seq          | String  | 否    | 用于日志查询                |

返回结果VideoImageIdentityResult：

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
>**人脸核身示例代码请参见*快速入门***

### 人脸核身---活体检测视频身份信息核验

自带人脸识别数据库，可实时为国内公民提供真实身份信息核验。根据用户的身份证号、姓名，与用户上传的图像进行人脸相似度对比。人脸核身构造函数：

```
VideoIdCardIdentityRequest(String bucket, String validateData, String videoPath, String idCardNumber, String idCardName, String seq);
```

参数说明

| 参数名称         | 类型     | 是否必填 | 参数描述          |
| ------------ | ------ | ---- | ------------- |
| bucket       | String | 是    | 用户创建的bucket名称 |
| validateData | String | 是    | 唇语字符串         |
| videoPath    | String | 是    | 本地视频路径        |
| idCardNumber | String | 是    | 身份证号码         |
| idCardName   | String | 是    | 身份证姓名         |
| seq          | String | 否    | 用于日志查询        |

返回结果VideoIdCardIdentityResult：

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

> **人脸核身示例代码请参见*快速入门***

