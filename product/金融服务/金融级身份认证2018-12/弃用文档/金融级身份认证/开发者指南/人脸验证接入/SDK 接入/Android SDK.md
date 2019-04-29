## 1. 前置条件
### 1.1 相机/录音/读取手机信息权限检测
SDK 需要用到相机/录音/读取手机信息权限，在 Android 6.0 以上系统，SDK 对其做了权限的运行时检测。但是由于 Android 6.0 以下系统 Android 并没有运行时权限，检测权限只能靠开关相机/麦克风进行。考虑到 SDK 的使用时间很短，快速频繁开关相机/麦克风可能会导致手机抛出异常，故 SDK 内对 Android 6.0 以下手机没有做权限的检测。为了进一步提高用户体验，在 Android 6.0 以下系统上，我们建议合作方在拉起 SDK 前，帮助 SDK 做相机/麦克风/读取手机信息权限检测，提示用户确认打开了这三项权限后再进行刷脸，可以使整个人脸验证体验更快更好。
### 1.2 CPU 平台设置
目前 SDK 只支持 armeabi-v7a 平台，为了防止在其他 CPU 平台上 sdk crash，我们建议在您的 App 的 build.gradle 里加上 abiFilter，如下图中红框所示：
![](https://mc.qcloudimg.com/static/img/61fab389aae7630adf751ec997dbdb16/image.png)

## 2. 接入配置
云刷脸 SDK（WbCloudFaceVerify）最低支持到** Android API 14: Android 4.0(ICS)**，请在构建项目时注意。
刷脸 SDK 将以 AAR 文件的形式提供，包括**代码包（WbCloudFaceVerifySdk）和资源包（WbCloudFaceRes）**两个部分，缺一不可。其中代码包分为动作活体和数字活体两个模式，资源包分为黑色皮肤和白色皮肤（SDK 皮肤的设定，除了接入对应的 AAR，还需要设定相关代码。详见本页第六部分：SDK 样式选择。默认黑色皮肤，无需格外设置），接入方可自由选择组合四个模式。
![](https://mc.qcloudimg.com/static/img/0d1fb1b5512b25f4efda0cd89fb33ddb/image.png)
另外刷脸 SDK 同时需要依赖**云公共组件（WbCloudNormal）**，同样也是以 AAR 文件的形式提供。
需要添加下面文档中所示的依赖（将提供的 AAR 文件加入到 App 工程的`'libs'`文件夹下面,
并且在** build.gradle **中添加下面的配置）:
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
 //2. 云normal SDK
 compile(name: 'WbCloudNormal', ext: 'aar')
 //3. 云刷脸皮肤资源包-可选择黑色/白色 默认黑色
 compile(name: 'WbCloudFaceResBlack', ext: 'aar')
 //compile(name: 'WbCloudFaceResWhite', ext: 'aar')
}
    }
```

## 3. 混淆配置
云刷脸产品的混淆规则分为三部分，分别是云刷脸 SDK 的混淆规则，云公共组件的混淆规则及依赖的第三方库混淆规则。
### 3.1 云刷脸 sdk 的混淆规则

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


您可以将如上代码拷贝到您的混淆文件中，也可以将 SDK 中的`webank-cloud-face-verify-proguard-rules.pro`拷贝到主工程根目录下，然后通过`-include webank-cloud-face-verify-rules.pro`加入到您的混淆文件中。

### 3.2 云公共组件的混淆规则

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
-keep public class com.webank.normal.thread.*$*{
   *;
}
-keep public class com.webank.normal.thread. *{
   *;
}
-keep public class com.webank.normal.tools.WLogger{
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

#webank normal包含的第三方库bugly
-keep class com.tencent.bugly.webank.**{
    *;
}
###########webank normal混淆规则-END#######################
 ```

您可以将如上代码拷贝到您的混淆文件中，也可以将 SDK 中的`webank-cloud-normal-proguard-rules.pro`拷贝到主工程根目录下，然后通过`-include webank-cloud-normal-rules.pro`加入到您的混淆文件中。

### 3.3 云刷脸依赖的第三方库的混淆规则

```
-keep public class com.webank.normal.thread.*$*{
   *;
}
-keep public class com.webank.normal.thread. *{
   *;
}



-keep public class com.webank.normal.tools.WLogger{
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

#webank normal包含的第三方库bugly
-keep class com.tencent.bugly.webank.**{
    *;
}
###########webank normal混淆规则-END#######################

```

您可以根据您现有的混淆规则，将缺少的第三库混淆规则拷贝到您的混淆文件中。

## 4. 调用 SDK 接口
SDK 代码调用的入口为：
**`com.webank.wbcloudfaceverify2.tools.WbCloudFaceVerifySdk`** 这个类。
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

`WbCloudFaceVerifySdk.init()` 的第二个参数用来传递数据.可以将参数打包到 data(Bundle) 中，必须传递的参数包括（参考要求详见下一节描述）:

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
//刷脸类别：动作活体 FaceVerifyStatus.Mode.MIDDLE
//          数字活体 FaceVerifyStatus.Mode.ADVANCED
FaceVerifyStatus.Mode verifyMode;
String keyLicence;   //给合作方派发的licence
 ```

以上参数被封装在`WbCloudFaceVerifySdk.InputData`对象中（它是一个 Serializable 对象）。

## 5. 接口参数说明

| 参数                | 说明                                       | 类型                    | 长度     | 是否必填                                     |
| ----------------- | ---------------------------------------- | --------------------- | ------ | ---------------------------------------- |
| userName          | 用户姓名                                     | String                | 20     | 必填                                       |
| idType            | 用户证件类型                                   | String                | 2      | 必填，01 为身份证                               |
| userId            | 用户证件号码                                   | String                | 18     | 必填，18 位身份证号                              |
| agreementNo       | 订单号                                      | String                | 32     | 必填，合作方订单的唯一标识                            |
| clientIp          | 用户 ip 信息                                 | String                | 30     | 必填，格式为”ip=xxx.xxx.xxx.xxx;”；示例：”ip=58.60.124.0”。 |
| gps               | 用户 gps 信息                                | String                | 30     | 必填，格式为”lgt= xxx;lat=xxx;”；示例：“lgt=22.5044;lat=113.9537“ |
| openApiAppId      | 腾讯服务分配的 app_id                           | String                | 腾讯服务分配 | 必填，腾讯服务分配的 app_id                        |
| openApiAppVersion | 接口版本号                                    | String                | 20     | 必填，默认填 1.0.0                             |
| openApiNonce      | 32 位随机字符串                                | String                | 32     | 必填，每次请求需要的一次性 nonce                      |
| openApiUserId     | User Id                                  | String                | 30     | 必填，每个用户唯一的标识                             |
| openApiSign       | 合作方后台服务器通过 ticket 计算出来的签名信息              | String                | 40     | 必填                                       |
| isShowGuide       | 是否需要显示刷脸指引，SDK 每次会返回这个结果，由 App 端存储，下次拉起时再传入 | boolean               | 1      | 必填                                       |
| verifyMode        | 刷脸类型：<br>动作活体<br>FaceVerifyStatus.Mode.MIDDLE<br>数字活体<br>FaceVerifyStatus.Mode.ADVANCED | FaceVerifyStatus.Mode |        | 必填                                       |
| keyLicence        | 腾讯给合作方派发的 licence                        | String                |        | 必填                                       |

## 6. 个性化参数设置
`WbCloudFaceVerifySdk.init()`里 Bundle data，除了必须要传的 InputData 对象(详情见上节)之外，还可以由合作方方传入一些个性化参数，量身打造更契合自己 App 的 SDK。如果合作方未设置这些参数，则以下所有参数按默认值设置。

### 6.1是否显示刷脸成功页面
合作方可以控制是否显示 SDK 自带的刷脸成功页面。 SDK 默认显示刷脸成功页面，但第三方可以控制关闭不显示，直接回到自己的业务场景或者自定义的成功页面。设置代码如下：

```
# 在 MainActivity 中点击某个按钮的代码逻辑：
  //先将必填的 InputData 放入 Bundle 中
  data.putSerializable(WbCloudFaceVerifySdk.INPUT_DATA, inputData);
  //是否展示刷脸成功页面，如果不设置则默认展示；设置了则以设置为准
  //此处设置为不显示刷脸成功页
  data.putBoolean(WbCloudFaceVerifySdk.SHOW_SUCCESS_PAGE, false);
```

### 6.2 是否显示刷脸失败原因页
合作方可以控制是否显示 SDK 自带的刷脸失败原因页。 SDK 默认显示刷脸失败原因页，但第三方可以控制关闭不显示，直接回到自己的业务场景或者自定义的失败页面。设置代码如下：

```
# 在 MainActivity 中点击某个按钮的代码逻辑：
  //先将必填的 InputData 放入 Bundle 中
  data.putSerializable(WbCloudFaceVerifySdk.INPUT_DATA, inputData);
  //是否展示刷脸失败原因页，如果不设置则默认展示；设置了则以设置为准
  //此处设置为不显示刷脸成功页
  data.putBoolean(WbCloudFaceVerifySdk.SHOW_FAIL_PAGE, false);
```

### 6.3 SDK 样式选择
合作方可以选择 SDK 样式，需要和 SDK 资源包一起加载显示。目前 SDK 有黑色模式和白色模式两种，默认显示黑色模式。设置代码如下:
```
# 在 MainActivity 中点击某个按钮的代码逻辑：
  //先将必填的 InputData 放入 Bundle中
  data.putSerializable(WbCloudFaceVerifySdk.INPUT_DATA, inputData);
  //对 sdk 样式进行设置，默认为黑色模式
  //此处设置为白色模式（需要与白色资源包一起配合使用）
  data.putString(WbCloudFaceVerifySdk.COLOR_MODE, WbCloudFaceVerifySdk.WHITE);
```

### 6.4 是否自带对比源数据
合作方可以选择给 SDK 送上自带的对比源数据进行对比。合作方可以上送两类照片，一类是水纹照，一类是高清照；照片需要转化为经过 base64 编码后的 String 来上送。图片大小不可超过 2M，经过编码后的图片 String 大小不可超过 3M。上送照片类型与上送照片 String 两者缺一不可，否则将不使用上送的数据源。不自带对比源的合作方可以不上送此两个字段。上送的代码设置如下：
```
# 在 MainActivity 中点击某个按钮的代码逻辑：
  //先将必填的 InputData 放入 Bundle 中
  data.putSerializable(WbCloudFaceVerifySdk.INPUT_DATA, inputData);
  //上送自带的数据源信息，照片类型与照片 string 缺一不可
//上送照片类型，1 是水纹照  2 是高清照
   data.putString(WbCloudFaceVerifySdk.SRC_PHOTO_TYPE, srcPhotoType);  
//比对源照片的 BASE64 string
data.putString(WbCloudFaceVerifySdk.SRC_PHOTO_STRING, srcPhotoString);  
```

#### 6.5 是否对录制视频进行检查

SDK 为了进一步确保刷脸的安全性，不论是简单还是中级模式都有录制用户刷脸视频做存证。但其实在简单/中级模式中，起到识别作用的并不是视频文件。在 SDK 使用过程中，发现视频录制在性能不太好的手机上可能会报错，导致刷脸中断，影响用户体验。

为了减少因为录制视频原因导致的刷脸中断问题，SDK 默认设置对录制的视频不作检测。如果合作方对刷脸安全有进一步的更加严格的要求，可以考虑打开这一选项。但打开这个字段可能导致某些低性能手机上用户刷脸不能进行，请慎重考虑。设置代码如下：

```
# 在 MainActivity 中点击某个按钮的代码逻辑：
  //先将必填的 InputData 放入 Bundle 中
  data.putSerializable(WbCloudFaceVerifySdk.INPUT_DATA, inputData);
  //设置是否对录制的视频进行检测，默认不检测
  //此处设置为检测
  data.putBoolean(WbCloudFaceVerifySdk.VIDEO_CHECK, true);
```

### 6.6 接入示例
```
# 在 MainActivity 中点击某个按钮的代码逻辑：
  //先将必填的 InputData 放入 Bundle 中
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

## 7. 整体接入示例
```
# 在 MainActivity 中点击某个按钮的代码逻辑：
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
  //sdk 样式设置，默认暗黑模式，此处设置为明亮模式
  data.putString(WbCloudFaceVerifySdk.COLOR_MODE, WbCloudFaceVerifySdk.WHITE);
  //是否对录制视频进行检查,默认不检查，此处设置为检查
  data.putBoolean(WbCloudFaceVerifySdk.VIDEO_CHECK, true);


//初始化 sdk，得到是否登录 sdk 成功的结果 
WbCloudFaceVerifySdk.getInstance().init(
  MainActivity.this,
  data,
  //由 FaceVerifyLoginListener 返回登录结果
  new WbCloudFaceVerifySdk.FaceVerifyLoginListener() {
            @Override
            public void onLoginSuccess() {
             //登录成功，拉起sdk页面
  WbCloudFaceVerifySdk.getInstance().startActivityForSecurity(new WbCloudFaceVerifySdk.FaceVerifyResultForSecureListener() {
     //由 FaceVerifyResultListener 返回刷脸结果
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

## 8. 错误码描述
### 8.1 刷脸登录错误码

| 错误码                                      | 错误描述             |
| ---------------------------------------- | ---------------- |
| FACEVERIFY_LOGIN_ERROR = "-10000";       | 登录请求错误，没有返回 code |
| FACEVERIFY_LOGIN_PARAMETER_ERROR = "-20000"; | 传入参数有误           |
| FACEVERIFY_LOGIN_NO_RESONSE = "-30000";  | 登录请求未到达后台，非 200  |


### 8.2 刷脸错误码

| 错误码                                      | 错误描述           |
| ---------------------------------------- | -------------- |
| FACEVERIFY_NOERROR = 0;                  | 刷脸成功完成，通过刷脸    |
| FACEVERIFY_ERROR_DEFAULT = 10000;        | 刷脸完成，但验证失败     |
| FACEVERIFY_ERROR_CANCELED = 20000;       | 用户取消           |
| FACEVERIFY_ERROR_CANCELED_BEFORE = 21000; | 引导页取消          |
| FACEVERIFY_ERROR_CANCELED_DURING = 22000; | 刷脸中取消          |
| FACEVERIFY_ERROR_CANCELED_AFTER = 23000; | 上传时取消          |
| FACEVERIFY_ERROR_CANCELED_VOICE_LOW=24000; | 高级模式音量太低取消     |
| FACEVERIFY_ERROR_NETWORK = 30000;        | 网络错误 没有网络      |
| FACEVERIFY_ERROR_NETWORK_ACTIVE = 32000; | 拉活体模式错误        |
| FACEVERIFY_ERROR_NETWORK_LIPS = 33000;   | 拉唇语错误          |
| FACEVERIFY_ERROR_NETWORK_UPLOAD = 34000; | 上传错误           |
| FACEVERIFY_ERROR_PERMISSION = 40000;     | 权限异常           |
| FACEVERIFY_ERROR_PERMISSION_CAMERA = 41000; | 相机未授权          |
| FACEVERIFY_ERROR_PERMISSION_MIC = 42000; | 麦克风未授权         |
| FACEVERIFY_ERROR_PERMISSION_READ_PHONE=43000; | READ_PHONE 未授权 |
| FACEVERIFY_ERROR_CAMERA = 50000;         | 音视频设备异常        |
| FACEVERIFY_ERROR_MEDIARECORD = 60000;    | 视频录制出错         |
| FACEVERIFY_ERROR_OUT_OF_TIME = 70000;    | 验证超时           |
| FACEVERIFY_ERROR_OUT_OF_TIME_FACE_DETECT = 71000; | 扫脸验证超时         |
| FACEVERIFY_ERROR_OUT_OF_TIME_ACTIVE_DETECT = 72000; | 活体验证超时         |
| FACEVERIFY_ERROR_ACTIVE_DETECT_NOFACE=80000; | 活体检测时人脸曾移出框外   |

上一步：[SDK 启动](https://cloud.tencent.com/document/product/655/13824)