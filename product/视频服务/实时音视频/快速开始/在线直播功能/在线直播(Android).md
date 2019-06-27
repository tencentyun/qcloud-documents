
## 文档导读
本文主要介绍如何基于 TRTC SDK 实现一个既支持视频连麦，又支持上万人高并发观看的在线直播功能：

- 本文仅提及了最基本的几个功能，如果您希望了解更多高级功能，请参见 [高级功能](https://cloud.tencent.com/document/product/647/32227)。
- 本文仅罗列了最常用的几个接口，如果您希望了解更多的接口函数，请参见 [API 文档](https://cloud.tencent.com/document/product/647/32228)。

## 示例代码

| 所属平台 | 示例代码 | 
|---------|---------|
| Android | [TRTCMainActivity.java](https://github.com/tencentyun/TRTCSDK/blob/master/Android/TRTCDemo/app/src/main/java/com/tencent/liteav/demo/trtc/TRTCMainActivity.java) | 
| iOS | [TRTCMainViewController.m](https://github.com/tencentyun/TRTCSDK/blob/master/iOS/TRTCDemo/TRTC/TRTCMainViewController.m) | 
| Mac OS | [TRTCMainWindowController.m](https://github.com/tencentyun/TRTCSDK/blob/master/Mac/TRTCDemo/TRTC/TRTCMainWindowController.m) | 
| Windows（MFC） | [TRTCMainViewController.cpp](https://github.com/tencentyun/TRTCSDK/blob/master/Windows/MFCDemo/TRTCMainViewController.cpp) |
| Windows（Duilib） | [TRTCMainViewController.cpp](https://github.com/tencentyun/TRTCSDK/blob/master/Windows/DuilibDemo/TRTCMainViewController.cpp) |

![](https://main.qcloudimg.com/raw/b5013afb3606fa02ce6c622b4e7085db.jpeg)

## 在线直播
### 1. 初始化 SDK

使用 TRTC SDK 的第一步，是先获取 `TRTCCloud` 的单例对象，并注册监听 SDK 事件的回调。

- 先继承 `TRTCCloudListener` 抽象类并重写您需要监听的事件（eg：用户加入房间、用户退出房间、警告信息和错误信息等）。
- 获取 `TRTCCloud` 单例对象，调用 setListener 方法设置 `TRTCCloudListener` 回调。

```java
import com.tencent.trtc.TRTCCloud;
import com.tencent.trtc.TRTCCloudListener;

// 继承 TRTCCloudListener 回调
static class TRTCCloudListenerImpl extends TRTCCloudListener {
	private WeakReference<TRTCMainActivity> mContext;
    public TRTCCloudListenerImpl(TRTCMainActivity activity) {
        super();
        mContext = new WeakReference<>(activity);
    }
	....
	// 错误通知是要监听的，错误通知意味着 SDK 不能继续运行了
	@Override
	public void onError(int errCode, String errMsg, Bundle extraInfo) {
	    Log.d(TAG, "sdk callback onError");
	    TRTCMainActivity activity = mContext.get();
	    if (activity != null) {
	        Toast.makeText(activity, "onError: " + errMsg + "[" + errCode+ "]" , Toast.LENGTH_SHORT).show();
	        if (errCode == TXLiteAVCode.ERR_ROOM_ENTER_FAIL) {
	            activity.exitRoom();
	        }
	    }
	}
}

// 在activity创建时获取 trtcCloud 单例
@Override
protected void onCreate(Bundle savedInstanceState) {
	super.onCreate(savedInstanceState);
	....
	trtcListener = new TRTCCloudListenerImpl(this);
    trtcCloud = TRTCCloud.sharedInstance(this);
    trtcCloud.setListener(listener);
}

// 销毁 trtcCloud 实例，在不再使用SDK能力时，销毁单例，节省开销
@Override
protected void onDestroy() {
    super.onDestroy();
    //销毁 trtc 实例
    if (trtcCloud != null) {
        trtcCloud.setListener(null);
    }
    trtcCloud = null;
    TRTCCloud.destroySharedInstance();
}

```

### 2. 组装 TRTCParams

TRTCParams 是 SDK 最关键的一个参数，它包含如下四个必填的字段 sdkAppId、userId、userSig 和 roomId。

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

```java
/** 打开本地摄像头预览画面 */
void startLocalPreview(boolean frontCamera, TXCloudVideoView localVideoView) {
	trtcCloud.setLocalViewFillMode(TRTCCloudDef.TRTC_VIDEO_RENDER_MODE_FIT);
	trtcCloud.startLocalPreview(frontCamera, localVideoView);
}
```

### 4. 主播开启麦克风采集
TRTC SDK 并不会默认打开本地的麦克风采集，主播调用 `startLocalAudio` 可以开启本地的声音采集并将音视频数据广播出去，`stopLocalAudio` 则会关闭。您可以在 `startLocalPreview` 之后继续调用 `startLocalAudio`。

>`startLocalAudio` 会检查麦克风使用权限，如果没有麦克风权限，SDK 会向用户申请开启。

### 5. 主播创建新房间开播

主播可以使用 `enterRoom` 创建一个音视频房间，参数 `TRTCParams` 中的 `roomId` 用于指定房间号，同时，我们还需要将 `role` 字段指定为 `TRTCRoleAnchor`（主播）。

`appScene` 参数指定 SDK 的应用场景，本文档中我们使用 `TRTC_APP_SCENE_LIVE`（在线直播）。

- 如创建成功，SDK 会回调 `onEnterRoom` 接口，参数：`elapsed` 代表进入耗时，单位：ms。
- 如创建失败，SDK 会回调 `onError` 接口，参数：`errCode`（错误码 `ERR_ROOM_ENTER_FAIL`，错误码可参考 `TXLiteAVCode.h`）、`errMsg`（错误原因）、`extraInfo`（保留参数）。

```java
void startBroadCasting() {
	//TRTCParams 定义参考头文件TRTCCloudDef.java
	trtcParams = new TRTCCloudDef.TRTCParams();
	trtcParams.sdkAppId = sdkappid;
	trtcParams.userId   = userid;
	trtcParams.userSig  = usersig;
	trtcParams.roomId   = 908; //输入您想进入的房间
	trtcParams.role     = TRTCRoleAnchor; //当前角色为主播
	trtcCloud.enterRoom(trtcParams, TRTC_APP_SCENE_LIVE);
}

@Override
public void onError(int errCode, String errMsg, Bundle extraInfo) {
    Log.d(TAG, "sdk callback onError");
    TRTCMainActivity activity = mContext.get();
    if (activity != null) {
        Toast.makeText(activity, "onError: " + errMsg + "[" + errCode+ "]" , Toast.LENGTH_SHORT).show();
        if (errCode == TXLiteAVCode.ERR_ROOM_ENTER_FAIL) {
            activity.exitRoom();
        }
    }
}

@Override
public void onEnterRoom(long elapsed) {
    TRTCMainActivity activity = mContext.get();
    if (activity != null) {
        Toast.makeText(activity, "加入房间成功", Toast.LENGTH_SHORT).show();
    }
}
```

### 6. 主播开关隐私模式
直播过程中，主播可能出于隐私目的希望屏蔽本地的音视频数据，可以调用 `muteLocalVideo` 屏蔽本地的视频采集，调用 `muteLocalAudio` 屏蔽本地的音频采集。
	
### 7. 观众加入房间观看

观众调用 `enterRoom` 可以进入一个音视频房间，参数 TRTCParams 中的 `roomId` 用于指定房间号。
`appScene` 同样填写 `TRTC_APP_SCENE_LIVE`（在线直播），但 `role` 字段需要指定为 `TRTCRoleAudience`（观众）。

```java
- (void)startPlaying {
	//TRTCParams 定义参考头文件TRTCCloudDef.java
	trtcParams = new TRTCCloudDef.TRTCParams();
	trtcParams.sdkAppId = sdkappid;
	trtcParams.userId   = userid;
	trtcParams.userSig  = usersig;
	trtcParams.roomId   = 908; //输入您想进入的房间
	trtcParams.role     = TRTCRoleAudience; //当前角色为观众
	trtcCloud.enterRoom(trtcParams, TRTC_APP_SCENE_LIVE);
}
```

如果主播在房间里，观众会通过 TRTCCloudListener 中的 `onUserVideoAvailable` 回调获知主播的 userid。之后，观众可以调用 `startRemoteView` 方法来显示主播的视频画面。

通过 `setRemoteViewFillMode` 可以指定视频显示模式为 `Fill` 或 `Fit` 模式。两种模式下视频尺寸都是等比缩放，区别在于：
- `Fill` 模式：优先保证视窗被填满。如果缩放后的视频尺寸与显示视窗尺寸不一致，多出的视频将被截掉。
- `Fit` 模式：优先保证视频内容全部显示。如果缩放后的视频尺寸与显示视窗尺寸不一致，未被填满的视窗区域将使用黑色填充。

```java
@Override
public void onUserVideoAvailable(final String userId, boolean available){
    TRTCMainActivity activity = mContext.get();
    if (activity != null) {
        if (available) {
            // 设置remoteView
            TXCloudVideoView remoteView = new TXCloudVideoView(mContext);
            mParentView.add(remoteView);
            trtcCloud.setRemoteViewFillMode(userId, TRTCCloudDef.TRTC_VIDEO_RENDER_MODE_FIT);
            trtcCloud.startRemoteView(userId, remoteView);
        } else {
            //停止观看画面
            trtcCloud.stopRemoteView(userId);
        }
    }
}
```

> ! 在 TRTC_APP_SCENE_LIVE 模式下，同一个房间中的观众（TRTCRoleAudience）人数没有限制。


### 8. 观众跟主播连麦
	
观众或主播都可以通过 TRTCCloud 提供的 `switchRole` 接口切换自己的角色，最常见的场景是观众跟主播连麦：观众通过如下代码可以切换到主播角色，也就是把自己变成“小主播”，跟房间里原来的“大主播”进行连麦通话。

```java
public void onChangeRole(int role) {
	trtcCloud.switchRole(role);
        
if (role == TRTCCloudDef.TRTCRoleAnchor) { //切换到“主播”角色
	startLocalVideo(true); // 开启本地视频
	trtcCloud.startLocalAudio(); // 开启本地音频
} else { // 切换到“观众”角色，观众不需要上行音频和视频
	startLocalVideo(false);
	trtcCloud.stopLocalAudio();
}
}
```
  
### 9. 退出房间
调用 `exitRoom` 方法退出房间。无论当前是否还在通话中，调用该方法会把视频通话相关的所有资源释放掉。在您调用 `exitRoom` 之后，SDK 会进入一个复杂的退房握手流程，当 SDK 回调 `onExitRoom` 方法时才算真正完成资源的释放。

```java
...
private void exitRoom() {
    if (trtcCloud != null) {
        trtcCloud.exitRoom();
    }
}
...
@Override
public void onExitRoom(int reason) {
    TRTCMainActivity activity = mContext.get();
    if (activity != null) {
        activity.finishActivity();
    }
}

```


