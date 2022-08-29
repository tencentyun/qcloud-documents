本文档主要介绍如何进入 TRTC 房间中，只有在进入音视频房间后，用户才能订阅房间中其他用户的音视频流，或者向房间中的其他用户发布自己的音视频流。
![](https://qcloudimg.tencent-cloud.cn/raw/861153473c6e4679affdb2d24a71f775.png)

[](id:step1)
## 步骤1：初始化 TRTC 实例
参见 [初始化 TRTC 实例](https://cloud.tencent.com/document/product/647/17018#.E5.88.9D.E5.A7.8B.E5.8C.96-trtc-.E5.AE.9E.E4.BE.8B)。

```javascript
// 生命周期函数--监听页面加载
onLoad(options) {
    this.TRTC = new TRTC(this)
},
```

[](id:step2)
## 步骤2：绑定事件回调
参见 [事件表](https://cloud.tencent.com/document/product/647/17018#Event)。
```html
<live-pusher
        bindstatechange="_pusherStateChangeHandler"
        bindnetstatus="_pusherNetStatusHandler"
        binderror="_pusherErrorHandler"
        bindbgmstart="_pusherBGMStartHandler"
        bindbgmprogress="_pusherBGMProgressHandler"
        bindbgmcomplete="_pusherBGMCompleteHandler"
        bindaudiovolumenotify="_pusherAudioVolumeNotify"
/>
```

```javascript
// 生命周期函数--监听页面加载
onLoad(options) {
    this.TRTC = new TRTC(this)
    this.bindTRTCRoomEvent()
},
// 事件监听
bindTRTCRoomEvent() {
    const TRTC_EVENT = this.TRTC.EVENT
    // 初始化事件订阅
    this.TRTC.on(TRTC_EVENT.LOCAL_JOIN, (event) => {
        console.log('* room LOCAL_JOIN', event)
    })
    this.TRTC.on(TRTC_EVENT.LOCAL_LEAVE, (event) => {
        console.log('* room LOCAL_LEAVE', event)
    })
    this.TRTC.on(TRTC_EVENT.ERROR, (event) => {
        console.log('* room ERROR', event)
    })
    // 远端用户加入
    this.TRTC.on(TRTC_EVENT.REMOTE_USER_JOIN, (event) => {
        console.error('* room REMOTE_USER_JOIN', event)
    })
    // 远端用户退出
    this.TRTC.on(TRTC_EVENT.REMOTE_USER_LEAVE, (event) => {
        console.error('* room REMOTE_USER_LEAVE', event)
    })
    // 远端用户推送视频
    this.TRTC.on(TRTC_EVENT.REMOTE_VIDEO_ADD, (event) => {
        console.log('* room REMOTE_VIDEO_ADD',  event)
    })
    // 远端用户取消推送视频
    this.TRTC.on(TRTC_EVENT.REMOTE_VIDEO_REMOVE, (event) => {
        console.log('* room REMOTE_VIDEO_REMOVE', event)
    })
    // 远端用户推送音频
    this.TRTC.on(TRTC_EVENT.REMOTE_AUDIO_ADD, (event) => {
        console.log('* room REMOTE_AUDIO_ADD', event)
    })
    // 远端用户取消推送音频
    this.TRTC.on(TRTC_EVENT.REMOTE_AUDIO_REMOVE, (event) => {
        console.log('* room REMOTE_AUDIO_REMOVE', event)
    })
    // 远端用户音量更新
    this.TRTC.on(TRTC_EVENT.REMOTE_AUDIO_VOLUME_UPDATE, (event) => {
        console.log('* room REMOTE_AUDIO_VOLUME_UPDATE', event)
    })
    // 本地用户音量更新
    this.TRTC.on(TRTC_EVENT.LOCAL_AUDIO_VOLUME_UPDATE, (event) => {
        console.log('* room LOCAL_AUDIO_VOLUME_UPDATE', event)
    })
},
// 请保持跟 wxml 中绑定的事件名称一致
_pusherStateChangeHandler(event) {
    this.TRTC.pusherEventHandler(event)
},
_pusherNetStatusHandler(event) {
    this.TRTC.pusherNetStatusHandler(event)
},
_pusherErrorHandler(event) {
    this.TRTC.pusherErrorHandler(event)
},
_pusherBGMStartHandler(event) {
    this.TRTC.pusherBGMStartHandler(event)
},
_pusherBGMProgressHandler(event) {
    this.TRTC.pusherBGMProgressHandler(event)
},
_pusherBGMCompleteHandler(event) {
    this.TRTC.pusherBGMCompleteHandler(event)
},
_pusherAudioVolumeNotify(event) {
    this.TRTC.pusherAudioVolumeNotify(event)
},
_playerStateChange(event) {
    this.TRTC.playerEventHandler(event)
},
_playerFullscreenChange(event) {
    this.TRTC.playerFullscreenChange(event)
},
_playerNetStatus(event) {
    this.TRTC.playerNetStatus(event)
},
_playerAudioVolumeNotify(event) {
    this.TRTC.playerAudioVolumeNotify(event)
}
```

[](id:step3)
## 步骤3：进入音视频通话房间
需要先调用 [createpusher](https://cloud.tencent.com/document/product/647/17018#createpusher(pusherattributes)) 初始化 pusher 实例并配置初始参数，再调用 [enterroom](https://cloud.tencent.com/document/product/647/17018#enterroom(params)) 获取新的 pusher 实例，通过 setData 赋值给 [live-pusher](https://developers.weixin.qq.com/miniprogram/dev/component/live-pusher.html) 标签。
```javascript
// 生命周期函数--监听页面加载
onLoad(options) {
	this.TRTC = new TRTC(this)
	this.bindTRTCRoomEvent()
	this.init()
	this.enterRoom(options)
},
init() {
  const pusherConfig = {
    beautyLevel: 9,
  }
  this.setData({
    pusher: this.TRTC.createPusher(pusherConfig)
  })
},
enterRoom(options) {
  const { roomID, sdkAppID, userID, userSig } = options
  this.setData({
    pusher: this.TRTC.enterRoom({
      roomID,
      sdkAppID,
      userID,
      userSig,
    }),
  })
},
```
```xml
 <live-pusher
        url="{{pusher.url}}"
        mode="{{pusher.mode}}"
        enable-camera="{{pusher.enableCamera}}"
        enable-mic="{{pusher.enableMic}}"
/>
```

