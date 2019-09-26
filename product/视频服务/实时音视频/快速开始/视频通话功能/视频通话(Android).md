## 文档导读
本文主要介绍如何基于 TRTC SDK 实现一个简单的视频通话功能：

- 本文仅提及最基本的几个功能，如果您希望了解更多高级功能，请参见 [高级功能](https://cloud.tencent.com/document/product/647/16826)。
- 本文仅罗列最常用的几个接口，如果您希望了解更多的接口函数，请参见 [API 文档](https://cloud.tencent.com/document/product/647/32258)。

## 示例代码

| 所属平台 | 示例代码 | 
|---------|---------|
| Android | [TRTCMainActivity.java](https://github.com/tencentyun/TRTCSDK/blob/master/Android/TRTCDemo/app/src/main/java/com/tencent/liteav/demo/trtc/TRTCMainActivity.java) | 
| iOS | [TRTCMainViewController.m](https://github.com/tencentyun/TRTCSDK/blob/master/iOS/TRTCDemo/TRTC/TRTCMainViewController.m) | 
| Mac OS | [TRTCMainWindowController.m](https://github.com/tencentyun/TRTCSDK/blob/master/Mac/TRTCDemo/TRTC/TRTCMainWindowController.m) | 
| Windows（MFC） | [TRTCMainViewController.cpp](https://github.com/tencentyun/TRTCSDK/blob/master/Windows/MFCDemo/TRTCMainViewController.cpp) |
| Windows（Duilib） | [TRTCMainViewController.cpp](https://github.com/tencentyun/TRTCSDK/blob/master/Windows/DuilibDemo/TRTCMainViewController.cpp) |

![](https://main.qcloudimg.com/raw/b5013afb3606fa02ce6c622b4e7085db.jpeg)


## 视频通话
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


### 3. 进入(或创建)房间
调用 `enterRoom` 可以加入 TRTCParams 参数中 roomId 所指定的音视频房间。如果该房间不存在，SDK 会自动创建一个以 roomId 为房间号的新房间。

**appScene** 参数指定 SDK 的应用场景，本文档中我们使用 `TRTCAppSceneVideoCall`（视频通话），该场景下 SDK 内部的编解码器和网络组件会更加侧重视频流畅性，降低通话延迟和卡顿率。

- 如进房成功，SDK 会回调 `onEnterRoom` 接口，参数：当 `result` 大于0时，进房成功，数值表示加入房间所消耗的时间，单位为毫秒（ms）；当 `result` 小于0时，进房失败，数值表示进房失败的错误码。
- 如进房失败，SDK 同时会回调 `onError` 接口，参数：`errCode`（错误码 `ERR_ROOM_ENTER_FAIL`，错误码可参考 `TXLiteAVCode.h`）、`errMsg`（错误原因）、`extraInfo`（保留参数）。
- 如果已在房间中，则必须调用 `exitRoom` 方法退出当前房间，才能进入下一个房间。 

```java
void enterRoom() {
	//TRTCParams 定义参考头文件TRTCCloudDef.java
	trtcParams = new TRTCCloudDef.TRTCParams();
	trtcParams.sdkAppId = sdkappid;
	trtcParams.userId   = userid;
	trtcParams.userSig  = usersig;
	trtcParams.roomId   = 908; //输入您想进入的房间
	trtcCloud.enterRoom(trtcParams, TRTC_APP_SCENE_VIDEOCALL);
}

...

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

>!请根据应用场景选择合适的 scene 参数，使用错误可能会导致卡顿率或画面清晰度不达预期。

### 4. 收听远端音频流
TRTC SDK 会默认接收远端的音频流，您无需为此编写额外的代码。如果您不希望收听某一个 userid 的音频流，可以使用 `muteRemoteAudio` 将其静音。

### 5. 观看远端视频流
TRTC SDK 并不会默认拉取远端的视频流，当房间里有用户上行视频数据时，房间里的其他用户可以通过 TRTCCloudListener 中的 `onUserVideoAvailable` 回调获知该用户的 userid。之后，即可调用 `startRemoteView` 方法来显示该用户的视频画面。

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

### 6. 开关本地声音采集
TRTC SDK 并不会默认打开本地的麦克风采集，`startLocalAudio` 可以开启本地的声音采集并将音视频数据广播出去，`stopLocalAudio` 则会关闭。

- `startLocalAudio` 会检查麦克风使用权限，如果没有麦克风权限，SDK 会向用户申请开启。
- 您可以在 `startLocalPreview` 之后继续调用 `startLocalAudio`。

### 7. 开关本地视频采集

TRTC SDK 并不会默认打开本地的摄像头采集，`startLocalPreview` 可以开启本地的摄像头并显示预览画面，`stopLocalPreview` 则会关闭。

- 启动本地预览前，可调用 `setLocalViewFillMode` 指定视频显示模式为 `Fill` 或 `Fit` 模式。两种模式下视频尺寸都是等比缩放，区别在于：  
	- `Fill` 模式：优先保证视窗被填满。如果缩放后的视频尺寸与显示视窗尺寸不一致，多出的视频将被截掉。  
	- `Fit`   模式：优先保证视频内容全部显示。如果缩放后的视频尺寸与显示视窗尺寸不一致，未被填满的视窗区域将使用黑色填充。

- 调用 `startLocalPreview`，参数：`frontCamera`（true：前置摄像头；false：后置摄像头）、`view`（TXCloudVideoView SDK 自定义渲染控件）。

```java
/** 打开本地摄像头预览画面 */
void startLocalPreview(boolean frontCamera, TXCloudVideoView localVideoView) {
	trtcCloud.setLocalViewFillMode(TRTCCloudDef.TRTC_VIDEO_RENDER_MODE_FIT);
    trtcCloud.startLocalPreview(frontCamera, localVideoView);
}
```

### 8. 屏蔽音视频数据流

- **屏蔽本地视频数据**
  如果用户在通话过程中，出于隐私目的希望屏蔽本地的视频数据，让房间里的其他用户暂时无法看到您的画面，可以调用 `muteLocalVideo`。
  
- **屏蔽本地音频数据**
  如果用户在通话过程中，出于隐私目的希望屏蔽本地的音频数据，让房间里的其他用户暂时无法听到您的声音，可以调用 `muteLocalAudio`。
  
- **屏蔽远程视频数据**
  通过 `stopRemoteView` 可以屏蔽某一个 userid 的视频数据。
  通过 `stopAllRemoteView` 可以屏蔽所有远端用户的视频数据。
  
- **屏蔽远程音频数据**
  通过 `muteRemoteAudio` 可以屏蔽某一个 userid 的音频数据。
  通过 `muteAllRemoteAudio` 可以屏蔽所有远端用户的音频数据。


### 9. 退出房间

调用 `exitRoom` 方法退出房间。不论当前是否还在通话中，调用该方法会把视频通话相关的所有资源释放掉。

>在您调用 `exitRoom` 之后，SDK 会进入一个复杂的退房握手流程，当 SDK 回调 `onExitRoom` 方法时才算真正完成资源的释放。

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

