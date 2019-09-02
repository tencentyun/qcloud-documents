## 开发准备

### SDK 获取
人脸核身 SDK 的 Android SDK-1.0.0 下载地址：[Android SDK](https://mc.qcloudimg.com/static/archive/96cb171e0810b55e85689d0c6f17af34/QCloudFaceIdSample_beta.zip)。


### 开发准备
 1. 前往注册： [腾讯云账号注册](https://cloud.tencent.com/register) （详细指引见 [注册腾讯云](https://cloud.tencent.com/document/product/378/9603)）
 2. 取得 `APPID`、`SecretId`、`SecretKey`：请前往 [云 API 密钥](https://console.cloud.tencent.com/cam/capi) ，单击“新建密钥”，目前只支持使用主账号进行调用。

# 快速体验 Demo
1. 修改：找到 app/src/main/java/com/tencent/faceiddemo/MainActivity.java 文件，定位到 initUserInfo() 方法，填入上面申请到的  `APPID`、`BucketName`、`SecretId`、`SecretKey`

2. 运行：工程使用 Gradle 构建，导入 Android Studio 中即可运行
>命令行方式编译安装：工程根目录下执行 `./gradlew installDebug` (macOS) 或 `.\gradlew.bat installDebug` (Windows)

# 集成 SDK 到您的工程中

1.复制 libs 目录下的所有 jar 文件到您工程的 libs 下：
```
faceid-1.1.jar
lib-camera.jar
okhttp-3.2.0.jar
okio-1.6.0.jar
slf4j-android-1.6.1-RC1.jar
```
2.AndroidManifest.xml 增加以下权限：
``` 
<!--网络-->
<uses-permission android:name="android.permission.INTERNET"/>
<!--选择照片或者视频需要-->
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
<!--录制视频需要-->
<uses-permission android:name="android.permission.RECORD_VIDEO" />
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<uses-permission android:name="android.permission.CAMERA" />
<uses-feature android:name="android.hardware.camera" />
``` 
>如果您的工程的 targetSdkVersion >= 23 (Android 6.0) ，那么还需要处理动态权限申请相关事宜，可参考 MainActivity.java 和 RecorderActivity.java

# 快速入门
## 初始化核身引擎 FaceIdClient
```
String appid = "your appid"; // 您申请到的 APPID
FaceIdClient mFaceIdClient = new FaceIdClient(context, appid);
```

## 照片核身（通过照片和身份证信息）
```
/**
 * 照片核身（通过照片和身份证信息）
 * <ol>
 *     <li>校验身份证姓名和号码是否正确</li>
 *     <li>人脸照片与公安照片相似度检测</li>
 * </ol>
 * @param name 姓名
 * @param number 身份证号码
 * @param url 人脸照片链接，如果为 null 则使用本地图片文件 imagePath
 * @param imagePath 人脸照片文件路径，如果为 null 则使用链接 url
 * @param seq 请求标识，用于日志查询
 * @param bucketName bucket 名称
 * @param sign 鉴权签名, 测试时可以调用 {@link CredentialProvider#getMultipleSign(java.lang.String, long)} 来生成
 */
private void sendRequest(String name, String number, String url, String imagePath, String seq, String bucketName, final String sign) {

    final ImageIdCardCompareRequest request;

    if (!TextUtils.isEmpty(url)) {
        request = ImageIdCardCompareRequest.getInstanceByUrl(bucketName, number, name, url, seq);
    } else if (!TextUtils.isEmpty(imagePath)) {
        request = ImageIdCardCompareRequest.getInstanceByPath(bucketName, number, name, imagePath, seq);
    } else {
        Toast.makeText(getApplicationContext(), "请先填写图片URL或者选择图片", Toast.LENGTH_SHORT).show();
        return;
    }

    request.setSign(sign);
    mCurrentRequestId = request.getRequestId();
    
    new Thread(new Runnable() {
        @Override
        public void run() {
            try {
                ImageIdCardCompareResult result = mFaceIdClient.imageIdCardCompare(request);
                if (result != null) {
                    print(result.toString());
                } else {
                    print("result == null");
                }
            } catch (ClientException e) {
                e.printStackTrace();
                print(e.toString());
            } catch (ServerException e) {
                e.printStackTrace();
                print(e.toString());
            }
        }
    }).start();
}
```
返回结果 ImageIdCardCompareResult ：

| 参数名称       | 类型     | 参数描述       |
| ---------- | ------ | ---------- |
| code       | int    | 状态码        |
| message    | String | 结果信息       |
| similarity | float  | 图像和身份证的相似度 |
| seq        | String | 用于日志查询     |

## 获取唇语验证码，用于活体核身
```
/**
 * 获取唇语验证码，用于活体核身
 * @param bucketName bucket 名称
 * @param sign 鉴权签名, 测试时可以调用 {@link CredentialProvider#getMultipleSign(String, long)} 来生成
 * @param seq 请求标识，用于日志查询
 */
private void sendRequest(final String bucketName, final String sign, final String seq) {
    
    final GetLipLanguageRequest request = new GetLipLanguageRequest(bucketName, seq);
    request.setSign(sign);
    mCurrentRequestId = request.getRequestId();

    new Thread() {
        @Override
        public void run() {
            try {
                GetLipLanguageResult result = mFaceIdClient.getLipLanguage(request);
                if (result != null) {
                    print(result.toString());
                } else {
                    print("result == null");
                }
            } catch (ClientException e) {
                e.printStackTrace();
                print(e.toString());
            } catch (ServerException e) {
                e.printStackTrace();
                print(e.toString());
            }
        }
    }.start();
}
```
返回结果 GetLipLanguageResult ：

| 参数名称         | 类型     | 参数描述 |
| ------------ | ------ | ---- |
| code         | int    | 状态码  |
| message      | String | 结果信息 |
| validateData | String | 唇语   |


## 活体核身（通过视频和照片）
```
/**
 * 活体核身（通过视频和照片）
 * <ol>
 *     <li>视频活体检测</li>
 *     <li>视频与照片相似度检测</li>
 * </ol>
 * @param lip 唇语验证码
 * @param videoPath 视频文件路径
 * @param imagePath 人脸图片文件路径
 * @param seq 请求标识，用于日志查询
 * @param sign 鉴权签名, 测试时可以调用 {@link CredentialProvider#getMultipleSign(String, long)} 来生成
 * @param bucketName bucket 名称
 */
private void sendRequest(String lip, String videoPath, String imagePath, String seq, String sign, String bucketName) {
    final VideoImageIdentityRequest request;
    if (TextUtils.isEmpty(imagePath)) {
        request = new VideoImageIdentityRequest(bucketName, lip, videoPath, seq);
    } else {
        request = new VideoImageIdentityRequest(bucketName, lip, videoPath, imagePath, true, seq);
    }
    request.setSign(sign);
    currentRequestId = request.getRequestId();
    
    new Thread(new Runnable() {
        @Override
        public void run() {
            try {
                 VideoImageIdentityResult result = mFaceIdClient.videoImageIdentity(request);
                if (result != null) {
                    print(result.toString());
                } else {
                    print("result == null");
                }
            } catch (ClientException e) {
                e.printStackTrace();
                print(e.toString());
            } catch (ServerException e) {
                e.printStackTrace();
                print(e.toString());
            }
        }
    }).start();
}
```
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


## 活体核身（通过视频和身份证信息）
```
/**
 * 活体核身（通过视频和身份证信息）
 * <ol>
 *     <li>校验身份证姓名和号码是否正确</li>
 *     <li>视频活体检测</li>
 *     <li>视频与公安照片相似度检测</li>
 * </ol>
 * @param name 姓名
 * @param number 身份证号码
 * @param lip 唇语验证码
 * @param videoPath 视频文件路径
 * @param seq 请求标识，用于日志查询
 * @param sign 鉴权签名
 */
private void sendRequest(String name, String number, String lip, String videoPath, String seq, String bucketName, String sign) {
    
    final VideoIdCardIdentityRequest request = new VideoIdCardIdentityRequest(bucketName, lip, videoPath, number, name, seq);
    request.setSign(sign);
    currentRequestId = request.getRequestId();

    new Thread(new Runnable() {
        @Override
        public void run() {
            try {
                VideoIdCardIdentityResult result = mFaceIdClient.videoIdCardIdentity(request);
                if (result != null) {
                    print(result.toString());
                } else {
                    print("result == null");
                }
            } catch (ClientException e) {
                e.printStackTrace();
                print(e.toString());
            } catch (ServerException e) {
                e.printStackTrace();
                print(e.toString());
            }
        }
    }).start();
}
```
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

## SDK 详细说明
### 用户配置
用户调用 ClientConfiguration 类的静态方法来修改全局配置。


| 方法                         | 方法描述       | 默认值        |
| -------------------------- | ---------- | ---------- |
| setMaxTaskConcurrentNumber | 设置最大任务并发数  | 5          |
| setHttpConnectTimeout      | HTTP 连接超时时间 | 30*1000ms  |
| setHttpReadTimeout         | HTTP 读超时时间  | 160*1000ms |
| setHttpWriteTimeout        | HTTP 写超时时间  | 160*1000ms |

示例：
```
ClientConfiguration.setMaxTaskConcurrentNumber(4);
ClientConfiguration.setHttpConnectTimeout(20 * 1000)；
ClientConfiguration.setHttpReadTimeout(100 * 1000);
ClientConfiguration.setHttpWriteTimeout(100 * 1000);
```
### 签名获取
所有请求均需要多次有效签名。为了方便用户测试，SDK 中提供了本地生成签名的方法，调用 CredentialProvider 对象的getMultipleSign方法即可获得有效签名。但是为了不暴露用户的 SecretKey，正式环境下请在第三方服务器上进行签名。具体签名算法可参考 [签名与鉴权](https://cloud.tencent.com/document/product/460/6968)。

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

### 取消单个任务
```
int requestId = request.getRequestId(); // 获取请求任务的ID号
boolean success = faceIdClient.cancel(requestId); // 通过请求ID号取消任务
```
