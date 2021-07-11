直播推流接口主要是通过浏览器采集用户的画面和声音，并通过 WebRTC 进行推送。

### checkSupport

静态函数，检查浏览器支持性。

```typescript
static checkSupport(): Promise<SupportResult>;
```

**返回**

返回 Promise 对象，其中检查结果 `SupportResult` 结构如下：

| 字段                     | 类型    | 描述                         |
| ------------------------ | ------- | ---------------------------- |
| isWebRTCSupported        | boolean | 是否支持 WebRTC              |
| isH264EncodeSupported    | boolean | 是否支持 H264 编码           |
| isH264DecodeSupported    | boolean | 是否支持 H264 解码           |
| isMediaDevicesSupported  | boolean | 是否支持获取媒体设备及媒体流 |
| isScreenCaptureSupported | boolean | 是否支持屏幕采集             |
| isMediaFileSupported     | boolean | 是否支持获取本地媒体文件流   |

---

### setRenderView

设置本地视频画面的预览容器，提供一个 div 节点，本地采集的视频会在容器里渲染。

```typescript
setRenderView(container: string | HTMLDivElement): void;
```

**参数**

`container`：容器的 ID 或者 dom 节点。

---

### setVideoQuality

设置推流视频质量，SDK 已经内置了视频质量模板，直接通过预定义的模板来设置推流视频质量。

```typescript
setVideoQuality(quality: string): void;
```

**参数**

`quality` 预定义的视频质量模板名称。内置的视频质量模板如下所示：

| 模板名 | 分辨率（宽 × 高） | 帧率（fps） | 码率（kbps） |
| ------ | ----------------- | ----------- | ------------ |
| 120p   | 160 × 120         | 15          | 200          |
| 180p   | 320 × 180         | 15          | 350          |
| 240p   | 320 × 240         | 15          | 400          |
| 360p   | 640 × 360         | 15          | 800          |
| 480p   | 640 × 480         | 15          | 900          |
| 720p   | 1280 × 720        | 15          | 1500         |
| 1080p  | 1920 × 1080       | 15          | 2000         |
| 2K     | 2560 × 1440       | 30          | 4860         |
| 4K     | 3840 × 2160       | 30          | 9000         |

**说明**

- 由于设备和浏览器的限制，视频分辨率不一定能够完全匹配，在这种情况下，浏览器会自动调整分辨率使其接近对应的分辨率。
- 如果以上视频质量参数（分辨率、帧率和码率）不符合您的要求，您可以通过 `setProperty` 单独设置自定义的值。
- 默认使用 `720p` ，即 `setVideoQuality('720p')` 。

---

### setAudioQuality

设置推流音频质量，SDK 已经内置了音频质量模板，直接通过预定义的模板来设置推流音频质量。

```typescript
setAudioQuality(quality: string): void;
```

**参数**

`quality` 预定义的音频质量模板名称。内置的音频质量模板如下所示：

| 模板名   | 采样率 | 码率（kbps） |
| -------- | ------ | ------------ |
| standard | 48000  | 40           |
| high     | 48000  | 128          |

**说明**

默认使用 `standard`，即 `setAudioQuality('standard')` 。

---

### setProperty

主要用于调用一些高级功能例如设置视频的分辨率、帧率和码率。

```typescript
setProperty(key: string, value: any): void;
```

**参数**

- `key` 高级 API 对应的 key。
- `value` 调用 key 所对应的高级 API 时，需要的参数。

**说明**
目前支持以下高级功能：
<table>
<tr><th>Key</th><th>Value</th><th>描述</th><th>示例</th></tr><tr>
<td>setVideoResolution</td>
<td>{<br>width: number;<br>height:number;<br>}</td>
<td>设置视频的分辨率</td>
<td>setProperty('setVideoResolution', { width: 1920, height: 1080 })</td>
</tr><tr>
<td>setVideoFPS</td>
<td>number</td>
<td>设置视频的帧率</td>
<td>setProperty('setVideoFPS', 25)</td>
</tr><tr>
<td>setVideoBitrate</td>
<td>number</td>
<td>设置视频的码率</td>
<td>setProperty('setVideoBitrate', 2000)</td>
</tr><tr>
<td>setAudioSampleRate</td>
<td>number</td>
<td>设置音频的采样率</td>
<td>setProperty('setAudioSampleRate', 44100)</td>
</tr><tr>
<td>setAudioBitrate</td>
<td>number</td>
<td>设置音频的码率</td>
<td>setProperty('setAudioBitrate', 200)</td>
</tr><tr>
<td>setConnectRetryCount</td>
<td>number</td>
<td>设置连接重试次数<ul style="margin:0"><li/>默认值：3，取值范围[0,10]<li/>当 SDK 与服务器异常断开连接时，SDK 会尝试与服务器重连</td>
<td>setProperty('setConnectRetryCount', 5)</td>
</tr><tr>
<td>setConnectRetryDelay</td>
<td>number</td>
<td>设置连接重试延迟<ul style="margin:0"><li/>默认值：1，单位为秒；取值范围[0,10]<li/>当 SDK 与服务器异常断开连接时， SDK 会尝试与服务器重连</td>
<td>setProperty('setConnectRetryDelay', 2)</td>
</tr></table>

>! 请在采集流和推流之前进行设置。

---

### startCamera

打开本地摄像头设备。需要用户授权允许浏览器访问摄像头，授权失败或者访问设备失败，会通过回调接口抛出警告通知。

```typescript
startCamera(deviceId?: string): void;
```

**参数**

`deviceId`：摄像头设备 ID，可选参数，指定打开的摄像头设备。设备 ID 可通过 TXDeviceManager 中的方法 [getDevicesList](https://cloud.tencent.com/document/product/454/56501#getdeviceslist) 获取。

---

### stopCamera

关闭本地摄像头设备。

```typescript
stopCamera(): void;
```

---

### startMicrophone

打开麦克风设备。需要用户授权允许浏览器访问麦克风，授权失败或者访问设备失败，会通过回调接口抛出警告通知。

```typescript
startMicrophone(deviceId?: string): void;
```

**参数**

`deviceId`：麦克风设备 ID，可选参数，指定打开的麦克风设备。设备 ID 可通过 TXDeviceManager 中的方法 [getDevicesList](https://cloud.tencent.com/document/product/454/56501#getdeviceslist) 获取。

---

### stopMicrophone

关闭麦克风设备。

```typescript
stopMicrophone(): void;
```

---

### startScreenCapture

开启屏幕采集。需要用户授权允许浏览器访问屏幕，授权失败或者访问设备失败，会通过回调接口抛出警告通知。

```typescript
startScreenCapture(): void;
```

---

### stopScreenCapture

关闭屏幕采集。

```typescript
stopScreenCapture(): void;
```

---

### startMediaFile

开始采集本地媒体文件流。将用户本地的 MP4 视频文件转换成音视频流。

```typescript
startMediaFile(file?: File): void;
```

**参数**

`file`：可选，本地媒体文件，不传则 javascript 模拟触发文件上传操作。

**说明**

- 需要先调用 [setRenderView](#setrenderview) 方法设置承载本地视频画面的 div 容器。
- 本地视频文件当前仅支持 MP4 文件。
- safari 浏览器限制，javascript 模拟触发文件上传操作可能不生效，建议手动传入 file 对象。
- 浏览器限制，页面处于未激活状态时（最小化、激活其它标签页），采集文件流会暂停。建议提示用户推流过程中不要切换浏览器标签页。

---

### stopMediaFile

停止采集本地媒体文件流，结束本地文件播放。

```typescript
stopMediaFile(): void;
```

---

### startPush

开始音视频数据推流，建立 WebRTC 连接，往腾讯云服务器推送数据。

```typescript
startPush(pushUrl: string): void;
```

**参数**

`pushUrl`：WebRTC 推流地址，请填写腾讯云的推流地址。推流地址的格式参见 [腾讯云标准直播 URL](https://cloud.tencent.com/document/product/267/32720) ，只需要将 RTMP 推流地址前面的 `rtmp://` 替换成 `webrtc://` 即可。

---

### stopPush

停止推送音视频数据，关闭 WebRTC 连接。

```typescript
stopPush(): void;
```

---

### isPushing

查询当前推流器是否正在推流中。

```typescript
isPushing(): boolean;
```

**返回**

true：正在推流；false：未推流。

---

### getDeviceManager

获取设备管理对象。通过设备管理，可以进行查询设备列表，切换设备等操作。

```typescript
getDeviceManager(): TXDeviceManager;
```

**返回**

`TXDeviceManager` 实例对象。具体参见 [TXDeviceManager](https://cloud.tencent.com/document/product/454/56501) 。

---

### setVideoMute

设置是否禁用视频流。

```typescript
setVideoMute(mute: boolean): void;
```

**参数**

`mute`：true - 禁用，false - 启用。

**说明**

- 只有当前有视频流时，设置才会生效。
- 禁用之后每一帧都会用黑色像素填充，实际上仍在采集视频流。

---

### setAudioMute

设置是否禁用音频流。

```typescript
setAudioMute(mute: boolean): void;
```

**参数**

`mute`：true - 禁用，false - 启用。

**说明**

- 只有当前有音频流时，设置才会生效。
- 禁用之后每一帧都是没有声音的，实际上仍在采集音频流。

---

### setObserver

设置推流器回调。通过设置回调，可以监听推流器的一些回调事件，包括推流器状态、统计数据、警告和错误信息等。

```typescript
setObserver(observer: TXLivePusherObserver): void;
```

**参数**

`observer`：推流器的回调目标对象。具体请参见 [TXLivePusherObserver](https://cloud.tencent.com/document/product/454/56500)。

---

### destroy

离开页面或者退出时，清理 SDK 实例，避免可能会产生的内存泄露，调用前先执行 stop 方法。

```typescript
destroy(): void;
```


