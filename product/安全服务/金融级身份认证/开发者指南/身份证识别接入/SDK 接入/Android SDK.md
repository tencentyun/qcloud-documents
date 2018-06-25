## 1. 前置条件
### 1.1 相机/读取手机信息权限检测
SDK 需要用到相机/读取手机信息权限，在 Android 6.0 以上系统，SDK 对其做了权限的运行时检测。但是由于 Android 6.0 以下系统 Android 并没有运行时权限，检测权限只能靠开关相机进行。考虑到 SDK 的使用时间很短，快速频繁开关相机可能会导致手机抛出异常，故 SDK 内对 Android 6.0 以下手机没有做权限的检测。为了进一步提高用户体验，在 Android 6.0 以下系统上，我们建议合作方在拉起 SDK 前，帮助 SDK 做相机/读取手机信息权限检测，提示用户确认打开了这三项权限后再进行身份证识别，可以使整个身份证识别体验更快更好。

## 2. 接入配置
OCR SDK（WbCloudOcr）最低支持到 ** Android API 14: Android 4.0(ICS) **，请在构建项目时注意。
WbCloudOcr 将以 AAR 文件的形式提供。
需要添加下面文档中所示的依赖(将提供的 AAR 文件加入到 app 工程的 `libs` 文件夹下面,
并且在 **build.gradle** 中添加下面的配置:
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
      compile(name: 'WbCloudOcrSdk-proRelease-v1.2.4-5cf1801', ext: 'aar')
  //2.云公共组件
compile(name: 'WbCloudNormal-release-v3.0.8-f0cefef', ext: 'aar')    }
```

## 3. 混淆配置
云 OCR 产品的混淆规则分为三部分，分别是云 OCR SDK 的混淆规则，云公共组件的混淆规则及依赖的第三方库混淆规则。

### 3.1 云 OCR SDK 的混淆规则
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
您可以将如上代码拷贝到您的混淆文件中，也可以将 SDK 中的` webank-cloud-ocr-proguard-rules.pro` 拷贝到主工程根目录下,然后通过`-include webank-cloud-ocr-rules.pro` 加入到您的混淆文件中。

### 3.2 云公共组件的混淆规则

```
#######################webank normal混淆规则-BEGIN#############################
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

#webank normal 包含的第三方库 bugly
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


#######################webank normal混淆规则-END#############################
```
您可以将如上代码拷贝到您的混淆文件中，也可以将 SDK 中的 `webank-cloud-normal-proguard-rules.pro` 拷贝到主工程根目录下，然后通过 `-include webank-cloud-normal-rules.pro` 加入到您的混淆文件中。

### 3.3 云 OCR 依赖的第三方库的混淆规则
```
云 OCR 依赖的第三方库的混淆规则全部内容变更为：
######################云OCR依赖的第三方库 混淆规则-BEGIN###########################
 
## support:appcompat-v7
-keep public class android.support.v7.widget.** { *; }
-keep public class android.support.v7.internal.widget.** { *; }
-keep public class android.support.v7.internal.view.menu.** { *; }
 
-keep public class * extends android.support.v4.view.ActionProvider {
	public <init>(android.content.Context);
}
##########################云OCR依赖的第三方库 混淆规则-END##############################


```
您可以根据您现有的混淆规则，将缺少的第三库混淆规则拷贝到您的混淆文件中。

### 3.4 调用 SDK 接口
SDK 代码调用的入口为
**com.webank.mbank.ocr.WbCloudOcrSDK** 这个类。
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
     * 登录成功后，调用此函数拉起SDK页面
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
```

WbCloudOcrSdk.init() 的第二个参数用来传递数据.可以将参数打包到 data(Bundle) 中，必须传递的参数包括，参加要求见下一章节描述：
```
//这些都是WbCloudOcrSdk.InputData对象里的字段，是需要传入的数据信息
String orderNo;  //订单号
String openApiAppId;  //APP_ID 
String openApiAppVersion;  //openapi  Version
String openApiNonce; //32位随机字符串
String openApiUserId; //user id
String openApiSign; //签名信息
```
以上参数被封装在 WbCloudOcrSdk.InputData 对象中（他是一个 Serializable 对象）。
EXIDCardResult 代表 SDK 返回的识别身份证的结果，该类属性如下所示：
```
public int type;//拉起 SDK 的模式所对应的int 值，也就是 startActivityForOcr 方法中 WBOCRTYPEMODE type 的枚举值 value
	// 识别人像面返回的信息
    public String cardNum;  //身份证号码
	public String name;//姓名
	public String sex;//性别
	public String address;//住址
	public String nation;//民族
	public String birth;//出生年月日
	public String frontFullImageSrc;// 人像面图片存放路径

    //识别国徽面返回的信息
    public String office;//签发机关
	public String validDate;//有效期限
	public String backFullImageSrc;//国徽面图片存放路径
//每次网络请求都会返回的信息
public String sign;//签名
public  String orderNo; //订单号
public String ocrId;//识别的唯一标识
public String warning;//识别的警告码
```

## 4. 登录接口
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

### 4.1 返回第三方接口
```
/**
  * 退出 SDK,返回第三方的回调,同时返回 ocr 识别结果
  */
public interface IDCardScanResultListener{
        /**
         * 退出 SDK,返回第三方的回调,同时返回 ocr 识别结果
         * @param errorCode        返回错误码，识别成功返回 0
         * @param errorMsg        返回错误信息，和错误码相关联         */
        void onFinish(String errorCode, String errorMsg);
}
```

### 4.2 第三方进入 SDK 的模式
 第三方调用 startActivityForOcr 方法进入 SDK 时，WBOCRTYPEMODE type 参数表示进入 SDK 的模式类型。总共有三种模式，当 type==WBOCRSDKTypeNormal，进入标准模式(进入扫描身份证界面前有个准备界面)；当 type==WBOCRSDKTypeFrontSide 时，直接进入扫描身份证人像面界面，进行人像面识别；当 type==WBOCRSDKTypeBackSide 时，直接进入扫描身份证国徽面界面，进行国徽面识别。
​		
## 5. 接口参数说明

| 参数                | 说明                          | 类型     | 长度     | 是否必填                |
| ----------------- | --------------------------- | ------ | ------ | ------------------- |
| orderNo           | 订单号                         | String | 32     | 必填，合作方订单的唯一标识       |
| openApiAppId      | 腾讯服务分配的 app_id              | String | 腾讯服务分配 | 必填，腾讯服务分配的 app_id   |
| openApiAppVersion | 接口版本号                       | String | 20     | 必填，默认填 1.0.0        |
| openApiNonce      | 32 位随机字符串                   | String | 32     | 必填，每次请求需要的一次性 nonce |
| openApiUserId     | User Id                     | String | 30     | 必填，每个用户唯一的标识        |
| openApiSign       | 合作方后台服务器通过 ticket 计算出来的签名信息 | String | 40     | 必填                  |

## 6. 个性化参数设置
WbCloudOcrSdk.init() 里 Bundle data，除了必须要传的 InputData 对象（详情见上节）之外，还可以由合作方方传入一些个性化参数，量身打造更契合自己 App 的 SDK。如果合作方未设置这些参数，则以下所有参数按默认值设置。

### 6.1 设置 SDK 的界面标题栏背景色
合作方可以设置进入 SDK 的准备界面的标题栏背景色（仅对标准模式此设置才有效）。 SDK 默认显示准备界面的标题栏背景颜色是白色 (#ffffff)，但第三方可对其个性化设置。设置代码如下：

```
# 在 MainActivity 中点击某个按钮的代码逻辑：
  //先将必填的 InputData 放入 Bundle 中
  data.putSerializable(WbCloudFaceVerifySdk.INPUT_DATA, inputData);
  //设置标题栏背景色，如果不设置则默认展示；设置了则以设置为准
  //此处设置进入 SDK 的第一个界面的标题栏背景色为蓝色(#409eff)
  data.putString(WbCloudOcrSDK.TITLE_BAR_COLOR, "#409eff");
```

### 6.2 设置 SDK 的界面标题栏内容
合作方可以设置进入 SDK 的准备界面的标题栏文字内容（仅对标准模式此设置才有效）。SDK 默认显示第一个界面的标题栏文字内容是身份证识别，但第三方可对其个性化设置。设置代码如下：

```
# 在 MainActivity 中点击某个按钮的代码逻辑：
  //先将必填的 InputData放入 Bundle 中
  data.putSerializable(WbCloudFaceVerifySdk.INPUT_DATA, inputData);
  //设置标题栏文字内容，如果不设置则默认展示；设置了则以设置为准
  //此处设置进入 SDK 的第一个界面的标题栏文字内容为居民身份证识别
   data.putString(WbCloudOcrSDK.TITLE_BAR_CONTENT, "居民身份证识别");
```

### 6.3 设置 SDK 的水印文字内容
合作方可以设置进入 SDK 的第一个界面上的水印文字内容。 SDK 默认显示第一个界面的水印文字内容是仅供内部业务使用，但第三方可对其个性化设置。设置时需要注意：水印文字长度不超过 8，且只支持汉字，若长度超过 8，SDK 会自动截取前 8 个汉字。设置代码如下：

```
# 在MainActivity 中点击某个按钮的代码逻辑：
  //先将必填的 InputData 放 入Bundle 中
  data.putSerializable(WbCloudFaceVerifySdk.INPUT_DATA, inputData);
  //设置水印文字内容，如果不设置则默认展示；设置了则以设置为准
  //此处设置进入 SDK 的第一个界面的水印文字内容为仅供本次业务使用      data.putString(WbCloudOcrSDK.WATER_MASK_TEXT, "仅供本次业务使用");
```

### 6.4 设置 SDK 的扫描识别的时间上限
合作方可以设置 SDK 的扫描识别时间的上限。 SDK 打开照相机进行扫描识别的时间上限默认是 20 秒，20 秒内若扫描识别成功则返回到 SDK 的第一个界面，否则直到 20 秒直接退出扫描界面。第三方可对其个性化设置，设置的时间上限不能超过 60 秒，建议第三方采用默认值，不要修改这个参数。设置代码如下：
```
# 在 MainActivity 中点击某个按钮的代码逻辑：
  //先将必填的 InputData 放入 Bundle 中
  data.putSerializable(WbCloudFaceVerifySdk.INPUT_DATA, inputData);
  //设置 SDK 扫描识别身份证的时间上限，如果不设置则默认 20 秒；设置了则以设置为准
  //此处设置 SDK 的扫描识别时间的上限为 20 秒
   data.putLong(WbCloudOcrSDK.SCAN_TIME, 20000);
```

### 6.5 接入示例
```
# 在 MainActivity 中点击某个按钮的代码逻辑：
  //先将必填的 InputData 放入 Bundle 中
  data.putSerializable(WbCloudOcrSDK.INPUT_DATA, inputData);
  //个性化参数设置,此处均设置为与默认不同
  //设置 SDK 标题栏背景颜色，默认白色，此处设置为蓝色（仅对标准模式有效）  data.putString(WbCloudOcrSDK.TITLE_BAR_COLOR, "#409eff");
  //设置 SDK 标题栏文字内容，默认展示身份证识别,此处设置为居民身份证识别（仅对标准模式有效）   
data.putString(WbCloudOcrSDK.TITLE_BAR_CONTENT, "居民身份证识别");
  //设置 SDK 水印文字内容，默认仅供内部业务使用，此处设置为仅供本次业务使用（仅对标准模式有效）
  data.putString(WbCloudOcrSDK.WATER_MASK_TEXT, "仅供本次业务使用");
  //设置扫描识别的时间上限,默认 20 秒，此处设置为 20 秒
  data.putLong(WbCloudOcrSDK.SCAN_TIME, 20000);

```

## 7. 整体接入示例
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
  //此处均设置为和默认设置不同
  data.putString(WbCloudOcrSDK.TITLE_BAR_COLOR, "#409eff");
  //设置 SDK 标题栏文字内容，默认展示身份证识别,此处设置为居民身份证识别data.putString(WbCloudOcrSDK.TITLE_BAR_CONTENT, "居民身份证识别");
  //设置 SDK 水印文字内容，默认仅供内部业务使用，此处设置为仅供本次业务使用
  data.putString(WbCloudOcrSDK.WATER_MASK_TEXT, "仅供本次业务使用");
  //设置扫描识别的时间上限,默认 20 秒，建议默认
  data.putLong(WbCloudOcrSDK.SCAN_TIME, 20000);
//初始化 SDK，得到是否登录 SDK 成功的结果 
        WbCloudOcrSDK.getInstance().init(MainActivity.this, data, new WbCloudOcrSDK.OcrLoginListener() {
            @Override
            public void onLoginSuccess() {  //登录成功,拉起 SDL 页面                              WbCloudOcrSDK.getInstance().startActivityForOcr(MainActivity.this,
      new  WbCloudOcrSDK.IDCardScanResultListener() {  //返退出 SDK 回调接口
                    @Override
                    public void onFinish(String resultCode, String resultMsg) {
           // resultCode为0，则识别成功；否则识别失败
               if ("0".equals(resultCode)) {
                            //  TODO:2017/10/30
               WLogger.d(TAG, "识别成功,识别身份证的结果是:"+WbCloudOcrSDK.getInstance().getResultReturn().toString());
               }else{  //  TODO:2017/10/30
               WLogger.d(TAG, "识别失败:"+resultCode+”--”+resultMsg);
               }
            }
},WbCloudOcrSDK.WBOCRTYPEMODE.WBOCRSDKTypeNormal);
}              
@Override
public void onLoginFailed(String errorCode, String errorMsg) {
if(errorCode.equals(ErrorCode.IDOCR_LOGIN_PARAMETER_ERROR)) {
Toast.makeText(MainActivity.this, "传入参数有误！" + errorMsg, Toast.LENGTH_SHORT).show();
} else {
Toast.makeText(MainActivity.this, "登录 OCR SDK 失败！" + "errorCode= " + errorCode + " ;errorMsg=" + errorMsg, Toast.LENGTH_SHORT).show();
}
}
})
```

## 8. 错误码描述
### 8.1 终端返回错误码

| 错误码                                      | 错误描述           |
| ---------------------------------------- | -------------- |
| IDOCR_LOGIN_PARAMETER_ERROR = "-20000";  | 传入参数有误         |
| IDOCR_USER_CANCEL="200101";              | 用户取消操作         |
| IDOCR__ERROR_USER_NO_NET="100101";       | 无网络            |
| IDOCR_USER_2G="100102";                  | 不支持 2G 网络      |
| IDOCR_ERROR_PERMISSION_CAMERA="100103";  | 无相机权限          |
| IDOCR_ERROR_PERMISSION_READ_PHONE="100103"; | READ PHONE 未权限 |
| IDOCR_ERROR_PERMISSION="100103";         | 权限异常           |
| IDOCR_LOGIN__ERROR="-10000";             | 登录错误           |
| SERVER_FAIL="-30000";                    | 内部服务错误         |



### 8.2 后台返回错误码

| 错误码                                   | 错误描述        |
| ------------------------------------- | ----------- |
| INTERNAL_SERVER_ERROR="999999"        | 网络不给力，请稍后再试 |
| FRONT_INTERNAL_SERVER_ERROR="999998"  | 网络不给力，请稍后再试 |
| SERVICE_TIME_OUT="999997"             | 网络不给力，请稍后再试 |
| OAUTH_INVALID_REQUEST="400101"        | 不合法请求       |
| OAUTH_INVALID_LOGIN_STATUS="400102"   | 不合法请求       |
| OAUTH_ACCESS_DENIED="400103"          | 服务器拒绝访问此接口  |
| OAUTH_INVALID_PRIVILEGE="400104"      | 无权限访问此请求    |
| OAUTH_REQUEST_VALIDATE_ERROR="400105" | 身份验证不通过     |
| OAUTH_TPS_EXCEED_LIMIT="400501"       | 请求超过最大限制    |
| OAUTH_INVALID_VERSION="400502"        | 请求上送版本参数错误  |
| OAUTH_INVALID_FILE_HASH="400503"      | 文件校验值错误     |
| OAUTH_REQUEST_RATE_LIMIT="400504"     | 请求访问频率过高    |

上一步：[SDK 启动](https://cloud.tencent.com/document/product/655/13846)