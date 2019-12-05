# 视频渲染

## 简介
iLiveSDK 将解码后的视频帧图像数据暴露给用户，用户收到视频数据后需要做渲染；iLiveSDK 1.7.1.2 开始提供渲染模块,推荐用户使用渲染模块进行视频渲染，渲染模块使用 DX 在 GPU 中渲染，降低 CPU 占用,用户只需要传入一个窗口句柄，即可在指定窗口中渲染视频；当然，用户也可以自己实现视频渲染,如下图所示,

![](https://mc.qcloudimg.com/static/img/bc921b590fe04aff6a018ebc96ff6484/1.png)


## iLiveSDK 渲染模块

### 检测支持的渲染模式

iLiveSDK 渲染模块默认使用DX加速，在极少情况( 如安全模式 )下系统不支持 DX，将会使用 GDI 渲染；目前的渲染模块，DX 模式只支持 I420 颜色格式的渲染，GDI 只支持 RGB24 的渲染;获取方式如下,

```c++
iLiveRootView* pView = iLiveCreateRootView();
E_RootViewType viewType = pView->getRootViewType(); //COLOR_FORMAT_I420\COLOR_FORMAT_RGB24
pView->destroy();
```

### 设置视频回调颜色格式

由于不同的渲染模式下，渲染模块支持的颜色格式不同，所以，需要设置 iLiveSDK 视频回调数据的颜色格式;
setVideoColorFormat() 接口可以设置视频回调颜色格式( RGB24\I420 ),设置了颜色格式后，本地及远端视频的回调将会按照指定的颜色格式回调给用户，如下所示,

```c++
E_ColorFormat fmt;  //COLOR_FORMAT_I420\COLOR_FORMAT_RGB24
GetILive()->setVideoColorFormat(fmt);
```

### 渲染器初始化及设置

要渲染视频，用户需要指定一个窗口句柄用于视频渲染，如下,

```c++
HWND hwnd; //用于视频渲染的窗口句柄
iLiveRootView* pRootView = iLiveCreateRootView();
bool bRet = pRootView->init( hwnd );
```

渲染器初始化后，需要为其指定 View，即设置要渲染视频的用户 id，及渲染画面在窗口中的位置信息等,如下,

```c++
String      userId; //要渲染视频的用户id
E_VideoSrc  type;		//要渲染视频的类型(主路摄像头、屏幕分享、文件播放);
iLiveView   view;
view.mode = VIEW_MODE_HIDDEN;	//VIEW_MODE_HIDDEN-按比例缩放,填充黑边; VIEW_MODE_FIT-拉伸画面到控件大小;
view.exclusive = true; //此view是否独占整个窗口;如果否,需要设置view的x、y、width、height、zorder等参数,详见api
pRootView->setView(userId, type, view, false);
```

在程序退出时，最好对渲染器进行释放销毁,

```c++
pRootView->uninit();
pRootView->destroy();
```

### 注册视频回调及视频渲染

在 iLiveSDK 中注册视频回调，将会受到每一帧的视频数据;在视频数据的回调中即可调用渲染模块的 doRender() 接口进行视频渲染，如渲染本地视频画面代码如下,

```c++
void OnLocalVideo(const LiveVideoFrame* frame, void* data)
{
	//这里会收到本地视频的每一帧数据,视频帧的颜色格式是上面设置的颜色格式
	m_pRootView->doRender(frame); //渲染模块会对有渲染角度的视频帧旋转渲染；
}
GetILive()->setLocalVideoCallBack(OnLocalVideo, NULL);
```

### 渲染器视频清空

在视频流断开,如关闭摄像头时，一般需要清理渲染的画面，不让其停留在最后一帧上，这时可以调用渲染器的 removeView()\removeAllView() 接口,如,

```c++
pRootView->removeAllView();
```
