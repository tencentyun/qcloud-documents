本文介绍开发者如何基于物联网开发平台 APP SDK（下称 SDK）构建自主品牌APP，通过 SDK 使用平台提供的用户管理，设备管理等能力。

## App 源码获取   

- iOS 版本 App 可通过 [腾讯连连-iOS](https://github.com/tencentyun/iot-link-ios/tree/master/Source/LinkApp) 下载源码 。
- Android 版本 App 可通过 [腾讯连连-Android](https://github.com/tencentyun/iot-link-android/tree/master/app) 下载源码 。      



## 创建应用      

1. 登录 [物联网智能视频服务（消费版）控制台](https://console.cloud.tencent.com/iot-video)，进入**应用开发**。
2. 新建应用，创建应用成功后，即可获取系统自动生成的 AppKey 与 AppSecret。
![](https://qcloudimg.tencent-cloud.cn/raw/aac6b59c869ff824d181c928c5ceb892.png)
3. 将App Key写入 [配置文件](https://cloud.tencent.com/document/product/1081/67511#app-.E5.8F.82.E6.95.B0.E5.86.99.E5.85.A5.E9.85.8D.E7.BD.AE.E6.96.87.E4.BB.B6), 将App Secret保存在 [自建后台](https://cloud.tencent.com/document/product/1081/40773), 将 appapi 调用由设备端发起切换为由自建后台服务发起。      

## 搭建后台服务, 将 App API 调用由设备端发起切换为由自建后台服务发起  

关于应用端 API，请参见 [应用端 API 简介](https://cloud.tencent.com/document/product/1081/40773) 。

>!  登录前所使用的 API URL 为 `https://iot.cloud.tencent.com/api/exploreropen/appapi`，不建议在设备端调用，需要替换为自建的后台服务，以避免密钥的泄漏。
>-   api/studioapp/\* 为公版 App 专用，OEM 的 App 使用的是应用端 API（api/exploreropen/），当在 [App 参数写入配置文件](https://cloud.tencent.com/document/product/1081/67511#E5.8F.82.E6.95.B0.E5.86.99.E5.85.A5.E9.85.8D.E7.BD.AE.E6.96.87.E4.BB.B6) 中配置 TencentIotLinkAppkey 后, api/studioapp 调用将自动切换为应用端 API 调用。
>-   App API （api/exploreropen/appapi）请在自建后台进行调用，Token API（api/exploreropen/tokenapi）可安全在设备端调用。

- iOS 版本 可通过 [TIoTAppEnvironment.m](https://github.com/tencentyun/iot-link-ios/blob/master/Source/LinkApp/Classes/AppConfig/APPContext/TIoTAppEnvironment.m) 的 selectEnvironmentType 方法中设置此 API 。
**登录前所使用的 API URL** 在 **environment.oemAppApi** 配置，**请务必替换成自建的后台服务地址。**
```
- (void)selectEnvironmentType {
TIoTAppConfigModel *model = [TIoTAppConfig loadLocalConfigList];
TIoTCoreAppEnvironment *environment = [TIoTCoreAppEnvironment shareEnvironment];
[environment setEnvironment];
environment.appKey = model.TencentIotLinkAppkey;
environment.appSecret = model.TencentIotLinkAppSecret;
// 请在 [environment setEnvironment]; 之后设置 oemAppApi 以免被覆盖。
environment.oemAppApi = @"需要替换为自建后台服务地址";
}
```
[TIoTCoreAppEnvironment.m](https://github.com/tencentyun/iot-link-ios/blob/master/Source/SDK/LinkCore/QCFoundation/TIoTCoreAppEnvironment.m) 的 setEnvironment方法中默认 API 配置说明。
```Objective-C
- (void)setEnvironment {
//公版&开源体验版使用  当在 app-config.json 中配置 TencentIotLinkAppkey TencentIotLinkAppSecret 后，将自动切换为 OEM 版本。
self.studioBaseUrl = @"https://iot.cloud.tencent.com/api/studioapp";
self.studioBaseUrlForLogined = @"https://iot.cloud.tencent.com/api/studioapp/tokenapi";         
//OEM App 使用
self.oemAppApi = @"https://iot.cloud.tencent.com/api/exploreropen/appapi"; // 需要在 TIoTAppEnvironment.m 的 -selectEnvironmentType: 中替换为自建后台服务地址。
self.oemTokenApi = @"https://iot.cloud.tencent.com/api/exploreropen/tokenapi";  // 可安全在设备端调用。         
self.wsUrl = @"wss://iot.cloud.tencent.com/ws/explorer";        
self.h5Url = @"https://iot.cloud.tencent.com/explorer-h5";
}
```
- Android 版本 可通过 [HttpRequest](https://github.com/tencentyun/iot-link-android/blob/master/app/src/main/java/com/tencent/iot/explorer/link/kitlink/util/HttpRequest.kt) 中设置API 。
**登录前所使用的 API URL** 在 **OEM_APP_API** 配置，**请务必替换成自建的后台服务地址。**

   ```
  /*
    接口请求文件
   */
     class HttpRequest private constructor() {
     companion object {              
     // 公版&开源体验版使用  当在 app-config.json 中配置 TencentIotLinkAppkey TencentIotLinkAppSecret 后，将自动切换为 OEM 版本。
     const val STUDIO_BASE_URL = "https://iot.cloud.tencent.com/api/studioapp"
     const val STUDIO_BASE_URL_FOR_LOGINED = "https://iot.cloud.tencent.com/api/studioapp/tokenapi"     
     // OEM App 使用
     const val OEM_APP_API = "https://iot.cloud.tencent.com/api/exploreropen/appapi" // 需要替换为自建后台服务地址
     const val OEM_TOKEN_API = "https://iot.cloud.tencent.com/api/exploreropen/tokenapi"  // 可安全在设备端调用。     
     const val APP_COS_AUTH = "https://iot.cloud.tencent.com/api/studioapp/AppCosAuth"
     const val BUSI_APP = "studioapp"
     const val BUSI_OPENSOURCE = "studioappOpensource"
     }
  }
   ```


## App Demo、SDK Demo 和 SDK 的关系   

#### iOS

工程中已经包含 [App Demo](https://github.com/tencentyun/iot-link-ios/tree/master/Source/LinkApp)、[SDK Demo](https://github.com/tencentyun/iot-link-ios/tree/master/Source/LinkSDKDemo) 和 [SDK](https://github.com/tencentyun/iot-link-ios/tree/master/Source/SDK/LinkCore)，无需额外引入。

#### Android

工程中已经包含 [App Demo](https://github.com/tencentyun/iot-link-android/tree/master/app) 、[SDK Demo](https://github.com/tencentyun/iot-link-android/tree/master/sdkdemo)  和 [SDK](https://github.com/tencentyun/iot-link-android/tree/master/sdk)，无需额外引入。

