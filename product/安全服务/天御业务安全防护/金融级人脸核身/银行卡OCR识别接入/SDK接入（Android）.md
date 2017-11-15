### 1.前置条件
** 1.1 相机/读取手机信息权限检测 **
- SDK 需要用到相机权限/读取手机信息权限。
- Android6.0 及以上系统  
SDK 运行时提示权限，需要用户授权。
- Android 6.0 以下系统
Android 并没有运行时权限，检测权限只能靠开关相机进行。考虑到 SDK 的使用时间很短，快速频繁开关相机可能会导致手机抛出异常，故 SDK 内对 Android 6.0 以下手机没有做权限的检测。为了进一步提高用户体验，在 Android6.0 以下系统上，我们建议合作方在拉起 SDK 前，帮助 SDK 做相机/读取手机信息权限检测，提示用户确认打开了这项权限后再进行银行卡识别，可以使整个银行卡识别体验更快更好。
 
 
### 2.接入配置
OCR SDK（WbCloudOcr）最低支持到  ** Android API 14: Android 4.0(ICS) **，请在构建项目时注意。
`WbCloudOcr` 将以 AAR 文件的形式提供。
需要添加下面文档中所示的依赖（将提供的 aar 文件加入到 app 工程的 `'libs'` 文件夹下面），
并且在 **build.gradle** 中添加下面的配置：

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
 compile(name: 'WbCloudOcrSdk-proRelease-v1.2.4-5cf1801
', ext: 'aar')
  //2.云公共组件
compile(name: 'WbCloudNormal-release-v3.0.8-f0cefef', ext: 'aar')    }
```


### 3.混淆配置
 云 OCR 产品的混淆规则分为三部分，分别是云 OCR SDK 的混淆规则，云公共组件的混淆规则及依赖的第三方库混淆规则。
#### 3.1 云 OCR SDK 的混淆规则
```
######################云 ocr 混淆规则 ocr-BEGIN###########################
-keepattributes InnerClasses
-keep public class com.webank.mbank.ocr.WbCloudOcrSDK{
    public <methods>;
    public static final *;
}
-keep public class com.webank.mbank.ocr.WbCloudOcrSDK$*{
    *;
}

-keep public class com.webank.mbank.ocr.tools.ErrorCode{
    *;
}

-keep public class com.webank.mbank.ocr.net.*$*{
    *;
}
-keep public class com.webank.mbank.ocr.net.*{
    *;
}
#######################云 ocr 混淆规则 ocr-END#############################
```

您可以将如上代码拷贝到您的混淆文件中，也可以将 SDK 中的 `webank-cloud-ocr-proguard-rules.pro `拷贝到主工程根目录下,然后通过`"-include webank-cloud-ocr-rules.pro"` 加入到您的混淆文件中。
#### 3.2 云公共组件的混淆规则

```
#######################webank normal 混淆规则 -BEGIN#############################
#不混淆内部类
-keepattributes InnerClasses
-keepattributes *Annotation*
-keepattributes Signature

-keep, allowobfuscation @interface com.webank.normal.xview.Inflater
-keep, allowobfuscation @interface com.webank.normal.xview.Find
-keep, allowobfuscation @interface com.webank.normal.xview.BindClick

-keep @com.webank.normal.xview.Inflater class *
-keepclassmembers class * {
    @com.webank.normal.Find *;
    @com.webank.normal.BindClick *;
}

-keep public class com.webank.normal.net.*$*{
    *;
}
-keep public class com.webank.normal.net.*{
    *;
}
-keep public class com.webank.normal.thread.*{
   *;
}
-keep public class com.webank.normal.thread.*$*{
   *;
}
-keep public class com.webank.normal.tools.WLogger{
    *;
}

#webank normal包含的第三方库 bugly
-keep class com.tencent.bugly.webank.**{
    *;
}

#wehttp 混淆规则
-dontwarn com.webank.mbank.okio.**

-keep class com.webank.mbank.wehttp.**{
    public <methods>;
}
-keep interface com.webank.mbank.wehttp.**{
    public <methods>;
}
-keep public class com.webank.mbank.wehttp.WeLog$Level{
    *;
}
-keep class com.webank.mbank.wejson.WeJson{
    public <methods>;
}


#######################webank normal 混淆规则 -END#############################
```

您可以将如上代码拷贝到您的混淆文件中，也可以将 SDK 中的` webank-cloud-normal-proguard-rules.pro `拷贝到主工程根目录下,然后通过`"-include webank-cloud-normal-rules.pro" `加入到您的混淆文件中。

#### 3.3 云 OCR 依赖的第三方库的混淆规则

```
######################云 OCR 依赖的第三方库 混淆规则 -BEGIN###########################

## support:appcompat-v7
-keep public class android.support.v7.widget.** { *; }
-keep public class android.support.v7.internal.widget.** { *; }
-keep public class android.support.v7.internal.view.menu.** { *; }

-keep public class * extends android.support.v4.view.ActionProvider {
    public <init>(android.content.Context);
}
##########################云 OCR 依赖的第三方库 混淆规则 -END##############################
```
您可以根据您现有的混淆规则，将缺少的第三库混淆规则拷贝到您的混淆文件中。

### 4. 调用 SDK 接口
SDK 代码调用的入口为
`com.webank.mbank.ocr.WbCloudOcrSDK`这个类。

```
public class WbCloudOcrSDK{

/**
* 该类为一个单例，需要先获得单例对象再进行后续操作
   */
       public static synchronized WbCloudOcrSDK getInstance() {
       //	...
       }

/**
* 在使用 SDK 前先初始化，传入需要的数据 data，由 OcrLoginListener 返回是否登录 SDK 成功
* 关于传入数据 data 见后面的说明
*/
public void init(Context context,Bundle data,OcrLoginListener loginListerner){
//	...
}
   /**
     * 登录成功后，调用此函数拉起 sdk 页面
     * @param context                  拉起 SDK 的上下文
     * @param idCardScanResultListener 返回到第三方的接口
     * @param type                     进入 SDK 的模式，参数是枚举类型
     */
    public void startActivityForOcr(Context context,IDCardScanResultListener,WBOCRTYPEMODE type){
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

`WbCloudOcrSdk.init() `的第二个参数用来传递数据。可以将参数打包到 `data(Bundle) `中，必须传递的参数包括（见 5. 接口参数说明）

```
//这些都是 WbCloudOcrSdk.InputData 对象里的字段，是需要传入的数据信息
String orderNo;  //订单号
String openApiAppId;  //APP_ID 
String openApiAppVersion;  //openapi  Version
String openApiNonce; //32 位随机字符串
String openApiUserId; //user id
String openApiSign; //签名信息
```

以上参数被封装在 WbCloudOcrSdk.InputData 对象中（他是一个 Serializable 对象）。

EXBankCardResult 代表 SDK 返回的识别银行卡的结果，该类属性如下所示：

```
public String ocrId;//识别的唯一标识
public String bankcardNo;//识别的银行卡号
public String bankcardValidDate;//识别的银行卡的有效期
public String orderNo;//订单号
public String warningMsg;   //识别的警告信息
public String warningCode;  //识别的警告码
public Bitmap bankcardNoPhoto;//识别的银行卡的卡号图片
```

#### 4.1 登录接口

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

#### 4.2 返回第三方接口

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

#### 4.3 第三方进入 SDK 的模式
当 type==WBOCRSDKTypeBankSide 时，直接进入扫描银行卡界面，进行银行卡识别。

### 5. 接口参数说明
| 参数 | 说明 |类型 |长度 | 是否必填 |
|---------|---------|---------|---------|---------|
|orderNo	|订单号|	String|	32	|必填，合作方订单的唯一标识|
|openApiAppId|	腾讯服务分配的 app_id	|String|	腾讯服务分配	|必填，腾讯服务分配的 app_id|
|openApiAppVersion	|接口版本号	|String|	20|	必填，默认填 1.0.0|
|openApiNonce|	32 位随机字符串	|String|	32|	必填，每次请求需要的一次性 nonce|
|openApiUserId	|User Id	|String	|30|	必填，每个用户唯一的标识|
|openApiSign	|合作方后台服务器通过 ticket 计算出来的签名信息	|String	|40	|必填|

### 6. 个性化参数设置
`WbCloudOcrSdk.init()`里 Bundle data，除了必须要传的 InputData 对象（详情见 5. 接口参数说明）之外，还可以由合作方方传入一些个性化参数，量身打造更契合自己 app 的 sdk。如果合作方未设置这些参数，则以下所有参数按默认值设置。
#### 6.1 设置 sdk 的扫描识别的时间上限
合作方可以设置 sdk 的扫描识别时间的上限。 SDK 打开照相机进行扫描识别的时间上限默认是 20 秒，20 秒内若识别成功则退出扫描界面，否则一直识别，直到 20 秒后直接退出扫描界面。第三方可对其个性化设置，设置的时间上限不能超过 60 秒，建议第三方采用默认值，不要修改这个参数。设置代码如下：

```
# 在 MainActivity 中点击某个按钮的代码逻辑：
  //先将必填的 InputData 放入 Bundle 中
  data.putSerializable(WbCloudFaceVerifySdk.INPUT_DATA, inputData);
  //设置 SDK 扫描识别证件（身份证、银行卡）的时间上限，如果不设置则默认 20 秒；设置了则以设置为准
  //此处设置 SDK 的扫描识别时间的上限为 20 秒
   data.putLong(WbCloudOcrSDK.SCAN_TIME, 20000);
```
 
#### 6.2 接入示例

```
# 在 MainActivity 中点击某个按钮的代码逻辑：
  //先将必填的 InputData 放入 Bundle 中
  data.putSerializable(WbCloudOcrSDK.INPUT_DATA, inputData);
  //设置扫描识别的时间上限,默认 20 秒，此处设置为 20 秒
  data.putLong(WbCloudOcrSDK.SCAN_TIME, 20000);
```


### 7. 接入示例

```
# 在 MainActivity 中点击某个按钮的代码逻辑：
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
  //设置扫描识别的时间上限,默认 20 秒，建议默认
  data.putLong(WbCloudOcrSDK.SCAN_TIME, 20000);
//初始化 sdk，得到是否登录 sdk 成功的结果 
        WbCloudOcrSDK.getInstance().init(MainActivity.this, data, new WbCloudOcrSDK.OcrLoginListener() {
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
},WbCloudOcrSDK.WBOCRTYPEMODE.WBOCRSDKTypeBackSide);
}
@Override
public void onLoginFailed(String errorCode, String errorMsg) {
if(errorCode.equals(ErrorCode.IDOCR_LOGIN_PARAMETER_ERROR)) {
Toast.makeText(MainActivity.this, "传入参数有误！" + errorMsg, Toast.LENGTH_SHORT).show();
} else {
Toast.makeText(MainActivity.this, "登录OCR sdk失败！" + "errorCode= " + errorCode + " ;errorMsg=" + errorMsg, Toast.LENGTH_SHORT).show();
}
}
});

```

### 8. 错误码描述
#### 8.1 终端返回错误码

```
IDOCR_LOGIN_PARAMETER_ERROR = "-20000";     //传入参数有误
IDOCR_USER_CANCEL="200101";    //用户取消操作
IDOCR__ERROR_USER_NO_NET="100101";    //无网络
IDOCR_USER_2G="100102";   //不支持2G网络
IDOCR_ERROR_PERMISSION_CAMERA="100103";  //无相机权限
IDOCR_ERROR_PERMISSION_READ_PHONE="100103";  //READ PHONE未权限
IDOCR_ERROR_PERMISSION="100103";  //权限异常 IDOCR_LOGIN__ERROR="-10000";  //登录错误
SERVER_FAIL="-30000";    //内部服务错误
```
    
#### 8.2 后台返回错误码

```
INTERNAL_SERVER_ERROR="999999"      //网络不给力,请稍后再试
FRONT_INTERNAL_SERVER_ERROR="999998"  //网络不给力，请您稍后再试
SERVICE_TIME_OUT="999997"            //网络不给力，请您稍后再试
OAUTH_INVALID_REQUEST="400101"     //不合法请求
OAUTH_INVALID_LOGIN_STATUS="400102"    //不合法请求 
OAUTH_ACCESS_DENIED="400103"    //服务器拒绝访问此接口
OAUTH_INVALID_PRIVILEGE="400104"    //无权限访问此请求
OAUTH_REQUEST_VALIDATE_ERROR="400105"  //身份验证不通过
OAUTH_TPS_EXCEED_LIMIT="400501"   //请求超过最大限制
OAUTH_INVALID_VERSION="400502"    //请求上送版本参数错误
OAUTH_INVALID_FILE_HASH="400503"   //文件校验值错误
OAUTH_REQUEST_RATE_LIMIT="400504"   //请求访问频率过高
```
