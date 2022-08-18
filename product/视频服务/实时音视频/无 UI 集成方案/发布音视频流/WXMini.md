本文档主要介绍主播如何发布自己的音视频流，所谓“发布”，也就是打开麦克风和摄像头，让自己的声音和视频能够被房间中其他用户听到和看到的意思。

![](https://qcloudimg.tencent-cloud.cn/raw/b887b390411aef1396bd593ccdd9eb0e.png)


[](id:step1)
## 步骤1：完成前序步骤
先参考文档 [导入 SDK 到项目中](https://cloud.tencent.com/document/product/647/32183)，再 [进入房间](https://cloud.tencent.com/document/product/647/74637)。


[](id:step2)
## 步骤2：本地推流
在进入房间后，调用 [getPusherInstance().start()](https://cloud.tencent.com/document/product/647/17018#enterroom(params)) 或者开启自动推流模式即可开始推流。
```javascript
 enterRoom(options) {
    this.setData({
      pusher: this.TRTC.enterRoom(options),
    }, () => {
      this.TRTC.getPusherInstance().start() // 开始推流
    })
  },
```
```xml
 <live-pusher
    url="{{pusher.url}}"
    autopush="{{true}}"
/>
```
