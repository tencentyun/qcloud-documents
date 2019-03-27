本文将指导您如何将主播的屏幕内容以视频的方式分享给观众观看
### 效果图
下图中，主播开启屏幕分享，观众端将看到主播的摄像头画面（主流）和屏幕画面（辅流，PS:主播在玩王者）。
![](https://main.qcloudimg.com/raw/b8df44614821adc2b43a72bb7a9361e3.png)

### 源码下载
在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。
[Demo 代码下载](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/Android/Demo_ScreenShared.rar)

### 相关概念
**视频数据类型**
 腾讯云支持一个帐号同时上行一路主流和一路辅流，这里用于区分视频流的来源称为视频类型，目前支持的视频类型有： 摄像头，屏幕分享，播片（PC端产生）。

|常量|视频类型|流类型|描述|
|--|--|--|--|
|CommonConstants.Const_VideoType_Camera|摄像头|主流|通过摄像头采集数据产生|
|CommonConstants.Const_VideoType_Screen|屏幕分享|辅流|通过分享屏幕产生|
|CommonConstants.Const_VideoType_File|播片|辅流|通过播放视频文件产生|

### 流程图
![](https://main.qcloudimg.com/raw/9689580d2f0a701d490f36c2603f97a4.png)

### 具体实现
#### 开启直播
创建房间，开启直播可参考（[创建房间](https://cloud.tencent.com/document/product/647/16806)）

#### 开启屏幕录制，分享屏幕
用户在创建房间成功后，调用屏幕录制接口，开启屏幕分享:
```Java
    /**
     * @param mode   质量模式
     * @param vertical 是否竖屏
     * @param callBack 回调
     */
ILiveRoomManager.getInstance().enableScreen(int mode, boolean vertical, ILiveCallBack callBack)
```

**参数说明：**
int mode：屏幕录制时的分辨率。目前屏幕分享有三种质量模式，可参考 `com.tencent.ilivesdk.adapter.CommonConstants` 中常量：
```Java
/** 超清（1280*720） */
public static int Const_Screen_Super_HD = AVVideoCtrl.SCREEN_SUPER_DEFINITION;
/** 高清(960*540) */
public static int Const_Screen_HD = AVVideoCtrl.SCREEN_HIGH_DEFINITION;
/** 标清(864*480) */
public static int Const_Screen_SD = AVVideoCtrl.SCREEN_STANDARD_DEFINITION;
```

boolean vertical：屏幕录制的旋转模式，true 为竖屏，false 为横屏

ILiveCallBack callBack：开启屏幕分享的结果回调，可处理成功或失败操作


#### 录屏权限获取
开启屏幕录制时需动态获取 Android 系统的屏幕录取权限，如下图所示。单击【立即开始】即可（勾选"不再显示"可永久授权，后续开启屏幕分享将无需再申请权限）。
![](https://main.qcloudimg.com/raw/1ebe38771d7dc85939533d5848eebed6.png)

至此开启屏幕分享相关操作完成了，如果开启成功，此时主播用户的上行有两路流，一路摄像头采集的主流，另一路为屏幕分享的辅流。观众端看到的直播画面将如此前的效果图所示，有两个画面
>注：上面相关代码及操作都为主播端的行为，观众端无需做任何处理。

#### 停止屏幕分享
如主播用户退出房间或想主动关闭屏幕分享，调用停止屏幕分享接口即可
```Java
    /**
     * @param callBack 回调
     */
ILiveRoomManager.getInstance().disableScreen(ILiveCallBack callBack);
```

## 常见问题
调用屏幕分享接口失败?
> 屏幕录制是 Android 5.0 之后提供的新接口，故需用户的 Android 系统高于 5.0，开发人员需在代码逻辑中对此做判断。
