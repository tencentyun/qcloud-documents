## 配置流程
>! 接入之前，请详细阅读 SDK 中的 readme 和接入指引。

以下为接入配置的步骤：
### 1. SDK 集成
SDK 支持 cocoapods 和手动两种方式集成。

#### 1.1 SDK pod 集成
如果您的项目已经支持 cocopods ，可以使用本方式集成 SDK，本示例使用的 cocoapods 为 1.7.2。
下载的 OCR SDK 文件夹目录结构如下：
```
├── OCR_private_pod
│ ├── LICENSE
│ ├── Libs
│ └── WBOCRService.podspec
├── README
├── WBOCRDemo
│ ├── Podfile
│ ├── Podfile.lock
│ ├── Pods
│ ├── WBOCRDemo
│ ├── WBOCRDemo.xcodeproj
│ └── WBOCRDemo.xcworkspace
└── 接入指引.md

```
OCR_private_pod 文件夹下面是 OCR SDK 的 pod 仓库，这个仓库名称为 WBOCRService ，WBOCRDemo 文件夹下是示例 demo，通过 pod 方式集成，需要完成以下 3 个步骤：
1. 将 OCRprivatepod 文件夹移动到指定的位置（这个位置可以依据您项目文件的布局而定）。
2. 在 podfile 中引用 pod。
3. 执行 pod install 完成安装。

#### 1.2 SDK 手动集成
- 下载 OCR SDK，找到 OCRprivatepod/Lib 文件夹，SDK 文件在这个文件夹下。
- 拖拽 SDK 文件到 Xcode 工程内 (请勾选Copy items if needed选项) ，其中包括WBOCRService.bundle、WBOCRService.framework、YTCommon.framework、YTImageRefiner.framework 以及 tiny_opencv2.framework。
```
├── WBOCRService.bundle
├── WBOCRService.framework
├── YTCommon.framework
├── YTImageRefiner.framework
└── tiny_opencv2.framework
```

- 在Build Phases -> link with libraries 下加入如下依赖。
```
CoreTelephony.framework
CoreServices.framework
CoreMedia.framework
AssetsLibrary.framework
AVFoundation.framework
SystemConfiguration.framework
WebKit.framework
libc++.tbd
```

- Build Setting --> Linking --> Other Linker Flag 设置 增加 -ObjC 和 -lz linker flag

### 2. 集成过程中注意事项
**cocoapods 集成时 `:path` 参数说明**
使用 `:path` 参数，在指定路径下加载 pods ，这个路径是本质上是 WBOCRService.podspec 相对 podfile 的路径。在示例 WBOCRDemo 中，如下：
```
target 'WBOCRDemo' do
pod 'WBOCRService',:path => '../OCR_private_pod'
end
```
## 接口调用
SDK 中需要使用 camera，需要在 Info.plist 中为 NSCameraUsageDescription 添加描述信息。
### 1. 概述
OCR SDK 对外提供以下两类证件的识别能力：
- 身份证识别
- 银行卡识别

SDK 提供以下接入方式：标准模式接入。传统的接入方式，SDK 完成整个识别流程，给用户返回识别结果。
在 SDK 附的 demo 中，有提供以上接入方式的接入示例，详细接入请参考 demo 工程中的示例代码。

### 2. SDK 头文件说明
SDK 一共对外暴露了 4 个头文件，如下所示：
```
├── Headers
│   ├── WBBankCardInfoModel.h
│   ├── WBIDCardInfoModel.h
│   ├── WBOCRConfig.h
│   ├── WBOCRService.h
```

这些头文件可以大致分为三类：
- 模型类（WBBankCardInfoModel 和 WBIDCardInfoModel ），这些模型类分别对应银行卡和身份证的识别结果字段。
- 配置类（WBOCRConfig），这个类提供了 SDK 的配置选项。
- 入口类（WBOCRService），这个类提供 SDK 的入口和回调。

#### 2.1 模型类说明
模型类对外暴露识别结果，以身份证识别为例，WBIDCardInfoModel 类的实例返回身份证识别结果，结果中包含如下字段：
```
• idcard 公民身份号码
• name 姓名
• sex 性别
• nation 民族
• address 住址
• birth 出生
• authority 签发机关
• validDate 有效期限
• frontFullImg 国徽面截图
• backFullImg 人像面截图
• orderNo 每次OCR识别请求的唯一订单号: 建议为32位字符串(不超过32位)
• sign 签名信息
• warning 识别结果警告信息
• multiWarning 多重告警码，人像面是 frontMultiWarning，国徽面对应 backMultiWarning
• clarity  图片清晰度，人像面是 frontClarity，国徽面对应 backClarity
```
开发者按需获取需要的信息。
其余证件识别与之类似，详情参考类头文件的字段注释。

#### 2.2 配置类说明
WBOCRConfig 对外提供配置接口，下面的内容逐一介绍其核心接口。
WBOCRConfig 是一个单例，开发者必须通过制定的初始化方法 sharedConfig 初始化。支持的主要配置项如下：
```
/// default NO, 设置成 YES 之后, 识别结果没有告警才判定为识别成功.
@property (nonatomic, assign) BOOL checkWarnings;
/**
 * @brief 设置识别超时时间，默认是20.0s
 */
@property (nonatomic) NSTimeInterval timeoutInterval;
/**
 * @brief 是否需要录制视频。此功能目前仅适用于身份证识别，默认为NO，即不录制；设置为 YES，识别成功之后，会返回长度不超过 3s 的视频地址
 */
@property (nonatomic) BOOL needRecordVideo ;
/**
 * @brief 控制身份证识别是否返回切边图, BOOL类型，默认值为 NO
 * 当这个值设置为 YES 的时候,进行身份证人像面识别时, 切边图会在 frontCrop 字段返回; 进行身份证国徽面识别时,切边图会在 backCrop 字段返回
 * 当这个值设置为 NO  的时候,进行身份证识别的时候, frontCrop 和 backCrop 返回 nil
 */
@property (nonatomic) BOOL retCrop;
```

#### 2.3 标准模式入口类说明
WBOCRService 是 SDK 的入口类，需要通过制定的初始化方法 sharedService 进行初始化。
```
/**
 * @brief WBOCRService 单例方法，通过调用该方法实例化 WBOCRService对象
 *
 * @return WBOCRService对象
 */
 + (nonnull instancetype) sharedService;

SDK支持身份证证件识别，提供 3 种识别模式，通过 WBOCRCardType 来定义。
/// * @brief  OCR SDK 提供证件的识别能力：身份证识别
///
/// WBOCRCardType 定义 SDK 不同的识别模式，下面描述这些模式：
/// 1. 身份证识别（识别身份证人像面和国徽面）
///     - WBOCRSDKTypeIDCardFrontSide: 身份证人像面识别模式，在 SDK 中完成人像面识别，识别完成之后，将本次识别结果返回第三方APP
///     - WBOCRSDKTypeIDCardBackSide: 身份证国徽面识别模式，在 SDK 中完成国徽面识别，识别完成之后，将本次识别结果返回第三方APP
///     - WBOCRSDKTypeIDCardContinuous:  身份证识别连拍模式，在 SDK 中完成人像面 + 国徽面识别，识别完成之后，将本次识别结果返回第三方APP

typedef NS_ENUM(NSInteger, WBOCRCardType) {
    WBOCRSDKTypeIDCardFrontSide = 1,
    WBOCRSDKTypeIDCardBackSide = 2,
    WBOCRSDKTypeIDCardContinuous = 7,
    WBOCRSDKTypeIDCardNormal NS_ENUM_DEPRECATED_IOS(9_0, 12_0,"User WBOCRSDKTypeIDCardContinuous") = 0,
};
```
SDK 接入分为两个步骤：
- init SDK，调用 init 接口完成 SDK 登录。
- startService，init 成功之后，调用这个接口开始识别。

>! init 和 startService 接口一一对应。

init SDK 接口如下：
```
/// 标准版本 SDK 登录接口, 这个接口完成 SDK 登录
/// @param sdkType     本次识别的卡证类型,详细参考 `WBOCRCardType`
/// @param appId       人脸核身控制台内申请的 ## 开发准备
### 权限检测
SDK 需要用到相机权限

#### Android 6.0 及以上系统
SDK 运行时提示权限，需要用户授权。

#### Android 6.0 以下系统
 - Android 并没有运行时权限，检测权限只能靠开关相机进行。考虑到 SDK 的使用时间很短，快速频繁开关相机可能会导致手机抛出异常，故 SDK 内对 Android 6.0 以下手机没有做权限的检测。
 - 为了进一步提高用户体验，在 Android 6.0 以下系统上，我们建议合作方在拉起 SDK 前，帮助 SDK 做相机权限检测，提示用户确认打开了权限后再进行银行卡 OCR 识别，可以使银行卡识别体验更快更好。

### CPU 平台设置
目前 SDK 支持 armeabi、armeabi-v7a、arm64-v8a，为了防止在其他 CPU 平台上 SDK Crash，建议在您的 App 的 build.gradle 里加上 abiFilter，如下所示：

```
defaultConfig {
    ndk {
          //设置支持的 so 库框架
          abiFilters 'armeabi-v7a', 'armeabi', 'arm64-v8a'
     }
}
```
## 配置流程
### 接入配置
#### 注意事项
- OCR SDK（WbCloudOcr）最低支持到 Android API 14: Android 4.0(ICS)，请在构建项目时注意版本是否支持。
- WbCloudOcr 将以 AAR 文件的形式提供。
- 需要为 Android SDK 添加依赖，方式如下：
将提供的 AAR 文件加入到 App 工程的 libs 文件夹下面，并且在 build.gradle 中添加下面的配置。
```
android{
     //...
     repositories {
        flatDir {
            dirs 'libs' //this way we can find the .aar file in libs folder
        }
    }
}
//添加依赖
dependencies {
     //0. appcompat-v4
 compile 'com.android.support:appcompat-v4:23.1.1'
  //1. 云Ocr SDK
 compile(name: 'WbCloudOcrSdk-proRelease', ext: 'aar')
  //2.云公共组件
compile(name: 'WbCloudNormal-release-v5.1.1', ext: 'aar')
}
```

### 混淆配置
云 OCR 产品的混淆规则分为两部分，分别是云 OCR SDK 的混淆规则(v2.7.X之后的版 WbCloudOcrSdk 已经内置了混淆规则，接入方可以忽略不加载)，云公共组件的混淆规则（接入方必须加载）。
- 云 OCR SDK 的混淆规则
```
######################云 ocr 混淆规则 ocr-BEGIN##########################
-keepattributes InnerClasses
-keep public class com.tencent.cloud.huiyansdkocr.net.*$*{
    *;
}
-keep public class com.tencent.cloud.huiyansdkocr.net.*{
    *;
}
-keep public class com.tencent.fujikoli.recdetectdemo.Jni.ScanRecNative{*;}

#######################云 ocr 混淆规则 ocr-END###########################
```

- 云公共组件的混淆规则
```
#######################normal混淆规则-BEGIN#############################
#不混淆内部类
-keepattributes InnerClasses
-keepattributes *Annotation*
-keepattributes Signature
-keepattributes Exceptions

-keep public class com.tencent.cloud.huiyansdkface.normal.net.*$*{
    *;
}
-keep public class com.tencent.cloud.huiyansdkface.normal.net.*{
    *;
}
-keep public class com.tencent.cloud.huiyansdkface.normal.thread.*{
   *;
}
-keep public class com.tencent.cloud.huiyansdkface.normal.tools.*{
   *;
}
-keep public class com.tencent.cloud.huiyansdkface.normal.thread.*$*{
   *;
}

-keep public class com.tencent.cloud.huiyansdkface.normal.tools.secure.*{
   *;
}

-keep public class com.tencent.cloud.huiyansdkface.normal.tools.WLogger{
    *;
}
-keep class com.tencent.bugly.idasc.**{
    *;
}
#wehttp混淆规则
-dontwarn com.tencent.cloud.huiyansdkface.okio.**
-keep class com.tencent.cloud.huiyansdkface.okio.**{
    *;
}

# 里面 有 Java8的一些类 如 Duration
-dontwarn com.tencent.cloud.huiyansdkface.okhttp3.OkHttpClient$Builder
-keep class com.tencent.cloud.huiyansdkface.wehttp2.**{
    public <methods>;
}

-keep class com.tencent.cloud.huiyansdkface.okhttp3.**{
    public <methods>;
}

-keep interface com.tencent.cloud.huiyansdkface.wehttp2.**{
    public <methods>;
}
-keep public class com.tencent.cloud.huiyansdkface.wehttp2.WeLog$Level{
    *;
}
-keep class com.tencent.cloud.huiyansdkface.wejson.*{
    *;
}

-keep public class com.tencent.cloud.huiyansdkface.wehttp2.WeReq$ErrType{
    *;
}

-keep class * extends com.tencent.cloud.huiyansdkface.wehttp2.WeReq$WeCallback{
   public <methods>;
}

-keep class com.tencent.cloud.huiyansdkface.okio.**{
    *;
}
#######################normal混淆规则-END#############################
```
您可以将如上代码拷贝到您的混淆文件中，也可以将 SDK 中的 `kyc-cloud-normal-proguard-rules.pro` 拷贝到主工程根目录下，然后通过 `-include kyc-cloud-normal-proguard-rules.pro` 加入到您的混淆文件中。

## 接口调用
SDK 接口提供的是有 UI 模式：：SDK 对接口进行封装并且实现了识别页面，合作方只需要调用接口，即可以快速拉起 SDK，接收结果回调。接入简单，适合快速接入。
### SDK 接口调用方法
SDK 代码调用的入口为 `com.tencent.cloud.huiyansdkocr.WbCloudOcrSDK ` 这个类。
```
public class WbCloudOcrSDK{

/**
* 该类为一个单例，需要先获得单例对象再进行后续操作
   */
       public static synchronized WbCloudOcrSDK getInstance() {
       //    ...
       }

 /**
  * 初始化云Ocr SDK，完成登录
  * @param context        拉起SDK的context
  * @param wbocrtypemode  识别证件的模式，参数是枚举类型
  * @param data           第三方需要传入的参数
  * @param loginListener  登录SDK回调
  */
public void init(Context context,WBOCRTYPEMODE wbocrtypemode,Bundle data,OcrLoginListener loginListerner){
//    ...
}
   /**
     * 登录成功后，调用此函数拉起 sdk 页面
     * @param context                  拉起 SDK 的上下文
     * @param idCardScanResultListener 返回到第三方的接口
     */
    public void startActivityForOcr(Context context,IDCardScanResultListener){
  // ...
 }
/**
  * 登录回调接口
  */
public interface OcrLoginListener {
        void onLoginSuccess();
        void onLoginFailed(String errorCode, String errorMsg);
    }

/**
  * 退出 SDK,返回第三方的回调,同时返回 ocr 识别结果
  */
public interface IDCardScanResultListener{
        /**
         * @RARAM exidCardResult   SDK 返回的识别结果的错误码  
* @RARAM exidCardResult   SDK 返回的识别结果的错误信息    
         */
        void onFinish(String errorCode, String errorMsg);
}
```

 **NONCE 类型的 ticket，其有效期为120秒，且一次性有效，即每次启动 SDK 刷脸都要重新请求 NONCE ticket，重新算 sign。同时建议合作方做前端保护，防止用户连续点击，短时间内频繁启动 SDK。**
`WbCloudOcrSdk.init()`的第二个参数用来传递数据，可以将参数打包到`data(Bundle)`中，必须传递的参数包括：

```
//这些都是 WbCloudOcrSdk.InputData 对象里的字段，是需要传入的数据信息
String orderNo;  //每次OCR识别请求的唯一订单号: 建议为32位字符串(不超过32位)
String openApiAppId;  //APP_ID 
String openApiAppVersion;  //openapi  Version
String openApiNonce; //32 位随机字符串
String openApiUserId; //user id
String openApiSign; //签名信息
```
>! 以上参数被封装在 WbCloudFaceVerifySdk.InputData 对象中（它是一个 Serializable 对象）。

EXBankCardResult 代表 SDK 返回的识别银行卡的结果，该类属性如下所示：
```
public String ocrId;//识别的唯一标识
public String bankcardNo;//识别的银行卡号
public String bankcardValidDate;//识别的银行卡的有效期
public String orderNo;//每次OCR识别请求的唯一订单号: 建议为32位字符串(不超过32位)
public String warningMsg;   //识别的警告信息
public String warningCode;  //识别的警告码
public Bitmap bankcardNoPhoto;//识别的银行卡的卡号图片
```
登录回调接口
```
/**
  * 登录回调接口
  */
public interface OcrLoginListener {
        void onLoginSuccess();//登录成功
          /**
           * @PARAM errorCode 登录失败错误码
           * @PARAM errorMsg  登录失败错误信息
           */        
         void onLoginFailed(String errorCode, String errorMsg);
    }
```
返回第三方接口
```
/**
  * 退出 SDK,返回第三方的回调,同时返回ocr识别结果
  */
public interface IDCardScanResultListener{
        /**
         * 退出 SDK,返回第三方的回调,同时返回 ocr 识别结果
         * @param errorCode        返回错误码，识别成功返回 0
         * @param errorMsg        返回错误信息，和错误码相关联         */
        void onFinish(String errorCode, String errorMsg);
}
```
#### 银行卡识别结果类
银行卡识别结果封装在 EXBankCardResult 类中，通过`WbCloudOcrSDK.getInstance().getBankCardResult()`获得，该类属性如下所示：
```
public String ocrId;//ocrId
public String bankcardNo;//卡号
public String bankcardValidDate;//有效期
public String orderNo;//每次OCR识别请求的唯一订单号: 建议为32位字符串(不超过32位)
public String warningMsg;//告警信息
public String warningCode;//告警码
public Bitmap bankcardNoPhoto; //卡号切边图
public String bankcardFullPhoto;//银行卡图片存放路径
public String multiWarningCode;//多重告警码
public String multiWarningMsg;//多重告警信息
public String clarity;//清晰度得分
public String sign;//签名
```

#### [接口参数说明](id:canshu)
**NONCE 类型的 ticket，其有效期为120秒，且一次性有效，即每次启动 SDK 刷脸都要重新请求 NONCE ticket，重新算 sign。同时建议合作方做前端保护，防止用户连续点击，短时间内频繁启动 SDK。**
InputData 是用来给 SDK 传递一些必须参数所需要使用的对象（WbCloudOcrSdk.init() 的第二个参数），合作方需要加入 SDK 需要的一些数据以便启动 OCR SDK。
其中 InputData 对象中的各个参数定义如下表，请合作方按下表标准加入对应的数据。

| 参数              | 说明                                                         | 类型                  | 长度（字节）       | 是否必填 |
| ----------------- | ------------------------------------------------------------ | --------------------- | ------------------ | -------- |
| orderNo     | 每次 OCR 识别请求的唯一订单号: 建议为32位字符串(不超过32位)         | String                | 32                 | 是       |
| openApiAppId  | 业务流程唯一标识，即 WBappid，可参考 [获取 WBappid](https://cloud.tencent.com/document/product/1007/49634) 指引在人脸核身控制台内申请| String | 8 | 必填 |
| openApiAppVersion | 接口版本号，默认填1.0.0                  | String                | 20                 | 是       |
| openApiNonce      | 与服务端生成签名的随机数保持一致   | String            | 32           | 是       |
| openApiUserId     | User Id，每个用户唯一的标识                | String                | 30                 | 是       |
| openApiSign       | 合作方后台服务器通过 ticket 计算出来的签名信息   | String      | 40                 | 是       |


### 个性化参数设置
`WbCloudOcrSdk.init()`里的`Bundle data`，除了必须要传的 InputData 对象之外，还可以由合作方为其传入一些个性化参数，量身打造更契合自己 App 的 SDK。如果合作方未设置这些参数，则以下所有参数按默认值设置。

#### 设置 SDK 的扫描识别的时间上限
合作方可以设置 SDK 的扫描识别时间的上限。 SDK 打开照相机进行扫描识别的时间上限默认是20秒，20秒内若识别成功则退出扫描界面，否则一直识别，直到20秒后直接退出扫描界面。第三方可对其个性化设置，设置的时间上限不能超过60秒，建议第三方采用默认值，不要修改这个参数。设置代码如下：
```
# 在 MainActivity 中单击某个按钮的代码逻辑：
  //先将必填的 InputData 放入 Bundle 中
  data.putSerializable(WbCloudFaceVerifySdk.INPUT_DATA, inputData);
  //设置 SDK 扫描识别证件（身份证、银行卡）的时间上限，如果不设置则默认 20 秒；设置了则以设置为准
  //此处设置 SDK 的扫描识别时间的上限为 20 秒
   data.putLong(WbCloudOcrSDK.SCAN_TIME, 20000);
```

#### 个性化设置接入示例
```
# 在 MainActivity 中单击某个按钮的代码逻辑：
  //先将必填的 InputData 放入 Bundle 中
  data.putSerializable(WbCloudOcrSDK.INPUT_DATA, inputData);
  //设置扫描识别的时间上限,默认 20 秒，此处设置为 20 秒
  data.putLong(WbCloudOcrSDK.SCAN_TIME, 20000);
```
## OCR Android 错误码
### 终端返回错误码

|错误码|   错误码描述|
|-|-|
|IDOCR_LOGIN_PARAMETER_ERROR = -20000|传入参数有误|
|IDOCR_USER_CANCEL = 200101|用户取消操作|
|IDOCR_RECOGNISE_TIME_OUT="200102"|识别超时|
|IDOCR__ERROR_USER_NO_NET = 100101  |无网络|
|IDOCR_USER_2G = 100102 |不支持2G网络|
|IDOCR_ERROR_PERMISSION_CAMERA = 100103     |无相机权限|
|IDOCR_ERROR_PERMISSION = 100105 |  权限异常|
|IDOCR_LOGIN__ERROR = -10000    |登录错误|
|SERVER_FAIL = -30000 | 内部服务错误|
|DECODE_FAIL="300101"|解码 emg 异常(包括 emg 为空)|
 
### 后台返回错误码

|错误码|   错误码描述|
|-|-|
|INTERNAL_SERVER_ERROR = 999999 |   网络不给力，请稍后再试|
|FRONT_INTERNAL_SERVER_ERROR = 999998 |网络不给力，请稍后再试|
|SERVICE_TIME_OUT = 999997 |    网络不给力，请稍后再试|
|OAUTH_INVALID_REQUEST = 400101     |不合法请求|
|OAUTH_INVALID_LOGIN_STATUS = 400102 |  不合法请求|
|OAUTH_ACCESS_DENIED = 400103   |服务器拒绝访问此接口|
|OAUTH_INVALID_PRIVILEGE = 400104   |无权限访问此请求|
|OAUTH_REQUEST_VALIDATE_ERROR = 400105 |    身份验证不通过|
|OAUTH_TPS_EXCEED_LIMIT = 400501    |请求超过最大限制|
|OAUTH_INVALID_VERSION = 400502     |请求上送版本参数错误|
|OAUTH_INVALID_FILE_HASH = 400503   |文件校验值错误|
|OAUTH_REQUEST_RATE_LIMIT = 400504 |请求访问频率过高|


## 接入示例
```
# 在 MainActivity 中单击某个按钮的代码逻辑：
//先填好数据 
  Bundle data = new Bundle();
        WbCloudOcrSDK.InputData inputData = new WbCloudOcrSDK.InputData(
                orderNo,
                appId,
                openApiAppVersion,
                nonce,
                userId,
                sign);
        data.putSerializable(WbCloudOcrSDK.INPUT_DATA, inputData);
  //个性化参数设置,可以不设置，不设置则为默认选项。
  //设置扫描识别的时间上限,默认20秒，建议默认。用户有效设置范围（0-60000）
  data.putLong(WbCloudOcrSDK.SCAN_TIME, 20000);
//初始化 sdk，得到是否登录 sdk 成功的结果 
        WbCloudOcrSDK.getInstance().init(MainActivity.this, WbCloudOcrSDK.WBOCRTYPEMODE.WBOCRSDKTypeBankSide,data, new WbCloudOcrSDK.OcrLoginListener() {
            @Override
            public void onLoginSuccess() {  //登录成功,拉起 SDK 页面                              WbCloudOcrSDK.getInstance().startActivityForOcr(MainActivity.this,
      new  WbCloudOcrSDK.IDCardScanResultListener() {  //返退出 SDK 回调接口
                    @Override
                    public void onFinish(String resultCode, String resultMsg) {
                        // resultCode为0，则识别成功；否则识别失败
                       if ("0".equals(resultCode)) {
                            WLogger.d(TAG, "识别成功，识别银行卡的结果是:"+WbCloudOcrSDK.getInstance().getBankCardResult().toString());
                        } else {
                            WLogger.d(TAG, "识别失败"+resultCode+”--”+resultMsg);
                        }

                    }
});
}
@Override
public void onLoginFailed(String errorCode, String errorMsg) {
if(errorCode.equals(ErrorCode.IDOCR_LOGIN_PARAMETER_ERROR)) {
Toast.makeText(MainActivity.this, "传入参数有误！" + errorMsg, Toast.LENGTH_SHORT).show();
} else {
Toast.makeText(MainActivity.this, "登录 OCR sdk 失败！" + "errorCode= " + errorCode + " ;errorMsg=" + errorMsg, Toast.LENGTH_SHORT).show();
}
}
});
```

/// @param nonce       每次请求需要的一次性nonce，一次有效
/// @param userId      每个用户唯一的标识
/// @param sign        签名信息，由接入方后台提供，一次有效
/// @param orderNo     每次OCR识别请求的唯一订单号: 建议为32位字符串(不超过32位)
/// @param version     openAPI接口版本号,默认为1.0.0
/// @param license     由腾讯服务分配的,和 bundle id 关联****
/// @param succeed      SDK 登录成功
/// @param failed        SDK 登录失败
- (void)initSDKWithSDKType:(WBOCRCardType)sdkType
                     appId:(nonnull NSString *)appId
                     nonce:(nonnull NSString *)nonce
                    userId:(nonnull NSString *)userId
                      sign:(nonnull NSString *)sign
                   orderNo:(nonnull NSString *)orderNo
                   version:(nonnull NSString *)version
                   license:(nonnull NSString *)license
                   succeed:(nonnull WBOCRServiceInitSucceedBlock)succeed
                    failed:(nonnull WBOCRServiceFailedBlock)failed;
startService 接口如下, 通过 recognizeSucceed 接收识别成功回调，通过 failed 接收识别失败回调。
/// 标准版本 SDK 识别接口
/// @warning 调用这个接口前, 需要完成 SDK 登录, 即需要调用 initSDK 接口,并收到 succeed 回调
/// @param recognizeSucceed 识别成功回调
/// @param failed           识别失败回调
- (void) startOCRService:(nonnull WBOCRServiceRecognizeSuccessBlock)recognizeSucceed
                  failed:(nonnull WBOCRServiceFailedBlock)failed;
```


### 3. 接入示例
具体接入示例，请参考 demo 工程。

### 4. 识别结果处理
SDK 入口方法提供了三个回调 block ，通过这几个 block 来捕获识别结果或者异常状况。

#### 4.1 WBOCRServiceInitSucceedBlock（成功进入 SDK 回调）
进入这个回调，说明当前用户已经通过 SDK 鉴权，应用成功进入 SDK 界面了。

#### 4.2 WBOCRServiceRecognizeSuccessBlock（识别成功，即将退出 SDK 回调）
进入这个回调，说明 SDK 已经识别成功，即将退出，回到 App 中的界面，这里面有两个参数 resultModel 和 extension。
- resultModel 是对识别结果的封装，如果当前识别的是身份证，就会返回一个 WBIDCardInfoModel 类型的实例；如果当前识别的是银行卡，返回的是一个 WBBankCardInfoModel 类型的实例。关于每个字段的详细含义，请参考 WBOCRService.h 头文件。
- extension 是一个扩展字段，备用，目前版本为空，不需要处理。

#### 4.3 WBOCRServiceFailedBlock（SDK 异常，即将退出 SDK 回调）
进入这个回调，说明 SDK 发生异常，SDK 即将退出，可以通过这个回调获取失败信息，这里面有两个参数 error 和 extension。
- error 是一个 NSError 类型的实例，里面会封装错误码和错误描述，下面代码展示了一条错误码为200101的 error 信息，具体的错误码对照表请参考 [OCR iOS 错误码](https://cloud.tencent.com/document/product/1007/35856) 文档。
```
NSError *error = [NSError errorWithDomain:@"com.ocr.error" code:200101 userInfo:@{NSLocalizedDescriptionKey:@"用户取消操作"}];
```
- extension 是一个扩展字段，备用，目前版本为空，不需要处理。

## OCR iOS 错误码

|返回码 | 返回信息 | 处理措施|
|------- |--------- |----------|
|100100|传入 SDK 参数不合法|检查传入参数是否合法|
|100101 | 无网络，请确认 | 确认网络正常|
|100102 | 不支持 2G 网络 | 更换网络环境|
|100103 | 无相机权限 | -|
|200101 | 用户取消操作 | 用户主动退出操作|
|200102 | 识别超时 | 用户在身份证正反面识别过程中超过设定的阈值（20S）无法识别，提示超时|


### 多重告警码描述
在 OCR SDK 2.2.0版本，引入了多重告警码：
- 银行卡识别时，在 WBBankCardInfoModel 类的头文件中，增加了三个字段：清晰度 clarity 字段，多重警告码 multiWarningCode 和多重警告码描述 multiWarningMsg 字段。
- 身份证人像面识别时，在 WBIDCardInfoModel 类的头文件中，增加了两个字段：清晰度 frontClarity 字段，多重警告码 frontMultiWarning 字段。
- 身份证国徽面识别时，在 WBIDCardInfoModel 类的头文件中，增加了两个字段：清晰度 backClarity 字段，多重警告码 backMultiWarning 字段。

识别成功的时候，在 recognizeSucceed 的回调中，通过获取 resultModel 中的相应字段来获取多重告警码。


