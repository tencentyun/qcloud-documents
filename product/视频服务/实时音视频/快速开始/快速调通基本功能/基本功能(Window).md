本文介绍使用腾讯云 TRTC SDK 快速实现视频通话的功能，阅读此文档有助于您对 TRTC 的基本使用流程有一个简单的认识。


## 初始化 SDK

使用 TRTC SDK 的第一步，是先创建一个 `TRTCCloud` 的实例对象，并注册监听 SDK 事件的回调。

- 继承`ITRTCCloudCallback`事件回调接口类，实现关键事件的回调接口，包括本地用户进房/退房事件、远端用户加入/退出事件、错误事件、警告事件等。
- 调用`addCallback`接口注册监听 SDK 事件。**注意：如果`addCallback`注册 N 次，同一个事件， SDK 就会触发 N 次回调，建议只调用一次`addCallback`。**

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
    if(m_pTRTCSDK)
    {
        m_pTRTCSDK->removeCallback(this);
    }
    
    // 释放 TRTCCloud 实例
	if(m_pTRTCSDK != NULL)
    {
        delete m_pTRTCSDK;
        m_pTRTCSDK = null
    }
}

virtual void TRTCMainViewController::onError(TXLiteAVError errCode, const char* errMsg, void* arg)
{
    LOGE(L"onError errorCode[%d], errorInfo[%s]", errCode, UTF82Wide(errMsg).c_str());
    // 错误通知是要监听的，错误通知意味着 SDK 不能继续运行了
}

...
```

## 组装 TRTCParams

TRTCParams 是 SDK 最关键的一个参数，它包含如下四个必填的字段 sdkAppId，userId，userSig 和 roomId。

- **sdkAppId**
  进入腾讯云实时音视频[控制台](https://console.cloud.tencent.com/rav)，如果您还没有应用，请创建一个，即可看到 sdkAppId。
  ![](https://main.qcloudimg.com/raw/832b48f444e86c00097d3f9f322a3439.png)
- **userId**
  您可以随意指定，由于是字符串类型，可以直接跟您现有的账号体系保持一致，但请注意，**同一个音视频房间里不应该有两个同名的 userId**。
- **userSig**
  基于 sdkAppId 和 userId 可以计算出 userSig，计算方法请参考 [DOC](https://cloud.tencent.com/document/product/647/17275)。
- **roomId**
  房间号是数字类型，您可以随意指定，但请注意，**同一个应用里的两个音视频房间不能分配同一个 roomid**。

## 进入房间

组装完 `TRTCParams` 后，即可调用 `enterRoom` 函数加入(或创建)房间。

- 调用`enterRoom`接口进入房间，如果这个房间不存在，就会创建房间，并进入这个房间。
- 监听`onEnterRoom` 回调，这个回调触发时表示进入房间成功，参数`elapsed`表示进房耗时，单位ms。
- 监听`onError` 回调，进入房间失败时，触发这个回调，参数`errCode`的值是`ERR_ROOM_ENTER_FAIL`。
- 注意：如果已在房间中，则必须调用 `exitRoom` 接口退出当前房间，才能进入下一个房间。 

```c++
// TRTCMainViewController.cpp

void TRTCMainViewController::enterRoom()
{
    // TRTCParams 定义参考头文件TRTCCloudDef.h
    TRTCParams params;
    params.sdkAppId = sdkappid;
    params.userId = userid;
    params.userSig = usersig;
    params.roomId = "908"; // 输入房间Id
    if(m_pTRTCSDK)
    {
    	m_pTRTCSDK->enterRoom(params);
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

## 设置视频编码参数

调用 `setVideoEncoderParam`  接口，设置视频编码参数，影响远端用户看到画面的质量。

- 分辨率，视频画面的大小，默认是横屏分辨率，也就是宽屏模式，如果想要使用竖屏分辨率，请指定 resMode 为 Portrait，比如：640x360 + Portrait = 360x640；
- 帧率，影响视频播放的流畅性，推荐设置为 15fps 或 20fps；
- 码率，推荐设置请参考 TRTCVideoResolution 定义处的注释说明，对不同分辨率，推荐了比较合理的码率设置；
- 编码模式，Smooth 模式（默认）能够获得理论上最低的卡顿率，而 Compatible 模式卡顿率高于 Smooth 模式，但性能优异，推荐在低端设备上开启。 

```c++
// TRTCMainViewController.cpp

// 加入房间成功后，默认开启音视频流的上行。
void TRTCMainViewController::onEnterRoom(uint64_t elapsed)
{
    ...

    if(m_pTRTCSDK)
    {
        // 通常设置分辨率和码率，其他的字段，推荐使用TRTCVideoEncParam的默认值
        TRTCVideoEncParam param;
        param.videoResolution = TRTCVideoResolution_640_360;
        param.videoBitrate = 550;
        m_pTRTCSDK->setVideoEncoderParam(param);
    }
}
```

## 打开摄像头画面

调用`startLocalPreview`接口，打开摄像头和预览视频画面。

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

## 播放远端音视频

调用`startRemoteView`接口，播放远端用户的视频和音频。

- 本地用户进入房间后，当有远端用户也进入这个房间时，SDK 会触发`onUserEnter`回调，在这个回调中，调用`startRemoteView`接口，指定远端用户视频渲染的窗口；
- 调用`setRemoteViewFillMode`接口，设置远端视频渲染的模式为`Fill`或者 `Fit` 。两种模式下视频尺寸都是等比缩放，区别在于：
  - `Fill` 模式：优先保证窗口被填满。如果缩放后的视频尺寸与窗口尺寸不一致，那么多出的部分将被裁剪掉；
  - `Fit`   模式：优先保证视频内容全部显示。如果缩放后的视频尺寸与窗口尺寸不一致，未被填满的窗口区域将使用黑色填充。
- 当有远端用户也进入这个房间时，SDK 会触发`onUserExit`回调，在这个回调中，调用`stopRemoteView`接口，停止播放远端用户的视频和音频。

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

## 退出房间

调用`exitRoom`接口退出房间。

- 调用`exitRoom`接口完成退出房间，**注：SDK 会关闭摄像头，停止本地音频和视频上行、停止播放远端音频和视频等所有资源**。
- 监听`onUserExit`回调，**不管退房成功还是失败， SDK 都会触发这个回调，在这个回调触发才真正完成资源释放**。

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

