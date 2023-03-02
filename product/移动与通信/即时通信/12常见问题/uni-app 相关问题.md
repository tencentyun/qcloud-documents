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
	npm config set registry http://r.cnpmjs.org/
```
[](id:Q2)
### 如何上传图片、视频、语音消息等富媒体消息？
请使用 [tim-upload-plugin](https://www.npmjs.com/package/tim-upload-plugin) 插件。
>! 请将 tim-upload-plugin 升级到 [1.1.0](https://www.npmjs.com/package/tim-upload-plugin) 版本，该版本支持了 iOS 和 安卓上传富媒体消息以及支持视频封面。
>
```javascript
    // 发送图片、语音、视频等消息需要 tim-upload-plugin 上传插件
	npm install tim-upload-plugin@latest --save
	import TIMUploadPlugin from "tim-upload-plugin";
	// 注册上传插件
	uni.$TUIKit.registerPlugin({
		"tim-upload-plugin": TIMUploadPlugin
	});
```
[](id:Q3)
###  如何实现非媒体文件消息上传？
- uni-app [官方文档](https://uniapp.dcloud.net.cn/api/media/file.html) 提示 `chooseFile` 不支持 APP 选择非媒体文件。故客户根据自己的需求在 [插件市场](https://ext.dcloud.net.cn/search?q=%E6%96%87%E4%BB%B6%E9%80%89%E6%8B%A9) 选择可用插件。
- 可参考插件库可用插件：[iOS 上传文件插件](https://ext.dcloud.net.cn/plugin?id=1311) 、 [安卓上传文件插件](https://ext.dcloud.net.cn/plugin?id=5263) （非官方）完成文件选择 ,并格式化数据符合文件消息数据格式要求。
- 可通过文件消息 [createFileMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#createFileMessage) API 实现文件上传功能。
- file 参数如下表所示：
 
| 参数      | 类型     | 含义               | 
| ---------| -------  | ------------------ |
| name   | String       | 文件名（必要）|
| size        | Number     |文件大小 （必要，不能为0） |
| type           |  String    | 文件类型 （必要）|
| path           |  String     | 文件路径 （必要）|
| lastModified |   String   | 修改时间 （非不要）|

参考示例：
```javascript
    const fileData = {
      files: [
        {
        name: '', // 文件名
        size: 10, //本地文件大小
        type: 'pdf', //文件类型
        path: '', //本地文件路径
        lastModified: '', // 修改时间
        },
      ],
    };
    tim.sendFileMessage(fileData).then((res) => {
      console.log(res, "sendFileMessage");
    });
```
[](id:Q4)
###  uni-app  打包 iOS 语音消息无法播放怎么办？
  请将 IM SDK 升级到 [2.15.0](https://cloud.tencent.com/document/product/269/38492)，该版本支持了 iOS 语音消息播放。

[](id:Q5)
### uni-app  打包 app 发送语音消息时间显示错误怎么办？
   uni-app 打包 app，`recorderManager.onStop` 回调中没有 `duration` 和 `fileSize`，需要用户自己补充 duration 和 fileSize。
- **通过本地起定时器记录时间，计算出 duration。**
- **本地计算文件大小，fileSize ＝ (音频码率) x 时间长度(单位：秒) / 8，粗略估算。**
详细代码请参见 [uni-app TUIKit](https://github.com/tencentyun/TIMSDK/tree/master/uni-app)。
>!语音消息对象中必须包括 `duration` 和 `fileSize`，如果没有 `fileSize`，语音消息时长是一串错误的数字
[](id:Q6)
### video 视频消息层级过高无法滑动怎么办？
 在项目中通过视频图片代替，没有直接渲染 `video`，在播放时渲染的方式规避了层级过高问题。
 详细代码请参见 [uni-app TUIKit](https://github.com/tencentyun/TIMSDK/tree/master/uni-app)。
>!请参见官方 [原生组件说明](https://uniapp.dcloud.io/component/native-component)。
[](id:Q7)
### 微信小程序环境在真机预览下报系统错误，体积过大怎么办？
运行时请勾选代码压缩，运行到小程序模拟器>运行时是否压缩代码。

[](id:Q8)
### 引入原生音视频插件报以下错怎么办？
![](https://qcloudimg.tencent-cloud.cn/raw/e68ad1caf6be5d7f551a3b765c4aca53.png)
根据 uni-app [原生插件调试](https://ask.dcloud.net.cn/article/35412) 制作 [自定义基座](https://ask.dcloud.net.cn/article/35115)
![](https://qcloudimg.tencent-cloud.cn/raw/7758e1f3b5214a1ecd5a1aac46445ac3.png)

[](id:Q9)
#### 6. 小程序如果需要上线或者部署正式环境怎么办？

请在**微信公众平台** > **开发** > **开发管理** > **开发设置** > **服务器域名**中进行域名配置：

从v2.11.2起 SDK 支持了 WebSocket，WebSocket 版本须添加以下域名到 **socket 合法域名**：

| 域名  | 说明  | 是否必须 |
| --- | --- | --- |
| `wss://wss.im.qcloud.com` | Web IM 业务域名 | 必须  |
| `wss://wss.tim.qq.com` | Web IM 业务域名 | 必须  |

将以下域名添加到 **request 合法域名**：

| 域名  | 说明  | 是否必须 |
| --- | --- | --- |
| `https://web.sdk.qcloud.com` | Web IM 业务域名 | 必须  |
| `https://webim.tim.qq.com` | Web IM 业务域名 | 必须  |
| `https://api.im.qcloud.com` | Web IM 业务域名 | 必须  |

将以下域名添加到 **uploadFile 合法域名**：

| 域名  | 说明  | 是否必须 |
| --- | --- | --- |
| `https://cos.ap-shanghai.myqcloud.com` | 文件上传域名 | 必须  |
| `https://cos.ap-shanghai.tencentcos.cn` | 文件上传域名 | 必须  |
| `https://cos.ap-guangzhou.myqcloud.com` | 文件上传域名 | 必须  |

将以下域名添加到 **downloadFile 合法域名**：

| 域名  | 说明  | 是否必须 |
| --- | --- | --- |
| `https://cos.ap-shanghai.myqcloud.com` | 文件下载域名 | 必须  |
| `https://cos.ap-shanghai.tencentcos.cn` | 文件下载域名 | 必须  |
| `https://cos.ap-guangzhou.myqcloud.com` | 文件下载域名 | 必须  |

[](id:QQ)
### 技术咨询
了解更多详情您可 QQ 咨询：<dx-tag-link link="#QQ" tag="技术交流群">309869925</dx-tag-link>
