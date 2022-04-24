## 准备工作
- 请阅读 Web 美颜特效 SDK [接入指南](https://cloud.tencent.com/document/product/616/71364)，熟悉 SDK 基本用法。
- 请阅读云直播 [入门文档](https://cloud.tencent.com/document/product/267/41870) 以及 [WebRTC 推流](https://cloud.tencent.com/document/product/267/56505)，了解 WebRTC 推流工具基本用法，并完成直播基础设置。

## 开始使用
### 步骤1：Web 美颜特效 SDK 引入[](id:step1)
在需要直播推流的页面（PC Web 端）中引入 js 脚本：
```html
<script charset="utf-8" src="https://webar-static.tencent-cloud.com/ar-sdk/resources/latest/webar-sdk.umd.js"></script>
```
>! 这里是示例项目，为了方便使用 script 标签方式引入，您也可以参考 [接入指南](https://cloud.tencent.com/document/product/616/71364) 中的方法，用 npm 包的方式引入。

### 步骤2：WebRTC 推流资源引入[](id:step2)
在需要直播推流的页面（PC Web 端）中引入 js 脚本：
```html
<script src="https://video.sdk.qcloudecdn.com/web/TXLivePusher-2.0.0.min.js" charset="utf-8"></script>
```
>! 请在 HTML 的 body 部分引入上述脚本，如果在 head 部分引入会报错。

### 步骤3：初始化 Web 美颜特效 SDK[](id:step3)
示例代码如下：
```js
const { ArSdk } = window.AR;

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

let w = 720;
let h = 480;

// 获取输入流
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

ar.on('ready', async (e) => {

	// 在 ready 回调里及该事件之后，可使用三种方法来设置美颜特效：setBeautify/setEffect/setFilter

	// 例如使用range input（滑动控件）设置美颜效果
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

	// 获取ar sdk 输出的流在下一步中进行 WebRTC 推流
	const arStream = await ar.getOutput();

});

ar.on('error', (e) => {
	console.log(e);
});

```
更细致的 UI 控制用法您可以通过下载文末提供的代码包来进一步查看。

### 步骤4：开始推流[](id:step4)
完成上一步之后，在 SDK ready 回调中获取输出流即可进行 WebRTC 推流，示例代码如下：
```javascript
let livePusher = new TXLivePusher()
// 设置直播推流基础参数 begin
let DOMAIN = '您的推流域名'
let AppName = '您的appName' 
let StreamName = '您的streamName'
let txSecret = '您的txSecret'
let txTime = '您的txTime'
// 设置直播推流基础参数 end

let pushUrl = `webrtc://${DOMAIN}/${AppName}/${StreamName}?txSecret=${txSecret}&txTime=${txTime}`

// 可选：设置预览界面元素
livePusher.setRenderView('id_local_video');
// 捕获流内容
livePusher.startCustomCapture(arStream);
// 立刻开始推流，您也可以通过其他函数来控制推流时机
livePusher.startPush(pushUrl)

```
其中 txSecret 和 txTime 都需要计算，为了方便您也可以通过 **直播控制台** 的 [**地址生成器**](https://console.cloud.tencent.com/live/addrgenerator/addrgenerator) 快速生成这些参数和推流  URL，具体请参见 [地址生成器](https://cloud.tencent.com/document/product/267/35257)。
推流（startPush）成功后，您应该就能看到应用了美颜特效的直播流的效果了。

### 步骤5：查看效果[](id:step5)
>! 示例项目需您自行启动本机 Web 服务，并保证通过端口号可访问到 HTML 文件。

- 若您有一个已备案成功的播放域名，可参考 [直播播放](https://cloud.tencent.com/document/product/267/32733#.E7.9B.B4.E6.92.AD.E6.92.AD.E6.94.BE) 查看实际的播放效果。
- 若您无播放域名，可在**直播控制台**的 [流管理](https://console.cloud.tencent.com/live/streammanage) 中预览当前流的画面。

## 代码示例 [](id:demo)
您可以下载 [示例代码](https://webar-static.tencent-cloud.com/docs/quick-demo/best_practice.zip) 解压后查看 `AR_LEB_WEB` 代码目录。
