## APP 发布前确认事项   

## iOS：  

* 确认填写用户自己的 Bundle ID 和对应的发布证书。

* 请根据实际情况调整配置文件中的内容，[详情可见](https://developers.weixin.qq.com/doc/oplatform/Mobile_App/WeChat_Login/Development_Guide.html)，需要配置的内容如下：

  ```json
  {
    "WXAccessAppId": "",
    "TencentIotLinkAppkey": "请输入从物联网开发平台申请的 App key，正式发布前务必填写",
    "TencentIotLinkAppSecret": "请输入从物联网开发平台申请的 App Secret，App Secret 请保存在服务端，此处仅为演示，如有泄露概不负责",
    "XgAccessId": "",
    "XgAccessKey": "",
    "TencentMapSDKValue": "",
    "TencentIotLinkSDKDemoAppkey": ""
  }
  ```
  * 用户需要使用从物联网平台自建应用所获得的 **TencentIotLinkAppkey** 和 **TencentIotLinkAppSecret**，来替换 APP 中对应的字符串。
  * 用户需要使用从腾讯推送平台自建应用所获得的 **XgAccessId** 和 **XgAccessKey**，来替换 APP 中对应的字符串。
  * 用户需要使用从微信开发平台自建应用所获得的 **WXAccessAppId**，来替换 APP 中对应的字符串。

* 如果用户确认接入 Firebase，用户需要使用从 Firebase 官网自建应用获得 **GoogleService-Info.plist**，替换 APP 中对应的文件，如下图所示：   

  <img src="https://main.qcloudimg.com/raw/7c17279a720b92ffb875e1b7ed46e89c/image-20200622184506.png" alt="image-20200622184506"  width = "35%" height = "50%"  /> 
  
## Android：   

1、请根据实际情况调整 **app-config.json** 中的内容，app-config.json 位于项目的根目录，如截图所示位置。

<img src="https://main.qcloudimg.com/raw/9d8f86a5e9bff3a3a2bd639a0c0f32bf.png" alt="image-20200619141407513"  width = "35%" height = "50%"  />

app-config.json 需要配置的内容，如下：

```json
{
  "WXAccessAppId": "",
  "TencentIotLinkAppkey": "请输入从物联网开发平台申请的 App key，正式发布前务必填写",
  "TencentIotLinkAppSecret": "请输入从物联网开发平台申请的 App Secret，App Secret 请保存在服务端，此处仅为演示，如有泄露概不负责",
  "XgAccessId": "",
  "XgAccessKey": "",
  "TencentMapSDKValue": "",
  "TencentIotLinkSDKDemoAppkey": ""
}
```

* **TencentIotLinkAppkey** 和 **TencentIotLinkAppSecret** 请使用在物联网平台创建应用时生成的 **APP Key** 和 **APP Secret**。     

* **XgAccessId** 和 **XgAccessKey** 请使用在信鸽推送平台申请获得的 **AccessID** 和 **AccessKey**，[申请步骤](https://cloud.tencent.com/product/tpns/getting-started)。   

* **WXAccessAppId** 请使用在微信开放平台申请并获得的 **AppID**；若确认使用自定义的微信授权登录，需要在[微信开放平台](https://open.weixin.qq.com/)注册开发者帐号，创建移动应用，审核通过后，即可获得相应的 AppID 和 AppSecret，[申请步骤](https://developers.weixin.qq.com/doc/oplatform/Mobile_App/WeChat_Login/Development_Guide.html)。

  使用微信授权登录还需：

  - 将 *opensource_keystore.jks* 文件替换成自己的签名文件并给应用签字

  - 前往[微信开放平台](https://developers.weixin.qq.com/doc/oplatform/Downloads/Android_Resource.html)下载签名生成工具，使用该工具生成应用的数字签名(需要将该工具和应用同时安装到手机上，打开签名生成工具输入应用包名即可生成数字签名，如下图所示)

    <img src="https://main.qcloudimg.com/raw/e5734b5731d77e8b1e271cbd78bb5fcf.png" alt="image-20200619162858817" width = "40%" height = "40%" />

  - 将该数字签名和应用包名登记到微信开放平台，否则微信授权登录将不可用

  最后将配置项 **WXAccessAppId** 设置为在微信开放平台申请并获得的 **AppID**；***<u>同时请遵从官方建议自建微信接入服务器，保证 AppSecret 不被泄露</u>***。

* **TencentMapSDKValue** 请使用腾讯地图开放平台申请并获得的 **key**，[申请步骤](https://lbs.qq.com/mobile/androidLocationSDK/androidGeoGuide/androidGeoCreat)。



2、项目配置了 **Firebase** 插件

* 若用户确认使用 Firebase 功能，需通过 Firebase 官网创建应用并获取 **google-services.json**，将 google-services.json 文件放置在 app 目录下，如截图所示位置。

  <img src="https://main.qcloudimg.com/raw/76bf90532ea498a57a7280cf3ce5e165/image-20200619150459211.png" alt="image-20200619150459211"  width = "40%" height = "40%"  />

* 若不使用 Firebase 功能，注释图中标注的内容即可。

  <img src="https://main.qcloudimg.com/raw/d1e21091c93ad724d21e833263081919.png" alt="image-20200628100119804" style="zoom:50%;" />

  <img src="https://main.qcloudimg.com/raw/e6ce262011f9309c516b7ff27283417f.png" alt="image-20200628100329841" style="zoom:50%;" />

  <img src="https://main.qcloudimg.com/raw/be98955a98abc5562bf45a1aaac127f5.png" alt="image-20200628100531109" style="zoom:50%;" />