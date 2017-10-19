### 1. 前置条件
**相机/读取手机信息权限检测**
SDK需要用到相机权限/读取手机信息权限。
1)Android6.0及以上系统
SDK运行时提示权限，需要用户授权。
2)Android 6.0以下系统
Android并没有运行时权限，检测权限只能靠开关相机进行。考虑到SDK的使用时间很短，快速频繁开关相机可能会导致手机抛出异常，故SDK内对Android 6.0以下手机没有做权限的检测。为了进一步提高用户体验，在Android6.0以下系统上，我们建议合作方在拉起SDK前，帮助SDK做相机/读取手机信息权限检测，提示用户确认打开了这项权限后再进行身份证识别，可以使整个身份证识别体验更快更好。
 
### 2. 接入配置
OCR SDK（WbCloudOcr）最低支持到** Android API 14: Android 4.0(ICS)**，请在构建项目时注意。
WbCloudOcr将以AAR文件的形式提供。
需要添加下面文档中所示的依赖(将提供的aar文件加入到app工程的'libs'文件夹下面,
并且在**build.gradle**中添加下面的配置:
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
 compile(name: 'WbCloudOcrSdk-proRelease-v0.1.0-8319e1a', ext: 'aar')
  //2.云公共组件
compile(name: 'WbCloudNormal-release-v3.0.1-917d1de', ext: 'aar')
```

### 3. 混淆配置
云OCR产品的混淆规则分为三部分，分别是云OCR SDK的混淆规则，云公共组件的混淆规则及依赖的第三方库混淆规则。
**1. 云OCR SDK的混淆规则**
```
######################云ocr混淆规则 ocr-BEGIN###########################
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
#######################云ocr混淆规则 ocr-END#############################
```
**2**.您可以将如上代码拷贝到您的混淆文件中，也可以将SDK中的webank-cloud-ocr-proguard-rules.pro拷贝到主工程根目录下,然后通过"-include webank-cloud-ocr-rules.pro" 加入到您的混淆文件中。
**3. 云公共组件的混淆规则**
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

#webank normal包含的第三方库bugly
-keep class com.tencent.bugly.webank.**{
    *;
}

#wehttp混淆规则
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
您可以将如上代码拷贝到您的混淆文件中，也可以将SDK中的webank-cloud-normal-proguard-rules.pro拷贝到主工程根目录下,然后通过"-include webank-cloud-normal-rules.pro" 加入到您的混淆文件中。

**4. 云OCR依赖的第三方库的混淆规则**
```
云OCR依赖的第三方库的混淆规则全部内容变更为：
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

### 4. 调用SDK接口
SDK代码调用的入口为
**com.webank.mbank.ocr.WbCloudOcrSDK**这个类。
```
public class WbCloudOcrSDK{

/**
* 该类为一个单例，需要先获得单例对象再进行后续操作
   */
       public static synchronized WbCloudOcrSDK getInstance() {
       //	...
       }

/**
* 在使用SDK前先初始化，传入需要的数据data，由 OcrLoginListener返回是否登录SDK成功
* 关于传入数据data见后面的说明
*/
public void init(Context context,Bundle data,OcrLoginListener loginListerner){
//	...
}
   /**
     * 登录成功后，调用此函数拉起sdk页面
     * @param context                  拉起SDK的上下文
     * @param idCardScanResultListener 返回到第三方的接口
     * @param type                     进入SDK的模式，参数是枚举类型
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
  * 退出SDK,返回第三方的回调,同时返回ocr识别结果
  */
public interface IDCardScanResultListener{
        /**
         * @RARAM exidCardResult   SDK返回的识别结果对象       
         */
        void onFinish(EXIDCardResult exidCardResult, 
                  String errorCode, String errorMsg);
}
```

WbCloudOcrSdk.init()的第二个参数用来传递数据.可以将参数打包到data(Bundle)中，必须传递的参数包括，参加要求见下一章节描述：
```
//这些都是WbCloudOcrSdk.InputData对象里的字段，是需要传入的数据信息
String orderNo;  //订单号
String openApiAppId;  //APP_ID 
String openApiAppVersion;  //openapi  Version
String openApiNonce; //32位随机字符串
String openApiUserId; //user id
String openApiSign; //签名信息
```
以上参数被封装在WbCloudOcrSdk.InputData对象中（他是一个Serializable对象）。
EXIDCardResult 代表SDK返回的识别结果，该类属性如下所示：
```
public int type;//拉起SDK的模式所对应的int 值，也就是startActivityForOcr 方法中WBOCRTYPEMODE type的枚举值value
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
  * 退出SDK,返回第三方的回调,同时返回ocr识别结果
  */
public interface IDCardScanResultListener{
        /**
         * 退出SDK,返回第三方的回调,同时返回ocr识别结果
         * @param exidCardResult   SDK 识别的结果对象
         * @param errorCode        返回码，识别成功返回 0
         * @param errorMsg         返回信息
         */
        void onFinish(EXIDCardResult exidCardResult, 
                  String errorCode, String errorMsg);
}
```

#### 4.3 第三方进入SDK的模式
 第三方调用startActivityForOcr方法进入SDK时，WBOCRTYPEMODE type参数表示进入SDK的模式类型。总共有三种模式，当type==WBOCRSDKTypeNormal，进入标准模式(进入扫描身份证界面前有个准备界面）;当type==WBOCRSDKTypeFrontSide时，直接进入扫描身份证人像面界面，进行人像面识别;当type==WBOCRSDKTypeBackSide时，直接进入扫描身份证国徽面界面，进行国徽面识别。
		
### 5.接口参数说明

| 标题1 | 标题2 | 标题3 |标题3 |标题3 |
|---------|---------|---------|---------|---------|
| orderNo | 订单号 | String |32 |必输，合作方订单的唯一标识 |
| openApiAppId | 腾讯服务分配的app_id | String |腾讯服务分配 |必输，腾讯服务分配的app_id |
| openApiAppVersion | 接口版本号 | String |20 |必输，默认填1.0.0 |
| openApiNonce | 32位随机字符串 | String |32 |必输，每次请求需要的一次性nonce |
| openApiUserId | User Id | String |30 |必输，每个用户唯一的标识 |
| openApiSign | 合作方后台服务器通过ticket计算出来的签名信息 | String |40 |必输 |

### 6. 个性化参数设置
WbCloudOcrSdk.init()里Bundle data，除了必须要传的InputData对象(详情见上节)之外，还可以由合作方方传入一些个性化参数，量身打造更契合自己app的sdk。如果合作方未设置这些参数，则以下所有参数按默认值设置。

#### 6.1 设置sdk的界面标题栏背景色
合作方可以设置进入sdk的第一个界面的标题栏背景色。 SDK默认显示第一个界面的标题栏背景颜色是白色(#ffffff)，但第三方可对其个性化设置。设置代码如下：
 ```
# 在MainActivity中点击某个按钮的代码逻辑：
  //先将必填的InputData放入Bundle中
  data.putSerializable(WbCloudFaceVerifySdk.INPUT_DATA, inputData);
  //设置标题栏背景色，如果不设置则默认展示；设置了则以设置为准
  //此处设置进入SDK的第一个界面的标题栏背景色为蓝色(#409eff)
  data.putString(WbCloudOcrSDK.TITLE_BAR_COLOR, "#409eff");
```

#### 6.2 设置sdk的界面标题栏内容
合作方可以设置进入sdk的第一个界面的标题栏文字内容。 SDK默认显示第一个界面的标题栏文字内容是身份证识别，但第三方可对其个性化设置。设置代码如下：
 ```
# 在MainActivity中点击某个按钮的代码逻辑：
  //先将必填的InputData放入Bundle中
  data.putSerializable(WbCloudFaceVerifySdk.INPUT_DATA, inputData);
  //设置标题栏文字内容，如果不设置则默认展示；设置了则以设置为准
  //此处设置进入SDK的第一个界面的标题栏文字内容为居民身份证识别
   data.putString(WbCloudOcrSDK.TITLE_BAR_CONTENT, "居民身份证识别");
```

#### 6.3 设置sdk的水印文字内容
合作方可以设置进入sdk的第一个界面上的水印文字内容。 SDK默认显示第一个界面的水印文字内容是仅供内部业务使用，但第三方可对其个性化设置。设置时需要注意：水印文字长度不超过8，且只支持汉字，若长度超过8，SDK会自动截取前8个汉字。设置代码如下：
 ```
# 在MainActivity中点击某个按钮的代码逻辑：
  //先将必填的InputData放入Bundle中
  data.putSerializable(WbCloudFaceVerifySdk.INPUT_DATA, inputData);
  //设置水印文字内容，如果不设置则默认展示；设置了则以设置为准
  //此处设置进入SDK的第一个界面的水印文字内容为仅供本次业务使用      data.putString(WbCloudOcrSDK.WATER_MASK_TEXT, "仅供本次业务使用");
```

#### 6.4 设置sdk的扫描识别的时间上限
合作方可以设置sdk的扫描识别时间的上限。 SDK打开照相机进行扫描识别的时间上限默认是20秒，20秒内若扫描识别成功则返回到SDK的第一个界面，否则直到20秒直接退出扫描界面。第三方可对其个性化设置，设置的时间上限不能超过60秒，建议第三方采用默认值，不要修改这个参数。设置代码如下：
 ```
# 在MainActivity中点击某个按钮的代码逻辑：
  //先将必填的InputData放入Bundle中
  data.putSerializable(WbCloudFaceVerifySdk.INPUT_DATA, inputData);
  //设置SDK扫描识别身份证的时间上限，如果不设置则默认20秒；设置了则以设置为准
  //此处设置SDK的扫描识别时间的上限为20秒
   data.putLong(WbCloudOcrSDK.SCAN_TIME, 20000);
```
  
#### 6.5 接入示例
```
# 在MainActivity中点击某个按钮的代码逻辑：
  //先将必填的InputData放入Bundle中
  data.putSerializable(WbCloudOcrSDK.INPUT_DATA, inputData);
  //个性化参数设置,此处均设置为与默认不同
  //设置sdk标题栏背景颜色，默认白色，此处设置为蓝色  data.putString(WbCloudOcrSDK.TITLE_BAR_COLOR, "#409eff");
  //设置sdk标题栏文字内容，默认展示身份证识别,此处设置为居民身份证识别   data.putString(WbCloudOcrSDK.TITLE_BAR_CONTENT, "居民身份证识别");
  //设置sdk水印文字内容，默认仅供内部业务使用，此处设置为仅供本次业务使用
  data.putString(WbCloudOcrSDK.WATER_MASK_TEXT, "仅供本次业务使用");
  //设置扫描识别的时间上限,默认20秒，此处设置为20秒
  data.putLong(WbCloudOcrSDK.SCAN_TIME, 20000);
```

### 7. 接入示例
```
# 在MainActivity中点击某个按钮的代码逻辑：
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
  //设置sdk标题栏文字内容，默认展示身份证识别,此处设置为居民身份证识别data.putString(WbCloudOcrSDK.TITLE_BAR_CONTENT, "居民身份证识别");
  //设置sdk水印文字内容，默认仅供内部业务使用，此处设置为仅供本次业务使用
  data.putString(WbCloudOcrSDK.WATER_MASK_TEXT, "仅供本次业务使用");
  //设置扫描识别的时间上限,默认20秒，建议默认
  data.putLong(WbCloudOcrSDK.SCAN_TIME, 20000);
//初始化sdk，得到是否登录sdk成功的结果 
        WbCloudOcrSDK.getInstance().init(MainActivity.this, data, new WbCloudOcrSDK.OcrLoginListener() {
            @Override
            public void onLoginSuccess() {  //登录成功,拉起SDL页面                              WbCloudOcrSDK.getInstance().startActivityForOcr(MainActivity.this,
      new  WbCloudOcrSDK.IDCardScanResultListener() {  //返退出SDK回调接口
                    @Override
                    public void onFinish(EXIDCardResult exidCardResult, String resultCode, String resultMsg) {
                        // resultCode为0，则识别成功；否则识别失败
                        if ("0"== resultCode) {
                            WLogger.d(TAG, "识别成功");
                            // 识别成功  第三方应用对扫描的结果进行操作
                        } else {
                            WLogger.d(TAG, "识别失败");
                        }

                    }
                },,WbCloudOcrSDK.WBOCRTYPEMODE.WBOCRSDKTypeNormal);
            }
            @Override
            public void onLoginFailed(String errorCode, String errorMsg) {
               //登录失败  第三方应用可以获取登录失败错误码和错误信息
            }
        });   
```
				
### 8. 错误码描述
#### 8.1 终端返回错误码
 IDOCR_LOGIN_PARAMETER_ERROR = "-20000";     //传入参数有误
IDOCR_USER_CANCEL="200101";    //用户取消操作
IDOCRERROR_USER_NO_NET="100101";    //无网络
IDOCR_USER_2G="100102";   //不支持2G网络
IDOCR_ERROR_PERMISSION_CAMERA="100103";  //无相机权限
IDOCR_LOGINERROR="-10000";  //登录错误
SERVER_FAIL="-30000";    //内部服务错误**

#### 8.2 后台返回错误码
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