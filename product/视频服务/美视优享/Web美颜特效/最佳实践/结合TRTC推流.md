## 准备工作
- 请阅读 Web 美颜特效 SDK [接入指南](https://cloud.tencent.com/document/product/616/71364)，熟悉 SDK 基本用法。
- 请阅读 TRTC [快速集成(Web)](https://cloud.tencent.com/document/product/647/16863)，了解 TRTC Web SDK 基本用法，并完成基础设置。
- 请阅读 TRTC [快速跑通 Web Demo](https://cloud.tencent.com/document/product/647/32398)，并先尝试在本地项目中运行 TRTC Web Demo。

## 开始使用
[](id:step1)
### 步骤1：Web 美颜特效 SDK 引入
**由于 TRTC 的 Web Demo 项目已经做的比较完善，我们在此基础上进行少量改造即可。**
在页面（PC Web 端）中引入 js 脚本：
```html
<script charset="utf-8" src="https://webar-static.tencent-cloud.com/ar-sdk/resources/latest/webar-sdk.umd.js"></script>
```
>! 这里是示例项目，为了方便使用 script 标签方式引入，您也可以参考 [接入指南](https://cloud.tencent.com/document/product/616/71364) 中的方法，用 npm 包的方式引入。


[](id:step2)
### 步骤2：理解 TRTC 流初始化逻辑
在 TRTC 的 Demo 项目里，查看 TRTC 本地流的初始化过程，TRTC 通过 createStream 方法创建流对象，
可以指定使用 TRTC SDK 的默认采集方式, 如下
```js
// 从麦克风和摄像头采集本地音视频流
const localStream = TRTC.createStream({ userId, audio: true, video: true });
localStream.initialize().then(() => {
	console.log('initialize localStream success');
	// 本地流初始化成功，可通过Client.publish(localStream)发布本地音视频流
}).catch(error => {
	console.error('failed initialize localStream ' + error);
});
```
以上为最基本的采集本地音视频流的初始化方式。
为了便于开发者对音视频流进行预处理，TRTC.createStream 也支持从外部音视频源创建本地流，通过这种方式创建本地流，开发者可以实现自定义处理（例如对视频进行美颜处理），以下为示例代码：
```js
// 从指定的音视频源创建本地音视频流
navigator.mediaDevices.getUserMedia({ audio: true, video: true }).then(stream => {
	const audioTrack = stream.getAudioTracks()[0];
	const videoTrack = stream.getVideoTracks()[0];
	const localStream = TRTC.createStream({ userId, audioSource: audioTrack, videoSource: videoTrack });
	localStream.initialize().then(() => {
		console.log('initialize localStream success');
		// 本地流初始化成功，可通过Client.publish(localStream)发布本地音视频流
	}).catch(error => {
		console.error('failed initialize localStream ' + error);
	});
});
```
createStream 方法的使用详情可见 [TRTC SDK 文档](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/TRTC.html#createStream)，为了获取经过美颜处理的流，我们需要先 [初始化 Web 美颜特效 SDK](#step3)。

[](id:step3)
### 步骤3：初始化 Web 美颜特效 SDK
示例代码如下：
```js
const { ArSdk } = window.AR

/** ----- 鉴权配置 ----- */

/**
 * 腾讯云账号 APPID
 * 
 * 进入[腾讯云账号中心](https://console.cloud.tencent.com/developer) 即可查看 APPID
 */
const APPID = ''; // 此处请填写您自己的参数

/**
 * Web LicenseKey
 * 
 * 登录音视频终端 SDK 控制台的[Web License 管理](https://console.cloud.tencent.com/vcube/web)，创建项目即可获得 LicenseKey
 */
const LICENSE_KEY = ''; // 此处请填写您自己的参数

/**
 * 计算签名用的密钥 Token
 * 
 * 注意：此处仅用于 DEMO 调试，正式环境中请将 Token 保管在服务端，签名方法迁移到服务端实现，通过接口提供，前端调用拉取签名，参考
 * [签名方法](https://https://cloud.tencent.com/document/product/616/71370#.E7.AD.BE.E5.90.8D.E6.96.B9.E6.B3.95)
 */
const token = ''; // 此处请填写您自己的参数

/** ----------------------- */

/**
 * 定义获取签名方法
 *
 * 注意：此处方案仅适用于 DEMO 调试，正式环境中签名方法推荐在服务端实现，通过接口提供，前端调用拉取签名
 * 如：
 * async function () {
 *  return fetch('http://xxx.com/get-ar-sign').then(res => res.json());
 * };
 */
const getSignature = function () {
	const timestamp = Math.round(new Date().getTime() / 1000);
	const signature = sha256(timestamp + token + APPID + timestamp).toUpperCase();
	return { signature, timestamp };
};

let w = 1280;
let h = 720;

// 获取设备输入流
const stream = await navigator.mediaDevices.getUserMedia({
	audio: true,
	video: { width: w, height: h }
})

// ar sdk 基础配置参数
const config = {
	input: stream,
	auth: {
		licenseKey: LICENSE_KEY,
		appId: APPID,
		authFunc: getSignature
	},
	// 初始美颜效果（可选参数）
	beautify: {
		whiten: 0.1, // 美白 0-1
		dermabrasion: 0.5, // 磨皮 0-1
		lift: 0.3, // 瘦脸 0-1
		shave: 0, // 削脸 0-1
		eye: 0, // 大眼 0-1
		chin: 0, // 下巴 0-1
	}
}

// config 传入 ar sdk
const ar = new ArSdk(config);

// created回调里可以获取内置特效与滤镜列表进行界面展示
ar.on('created', () => {
	// 获取内置特效，支持分页
	ar.getEffectList({
		Type: 'Preset',
		PageSize: 10,
		PageNumber: 0,
	}).then((res) => {
		const list = res.map(item => ({
			name: item.Name,
			id: item.EffectId,
			cover: item.CoverUrl,
			url: item.Url,
			label: item.Label,
			type: item.PresetType,
		}));

		// 渲染美妆特效列表视图
		renderEffectList(list);

	}).catch((e) => {
		console.log(e);
	});
	// 内置滤镜
	ar.getCommonFilter().then((res) => {
		const list = res.map(item => ({
			name: item.Name,
			id: item.EffectId,
			cover: item.CoverUrl,
			url: item.Url,
			label: item.Label,
			type: item.PresetType,
		}));

		// 渲染滤镜列表视图
		renderFilterList(list);

	}).catch((e) => {
		console.log(e);
	});
});

ar.on('ready', (e) => {

	// 在 ready 回调里及该事件之后，可使用三种方法来设置美颜特效：setBeautify/setEffect/setFilter

	//  例如使用range input（滑动控件）设置美颜效果，例如
	$('#dermabrasion_range_input').change((e) => {
		ar.setBeautify({
			dermabrasion: e.target.value, // 磨皮 0-1
		});
	});

	// 通过created回调中创建的美妆特效列表交互设置美妆效果(setEffect的输入参数支持三种格式，详见SDK接入指南)
	$('#effect_list li').click(() => {
		ar.setEffect([{id: effect.id, intensity: 1}]);
	});

	// 通过created回调中创建的滤镜列表交互设置滤镜效果(setFilter第二个参数1表示强度，详见SDK接入指南）
	ar.setFilter(filterList[0].id, 1);
	$('#filter_list li').click(() => {
		ar.setFilter(filter.id, 1);
	});
});

ar.on('error', (e) => {
	console.log(e);
});
```
上述代码对 Web 美颜特效 SDK 进行了初始化配置，且在 ready 事件内进行了一些简单的美颜设置交互处理，更细致的UI交互可以通过下载文末提供的代码包来进一步查看。


[](id:step4)
### 步骤4：修改 TRTC stream 初始化过程

Web 美颜特效 SDK 初始化完成后就可以使用 `getOutput` 方法获取输出的流，再根据 [步骤2](#step2) 的介绍完成 TRTC 流初始化，示例代码如下：
```js
// 获取 ar sdk 输出流
const arStream = await this.ar.getOutput();

const audioSource = arStream.getAudioTracks()[0];
const videoSource = arStream.getVideoTracks()[0];

// create a local stream with audio/video from custom source
this.localStream_ = TRTC.createStream({
	audioSource,
	videoSource
});

```


[](id:step5)
### 步骤5：查看效果
>! 示例项目需您自行启动本机 Web 服务，并保证通过指定端口号可访问到 HTML 文件。

您在进入房间后可以很快查看实际的播放效果（运行示例代码中的 `index_AR.html`），成功后可以新开浏览器标签页进入刚才创建的房间模拟其他人加入房间的效果。


## 示例代码
您可以下载 [示例代码](https://webar-static.tencent-cloud.com/docs/quick-demo/best_practice.zip) 解压后查看，
主要改动部分在 `index_AR.html` 和 `rtc-client-with-webar.js`，美颜特效的交互逻辑代码在`base-js/js/ar_interact.js`，您的 TRTC 密钥信息配置在 `base-js/js/debug/GenerateTestUserSig.js`。
