SDK 提供了内置相机，如开发者无需自行维护媒体流，仅需要快速调起摄像头，推荐使用内置相机方式。

### 步骤1：引入SDK
```javascript
import { ArSdk } from 'tencentcloud-webar';// SDK 类
```
如果项目无需编译，则可以直接以如下方式引用：
```html
<script charset="utf-8" src="https://webar-static.tencent-cloud.com/ar-sdk/resources/latest/webar-sdk.umd.js"></script>
```

### 步骤2：初始化实例
接下来初始化一个 SDK 实例用于显示：
```javascript
// 获取鉴权参数
const authData = {
	licenseKey: 'xxxxxxxxx',
	appId: 'xxx',
	authFunc: authFunc // 详见「License 配置与使用 - 签名方法」
};

const config = {
    auth: authData, // 鉴权参数
    camera: { // 传camera配置调起内置相机
        width: 1280,
        height: 720
    },
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

let effectList = [];
let filterList = [];

sdk.on('created', () => {
    // 在 created 回调中可拉取特效和滤镜列表供页面展示，详见[参数与方法]()
    sdk.getEffectList({
        Type: 'Preset',
        Label: '美妆',
    }).then(res => {
        effectList = res
    });
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

>! `config`中的 `camera` 参数表示将由 SDK 来采集当前设备的摄像头媒体流作为输入，当设置了 `camera` 参数，SDK 还提供一系列基础的设备管理方法。

为了方便控制，内置的`camera`提供了以下方法调用：
<table>
<thead><tr><th>方法名</th><th>说明</th><th>入参</th><th>返回值</th></tr></thead>
<tbody>
<tr>
<td>getDevices</td>
<td>获取当前所有设备列表</td>
<td>-</td>
<td>Promise&lt;Array&lt;MediaDeviceInfo&gt;&gt;</td>
</tr><tr>
<td>switchDevice</td>
<td>切换设备</td>
<td><pre style="color:white">type:string, deviceId:string</pre></td>
<td>Promise
</td>
</tr>
<tr>
<td>muteAudio</td>
<td>静音当前摄像头流</td>
<td>-</td>
<td>-</td>
</tr><tr>
<td>unmuteAudio</td>
<td>恢复静音</td>
<td>-</td>
<td>-</td>
</tr><tr>
<td>muteVideo</td>
<td>禁用当前摄像头流内画面，此时流仍存在只是视频轨道已禁用</td>
<td>-</td>
<td>-</td>
</tr><tr>
<td>unmuteVideo</td>
<td>启用当前摄像头流内画面</td>
<td>-</td>
<td>-</td>
</tr><tr>
<td>stopVideo</td>
<td>停止当前摄像头设备，视频流会停止（音频流还存在）</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>restartVideo</td>
<td>重启当前摄像头，在 stopVideo 之后使用</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>stop</td>
<td>停止当前摄像头视频以及音频设备</td>
<td>-</td>
<td>-</td>
</tr>
</tbody></table>

### 步骤3：获取输出
如果有推流等需求，可以使用`getOutput`方法获取输出的媒体流
```javascript
const output = await sdk.getOutput()
```
> getOutput方法支持传入一个fps参数，表示设置输出的帧率为fps（比如15）,不传则默认取输入流的帧率。
> getOutput可以执行多次，每次执行会产生一个新的媒体流；

### 步骤4：播放流
拿到输出的 `MediaStream` 之后，可以进行推流等后续处理，也可以直接在页面里播放。
SDK 提供了一个快速在页面预览输出效果的播放器，可用于本地预览效果场景，代码如下：
```javascript
// 初始化一个SDK的player，其中my-dom-id表示您需要放置播放器的容器id
const player = await sdk.initLocalPlayer('my-dom-id')
// 直接播放
await player.play()

// 可以暂停
// player.pause()

// 可以设置镜像，默认已设置为true
// player.setMirror(true)

// 可以获取播放器内置video元素，用来自定义一些原生配置
// const video = player.getVideoElement()

// 不需要的时候可以销毁
// player.destroy()
```
>! 注意：initLocalPlayer 获取到的播放器默认静音，如果开启静音则可能产生回声。
获取到的player，内部已封装了sdk.getOutput()方法，方便用户使用

SDK initLocalPlayer 后，其 player 对象支持以下方法：

| 方法名          | 说明                       | 入参        | 返回值           |
| :-------------- | :------------------------- | :---------- | :--------------- |
| play            | 播放                       | -           | Promise;         |
| pause           | 暂停（流不会停止，可恢复） | -           | -                |
| stop            | 停止（会把流也停止）       | -           | -                |
| mute            | 静音                       | -           | -                |
| unmute          | 取消静音                   | -           | -                |
| setMirror       | 设置镜像                   | true\|false | -                |
| getVideoElement | 获取内置 video 对象        | -           | HTMLVideoElement |
| destroy         | 销毁                       | -           | -                |

>! 注意：播放器会默认跟随camera的变化。您可以简单理解为camera的设备控制是总开关，
而localPlayer的播放控制是一个子开关；例如调用camera.muteVideo后，此时禁用了设备视频流，此时
localPlayer即使再调用play也相当于处于停止播放状态；调用camera.unmuteVideo后，重新启用了视频流，
此时localPlayer会默认自动恢复播放状态；因此启用camera配置情况下您无须再手动控制localPlayer的状态，
管理好camera设备状态即可。

## 步骤4：设置美颜和特效
SDK的所有素材均兼容微信小程序端与Web端，调用方式一致，详情可参见[设置美颜和特效]()。



