本文主要介绍腾讯云 TRTC SDK(Window) 的几个最基本功能的使用方法，阅读此文档有助于您对 TRTC 的基本使用流程有一个简单的认识。


## 初始化 SDK

使用 TRTC SDK 的第一步，是先创建一个 `TRTCCloud` 的实例对象，并注册监听 SDK 事件的回调。

- 继承`ITRTCCloudCallback`事件回调接口类，重写关键事件的回调接口，包括本地用户进房/退房事件、远端用户加入/退出事件、错误事件、警告事件等。
- 调用`addCallback`接口注册监听 SDK 事件。

>!如果`addCallback`注册 N 次，同一个事件， SDK 就会触发 N 次回调，建议只调用一次`addCallback`。

```c++
// TRTCMainViewController.h

// 继承 TRTCCloudListener 事件回调接口类
class TRTCMainViewController : public ITRTCCloudCallback
{
public:
	TRTCMainViewController();
	virtual ~TRTCMainViewController();

    virtual void onError(TXLiteAVError errCode, const char* errMsg, void* arg);
    virtual void onWarning(TXLiteAVWarning warningCode, const char* warningMsg, void* arg);
    virtual void onEnterRoom(uint64_t elapsed);
    virtual void onExitRoom(int reason);
    virtual void onUserEnter(const char* userId);
    virtual void onUserExit(const char* userId, int reason);
...
private:
	TRTCCloud * m_pTRTCSDK = NULL；
...
}

// TRTCMainViewController.cpp

TRTCMainViewController::TRTCMainViewController()
{
    // 创建 TRTCCloud 实例
    m_pTRTCSDK = new TRTCCloud;
    
    // 注册 SDK 回调事件
    m_pTRTCSDK->addCallback(this);
}

TRTCMainViewController::~TRTCMainViewController()
{
    // 取消监听 SDK 事件
    if(m_pTRTCSDK) {
        m_pTRTCSDK->removeCallback(this);
    }
    
    // 释放 TRTCCloud 实例
	  if(m_pTRTCSDK != NULL) {
        delete m_pTRTCSDK;
        m_pTRTCSDK = null;
    }
}

// 错误通知是要监听的，错误通知意味着 SDK 不能继续运行了
virtual void TRTCMainViewController::onError(TXLiteAVError errCode, const char* errMsg, void* arg)
{
    if (errCode == ERR_ROOM_ENTER_FAIL) {
        LOGE(L"onError errorCode[%d], errorInfo[%s]", errCode, UTF82Wide(errMsg).c_str());
		    exitRoom();
	 }
}
```

## 组装 TRTCParams

TRTCParams 是 SDK 最关键的一个参数，它包含如下四个必填的字段 SDKAppid，userId，userSig 和 roomId。

- **SDKAppid**
  进入腾讯云实时音视频[控制台](https://console.cloud.tencent.com/rav)，如果您还没有应用，请创建一个，即可看到 SDKAppid。
 ![](https://main.qcloudimg.com/raw/af782656b5042abce3dd8dc1f164791e.png)

- **userId**
  您可以随意指定，由于是字符串类型，可以直接跟您现有的账号体系保持一致，但请注意，**同一个音视频房间里不应该有两个同名的 userId**。

- **userSig**
  基于 SDKAppid 和 userId 可以计算出 userSig，计算方法请参考 [如何计算UserSig](https://cloud.tencent.com/document/product/647/17275)。

- **roomId**
  房间号是数字类型，您可以随意指定，但请注意，**同一个应用里的两个音视频房间不能分配同一个 roomId**。

## 进入（或创建）房间

调用 `enterRoom` 函数进入房间时，除了需要 TRTCParams 参数，还需要一个叫做 **appScene** 的参数，该参数是指定应用场景用的。

- **VideoCall** 对应视频通话场景，即绝大多数时间都是两人或两人以上视频通话的场景，内部编码器和网络协议优化侧重流畅性，降低通话延迟和卡顿率。
- **LIVE** 对应直播场景，即绝大多数时间都是一人直播，偶尔有多人视频互动的场景，内部编码器和网络协议优化侧重性能和兼容性，性能和清晰度表现更佳。		
- 如进入房间，SDK 会回调 `onEnterRoom` 接口，参数：`elapsed`代表进入耗时，单位ms。
- 如进房失败，SDK 会回调 `onError` 接口，参数：`errCode`（错误码`ERR_ROOM_ENTER_FAIL`，错误码可参考`TXLiteAVCode.h`）、`errMsg`（错误原因）、`extraInfo`（保留参数）。
- 如果已在房间中，则必须调用 `exitRoom` 方法退出当前房间，才能进入下一个房间。 

```c++
// TRTCMainViewController.cpp

void TRTCMainViewController::enterRoom()
{
    // TRTCParams 定义参考头文件TRTCCloudDef.h
    TRTCParams params;
    params.sdkAppId = sdkappid;
    params.userId   = userid;
    params.userSig  = usersig;
    params.roomId   = 908; // 输入您想进入的房间
    if(m_pTRTCSDK)
    {
    	m_pTRTCSDK->enterRoom(params, TRTCAppSceneVideoCall);
    }
}

...
    
void TRTCMainViewController::onError(TXLiteAVError errCode, const char* errMsg, void* arg)
{
    if(errCode == ERR_ROOM_ENTER_FAIL)
    {
        LOGE(L"onError errorCode[%d], errorInfo[%s]", errCode, UTF82Wide(errMsg).c_str());
        // 检查userSig是否合法、网络是否正常等
    }
}

...

void TRTCMainViewController::onEnterRoom(uint64_t elapsed)
{
    LOGI(L"onEnterRoom elapsed[%lld]", elapsed);
    
	// 启动本地的视频预览，请参考下面 设置视频编码参数 和 预览本地摄像头画面 的内容
}
```

>!请根据应用场景选择合适的 scene 参数，使用错误可能会导致卡顿率或画面清晰度不达预期。

## 收听远端音频流

- TRTC SDK 会默认接收远端的音频流，您无需为此编写额外的代码。
- 如果您不希望收听某一个 userid 的音频流，可以使用 `muteRemoteAudio`将其静音。

## 观看远端视频流

调用`startRemoteView`接口，播放远端用户的视频和音频。

- 本地用户进入房间后，当有远端用户也进入这个房间时，SDK 会触发`onUserEnter`回调，在这个回调中，调用`startRemoteView`接口，指定远端用户视频渲染的窗口；
- 调用`setRemoteViewFillMode`接口，设置远端视频渲染的模式为`Fill`或者 `Fit` 。两种模式下视频尺寸都是等比缩放，区别在于：
  - `Fill` 模式：优先保证窗口被填满。如果缩放后的视频尺寸与窗口尺寸不一致，那么多出的部分将被裁剪掉；
  - `Fit`   模式：优先保证视频内容全部显示。如果缩放后的视频尺寸与窗口尺寸不一致，未被填满的窗口区域将使用黑色填充。
- 当有远端用户退出这个房间时，SDK 会触发`onUserExit`回调，在这个回调中，调用`stopRemoteView`接口，停止播放远端用户的视频和音频。

```c++
// TRTCMainViewController.cpp

void TRTCMainViewController::onUserEnter(const char * userId)
{
    // 获取渲染窗口的句柄。
    CWnd *pRemoteVideoView = GetDlgItem(IDC_REMOTE_VIDEO_VIEW);
    HWND hwnd = pRemoteVideoView->GetSafeHwnd();
     
    if(m_pTRTCSDK)
    {
        // 设置远端用户视频的渲染模式。
        m_pTRTCSDK->setRemoteViewFillMode(TRTCVideoFillMode_Fill);

        // 调用SDK接口播放远端用户流。
        m_pTRTCSDK->startRemoteView(userId， hwnd);
    }
}

void TRTCMainViewController::onUserExit(const char* userId, int reason)
{
    if(m_pTRTCSDK)
    {
        m_pTRTCSDK->stopRemoteView(userId);
    }
}

```

## 开启（或关闭）本地声音采集
TRTC SDK 并不会默认打开本地的麦克风采集，`startLocalAudio`可以开启本地的声音采集并将音视频数据广播出去，`stopLocalAudio`则会关闭之。
- 您可以在 `startLocalPreview` 之后紧接着调用 `startLocalAudio`。

## 开启（或关闭）本地视频采集

TRTC SDK 并不会默认打开本地的摄像头采集，`startLocalPreview` 可以开启本地的摄像头并显示预览画面，`stopLocalPreview` 则会关闭之。

- 调用`startLocalPreview`，指定本地视频渲染的窗口，**注：SDK 动态检测窗口大小，在`rendHwnd`表示的整个窗口进行渲染**；
- 调用`setLocalViewFillMode`接口，设置本地视频渲染的模式为`Fill`或者 `Fit` 。两种模式下视频尺寸都是等比缩放，区别在于：
  - `Fill` 模式：优先保证窗口被填满。如果缩放后的视频尺寸与窗口尺寸不一致，那么多出的部分将被裁剪掉；
  - `Fit`   模式：优先保证视频内容全部显示。如果缩放后的视频尺寸与窗口尺寸不一致，未被填满的窗口区域将使用黑色填充。

```c++
// TRTCMainViewController.cpp

void TRTCMainViewController::onEnterRoom(uint64_t elapsed)
{
    ...
    
	// 获取渲染窗口的句柄。
    CWnd *pLocalVideoView = GetDlgItem(IDC_LOCAL_VIDEO_VIEW);
    HWND hwnd = pLocalVideoView->GetSafeHwnd();
    
    if(m_pTRTCSDK)
    {
        // 调用SDK接口设置渲染模式和渲染窗口。
        m_pTRTCSDK->setLocalViewFillMode(TRTCVideoFillMode_Fit);
        m_pTRTCSDK->startLocalPreview(hwnd);
    }
    
	...
}
```

## 屏蔽音视频数据流

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

## 退出房间

调用`exitRoom`方法退出房间。不论当前是否还在通话中，调用该方法会把视频通话相关的所有资源释放掉。
- 在您调用`exitRoom`之后，SDK 会进入一个复杂的退房握手流程，当 SDK 回调 `onExitRoom` 方法时才算真正完成资源的释放。

```c++
// TRTCMainViewController.cpp

void TRTCMainViewController::exitRoom()
{
    if(m_pTRTCSDK)
    {
    	m_pTRTCSDK->exitRoom();
    }
}
....
void TRTCMainViewController::onExitRoom(int reason)
{
	// 退房成功，reason参数保留，暂未使用。

    ...
}
```

