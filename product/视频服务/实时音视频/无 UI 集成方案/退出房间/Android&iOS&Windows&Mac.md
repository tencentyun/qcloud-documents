本文档主要介绍如何主动退出当前 TRTC 房间，同时还会介绍在什么情况下会被迫退出房间：
![](https://qcloudimg.tencent-cloud.cn/raw/b155aaff08a5baaaecaaa14a4f2229cc.png)

## 调用指引


[](id:step1)
### 步骤1：完成前序步骤
请参考文档 [导入 SDK 到项目中](https://cloud.tencent.com/document/product/647/32173) 完成 SDK 的导入和 App 权限的配置。
请参考文档 [进入房间](https://cloud.tencent.com/document/product/647/74634) 完成进房流程。

[](id:step2)
### 步骤2：主动退出当前房间
调用 exitRoom 接口即可退出当前的房间，SDK 会在退房结束后通过 onExitRoom(int reason) 回调事件通知您。
<dx-codeblock>
::: Android  java
// 退出当前房间
mCloud.exitRoom();
:::
::: iOS&Mac  swift
self.trtcCloud = [TRTCCloud sharedInstance];
// 退出当前房间
[self.trtcCloud exitRoom];
:::
::: Windows  C++
trtc_cloud_ = getTRTCShareInstance();
// 退出当前房间
trtc_cloud_->exitRoom();
:::
</dx-codeblock>

当您调用了 exitRoom 接口之后，SDK 会进入退房流程，其中有两项非常重要的任务：
- **关键任务一：通告自己的离开**
通知房间中的其他用户自己将要退出当前的这个房间，房间中的其他用户会收到来自该用户的 **onRemoteUserLeaveRoom** 回调，否则其他用户可能误以为该用户已经“卡死了”。
- **关键任务二：释放设备权限**
如果用户在退房之前正在发布音视频流，则退房流程中还需要关闭摄像头和麦克风并释放设备的使用权限。

因此，如果您希望释放 TRTCCloud 实例，建议等收到 onExitRoom 回调之后再释放。


[](id:step3)
### 步骤3：被迫退出当前房间
除了用户主动退出房间，还有两种情况下您也会收到 onExitRoom(int reason) 回调：
- **情况一：被踢出当前房间**
您可以通过服务端的 [RemoveUser](https://cloud.tencent.com/document/api/647/40496) | [RemoveUserByStrRoomId](https://cloud.tencent.com/document/api/647/50426) 接口将某个用户踢出某个 TRTC 房间，将该用户踢出后，该用户会收到 onExitRoom(1) 的回调。

- **情况二：当前房间被解散**
您可以通过服务端的 [DismissRoom](https://cloud.tencent.com/document/api/647/50089) | [DismissRoomByStrRoomId](https://cloud.tencent.com/document/api/647/37088)接口将某个 TRTC 房间解散，解散房间之后，该房间的所有用户都会收到 onExitRoom(2) 的回调。


<dx-codeblock>
::: Android  java
// 监听 onExitRoom 回调即可获知自己的退房原因
@Override
public void onExitRoom(int reason) {
    if (reason == 0) {
        Log.d(TAG, "Exit current room by calling the 'exitRoom' api of sdk ...");
    } else if (reason == 1) {
        Log.d(TAG, "Kicked out of the current room by server through the restful api...");
    } else if (reason == 2) {
        Log.d(TAG, "Current room is dissolved by server through the restful api...");
    }
}
:::
::: iOS&Mac  ObjC
// 监听 onExitRoom 回调即可获知自己的退房原因
- (void)onExitRoom:(NSInteger)reason {
    if (reason == 0) {
        NSLog(@"Exit current room by calling the 'exitRoom' api of sdk ...");
    } else if (reason == 1) {
        NSLog(@"Kicked out of the current room by server through the restful api...");
    } else if (reason == 2) {
        NSLog(@"Current room is dissolved by server through the restful api...");
    }
}
:::
::: Windows  C++
// 监听 onExitRoom 回调即可获知自己的退房原因
void onExitRoom(int reason) {
    if (reason == 0) {
        printf("Exit current room by calling the 'exitRoom' api of sdk ...");
    } else if (reason == 1) {
        printf("Kicked out of the current room by server through the restful api...");
    } else if (reason == 2) {
        printf("Current room is dissolved by server through the restful api...");
    }
}
:::
</dx-codeblock>
