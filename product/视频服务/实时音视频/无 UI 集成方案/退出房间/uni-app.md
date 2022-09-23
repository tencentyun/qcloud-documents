本文档主要介绍如何主动退出当前 TRTC 房间，同时还会介绍在什么情况下会被迫退出房间

## 调用指引

[](id:step1)
### 步骤1：完成前序步骤
- 参考文档 [导入 SDK 到项目中](https://cloud.tencent.com/document/product/647/73371) 完成 SDK 的导入和 App 权限的配置。
- 参考文档 [进入房间](https://cloud.tencent.com/document/product/647/74638) 完成进房流程。

[](id:step2)
### 步骤2：主动退出当前房间
调用 [exitRoom](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#exitRoom) 接口即可退出当前的房间，SDK 会在退房结束后通过 [onExitRoom](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#exitRoom) 回调事件通知您。
```javascript
import TrtcCloud from "@/TrtcCloud/lib/index";
this.trtcCloud = TrtcCloud.createInstance();

// 退出当前房间
this.trtcCloud.exitRoom();
```

当您调用了 [exitRoom](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#exitRoom) 接口之后，SDK 会进入退房流程，其中有两项非常重要的任务：
- **关键任务一：通告自己的离开**
通知房间中的其他用户自己将要退出当前的这个房间，房间中的其他用户会收到来自该用户的 [**onRemoteUserLeaveRoom**](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TRTCCallback.html#event:onRemoteUserLeaveRoom) 回调，否则其他用户可能误以为该用户已经“卡死了”。
- **关键任务二：释放设备权限**
如果用户在退房之前正在发布音视频流，则退房流程中还需要关闭摄像头和麦克风并释放设备的使用权限。

因此，如果您希望释放 `TRTCCloud` 实例，建议等收到 [onExitRoom](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TRTCCallback.html#event:onExitRoom) 回调之后再释放。

[](id:step3)
### 步骤3：被迫退出当前房间
除了用户主动退出房间，还有两种情况下您也会收到 [onExitRoom](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TRTCCallback.html#event:onExitRoom) 回调：
- **情况一：被踢出当前房间**
用户被踢出后，该用户会收到 [onExitRoom(1)](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TRTCCallback.html#event:onExitRoom) 的回调。
- **情况二：当前房间被解散**
解散房间后，该房间的所有用户都会收到 [onExitRoom(2)](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TRTCCallback.html#event:onExitRoom) 的回调。

```javascript
import TrtcCloud from "@/TrtcCloud/lib/index";
this.trtcCloud = TrtcCloud.createInstance();

// 监听 onExitRoom 回调即可获知自己的退房原因
this.trtcCloud.on('onExitRoom', (reason) => {
	console.log(`onExitRoom reason = ${reason}`);
});
```
