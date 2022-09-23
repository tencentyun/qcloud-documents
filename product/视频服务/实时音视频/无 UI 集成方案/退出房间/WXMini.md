本文档主要介绍如何主动退出当前 TRTC 房间，同时还会介绍在什么情况下会被迫退出房间：
![](https://qcloudimg.tencent-cloud.cn/raw/b155aaff08a5baaaecaaa14a4f2229cc.png)

[](id:step1)
## 步骤1：完成前序步骤
先参考文档 [导入 SDK 到项目中](https://cloud.tencent.com/document/product/647/32183) 并 [进入房间](https://cloud.tencent.com/document/product/647/74637)。


[](id:step2)
## 步骤2：主动退出当前房间
通话结束时调用 [exitRoom](https://cloud.tencent.com/document/product/647/17018#exitroom()) 方法退出音视频通话房间，整个音视频通话会话结束。

```javascript
exitRoom() {
    const result = this.TRTC.exitRoom()
    // 状态机重置，会返回更新后的pusher和playerList
    this.setData({
        pusher: result.pusher,
        playerList: result.playerList,
    })
},
```

[](id:step3)
## 步骤3：被动退出当前房间
除了用户主动退出房间，在以下情况下，用户会收到 [`KICKED_OUT`](https://cloud.tencent.com/document/product/647/17018#kicked_out) 事件，表示当前用户被动退出房间：

```javascript
let onKickedout = function(event){
  console.log('被服务端踢出或房间被解散')
}
this.TRTC.on(EVENT.KICKED_OUT, onKickedout)
```
