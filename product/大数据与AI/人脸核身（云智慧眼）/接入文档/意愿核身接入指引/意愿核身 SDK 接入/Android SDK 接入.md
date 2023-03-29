## 开发准备
### CPU 平台设置
目前 SDK 支持 armeabi，armeabi-v7a，arm64-v8a，为了防止在其他 CPU 平台上 SDK Crash，我们建议在您的 App 的 build.gradle 里加上 abiFilter，如下所示：
```
defaultConfig {
    ndk {
          //设置支持的so库框架
          abiFilters 'armeabi-v7a', 'armeabi', 'arm64-v8a',
     }
}
```

## 配置流程
### 接入配置
意愿核身 SDK（WbCloudFaceLiveSdk、WbCloudFaceWillSdk）最低支持到 **Android API 19: Android 4.4 (KitKat)**  ，请在构建项目时注意。
意愿核身 SDK 将以 AAR 文件的形式提供。另外 意愿核身 SDK  同时需要依赖云公共组件 WBCloudNormal，同样也是以 AAR 文件的形式提供。
需要添加下面文档中所示的依赖（将提供的 AAR 文件加入到 app 工程的 libs 文件夹下面，并且在 build.gradle 中添加下面的配置）：
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
    //1. 云刷脸SDK
    implementation(name: 'WbCloudFaceLiveSdk-v4.5.5.0-3b725d95', ext: 'aar')
    //2. 云common SDK
    implementation(name: 'WbCloudNormal-v5.1.3-0f08e6d', ext: 'aar')
//3.意愿性 SDK
implementation(name: 'WbCloudFaceWillSdk-v1.0.0-3b725d95', ext: 'aar')
   }
```

### 混淆配置
混淆规则已经嵌入 sdk 内，此处不另外提供。

## 接口调用
1. 标准模式 SDK 接口调用方法
SDK 代码调用的入口为 `com.tencent.cloud.huiyansdkface.facelight.api.WbCloudFaceVerifySdk `这个类。     
```
public class WbCloudFaceVerifySdk{

/**
* 该类为一个单例，需要先获得单例对象再进行后续操作
   */
       public static synchronized WbCloudFaceVerifySdk getInstance() {
       //    ...
       }
/**
* 在使用SDK前先初始化，传入需要的数据data
* 由 WbCloudFaceVerifyLoginListener返回是否登录SDK成功
* 关于传入数据data见后面的说明
*/
public void initWillSdk(Context context,Bundle data,
WbCloudFaceVerifyLoginListener loginListerner){
//    ...
}
   /**
     * 登录成功后，调用此函数拉起sdk页面。
     * 由 FaceVerifyResultForSecureListener返回刷脸结果。
     */
public void startWbFaceVerifySdk(Context ctx,
WbCloudFaceVerifyResultListener listener) {    // ...
}
```
WbCloudFaceVerifySdk.initSdk() 的第二个参数用来传递数据.可以将参数打包到 data(Bundle) 中，必须传递的参数包括：
```
//这些都是WbCloudFaceVerifySdk.InputData对象里的字段，是需要传入的数据信息
String faceId; //此次刷脸用户标识，合作方需要向人脸识别后台拉取获得，详见获取faceId接口
String agreementNo;  //订单号
String openApiAppId;  //APP_ID 
String openApiAppVersion;  //openapi  Version
String openApiNonce; //32位随机字符串
String openApiUserId; //user id
String openApiSign; //签名信息
//刷脸类别：分级活体 FaceVerifyStatus.Mode.GRADE      
FaceVerifyStatus.Mode verifyMode;
String keyLicence;   //在人脸核身控制台内申请
```
以上参数被封装在 WbCloudFaceVerifySdk.InputData 对象中（它是一个 Serializable 对象）。
2. 登录接口
```
/**
  * 登录回调接口
  */
public interface WbCloudFaceVerifyLoginListener {
    void onLoginSuccess();
    void onLoginFailed(WbFaceError error);
}
```
3. 返回第三方接口
```
/**
  * 退出SDK,返回第三方的回调,同时返回识别结果
  */
public interface WbCloudFaceVerifyResultListener {
    /**
     * @PARAM result 刷脸结果
     */
    void onFinish(WbFaceVerifyResult result);
}

```

### 识别结果类
WbFaceVerifyResult 是 SDK 用来给合作方传递身份识别结果的对象，在 WbCloudFaceVerifyResultListener 回调中作为参数返回给合作方 App。WbFaceVerifyResult 对象的各个字段意义如下表所示：

| 字段名 | 类型 | 字段含义 | 说明| 
|---------|---------|---------|---------|
| isSuccess | boolean   | 人脸核身是否成功  | True 代表人脸核身对比成功；false 代表人脸核身失败，具体的失败原因请参考 [WbFaceError 对象说明](#WbFaceError)| 
| sign  | String    | 签名|   供 App 校验人脸核身结果的安全性| 
| liveRate  | String    | 活体检测分数|   -| | 
| similarity    | String    | 人脸比对分数    | “仅活体检测” 类型不提供此分数| 
| userImageString   | String|   用户人脸核身图片    | 经过 Base64 编码后的用户人脸核身图片，仅用户成功通过验证时返回| 
| WbFaceError   | 自定义对象 | 人脸核身错误    | 人脸核身成功时为 null| 
| WbFaceWillModeResult  | 自定义对象 | 意愿性结果信息   | -| 

### WbFaceError 对象说明 [](id:WbFaceError)
WbFaceError 是 SDK 用来给合作方传递人脸核身错误信息的对象，在 WbCloudFaceVerifyLoginListener 回调和 WbFaceVerifyResult 对象中作为参数返回给合作方 App。WbFaceError 对象的各个字段意义如下表所示，各个字段的内容取值详情请参见 SaaS 服务[ 错误码](https://cloud.tencent.com/document/product/1007/35871)。

| 字段名 | 类型 | 字段含义 |说明| 
|---------|---------|---------|---------|
| domain    | String    | 错误发生的阶段   | 只有当domain=WBFaceErrorDomainCompareServer时表示用户完成了刷脸，可以通过接口去拉取刷脸结果。其他domain表示用户刷脸中途退出或命中了风控逻辑，后端无法查询到刷脸结果| 
| code  | String    | 错误码   | -| 
| desc  | String    | 错误描述|     如有需求，可以展示给用户| 
| reason    | String    | 错误信息内容    | 错误的详细实际原因，主要用于定位问题| 

### WbFaceWillModeResult 对象说明
WbFaceWillModeResult 是 SDK 用来给合作方传递意愿性表达综合信息的对象，在 WbCloudFaceVerifyResultListener 中的 WbFaceVerifyResult 对象中作为参数返回给合作方 App。WbFaceWillModeResult 对象的各个字段意义如下表所示，各个字段的内容取值详情请参见 SaaS 服务 [错误码](https://cloud.tencent.com/document/product/1007/35871)。

| 字段名 | 类型 | 字段含义 | 说明|
|---------|---------|---------|---------|
| faceCode  | String    | 人脸识别结果码|  -| 
| faceMsg   | String    | 人脸识别结果信息|     -| 
| willCode  | String|   ASR 结果码 | -| 
| willMsg   | String    | ASR 结果信息  | -| 
| videoPath|    String| 意愿性存证视频存储地址 | 如果打开了本地存储意愿性视频开关，将在此处返回意愿性视频地址| 

### 接口参数说明
**InputData 对象说明**
InputData 是用来给 SDK 传递一些必须参数所需要使用的对象（WbCloudFaceVerifySdk.initWillSdk() 的第二个参数），合作方需要往里塞入SDK 需要的一些数据以便启动刷脸 SDK。
其中 InputData 对象中的各个参数定义如下表，请合作方按下表标准传入对应的数据。

| 参数 | 说明 | 类型 |    <nobr>长度（字节）|       是否必填|   
|---------|---------|---------|---------|---------|
| faceId    | 刷脸 id 号，由合作方向人脸识别后台拉取获得   | String    | - | 是| 
| agreementNo|  订单号，合作方订单的唯一标识  | String    | 32    | 是| 
| openApiAppId  | 业务流程唯一标识，即   WBappid，可参考 获取 WBappid 指引在人脸核身控制台内申请|    String|     8|  是| 
|openApiAppVersion  | 接口版本号，默认填 1.0.0   |String|    20  |是|
| openApiNonce  | 32 位随机字符串，每次请求需要的一次性  nonce|  String  | 32|   是| 
| openApiUserId | User Id，每个用户唯一的标识|    String|     30|     是| 
| openApiSign   | 获取方式请参考 生成SDK接口调用步骤使用签名 |     String  | 40|   是| 
|verifyMode |刷脸类型：分级模式 FaceVerifyStatus.Mode.GRADE| FaceVerifyStatus.Mode   |-  |是|
| keyLicence    |在人脸核身控制台内申请    | String    |以实际申请为准|   是|

**个性化参数设置（可选）**
WbCloudFaceVerifySdk.initSdk() 里 Bundle data，除了必须要传的 InputData 对象之外，还可以由合作方为其传入一些个性化参数，量身打造更契合自己 App 的 SDK。如果合作方未设置这些参数，则以下所有参数按默认值设置。

**是否录制意愿性视频存证**
SDK 默认不录制视频存证。如果合作方需要视频存证，可以通过该字段进行设置。设置代码如下：
```
# 在MainActivity中单击某个按钮的代码逻辑：
  //先将必填的InputData放入Bundle中
  data.putSerializable(WbCloudFaceContant.INPUT_DATA, inputData);
  //设置是否录制视频进行存证，默认不录制存证。
  //此处设置为录制存证
  data.putBoolean(WbCloudFaceContant.RECORD_WILL_VIDEO, true);
```
**是否对录制视频进行检查**
>? 如果上一节的 **是否录制视频存证** 的设置为录制存证，则目前该字段有效，否则不录制视频的话，也不会对视频进行检查，设置无效。
>
在 SDK 使用过程中，发现视频录制在性能不太好的手机上可能会报错，导致刷脸中断，影响用户体验。

为了减少因为录制视频原因导致的刷脸中断问题，SDK 默认设置对录制的视频不作检测。如果合作方对刷脸安全有进一步的更加严格的要求，可以考虑打开这一选项。但打开这个字段可能导致某些低性能手机上用户刷脸不能进行，请慎重考虑。设置代码如下：
```
# 在MainActivity中单击某个按钮的代码逻辑：
  //先将必填的InputData放入Bundle中
  data.putSerializable(WbCloudFaceContant.INPUT_DATA, inputData);
  //设置是否对录制的视频进行检测，默认不检测
  //此处设置为检测
  data.putBoolean(WbCloudFaceContant.CHECK_WILL_VIDEO, true);
```

## 错误码描述
SDK 在登录以及返回人脸服务结果时，如果发生错误或者识别失败会返回 WBFaceError 对象，该对象的字段结构意义见 接口参数说明，其中各个字段的内容如下：
### WBFaceErrorDomainParams

| Code（错误码） | Description（描述） | Reason（详细实际原因） |
|---------|---------|---------|
| 11000 | 传入参数为空    | 传入的xx为空| 
| 11001 | 传入的 keyLicence | 不可用  传入的 keyLicence 不可用| 
| 11002 | 报文加解密失败   | 报文加解密失败| 

### WBFaceErrorDomainLoginNetwork
| Code（错误码） | Description（描述） | Reason（详细实际原因） |
|---------|---------|---------|
|21100| 网络异常    |登录时网络异常（请求未到达后台）|
|21200  |网络异常   |登录时后台返回参数有误（请求到达后台）|


### WBFaceErrorDomainLoginServer
| Code（错误码） | Description（描述） | Reason（详细实际原因） |
|---------|---------|---------|
|其他错误码  |透传后台错误码    |例如签名问题等|

### WBFaceErrorDomainGetInfoNetwork
| Code（错误码） | Description（描述） | Reason（详细实际原因） |
|---------|---------|---------|
|31100| 网络异常    |获取活体类型/光线/意愿性表达资源，网络异常（请求未到达后台）|
|31200  |网络异常   |获取活体类型/光线/意愿性表达资源，后台返回参数有误（请求到达后台）|


### WBFaceErrorDomainNativeProcess
| Code（错误码） | Description（描述） | Reason（详细实际原因） |
|---------|---------|---------|
| 41000 | 用户取消  | 回到后台/单击 home/左上角/上传时左上角取消| 
| 41001 | 无法获取唇语数据  | 获取数字活体的数字有问题| 
| 41002 | 权限异常，未获取权限    | 相机| 
| 41003 | 相机运行中出错   | -| 
| 41004 | 视频录制中出错   | 不能存/启动失败/结束失败| 
| 41005 | 请勿晃动人脸，保持姿势   | 未获取到最佳图片| 
| 41006 | 视频大小不满足要求 | 视频大小不满足要求| 
| 41007 | 超时    | 预检测/动作活体| 
| 41008|    检测中人脸移出框外   | 活体/数字/反光| 
| 41009 | 光线活体本地错误  | -| 
| 41010 | 风险控制超出次数  | 用户重试太多次| 
| 41011 | 没有检测到读数声音 | 数字活体过程中没有发声| 
| 41012 | 初始化模型失败，请重试   | 初始化算法模型失败| 
| 41013 | 初始化 sdk 异常    | WbCloudFaceVerifySdk 未被初始化| 
| 41014 | 简单模式本地加密失败|   编码转换异常/加解密编码失败| 
| 41101 | 音频录制中出错   | 意愿性录音失败| 
| 41102|    没有检测到麦克风声音  | 意愿性检测音量过低| 
| 41103 | 播报音频文件加载失败    | 意愿性播放音频失败| 

### WBFaceErrorDomainCompareNetwork
| Code（错误码） | Description（描述） | Reason（详细实际原因） |
|---------|---------|---------|
| 51100 | 网络异常  | 对比时，网络异常（请求未到达后台）| 
| 51200 | 网络异常  | 对比时，后台返回参数有误（请求到达后台）| 

### WBFaceErrorDomainCompareServer
| Code（错误码） | Description（描述） | Reason（详细实际原因） |
|---------|---------|---------|
|其他错误码| 透传后台错误码 |-|

## 接入示例
权威库网纹图片比对、自带对比源对比接入示例：
```
# 在MainActivity中单击某个按钮的代码逻辑：
//先填好数据 
Bundle data = new Bundle();
WbCloudFaceVerifySdk.InputData inputData = new WbCloudFaceVerifySdk.InputData(
                faceId,
                agreementNo,
                openApiAppId,
                openApiAppVersion,
                openApiNonce,
                userId,
                userSign,
                verifyMode,
                keyLicence);
  data.putSerializable(WbCloudFaceContant.INPUT_DATA, inputData);

//设置选择的比对类型  默认为权威库网纹图片对比
//此处设置权威库网纹图片对比
  data.putString(WbCloudFaceContant.COMPARE_TYPE, WbCloudFaceContant.ID_CRAD);

//初始化 SDK，得到是否登录 SDK 成功的结果,由 WbCloudFaceVerifyLoginListener  返回登录结果
//【特别注意】建议对拉起人脸识别按钮做防止重复点击的操作
//避免用户快速点击导致二次登录，二次拉起刷脸等操作引起问题
WbCloudFaceVerifySdk.getInstance().initWillSdk(DemoActivity.this, data, new WbCloudFaceVerifyLoginListener() {
        @Override
        public void onLoginSuccess() {
                //登录成功，拉起 sdk 页面,由 FaceVerifyResultListener   返回刷脸结果
                WbCloudFaceVerifySdk.getInstance().startWbFaceVerifySdk(DemoActivity.this, new WbCloudFaceVerifyResultListener() {
                        @Override
                        public void onFinish(WbFaceVerifyResult result) {
                                if (result != null) {
                                        if (result.isSuccess()) {
                                                Log.d(TAG, "刷脸成功！");
                                        } else {
                                                Log.d(TAG, "刷脸失败！");
                                        }
                                }
                                //刷脸结束后，及时释放资源
                                WbCloudFaceVerifySdk.getInstance().release();
                        }
                });
        }
        @Override
        public void onLoginFailed(WbFaceError error) {
                Log.d(TAG, "登录失败！");
                //刷脸结束后，及时释放资源
                WbCloudFaceVerifySdk.getInstance().release();
        }
}); 

```
详细接入代码，请参考 SDK 附的 KnowYourCustomerDemo 工程。
 
