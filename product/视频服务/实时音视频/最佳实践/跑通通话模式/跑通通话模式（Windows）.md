## 文档导读
本文主要介绍如何基于 TRTC SDK 实现一个简单的视频通话功能。本文仅罗列最常用的几个接口，如果您希望了解更多的接口函数，请参见 [API 文档](https://cloud.tencent.com/document/product/647/32258)。


## 示例代码

| 所属平台 | 示例代码 |
|---------|---------|
| Windows（MFC） | [TRTCMainViewController.cpp](https://github.com/tencentyun/TRTCSDK/blob/master/Windows/MFCDemo/TRTCMainViewController.cpp) |
| Windows（Duilib） | [TRTCMainViewController.cpp](https://github.com/tencentyun/TRTCSDK/blob/master/Windows/DuilibDemo/TRTCMainViewController.cpp) |
| Windows（C#） | [TRTCMainForm.cs](https://github.com/tencentyun/TRTCSDK/blob/master/Windows/CSharpDemo/TRTCMainForm.cs) |

## 视频通话
### 1. 初始化 SDK
使用 TRTC SDK 的第一步，是先通过 `getTRTCShareInstance` 导出接口获取一个 `TRTCCloud` 单实例对象的指针 `ITRTCCloud*`，并注册监听 SDK 事件的回调。

- 继承 `ITRTCCloudCallback` 事件回调接口类，重写关键事件的回调接口，包括本地用户进房/退房事件、远端用户加入/退出事件、错误事件和警告事件等。
- 调用 `addCallback` 接口注册监听 SDK 事件。

>!如果 `addCallback` 注册 N 次，同一个事件， SDK 就会触发 N 次回调，建议只调用一次 `addCallback`。

<dx-codeblock>
::: C++ C++
// TRTCMainViewController.h

// 继承 ITRTCCloudCallback 事件回调接口类
class TRTCMainViewController : public ITRTCCloudCallback
{
public:
	TRTCMainViewController();
	virtual ~TRTCMainViewController();

    virtual void onError(TXLiteAVError errCode, const char* errMsg, void* arg);
    virtual void onWarning(TXLiteAVWarning warningCode, const char* warningMsg, void* arg);
    virtual void onEnterRoom(int result);
    virtual void onExitRoom(int reason);
    virtual void onRemoteUserEnterRoom(const char* userId);
    virtual void onRemoteUserLeaveRoom(const char* userId, int reason);
    virtual void onUserVideoAvailable(const char* userId, bool available);
    virtual void onUserAudioAvailable(const char* userId, bool available);
...
private:
	ITRTCCloud * m_pTRTCSDK = NULL；
...
}

// TRTCMainViewController.cpp

TRTCMainViewController::TRTCMainViewController()
{
    // 创建 TRTCCloud 实例
    m_pTRTCSDK = getTRTCShareInstance();
    
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
       destroyTRTCShareInstance();
        m_pTRTCSDK = null;
    }
}

// 错误通知是需要监听的，错误通知意味着 SDK 无法继续运行
virtual void TRTCMainViewController::onError(TXLiteAVError errCode, const char* errMsg, void* arg)
{
    if (errCode == ERR_ROOM_ENTER_FAIL) {
        LOGE(L"onError errorCode[%d], errorInfo[%s]", errCode, UTF82Wide(errMsg).c_str());
		    exitRoom();
	 }
}
:::
::: C# C#
// TRTCMainForm.cs

// 继承 ITRTCCloudCallback 事件回调接口类
public partial class TRTCMainForm : Form, ITRTCCloudCallback, ITRTCLogCallback
{
	...
	private ITRTCCloud mTRTCCloud; 
	...
	
	public TRTCMainForm(TRTCLoginForm loginForm)
    {
    	InitializeComponent();
    	this.Disposed += new EventHandler(OnDisposed);
    	// 创建 TRTCCloud 实例
    	mTRTCCloud = ITRTCCloud.getTRTCShareInstance();
    	// 注册 SDK 回调事件
    	mTRTCCloud.addCallback(this);
    	...
    }
    
    private void OnDisposed(object sender, EventArgs e)
    {
    	if (mTRTCCloud != null)
    	{
    		// 取消监听 SDK 事件
    		mTRTCCloud.removeCallback(this);
    		// 释放 TRTCCloud 实例
    		ITRTCCloud.destroyTRTCShareInstance();
    		mTRTCCloud = null;
    	}
    	...
    }
    ...
    // 错误通知是需要监听的，错误通知意味着 SDK 无法继续运行
    public void onError(TXLiteAVError errCode, string errMsg, IntPtr arg)
    {
         if (errCode == TXLiteAVError.ERR_ROOM_ENTER_FAIL) {
		    exitRoom();
		}
         ...
    }
    ...
}
:::
</dx-codeblock>

### 2. 组装 TRTCParams

TRTCParams 是 SDK 最关键的一个参数，它包含如下四个必填的字段：SDKAppID、userId、userSig 和 roomId。

- **SDKAppID**
  进入腾讯云实时音视频 [控制台](https://console.cloud.tencent.com/rav)，如果您还没有应用，请创建一个，即可看到 SDKAppID。
  ![](https://main.qcloudimg.com/raw/e42c76fd9d4fd3e3e5d80e8fb2763134.png)

- **userId**
  您可以随意指定，由于是字符串类型，可以直接跟您现有的账号体系保持一致，但请注意，**同一个音视频房间里不应该有两个同名的 userId**。

- **userSig**
  基于 SDKAppID 和 userId 可以计算出 userSig，计算方法请参见 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。

- **roomId**
  房间号是数字类型，您可以随意指定，但请注意，**同一个应用里的两个音视频房间不能分配同一个 roomId**。如果您想使用字符串形式的房间号，请使用 TRTCParams 中的 strRoomId。

### 3. 进入（或创建）房间
调用 `enterRoom` 可以加入 TRTCParams 参数中 roomId 所指定的音视频房间。如果该房间不存在，SDK 会自动创建一个以 roomId 为房间号的新房间。

**appScene** 参数指定 SDK 的应用场景，本文档中我们使用 `TRTCAppSceneVideoCall`（视频通话），该场景下 SDK 内部的编解码器和网络组件会更加侧重视频流畅性，降低通话延迟和卡顿率。
				
- 如进房成功，SDK 会回调 `onEnterRoom` 接口，参数：当 `result` 大于0时，进房成功，数值表示加入房间所消耗的时间，单位为毫秒（ms）；当 `result` 小于0时，进房失败，数值表示进房失败的错误码。
- 如进房失败，SDK 同时会回调 `onError` 接口，参数：`errCode`（错误码 `ERR_ROOM_ENTER_FAIL`，错误码可参考 `TXLiteAVCode.h`）、`errMsg`（错误原因）、`extraInfo`（保留参数）。
- 如果已在房间中，则必须调用 `exitRoom` 方法退出当前房间，才能进入下一个房间。 

<dx-codeblock>
::: C++ C++
// TRTCMainViewController.cpp

void TRTCMainViewController::enterRoom()
{
    // TRTCParams 定义参考头文件 TRTCCloudDef.h
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
        // 检查 userSig 是否合法、网络是否正常等
    }
}

...

void TRTCMainViewController::onEnterRoom(int result)
{
    LOGI(L"onEnterRoom result[%d]", result);
    if(result >= 0)
	{
		//进房成功
	}
	else
	{
		//进房失败，错误码 = result；
	}
}
:::
::: C# C#
// TRTCMainForm.cs

public void EnterRoom()
{
    // TRTCParams 定义参考头文件 TRTCCloudDef.h
    TRTCParams @params = new TRTCParams();
    @params.sdkAppId = sdkappid;
    @params.userId   = userid;
    @params.userSig  = usersig;
    @params.roomId   = 908; // 输入您想进入的房间
    if(mTRTCCloud != null)
    {
    	mTRTCCloud.enterRoom(@params, TRTCAppSceneVideoCall);
    }
}

...
    
public void onError(TXLiteAVError errCode, string errMsg, IntPtr arg)
{
    if(errCode == TXLiteAVError.ERR_ROOM_ENTER_FAIL)
    {
        Log.E(String.Format("errCode : {0}, errMsg : {1}, arg = {2}", errCode, errMsg, arg));
        // 检查 userSig 是否合法、网络是否正常等
    }
}

...

public void onEnterRoom(int result)
{
    if(result >= 0)
	{
		//进房成功
	}
	else
	{
		//进房失败，错误码 = result；
	}
}
:::
</dx-codeblock>


>!
>- 请根据应用场景选择合适的 scene 参数，使用错误可能会导致卡顿率或画面清晰度不达预期。
>- 每个端在应用场景 appScene 上必须要进行统一，否则会出现一些不可预料的问题。

### 4. 收听远端音频流
TRTC SDK 会默认接收远端的音频流，您无需为此编写额外的代码。如果您不希望收听某一个 userid 的音频流，可以使用 `muteRemoteAudio` 将其静音。

### 5. 观看远端视频流

TRTC SDK 并不会默认拉取远端的视频流，当房间里有用户上行视频数据时，房间里的其他用户可以通过 ITRTCCloudCallback 中的 `onUserVideoAvailable` 回调获知该用户的 userid。之后，即可调用 `startRemoteView` 方法来显示该用户的视频画面。

通过 `setRemoteViewFillMode` 可以指定视频显示模式为 `Fill` 或 `Fit` 模式。两种模式下视频尺寸都是等比缩放，区别在于：
- `Fill` 模式：优先保证视窗被填满。如果缩放后的视频尺寸与显示视窗尺寸不一致，多出的视频将被截掉。
- `Fit` 模式：优先保证视频内容全部显示。如果缩放后的视频尺寸与显示视窗尺寸不一致，未被填满的视窗区域将使用黑色填充。

<dx-codeblock>
::: C++ C++
// TRTCMainViewController.cpp
void TRTCMainViewController::onUserVideoAvailable(const char* userId, bool available){
    if (available) {
        // 获取渲染窗口的句柄。
        CWnd *pRemoteVideoView = GetDlgItem(IDC_REMOTE_VIDEO_VIEW);
        HWND hwnd = pRemoteVideoView->GetSafeHwnd();  
        
        // 设置远端用户视频的渲染模式。
        m_pTRTCSDK->setRemoteViewFillMode(TRTCVideoFillMode_Fill);
        // 调用 SDK 接口播放远端用户流。
        m_pTRTCSDK->startRemoteView(userId， hwnd);
    } else {
        m_pTRTCSDK->stopRemoteView(userId);
    }    
}
:::
::: C# C#
// TRTCMainForm.cs
public void onUserVideoAvailable(string userId, bool available)
{
    if (available)
	{
		// 获取窗口句柄
		IntPtr ptr = GetHandleAndSetUserId(pos, userId, false);
		SetVisableInfoView(pos, false);
		// 设置远端用户视频的渲染模式。
		mTRTCCloud.setRemoteViewFillMode(userId, TRTCVideoFillMode.TRTCVideoFillMode_Fit);
		// 调用 SDK 接口播放远端用户流。
		mTRTCCloud.startRemoteView(userId, ptr);
	}
	else
	{
		mTRTCCloud.stopRemoteView(userId);
		...
	}
}
:::
</dx-codeblock>


### 6. 开关本地声音采集

TRTC SDK 并不会默认打开本地的麦克风采集，`startLocalAudio` 可以开启本地的声音采集并将音视频数据广播出去，`stopLocalAudio` 则会关闭。
>?您可以在 `startLocalPreview` 之后继续调用 `startLocalAudio`。

### 7. 开关本地视频采集

TRTC SDK 并不会默认打开本地的摄像头采集，`startLocalPreview` 可以开启本地的摄像头并显示预览画面，`stopLocalPreview` 则会关闭。

- 调用 `startLocalPreview`，指定本地视频渲染的窗口，**SDK 动态检测窗口大小，在 `rendHwnd` 表示的整个窗口进行渲染**。
- 调用 `setLocalViewFillMode` 接口，设置本地视频渲染的模式为 `Fill` 或者 `Fit` 。两种模式下视频尺寸都是等比缩放，区别在于：
  - `Fill` 模式：优先保证窗口被填满。如果缩放后的视频尺寸与窗口尺寸不一致，那么多出的部分将被裁剪掉。
  - `Fit`   模式：优先保证视频内容全部显示。如果缩放后的视频尺寸与窗口尺寸不一致，未被填满的窗口区域将使用黑色填充。

<dx-codeblock>
::: C++ C++
// TRTCMainViewController.cpp

void TRTCMainViewController::onEnterRoom(uint64_t elapsed)
{
    ...
    
	// 获取渲染窗口的句柄。
    CWnd *pLocalVideoView = GetDlgItem(IDC_LOCAL_VIDEO_VIEW);
    HWND hwnd = pLocalVideoView->GetSafeHwnd();
    
    if(m_pTRTCSDK)
    {
        // 调用 SDK 接口设置渲染模式和渲染窗口。
        m_pTRTCSDK->setLocalViewFillMode(TRTCVideoFillMode_Fit);
        m_pTRTCSDK->startLocalPreview(hwnd);
    }
    
	...
}
:::
::: C# C#
// TRTCMainForm.cs

public void onEnterRoom(int result)
{
	...
	// 获取渲染窗口的句柄。
	IntPtr ptr = GetHandle();
    if (mTRTCCloud != null)
    {
        // 调用 SDK 接口设置渲染模式和渲染窗口。
        mTRTCCloud.setLocalViewFillMode(TRTCVideoFillMode_Fit);
        mTRTCCloud.startLocalPreview(ptr);
    }
	...
}
:::
</dx-codeblock>


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
>?在您调用 `exitRoom` 之后，SDK 会进入一个复杂的退房握手流程，当 SDK 回调 `onExitRoom` 方法时才算真正完成资源的释放。
<dx-codeblock>
::: C++ C++
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
	// 退房成功，reason 参数保留，暂未使用。

    ...
}
:::
::: C# C#
// TRTCMainForm.cs

public void OnExit()
{
    if(mTRTCCloud != null)
    {
    	mTRTCCloud.exitRoom();
    }
}
...
public void onExitRoom(int reason)
{
    // 退房成功
    ...
}
:::
</dx-codeblock>

