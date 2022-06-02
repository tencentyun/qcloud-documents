本文档主要介绍如何主动退出当前 TRTC 房间，同时还会介绍在什么情况下会被迫退出房间：
![](https://qcloudimg.tencent-cloud.cn/raw/b155aaff08a5baaaecaaa14a4f2229cc.png)

在使用 TRTC Web SDK 中，经常会接触到以下对象：
- Client 对象，代表一个本地客户端。[Client](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/Client.html) 类的方法提供了加入通话房间、发布本地流、订阅远端流等功能。
- Stream 对象，代表一个音视频流对象，包括本地音视频流对象 [LocalStream](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/LocalStream.html) 和远端音视频流对象 [RemoteStream](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/RemoteStream.html)。Stream 类的方法主要提供音视频流对象的行为，包括音频和视频的播放控制。

[](id:step1)
## 步骤1：完成前序步骤
可以参考文档 [进入房间](https://cloud.tencent.com/document/product/647/74636)，创建 Client 并进入房间。

[](id:step2)
## 步骤2：主动退出当前房间

通话结束时调用 [Client.leave()](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/Client.html#leave) 方法退出音视频通话房间，整个音视频通话会话结束。

```javascript
await client.leave(); 
```

[](id:step3)
## 步骤3：被动退出当前房间
除了用户主动退出房间，在以下情况下，用户会收到 [`CLIENT_BANNED`](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/module-ClientEvent.html#.CLIENT_BANNED) 事件，表示当前用户被动退出房间：

```javascript
client.on('client-banned', error => {
  console.error('client-banned observed: ' + error.message);
  // client-banned observed: client was banned because of duplicated userId joining the room.
  // client-banned observed: client was banned because of you got banned by account admin
});
```

- **情况一：被同名用户踢出当前房间**
在一个房间内，如果同时出现两个 userId 一样且角色都为主播的用户，那么先进入房间的用户会被踢出房间。
例如：A、B 两个用户，先后以相同的 `userId` 进入房间， A 会被 B 挤出房间。
同名用户同时进入同一房间是不允许的行为，可能会导致双方音视频通话异常，应避免出现这种情况。

- **情况二：通过服务端 API 踢出当前房间或者解散当前房间**
您可以通过服务端的 [RemoveUser](https://cloud.tencent.com/document/api/647/40496) | [RemoveUserByStrRoomId](https://cloud.tencent.com/document/api/647/50426) 接口将某个用户踢出某个 TRTC 房间，将该用户踢出后，该用户会收到 [`CLIENT_BANNED`](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/module-ClientEvent.html#.CLIENT_BANNED) 事件。也可以通过服务端的 [DismissRoom](https://cloud.tencent.com/document/api/647/50089) | [DismissRoomByStrRoomId](https://cloud.tencent.com/document/api/647/37088)接口将某个 TRTC 房间解散，解散房间之后，该房间的所有用户都会 [`CLIENT_BANNED`](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/module-ClientEvent.html#.CLIENT_BANNED) 事件。
