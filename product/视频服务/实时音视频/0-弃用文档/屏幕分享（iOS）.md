本文将指导您如何将主播的屏幕内容以视频的方式分享给观众观看。
### 效果图
效果图中，主播（右侧手机）开启屏幕分享，观众端（左侧手机）将看到主播的拖动黄块画面。
![](https://main.qcloudimg.com/raw/570051276c21297d4556d4044f197d97.gif)

### 提前准备
1. **屏幕分享功能只支持 iOS9，iOS10 系统**；
2. 如果需要集成录屏功能，请提前发送 App 的 `Bundle identifier` 给到腾讯云(走工单流程)，我们会为您分配与 `Bundle identifier` 相对应的 `appid`（屏幕录制插件中需要，必需）；


### 源码下载
1. 在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。 [Demo 代码下载](	http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/iOS/SreenRecord_Demo.zip)
2. 下载完成并解压后，命令行到`Frameworks`目录下，运行`LoadSDK.sh`，即可下载所有依赖的SDK，其中包括录屏插件`QAVScreenRecorkKit.framework`。

### SDK 集成
1. 录屏插件`QAVScreenRecordKit.framework`是动态库（下载 demo 源码后在工程目录下可以找到），需要用以下方式添加到工程：`TARGETS` --> `General` --> `Embedded Binaries`。
![](https://main.qcloudimg.com/raw/3dffb25a3400b2a1ae690c59a3ef263e.png)

2. 如果需要在程序退后台后，能继续进行录屏，需要开启后台模式：`TARGETS` --> `Capabilities` --> `Background Modes`
![](https://main.qcloudimg.com/raw/3b749f3ba5dfcc09bf4c8d44cd4afba6.png)


### 相关概念
**视频数据类型**
 腾讯云支持一个帐号同时上行一路主流和一路辅流，这里用于区分视频流的来源称为视频类型，目前支持的视频类型有： 摄像头，屏幕分享，播片（PC端产生）。

|常量|视频类型|流类型|描述|
|--|--|--|--|
|QAVVIDEO_SRC_TYPE_CAMERA|摄像头|主流|通过摄像头采集数据产生|
|QAVVIDEO_SRC_TYPE_SCREEN|屏幕分享|辅流|通过分享屏幕产生|
|QAVVIDEO_SRC_TYPE_MEDIA|播片|辅流|通过播放视频文件产生|

### 流程图
![](https://main.qcloudimg.com/raw/9689580d2f0a701d490f36c2603f97a4.png)

### 具体实现

#### 开启直播
创建房间，开启直播可参考（[创建房间](https://cloud.tencent.com/document/product/647/16811)）

#### 开启屏幕分享功能

1.用户在创建房间成功后，调用`QAVVideoCtrl`接口，开启屏幕分享：

```
/*!
 @abstract      开启/关闭录屏
 @param         isEnable    YES 开启，NO 关闭。
 @param         mode                    清晰度模式，1 超清模式，2 高清模式，3 标清模式。
 @param         block                   异步返回执行结果的 (^screenOptionComplete)
 @return        QAV_OK 调用成功。只有返回QAV_OK时，才会通过block异步返回执行结果；其他情况不会回调block。
                QAV_ERR_NOT_IN_MAIN_THREAD  非主线程调用。
                QAV_ERR_CONTEXT_NOT_START   context未start。
                QAV_ERR_ROOM_NOT_EXIST      房间未创建或已销毁。
                AV_ERR_RESOURCE_IS_OCCUPIED 房间内已有人进行屏幕分享或者播放视频文件
                QAV_ERR_FAIL 其他错误
 @see           QAVResult
 */
- (QAVResult)enableScreenRecord:(BOOL)isEnable withMode:(int)mode complete:(screenOptionComplete)block;
```

**参数说明：**

* BOOL enable : YES 开启 ; NO 关闭
* int mode：屏幕录制时的分辨率。目前屏幕分享有三种质量模式，可参考`QAVScreenRecordKit.framework/QAVScreenRecord.h`中`QAVRecordPreset`枚举

```
typedef NS_ENUM(NSInteger, QAVRecordPreset) {

    QAVRecordPreset1280x720  = 1,//超清模式
    QAVRecordPreset960x540   = 2,//高清模式
    QAVRecordPreset864x480   = 3,//标清模式

};
```
* screenOptionComplete block：开启屏幕分享的结果回调，可处理成功或失败操作

**示例代码如下：**

```
[[[ILiveSDK getInstance] getAVContext].videoCtrl enableScreenRecord:YES withMode:rec complete:^(int result) {
      //  成功时，调用插件录制
 }];
```
2.开启屏幕分享功能之后，实际并未开始录制，此时需要手动去调用`QAVScreenRecordKit.framework`中的`startRecord`方法才能开始录屏，注意：**该步中插件中的`mode`需要与上一步一致**。示例代码如下：

```
// 来源于示例中的AppDelegate方法
- (void)startScreenRecord:(QAVRecordPreset)mode
{
    if (self.isScreenRecording)
    {
        return;
    }

    self.screenRecord = [QAVScreenRecord shareInstance];
    self.screenRecord.context = [[ILiveSDK getInstance] getAVContext];
    self.screenRecord.userId = [[ILiveLoginManager getInstance] getLoginId];
    self.screenRecord.appid = kRecordAppId;
    self.screenRecord.mode = mode;

    //    UIDeviceOrientationPortrait ：0
    //    UIDeviceOrientationLandscapeRight：1
    //    UIDeviceOrientationPortraitUpsideDown：2
    //    UIDeviceOrientationLandscapeLeft：3
    [self.screenRecord setRotation:0];
    [self.screenRecord setDelegate:self];
    QAVResult res = [self.screenRecord startRecord];

    self.isScreenRecording = res == QAV_OK;
}
```

#### 停止屏幕分享
如主播用户退出房间或想主动关闭屏幕分享，调用先停止屏幕分享，并调用`QAVScreenRecordKit.framework`中方法销毁即可

```
[[[ILiveSDK getInstance] getAVContext].videoCtrl enableScreenRecord:NO withMode:QAVRecordPreset1280x720 complete:^(int result) {
 	// TODO: 停止录屏
   // [app stopScreenRecord];     
   // TODO：退房
}];

// 来源于示例中的AppDelegate方法
- (void)stopScreenRecord
{
    [[QAVScreenRecord shareInstance] setDelegate:nil];//释放回调
    [[QAVScreenRecord shareInstance] stopRecord];//结束录屏
    [[QAVScreenRecord shareInstance] destroy]; //资源回收
    self.isScreenRecording = NO;
}
```

### 常见问题
- 调用屏幕分享接口失败?
> 屏幕分享功能只支持iOS9，iOS10系统。
> `kRecordAppId`与`Bundle identifier`是绑定的，请检查是否对应；
