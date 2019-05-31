本文将指导您将如何创建一个房间，获取直播画面并在合适的时候退出房间。
## 源码下载
在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。
[Demo 代码下载](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/MAC_TRTC.zip)

## 相关概念
 - [房间](https://cloud.tencent.com/document/product/647/16792#.E6.88.BF.E9.97.B4)
 - [privateMapKey](https://cloud.tencent.com/document/product/647/17230#privatemapkey)
 - [角色配置](https://cloud.tencent.com/document/product/647/16792#.E8.A7.92.E8.89.B2.E9.85.8D.E7.BD.AE)
 - 渲染控件
 在拿到视频数据时，我们需要一个展示数据的地方，这个就是渲染控件。
 - 视频数据类型
 腾讯云支持一个帐号同时上行一路主流和一路辅流，这里用于区分视频流的来源称为视频类型，目前支持的视频类型有： 摄像头，屏幕分享，播片（PC 端产生）。

|视频类型|流类型|描述|
|--|--|--|
|摄像头|主流|通过摄像头采集数据产生|
|屏幕分享|辅流|通过分享屏幕产生|
|播片|辅流|通过播放视频文件产生|

## 操作步骤
### 创建房间
创建房间的方法在 `ILiveRoomManager.h` 中，该方法需要传入两个重要参数，房间 ID（roomId）和房间配置对象（option）：
* 房间 ID 可以搭建一个界面（如 demo 中）让用户输入，也可在代码中 hard code 用于测试，但是 roomID 需要符合前面预备知识中介绍的规则。
    
* 配置对象需要您创建，ILiveRoomOption 是用来对您准备创建的这个房间的音视频，即时通讯等功能进行配置的类，这里我们可以使用默认配置 defaultHostLiveOption。

最后，创建房间的结果会以回调 Block 的方式返回，您可以根据自己的业务逻辑，在成功或者失败回调中做相应的处理。

```objc
> TCLiveRoomWC.m
// 导入头文件
#import <ILiveSDK/ILiveCoreHeader.h>

// 创建房间
- (void)enterRoom{
    //step3 房间配置
    ILiveRoomOption *option = [ILiveRoomOption defaultHostLiveOption];
    option.imOption.imSupport = YES;
    // 设置房间内音视频监听
    option.memberStatusListener = self;
    // 设置房间中断事件监听
    option.roomDisconnectListener = self;
    option.firstFrameListener = self;
    // 该参数代表进房之后使用什么规格音视频参数，参数具体值为客户在腾讯云实时音视频控制台画面设定中配置的角色名（例如：默认角色名为user, 可设置controlRole = @"user"）
    option.controlRole = self.role;

    //step4 调用创建房间接口，传入房间ID和房间配置对象
    [[ILiveRoomManager getInstance] createRoom:[self.roomID intValue] option:option succ:^{
        NSLog(@"-----> create room succ");
    } failed:^(NSString *module, int errId, NSString *errMsg) {
        NSLog(@"-----> create room fail,%@ %d %@",module, errId, errMsg);
    }];

}
```

用户进入房间后，会自动打开摄像头和麦克风并自动推流（这个是在创建房间时传入的 `ILiveRoomOption` 配置对象中设置）。在直播房间中，所有的音视频事件都是通过音视频事件回调来通知监听对象，所以需要先设置监听对象option.memberStatusListener = self;。


### 监听房间内事件
创建房间时，我们在配置对象中设置了房间音视频事件监听和房间中断事件监听，用来监听房间内的事件。
音视频事件监听对象遵守`ILiveMemStatusListener`协议，并实现以下方法：

```objc
@protocol ILiveMemStatusListener <NSObject>
/**
 房间成员状态变化通知的函数，房间成员发生状态变化(如是否发音频、是否发视频等)时，会通过该函数通知业务侧。

 @param event     状态变化id，详见QAVUpdateEvent的定义
 @param endpoints 发生状态变化的成员id列表。

 @return YES 执行成功
 */
- (BOOL)onEndpointsUpdateInfo:(QAVUpdateEvent)event updateList:(NSArray *)endpoints;
@end
```

>**说明：**
>该方法即为房间音视频事件回调方法，只要房间内有人开关摄像头、麦克风等，SDK 底层就会回调该方法，通知监听者，该方法有 event 和 endpoints 两个参数。
> - event 是一个事件枚举值，定义了房间内成员可能发生的事件类型，包括成员进出房间，开关摄像头、麦克风等。
>
> - endpoints 是一个数组，里面装的是 QAVEndpoint 对象，代表每一个发送事件的用户，该方法的作用即通知哪些用户发生了哪种类型的音视频改变，在监听到事件发生时，通常需要再界面上做出一些调整，比如，监听到某用户打开了摄像头，应该添加一个渲染图到界面上，将该用户的画面渲染出来。


event 有以下一些取值：

```objc
typedef NS_ENUM(NSInteger, QAVUpdateEvent) {
    QAV_EVENT_ID_NONE                      = 0, ///< 默认值，无意义。
    QAV_EVENT_ID_ENDPOINT_ENTER            = 1, ///< 进入房间事件。
    QAV_EVENT_ID_ENDPOINT_EXIT             = 2, ///< 退出房间事件。
    QAV_EVENT_ID_ENDPOINT_HAS_CAMERA_VIDEO = 3, ///< 有发摄像头视频事件。
    QAV_EVENT_ID_ENDPOINT_NO_CAMERA_VIDEO  = 4, ///< 无发摄像头视频事件。
    QAV_EVENT_ID_ENDPOINT_HAS_AUDIO        = 5, ///< 有发语音事件。
    QAV_EVENT_ID_ENDPOINT_NO_AUDIO         = 6, ///< 无发语音事件。
    QAV_EVENT_ID_ENDPOINT_HAS_SCREEN_VIDEO = 7, ///< 有发屏幕视频事件。
    QAV_EVENT_ID_ENDPOINT_NO_SCREEN_VIDEO  = 8, ///< 无发屏幕视频事件。
    QAV_EVENT_ID_ENDPOINT_HAS_MEDIA_FILE_VIDEO = 9, ///< 有发文件视频事件。
    QAV_EVENT_ID_ENDPOINT_NO_MEDIA_FILE_VIDEO  = 10, ///< 无发文件视频事件。
};
```
可以看到，前面提到的 "视频数据类型" 在事件中都有定义。
接着您要做的就是设置监听对象，然后在代理方法中监听摄像头开启的事件QAV_EVENT_ID_ENDPOINT_HAS_CAMERA_VIDEO，并将该用户的渲染画面添加到界面上。

```objc
// 导入头文件
#import <ILiveSDK/ILiveCoreHeader.h>

// 音视频事件回调
- (BOOL)onEndpointsUpdateInfo:(QAVUpdateEvent)event updateList:(NSArray *)endpoints {
    switch (event) {
        case QAV_EVENT_ID_ENDPOINT_HAS_CAMERA_VIDEO:
            {
                /*
                 创建并添加渲染视图，传入userID和渲染画面类型，这里传入 QAVVIDEO_SRC_TYPE_CAMERA（摄像头画面）
                 */
                ILiveFrameDispatcher *frameDispatcher = [[ILiveRoomManager getInstance] getFrameDispatcher];
                ILiveRenderViewForMac  *renderView = [frameDispatcher addRenderAt:CGRectMake(0,  0, self.videoLayoutView.frame.size.width, self.videoLayoutView.frame.size.height - 20) forIdentifier:endoption.identifier srcType:QAVVIDEO_SRC_TYPE_CAMERA];
                renderView.identifier = endoption.identifier;
                [self.window.contentView addSubview:renderView];
            }
            break;
    }
    return YES;
}
```

如果一切顺利，在创建房间成跳转到直播页面时，您就能看到直播画面了。

> 由于本文目的是创建直播间和获取画面，所以这里对音视频事件回调的处理比较简单，但也是最基本的，在后续文档中还会介绍该方法使用，您可以根据自己需求监听不同的事件，例如，监听成员进出房间事件，在界面上显示成员进出的通知。

房间中断事件监听遵守`ILiveRoomDisconnectListener`协议，并实现以下方法：

```objc

/**
 SDK主动退出房间提示。该回调方法表示SDK内部主动退出了房间。SDK内部会因为30s心跳包超时等原因主动退出房间，APP需要监听此退出房间事件并对该事件进行相应处理

 @param reason 退出房间的原因，具体值见返回码

 @return YES 执行成功
 */
- (BOOL)onRoomDisconnect:(int)reason;
```

该方法为SDK内部主动退出房间的回调，开发者可以根据自己的业务需求，在方法中进行相应处理。

### 退出房间
调用 ILiveSDk 的退出房间接口。
接口选择在关闭窗口时执行。


```objc
//关闭窗口退出房间
-(void)windowWillClose:(NSNotification *)notification{
    [[ILiveRoomManager getInstance] quitRoom:^{
        NSLog(@"-----> quit room succ");
    } failed:^(NSString *module, int errId, NSString *errMsg) {
        NSLog(@"-----> quit room fail,%@ %d %@",module, errId, errMsg);
    }];
}
```
退出房间成功之后，房间内资源将被回收，包括 roomID，我们可以以一个相同的 roomID 再创建一个新的房间。

## 常见问题
#### 进房失败，提示没有权限
确认正确配置了进房票据privateMapKey
> 新接入用户进房票据为必填字段，老用户(不使用进房票据)需在初始化时配置
```
[[ILiveSDK getInstance] setChannelMode:E_ChannelIMSDK withHost:@""];
```

#### 失败回调，错误码 1003 或 8011
1. 进房/退房为线性互斥操作，若请求太频繁，sdk 便会上抛 8011，这种情况需要上次操作完成(回调上抛)再继续操作(进出房间)
2. 用户一次只能加入一个房间，所以若上次房间未退出，再次调用创建(或加入)便会上抛 1003，这种情况需要先退出上次房间
