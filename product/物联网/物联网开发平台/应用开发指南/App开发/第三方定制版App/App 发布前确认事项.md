## iOS

1. 确认填写用户自己的 Bundle ID 和 对应发布证书。   
2. 用户需要使用从 [物联网开发平台](https://console.cloud.tencent.com/iotexplorer) 自建应用所获得的 **TencentIotLinkAppkey** 和 **TencentIotLinkAppSecrecy**，来替换 App Demo 中相对应的字符串，如下图所示：
	![](https://main.qcloudimg.com/raw/f7d36664333f13ddf725bd8bf078edaf.png)
3. 用户需要使用从 [腾讯推送平台](https://console.cloud.tencent.com/tpns) 自建应用所获得的 **XgAccessId** 和 **XgAccessKey**，来替换 App Demo 中相对应的字符串，如下图所示：
![](https://main.qcloudimg.com/raw/3eb506a9945405c92a367eecd2ff9062.png)
4. 用户需要使用从 [微信开放平台](https://open.weixin.qq.com/cgi-bin/frame?t=home/app_tmpl&lang=zh_CN) 自建应用所获得的 **WXAccessAppId**，来替换 App Demo 中相对应的字符，详情可参见 [移动应用微信登录开发指南](https://developers.weixin.qq.com/doc/oplatform/Mobile_App/WeChat_Login/Development_Guide.html)。
![](https://main.qcloudimg.com/raw/e96694bd1962970c785d1b1fcd68b51b.png)
5. 如果用户确认接入 Firebase，用户需要使用从 Firebase 官网自建应用获得 **GoogleService-Info.plist**，替换 App Demo 中原有相对应的文件，如下图所示：<br>
  <img src="https://main.qcloudimg.com/raw/7c17279a720b92ffb875e1b7ed46e89c/image-20200622184506.png" alt="image-20200622184506" style="zoom:85%;" />




## Android

1. 请根据实际情况调整 **config.json** 中的内容，config.json 位于项目的根目录，如下截图所示位置：
<img src="https://main.qcloudimg.com/raw/49cd7841a58e80f80db1dbf43e6f36e2/image-20200619141407513.png" alt="image-20200619141407513" style="zoom: 67%;" /><br>
config.json 需要配置的内容，如下图所示：
![](https://main.qcloudimg.com/raw/35bbf3f276f93336136572bdc6a1d7fa.jpg)
	- **TencentIotLinkAppkey** 和 **TencentIotLinkAppSecrecy** 请使用在物联网平台创建应用时生成的 **App Key** 和 **App Secret**。     
	- **XgAccessId** 和 **XgAccessKey** 请使用在信鸽推送平台申请获得的 **AccessID** 和 **AccessKey**，详情可见 [腾讯移动推送入门](https://cloud.tencent.com/product/tpns/getting-started)。   
	- **WXAccessAppId** 请使用在微信开放平台申请并获得的 **AppID**；可通过在微信开放平台注册开发者帐号，创建移动应用，审核通过后，即可获得相应的 AppID 和 AppSecret，详情可参见 [移动应用微信登录开发指南](https://developers.weixin.qq.com/doc/oplatform/Mobile_App/WeChat_Login/Development_Guide.html)。

 使用微信授权登录还需：
  - 将 **opensource_keystore.jks** 文件替换成自己的签名文件并给应用签字。
  - 前往 [微信开放平台](https://developers.weixin.qq.com/doc/oplatform/Downloads/Android_Resource.html) 下载签名生成工具，使用该工具生成应用的数字签名（需要将该工具和应用同时安装到手机上，打开签名生成工具输入应用包名即可生成数字签名，如下图所示）。
    <img src="https://main.qcloudimg.com/raw/b83597a8f1c676d8cd6312cf2694153b/image-20200619162858817.png" alt="image-20200619162858817" style="zoom: 33%;" />
  - 将该数字签名和应用包名登记到微信开放平台，否则微信授权登录将不可用。
 - **TencentMapSDKValue** 请使用腾讯地图开放平台申请并获得的 **key**，详情可参见 [创建工程](https://lbs.qq.com/mobile/androidLocationSDK/androidGeoGuide/androidGeoCreat)。

2. 项目配置了 **Firebase** 插件。
 - 若用户确认使用 Firebase 功能，需通过 Firebase 官网创建应用并获取 **google-services.json**；将 google-services.json 文件放置在 app 目录下，如截图所示位置：<br>
		<img src="https://main.qcloudimg.com/raw/76bf90532ea498a57a7280cf3ce5e165/image-20200619150459211.png" alt="image-20200619150459211" style="zoom:67%;" /><br>
 - 若不使用 Firebase 功能，请注释截图中标注的内容即可，如下图所示：<br>
		<img src="https://main.qcloudimg.com/raw/18586d6e1d6a46b3be59478f3efcee82/image-20200619150752594.png" alt="image-20200619150752594" style="zoom: 50%;" />
		<img src="https://main.qcloudimg.com/raw/47bdd7ccf15ad948b26617b9fb5afe6a/image-20200619151433681.png" alt="image-20200619151433681" style="zoom: 50%;" /><br>
		<img src="https://main.qcloudimg.com/raw/07864363b6d518597bd6857c55516265/image-20200619151507503.png" alt="image-20200619151507503" style="zoom: 50%;" />
