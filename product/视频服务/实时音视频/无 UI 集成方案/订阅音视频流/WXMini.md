本文档主要介绍如何订阅房间中其他用户的音视频流，也就是如何播放其他用户的音频和视频。为了方便起见，我们在接下来的文档中，会将“房间中的其他用户”统称为“远端用户”。
![](https://qcloudimg.tencent-cloud.cn/raw/692f3cddee1dc9e9dfadde81448643ad.png)


## 步骤1：完成前序步骤
先参考文档 [导入 SDK 到项目中](https://cloud.tencent.com/document/product/647/32183) 并 [进入房间](https://cloud.tencent.com/document/product/647/74637)。

## 步骤2：订阅远端流
在远端用户进入的回调中，更新 playerList，通过循环遍历。
```javascript
    // 远端用户推送视频
    this.TRTC.on(TRTC_EVENT.REMOTE_VIDEO_ADD, (event) => {
      console.log('* room REMOTE_VIDEO_ADD',  event)
      const { player } = event.data
      // 开始播放远端的视频流，默认是不播放的
      this.setPlayerAttributesHandler(player, { muteVideo: false })
    })
    // 远端用户推送音频
    this.TRTC.on(TRTC_EVENT.REMOTE_AUDIO_ADD, (event) => {
      console.log('* room REMOTE_AUDIO_ADD', event)
      const { player } = event.data
      this.setPlayerAttributesHandler(player, { muteAudio: false })
    })
```
```javascript
 // 设置某个 player 属性
  setPlayerAttributesHandler(player, options) {
    this.setData({
      playerList: this.TRTC.setPlayerAttributes(player.streamID, options),
    })
  },
```
```xml
   <view wx:for="{{playerList}}" wx:key="id">
     <live-player
       id="{{item.id}}"
       src= "{{item.src}}"
     />
  </view>
```