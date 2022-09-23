腾讯云直播推流的回调通知，回调包括推流器状态，统计信息，警告以及错误信息。
  
### onError

直播推流器错误通知，推流器出现错误时，会回调该通知。

```typescript
onError(code: number, msg: string, extraInfo: Object): void;
```

**参数**

- `code`：错误码，请参见 [推流错误码](#errocode)。
- `msg`：错误信息。
- `extraInfo`：扩展信息，目前未用到。

---

### onWarning

直播推流器警告通知。

```typescript
onWarning(code: number, msg: string, extraInfo: Object): void;
```

**参数**

- `code`：错误码，请参见 [推流错误码](#errocode) 。
- `msg`：错误信息。
- `extraInfo`：扩展信息，目前未用到。

**说明**

打开摄像头、麦克风、屏幕录制失败时返回的错误信息，可参见 [getUserMedia 异常](https://developer.mozilla.org/zh-CN/docs/Web/API/MediaDevices/getUserMedia#%E5%BC%82%E5%B8%B8) 和 [getDisplayMedia 异常](https://developer.mozilla.org/zh-CN/docs/Web/API/MediaDevices/getDisplayMedia#%E5%BC%82%E5%B8%B8) 。

---

### onCaptureFirstAudioFrame

首帧音频采集完成的回调通知。

```typescript
onCaptureFirstAudioFrame(): void;
```

---

### onCaptureFirstVideoFrame

首帧视频采集完成的回调通知。

```typescript
onCaptureFirstVideoFrame(): void;
```

---

### onPushStatusUpdate

推流器连接状态回调通知。

```typescript
onPushStatusUpdate(status: number, msg: string, extraInfo: Object): void;
```

**参数**

- `status`：连接状态码，请参见 [推流状态码](#pushstate)。
- `msg`：连接状态信息。
- `extraInfo`：扩展信息，目前未用到。

---

### onStatisticsUpdate

直播推流器统计数据回调，主要是 WebRTC 相关的统计数据，不同浏览器返回的数据可能不一致。

```typescript
onStatisticsUpdate(statistics: Object): void;
```

**参数**

`statistics`：推流统计数据，请参见 [推流统计数据](#pushdate)。

---

[](id:errocode)

### 推流错误码

[onError](#onerror) 和 [onWarning](#onwarning) 中用到的错误码如下：

| 枚举值                                     | 数值  | 描述                       |
| ------------------------------------------ | ----- | -------------------------- |
| TXLIVE_ERROR_WEBRTC_FAILED                 | -1    | WebRTC 接口调用失败        |
| TXLIVE_ERROR_REQUEST_FAILED                | -2    | 请求服务器推流接口返回报错 |
| TXLIVE_WARNING_CAMERA_START_FAILED         | -1001 | 打开摄像头失败             |
| TXLIVE_WARNING_MICROPHONE_START_FAILED     | -1002 | 打开麦克风失败             |
| TXLIVE_WARNING_SCREEN_CAPTURE_START_FAILED | -1003 | 打开屏幕录制失败           |
| TXLIVE_WARNING_MEDIA_FILE_START_FAILED     | -1004 | 打开本地媒体文件失败       |
| TXLIVE_WARNING_CAMERA_INTERRUPTED     | -1005 | 摄像头被中断（设备被拔出或者权限被用户取消）       |
| TXLIVE_WARNING_MICROPHONE_INTERRUPTED     | -1006 | 麦克风被中断（设备被拔出或者权限被用户取消）       |
| TXLIVE_WARNING_SCREEN_CAPTURE_INTERRUPTED     | -1007 | 屏幕录制被中断（Chrome 浏览器单击自带的停止共享按钮）      |

---

[](id:pushstate)

### 推流状态码

[onPushStatusUpdate](#onpushstatusppdate ) 用到的状态码如下：

| 枚举值                             | 数值 | 描述             |
| ---------------------------------- | ---- | ---------------- |
| TXLIVE_PUSH_STATUS_DISCONNECTED    | 0    | 与服务器断开连接 |
| TXLIVE_PUSH_STATUS_CONNECTING      | 1    | 正在连接服务器   |
| TXLIVE_PUSH_STATUS_CONNECT_SUCCESS | 2    | 连接服务器成功   |
| TXLIVE_PUSH_STATUS_RECONNECTING    | 3    | 重连服务器中     |

---

[](id:pushdate)

### 推流统计数据

通过 [onStatisticsUpdate](#onstatisticsupdate ) 回调接口可以监听直播推流过程中 WebRTC 相关的统计数据。SDK 会以一秒一次的频率统计数据，返回的对象基本结构如下：

| 字段            | 说明                                                |
| --------------- | --------------------------------------------------- |
| timestamp       | 数据采样的时间，自1970年1月1日（UTC）起经过的毫秒数 |
| [video](#video) | 视频流相关的数据                                    |
| [audio](#audio) | 音频流相关的数据                                    |

#### video

| 字段               | 说明                                                        |
| ------------------ | ----------------------------------------------------------- |
| bitrate            | 视频码率，单位：bit/s                                       |
| framesPerSecond    | 视频帧率                                                    |
| frameWidth         | 视频宽度，Firefox下不存在                                   |
| frameHeight        | 视频高度，Firefox下不存在                                   |
| framesEncoded      | 编码帧数                                                    |
| framesSent         | 发送帧数，Firefox下不存在                                   |
| packetsSent        | 发送包数                                                    |
| nackCount          | NACK（Negative ACKnowledgement）数                          |
| firCount           | FIR（Full Intra Request），关键帧重传请求数                 |
| pliCount           | PLI（Picture Loss Indication），视频帧丢失重传数            |
| frameEncodeAvgTime | 平均编码时间，单位：ms，Safari / Firefox 下不存在            |
| packetSendDelay    | 数据包发送之前本地缓存的平均时间，单位：ms，Firefox 下不存在 |

---

#### audio

| 字段        | 说明                  |
| ----------- | --------------------- |
| bitrate     | 音频码率，单位：bit/s |
| packetsSent | 发送包数              |
