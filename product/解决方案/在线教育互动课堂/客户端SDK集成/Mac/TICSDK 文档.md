## 1. 快速集成 

`TICSDK_MAC`支持 macOS 10.13+ 系统，目前只支持手动集成，集成之后需进行相应的工程配置。

### 1.1 手动集成

[下载 TICSDK](	http://dldir1.qq.com/hudongzhibo/TICSDK/Mac/TICSDK_MAC.zip) ，添加至工程，并添加以下依赖库：

|需添加依赖库|
|---|
|AVFoundation.framework|
|CoreGraphics.framework|
|CoreMedia.framework|
|CoreTelephony.framework|
|SystemConfiguration.framework|
|CoreWLAN.framework|
|libc++.tbd|
|libiconv.tbd|
|libresolv.tbd|
|libsqlite3.tbd|
|libz.tbd|

### 1.2 工程配置
为保障工程正常编译，需修改以下工程配置：

* 在`Build Settings`>`Other Linker Flags`里添加选项 `-ObjC`。

* 在`Build Settings`中将`Allow Non-modular includes in Framework Modules`设置为`YES`。

* 在`Build Settings`中将 `Enable Bitcode`设置为`NO`。

* 在项目的`info.plist`文件中增加`Privacy - Camera Usage Description`和`Privacy - Microphone Usage Description`。

* 腾讯云对象存储使用 HTTP 协议，为确保在 iOS 系统上正常运行，您需开启设置允许通过 HTTP 传输。
您可通过以下两种方式开启允许通过 HTTP 传输：
    - 手动设置
    在项目的`info.plist`文件中添加以下配置：
    ![](https://main.qcloudimg.com/raw/0204a82988bb42696b7bcbe1d47e5c8c.png)
    - 代码设置
    在项目的`info.plist`文件中添加以下代码：
    ```xml
    <key>NSAppTransportSecurity</key>
    <dict>
        <key>NSExceptionDomains</key>
        <dict>
            <key>myqcloud.com</key>
            <dict>
                <key>NSIncludesSubdomains</key>
                <true/>
                <key>NSTemporaryExceptionAllowsInsecureHTTPLoads</key>
                <true/>
            </dict>
        </dict>
    </dict>
    ```

### 1.3 集成验证
在`appdelegate.m`中导入头文件`<TICSDK/TICSDK.h>`，该头文件包含了`TICSDK`中所有公开的头文件，调用`getVersion`获取版本号。
```objc
#import <TICSDK/TICSDK.h>

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    NSLog(@"%@",[TICSDK getVersion]);
    return YES;
}
```
 集成验证成功后，控制台会显示 TICSDK 的版本号。
 
## 2. 使用 TICSDK
集成成功后，可参照开发者 Demo 使用TICSDK，[下载开发者 Demo](http://dldir1.qq.com/hudongzhibo/TICSDK/Mac/TICSDK_Demo_Mac.zip)。
> 开发者 Demo 为用户提供 TICSDK 的基本使用方法，并简化了不必要的 UI 代码。

### 2.1 头文件

类名 | 主要功能
--------- | ---------
TICSDK.h | SDK 头文件类，包含了用户所需的所有头文件，用户集成时，只需导入该头文件即可。
TICManager.h | 互动课堂管理类，互动课堂 SDK 对外主要接口类，提供【初始化】、【登录/登出SDK】、【创建/加入/销毁课堂】、【添加白板】、【音视频操作】、【IM操作】等接口。
TICClassroomOption.h |课堂配置类，用于配置加入课堂时的角色（学生或老师）、是否自动开启摄像头，麦克风等，课堂配置对象支持以下两个可选的代理对象：<ul><li>监听课堂内部事件</li><li>监听课堂内的 IM 消息</li></ul>


### 2.2 使用流程
TICSDK 使用流程如下：
![](https://main.qcloudimg.com/raw/30b9189f6c8fe279750cef683e44b56f.png)
>? 【创建课堂】和【销毁课堂】仅支持老师操作。

### 2.3 初始化 SDK
初始化 SDK 前，需确认已 [开通实时音视频服务](https://cloud.tencent.com/document/product/647/17195)，并获取到 SDKAppID。

接口 | 说明
---|---
-initSDK |初始化SDK

`TICSDK`的帐号体系基于`IMSDK`，支持多终端登录互踢功能（默认开启），初始化后，用户可设置以下回调来监听该帐号是否被踢，帐号被踢时可在界面展示提示来提醒用户。帐号被踢后需重新登录方可正常使用TICSDK。

```objc
>TICMange.h

/**
 @brief 用户在线状态通知（登录之前设置）
 
 @param listener    监听者
 */
- (void)setUserStatusListener:(id<TIMUserStatusListener>)listener;
```

### 2.4 登录

接口 | 说明
---|---
-loginWithUid:userSig:succ:failed |登录

登录接口需传入两个参数，uid 和 userSig，uid 为用户 ID（即 identifier），userSig 为腾讯云后台用来鉴权的用户签名，需由用户开发者服务器生成并传给客户端，详情请参考 [生成签名](https://cloud.tencent.com/document/product/647/17275)。

> ?开发调试阶段，用户可在 [实时音视频控制台](https://console.cloud.tencent.com/rav) 选择【开发辅助】>【签名(UserSig)生成工具】生成临时 uid 和 userSig，可在控制选择【功能配置】下载公私钥。

### 2.5 创建课堂

接口 | 说明
---|---
-createClassroomWithRoomID:succ:failed: | 创建课堂（老师端调用）

其中参数`roomID`由业务层指定（必须为正整数），该接口会根据传入的 roomID 创建了一个 IM 群组。

### 2.6 加入课堂

接口 | 说明
---|---
-joinClassroomWithOption:succ:failed: | 加入课堂

该接口需传入一个配置 block，block 接收一个方法内部创建好的`TICClassroomOption`默认配置对象，用户需在 block 中修改自定义配置，并将修改后的 option 返回。

为保证课堂内的逻辑正常以及触发的事件正常监听，进入房间时`TICClassroomOption`的属性都是必填参数，其中一个父类的参数必须填写：**controlRole**。
 **controlRole** 参数为进入房间后所使用的音视频参数，参数具体值为用户在 [腾讯云实时音视频控制台](https://console.cloud.tencent.com/rav) 的【画面设定】中配置的角色名（例如默认角色名为 user, 可设置 controlRole = @"user"）。
示例代码如下：
```objc
[[TICManager sharedInstance] joinClassroomWithOption:^TICClassroomOption *(TICClassroomOption *option) {
    option.roomID = #房间号#;
    option.role = kClassroomRoleStudent;
    option.eventListener = #课堂事件监听对象#;
    option.imListener = #课堂消息监听对象#;
    option.controlRole = @“user”;
    return option;
} succ:^{
    NSLog(@"进房成功");
} failed:^(NSString *module, int errId, NSString *errMsg) {
    NSLog(@"进房失败：%d %@", errId, errMsg);
}];
```

### 2.7 使用音视频
音视频功能封装于腾讯云实时音视频 SDK `ILiveSDK`，TICSDK 中封装了打开/关闭摄像头、麦克风、扬声器、切换当前相机方向等接口。

接口 | 说明
---|---
-enableCamera:enable:succ:failed: | 打开/关闭 摄像头
-enableMic:succ:failed: | 打开/关闭 麦克风
-enableSpeaker:succ:failed: | 打开/关闭 扬声器
-setAudioMode: | 设置声音模式(听筒或扬声器)
-enableScreenShare:succ:failed: | 打开/关闭 屏幕分享
-setScreenShareRect:succ:failed: | 设置屏幕分享区域


课堂内成员在打开/关闭摄像头、麦克风等操作时，会触发音视频事件，在加入课堂前设置课堂事件监听代理 `id<TICClassroomEventListener> eventListener`后，一端进行音视频操作，另一端就可在课堂内音视频事件回调中得到通知：

接口 | 说明
---|---
-onUserUpdateInfo:users: | 课堂内音视频事件回调

课堂内的音视频事件都会通过该方法回调给所有人（包括操作者自己），event 表示事件类型（开关摄像头等），user 表示触发事件的用户 ID，收到回调后，可根据事件类型，进行相应的处理，例如收到开摄像头事件，可添加一个对应用户的渲染视图（详细操作可参考 [demo](	http://dldir1.qq.com/hudongzhibo/TICSDK/Mac/TICSDK_Demo_Mac.zip)）：

```objc
/**
 * 音视频事件回调
 */
- (void)onUserUpdateInfo:(QAVUpdateEvent)event users:(NSArray *)users {
    if (users.count <= 0) {
        return;
    }
    for (NSString *identifier in users) {
        switch (event) {
            case QAV_EVENT_ID_ENDPOINT_HAS_CAMERA_VIDEO:
            {
                /*
                 创建并添加渲染视图，传入userID和渲染画面类型，这里传入 QAVVIDEO_SRC_TYPE_CAMERA（摄像头画面）,
                 */
                ILiveFrameDispatcher *frameDispatcher = [[ILiveRoomManager getInstance] getFrameDispatcher];
                ILiveRenderView *renderView = [frameDispatcher addRenderAt:CGRectZero forIdentifier:identifier srcType:QAVVIDEO_SRC_TYPE_CAMERA];                
                [self.window.contentView addSubview:renderView];
                
                // 房间内上麦用户数量变化，重新布局渲染视图
                [self onCameraNumChange];
            }
                break;
            case QAV_EVENT_ID_ENDPOINT_NO_CAMERA_VIDEO:
            {
                // 移除渲染视图
                ILiveFrameDispatcher *frameDispatcher = [[ILiveRoomManager getInstance] getFrameDispatcher];
                ILiveRenderView *renderView = [frameDispatcher removeRenderViewFor:identifier srcType:QAVVIDEO_SRC_TYPE_CAMERA];
                [renderView removeFromSuperview];
                
                // 房间内上麦用户数量变化，重新布局渲染视图
                [self onCameraNumChange];
            }
                break;
            default:
                break;
        }
    }
}

```

TICSDK 对`iLiveSDK`的基础接口进行了封装，如开发者需使用`iLiveSDK`的高级功能，可直接调用`iLiveSDK`的接口，详情请参考 [ILiveSDK接口文档](https://cloud.tencent.com/document/product/647/16810)。


### 2.8 使用互动白板
使用白板前，需先确认已开通 [白板服务](https://cloud.tencent.com/document/product/680/14782#.E7.99.BD.E6.9D.BF.E6.9C.8D.E5.8A.A1)。

TICSDK 中只有一个添加白板视图对象的接口：

接口 | 说明
---|---
-addBoardView:andLoadHistoryData: | 添加白板到 TICManager，并拉取课堂历史数据

用户使用时创建一个 boardView 对象，并调用该接口将其添加至 TICManager，即可使用白板进行涂鸦并与各端互动。

> ?为保证数据展示的准确性，各端白板视图的长宽比需保持一致，demo中为 16：9。

关于白板的更多高级功能，请参考 [TXBoardSDK 文档](/document/product/680/17890)。

### 2.9 收发消息

IM 相关的接口封装于腾讯云通信 SDK`IMSDK`，TICSDK 仅封装一些基础接口：

接口 | 说明
---|---
-sendTextMessage:toUser:succ:failed: | 发送文本消息
-sendCustomMessage:toUser:succ:failed: | 发送自定义消息
-sendMessage:toUser:succ:failed: | 发送消息（可以发送所有类型的消息）

课堂内成员在调用以上接口发送消息时，会触发 IM 事件，在加入课堂前设置 IM 事件监听代理 `id<TICClassroomIMListener> imListener;`后，一端发送 IM 消息时，另一端就可以在对应的消息回调方法中得到通知。

接口 | 说明
---|---
-onRecvTextMsg:from:type: | 收到文本消息
-onRecvCustomMsg:from:type: | 收到自定义消息
-onRecvMessage: | 收到消息(所有类型的消息，需自行解析)

以上3个接受消息接口，分别对应前面3个消息发送接口，对应类型的消息会在对应类型的代理方法中回调，收到回调后可将消息展示在界面上。

TICSDK 只对`IMSDK`基础接口进行了封装，用户如需使用`IMSDK`的高级功能，可直接调用`IMSDK`接口，详情请参考 [IMSDK接口文档](https://cloud.tencent.com/document/product/269/1566)。

### 2.10 课堂内其他事件监听

进入课堂的配置对象中的课堂事件监听代理`TICClassroomEventListener`还可使用以下接口。

接口 | 说明
---|---
-onMemberJoin: | 有人加入课堂时的通知
-onMemberQuit: | 有人退出课堂时的通知（包括被踢出教室的情况）
-onClassroomDestroy: | 课堂被解散通知

用户可根据实际业务需求，对回调事件进行相应的处理，例如在收到课堂解散回调时（老师退出课堂即触发该回调），课堂内的学生端可弹出一个提示框，提示学生课堂已经结束。


### 2.11 退出课堂

接口 | 说明
---|---
-quitClassroomSucc:failed: | 退出课堂

退出课堂操作仅是退出，课堂并不会销毁。

### 2.12 销毁课堂

接口 | 说明
---|---
-destroyClassroom:succ:failed: | 销毁课堂（老师端调用）

调用销毁课堂接口销毁课堂，销毁后，课堂的历史消息将会被清空，课堂的`roomID`也会被回收，用户可使用该`roomID`重新创建课堂。
