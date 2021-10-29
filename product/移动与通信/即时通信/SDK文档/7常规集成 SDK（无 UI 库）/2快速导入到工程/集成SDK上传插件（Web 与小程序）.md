## 简介
[tim-upload-plugin](https://www.npmjs.com/package/tim-upload-plugin) 即腾讯云即时通信 IM 上传插件，是基于腾讯云对象存储预签名 URL 方式实现资源上传。开发者在集成腾讯云即时通信 IM 时使用 [tim-upload-plugin](https://www.npmjs.com/package/tim-upload-plugin)  可以彻底替代 cos-js-sdk 或 cos-wx-sdk 的资源上传功能，该插件不仅提升了应用数据的安全性，而且具有上传速度快、体积小、支持跨平台小程序应用等特性。

## 优势

- ### 应用数据更安全
每次资源上传都会获取新的预签名 URL，预签名 URL 与当前文件类型和文件信息进行绑定，预签名 URL 设置有过期时间，过期后不可再使用。

- ### 平均上传速度提升10%~50%
	- 5M以内的资源文件平均上传速度比 cos-js-sdk 和 cos-wx-sdk 提升了50%。
	- 5M~12M的资源文件平均上传速度比 cos-js-sdk 和 cos-wx-sdk 提升了30%。

- ### 支持多平台的小程序应用
目前支持在微信小程序、QQ小程序、百度小程序、头条小程序、支付宝小程序接入腾讯云即时通信 IM 时使用，而 cos-wx-sdk 目前只支持在微信小程序中接入，tim-upload-plugin 提供了更好的跨平台小程序兼容性。

- ### 支持多种格式文件上传
目前可以支持 JPG、JPEG、PNG、BMP、GIF 五种格式的图片，MP4 格式的视频，语音以及 word、excel、pdf 等普通文件的上传。

- ### 轻量级插件
插件的体积在10KB以内，而目前在腾讯云即时通信 IM web 应用中接入的 cos-js-sdk 体积为1.8M，小程序应用中接入的 cos-wx-sdk 体积为1.2M，在体积方面 tim-upload-plugin 减少了98%左右，对优化应用体积很有帮助。

## 工作原理
![](https://main.qcloudimg.com/raw/4aee23c79c5ae9d0b9fd1cd4c9eba912.png)

## 注意事项

- 使用前请将 tim-js-sdk 或 tim-wx-sdk 升级到v2.9.2或更高版本。
- 小程序端使用 tim-upload-plugin 需要在小程序管理后台配置 uploadFile 和 downloadFile 合法域名： https://cos.ap-shanghai.myqcloud.com。
- 不能同时注册 tim-upload-plugin 和 cos sdk，IM SDK 会优先检测 tim-upload-plugin。
- 插件目前不支持在 Nodejs 环境中使用。

## 接入
接入 tim-upload-plugin 前需要将腾讯云即时通信 IM SDK 升级到2.9.2或更高版本才可以使用。

### 1. npm 方式接入

```javascript
// 下载依赖
npm i tim-upload-plugin --save
// tim-js-sdk 或 tim-wx-sdk的版本请使用 v2.9.2 或更高版本才能集成 tim-upload-plugin
npm i tim-js-sdk@latest --save // web环境使用
// npm i tim-wx-sdk@latest --save // 小程序环境使用

// 在项目脚本里引入模块，并初始化
import TIM from 'tim-js-sdk'; // web环境使用
// import TIM from 'tim-wx-sdk'; //  小程序环境使用
import TIMUploadPlugin from 'tim-upload-plugin';

let options = {
  SDKAppID: 0 // 接入时需要将 0 替换为您的云通信应用的 SDKAppID
};
// 创建 SDK 实例，`TIM.create()`方法对于同一个 `SDKAppID` 只会返回同一份实例
let tim = TIM.create(options); // SDK 实例通常用 tim 表示

// 设置 SDK 日志输出级别，详细分级请参见 setLogLevel 接口的说明
tim.setLogLevel(0); // 普通级别，日志量较多，接入时建议使用
// tim.setLogLevel(1); // release级别，SDK 输出关键信息，生产环境时建议使用

// 注册腾讯云即时通信IM上传插件
tim.registerPlugin({'tim-upload-plugin': TIMUploadPlugin});
```

### 2. script 方式接入

```html
<!-- tim-js.js 和 tim-upload-plugin.js 可以从 https://github.com/tencentyun/TIMSDK/tree/master/Web/Demo/sdk 获取 -->
<script src='./tim-js.js'></script>
<script src='./tim-upload-plugin.js'></script>
<script>
let options = {
  SDKAppID: 0 // 接入时需要将 0 替换为您的云通信应用的 SDKAppID
};
// 创建 SDK 实例，`TIM.create()`方法对于同一个 `SDKAppID` 只会返回同一份实例
let tim = TIM.create(options);
// 设置 SDK 日志输出级别，详细分级请参见 setLogLevel 接口的说明
tim.setLogLevel(0); // 普通级别，日志量较多，接入时建议使用
// tim.setLogLevel(1); // release级别，SDK 输出关键信息，生产环境时建议使用

// 注册腾讯云即时通信IM上传插件
tim.registerPlugin({'tim-upload-plugin': TIMUploadPlugin});

// 接下来可以通过 tim 进行事件绑定和构建 IM 应用
</script>
```


