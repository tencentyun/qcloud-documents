本文讲解加入房间前，如何开启本地画面的预览。

### 效果图
![](https://main.qcloudimg.com/raw/07f03c92cd06ad39668a78e4d0542d4d.png)

### 源码下载
在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。[Demo 代码下载](	http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/iOS/Demo_Preview.zip)
### 相关概念
**预览：**
加入房间前试看本地画面，称为预览。普通的视频画面需要在加入房间后才能看到，如果想在加入房间前，先试看一下本地画面，则需要用到预览功能，预览画面无上行

### 流程图
![](https://main.qcloudimg.com/raw/2f08a916a63adf60344d252aaec50f9a.png)

### 具体实现
#### 设置本地代理
1. 设置代理
```
QAVContext *context = [[ILiveSDK getInstance] getAVContext];
[context.videoCtrl setLocalVideoDelegate:self];
```
2. 代理回调中分发视频帧

<pre>
- (void)OnLocalVideoPreview:(QAVVideoFrame *)frameData
{
    frameData.userId = [[ILiveLoginManager getInstance] getLoginId];
    ILiveFrameDispatcher *dispatch = [[ILiveRoomManager getInstance] getFrameDispatcher];
    [dispatch dispatchVideoFrame:frameData];
}

</pre>

#### 设置根视图
```
[[TILLiveManager getInstance] setAVRootView:self.view];
```
#### 启动渲染模块
```
[[[ILiveRoomManager getInstance] getFrameDispatcher] startDisplay];
```
#### 设置预览参数
```
ILiveCameraPreviewOption *option = [[ILiveCameraPreviewOption alloc] init];
option.width = 1280;    //最低配置是192*114
option.height = 720;
option.fps = 20;
[[ILiveRoomManager getInstance] setCameraPreviewParam:option succ:^{
    NSLog(@"set camera param succ");
} failed:^(NSString *module, int errId, NSString *errMsg) {
    NSLog(@"set camera param fail");
}];
```
#### 开始预览
```
[[ILiveRoomManager getInstance] enableCameraPreview:CameraPosFront enable:YES succ:^{
	NSString *loginId = [[ILiveLoginManager getInstance] getLoginId];
	[[TILLiveManager getInstance] addAVRenderView:[UIScreen mainScreen].bounds foruserId:loginId srcType:QAVVIDEO_SRC_TYPE_CAMERA];
} failed:^(NSString *module, int errId, NSString *errMsg) {
	NSLog(@"enable camera fail. m=%@,errid=%d,msg=%@",module,errId,errMsg);
}];
```


## 常见问题
* 看不到预览画面: 检查是否设置了根视图，检查是否在开启预览之前，已经设置了本地代理，并分发视频帧。
* 开启预览之后，再次进入房间，不需要再打开摄像头，但需要给视频赋予上行权限，接口是`requestVideoAuth:succ:fail`。
