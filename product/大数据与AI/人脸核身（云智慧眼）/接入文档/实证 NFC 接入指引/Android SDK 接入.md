## 开发准备
CPU 平台设置
目前 SDK 支持 armeabi，armeabi-v7a，arm64-v8a，x86， x86_64平台，为了防止在其他 CPU 平台上 SDK Crash，我们建议在您的 App 的 build.gradle 里加上 abiFilter，如下所示：
```
defaultConfig {
    ndk {
          //设置支持的so库框架
          abiFilters 'armeabi-v7a'，'armeabi'，'arm64-v8a'，'x86'，'x86_64'
     }
}
```

## 配置流程
### 1. 接入配置
云 NFC SDK（WbCloudNfcSdk）最低支持到 **Android API 14: Android 4.0(ICS**) ，请在构建项目时注意。
云 NFC SDK 将以 AAR 文件的形式提供。另外 OCR SDK 同时需要依赖云公共组件 WBCloudNormal，同样也是以 AAR 文件的形式提供。
需要添加下面文档中所示的依赖（将提供的 AAR 文件加入到 App 工程的 libs 文件夹下面，
并且在 **build.gradle** 中添加下面的配置）：

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
        //1. 云NFC SDK
        implementation(name: 'WbCloudNfcSdk-pro-v2.0.0-1fec32a', ext: 'aar')
        //2.云公共组件
        implementation(name: 'WbCloudNormal-v5.1.3-90776e2', ext: 'aar')    }
```

### 2. 混淆配置
云 NFC 产品的混淆规则，对接入方而言，只需加载云公共组件的混淆规则。
您可以将 SDK 中的` txkyc-cloud-normal-consumer-proguard-rules.pro` 拷贝到主工程根目录下，然后通过` -include txkyc-cloud-normal-consumer-proguard-rules.pro `加入到您的混淆文件中。

## 接口调用
1. 标准模式 SDK 接口调用方法
SDK 代码调用的入口为 **com.tencent.cloud.huiyansdknfc.WbCloudNfcSDK** 这个类。
```
public class WbCloudNfcSDK{

/**
* 该类为一个单例，需要先获得单例对象再进行后续操作
   */
       public static synchronized WbCloudNfcSDK getInstance() {
       //    ...
       }
/**
* 在使用SDK前先初始化，传入需要的数据data
*由 nfcLoginListener返回是否登录SDK成功
* 关于传入数据data见后面的说明
*/
public void init(Context context，Bundle data，NfcLoginListener nfcLoginListerner){
//    ...
}
   /**
     * 登录成功后，调用此函数拉起sdk页面
     * @param context                  拉起SDK的上下文
     * @param nfcResultListener      返回到第三方的接口
     */
    Public void startActivityForNfc(Context context，NfcResultListener){
    // ...
 }
/**
  * 登录回调接口
  */
public interface NfcLoginListener {
        void onLoginSuccess();
        void onLoginFailed(String errorCode，String errorMsg);
    }

/**
  * 退出SDK，返回第三方的回调，同时返回NFC识别结果
  */
public interface NfcResultListener{
        /**
         * @RARAM wbNfcResult   SDK返回的NFC识别结果 
         */
        void onFinish(WBNfcResult wbNfcResult);
}
```
WbCloudNfcSdk.init() 的第二个参数用来传递数据.可以将参数打包到 data(Bundle) 中，必须传递的参数包括：
```
//这些都是WbCloudNfcSdk.InputData对象里的字段，是需要传入的数据信息
String orderNo;  //订单号，字母/数字组成的字符串
String openApiAppId;  //APP_ID 
String openApiAppVersion;  //openapi  Version
String openApiNonce; //32位随机字符串
String openApiUserId; //user id
String openApiSign; //签名信息
String openOcrCertId; //ocrCertId
```
以上参数被封装在 WbCloudNfcSdk.InputData 对象中（它是一个 Serializable 对象）。

2. 登录接口
```
/**
  * 登录回调接口
  */
public interface NfcLoginListener {
        void onLoginSuccess();//登录成功
          /**
           * @PARAM errorCode 登录失败错误码
           * @PARAM errorMsg  登录失败错误信息
           */        
         void onLoginFailed(String errorCode，String errorMsg);
    }
```

3. 返回第三方接口
```
/**
  * 退出SDK，返回第三方的回调，同时返回NFC识别结果
  */
public interface NfcResultListener{
        /**
         * 退出SDK，返回第三方的回调，同时返回NFC识别结果
         * @param wbNfcResult   返回NFC 识别结果
       */
        void onFinish(WBNfcResult wbNfcResult);
}
```

### NFC 识别结果类
NFC 识别结果，封装在 WBNfcResult 类中，该类属性如下所示：

```
     public String code;//识别结果的code
     public String message; //识别结果的msg
     public String orderNo;//识别结果的订单号
     public String ocrCertId;//订单结果的ocrCertId
     public String reqId; //订单结果的reqId

```

### 接口参数说明
InputData 是用来给 SDK 传递一些必须参数所需要使用的对象（WbCloudOcrSdk.init() 的第二个参数），合作方需要往里塞入 SDK 需要的一些数据以便启动 OCR SDK。
其中 InputData 对象中的各个参数定义如下表，请合作方按下表标准传入对应的数据。

| 参数 | 说明 | 类型 |长度 | 是否必填 |
|---------|---------|---------|---------|---------|
| orderNo| 订单号| String| 32| 必填，合作方订单的唯一标识，字母/数字组成的字符串| 
| openApiAppId| 业务流程唯一标识，即 wbappid，可参考 [获取 WBappid ](https://cloud.tencent.com/document/product/1007/49634)指引在人脸核身控制台内申请| String| 8| 必填| 
| openApiAppVersion| 接口版本号| String| 20| 必填，默认填 1.0.0|
| openApiNonce| 32位随机字符串| String| 32| 必填，每次请求需要的一次性 nonce| 
| openApiUserId | User Id| String| 30| 必填，每个用户唯一的标识| 
| openApiSign| 合作方后台服务器通过 ticket 计算出来的签名信息| String| 40| 必填| 
| openApiOcrCertId| 合作方后台服务器通过 ticket 计算出来的 ocrCertId| String| 40| 必填| 


### 个性化参数设置
WbCloudOcrSdk.init() 里 Bundle data，除了必须要传的 InputData 对象（详情见上节）之外，还可以由合作方传入一些个性化参数，量身打造更契合自己 App 的 SDK。如果合作方未设置这些参数，则以下所有参数按默认值设置。

## 错误码描述
| 终端返回错误码| 描述 | 
|---------|---------|
| UNABLE_SUPPORT_NFC_ERROR  = "600100"; | 设备不支持 | 
| USER_CANCEL_NFC_ERROR =" 600101 "| 用户取消操作| 
| ILLEGAL_PARAM_ERROR =" 600102 ";| 传入的参数不合法| 
| RECOGNISE_TIME_OUT =" 600103 ";| 识别超时| 
| NO_NET_ERROR =" 600104 ";| 网络不给力| 
| DECODE_ENMSG_ERROR =" 600105 ";| 解码异常| 
| INIT_NFC_ERROR =" 600106 ";| 初始化 NFC SDK 出错| 

## 接入示例

```
# 在 合作方的页面中单击某个按钮的代码逻辑：
//先填好数据 
  Bundle data = new Bundle();
        WbCloudNfcSDK.InputData inputData = new WbCloudNfcSDK.InputData(
                orderNo，
                openApiAppId，
                openApiAppVersion，
                openApiNonce，
                openApiUserId，
                openApiSign，
 openApiOcrCertId);
        data.putSerializable(WbCloudOcrSDK.INPUT_DATA，inputData);
    //个性化参数设置，可以不设置，不设置则为默认选项。
    //此处均设置为和默认设置不同
    data.putLong(WbCloudNfcSDK.NFC_TIME, 60000);//识别超时时间。身份证默认20s,回乡证默认60s。
    data.putString(WbCloudNfcSDK.NFC_TYPE, "3");//1表示身份证，3表示回乡证。默认身份证
      //1.初始化 SDK，得到是否登录 SDK成功的回调结果，请在主线程中调用此接口。
        WbCloudNfcSDK.getInstance().init(MainActivity.this，data，new WbCloudNfcSDK.NfcLoginListener() {
            @Override
            public voidonLoginSuccess() {  
             //2.登录成功，拉起 SDK页面。请在主线程中调用此接口。
        WbCloudNfcSDK.getInstance().startActivityForNfc(MainActivity.this，
            new  WbCloudNfcSDK.WBNfcResultListener() {  //返退出 SDK 回调接口
                    @Override
                    public voidonFinish(WBNfcResult wbNfcResult) {
           // resultCode为0，则NFC识别成功；否则识别失败
               if ("0".equals(wbNfcResult.code)) {      
//识别成功后，可以拿wbNfcResult.reqId去查询身份证结果
               WLogger.d(TAG，"识别成功，NFC的结果是:"+wbNfcResult.toString());
               }else{  // 
               WLogger.d(TAG，"NFC识别失败 code="+wbNfcResult.code+" message="+wbNfcResult.message);
               }
  });
}              
@Override
public void onLoginFailed(String errorCode，String errorMsg) {
if(errorCode.equals(ErrorCode.ILLEGAL_PARAM_ERROR)) {
Toast.makeText(MainActivity.this，"传入参数有误！" + errorMsg，Toast.LENGTH_SHORT).show();
} else {
Toast.makeText(MainActivity.this，"登录 NFC SDK 失败！" + "errorCode= " + errorCode + " ;errorMsg=" + errorMsg，Toast.LENGTH_SHORT).show();
}
}
})
```
详细接入代码，请参考 SDK 附的 wbcloudnfcdemo 工程。
