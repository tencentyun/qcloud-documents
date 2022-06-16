### 步骤1：引入SDK
```javascript
import { ArSdk } from 'tencentcloud-webar';// SDK 类
```
如果项目无需编译，则可以直接以如下方式引用：
```html
<script charset="utf-8" src="https://webar-static.tencent-cloud.com/ar-sdk/resources/latest/webar-sdk.umd.js"></script>
```

### 步骤2：初始化实例
接下来初始化一个SDK实例。
```javascript
// 获取鉴权参数
const authData = {
	licenseKey: 'xxxxxxxxx',
	appId: 'xxx',
	authFunc: authFunc // 详见「License 配置与使用 - 签名方法」
};
// 输入SDK的流
const stream = await navigator.mediaDevices.getUserMedia({
	audio: true,
	video: { width: w, height: h }
})

const config = {
	auth: authData, // 鉴权参数
    input: stream, // input传输入流
	beautify: { // 初始化美颜参数(可选)
		whiten: 0.1,
		dermabrasion: 0.3,
		eye: 0.2,
		chin: 0,
		lift: 0.1,
		shave: 0.2
	}
}
const sdk = new ArSdk(
	// 传入一个 config 对象用于初始化 sdk
	config
)
```
输入除了媒体流外，也支持传'string|HTMLImageElement'来处理图片。
```javascript
const config = {
	auth: authData, // 鉴权参数
    input: 'https://xxx.png', // input传输入流
}
const sdk = new ArSdk(
	// 传入一个 config 对象用于初始化 sdk
	config
)

// 在 created 回调中可拉取特效和滤镜列表供页面展示，详见[参数与方法]()
sdk.on('created', () => {
    // 获取内置美妆
    sdk.getEffectList({
        Type: 'Preset',
        Label: '美妆',
    }).then(res => {
        effectList = res
    });
    // 获取内置滤镜
    sdk.getCommonFilter().then(res => {
        filterList = res
    })
})

// 在 ready 回调中调用 setBeautify/setEffect/setFilter 等渲染方法
// 详情可参见[设置美颜和特效]()
sdk.on('ready', () => {
    // 设置美颜
    sdk.setBeautify({
        whiten: 0.2
    });
    // 设置特效
    sdk.setEffect({
        id: effectList[0].EffectId,
        intensity: 0.7
    });
    // 设置滤镜
    sdk.setFilter(filterList[0].EffectId, 0.5)
})
```

### 步骤3：播放流
初始化完成后，可以使用 `ArSdk.prototype.getOutput` 方法获取输出的媒体流。
```javascript
const output = await sdk.getOutput()
```
拿到输出的 `MediaStream` 之后，可以直接在页面里播放。
```javascript
// 在页面内使用video播放输出的媒体流，预览效果
const video = document.createElement('video')
video.setAttribute('playsinline', '');
video.setAttribute('autoplay', '');
video.srcObject = output
document.body.appendChild(video)
video.play()
```

### 步骤4：获取输出
拿到输出的 `MediaStream` 之后，可以结合第三方SDK（如TRTC Web SDK，快直播Web SDK）进行推流等后续处理。
```javascript
const output = await sdk.getOutput()
```
推流等操作参见[最佳实践-结合TRTC推流](),[最佳实践-结合WebRTC推流]()

>!
- 如果传入的 input 是图片，则返回为 string 类型的 DataURL，其他场景均返回 `MediaStream` 类型。
- 输出的媒体流中 `video` 轨道是 ArSdk 实时处理的，如有 `audio` 轨道则保持不变。
- getOutput方法是异步方法，会等到sdk执行完一系列初始化工作并且可以生成流之后返回。
- getOutput方法支持传入一个fps参数，表示设置输出的帧率为fps（比如15）,不传则默认取输入流的帧率。
- getOutput可以执行多次，每次执行会产生一个新的媒体流，可用于输出不同帧率媒体流的场景（例如预览时使用高帧率流，推流时使用低帧率流）。


## 步骤5：设置美颜和特效
SDK的所有素材均兼容微信小程序端与Web端，调用方式一致，详情可参见[设置美颜和特效]()。


