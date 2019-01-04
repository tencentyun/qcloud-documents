本文主要介绍腾讯云 TRTC SDK 的几个最基本功能的使用方法，阅读此文档有助于您对 TRTC 的基本使用流程有一个简单的认识。


## 初始化 SDK

使用 TRTC SDK 的第一步，是先创建一个 `TRTCCloud` 的实例对象，并注册监听 SDK 事件的回调。

- 先继承`ITRTCCloudCallback`虚接口类并重写你需要监听的方法（eg：接口调用状态、其他用户加入房间、其他用户退出房间、警告信息、错误信息等 SDK 回调接口）。
- 创建一个`TRTCCloud`实例，并在使用其他功能之前，调用`addCallback`注册事件回调（注：`addCallback`注册 N 次， SDK 就会回调 N 次，建议只调用一次`addCallback`）。
- 在您不需要 SDK 回调或者释放`TRTCCloud`之前，需要调用`removeCallback`删除回调。

```c++
//TRTCMainViewController.h 申明
class TRTCMainViewController : public ITRTCCloudCallback
{
...
public:
    virtual void onError(TXLiteAVError errCode, const char* errMsg, void* arg);
    virtual void onEnterRoom(uint64_t elapsed);
    virtual void onUserEnter(const char* userId);
...
private:
	TRTCCloud * m_pTRTCSDK = NULL；
...
}

//TRTCMainViewController.cpp 定义
TRTCMainViewController::TRTCMainViewController()
{
    m_pTRTCSDK = new TRTCCloud;
    m_pTRTCSDK->addCallback(this);
    ...
}
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

## 进入(或创建)房间

组装完 `TRTCParams` 后，即可调用 `enterRoom` 函数进入房间。

- 进入房间前，请确保您已成功获取`sdkappid、userid、usersig`信息，详情参考【获取账户信息】。
- 进房前需要初始化`TRTCParams`结构体中：`sdkAppId、userSig、usersig、roomId`信息，然后调用`enterRoom`接口。
- 如进入房间，SDK 会回调`onEnterRoom`接口，参数：`elapsed`代表进入耗时，单位ms。
- 如进房失败 SDK 会回调`onError`接口，参数：`errCode`（错误码`ERR_ROOM_ENTER_FAIL`，错误码可参考`TXLiteAVCode.h`）、`errMsg`（错误原因）、`arg`（保留参数）。
- 如果已在房间中，则必须调用 `exitRoom` 方法退出当前房间，才能进入下一个房间。 

```c++
void TRTCMainViewController::enterRoom()
{
    //TRTCParams 定义参考头文件TRTCCloudDef.h
    TRTCParams params;
    params.sdkAppId = sdkappid;
    params.userId = userid;
    params.userSig = usersig;
    params.roomId = 908; //输入你想进入的房间
    m_pTRTCSDK->enterRoom(params);
}
...
void TRTCMainViewController::onError(TXLiteAVError errCode, const char* errMsg, void* arg)
{
    if(errCode == ERR_ROOM_ENTER_FAIL)
    {
        //todo 进房失败
        ...
    }
}
...
void TRTCMainViewController::onEnterRoom(uint64_t elapsed)
{
	//todo 进房成功
    ...
}
```



## 打开本地摄像头画面

调用`startLocalPreview`打开本地的摄像头并预览视频画面。

- 启动本地预览前，调用`setLocalViewFillMode`设指定你想要的视频显示模式`Fill`和 `Fit` 模式。两种模式下视频尺寸都是等比缩放，区别在于：
  - `Fill` 模式：优先保证视窗被填满。如果缩放后的视频尺寸与显示视窗尺寸不一致，多出的视频将被截掉。
  - `Fit`   模式：优先保证视频内容全部显示。如果缩放后的视频尺寸与显示视窗尺寸不一致，未被填满的视窗区域将使用黑色填充。
- 调用`startLocalPreview`，参数：`rendHwnd`（渲染视频的窗口句柄，SDK 内部会动态检测窗口大小，对整个窗口进行视频渲染）。
- 在初始化SDK完成后就可以使用`startLocalPreview`。

```c++
//hwnd 渲染视频的窗口句柄，此窗口必须只用来渲染视频。
void TRTCMainViewController::previewLocalVideo(HWND hwnd)
{
    m_pTRTCSDK->setLocalViewFillMode(TRTCVideoFillMode_Fill);
    m_pTRTCSDK->startLocalPreview(hwnd);
}
```

## 本地音视频流

调用 `muteLocalVideo` 和 `muteLocalAudio` 接口可实现发布和停止发布本地音视频流。

- 发布视频流确保已经打开`startLocalPreview`本地视频预览。
- 进房成功后，SDK 内部会默认发布本地音视频流，无需额外再调用。
- 发布本地视频流调用`muteLocalVideo`，参数值为 true 或者 false。如果设置为 true 则关闭本地视频地流，反之则发布本地视频流。 
- 发布本地音频流调用`muteLocalAudio`，参数值为 true 或者 false。如果设置为 true 则关闭本地音频地流，反之则发布本地音频流。 

```c++
void TRTCMainViewController::closeLocalStream()
{
    m_pTRTCSDK->muteLocalVideo(true);
    m_pTRTCSDK->muteLocalAudio(true);
}
```

## 远端音视频流

调用`startRemoteView`方法设置本地看到的远端用户的视频视图。

- 进入房间后，当有远端用户加入本房间，SDK 会回调`onUserEnter`方法，参数：`userId`（加入房间的用户ID）。
- 订阅远端用户流前，调用`setRemoteViewFillMode`设指定你想要的视频显示模式`Fill`和`Fit`模式。两种模式下视频尺寸都是等比缩放，区别在于：
  - `Fill` 模式：优先保证视窗被填满。如果缩放后的视频尺寸与显示视窗尺寸不一致，多出的视频将被截掉。
  - `Fit`   模式：优先保证视频内容全部显示。如果缩放后的视频尺寸与显示视窗尺寸不一致，未被填满的视窗区域将使用黑色填充。
- 收到 SDK 回调`onUserEnter`方法后，调用`startRemoteView`方法来订阅远端用户视频。
- 收到 SDK 回调`onUserExit`方法后，调用`stopRemoteView`停止订阅远端用户流。

```c++
 HWND remoteVideoRendHwnd = ...//指定你需要渲染窗口的句柄。
...
void TRTCMainViewController::onUserEnter(const char * userId)
{
    m_pTRTCSDK->setRemoteViewFillMode(TRTCVideoFillMode_Fill);
    m_pTRTCSDK->startRemoteView(userId， remoteVideoRendHwnd);
}

void TRTCMainViewController::onUserExit(const char* userId, int reason)
{
    m_pTRTCSDK->stopRemoteView(userId);
}

```

## 退出房间

调用`exitRoom`方法退出房间。不论当前是否还在通话中，调用该方法会把视频通话相关的所有资源释放掉。`exitRoom` 并不会直接让用户离开频道。

- `exitRoom` 并不会直接让用户离开频道， SDK 回调 `onExitRoom` 方法后才真正完成释放资源。

```c++
void TRTCMainViewController::exitRoom()
{
    m_pTRTCSDK->exitRoom();
}
....
void TRTCMainViewController::onExitRoom(int reason)
{
	//退房成功，reason参数保留，暂未使用。
    ...
}
```
