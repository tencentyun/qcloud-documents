### 1.前置条件
**1.相机/录音/读取手机信息权限检测**
SDK需要用到相机/录音/读取手机信息权限，在android6.0以上系统，sdk对其做了权限的运行时检测。但是由于android 6.0以下系统android并没有运行时权限，检测权限只能靠开关相机/麦克风进行。考虑到sdk的使用时间很短，快速频繁开关相机/麦克风可能会导致手机抛出异常，故sdk内对android 6.0以下手机没有做权限的检测。为了进一步提高用户体验，在android6.0以下系统上，我们建议合作方在拉起sdk前，帮助sdk做相机/麦克风/读取手机信息权限检测，提示用户确认打开了这三项权限后再进行刷脸，可以使整个刷脸体验更快更好。
**2.CPU平台设置**
目前SDK只支持armeabi-v7a平台，为了防止在其他cpu平台上sdk crash，我们建议在您的app的build.gradle里加上abiFilter，如下图8-2-1-2-1中红框所示：
![](https://mc.qcloudimg.com/static/img/61fab389aae7630adf751ec997dbdb16/image.png)

### 2.接入配置
云刷脸SDK（WbCloudFaceVerify）最低支持到** Android API 14: Android 4.0(ICS)**，请在构建项目时注意。
WbCloudFaceVerify将以AAR文件的形式提供，同时需要依赖云公共组件WbCloudNormal，同样也是以AAR文件的形式提供。
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
     //0. appcompat-v7
 compile 'com.android.support:appcompat-v7:23.0.1'
  //1. 云刷脸SDK
 compile(name: 'WbCloudFaceVerifySdk', ext: 'aar')
  //2.云公共组件
compile(name:’WbCloudNormal’,ext:’aar’)
      // 3. 依赖的第三方jar包
   compile 'com.google.code.gson:gson:2.3.1' //网络请求json解析
   compile 'com.squareup.okhttp:okhttp-urlconnection:2.4.0' //网络请求
    }
 ```
 
### 3.混淆配置
云刷脸产品的混淆规则分为三部分，分别是云刷脸sdk的混淆规则，云公共组件的混淆规则及依赖的第三方库混淆规则。
**1.云刷脸sdk的混淆规则**
 ```
###############云刷脸混淆规则 faceverify-BEGIN##################
#不混淆内部类
-keepattributes InnerClasses
-keep public class com.webank.wbcloudfaceverify2.tools.WbCloudFaceVerifySdk{
    public <methods>;
    public static final *;
}
-keep public class com.webank.wbcloudfaceverify2.tools.WbCloudFaceVerifySdk$*{
    *;
}
-keep public class com.webank.wbcloudfaceverify2.tools.ErrorCode{
    *;
}
-keep public class com.webank.wbcloudfaceverify2.ui.FaceVerifyStatus{

}
-keep public class com.webank.wbcloudfaceverify2.ui.FaceVerifyStatus$Mode{
    *;
}
-keep public class com.webank.wbcloudfaceverify2.tools.IdentifyCardValidate{
    public <methods>;
}
-keep public class com.tencent.youtulivecheck.**{
    *;
}
-keep public class com.webank.wbcloudfaceverify2.Request.*$*{
    *;
}
-keep public class com.webank.wbcloudfaceverify2.Request.*{
    *;
}
################云刷脸混淆规则 faceverify-END########################
 ```
 
您可以将如上代码拷贝到您的混淆文件中，也可以将SDK中的webank-cloud-face-verify-proguard-rules.pro拷贝到主工程根目录下,然后通过"-include webank-cloud-face-verify-rules.pro" 加入到您的混淆文件中。

**2.云公共组件的混淆规则**
 ```
#############webank normal混淆规则-BEGIN###################
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
-keep public class com.webank.normal.thread.ThreadOperate{
   *;
}
-keep public class com.webank.normal.thread.ThreadOperate$*{
   *;
}
-keep public class com.webank.normal.net.RequestParam$ParamType{
    *;
}
-keep public class com.webank.normal.tools.WLogger{
    *;
}

#webank normal包含的第三方库bugly
-keep class com.tencent.bugly.webank.**{
    *;
}
###########webank normal混淆规则-END#######################
 ```

您可以将如上代码拷贝到您的混淆文件中，也可以将SDK中的webank-cloud-normal-proguard-rules.pro拷贝到主工程根目录下,然后通过"-include webank-cloud-normal-rules.pro" 加入到您的混淆文件中。

**3.云刷脸依赖的第三方库的混淆规则**
 ```
########云产品依赖的第三方库 混淆规则-BEGIN############

## support:appcompat-v7
-keep public class android.support.v7.widget.** { *; }
-keep public class android.support.v7.internal.widget.** { *; }
-keep public class android.support.v7.internal.view.menu.** { *; }

-keep public class * extends android.support.v4.view.ActionProvider {
    public <init>(android.content.Context);
}

## Gson
# Gson uses generic type information stored in a class file when working with fields. Proguard
# removes such information by default, so configure it to keep all of it.
-keepattributes Signature

# For using GSON @Expose annotation
-keepattributes *Annotation*
-keepattributes EnclosingMethod
# If in your rest service interface you use methods with Callback argument.
-keepattributes Exceptions

# Gson specific classes
-keep class sun.misc.Unsafe { *; }
-keep class com.google.gson.stream.** { *; }

# Application classes that will be serialized/deserialized over Gson
-keep class com.google.gson.examples.android.model.** { *; }

# Prevent proguard from stripping interface information from TypeAdapterFactory,
# JsonSerializer, JsonDeserializer instances (so they can be used in @JsonAdapter)
-keep class * implements com.google.gson.TypeAdapterFactory
-keep class * implements com.google.gson.JsonSerializer
-keep class * implements com.google.gson.JsonDeserializer
##---------------End: proguard configuration for Gson  ----------

# OkHttp
-keep class com.squareup.okhttp.** { *; }
-keep interface com.squareup.okhttp.** { *; }
-dontwarn com.squareup.okhttp.**

# Okio
-keep class sun.misc.Unsafe { *; }
-dontwarn java.nio.file.*
-dontwarn org.codehaus.mojo.animal_sniffer.IgnoreJRERequirement
-dontwarn okio.**

#########云产品依赖的第三方库 混淆规则-END#############
 ```

您可以根据您现有的混淆规则，将缺少的第三库混淆规则拷贝到您的混淆文件中。

### 4.调用SDK接口
SDK代码调用的入口为：
com.webank.WbCloudFaceVerify.tools.WbCloudFaceVerifySdk这个类。
 ```
public class WbCloudFaceVeirfySdk {

/**
* 该类为一个单例，需要先获得单例对象再进行后续操作
   */
public static WbCloudFaceVeirfySdk getInstance(){
//	...
}
/**
* 在使用SDK前先初始化，传入需要的数据data，由 FaceVerifyLoginListener返回是否登录SDK成功
* 关于传入数据data见后面的说明
*/
public void init(Context context,Bundle data,FaceVerifyLoginListener loginListerner){
//	...
}
    /**
     * 登录成功后，调用此函数拉起sdk页面。
     * 由 FaceVerifyResultForSecureListener返回刷脸结果。
     */
    public void startActivityForSecurity(FaceVerifyResultForSecureListener listener) {	// ...
}

/**
  * 登录回调接口
  */
public interface FaceVerifyLoginListener {
        void onLoginSuccess();
        void onLoginFailed(String errorCode, String errorMsg);
    }

/**
  * 刷脸结果回调接口
  */
public interface FaceVerifyResultForSecureListener {
        /**
         * @PARAM resultCode 终端自己定义的错误码，详见ErrorCode
         * @PARAM nextShowGuide  下次是否要显示指引，返回第三方，由第三方存储传入
         * @PARAM faceCode  若错误是后台返回的，这里展示后台返回的错误码
         * @PARAM faceMsg 若错误是后台返回的，这里展示后台返回的错误信息;如果错误是终端返回的，这里展示前端错误信息
         * @PARAM sign 供app校验刷脸结果的安全性
         * @RARAM extendData  供后续增加接口字段
         */
        void onFinish(int resultCode, boolean nextShowGuide, String faceCode, String faceMsg, String sign, Bundle extendData);
    }
 ```

WbCloudFaceVerifySdk.init()的第二个参数用来传递数据.可以将参数打包到data(Bundle)中，必须传递的参数包括(参数要求见下一节描述):

 ```
//这些都是WbCloudFaceVerifySdk.InputData对象里的字段，是需要传入的数据信息
String userName;    //用户姓名
String idType;  //用户证件类型，01为身份证
String idNo; //用户身份证号
String agreementNo;  //订单号
String clientIp;   //用户ip信息,格式为”ip=xxx.xxx.xxx.xxx;”
// 示例：”ip=58.60.124.0”
String gps;       //用户gps信息, 格式为”lgt=xxx;lat=xxx;”
                  //示例：“lgt=22.5044;lat=113.9537“

String openApiAppId;  //APP_ID 
String openApiAppVersion;  //openapi  Version
String openApiNonce; //32位随机字符串
String openApiUserId; //user id
String openApiSign; //签名信息

//是否需要显示刷脸指引
boolean isShowGuide;      
//刷脸类别：简单FaceVerifyStatus.Mode.EASY  
//          中级FaceVerifyStatus.Mode.MIDDLE
//          高级 FaceVerifyStatus.Mode.ADVANCED
FaceVerifyStatus.Mode verifyMode;
String keyLicence;   //给合作方派发的licence
 ```
 
以上参数被封装在WbCloudFaceVerifySdk.InputData对象中（他是是一个Serializable对象）。

### 5.接口参数说明

| 参数 | 说明 |类型 |长度 | 是否必输 |
|---------|---------|---------|---------|---------|
| userName | 用户姓名| String |20 |必输 |
| idType | 用户证件类型| String |2 |必输 |
| userId | 用户证件号码| String |18 |必输，18位身份证号 |
| agreementNo | 订单号| String |32 |必输，合作方订单的唯一标识 |
| clientIp | 用户ip信息| String |30 |必输,格式为”ip=xxx.xxx.xxx.xxx;”；示例：”ip=58.60.124.0”。 |
| gps | 用户gps信息| String |30 |必输,格式为”lgt= xxx;lat=xxx;”；示例：“lgt=22.5044;lat=113.9537“ |
| openApiAppId | 腾讯服务分配的app_id| String |腾讯服务分配 |必输，腾讯服务分配的app_id |
| openApiAppVersion | 接口版本号| String |20 |必输，每次请求需要的一次性nonce |
| openApiNonce | 32位随机字符串| String |32 |必输，每次请求需要的一次性nonce |
| openApiUserId | User Id| String |30 |必输，每个用户唯一的标识 |
| openApiSign | 合作方后台服务器通过ticket计算出来的签名信息| String |40 |必输 |
| isShowGuide | 是否需要显示刷脸指引，sdk每次会返回这个结果，由app端存储，下次拉起时再传入| boolean |1 |必输 |
| verifyMode | 刷脸类型：<br>简单<br>FaceVerifyStatus.Mode.EASY  <br>中级<br>FaceVerifyStatus.Mode.MIDDLE<br>高级<br>FaceVerifyStatus.Mode.ADVANCED| FaceVerifyStatus.Mode | |必输 |
| keyLicence | 腾讯给合作方派发的licence| String | |必输 |

### 6.个性化参数设置
WbCloudFaceVerifySdk.init()里Bundle data，除了必须要传的InputData对象(详情见上节)之外，还可以由合作方方传入一些个性化参数，量身打造更契合自己app的sdk。如果合作方未设置这些参数，则以下所有参数按默认值设置。
#### 6.1是否显示刷脸成功页面
合作方可以控制是否显示SDK自带的刷脸成功页面。 SDK默认显示刷脸成功页面，但第三方可以控制关闭不显示，直接回到自己的业务场景或者自定义的成功页面。设置代码如下：

```
# 在MainActivity中点击某个按钮的代码逻辑：
  //先将必填的InputData放入Bundle中
  data.putSerializable(WbCloudFaceVerifySdk.INPUT_DATA, inputData);
  //是否展示刷脸成功页面，如果不设置则默认展示；设置了则以设置为准
  //此处设置为不显示刷脸成功页
  data.putBoolean(WbCloudFaceVerifySdk.SHOW_SUCCESS_PAGE, false);
```

#### 6.2 是否显示刷脸失败原因页
合作方可以控制是否显示SDK自带的刷脸失败原因页。 SDK默认显示刷脸失败原因页，但第三方可以控制关闭不显示，直接回到自己的业务场景或者自定义的失败页面。设置代码如下：
```
# 在MainActivity中点击某个按钮的代码逻辑：
  //先将必填的InputData放入Bundle中
  data.putSerializable(WbCloudFaceVerifySdk.INPUT_DATA, inputData);
  //是否展示刷脸失败原因页，如果不设置则默认展示；设置了则以设置为准
  //此处设置为不显示刷脸成功页
  data.putBoolean(WbCloudFaceVerifySdk.SHOW_FAIL_PAGE, false);
```

#### 6.3 SDK样式选择
合作方可以选择sdk样式。目前sdk有明亮模式和暗黑模式两种，默认显示暗黑模式。设置代码如下:
```
# 在MainActivity中点击某个按钮的代码逻辑：
  //先将必填的InputData放入Bundle中
  data.putSerializable(WbCloudFaceVerifySdk.INPUT_DATA, inputData);
  //对sdk样式进行设置，默认为暗黑模式
  //此处设置为明亮模式
  data.putString(WbCloudFaceVerifySdk.COLOR_MODE, WbCloudFaceVerifySdk.WHITE);
```

#### 6.4 是否对录制视频进行检查

SDK为了进一步确保刷脸的安全性，不论是简单还是中级模式都有录制用户刷脸视频做存证。但其实在简单/中级模式中，起到识别作用的并不是视频文件。在sdk使用过程中，发现视频录制在性能不太好的手机上可能会报错，导致刷脸中断，影响用户体验。
    为了减少因为录制视频原因导致的刷脸中断问题，sdk默认设置对录制的视频不作检测。如果合作方对刷脸安全有进一步的更加严格的要求，可以考虑打开这一选项。但打开这个字段可能导致某些低性能手机上用户刷脸不能进行，请慎重考虑。设置代码如下：
		
```
# 在MainActivity中点击某个按钮的代码逻辑：
  //先将必填的InputData放入Bundle中
  data.putSerializable(WbCloudFaceVerifySdk.INPUT_DATA, inputData);
  //设置是否对录制的视频进行检测，默认不检测
  //此处设置为检测
  data.putBoolean(WbCloudFaceVerifySdk.VIDEO_CHECK, true);
```

#### 6.5 接入示例
```
# 在MainActivity中点击某个按钮的代码逻辑：
  //先将必填的InputData放入Bundle中
  data.putSerializable(WbCloudFaceVerifySdk.INPUT_DATA, inputData);
  //个性化参数设置,此处均设置为与默认相反
  //是否显示成功结果页，默认显示，此处设置为不显示
  data.putBoolean(WbCloudFaceVerifySdk.SHOW_SUCCESS_PAGE, false);
  //是否展示刷脸失败页面，默认展示,此处设置为不显示
  data.putBoolean(WbCloudFaceVerifySdk.SHOW_FAIL_PAGE, false);
  //sdk样式设置，默认暗黑模式，此处设置为明亮模式
  data.putString(WbCloudFaceVerifySdk.COLOR_MODE, WbCloudFaceVerifySdk.WHITE);
  //是否对录制视频进行检查,默认不检查，此处设置为检查
  data.putBoolean(WbCloudFaceVerifySdk.VIDEO_CHECK, true);
```

### 7.接入示例
```
# 在MainActivity中点击某个按钮的代码逻辑：
//先填好数据 
Bundle data = new Bundle();
WbCloudFaceVerifySdk.InputData inputData = new WbCloudFaceVerifySdk.InputData(
                userName,
                idType,
                idNo,
                agreementNo,
                clientIp,
                gps,
                openApiAppId,
                openApiAppVersion,
                openApiNonce,
                userId,
                userSign,
                isShowGuide,
                verifyMode,
                keyLicence);
  data.putSerializable(WbCloudFaceVerifySdk.INPUT_DATA, inputData);

  //个性化参数设置,可以不设置，不设置则为默认选项。
  //此处均设置为与默认相反
  //是否显示成功结果页，默认显示，此处设置为不显示
  data.putBoolean(WbCloudFaceVerifySdk.SHOW_SUCCESS_PAGE, false);
  //是否展示刷脸失败页面，默认展示,此处设置为不显示
  data.putBoolean(WbCloudFaceVerifySdk.SHOW_FAIL_PAGE, false);
  //sdk样式设置，默认暗黑模式，此处设置为明亮模式
  data.putString(WbCloudFaceVerifySdk.COLOR_MODE, WbCloudFaceVerifySdk.WHITE);
  //是否对录制视频进行检查,默认不检查，此处设置为检查
  data.putBoolean(WbCloudFaceVerifySdk.VIDEO_CHECK, true);


//初始化sdk，得到是否登录sdk成功的结果 
WbCloudFaceVerifySdk.getInstance().init(
  MainActivity.this,
  data,
  //由FaceVerifyLoginListener返回登录结果
  new WbCloudFaceVerifySdk.FaceVerifyLoginListener() {
            @Override
            public void onLoginSuccess() {
             //登录成功，拉起sdk页面
  WbCloudFaceVerifySdk.getInstance().startActivityForSecurity(new WbCloudFaceVerifySdk.FaceVerifyResultForSecureListener() {
     //由FaceVerifyResultListener返回刷脸结果
       @Override
public void onFinish(int resultCode, boolean nextShowGuide, String faceCode, String faceMsg, String sign, Bundle extendData) { 
    // resultCode为0，则刷脸成功；否则刷脸失败
         if (resultCode == 0) {
              Log.d(TAG, "刷脸成功！");
           } else {
              Log.d(TAG, "刷脸失败！);
                              }
                    }
                });
            }
            @Override
            public void onLoginFailed(String errorCode, String errorMsg) {
              //登录失败
              ...
         }     
 ```

### 8.错误码描述
#### 8.1刷脸登录错误码

   FACEVERIFY_LOGIN_ERROR = "-10000";     //登录请求错误，没有返回code
   FACEVERIFY_LOGIN_PARAMETER_ERROR = "-20000";    //传入参数有误
   FACEVERIFY_LOGIN_NO_RESONSE = "-30000";   //登录请求未到达后台，非200
	 
#### 8.2 刷脸错误码

   FACEVERIFY_NOERROR = 0;                 //刷脸成功完成，通过刷脸
    FACEVERIFY_ERROR_DEFAULT = 10000;      //刷脸完成，但验证失败
    FACEVERIFY_ERROR_CANCELED = 20000;           //用户取消
    FACEVERIFY_ERROR_CANCELED_BEFORE = 21000;    //引导页取消
    FACEVERIFY_ERROR_CANCELED_DURING = 22000;    //刷脸中取消
FACEVERIFY_ERROR_CANCELED_AFTER = 23000;     //上传时取消
FACEVERIFY_ERROR_CANCELED_VOICE_LOW=24000; //高级模式音量太低取消
    FACEVERIFY_ERROR_NETWORK = 30000;            //网络错误 没有网络
    FACEVERIFY_ERROR_NETWORK_ACTIVE = 32000;          //拉活体模式错误
    FACEVERIFY_ERROR_NETWORK_LIPS = 33000;            //拉唇语错误
    FACEVERIFY_ERROR_NETWORK_UPLOAD = 34000;            //上传错误
    FACEVERIFY_ERROR_PERMISSION = 40000;            //权限异常
    FACEVERIFY_ERROR_PERMISSION_CAMERA = 41000;         //相机未授权
FACEVERIFY_ERROR_PERMISSION_MIC = 42000;            //麦克风未授权
FACEVERIFY_ERROR_PERMISSION_READ_PHONE=43000; //READ_PHONE未授权
    FACEVERIFY_ERROR_CAMERA = 50000;            //音视频设备异常
    FACEVERIFY_ERROR_MEDIARECORD = 60000;      //视频录制出错
    FACEVERIFY_ERROR_OUT_OF_TIME = 70000;   //验证超时
    FACEVERIFY_ERROR_OUT_OF_TIME_FACE_DETECT = 71000;   //扫脸验证超时
    FACEVERIFY_ERROR_OUT_OF_TIME_ACTIVE_DETECT = 72000; //活体验证超时
