本文主要介绍如何快速地将腾讯云 IM SDK 集成到您的 Web 或者小程序项目中。
- 您可以通过 NPM 和 Script 方式将 IM SDK 集成到您的 Web 项目中，推荐使用 NPM 集成。
- 您可以通过 NPM 方式将 IM SDK 集成到您的小程序项目中。
- 您可以通过集成 SDK 上传插件，实现更快更安全的富文本消息资源上传，请参见 [集成 SDK 上传插件](https://cloud.tencent.com/document/product/269/52962)。

以下视频将帮助您快速了解如何将 IM SDK 集成到您的 Web 或者小程序项目中：
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/2545-43224?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

## 准备工作
- 已创建即时通信 IM 应用并获取 SDKAppID。
- 已获取密钥信息。


## 相关文档
- [一分钟跑通 Demo](https://cloud.tencent.com/document/product/269/36838)
- [IM SDK（小程序）TUIKit 运行](https://github.com/tencentyun/TIMSDK/tree/master/MiniProgram/TUIKit)
- [IM SDK（Web） Demo 运行](https://github.com/tencentyun/TIMSDK/tree/master/Web/Demo)
- [集成 SDK 上传插件（Web & 小程序）](https://cloud.tencent.com/document/product/269/52962)

## 集成 SDK


### NPM 集成（推荐）
在您的项目中使用 NPM 安装相应的 IM SDK 依赖。

#### **Web 项目**
```javascript
// IM Web SDK
// 从v2.11.2起，SDK 支持了 WebSocket，推荐接入；v2.10.2及以下版本，使用 HTTP
npm install tim-js-sdk --save
// 发送图片、文件等消息需要腾讯云即时通信 IM 上传插件
npm install tim-upload-plugin --save
```
>?若同步依赖过程中出现问题，请切换 npm 源后再次重试。
>```
>// 切换 cnpm 源
>npm config set registry http://r.cnpmjs.org/
>```
 
 在项目脚本里引入模块。
```
// 从v2.11.2起，SDK 支持了 WebSocket，推荐接入；v2.10.2及以下版本，使用 HTTP
import TIM from 'tim-js-sdk';
import TIMUploadPlugin from 'tim-upload-plugin';

let options = {
  SDKAppID: 0 // 接入时需要将0替换为您的即时通信 IM 应用的 SDKAppID
};
// 创建 SDK 实例，`TIM.create()`方法对于同一个 `SDKAppID` 只会返回同一份实例
let tim = TIM.create(options); // SDK 实例通常用 tim 表示

// 设置 SDK 日志输出级别，详细分级请参见 <a href="https://web.sdk.qcloud.com/im/doc/zh-cn//SDK.html#setLogLevel">setLogLevel 接口的说明</a>
tim.setLogLevel(0); // 普通级别，日志量较多，接入时建议使用
// tim.setLogLevel(1); // release 级别，SDK 输出关键信息，生产环境时建议使用

// 注册腾讯云即时通信 IM 上传插件
tim.registerPlugin({'tim-upload-plugin': TIMUploadPlugin});
```

#### **小程序项目**
```javascript
// IM 小程序 SDK
// 从v2.11.2起，SDK 支持了 WebSocket，推荐接入；v2.10.2及以下版本，使用 HTTP
npm install tim-wx-sdk --save
// 发送图片、文件等消息需要腾讯云 即时通信 IM 上传插件
npm install tim-upload-plugin --save
```
>?若同步依赖过程中出现问题，请切换 npm 源后再次重试。
>```
>// 切换 cnpm 源
>npm config set registry http://r.cnpmjs.org/
>```

 在项目脚本里引入模块，并初始化。
```
// 从v2.11.2起，SDK 支持了 WebSocket，推荐接入；v2.10.2及以下版本，使用 HTTP
import TIM from 'tim-wx-sdk';
import TIMUploadPlugin from 'tim-upload-plugin';

let options = {
  SDKAppID: 0 // 接入时需要将0替换为您的即时通信 IM 应用的 SDKAppID
};
// 创建 SDK 实例，`TIM.create()`方法对于同一个 `SDKAppID` 只会返回同一份实例
let tim = TIM.create(options); // SDK 实例通常用 tim 表示

// 设置 SDK 日志输出级别，详细分级请参见 <a href="https://web.sdk.qcloud.com/im/doc/zh-cn//SDK.html#setLogLevel">setLogLevel 接口的说明</a>
tim.setLogLevel(0); // 普通级别，日志量较多，接入时建议使用
// tim.setLogLevel(1); // release 级别，SDK 输出关键信息，生产环境时建议使用

// 注册腾讯云即时通信 IM 上传插件
tim.registerPlugin({'tim-upload-plugin': TIMUploadPlugin});
```

更详细的初始化流程和 API 使用介绍请参见 [SDK 初始化](https://web.sdk.qcloud.com/im/doc/zh-cn//SDK.html)。

### Script 集成
在您的项目中使用 script 标签引入 SDK，并初始化。

```html
<!-- tim-js.js 和 tim-upload-plugin.js 可以从 https://github.com/tencentyun/TIMSDK/tree/master/Web/Demo/sdk 获取 -->
<script src="./tim-js.js"></script>
<script src="./tim-upload-plugin.js"></script>
<script>
var options = {
  SDKAppID: 0 // 接入时需要将0替换为您的即时通信 IM 应用的 SDKAppID
};
// 创建 SDK 实例，`TIM.create()`方法对于同一个 `SDKAppID` 只会返回同一份实例
var tim = TIM.create(options);
// 设置 SDK 日志输出级别，详细分级请参见 setLogLevel 接口的说明
tim.setLogLevel(0); // 普通级别，日志量较多，接入时建议使用
// tim.setLogLevel(1); // release 级别，SDK 输出关键信息，生产环境时建议使用

// 注册腾讯云即时通信 IM 上传插件
tim.registerPlugin({'tim-upload-plugin': TIMUploadPlugin});

// 接下来可以通过 tim 进行事件绑定和构建 IM 应用
</script>
```

>?设置 SDK 日志输出级别，详细分级请参见 [setLogLevel 接口的说明](https://web.sdk.qcloud.com/im/doc/zh-cn//SDK.html#setLogLevel)。

更详细的初始化流程和 API 使用介绍请参见 [SDK 初始化](https://web.sdk.qcloud.com/im/doc/zh-cn//SDK.html)。

### 相关资源
- [SDK 更新日志](https://cloud.tencent.com/document/product/269/38492)
- [SDK 接口文档](https://web.sdk.qcloud.com/im/doc/zh-cn//SDK.html)
- [常见问题](https://web.sdk.qcloud.com/im/doc/zh-cn//tutorial-01-faq.html)
- [IM Web Demo](https://github.com/tencentyun/TIMSDK/tree/master/Web/Demo)
- [腾讯云即时通信 IM 上传插件下载地址](https://www.npmjs.com/package/tim-upload-plugin)


## 常见问题

**1. 小程序如果需要上线或者部署正式环境怎么办？**
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

