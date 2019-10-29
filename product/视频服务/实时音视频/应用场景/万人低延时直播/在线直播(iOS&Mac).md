
## 文档导读
本文主要介绍如何基于 TRTC SDK 实现一个既支持视频连麦，又支持上万人高并发观看的在线直播功能：

- 本文仅提及了最基本的几个功能，如果您希望了解更多高级功能，请参见 [高级功能](https://cloud.tencent.com/document/product/647/32227)。
- 本文仅罗列了最常用的几个接口，如果您希望了解更多的接口函数，请参见 [API 文档](https://cloud.tencent.com/document/product/647/32228)。

## 示例代码

| 所属平台 | 示例代码 | 
|---------|---------|
| iOS | [TRTCMainViewController.m](https://github.com/tencentyun/TRTCSDK/blob/master/iOS/TRTCDemo/TRTC/TRTCMainViewController.m) | 
| Mac OS | [TRTCMainWindowController.m](https://github.com/tencentyun/TRTCSDK/blob/master/Mac/TRTCDemo/TRTC/TRTCMainWindowController.m) | 
| Android | [TRTCMainActivity.java](https://github.com/tencentyun/TRTCSDK/blob/master/Android/TRTCDemo/app/src/main/java/com/tencent/liteav/demo/trtc/TRTCMainActivity.java) | 
| Windows（MFC） | [TRTCMainViewController.cpp](https://github.com/tencentyun/TRTCSDK/blob/master/Windows/MFCDemo/TRTCMainViewController.cpp) |
| Windows（Duilib） | [TRTCMainViewController.cpp](https://github.com/tencentyun/TRTCSDK/blob/master/Windows/DuilibDemo/TRTCMainViewController.cpp) |

![](https://main.qcloudimg.com/raw/881d7bf09c7e17a31091b1ce008fdb00.jpeg)

## 在线直播
### 1. 初始化 SDK

使用 TRTC SDK 的第一步，是先获取 `TRTCCloud` 的单例对象，并注册监听 SDK 事件的回调。

- 先继承 `TRTCCloudDelegate` 虚接口类并重写您需要监听的事件（例如：用户加入房间、用户退出房间、警告信息和错误信息等）。
- 获取 `TRTCCloud` 单例对象，调用 setDelegate 方法设置 `TRTCCloudDelegate` 回调。

```Objective-C
#import "TRTCCloud.h"
#import "TRTCCloudDelegate.h"

// 继承 TRTCCloudDelegate 回调 
@interface TRTCViewController() <TRTCCloudDelegate> {
	TRTCCloud       *trtcCloud;
	//...
}
@end

// 获取 trtcCloud 实例
- (void)viewDidLoad {
	[super viewDidLoad];
	//...
	trtcCloud = [TRTCCloud sharedInstance];
	[trtcCloud setDelegate:self];
}

// 销毁 trtcCloud 实例，在不再使用 SDK 能力时，销毁单例，节省开销
- (void)dealloc {
    if (trtcCloud != nil) {
        [trtcCloud exitRoom];
    }
    [TRTCCloud destroySharedIntance];
}

// 错误通知是要监听的，错误通知意味着 SDK 不能继续运行了
- (void)onError:(int)errCode errMsg:(NSString *)errMsg extInfo:(nullable NSDictionary *)extInfo {
	if (errCode == ERR_ROOM_ENTER_FAIL) {
		[self toastTip:[NSString stringWithFormat:@"进房失败[%@]", errMsg]];
		[self exitRoom];
		return;
	}
}
```

### 2. 组装 TRTCParams

TRTCParams 是 SDK 最关键的一个参数，它包含如下四个必填的字段：sdkAppId、userId、userSig 和 roomId。

- **sdkAppId**
进入腾讯云实时音视频 [控制台](https://console.cloud.tencent.com/rav)，如果您还没有应用，请创建一个，即可看到 sdkAppId。
![](https://main.qcloudimg.com/raw/e42c76fd9d4fd3e3e5d80e8fb2763134.png)

- **userId**
您可以随意指定，由于是字符串类型，可以直接跟您现有的账号体系保持一致，但请注意，**同一个音视频房间里不应该有两个同名的 userId**。

- **userSig**
基于 sdkAppId 和 userId 可以计算出 userSig，计算方法请参见 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。

- **roomId**
房间号是数字类型，您可以随意指定，但请注意，**同一个应用里的两个音视频房间不能分配同一个 roomId**。

### 3. 主播预览摄像头画面
TRTC SDK 并不会默认打开本地的摄像头采集，`startLocalPreview` 可以开启本地的摄像头并显示预览画面，`stopLocalPreview` 则会关闭。

启动本地预览前，可调用 `setLocalViewFillMode` 指定视频显示模式为 `Fill` 或 `Fit` 模式。两种模式下视频尺寸都是等比缩放，区别在于：`Fill` 模式优先保证视窗被填满。如果缩放后的视频尺寸与显示视窗尺寸不一致，多出的视频将被截掉； `Fit` 模式则优先保证视频内容全部显示。如果缩放后的视频尺寸与显示视窗尺寸不一致，未被填满的视窗区域将使用黑色填充。

另外，iOS 和 Mac 两个平台的 startLocalPreivew 函数会有一些差异：
-  （`iOS`）调用 `startLocalPreview`，参数：`frontCamera`（YES：前置摄像头；NO：后置摄像头）、`view`（UIView 控件）。
-  （`Mac`）调用 `startLocalPreview`，参数：`view`（NSView 控件）。

```Objective-C
/** 打开本地摄像头预览画面 */
//iOS调用示例
- (void)startLocalPreview:(BOOL)frontCamera localView:(UIView*)localView {
	[trtcCloud setLocalViewFillMode:TRTCVideoFillMode_Fit];
	[trtcCloud startLocalPreview:frontCamera view:localView];
}

//Mac调用示例
- (void)startLocalPreview:(NSView*)localView {
	[trtcCloud setLocalViewFillMode:TRTCVideoFillMode_Fit];
	[trtcCloud startLocalPreview:localView];
}
```

>? Mac 版的 SDK 默认会使用当前系统默认设备。如有多个摄像头可以通过调用 `setCurrentCameraDevice` 接口设置所要使用的摄像头，参数 `deviceId` 为摄像头设备 ID， 您可以通过 `getCameraDevicesList` 接口返回的摄像头设备列表中获得期望的 `deviceId` 。


### 4. 主播开启麦克风采集
TRTC SDK 并不会默认打开本地的麦克风采集，主播调用 `startLocalAudio` 可以开启本地的声音采集并将音视频数据广播出去，`stopLocalAudio` 则会关闭。您可以在 `startLocalPreview` 之后继续调用 `startLocalAudio`。

>`startLocalAudio` 会检查麦克风使用权限，如果没有麦克风权限，SDK 会向用户申请开启。

### 5. 主播创建新房间开播

主播可以使用 `enterRoom` 创建一个音视频房间，参数 `TRTCParams` 中的 `roomId` 用于指定房间号，同时，我们还需要将 `role` 字段指定为 `TRTCRoleAnchor`（主播）。

`appScene` 参数指定 SDK 的应用场景，本文档中我们使用 `TRTCAppSceneLIVE`（在线直播）。

- 如创建成功，SDK 会回调 `onEnterRoom` 接口，参数：`elapsed`代表进入耗时，单位：ms。
- 如创建失败，SDK 会回调 `onError` 接口，参数：`errCode`（错误码 `ERR_ROOM_ENTER_FAIL`，错误码可参考 `TXLiteAVCode.h`）、`errMsg`（错误原因）、`extraInfo`（保留参数）。

```Objective-C
- (void)startBroadCasting {
{
	//TRTCParams 定义参考头文件TRTCCloudDef.h
	TRTCParams *params = [[TRTCParams alloc] init];
	params.sdkAppId    = sdkappid;
	params.userId      = userid;
	params.userSig     = usersig;
	params.roomId      = 908; //输入您想进入的房间
	params.role        = TRTCRoleAnchor; //当前角色为主播
	[trtcCloud enterRoom:params appScene:TRTCAppSceneLIVE];
}

- (void)onError:(int)errCode errMsg:(NSString *)errMsg extInfo:(nullable NSDictionary *)extInfo {
	if (errCode == ERR_ROOM_ENTER_FAIL) {
		[self toastTip:[NSString stringWithFormat:@"进房失败[%@]", errMsg]];
		[self exitRoom];
		return;
	}
}

- (void)onEnterRoom:(NSInteger)elapsed {
	NSString *msg = [NSString stringWithFormat:@"[%@]进房成功[%u]: elapsed[%d]", _userID, _roomID, elapsed];
}
```

### 6. 主播开关隐私模式
直播过程中，主播可能出于隐私目的希望屏蔽本地的音视频数据，可以调用 `muteLocalVideo` 屏蔽本地的视频采集，调用 `muteLocalAudio` 屏蔽本地的音频采集。

### 7. 观众加入房间观看

观众调用 `enterRoom` 可以进入一个音视频房间，参数 TRTCParams 中的 `roomId` 用于指定房间号。
`appScene` 同样填写 `TRTCAppSceneLIVE`（在线直播），但 `role` 字段需要指定为 `TRTCRoleAudience`（观众）。

```Objective-C
- (void)startPlaying {
{
	//TRTCParams 定义参考头文件TRTCCloudDef.h
	TRTCParams *params = [[TRTCParams alloc] init];
	params.sdkAppId    = sdkappid;
	params.userId      = userid;
	params.userSig     = usersig;
	params.roomId      = 908; //输入您想进入的房间
	params.role        = TRTCRoleAudience; //当前角色为观众
	[trtcCloud enterRoom:params appScene:TRTCAppSceneLIVE];
}
```

如果主播在房间里，观众会通过 TRTCCloudDelegate 中的 `onUserVideoAvailable` 回调获知主播的 userid。之后，观众可以调用 `startRemoteView` 方法来显示主播的视频画面。

通过 `setRemoteViewFillMode` 可以指定视频显示模式为 `Fill` 或 `Fit` 模式。两种模式下视频尺寸都是等比缩放，区别在于：
- `Fill` 模式：优先保证视窗被填满。如果缩放后的视频尺寸与显示视窗尺寸不一致，多出的视频将被截掉。
- `Fit` 模式：优先保证视频内容全部显示。如果缩放后的视频尺寸与显示视窗尺寸不一致，未被填满的视窗区域将使用黑色填充。

```Objective-C
- (void)onUserVideoAvailable:(NSString *)userId available:(BOOL)available {
    if (userId != nil) {
        TRTCVideoView* remoteView = [_remoteViewDic objectForKey:userId];
        if (available) {
            // 启动远程画面的解码和显示逻辑，FillMode 可以设置是否显示黑边
            [_trtc startRemoteView:userId view:remoteView];
            [_trtc setRemoteViewFillMode:userId mode:TRTCVideoFillMode_Fit];
        }
        else {
            [_trtc stopRemoteView:userId];
        }
   }  
}
```

> ! 在 TRTCAppSceneLIVE 模式下，同一个房间中的观众（TRTCRoleAudience）人数没有限制。


### 8. 观众跟主播连麦
不管是主播还是观众，都可以通过 TRTCCloud 提供的 `switchRole` 进行角色间的相互切换，最常见的场景是观众跟主播连麦：观众可以通过该接口切换成“小主播”，然后跟房间里原来的“大主播”进行连麦互动。

```Objective-C
- (void)onClickedSwitch2Role:(BOOL)isAudience
{
    [_trtc switchRole:(isAudience? TRTCRoleAudience : TRTCRoleAnchor)];
    
    if (!isAudience) {
        // 切换到 “主播” 角色，开启本地的音视频上行
        [_trtc startLocalAudio];
        [self startPreview];
    }
    else {
        // 切换到 “观众” 角色，关闭本地的音视频上行
        [_trtc stopLocalAudio];
        [self stopPreview];
    }
}
```
  
### 9. 退出房间
调用 `exitRoom` 方法退出房间。无论当前是否还在通话中，调用该方法会把视频通话相关的所有资源释放掉。在您调用 `exitRoom` 之后，SDK 会进入一个复杂的退房握手流程，当 SDK 回调 `onExitRoom` 方法时才算真正完成资源的释放。

```Objective-C
- (void)exitRoom {
{
	[trtcCloud exitRoom];
}

- (void)onExitRoom:(NSInteger)reason {
	NSString *msg = [NSString stringWithFormat:@"离开房间[%u]: reason[%d]", _roomID, reason];
}
```


