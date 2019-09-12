## 内容介绍

如果您希望给某些房间加入进房的条件限制（e.g. 有些房间需要是会员才能进入），而您又担心在客户端限制很容易遭遇破解问题，那么可以考虑**开启房间权限控制**。

## 支持的平台

| iOS | Android | Mac OS | Windows | 微信小程序 | Chrome浏览器|
|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
|     ✔  |    ✔    |    ✔   |    ✔    |   ✔    |   ✔    |

## PrivateMapKey

### 作用介绍
privateMapKey 是 TRTCParamEnc 中的一个可选字段，它的作用是让腾讯云检查用户是否拥有进入指定房间的权限。

![](https://main.qcloudimg.com/raw/108b2c9e60cf28c24c2a42f5f2ce0110.png)

### 与UserSig的区别

- [**UserSig**](https://cloud.tencent.com/document/product/647/17275) 
TRTCParamEnc 的必选项，作用是检查当前用户是否有权使用 TRTC 云服务，用于防止攻击者盗用您的 sdkappid 账号内的流量。

- **privateMapKey**
TRTCParamEnc 的非必选项，作用是检查当前用户是否有权进入指定roomid的房间，当您的业务需要对用户进行身份区分的时候才有必要开启。

 而且，您在 App 端直接判定当前用户是否有权进入指定房间也是可以的，privateMapKey 的作用仅仅是做的更安全，它可以避免客户端被破解后，出现“非会员也能进高等级房间”的破解版本。
 
## 如何开启
 - **在腾讯云实时音视频[控制台](https://console.cloud.tencent.com/rav)开启房间权限控制。**
 ![](https://main.qcloudimg.com/raw/4d15eb603459c6af1ea2c0af1c31450c.png)
 
 - **在您的服务器端计算 privateMapKey。**
  由于 privateMapKey 的价值就是为了防止客户端被逆向破解，从而出现“非会员也能进高等级房间”的破解版本，所以它只适合在您的后台服务器计算再返回客户端。
  我们提供了 java、php 和 nodejs 三个版本的 PrivateMapKey 计算代码，您可以直接下载并集成到您的服务端。

| 语言版本 | 关键函数 | 下载链接 |
|:---------:|:---------:|:---------:|
| java | `genPrivateMapKey` | [Github](https://github.com/TencentVideoCloudMLVBDev/usersig_server_source/tree/master/java)|
| php | `genPrivateMapKey` | [Github](https://github.com/TencentVideoCloudMLVBDev/usersig_server_source/tree/master/php)|
| nodejs | `genPrivateMapKey` | [Github](https://github.com/TencentVideoCloudMLVBDev/usersig_server_source/tree/master/nodejs)|

 - **将 privateMapKey 下发到您的 App 并用来设置 TRTCParamEnc 的 privateMapKey 参数。**

## 常见问题
 - **线上的房间都进不去了？**
 房间权限控制一旦开启后，当前 sdkappid 下的房间就需要在 TRTCParamEnc 中设置 privateMapKey 才能进入，所以如果您线上业务正在运营中，并且线上版本并没有加入 privateMapKey 的相关逻辑，请不要开启此开关。

