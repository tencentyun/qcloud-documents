在进行视频通话之前，建议先进行浏览器环境检测，以及摄像头和麦克风等设备的测试，否则等用户真正进行通话时很难发现设备问题。

## 浏览器环境检测

在调用 SDK 的通信能力之前，建议您先使用 {@link TRTC.checkSystemRequirements checkSystemRequirements()} 接口检测 SDK 是否支持当前网页。如果 SDK 不支持当前浏览器，请根据用户设备类型建议用户使用 SDK 支持的浏览器。

```javascript
TRTC.checkSystemRequirements().then(checkResult => {
  if (checkResult.result) {
    // 支持进房
    if (checkResult.isH264DecodeSupported) {
    	// 支持拉流
    }
    if (checkResult.isH264EncodeSupported) {
    	// 支持推流
    }
  }
})
```

>! 当用户使用 SDK 支持的浏览器，且收到 `TRTC.checkSystemRequirements` 返回的检测结果为 false 时，可能是以下原因：
- **情况一：**请检查链接是否满足以下三种情况之一
	- localhost 域（ Firefox 浏览器支持 localhost 及本地 IP 访问 ）
	- 开启了 HTTPS 的域
	- 使用 `file:///` 协议打开的本地文件
- **情况二：**Firefox 浏览器安装完成后需要动态加载 H264 编解码器，因此会出现短暂的检测结果为 false 的情况，请稍等再试或先使用其他推荐浏览器打开链接。


### 已知的浏览器使用限制说明
- **Firefox：**Firefox 只支持视频帧率为 30 fps, 如有帧率设置需求，请使用 SDK 支持的其他浏览器。
- **QQ 浏览器：**个别摄像头，麦克风正常的 Windows 设备在 localhost 环境下调用 `localStream.initialize() ` 时抛出 NotFoundError 错误。


## 音视频设备测试

为保证用户在使用 TRTC-SDK 的过程中有更好的用户体验，我们建议您在用户加入 TRTC 房间之前，对用户设备及网络状况进行检测并给出建议和引导。
为方便您快速集成设备检测及网络检测功能，我们提供一下几种方式供您参考：
- [rtc-detect 的 JS 库](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-23-advanced-support-detection.html#h2-4)
- [设备检测的 React 组件](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-23-advanced-support-detection.html#h2-5)
- [TRTC 能力检测页面](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-23-advanced-support-detection.html#h2-6)

## rtc-detect 库

您可以使用 [rtc-detect](https://www.npmjs.com/package/rtc-detect) 用来检测当前环境对 TRTC SDK 的支持度，以及当前环境的详细信息。

### 安装

```shell
npm install rtc-detect
```

### 使用方法

```javascript
import RTCDetect from 'rtc-detect';
// 初始化监测模块
const detect = new RTCDetect();
// 获得当前环境监测结果
const result = await detect.getReportAsync();
// result 包含了当前环境系统的信息，API 支持度，编解码支持度，设备相关的信息
console.log('result is: ' + result);
```

### API

#### (async) isTRTCSupported()

判断当前环境是否支持 TRTC。

```javascript
const detect = new RTCDetect();
const data = await detect.isTRTCSupported();

if (data.result) {
  console.log('current browser supports TRTC.')
} else {
  console.log(`current browser does not support TRTC, reason: ${data.reason}.`)
}
```

#### getSystem()

获取当前系统环境参数。

| Item                   | Type   | Description                     |
| ---------------------- | ------ | ------------------------------- |
| UA                     | string | 浏览器的 ua                     |
| OS                     | string | 当前设备的系统型号              |
| browser                | object | 当前浏览器信息{ name, version } |
| displayResolution      | object | 当前分辨率 { width, height }    |
| getHardwareConcurrency | number | 当前设备 CPU 核心数             |

```javascript
const detect = new RTCDetect();
const result = detect.getSystem();
```

#### getAPISupported()

获取当前环境 API 支持度。

| Item                              | Type    | Description                                           |
| --------------------------------- | ------- | ----------------------------------------------------- |
| isUserMediaSupported              | boolean | 是否支持获取用户媒体数据流                            |
| isWebRTCSupported                 | boolean | 是否支持 WebRTC                                       |
| isWebSocketSupported              | boolean | 是否支持 WebSocket                                    |
| isWebAudioSupported               | boolean | 是否支持 WebAudio                                     |
| isScreenCaptureAPISupported       | boolean | 是否支持获取屏幕的流                                  |
| isCanvasCapturingSupported        | boolean | 是否支持从 canvas 获取数据流                          |
| isVideoCapturingSupported         | boolean | 是否支持从 video 获取数据流                           |
| isRTPSenderReplaceTracksSupported | boolean | 是否支持替换 track 时不和 peerConnection 重新协商     |
| isApplyConstraintsSupported       | boolean | 是否支持变更摄像头的分辨率不通过重新调用 getUserMedia |

```javascript
const detect = new RTCDetect();
const result = detect.getAPISupported();
```

#### (async) getDevicesAsync()

获取当前环境可用的设备。

| Item                    | Type                | Description                                        |
|-------------------------|---------------------|----------------------------------------------------|
| hasWebCamPermissions    | boolean             | 是否支持获取用户摄像头数据                                      |
| hasMicrophonePermission | boolean             | 是否支持获取用户麦克风数据                                      |
| cameras                 | [array&lt;CameraItem&gt; ](#CameraItem)  | 用户的摄像头设备列表，包含支持视频流的分辨率信息，最大宽高以及最大帧率（最大帧率有部分浏览器不支持） |
| microphones             | [array&lt;DeviceItem&gt;](#DeviceItem)   | 用户的麦克风设备列表                                         |
| speakers                | [array&lt;DeviceItem&gt;](#DeviceItem)   | 用户的扬声器设备列表                                         |

**CameraItem**[](#CameraItem)

| Item       | Type    | Description                                                          |
|------------|---------|----------------------------------------------------------------------|
| deviceId   | string  | 设备 ID， 通常是唯一的，可以用于采集识别设备                                             |
| groupId    | string  | 组的标识符，如果两个设备属于同一个物理设备，他们就有相同的标识符                                     |
| kind       | string  | 摄像头设备类型：'videoinput'                                                 |
| label      | string  | 描述该设备的标签                                                             |
| resolution | object  | 摄像头支持的最大分辨率的宽高和帧率 {maxWidth：1280，maxHeight：720，maxFrameRate：30} |

**DeviceItem**[](id:DeviceItem)

| Item     | Type     | Description                          |
|----------|----------|--------------------------------------|
| deviceId | string   | 设备 ID， 通常是唯一的，可以用于采集识别设备             |
| groupId  | string   | 组的标识符，如果两个设备属于同一个物理设备，他们就有相同的标识符     |
| kind     | string   | 设备类型，例如：'audioinput'、'audiooutput' |
| label    | string   | 描述该设备的标签                             |

```javascript
const detect = new RTCDetect();
const result = await detect.getDevicesAsync();
```

#### (async) getCodecAsync()
获取当前环境参数对编码的支持度。

| Item                  | Type    | Description        |
| --------------------- | ------- | ------------------ |
| isH264EncodeSupported | boolean | 是否支持 h264 编码 |
| isH264DecodeSupported | boolean | 是否支持 h264 解码 |
| isVp8EncodeSupported  | boolean | 是否支持 vp8 编码  |
| isVp8DecodeSupported  | boolean | 是否支持 vp8 解码  |

支持编码即支持发布音视频，支持解码即支持拉取音视频播放。
```javascript
const detect = new RTCDetect();
const result = await detect.getCodecAsync();
```

#### (async) getReportAsync()

获取当前环境监测报告。

| Item            | Type   | Description                       |
| --------------- | ------ | --------------------------------- |
| system          | object | 和 getSystem() 的返回值一致       |
| APISupported    | object | 和 getAPISupported() 的返回值一致 |
| codecsSupported | object | 和 getCodecAsync() 的返回值一致   |
| devices         | object | 和 getDevicesAsync() 的返回值一致 |

```javascript
const detect = new RTCDetect();
const result = await detect.getReportAsync();
```

#### (async) isHardWareAccelerationEnabled()

检测 Chrome 浏览器是否开启硬件加速。

> !该接口的实现依赖于 WebRTC 原生接口，建议在 isTRTCSupported 检测支持后，再调用该接口进行检测。检测最长耗时 30s。经实测：
>   1. 开启硬件加速的情况下，该接口在 Windows 耗时 2s 左右， Mac 需耗时 10s 左右。
>   2. 关闭硬件加速的情况下，该接口在 Windows 和 Mac 耗时均为 30s。


```javascript
const detect = new RTCDetect();
const data = await detect.isTRTCSupported();

if (data.result) {
  const result = await detect.isHardWareAccelerationEnabled();
  console.log(`is hardware acceleration enabled: ${result}`);
} else {
  console.log(`current browser does not support TRTC, reason: ${data.reason}.`)
}
```


## 设备检测的 React 组件

### 设备检测 UI 组件特点

- 处理了设备连接及设备检测逻辑
- 处理了网络检测的逻辑
- 网络检测 Tab 页可选
- 支持中、英文两种语言

### 设备检测 UI 组件相关链接
- 组件 npm 包使用说明请参考：[rtc-device-detector-react](https://www.npmjs.com/package/rtc-device-detector-react)
- 组件源码调试请参考：[github/rtc-device-detector](https://github.com/FTTC/rtc-device-detector)
- 组件引用示例请参考：[WebRTC API Example](https://web.sdk.qcloud.com/trtc/webrtc/demo/api-sample/index.html)

### 设备检测 UI 组件界面
![](https://qcloudimg.tencent-cloud.cn/raw/64db21e3a56556446fa461a336bb8505.jpeg)

### 设备及网络检测逻辑
1. **设备连接**
设备连接的目的是检测用户使用的机器是否有摄像头，麦克风，扬声器设备，是否在联网状态。如果有摄像头，麦克风设备，尝试获取音视频流并引导用户授予摄像头，麦克风的访问权限。
	- 判断设备是否有摄像头，麦克风，扬声器设备
```javascript
import TRTC from 'trtc-js-sdk';

const cameraList = await TRTC.getCameras();
const micList = await TRTC.getMicrophones();
const speakerList = await TRTC.getSpeakers();
const hasCameraDevice = cameraList.length > 0;
const hasMicrophoneDevice = micList.length > 0;
const hasSpeakerDevice = speakerList.length > 0;
```
	- 获取摄像头，麦克风的访问权限
```javascript
navigator.mediaDevices
	.getUserMedia({ video: hasCameraDevice, audio: hasMicrophoneDevice })
	.then((stream) => {
		// 获取音视频流成功
		// ...
		// 释放摄像头，麦克风设备
		stream.getTracks().forEach(track => track.stop());
	})
	.catch((error) => {
		// 获取音视频流失败
	});
```
	- 判断设备是否联网
```javascript
export function isOnline() {
	const url = 'https://web.sdk.qcloud.com/trtc/webrtc/assets/trtc-logo.png';
	return new Promise((resolve) => {
		try {
			const xhr = new XMLHttpRequest();
			xhr.onload = function () {
				resolve(true);
			};
			xhr.onerror = function () {
				resolve(false);
			};
			xhr.open('GET', url, true);
			xhr.send();
		} catch (err) {
			// console.log(err);
		}
	});
}
const isOnline = await isOnline();
```
2. **摄像头检测**
摄像头检测为用户渲染了选中的摄像头采集的视频流，帮助用户确认摄像头是否可以正常使用。
	- 获取摄像头列表，默认使用摄像头列表中的第一个设备
```javascript
import TRTC from 'trtc-js-sdk';
let cameraList = await TRTC.getCameras();
let cameraId = cameraList[0].deviceId;
```
	- 初始化视频流并在 id 为 camera-video 的 dom 元素中播放流
```javascript
const localStream = TRTC.createStream({
	video: true,
	audio: false,
	cameraId,
});
await localStream.initialize();
localStream.play('camera-video');
```
	- 用户切换摄像头设备后更新流
```javascript
localStream.switchDevice('video', cameraId);
```
	- 监听设备插拔
```javascript
navigator.mediaDevices.addEventListener('devicechange', async () => {
	cameraList = await TRTC.getCameras();
		cameraId = cameraList[0].deviceId; 
	localStream.switchDevice('video', cameraId);
})
```
	- 检测完成后释放摄像头占用
```javascript
localStream.close();
```
3. **麦克风检测**
麦克风检测为用户渲染了选中的麦克风采集的音频流的音量，帮助用户确认麦克风是否可以正常使用。
	- 获取麦克风列表，默认使用麦克风列表中的第一个设备
```javascript
import TRTC from 'trtc-js-sdk';

let microphoneList = await TRTC.getMicrophones();
let microphoneId = microphoneList[0].deviceId;
```
	- 初始化音频流并在 id 为 audio-container 的 dom 元素中播放流
```javascript
const localStream = TRTC.createStream({
	video: false,
	audio: true,
	microphoneId,
});
await localStream.initialize();
localStream.play('audio-container');
timer = setInterval(() => {
	const volume = localStream.getAudioLevel();
}, 100);
```
	 - 用户切换麦克风设备后更新流
```javascript
// 获取用户新选中的 microphoneId
localStream.switchDevice('audio', microphoneId);
```
	- 监听设备插拔
```javascript
navigator.mediaDevices.addEventListener('devicechange', async () => {
	microphoneList = await TRTC.getMicrophones();
		microphoneId = microphoneList[0].deviceId;
	localStream.switchDevice('audio', microphoneId);
})
```
	- 检测完成后释放麦克风占用，停止音量监听
```javascript
localStream.close();
clearInterval(timer);
```
4. **扬声器检测**
扬声器检测提供了音频播放器，用户可以通过播放音频确认选中的扬声器是否可以正常使用。
	- 提供 mp3 播放器，提醒用户跳高设备播放音量，播放 mp3 确认扬声器设备是否正常
```html
<audio id="audio-player" src="xxxxx" controls></audio>
```
	- 检测结束后停止播放
```javascript
const audioPlayer = document.getElementById('audio-player');
if (!audioPlayer.paused) {
		audioPlayer.pause();
}
audioPlayer.currentTime = 0;
```
5. **网络检测**
	- 调用 [TRTC.createClient](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/TRTC.html#.createClient) 创建两个 Client，分别称为 uplinkClient 和 downlinkClient，这两个 Client 都进入同一个房间。
	- 使用 uplinkClient 进行推流，监听 [NETWORK_QUALITY](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/module-ClientEvent.html#.NETWORK_QUALITY) 事件来检测上行网络质量。
	- 使用 downlinkClient 进行拉流，监听 [NETWORK_QUALITY](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/module-ClientEvent.html#.NETWORK_QUALITY) 事件来检测下行网络质量。
整个过程可持续 15s 左右，最后取平均网络质量，从而大致判断出上下行网络情况。
> !检测过程将产生少量的[基础服务费用](https://cloud.tencent.com/document/product/647/17157#.E5.9F.BA.E7.A1.80.E6.9C.8D.E5.8A.A1)。如果未指定推流分辨率，则默认以 640*480 的分辨率推流。
>
```javascript
let uplinkClient = null; // 用于检测上行网络质量
let downlinkClient = null; // 用于检测下行网络质量
let localStream = null; // 用于测试的流
let testResult = {
  // 记录上行网络质量数据
  uplinkNetworkQualities: [],
  // 记录下行网络质量数据
  downlinkNetworkQualities: [],
  average: {
    uplinkNetworkQuality: 0,
    downlinkNetworkQuality: 0
  }
}

// 1. 检测上行网络质量
async function testUplinkNetworkQuality() {
  uplinkClient = TRTC.createClient({
    sdkAppId: 0, // 填写 sdkAppId
    userId: 'user_uplink_test',
    userSig: '', // uplink_test 的 userSig
    mode: 'rtc'
  });

  localStream = TRTC.createStream({ audio: true, video: true });
  // 根据实际业务场景设置 video profile
  localStream.setVideoProfile('480p'); 
  await localStream.initialize();

  uplinkClient.on('network-quality', event => {
    const { uplinkNetworkQuality } = event;
    testResult.uplinkNetworkQualities.push(uplinkNetworkQuality);
  });

  // 加入用于测试的房间，房间号需要随机，避免冲突
  await uplinkClient.join({ roomId: 8080 }); 
  await uplinkClient.publish(localStream);
}

// 2. 检测下行网络质量
async function testDownlinkNetworkQuality() {
  downlinkClient = TRTC.createClient({
    sdkAppId: 0, // 填写 sdkAppId
    userId: 'user_downlink_test',
    userSig: '', // userSig
    mode: 'rtc'
  });

  downlinkClient.on('stream-added', async event => {
    await downlinkClient.subscribe(event.stream, { audio: true, video: true });
		// 订阅成功后开始监听网络质量事件
    downlinkClient.on('network-quality', event => {
      const { downlinkNetworkQuality } = event;
      testResult.downlinkNetworkQualities.push(downlinkNetworkQuality);
    });
  })
  // 加入用于测试的房间，房间号需要随机，避免冲突
  await downlinkClient.join({ roomId: 8080 });
}

// 3. 开始检测
testUplinkNetworkQuality();
testDownlinkNetworkQuality();

// 4. 15s 后停止检测，计算平均网络质量
setTimeout(() => {
  // 计算上行平均网络质量
  if (testResult.uplinkNetworkQualities.length > 0) {
    testResult.average.uplinkNetworkQuality = Math.ceil(
      testResult.uplinkNetworkQualities.reduce((value, current) => value + current, 0) / testResult.uplinkNetworkQualities.length
    );
  }

  if (testResult.downlinkNetworkQualities.length > 0) {
    // 计算下行平均网络质量
    testResult.average.downlinkNetworkQuality = Math.ceil(
      testResult.downlinkNetworkQualities.reduce((value, current) => value + current, 0) / testResult.downlinkNetworkQualities.length
    );
  }
    
  // 检测结束，清理相关状态。
  uplinkClient.leave();
  downlinkClient.leave();
  localStream.close();
}, 15 * 1000);
```

## TRTC 能力检测页面

您可以在当前使用 TRTC SDK 的地方，使用 [TRTC 检测页面](https://web.sdk.qcloud.com/trtc/webrtc/demo/detect/index.html) ，可用于探测当前环境，还可以点击生成报告按钮，得到当前环境的报告，用于环境检测，或者问题排查。

