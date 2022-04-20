[](id:Q1)
### uni-app  同时支持 Android、iOS 和微信小程序平台，IM SDK 如何选择？
请选择 `tim-wx-sdk` ，npm 安装或者静态引入：
```javascript
    // 从v2.11.2起，SDK 支持了 WebSocket，推荐接入；v2.10.2及以下版本，使用 HTTP
	npm install tim-wx-sdk@latest --save  
	import TIM from 'tim-wx-sdk';
	// 创建 SDK 实例，`TIM.create()`方法对于同一个 `SDKAppID` 只会返回同一份实例
	uni.$TUIKit = TIM.create({
		SDKAppID: 0  // 接入时需要将0替换为您的即时通信 IM 应用的 SDKAppID
	});
	
	// 设置 SDK 日志输出级别，详细分级请参见 setLogLevel 接口的说明
	uni.$TUIKit.setLogLevel(0); // 普通级别，日志量较多，接入时建议使用
	// uni.$TUIKit.setLogLevel(1); // release 级别，SDK 输出关键信息，生产环境时建议使用
```
如果您的项目需要关系链功能，请使用 `tim-wx-friendship.js`：
```javascript
	import TIM from 'tim-wx-sdk/tim-wx-friendship.js';
```
>?
>- **为了 uni-app 更好地接入使用 tim，快速定位和解决问题，请勿修改 uni.$TUIKit 命名，如果您已经接入 tim ，请将 uni.tim 修改为 uni.$TUIKit。**
>- 请将 IM SDK 升级到 [2.15.0](https://cloud.tencent.com/document/product/269/38492)，该版本支持了 iOS 语音播放。
>- 若同步依赖过程中出现问题，请切换 npm 源后再次重试。
```javascript
	切换 cnpm 源
	>npm config set registry http://r.cnpmjs.org/
	>
	>
```

[](id:Q2)
### 如何上传图片、视频、语音消息等富媒体消息？
请使用 `cos-wx-sdk-v5`：
```javascript
    // 发送图片、语音、视频等消息需要 cos-wx-sdk-v5 上传插件
	npm install cos-wx-sdk-v5@0.7.11 --save
	import COS from "cos-wx-sdk-v5";
	// 注册 COS SDK 插件
	uni.$TUIKit.registerPlugin({
		'cos-wx-sdk': COS
	});
```

[](id:Q3)
###  uni-app  打包 iOS 语音消息无法播放怎么办？
  请将 IM SDK 升级到 [2.15.0](https://cloud.tencent.com/document/product/269/38492)，该版本支持了 iOS 语音消息播放。

[](id:Q4)
### uni-app  打包 app 发送语音消息时间显示错误怎么办？
   uni-app 打包 app，`recorderManager.onStop` 回调中没有 `duration` 和 `fileSize`，需要用户自己补充 duration 和 fileSize。
- **通过本地起定时器记录时间，计算出 duration。**
- **本地计算文件大小，fileSize ＝ (音频码率) x 时间长度(单位：秒) / 8，粗略估算。**
详细代码请参见 [uni-app TUIKit](https://github.com/tencentyun/TIMSDK/tree/master/uni-app)。
>!语音消息对象中必须包括 `duration` 和 `fileSize`，如果没有 `fileSize`，语音消息时长是一串错误的数字

[](id:Q5)
### video 视频消息层级过高无法滑动怎么办？
 在项目中通过视频图片代替，没有直接渲染 `video`，在播放时渲染的方式规避了层级过高问题。
 详细代码请参见 [uni-app TUIKit](https://github.com/tencentyun/TIMSDK/tree/master/uni-app)。
>!请参见官方 [原生组件说明](https://uniapp.dcloud.io/component/native-component)。

[](id:Q6)
### 微信小程序环境在真机预览下报系统错误，体积过大怎么办？
运行时请勾选代码压缩，运行到小程序模拟器>运行时是否压缩代码。

[](id:Q7)
### 引入原生音视频插件报以下错怎么办？
![](https://qcloudimg.tencent-cloud.cn/raw/e68ad1caf6be5d7f551a3b765c4aca53.png)
根据 uni-app [原生插件调试](https://ask.dcloud.net.cn/article/35412) 制作 [自定义基座](https://ask.dcloud.net.cn/article/35115)
![](https://qcloudimg.tencent-cloud.cn/raw/7758e1f3b5214a1ecd5a1aac46445ac3.png)

[](id:Q8)
### 微信小程序如果需要上线或者部署正式环境怎么办？
请在**微信公众平台**>**开发**>**开发设置**>**服务器域名**中进行域名配置：

将以下域名添加到 **request 合法域名**：

从v2.11.2起，SDK 支持了 WebSocket，WebSocket 版本须添加以下域名：

| 域名 | 说明 |  是否必须 |
|:-------:|---------|----|
|`wss://wss.im.qcloud.com`| Web IM 业务域名 | 必须|
|`wss://wss.tim.qq.com`| Web IM 业务域名 | 必须|
|`https://web.sdk.qcloud.com`| Web IM 业务域名 | 必须|
|`https://webim.tim.qq.com` | Web IM 业务域名 | 必须|

v2.10.2及以下版本，使用 HTTP，HTTP 版本须添加以下域名：

| 域名 | 说明 |  是否必须 |
|:-------:|---------|----|
|`https://webim.tim.qq.com` | Web IM 业务域名 | 必须|
|`https://yun.tim.qq.com` | Web IM 业务域名 | 必须|
|`https://events.tim.qq.com` | Web IM 业务域名 | 必须|
|`https://grouptalk.c2c.qq.com`| Web IM 业务域名 | 必须|
|`https://pingtas.qq.com` | Web IM 统计域名 | 必须|

将以下域名添加到 **uploadFile 合法域名**：

| 域名 | 说明 |  是否必须 |
|:-------:|---------|----|
|`https://cos.ap-shanghai.myqcloud.com` | 文件上传域名 | 必须|

将以下域名添加到 **downloadFile 合法域名**：

| 域名 | 说明 |  是否必须 |
|:-------:|---------|----|
|`https://cos.ap-shanghai.myqcloud.com` | 文件下载域名 | 必须|

[](id:QQ)
### 技术咨询
了解更多详情您可 QQ 咨询：<dx-tag-link link="#QQ" tag="技术交流群">309869925</dx-tag-link>

