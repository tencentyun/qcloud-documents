## 组件介绍

**&lt;trtc-room&gt;** 标签是基于 &lt;live-pusher&gt; 和 &lt;live-player&gt; 实现的用于 TRTC 互通的自定义组件，支持多种应用场景：

**视频通话&语音通话（scene = "rtc"）**
- 视频通话场景，支持 [720P、1080P](#quality) 高清画质。
- 视频通话场景，支持48kHz全频带，支持双声道。
- 单个房间最多支持300人同时在线，最高支持30人同时发言。
- 适用场景：1对1视频通话、300人视频会议、在线问诊、远程面试、视频客服、在线狼人杀等。
- 使用方法：需要您将 &lt;trtc-room&gt; 的 [scene](#Config) 属性设置为 **rtc**。

**互动直播&语音聊天室（scene = "live"）**
- 支持十万人级别观众同时播放，播放延时低至1000ms。
- 支持平滑上下麦，切换过程无需等待，主播延时小于300ms。
- 适用场景：视频低延时直播、十万人互动课堂、视频相亲、在线教育、远程培训、超大型会议等。
- 使用方法：使用时需要您将 &lt;trtc-room&gt; 的 [scene](#Config) 属性设置为 **live**。

<table>
<tr>
<td><img width="260" height="561" src="https://demovideo-1252463788.cos.ap-shanghai.myqcloud.com/trtcvoiceroom.gif"/></td>
<td><img width="260" height="561" src="https://demovideo-1252463788.cos.ap-shanghai.myqcloud.com/trtcvideocall.gif"/></td>
<td><img width="260" height="561" src="https://demovideo-1252463788.cos.ap-shanghai.myqcloud.com/trtcmeeting1.gif"/></td>
<td><img width="260" height="561" src="https://demovideo-1252463788.cos.ap-shanghai.myqcloud.com/trtcmeeting2.gif"/></td>
</tr>
</table>


<h2 id="API">API 概览</h2>

**基础方法**

| API | 描述 |
|-----|-----|
| [on(EventCode, handler, context)](#on(eventcode.2C-handler.2C-context)) | 用于监听组件派发的事件，详细事件请参考 [事件表](#Event)。 |
| [off(EventCode, handler)](#off(eventcode.2C-handler))|取消事件监听。|
| [enterRoom(params)](#enterroom(params)) | 进入房间，若房间不存在，系统将自动创建一个新房间。|
| [exitRoom()](#exitroom()) | 停止推流和取消订阅所有远端音视频，并退出房间。|

**发布订阅**

| API | 描述 |
|-----|-----|
| [publishLocalVideo()](#publishlocalvideo()) | 发布本地视频，即开启本地摄像头采集并启动视频推流。 |
| [unpublishLocalVideo()](#unpublishlocalvideo()) | 取消发布本地视频，关闭本地视频推流。 |
| [publishLocalAudio()](#publishlocalaudio())|发布本地音频，即开启本地麦克风采集并启动音频推流。|
| [unpublishLocalAudio()](#unpublishlocalaudio()) | 取消发布本地音频，关闭本地音频推流。|
| [subscribeRemoteVideo(params)](#subscriberemotevideo(params)) | 订阅远端用户的视频流并进行播放。|
| [unsubscribeRemoteVideo(params)](#unsubscriberemotevideo(params)) | 取消订阅远端用户的视频并停止播放。|
| [subscribeRemoteAudio(params)](#subscriberemoteaudio(params)) | 订阅远端用户的音频并进行播放。|
| [unsubscribeRemoteAudio(params)](#unsubscriberemoteaudio(params)) | 取消订阅远端用户的音频并且停止播放。|
| [getRemoteUserList()](#getremoteuserlist()) | 获取远端用户列表。|

**视图控制**

| API | 描述 |
|-----|-----|
| [enterFullscreen(params)](#enterfullscreen(params)) | 将远端视频切换为全屏播放，辅路（即屏幕分享）的画面一般适合全屏播放。 |
| [exitFullscreen(params)](#exitfullscreen(params)) | 取消远端视频的全屏模式。 |
| [setViewOrientation(params)](#setvieworientation(params))|设置指定远端画面的显示方向。|
| [setViewFillMode(params)](#setviewfillmode(params))|设置指定远端画面的填充模式。|
| [setViewVisible(params)](#setviewvisible(params))|显示或者隐藏某一路视频画面。|
| [setViewRect(params)](#setviewrect(params))|设置指定视频画面的坐标和尺寸。|
| [setViewZIndex(params)](#setviewzindex(params))|设置指定视频画面的层级。|

**背景音乐**

| API | 描述 |
|-----|-----|
| [playBGM(params)](#playbgm(params)) | 播放背景音乐。背景音乐会同麦克风采集的人声混合在一起发布到云端，即“背景混音”。 |
| [stopBGM()](#stopbgm()) | 停止播放背景音乐。 |
| [pauseBGM()](#pausebgm()) | 暂停播放背景音乐。 |
| [resumeBGM()](#resumebgm()) | 恢复播放背景音乐。 |
| [setBGMVolume(params)](#setbgmvolume(params))|设置混音中背景音乐的音量。|
| [setMICVolume(params)](#setmicvolume(params))|设置混音中麦克风采集的音量。|

**消息收发**
消息收发功能需开通 [即时通信 IM](https://cloud.tencent.com/product/im) 服务并将 [属性表](#Config) 中的 enableIM 选项设置为 true 才有效。

| API | 描述 |
|-----|-----|
| [sendC2CTextMessage(params)](#sendc2ctextmessage(params)) | 发送 C2C（即定向发给某个人）文本消息。 |
| [sendC2CCustomMessage(params)](#sendc2ccustommessage(params)) | 发送 C2C 自定义消息，自定义消息可以用来发送控制信令（例如邀请发言、申请上麦等）。 |
| [sendGroupTextMessage(params)](#sendgrouptextmessage(params)) | 发送群组文本消息。 |
| [sendGroupCustomMessage(params)](#sendgroupcustommessage(params)) | 发送群组自定义消息。 |

**其他功能**

| API | 描述 |
|-----|-----|
| [switchCamera()](#switchcamera()) | 切换本地前后摄像头。|
| [snapshot()](#snapshot(params)) | 截取指定远端视频或本地视频的图像，并保存到系统相册中。|


<h2 id="Config">属性表</h2>
&lt;trtc-room&gt; 只有一个 config 属性，通过该属性可以传入以下参数：

| 参数                 | 类型    | 默认值    | 说明         |
|:---------------------|:--------|:----------|:-------------|
| scene                | String  | rtc       | 必填参数，使用场景：<li>rtc：实时通话，采用优质线路，同一房间中的人数不应超过300人。</li><li>live：直播模式，采用混合线路，支持单一房间十万人在线（同时上麦的人数应控制在20人以内）。</li>  |
| sdkAppID             | String  | -         | 必填参数，开通实时音视频服务创建应用后分配的 SDKAppID。            |
| userID               | String  | -         | 必填参数，用户 ID，可以由您的帐号体系指定。 |
| userSig              | String  | -         | 必填参数，身份签名（即相当于登录密码），由 userID 计算得出，具体计算方法请参见 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。    |
| template             | String  | custom    | 必填参数，组件内置的画面排版模式，支持如下三种模式：<li>"1v1"：大小画面上下叠加。</li><li>"grid"：网格模版，画面间相互重叠，最多显示9路画面。</li><li>"custom"：自定义，需要您修改组件的 custom.wxml 模版</li>  |
| enableCamera         | Boolean | false     | 是否开启摄像头。设置为 true 时，调用 enterRoom 后，会自动发布视频   |
| enableMic            | Boolean | false     | 是否开启麦克风。设置为 true 时，调用 enterRoom 后，会自动发布音频   |
| enableAgc            | Boolean | false     | 是否开启音频自动增益，该特性可以补偿部分手机麦克风音量太小的问题，但也会放大噪音，建议配合 ANS 同时开启。|
| enableAns            | Boolean | false     | 是否开启音频噪声抑制，该特性会自动检测背景噪音并进行过滤，但也会误伤周围的音乐，只有会议、教学等场景才适合开启。    |
| enableEarMonitor     | Boolean | false     | 是否开启耳返（目前仅在 iOS 平台有效）。    |
| enableAutoFocus      | Boolean | true      | 是否开启摄像头自动对焦，如果关闭则需要用户手动点击摄像头中的预览画面进行对焦。 |
| enableZoom           | Boolean | false     | 是否支持双手滑动调整摄像头焦距。    |
| minBitrate<span id="quality"></span>          | String  | 200       | 最小码率，不建议设置太低。  |
| maxBitrate           | String  | 1000      | 最大码率，需要跟分辨率相匹配，建议参考 [分辨率码率参照表](https://cloud.tencent.com/document/product/647/32236#.E5.88.86.E8.BE.A8.E7.8E.87.E7.A0.81.E7.8E.87.E5.8F.82.E7.85.A7.E8.A1.A8)。 |
| videoWidth           | String  | 360       | 视频宽，若设置视频宽高，会忽略 aspect。  |
| videoHeight          | String  | 640       | 视频高，若设置视频宽高，会忽略 aspect。  |
| beautyLevel          | Number  | 0         | 美颜，取值范围 0-9，0表示关闭。 |
| whitenessLevel       | Number  | 0         | 美白，取值范围 0-9，0表示关闭。 |
| videoOrientation     | String  | vertical  | 设置本地画面方向，可选值：vertical 或 horizontal。 |
| videoAspect          | String  | 9:16      | 宽高比，可选值：3:4 或 9:16。  |
| frontCamera          | String  | front     | 设置前置还是后置摄像头，可选值：front 或 back。 |
| enableRemoteMirror   | Boolean | false     | 设置观众端看到的画面的镜像效果，该属性的变化不会影响到本地画面，仅影响观众端看到的画面效果。 |
| localMirror          | String  | auto      | 设置主播本地摄像头预览画面的镜像效果，支持如下取值：<li>auto：前置摄像头镜像，后置摄像头不镜像（系统相机的表现）。</li><li>enable：前置摄像头和后置摄像头都镜像。</li><li>disable： 前置摄像头和后置摄像头都不镜像。</li>|
| enableBackgroundMute | Boolean | false     | 设置主播端小程序切入后台时是否暂停声音的采集。 |
| audioQuality         | String  | high      | 高音质（48KHz）或低音质（16KHz），可选值：high 或 low。 |
| audioVolumeType      | String  | voicecall | 系统音量类型，可选值为：<li>media：媒体音量。</li><li>voicecall：通话音量。</li>|
| audioReverbType      | Number  | 0         | 音频混响类型，可选值为： 0：关闭，1：KTV，2：小房间，3：大会堂，4：低沉，5：洪亮，6：金属声，7：磁性。|
| enableIM             | Boolean | false     | 是否启用即时通信功能 |
| debugMode            | Boolean | false     | 是否打开组件的调试模式，开启后视频画面上会有一个半透明浮层展示音视频数据指标。    |


示例代码：
``` 
 // index.wxml
<trtc-room id="trtcroom" config="{{trtcConfig}}"></trtc-room>
```

```
// videocall.js
trtcConfig = {
  sdkAppID: '1401000123', // 开通实时音视频服务创建应用后分配的 SDKAppID
  userID: 'test_user_001', // 用户 ID，可以由您的帐号系统指定
  userSig: 'xxxxxxxxxxxx', // 身份签名，相当于登录密码的作用
  template: 'grid', // 画面排版模式
}
```

## 组件方法

### selectComponent()
您可以通过小程序提供的 this.selectComponent() 方法获取组件实例。

示例代码：

```
let trtcRoomContext = this.selectComponent('#trtcroom')
trtcRoomContext.enterRoom({roomID: 2233})
```

### on(EventCode, handler, context)

**说明：**

用于监听组件派发的事件，详细事件请参考 [事件表](#Event)。
>! 请在调用 enterRoom 前监听事件，避免漏掉组件派发的事件。

**参数：**

| 参数名    | 类型     | 默认值 | 说明           |
|:----------|:---------|:-------|:-------------|
| EventCode | String   | -      | 事件码         |
| handler   | Function | -      | 监听函数       |
| context   | Object   | -      | 当前执行上下文 |

**返回值：**

无

**示例代码：**
```
function onLocalJoin(event) {
  // 本地进房成功
}
trtcRoomContext.on(trtcRoomContext.EVENT.LOCAL_JOIN, onLocalJoin, this)
```

### off(EventCode, handler)

**说明：**

取消事件监听。

**参数：**

| 参数名    | 类型     | 默认值 | 说明                   |
|:----------|:---------|:-------|:---------------------|
| EventCode | String   | -      | 事件码                 |
| handler   | Function | -      | 需要取消的具名监听函数 |

**返回值：**

无

**示例代码：**
```
function onLocalJoin(event) {
  // 本地进房成功
}
trtcRoomContext.off(trtcRoomContext.EVENT.LOCAL_JOIN, onLocalJoin)
```

### enterRoom(params)

**说明：**
进入房间，调用参数必须传入 roomID。

**参数：**

| 参数名 | 类型   | 默认值 | 说明                                         |
|:-------|:-------|:-------|:-------------------------------------------|
| roomID | Number | -      | 房间 ID，由您的系统决定，取值范围1 - 4294967295 |

**返回值：**
Promise

**示例代码：**
```
trtcRoomContext.enterRoom({roomID: 2233}).catch((error)=>{
  // 进入房间失败
  // 注意：进入房间成功通过事件 LOCAL_JOIN 通知
})
```

### exitRoom()
**说明：**

停止推流和取消订阅所有远端音视频，并退出房间。

>! 由于微信最新版本小程序引擎限制，请勿在 onHide() 回调函数中调用 exitRoom()，会导致各种状态紊乱的 bug。

**参数：**

无

**返回值：**

Promise

**示例代码：**
```
trtcRoomContext.exitRoom().then(()=>{
  // 退出房间成功
})
```

### publishLocalVideo()
**说明：**

发布本地视频，即开启本地摄像头采集并启动视频推流。一般要配合 `publishLocalAudio()` 一起使用。

**参数：**

无

**返回值：**

Promise

**示例代码：**
```
trtcRoomContext.publishLocalVideo().then(()=>{
  // 发布成功
})
```

### unpublishLocalVideo()
**说明：**

取消发布本地视频，关闭本地视频推流。

**参数：**

无

**返回值：**

Promise

**示例代码：**
```
trtcRoomContext.unpublishLocalVideo().then(()=>{
  // 取消发布成功
})
```

### publishLocalAudio()
**说明：**

发布本地音频，即开启本地麦克风采集并启动音频推流。如果是纯音频沟通场景，则不需要调用`publishLocalVideo()`。 

**参数：**

无

**返回值：**

Promise

**示例代码：**
```
trtcRoomContext.publishLocalAudio().then(()=>{
  // 发布成功
})
```

### unpublishLocalAudio()
**说明：**

取消发布本地音频，关闭本地音频推流。

**参数：**

无

**返回值：**

Promise

**示例代码：**
```
trtcRoomContext.unpublishLocalAudio().then(()=>{
  // 取消发布成功
})
```

### subscribeRemoteVideo(params)
**说明：**

订阅远端用户的视频流并进行播放。

**参数：**

| 参数名     | 类型   | 默认值 | 说明                                                                                           |
|:-----------|:-------|:-------|:---------------------------------------------------------------------------------------------|
| userID     | String | -      | 必填参数，远端用户 ID，通过组件通知的 REMOTE_VIDEO_ADD 事件，可以获知（可以订阅的）远端视频流的 userID 和 streamType。 |
| streamType | String | -      | 必填参数，远端用户的流类型，可选值：<li> main：大画面。</li><li>small：小画面。</li><li>aux：辅流（即屏幕分享）。 |

**返回值：**

Promise

**示例代码：**

```
// 有可以订阅的远端视频流
function onRemoteVideoAdd(event) {
  trtcRoomContext.subscribeRemoteVideo({
    userID: event.data.userID,
    streamType: event.data.streamType
  }).then(()=>{
    // 订阅成功
  })
}

trtcRoomContext.on(trtcRoomContext.EVENT.REMOTE_VIDEO_ADD, onRemoteVideoAdd)
```

### unsubscribeRemoteVideo(params)
**说明：**

取消订阅远端用户的视频并停止播放。

**参数：**

| 参数名     | 类型   | 默认值 | 说明                                                              |
|:-----------|:-------|:-------|:----------------------------------------------------------------|
| userID     | String | -      | 必填参数，远端用户 ID，通过组件通知的 REMOTE_VIDEO_REMOVE 事件，可以获知（取消发布的）远端视频流的 userID 和 streamType。   |
| streamType | String | -      | 必填参数，远端用户的流类型，可选值：<li>main：大画面。</li><li>aux：辅流（即屏幕分享）。</li> |

**返回值：**

Promise

**示例代码：**

```
// 有一路远端视频流关闭了
function onRemoteVideoRemove(event) {
  trtcRoomContext.unsubscribeRemoteVideo({
    userID: event.data.userID,
    streamType: event.data.streamType
  }).then(()=>{
    // 取消订阅成功
  })
}
trtcRoomContext.on(trtcRoomContext.EVENT.REMOTE_VIDEO_REMOVE, onRemoteVideoRemove)
```

### subscribeRemoteAudio(params)
**说明：**

订阅远端用户的音频并进行播放。

**参数：**

| 参数名 | 类型   | 默认值 | 说明                                                  |
|:-------|:-------|:-------|:----------------------------------------------------|
| userID | String | -      | 远端用户 ID，通过组件通知的 REMOTE_AUDIO_ADD 事件，可以获知（可以订阅的）远端音频流的 userID。 |

**返回值：**

Promise

**示例代码：**
```
// 有可以订阅的远端音频流
function onRemoteAudioAdd(event) {
  trtcRoomContext.subscribeRemoteAudio({
    userID: event.data.userID
  }).then(()=>{
    // 订阅成功
  })
}

trtcRoomContext.on(trtcRoomContext.EVENT.REMOTE_AUDIO_ADD, onRemoteAudioAdd)
```

### unsubscribeRemoteAudio(params)
**说明：**

取消订阅远端用户的音频并停止播放 。

**参数：**

| 参数名 | 类型   | 默认值 | 说明                                                     |
|:-------|:-------|:-------|:-------------------------------------------------------|
| userID | String | -      | 远端用户 ID，通过组件派发的事件 REMOTE_AUDIO_REMOVE 可以获知（取消发布的）远端音频流的 userID。 |

**返回值：**

Promise

**示例代码：**
```
// 有一路远端音频流关闭了
function onRemoteAudioRemove(event) {
  trtcRoomContext.unsubscribeRemoteAudio({
    userID: event.data.userID
  }).then(()=>{
    // 取消订阅成功
  })
}

trtcRoomContext.on(trtcRoomContext.EVENT.REMOTE_AUDIO_REMOVE, onRemoteAudioRemove)
```

### switchCamera()
**说明：**

切换本地前后摄像头。

**参数：**

无

**返回值：**

无

**示例代码：**
```
trtcRoomContext.switchCamera()
```

### getRemoteUserList()
**说明：**

获取远端用户列表。

**参数：**

无

**返回值：**

Array[Object]

**示例代码：**
```
let userList = trtcRoomContext.getRemoteUserList()
// 数据格式示例
// userList = [
//   {
//     userID:'xxx',       // 该用户 ID 
//     hasMainVideo: true, // 该用户是否有主流视频
//     hasMainAudio: true, // 该用户是否有主流音频
//     hasAuxVideo: false  // 该用户是否有辅流（屏幕分享）视频
//   }
//   ...
// ]
```

### enterFullscreen(params)
**说明：**

将远端视频切换为全屏播放，辅路（即屏幕分享）的画面一般适合全屏播放。

**参数：**

| 参数名     | 类型   | 默认值 | 说明                                                              |
|:-----------|:-------|:-------|:----------------------------------------------------------------|
| userID     | String | -      | 必填参数，用户 ID。 |
| streamType | String | -     | 必填参数，流类型，可选值：<li>main：主流。</li> <li>aux：辅流（屏幕分享）。</li>|

**返回值：**

Promise

**示例代码：**

```javascript
trtcRoomContext.enterFullscreen({
  userID: 'xxx',
  streamType: 'main'
}).then((event)=>{
  // 全屏成功
}).catch((event)=>{
  // 全屏失败
})
```

### exitFullscreen(params)

**说明：**

取消远端视频的全屏模式。

**参数：**

| 参数名     | 类型   | 默认值 | 说明                                                              |
|:-----------|:-------|:-------|:----------------------------------------------------------------|
| userID     | String | -      | 必填参数，用户 ID。 |
| streamType | String | -      | 必填参数，流类型，可选值：<li>main：主流。</li><li>aux：辅流（屏幕分享）。</li>|

**返回值：**

Promise

**示例代码：**
```
trtcRoomContext.exitFullscreen({
  userID: 'xxx',
  streamType: 'main'
}).then((event)=>{
  // 退出全屏成功
}).catch((event)=>{
  // 退出全屏失败
})
```

### setViewOrientation(params)
**说明：**

设置指定远端画面的显示方向。

**参数：**

| 参数名      | 类型   | 默认值 | 说明                                                                |
|:------------|:-------|:-------|:------------------------------------------------------------------|
| userID      | String | -      | 必填参数，远端用户 ID。 |
| streamType  | String | -      | 必填参数，远端用户的流类型，可选值：<li>main：主流。</li><li>aux：辅流（屏幕分享）。</li> |
| orientation | String | -      | 必填参数，竖向：vertical，横向：horizontal。                    |

**返回值：**

Promise

**示例代码：**
```
trtcRoomContext.setViewOrientation({
  userID: 'xxx',
  streamType: 'main',
  orientation: 'vertical'
}).then((event)=>{
  // 设置成功
})
```

### setViewFillMode(params)
**说明：**

设置指定远端画面的填充模式。

**参数：**

| 参数名     | 类型   | 默认值 | 说明                                                                                                           |
|:-----------|:-------|:-------|:-----------------------------------------------------|
| userID     | String | -      | 必填参数，远端用户 ID。                                                                   |
| streamType | String | -      | 必填参数，远端用户的流类型，可选值：<li>main：主流。</li><li>aux：辅流（屏幕分享）。</li>     |
| fillMode   | String | -      | 必填参数，可选值：<li>适应：contain（完整显示画面，可能会有黑边）。</li><li>填充：fillCrop（铺满视图，可能会裁切部分画面）。</li> |

**返回值：**

Promise

**示例代码：**
```
trtcRoomContext.setViewFillMode({
  userID: 'xxx',
  streamType: 'main',
  fillMode: 'contain'
}).then((event)=>{
  // 设置成功
})
```

### setViewVisible(params)
**说明：**
显示或者隐藏某一路视频画面。
>!该方法仅在 template:"custom" 时才有效。

**参数：**

| 参数名     | 类型    | 默认值 | 说明                                                                |
|:-----------|:--------|:-------|:------------------------------------------------------------------|
| userID     | String  | -      | 必填参数，用户 ID。                                                        |
| streamType | String  | -      | 设置远端用户时必填，远端用户的流类型，可选值：<li>main：主流。</li><li>aux：辅流（屏幕分享）。</li>  |
| isVisible  | Boolean | -      | 必填参数，是否显示改视图。                                                |

**返回值：**

Promise

**示例代码：**
```
trtcRoomContext.setViewVisible({
  userID: 'xxx',
  streamType: 'main',
  isVisible: true
}).then((event)=>{
  // 设置成功
})
```

### setViewRect(params)
**说明：**

设置指定视频画面的坐标和尺寸。
>!该方法仅在 template:"custom" 时才有效。

**参数：**

| 参数名     | 类型   | 默认值 | 说明                                                                |
|:-----------|:-------|:-------|:------------------------------------------------------------------|
| userID     | String | -      | 必填，用户 ID。                                                        |
| streamType | String | -      | 设置远端用户时必填，远端用户的流类型，可选值：<li>main：主流。</li><li>aux：辅流（屏幕分享）。</li>   |
| xAxis      | String | -      | 可选，视图的横坐标。                                                   |
| yAxis      | String | -      | 可选，视图的纵坐标。                                                   |
| width      | String | -      | 可选，设置视图的宽度。                                                 |
| height     | String | -      | 可选，设置视图的高度。                                                 |

**返回值：**

Promise

**示例代码：**
```
trtcRoomContext.setViewRect({
  userID: 'xxx',
  streamType: 'main',
  xAxis: '480rpx', 
  yAxis: '160rpx', 
  width: '240rpx', 
  height: '320rpx',
}).then((event)=>{
  // 设置成功
})
```

### setViewZIndex(params)
**说明：**

设置指定视频画面的层级。
>!
>- 该方法仅在 template:"custom" 时才有效。
>- 该方法仅在小程序同层模式下有效，微信7.0.8以上的版本支持同层模式。

**参数：**

| 参数名     | 类型   | 默认值 | 说明                                                                |
|:-----------|:-------|:-------|:------------------------------------------------------------------|
| userID     | String | -      | 必填参数，用户 ID。                                                        |
| streamType | String | -      | 设置远端用户时必填，远端用户的流类型，可选值：<li>main：主流。</li><li>aux：辅流（屏幕分享）。</li>   |
| zIndex     | Number | -      | 必填参数，视图的层级，必须为整数。                                          |

**返回值：**

Promise

**示例代码：**
```
trtcRoomContext.setViewZIndex({
  userID: 'xxx',
  streamType: 'main',
  zIndex: 10
}).then((event)=>{
  // 设置成功
})
```

### playBGM(params)
**说明：**

播放背景音乐。背景音乐会同麦克风采集的人声混合在一起发布到云端，即“背景混音”。

**参数：**

| 参数名 | 类型   | 默认值 | 说明                                              |
|:-------|:-------|:-------|:------------------------------------------------|
| url    | String | -      | 背景音播放地址，仅支持 HTTPS 协议的在线音乐，音乐文件仅支持 mp3 以及 aac 格式。 |

**返回值：**

Promise

**示例代码：**
```
trtcRoomContext.playBGM({
  url: 'https://a.xxx.com/bgm.mp3' 
}).then(()=>{
    // 播放成功
}).catch(()=>{
    // 播放失败
})
```

### stopBGM()
**说明：**

停止播放背景音乐。

**参数：**

无

**返回值：**

无

**示例代码：**
```
trtcRoomContext.stopBGM()
```

### pauseBGM()
**说明：**

暂停播放背景音乐。

**参数：**

无

**返回值：**

无

**示例代码：**
```
trtcRoomContext.pauseBGM()
```

### resumeBGM()
**说明：**

恢复播放背景音乐。

**参数：**

无

**返回值：**

无

**示例代码：**
```
trtcRoomContext.resumeBGM()
```

### setBGMVolume(params)
**说明：**

设置混音中背景音乐的音量。

**参数：**

| 参数名 | 类型   | 默认值 | 说明                  |
|:-------|:-------|:-------|:--------------------|
| volume | number | -      | 音量大小，取值范围0 - 1。 |

**返回值：**

无

**示例代码：**
```
trtcRoomContext.setBGMVolume({
  volume: 0.5
})
```

### setMICVolume(params)
**说明：**

设置混音中麦克风采集的音量。

**参数：**

| 参数名 | 类型   | 默认值 | 说明                  |
|:-------|:-------|:-------|:--------------------|
| volume | number | -      | 音量大小，取值范围0 - 1。 |

**返回值：**

无

**示例代码：**
```
trtcRoomContext.setMICVolume({
  volume: 0.5
})
```

### snapshot(params)
**说明：**

截取指定远端视频或本地视频的图像，并保存到系统相册中。

**参数：**

| 参数名     | 类型   | 默认值 | 说明                                                              |
|:-----------|:-------|:-------|:----------------------------------------------------------------|
| userID     | String | -      | 必填参数，用户 ID。 |
| streamType | String | -      | 必填参数，流类型，可选值：<li>main：主流。</li><li>aux：辅流（屏幕分享）。</li> 本地视频流类型仅支持 main。|

**返回值：**

无

**示例代码：**
```
// 截取远端用户视频图像
trtcRoomContext.snapshot({
  userID: 'xxx',            // 远端用户 ID
  streamType: 'main'        // 远端用户流类型
}).then((event)=>{
  // 截图成功
})

// 截取本地用户视频图像
trtcRoomContext.snapshot({
  userID: 'xxx',            // 本地用户 ID
  streamType: 'main'        // 本地用户流类型仅支持 'main'：主流 
}).then((event)=>{
  // 截图成功
})
```

### sendC2CTextMessage(params)
**说明：**

发送 C2C（即定向发给某个人）文本消息，需开通 [即时通信 IM](https://cloud.tencent.com/product/im) 服务并将 [属性表](#Config) 中的 enableIM 选项设置为 true 才有效。

**参数：**

| 参数名  | 类型   | 默认值 | 说明                     |
|:--------|:-------|:-------|:-----------------------|
| userID  | String | -      | 必填参数，消息接收方的 ID。 |
| message | String | -      | 必填参数，需要发送的文本消息。  |

**返回值：**

Promise

**示例代码：**
```
trtcRoomContext.sendC2CTextMessage({
  userID: 'xxx',
  message: 'Hello!'
})
```


### sendC2CCustomMessage(params)
**说明：**

发送 C2C 自定义消息，自定义消息可以用来发送控制信令（例如邀请发言、申请上麦等）。
需开通 [即时通信 IM](https://cloud.tencent.com/product/im) 服务并将 [属性表](#Config) 中的 enableIM 选项设置为 true 才有效。

**参数：**

| 参数名  | 类型   | 默认值 | 说明                  |
|:--------|:-------|:-------|:--------------------|
| userID  | String | -      | 必填参数，消息接收方的 ID。  |
| payload | Object | -      | 必填参数，自定义消息的载体。 |

payload 支持三个参数：

| 参数名      | 类型   | 默认值 | 说明                 |
|:------------|:-------|:-------|:-------------------|
| data        | String | -      | 自定义消息的数据字段。 |
| description | String | -      | 自定义消息的说明字段。 |
| extension   | String | -      | 自定义消息的扩展字段。 |

**返回值：**

Promise

**示例代码：**
```
trtcRoomContext.sendC2CCustomMessage({
  userID: 'xxx',
  payload: {
    data: '自定义消息的数据字段',
    description: '自定义消息的说明字段',
    extension: '自定义消息的扩展字段'
  } 
})
```

### sendGroupTextMessage(params)
**说明：**

发送群组文本消息，需开通 [即时通信 IM](https://cloud.tencent.com/product/im) 服务并将 [属性表](#Config) 中的 enableIM 选项设置为 true 才有效。

**参数：**

| 参数名  | 类型   | 默认值 | 说明                     |
|:--------|:-------|:-------|:-----------------------|
| roomID  | Number | -      | 必填参数，房间 ID。    |
| message | String | -      | 必填参数，需要发送的文本消息。  |

**返回值：**

Promise

**示例代码：**
```
trtcRoomContext.sendGroupTextMessage({
  roomID: 'xxx', // 房间 ID
  message: 'Hello!'
})
```


### sendGroupCustomMessage(params)
**说明：**

发送群组自定义消息，需开通 [即时通信 IM](https://cloud.tencent.com/product/im) 服务并将 [属性表](#Config) 中的 enableIM 选项设置为 true 才有效。

**参数：**

| 参数名  | 类型   | 默认值 | 说明                  |
|:--------|:-------|:-------|:--------------------|
| roomID  | Number | -      | 必填参数，房间 ID。  |
| payload | Object | -      | 必填参数，自定义消息的载体。 |

payload 支持三个参数：

| 参数名      | 类型   | 默认值 | 说明                 |
|:------------|:-------|:-------|:-------------------|
| data        | String | -      | 自定义消息的数据字段。 |
| description | String | -      | 自定义消息的说明字段。 |
| extension   | String | -      | 自定义消息的扩展字段。 |

**返回值：**

Promise

**示例代码：**
```
trtcRoomContext.sendGroupCustomMessage({
  roomID: 'xxx', // 房间 ID
  payload: {
    data: '自定义消息的数据字段'，
    description: '自定义消息的说明字段'，
    extension: '自定义消息的扩展字段'
  }
})
```

<h2 id="Event">事件表</h2>

通过组件实例的 EVENT 属性可以获取到事件常量字段，示例：

```
let EVENT = trtcRoomContext.EVENT
trtcRoomContext.on(EVENT.REMOTE_VIDEO_ADD,(event)=>{
    // 远端视频流添加事件，当远端用户发布视频流后会收到该通知
})

// 接收 IM 消息
trtcRoomContext.on(EVENT.IM_MESSAGE_RECEIVED,(event)=>{
  let messageEvent = event.data
  // 收到推送的单聊、群聊、群提示、群系统通知的新消息，可通过遍历 messageEvent.data 获取消息列表数据并渲染到页面
  // messageEvent.data - 存储 Message 对象的数组
})
```
| CODE                       | 说明                                                     |
|----------------------------|----------------------------------------------------------|
| LOCAL_JOIN                 | 成功进入房间。                                               |
| LOCAL_LEAVE                | 成功离开房间。                                               |
| REMOTE_USER_JOIN           | 远端用户进入房间时触发。                                     |
| REMOTE_USER_LEAVE          | 远端用户退出房间时触发。                                     |
| REMOTE_VIDEO_ADD           | 远端视频流添加事件，当远端用户发布视频流后会收到该通知。 |
| REMOTE_VIDEO_REMOVE        | 远端视频流移出事件，当远端用户取消发布视频流后会收到该通知。 |
| REMOTE_AUDIO_ADD           | 远端音频流添加事件，当远端用户发布音频流后会收到该通知。 |
| REMOTE_AUDIO_REMOVE        | 远端音频流移除事件，当远端用户取消发布音频流后会收到该通知。 |
| REMOTE_STATE_UPDATE        | 远端用户播放状态变更通知。                                   |
| LOCAL_NET_STATE_UPDATE     | 本地推流的网络状态变更通知。                                   |
| REMOTE_NET_STATE_UPDATE    | 远端用户网络状态变更通知。                                   |
| REMOTE_AUDIO_VOLUME_UPDATE | 远端用户音量变更通知。                                       |
| VIDEO_FULLSCREEN_UPDATE    | 远端视图全屏状态变更通知。                                   |
| BGM_PLAY_PROGRESS          | BGM 播放时间戳变更通知。                                     |
| BGM_PLAY_COMPLETE          | BGM 播放结束通知。                                           |
| ERROR                      | 本地推流出现错误、渲染错误事件等。                           |
| IM_READY                   | IM 就绪的通知，收到该通知后可以进行收发消息操作。            |
| IM_MESSAGE_RECEIVED        | 收到 IM 消息的通知，详情请参见 [Message 对象文档](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html)。|
| IM_NOT_READY               | IM 未就绪的通知，收到该通知后不可以进行收发消息操作。            |
| IM_ERROR                   | IM 错误事件，详情请参见 [即时通信 IM 错误码](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#%E9%94%99%E8%AF%AF%E7%A0%81%E5%AF%B9%E7%85%A7%E8%A1%A8) 。|                                            |

## 错误码
ERROR 事件触发时会返回响应的错误码，错误码含义如下
```
let EVENT = trtcRoomContext.EVENT
trtcRoomContext.on(EVENT.ERROR,(event)=>{
  console.log(event.data.code)
})
```
错误码详细信息请参见 [错误码](https://cloud.tencent.com/document/product/647/38313)。
