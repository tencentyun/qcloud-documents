本文将指导您的客户端在创建或加入房间前进行预览。

### 效果图
![](https://main.qcloudimg.com/raw/07f03c92cd06ad39668a78e4d0542d4d.png)

### 源码下载
在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。
[Demo 代码下载](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/Android/Demo_Preview.rar)

### 相关概念
- **本地采集模式**
指 SDK 定义的 Camera 的预览模式。我们知道，出于安全考虑，在设计 Android 的时候规定，如果需要调用 Camera，必须为其制显示在屏幕上的 SurfaceView 预览，否则将无法使用 Camera。设置参考 [setCaptureMode](#setCaptureMode)

|常量|模式名称|描述|
|--|--|--|
| ILiveConstants.CAPTURE_MODE_AUTO|自适应模式|使用自适应(Android 7.0 以上采用 SurfaceTexture 预览)|
| ILiveConstants.CAPTURE_MODE_SURFACETEXTURE|无悬浮窗模式|采用 SurfaceTexture 预览(无需悬浮窗权限)|
| ILiveConstants.CAPTURE_MODE_SURFACEVIEW|悬浮窗模式|采用 SurfaceView(需要悬浮窗权限)|

示例:
```
// 设置无悬浮窗模式(登录前调用有效)
ILiveSDK.getInstance().setCaptureMode(ILiveConstants.CAPTURE_MODE_SURFACETEXTURE);
```
>悬浮窗模式为官方方案，但鉴于添加悬浮窗权限申请在高版本系统中较为麻烦，推荐是使用自动模式。


### 流程图
![](https://main.qcloudimg.com/raw/03860af94f0b873df0c707e3ec7ce972.png)

### 具体实现
#### 设置渲染控件
```
ILiveRoomManager.getInstance().initAvRootView(arvRoot);
```
#### 打开摄像头
- 如果是使用 **无悬浮窗模式**，可以直接打开:
```
ILiveRoomManager.getInstance().enableCamera(ILiveConstants.FRONT_CAMERA, true);
```
- 如果是使用 **悬浮窗模式**，需确认悬浮窗已创建成功:
```
if (ILiveRoomManager.getInstance().isSurfaceViewCreated()) {
    // 悬浮窗已创建，直接打开
    ILiveRoomManager.getInstance().enableCamera(ILiveConstants.FRONT_CAMERA, true);
}else{
    // 悬浮窗尚未创建成功，等悬浮窗创建成功后再打开
    arvRoot.setSurfaceCreateListener(new AVRootView.onSurfaceCreatedListener() {
        @Override
        public void onSurfaceCreated() {
            ILiveRoomManager.getInstance().enableCamera(ILiveConstants.FRONT_CAMERA, true);
        }
    });
}
```

#### 渲染本地视频画面
由于渲染视频的 AVVideoView 并不是创建时直接创建的，需要等创建成功再开始渲染:
```
arvRoot.setSubCreatedListener(new AVRootView.onSubViewCreatedListener() {
    @Override
    public void onSubViewCreated() {
        arvRoot.renderVideoView(true, ILiveLoginManager.getInstance().getMyUserId(), CommonConstants.Const_VideoType_Camera, true);
    }
});
```
### API说明
#### setCaptureMode
属于 ILiveSDK 的方法，用于设置 Camera 的预览模式，参数说明:

|名称|类型|描述|
|--|--|--|
|CaptureMode|int|Camera的预览模式,参考[预览模式](#相关概念)|
