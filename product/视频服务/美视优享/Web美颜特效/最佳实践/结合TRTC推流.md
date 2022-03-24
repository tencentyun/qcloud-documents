## 准备工作
- 请阅读 Web 美颜特效 SDK [接入指南](https://tcloud-doc.isd.com/document/product/616/71364?!preview&!editLang=zh)，熟悉 SDK 基本用法。
- 请阅读 TRTC [快速集成(Web)](https://cloud.tencent.com/document/product/647/16863)，了解 TRTC Web SDK 基本用法，并完成基础设置。
- 请阅读 TRTC [快速跑通 Web Demo](https://cloud.tencent.com/document/product/647/32398)，并先尝试在本地项目中运行 TRTC Web Demo。

## 开始使用
[](id:step1)
### 步骤1：Web 美颜特效 SDK 引入
**由于 TRTC 的 Web Demo 项目已经做的比较完善，我们在此基础上进行少量改造即可。**
在页面（PC Web 端）中引入 js 脚本：
```html
<script charset="utf-8" src="https://webar-static.tencent-cloud.com/ar-sdk/resources/0.0.1/webar-sdk.umd.js"></script>
```
>! 这里是示例项目，为了方便使用 script 标签方式引入，您也可以参考 [接入指南](https://tcloud-doc.isd.com/document/product/616/71364?!preview&!editLang=zh) 中的方法，用 npm 包的方式引入。


[](id:step2)
### 步骤2：理解 TRTC client 流初始化逻辑
在 TRTC 的 Demo 项目里，查看 TRTC client 的初始化过程，如下：
```js
this.localStream_ = TRTC.createStream({
  audio: true,
  video: true,
  userId: this.userId_,
  cameraId: getCameraId(),
  microphoneId: getMicrophoneId(),
  mirror: true
});
```
调整初始化代码前，我们需要先 [初始化 Web 美颜特效 SDK](#step3)。


[](id:step3)
### 步骤3：初始化 Web 美颜特效 SDK
示例代码如下：
```js
const {ENTRY_TYPES, ArSdk, OUTPUT_TYPES} = window.AR

/** ----- License 配置 ----- */
/** ----- 请填写您自己的参数 ----- */
const APPID = '您的appid';
const token = '您的token';
const LICENSE_KEY = '您的licenseKey';
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

let width = 640;
let height = 360;

const ar = new ArSdk(
	ENTRY_TYPES.CAMERA,
	{
		width,
		height,
		mirror: true,
		enableLoadingIcon: true,
	},
	LICENSE_KEY,
	APPID,
	async () => {
		const { signature, timestamp } = await getSignature();
		return {
			signature,
			timestamp,
		};
	},
);

ar.on('ready', (e) => {

	// 记录AR SDK 初始化就绪状态
	this.isARReady = true;

	// 设置美颜效果
	ar.setBeautify({
		whiten: 0.4, // 美白 0-1
		dermabrasion: 0.5, // 磨皮 0-1
		lift: 0.3, // 瘦脸 0-1
		shave: 0, // 削脸 0-1
		eye: 0, // 大眼 0-1
		chin: 0, // 下巴 0-1
	});


    // 获取内置特效，支持分页
    ar.getEffectList({
        Type: 'Preset',
        // PageSize: 10,
        // PageNumber: 0,
    }).then((res) => {
        const list = res.map(item => ({
            name: item.Name,
            id: item.EffectId,
            cover: item.CoverUrl,
            url: item.Url,
            label: item.Label,
            type: item.PresetType,
        }));

        // todo 尝试设置一个特效
        // ar.setEffect([{id: list[0].id, intensity:0.8}])
    }).catch((e) => {
        console.log(e);
    });

});

ar.on('error', (e) => {
	console.log(e);
});
```


[](id:step4)
### 步骤4：修改 TRTC client 初始化过程
**请确保 Web 美颜特效 SDK 就绪后再执行这里的逻辑**。
因此在 TRTC client 的代码片段里，我们要用一个变量记录一下 ready 状态，示例代码如下：
```js
const {OUTPUT_TYPES} = window.AR;
// 获取AR的流
const mystream = this.ar.getOutput(OUTPUT_TYPES.MEDIA_STREAM);

let stream = null;
try {
	stream = await navigator.mediaDevices.getUserMedia({
		audio: true
	});
} catch (error) {
	console.error('failed to getUserMedia');
	return;
}

// 分别获取视频和音频的track
const audioSource = stream.getAudioTracks()[0];
const videoSource = mystream.getVideoTracks()[0];

// 初始化TRTC流
this.localStream_ = TRTC.createStream({
	audioSource,
	videoSource
});
// todo
```


[](id:step5)
### 步骤5：查看效果
>! 示例项目需您自行启动本机 Web 服务，并保证通过 `8090` 端口可访问到 HTML 文件。

您在进入房间后可以很快查看实际的播放效果（运行示例代码中的 `index_AR.html`），成功后可以新开新的浏览器标签页来模拟其他人加入房间的效果。


## 示例代码
您可以访问 [示例代码](https://webar-static.tencent-cloud.com/docs/best_practice.zip) 下载后查看，主要改动部分在 `index_AR.html` 和 `rtc-client-with-webar.js`。
