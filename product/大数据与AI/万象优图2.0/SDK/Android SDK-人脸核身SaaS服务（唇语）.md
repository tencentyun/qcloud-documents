## 唇语人脸核身 SaaS 服务 Android-SDK 说明文档

腾讯云万象优图人脸核身服务指通过人脸智能识别技术与OCR技术相结合，在线验证用户自拍视频或照片与身份证照片的匹配关系，秒级确认用户的身份是否真实有效。基于唇语活体检测的人脸核身SaaS服务提供集成了UI的一站式服务，开发者可以轻松集成SDK即可使用人脸核身服务。腾讯云提供IOS与Android的SDK，本文将介绍Android的SDK的集成方式。

### 1、开发准备

[参考demo：](https://github.com/rickenwang/facein-sdk-android/tree/master)请单击此链接查看Android开发参考demo。

#### 获取账号

- 开发者使用人脸识别功能前，需要先在腾讯云-万象优图控制台注册账号，并获得appid、SecretId和SecretKey等；
- 支持Android 4.0及其以上版本；

#### SDK配置

##### 导入下列相关库：
**腾讯云相关**

- facein：腾讯云人脸核身SAAS组件
- faceid：腾讯云人脸核身PAAS SDK
- qimage：腾讯云图片云PAAS SDK

**其他常用类库**

- okhttp-3.2.0.jar
- okio-1.6.0.jar
- slf4j-android-1.6.1-RC1.jar

**人脸核身SAAS服务可以通过本地构建和远程构建两种方式来添加到您的应用中:**

**远程构建方式（推荐）**
如果您是用gradle的方式来构建应用，那么我们强烈建议您使用远程方式进行构建。您只需要在Module目录下的build.gradle文件下添加：

```
compile 'com.tencent.facein:facein:latest.release:@aar'
compile 'com.tencent.faceid:faceid:1.0.1'
compile 'com.tencent.qimage:qimage:2.0.0'
compile 'com.squareup.okhttp3:okhttp:3.6.0'
compile 'org.slf4j:slf4j-android:1.6.1-RC1'
```
**本地构建方式**

下载腾讯云facein、faceid、qimage三个库，以及常用的okhttp3、okio以及slf4j三个库，然后将这6个库文件放在lib目录下，并添加到gradle的构建路径中即可。


SDK需要的危险权限包括

```
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
<uses-permission android:name="android.permission.RECORD_VIDEO" />
<uses-permission android:name="android.permission.RECORD_AUDIO"/>
<uses-permission android:name="android.permission.CAMERA" />
```
feature包括

```
<uses-feature android:name="android.hardware.camera"/>
<uses-feature android:name="android.hardware.camera.front"/>
<uses-feature android:name="android.hardware.camera.autofocus"/>
```
这些权限和特性均已经在SDK Module中的AndroidManifest.xml文件中定义，其动态权限SDK也自动帮您进行管理，您**无需**自己去写代码添加和管理这些权限。

### 2、快速入门

首先，您只需要配置一些FaceInConfig类的静态成员变量，然后在您自定义的Activity中启动FaceInEntryActivty即可。

代码示例

```
String appid = "your appid";
String bucket = "your bucket";
String secret_id = "your secret id";
String secret_key = "your secret key";

// 1、配置用户基本信息
FaceInConfig.setAppid(appid);
FaceInConfig.setBucket(bucket);

// 2、配置本地签名方式    
AbsCredentialProvider credentialProvider = new LocalCredentialProvider(secret_id, secret_key);
FaceInConfig.setCredentialProvider(credentialProvider);

// 3、配置识别模式为短视频活体检测
FaceInConfig.setOcrModel(FaceInModelType.OCR_ID_CARD_LIP_VIDEO_COMPARE);

// 4、启动人脸核身入口Activity
Intent intent = new Intent(YourActivity.this, FaceInEntryActivity.class);
YourActivity.this.startActivity(intent);
```

### 3、详细说明

#### 签名
签名是后台对SDK请求合法性的校验凭据，我们提供了两种方式来对请求进行签名：

- 本地签名：SDK中提供了LocalCredentialProvider类来进行本地签名，但是需要用户提供secret_key，这会使得用户将自己的机密信息硬编码到代码中，存在泄漏的风险，因此在您的发布版本中我们强烈建议您不要使用这种方式进行签名。
- 远程服务器签名：用户需要自己子类化AbsCredentialProvider这个抽象类，实现该类的encrypt方法（实现方式可以参考LocalCredentialProvider），将对secret_key和加密原始串的过程放在远程服务器中，来保证secret_key的安全性。

[签名算法](https://cloud.tencent.com/document/product/460/6968)主要包括拼凑原始串和利用secret_key将原始串加密为签名两个步骤，使用本地签名时SDK帮用户实现了这两个步骤，而在远程服务器中签名方式下，SDK帮用户实现了第一步，用户只需要将拼凑好的原始串利用secret_key进行加密即可。
代码示例：

```
// 1、获得secret_id （secret_id不是机密信息）
String secretId = "your secret_id";

// 2、自定义credentialProvider
AbsCredentialProvider credentialProvider = new AbsCredentialProvider(secret_id) {
    @Override
    protected String encrypt(String source) {
    	// todo 
    	String sign = ... // 自己在远程服务器上将source加密为sign
        return sign;
    }
};

// 3、将credentialProvider设置到FaceInConfig的静态变量中
FaceInConfig.setCredentialProvider(credentialProvider);
```

#### 人脸核身类型

目前支持的人脸核身类型（**FaceInModelType**）包括：

- ```OCR_ID_CARD_IMAGE_COMPARE``` ：用户扫描身份证后，拍照进行身份验证。
- ```OCR_ID_CARD_LIP_VIDEO_COMPARE```：用户扫描身份证后，录制短视频来进行身份以及活体校验

代码示例：

```
// 设置人脸核身类型为 OCR_ID_CARD_LIP_VIDEO_COMPARE
FaceInConfig.setOcrModel(FaceInModelType.OCR_ID_CARD_LIP_VIDEO_COMPARE);
```

#### 识别完成回调

当用户在任意核身类型下完成最后校验过程后，SDK会根据识别的结果进行回调。
##### FaceInResultListener

```
/**
 * 识别成功回调函数
 *
 * @param modelType 识别类型
 * @param person 扫描到的身份证信息
 */
void onSuccess(FaceInModelType modelType, IdCardInfo person);

/**
 * 识别失败回调函数
 *
 * @param modelType 识别类型
 * @param failedType 失败原因
 */
void onFailed(FaceInModelType modelType, FaceInFailedType failedType);
```
识别成功后，通过onSuccess方法返回识别类型以及识别人的基本信息，如果识别失败，则通过onFailed方法返回识别失败原因。

##### IdCardInfo

IdCardInfo类包括了身份证上的5个基本信息：

| 类型     | 名称        | 信息     |
| ------ | --------- | ------ |
| String | name      | 姓名     |
| String | idNumber  | 公民身份号码 |
| String | address   | 住址     |
| String | authority | 签发机关   |
| String | date      | 有效期限   |

##### FaceInFailedType

目前只返回识别置信度小于阈值错误

- ```FACE_IN_SIMILARITY_LOW``` ：识别置信度小于用户设置的阈值。

代码示例：

```
FaceInConfig.setFaceInResultListener(new FaceInResultListener() {
    @Override
    public void onSuccess(FaceInModelType modelType, IdCardInfo person) {

        QLogger.debug(logger, "{} 识别成功，识别人信息为：{}", modelType.getMessage(), person.toString());
    }

    @Override
    public void onFailed(FaceInModelType modelType, FaceInFailedType failedType) {

        QLogger.debug(logger, "{} 识别失败，失败原因为：{}", modelType.getMessage(), failedType.getMessage());
    }
});
```

#### 其他

置信度阈值设置、HTTP超时时间设置、是否打印debug日志

| 类型   | 名称                              | 信息                                       | 默认值     | 范围     |
| ---- | ------------------------------- | ---------------------------------------- | ------- | ------ |
| int  | idCardPersonCompareConfidence   | ```OCR_ID_CARD_IMAGE_COMPARE```置信度阈值     | 70      | 0~100  |
| int  | lipVideoPersonCompareConfidence | ```OCR_ID_CARD_LIP_VIDEO_COMPARE``` 置信度阈值 | 70      | 0~100  |
| int  | httpConnectTimeout              | HTTP连接超时时间                               | 10000ms | >500ms |
| int  | httpWriteTimeout                | HTTP写超时时间                                | 20000ms | >500ms |
| int  | httpReadTimeout                 | HTTP读超时时间                                | 20000ms | >500ms |

代码示例：

```
// 设置识别成功置信度阈值
FaceInConfig.setIdCardPersonCompareConfidence(70);
FaceInConfig.setLipVideoPersonCompareConfidence(70);

// 设置HTTP超时时间
FaceInConfig.setHttpConnectTimeout(5000);
FaceInConfig.setHttpWriteTimeout(20000);
FaceInConfig.setHttpReadTimeout(20000);

// 设置是否打印debug日志，默认打印
FaceInConfig.setDebug(true);
```
