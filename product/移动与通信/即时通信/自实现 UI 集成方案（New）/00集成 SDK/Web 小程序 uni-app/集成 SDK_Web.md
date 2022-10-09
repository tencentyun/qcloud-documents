本文主要介绍如何快速将腾讯云即时通信 IM SDK 集成到您的 Web、小程序、uni-app 项目中。

## 集成 SDK

- 通过 npm 和 script 方式将 IM SDK 集成到您的 Web 项目中，推荐使用 npm 集成。
- 通过 npm 方式将 IM SDK 集成到您的小程序或者 uni-app 项目中。
- 通过集成 SDK 上传插件 [tim-upload-plugin](https://www.npmjs.com/package/tim-upload-plugin)，实现更快更安全的富文本消息资源上传。

### npm 集成（推荐）

在您的项目中使用 npm 安装相应的 IM SDK 依赖。

#### **Web 项目**

<dx-codeblock>
:::  js
// IM Web SDK
// 从v2.11.2起，SDK 支持了 WebSocket，推荐接入；v2.10.2及以下版本，使用 HTTP
npm install tim-js-sdk --save
// 发送图片、文件等消息需要腾讯云即时通信 IM 上传插件
npm install tim-upload-plugin --save
:::
</dx-codeblock>

>?若同步依赖过程中出现问题，请切换 npm 源后再次重试。
><dx-codeblock>
:::  js

npm config set registry http://r.cnpmjs.org/

:::
</dx-codeblock>

 
 在项目脚本里引入模块。
<dx-codeblock>
:::  js

// 从v2.11.2起，SDK 支持了 WebSocket，推荐接入；v2.10.2及以下版本，使用 HTTP
import TIM from 'tim-js-sdk';
import TIMUploadPlugin from 'tim-upload-plugin';

let options = {
  SDKAppID: 0 // 接入时需要将0替换为您的即时通信 IM 应用的 SDKAppID
};
// 创建 SDK 实例，`TIM.create()`方法对于同一个 `SDKAppID` 只会返回同一份实例
let tim = TIM.create(options); // SDK 实例通常用 tim 表示

// 设置 SDK 日志输出级别，详细分级请参见 setLogLevel https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#setLogLevel 接口的说明</a>
tim.setLogLevel(0); // 普通级别，日志量较多，接入时建议使用
// tim.setLogLevel(1); // release 级别，SDK 输出关键信息，生产环境时建议使用

// 注册腾讯云即时通信 IM 上传插件
tim.registerPlugin({'tim-upload-plugin': TIMUploadPlugin});

:::
</dx-codeblock>

#### **小程序或者 uni-app 项目**

<dx-codeblock>
:::  js

// 从v2.11.2起，SDK 支持了 WebSocket，推荐接入；v2.10.2及以下版本，使用 HTTP
npm install tim-wx-sdk --save
// 发送图片、文件等消息需要腾讯云 即时通信 IM 上传插件
npm install tim-upload-plugin --save

:::
</dx-codeblock>

>?若同步依赖过程中出现问题，请切换 npm 源后再次重试。
><dx-codeblock>
:::  js

npm config set registry http://r.cnpmjs.org/

:::
</dx-codeblock>

在项目脚本里引入模块，并初始化。
<dx-codeblock>
:::  js
// 从v2.11.2起，SDK 支持了 WebSocket，推荐接入；v2.10.2及以下版本，使用 HTTP
import TIM from 'tim-wx-sdk';
import TIMUploadPlugin from 'tim-upload-plugin';

let options = {
  SDKAppID: 0 // 接入时需要将0替换为您的即时通信 IM 应用的 SDKAppID
};
// 创建 SDK 实例，`TIM.create()`方法对于同一个 `SDKAppID` 只会返回同一份实例
let tim = TIM.create(options); // SDK 实例通常用 tim 表示

// 设置 SDK 日志输出级别，详细分级请参见 setLogLevel  https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#setLogLevel 接口的说明</a>
tim.setLogLevel(0); // 普通级别，日志量较多，接入时建议使用
// tim.setLogLevel(1); // release 级别，SDK 输出关键信息，生产环境时建议使用

// 注册腾讯云即时通信 IM 上传插件
tim.registerPlugin({'tim-upload-plugin': TIMUploadPlugin});

// v2.22.0 起支持 uni-app 打包 native app 时使用离线推送插件
// 请注意！应合规要求，在用户同意隐私协议的前提下，登录成功后 SDK 会通过推送插件获取推送 token，并将推送 token 传递至后台（若获取 token 失败则会导致离线推送无法正常使用）
const TUIOfflinePush = uni.requireNativePlugin("TencentCloud-TUIOfflinePush");
tim.registerPlugin({
  'tim-offline-push-plugin': TUIOfflinePush,
  'offlinePushConfig': {
    // huawei
    'huaweiBusinessID': '', // 在腾讯云控制台上传第三方推送证书后分配的证书 ID
    // xiaomi
    'xiaomiBusinessID': '', // 在腾讯云控制台上传第三方推送证书后分配的证书 ID
    'xiaomiAppID': '', // 小米开放平台分配的应用 APPID
    'xiaomiAppKey': '', // 小米开放平台分配的应用 APPKEY
    // meizu
    'meizuBusinessID': '', // 在腾讯云控制台上传第三方推送证书后分配的证书 ID
    'meizuAppID': '', // 魅族开放平台分配的应用 APPID
    'meizuAppKey': '', // 魅族开放平台分配的应用 APPKEY
    // vivo
    'vivoBusinessID': '', // 在腾讯云控制台上传第三方推送证书后分配的证书 ID
    // oppo
    'oppoBusinessID': '', // 在腾讯云控制台上传第三方推送证书后分配的证书 ID
    'oppoAppKey': '', // oppo 开放平台分配的应用 APPID
    'oppoAppSecret': '', // oppo 开放平台分配的应用 Secret
    // ios
    'iosBusinessID': '', // 在腾讯云控制台上传第三方推送证书后分配的证书 ID
  }
});

:::
</dx-codeblock>

### Script 集成

在您的项目中使用 script 标签引入 SDK，并初始化。

<dx-codeblock>
:::  js

<!-- tim-js.js 和 tim-upload-plugin.js 可以从 https://github.com/TencentCloud/TIMSDK/tree/master/Web/IMSDK 获取 -->
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

:::
</dx-codeblock>


### 相关资源
- [SDK 更新日志](https://cloud.tencent.com/document/product/269/38492)
- [SDK 接口文档](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html)
- [常见问题](https://cloud.tencent.com/document/product/269/68275)
- [IM Web Demo](https://github.com/TencentCloud/TIMSDK/tree/master/Web)
- [腾讯云即时通信 IM 上传插件下载地址](https://www.npmjs.com/package/tim-upload-plugin)


## 常见问题

**1. 小程序如果需要上线或者部署正式环境怎么办？**
请在**微信公众平台**>**开发**>**开发管理**>**开发设置**>**服务器域名**中进行域名配置：

从v2.11.2起 SDK 支持了 WebSocket，WebSocket 版本须添加以下域名到 **socket 合法域名**：

| 域名 | 说明 |  是否必须 |
|:-------:|---------|----|
|`wss://wss.im.qcloud.com`| Web IM 业务域名 | 必须|
|`wss://wss.tim.qq.com`| Web IM 业务域名 | 必须|

将以下域名添加到 **request 合法域名**：

| 域名 | 说明 |  是否必须 |
|:-------:|---------|----|
|`https://web.sdk.qcloud.com`| Web IM 业务域名 | 必须|
|`https://webim.tim.qq.com` | Web IM 业务域名 | 必须|
|`https://api.im.qcloud.com` | Web IM 业务域名 | 必须|

v2.10.2及以下版本使用 HTTP，HTTP 版本须添加以下域名到 **request 合法域名**：

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

