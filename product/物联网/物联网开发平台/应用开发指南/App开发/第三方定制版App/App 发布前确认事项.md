

## iOS  

* 确认填写用户自己的 Bundle ID 和对应的发布证书。
* 根据实际情况调整配置文件中的内容，需要配置的内容可参考[ App 参数写入配置文件](https://cloud.tencent.com/document/product/1081/45902#app-.E5.8F.82.E6.95.B0.E5.86.99.E5.85.A5.E9.85.8D.E7.BD.AE.E6.96.87.E4.BB.B6)，获取到相应的 ID 和 key 值替换 App 中的字符串。
* 如果用户确认接入 Firebase，用户需要使用从 Firebase 官网自建应用获得 **GoogleService-Info.plist**，替换 App 中 [GoogleService-Info.plist](https://github.com/tencentyun/iot-link-ios/blob/master/Source/LinkApp/Supporting%20Files/GoogleService-Info.plist) 文件。  
 

## Android   
1. 请根据实际情况调整 **app-config.json** 中的内容。app-config.json 需要配置的内容，如下所示。
```json
{
  "TencentIotLinkAppkey": "请输入从物联网开发平台申请的 App Key，正式发布前务必填写",
  "TencentIotLinkAppSecret": "请输入从物联网开发平台申请的 App Secret，App Secret 请保存在服务端，此处仅为演示，如有泄露概不负责",
  "WXAccessAppId": ""
}
```

 - **TencentIotLinkAppkey** 和 **TencentIotLinkAppSecret** 请使用在物联网平台创建应用时生成的[ App Key 和 App Secret](https://cloud.tencent.com/document/product/1081/45901#.E8.8E.B7.E5.8F.96-app-key-.E5.92.8C-app-secret)，TencentIotLinkAppSecret 存放在用户自建后台服务器中，详情可参见 [应用端 API 简介](https://cloud.tencent.com/document/product/1081/40773)。 
 - **WXAccessAppId** 请使用在微信开放平台申请并获得的 **AppID**；若确认使用自定义的微信授权登录，需要在 [微信开放平台](https://open.weixin.qq.com/) 注册开发者帐号，创建移动应用，审核通过后，即可获得相应的 [AppID 和 AppSecret](https://developers.weixin.qq.com/doc/oplatform/Mobile_App/WeChat_Login/Development_Guide.html)。
 使用微信授权登录还需：
    1. 将 `opensource_keystore.jks`文件替换成自己的签名文件并给应用签字。
    2.  前往 [微信开放平台](https://developers.weixin.qq.com/doc/oplatform/Downloads/Android_Resource.html) 下载签名生成工具，使用该工具生成应用的数字签名(需要将该工具和应用同时安装到手机上，打开签名生成工具输入应用包名即可生成数字签名)
    3. 将该数字签名和应用包名登记到微信开放平台，否则微信授权登录将不可用。
    4. 最后将配置项 WXAccessAppId 设置为在微信开放平台申请并获得的 AppID；**同时请遵从官方建议自建微信接入服务器，保证 AppSecret 不被泄露**。

2. 项目配置 **Firebase** 插件。
 - 若用户确认使用 Firebase 功能，需通过 Firebase 官网创建应用并获取 **google-services.json**，替换项目中的 [google-services.json](https://github.com/tencentyun/iot-link-android/blob/master/app/google-services.json) 文件。
 - 若不使用 Firebase 功能，需要在以下文件中注释掉对应依赖。 
    - 在项目级 [build.gradle](https://github.com/tencentyun/iot-link-android/blob/master/build.gradle) 中注释掉以下三个依赖项。
 ```
dependencies {
//        classpath 'com.google.gms:google-services:4.3.3'
//        classpath 'com.google.firebase:firebase-crashlytics-gradle:2.1.1'
//        classpath 'com.google.firebase:perf-plugin:1.3.1'
}
```
    - 在应用级 [build.gradle](https://github.com/tencentyun/iot-link-android/blob/master/app/build.gradle) 中注释掉以下三个应用插件和三个依赖项。
```
//apply plugin: 'com.google.gms.google-services'
//apply plugin: 'com.google.firebase.crashlytics'
//apply plugin: 'com.google.firebase.firebase-perf'
dependencies {
//    implementation 'com.google.firebase:firebase-analytics-ktx:17.4.3'
//    implementation 'com.google.firebase:firebase-crashlytics:17.0.1'
//    implementation 'com.google.firebase:firebase-perf:19.0.7'
}
```
