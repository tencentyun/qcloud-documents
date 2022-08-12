## 准备工作
WebRTC 的推流相关请参见 [结合 WebRTC 的推流](https://cloud.tencent.com/document/product/616/71373)，本文重点介绍采取预初始方案时代码及流程差异部分。
预初始化方案相关介绍，请参见 [加载优化](https://cloud.tencent.com/document/product/616/76111)。

## 开始使用
预初始化方案与常规加载方案相比，最大的差异在于初始化 SDK 时不需要指 input 或 camera 属性，即初始化时不为 SDK 指定输入数据，后续根据业务需求在适当的位置调用 initCore 接口指定输入数据。这样做的好处是将 SDK 依赖的资源提前加载，后续调用 initCore 后，SDK 的 ready 事件就会更快地触发，便于获取输出流展示等。以下为关键代码示例：

### 初始化SDK

```js
...
let resourceReady = false
// ar sdk 基础配置参数
const config = {
	// input: stream, // 不指定input
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
// resourceReady 回调事件触发，意味着相关资源已加载完成，等待 initCore 提供输入
ar.on('resourceReady', () => {
	resourceReady = true
})
// 调用 initCore 后会触发 ready 事件
ar.on('ready', () => {
	// 获取 ar sdk 输出流数据
	const arStream = await ar.getOutput();
	// 处理输出流
	...
})
...
```
### 用户操作触发 initCore 事件
```js
// 此处以用户点击【开启摄像头】为例，介绍预初始化方案设置输入流的方式
function onClickStartCamera(){
	let w = 1280;
	let h = 720;

	// 获取设备输入流
	const arInputStream = await navigator.mediaDevices.getUserMedia({
		audio: true,
		video: {
			width: w,
			height: h
		}
	});
	if(!resourceReady){ // 此模式下，resourceReady未触发时，调用initCore无意义，业务可以做一些个性化处理
		return
	}
	// 设置 ar sdk 输入流数据
	ar.initCore({
		input: arInputStream
	})
}
```

[](id:demo)
## 代码示例 
您可以下载 [示例代码](https://webar-static.tencent-cloud.com/docs/quick-demo/best_practice.zip) 解压后查看 `AR_LEB_WEB` 代码目录中的 `AR_and_LEB_Preload.html` 文件。
