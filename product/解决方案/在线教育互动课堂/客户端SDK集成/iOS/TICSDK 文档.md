## 1. 快速集成

`TICSDK`支持 iOS8+ 系统，支持 Cocoapods 集成，集成完之后还需进行相应的工程配置。

### Cocoapods 集成（推荐）

在 Podfile 文件中加入：

```
pod 'TICSDK'    
```

安装：

```
pod install // 由于SDK源文件较大，这步可能需要等待几分钟
```
  
如果无法安装 SDK 最新版本，运行以下命令更新本地的 CocoaPods 仓库列表。

```
pod repo update
```

### 手动集成

[下载 TICSDK](http://dldir1.qq.com/hudongzhibo/TICSDK/iOS/TICSDK.zip) ，将其拖进工程中，并添加以下依赖库：

|需添加依赖库|
|---|
|Accelerate.framework|
|AssetsLibrary.framework|
|AVFoundation.framework|
|CoreGraphics.framework|
|CoreMedia.framework|
|CoreTelephony.framework|
|CoreVideo.framework|
|ImageIO.framework|
|JavaScriptCore.framework|
|OpenAL.framework|
|OpenGLES.framework|
|QuartzCore.framework|
|SystemConfiguration.framework|
|VideoToolbox.framework|
|libbz2.tbd|
|libc++.tbd|
|libiconv.tbd|
|libicucore.tbd|
|libprotobuf.tbd|
|libresolv.tbd|
|libsqlite3.tbd|
|libz.tbd|

### 工程配置
为保障工程正常编译，需修改以下工程配置（**Cocoapods 集成方式也需要配置**）：

* 在`Build Settings` > `Other Linker Flags`里添加选项 `-ObjC`。

* 在`Build Settings`中将`Allow Non-modular includes in Framework Modules`设置为`YES`。

* 在`Build Settings`中将 `Enable Bitcode`设置为`NO`。

* 由于要用到手机的相机和麦克风，所以需要在项目的`info.plist`文件中增加`Privacy - Camera Usage Description`和`Privacy - Microphone Usage Description`两项。

* 腾讯云对象存储使用的是 HTTP 协议。为确保在 iOS 系统上可以运行，您需要开启允许通过 HTTP 传输。
您可以通过以下两种方式开启允许通过 HTTP 传输：

    - 手动设置

    在项目的`info.plist`文件中增加以下配置：
    
    ![](https://main.qcloudimg.com/raw/0204a82988bb42696b7bcbe1d47e5c8c.png)
    
    - 代码设置

    在项目的`info.plist`文件中增加以下代码：
    
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

### 集成验证
在`appdelegate.m`中导入头文件`<TICSDK/TICSDK.h>`，该头文件包含了`TICSDK`中所有公开的头文件，调用`getVersion`方法获取版本号：

```objc
#import <TICSDK/TICSDK.h>

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    NSLog(@"%@",[TICSDK getVersion]);
    return YES;
}
```
 如果集成没问题，控制台就能打印出`TICSDK`的版本号。
 
## 2. 使用详解
集成成功之后，可进一步了解 TICSDK 的使用方法，开发者可以参照该 Demo 使用TICSDK，[下载开发者 Demo](http://dldir1.qq.com/hudongzhibo/TICSDK/iOS/TICSDK_Demo.zip)。

>? 开发者 Demo 主要为开发者展示 TICSDK 的基本使用方法，简化了很多不必要的 UI 代码，使开发者更加专注于了解 TICSDK 的使用方法。

### 2.1 头文件概览

SDK 中暴露的公开头文件的主要功能：

类名 | 主要功能
--------- | ---------
TICSDK.h | SDK头文件类，包含了开发者可能用到的所有头文件，开发者集成时，只需导入该头文件即可
TICManager.h | 互动课堂管理类，互动课堂SDK对外主要接口类，提供了【初始化】、【登录/登出SDK】、【创建/加入/销毁课堂】、【添加白板】、【音视频操作】、【IM操作】等接口。
TICClassroomOption.h | 加入课堂时的课堂配置类，主要用来配置加入课堂时的角色（学生 or 老师）、是否自动开启摄像头，麦克风等，另外课堂配置对象还带有两个可选的代理对象，一个是复制监听课堂内部事件，另一个则负责监听课堂内的 IM 消息。


### 2.2 使用流程

TICSDK 使用的一般流程如下：

![](https://main.qcloudimg.com/raw/30b9189f6c8fe279750cef683e44b56f.png)


<!--```flow
st=>start: 1. 初始化【initSDK:accountType:】
op0=>operation: 2. 配置COS云存储（可选）【initCOS:】
op1=>operation: 3. 登录【loginWithUid:userSig:】
op2=>operation: 4. 创建课堂【createClassroomWithRoomID:】
op3=>operation: 5. 加入课堂（设置课堂事件代理和 IM 消息代理）【joinClassroom:option:】
op4=>subroutine: 6.1 创建并添加白板，进行白板相关操作【addBoardView:】
op5=>subroutine: 6.2 音视频相关操作
op6=>subroutine: 6.3 IM 相关操作
op7=>operation: 7. 退出课堂【quitClassroomSucc:】
e=>end: 8. 登出【logout:】


st->op0->op1->op2->op3->op4->op5->op6->op7->e

```-->
 
>? 其中【创建课堂】和【销毁课堂】为老师端特有步骤。


### 2.3 初始化 SDK
>?初始化前，需确认已开通 [实时音视频服务](https://cloud.tencent.com/document/product/647/17195)，并获取 SDKAppID。

使用`TICSDK`前，需先进行初始化。

接口 | 说明
---|---
-initSDK:| 初始化 SDK

`TICSDK`的账号体系基于`IMSDK`，支持多终端登录互踢功能（默认开启），初始化后，开发者可以设置以下回调，用来监听该账号是否被踢，当账号被踢时可以在界面上做出一些提示来提醒用户。账号被踢之后需重新登录方可正常使用TICSDK。

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
-loginWithUid:userSig:succ:failed: | 登录

该方法需要传入两个参数 uid 和 userSig，uid 为用户 ID，userSig 为腾讯云后台用来鉴权的用户签名，相当于登录 TICSDK 的用户密码，需要由开发者业务服务器生成并传给客户端，详情请参考 [生成签名](https://cloud.tencent.com/document/product/647/17275)。

> 开发调试阶段，可使用腾讯云 [实时音视频控制台](https://console.cloud.tencent.com/rav) >【开发辅助】>【签名(UserSig)生成工具】生成临时的 uid 和 userSig 用于开发测试（在控制台 >【功能配置】下载公私钥）。

### 2.5 创建课堂
登录成功之后，就可以加入课堂了，如果当前没有课堂需要先创建一个，创建课堂接口如下：

接口 | 说明
---|---
-createClassroomWithRoomID:succ:failed: | 创建课堂(老师端调用)


其中参数`roomID`由业务层自行指定（必须为正整数）。该方法会根据传进去的 roomID 创建了一个 IM 群组并进行一些准备工作。

### 2.6 加入课堂

老师端和学生端，都需要调用加入课堂接口来进入课堂：

接口 | 说明
---|---
-joinClassroomWithOption:succ:failed: | 加入的课堂

该接口需要传入一个配置 block，该 block 接收一个方法内部创建好的`TICClassroomOption`默认配置对象，开发者需在该 block 中修改自定义配置，然后将修改后的 option 返回。

为保证课堂内的逻辑正常以及触发的事件能被监听到，进房时`TICClassroomOption`的属性都是必填参数，另外还有一个父类的参数必须填写 **controlRole**。

* **controlRole**：代表进房之后使用哪些音视频参数，参数具体值为客户在 [实时音视频控制台](https://console.cloud.tencent.com/rav) > 【画面设定】中配置的角色名（例如默认角色名为 user，可设置 controlRole = @"user"）。

示例代码：

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
音视频功能封装于腾讯云实时音视频 SDK `ILiveSDK`，TICSDK 中只封装了一些常用的接口：打开/关闭摄像头、麦克风、扬声器、切换当前相机方向等，如下：

接口 | 说明
---|---
-enableCamera:enable:succ:failed: | 打开/关闭 摄像头
-switchCamera:failed: | 切换当前相机方向
-enableMic:succ:failed: | 打开/关闭 麦克风
-enableSpeaker:succ:failed: | 打开/关闭 扬声器

课堂内成员在进行打开/关闭摄像头、麦克风操作时，会触发音视频事件，如果在加入课堂前设置了课堂事件监听代理 `id<TICClassroomEventListener> eventListener`，一端进行音视频操作时，另一端就可以在课堂内音视频事件回调中得到通知：

接口 | 说明
---|---
-onUserUpdateInfo:users: | 课堂内音视频事件回调

课堂内的音视频事件都会通过该方法回调给所有人（包括操作者自己），event 表示事件类型（开关摄像头等），user 表示触发事件的用户 ID，收到回调之后，可以根据事件类型，进行相应的处理，例如收到开摄像头事件，就添加一个对应用户的渲染视图，收到关摄像头事件，就移除对应用户的渲染视图（具体用法可参考 [Demo](http://dldir1.qq.com/hudongzhibo/TICSDK/iOS/TICSDK_Demo.zip)）：

```objc
/**
 * 音视频事件回调
 */
- (void)onUserUpdateInfo:(QAVUpdateEvent)event users:(NSArray *)users {
    for (NSString *identifier in users) {
        switch (event) {
            case QAV_EVENT_ID_ENDPOINT_HAS_CAMERA_VIDEO: // 房间内有人打开了摄像头
            {
                /*
                 创建并添加渲染视图，传入userID和渲染画面类型 QAVVIDEO_SRC_TYPE_CAMERA（摄像头画面）,
                 */
                ILiveFrameDispatcher *frameDispatcher = [[ILiveRoomManager getInstance] getFrameDispatcher];
                ILiveRenderView *renderView = [frameDispatcher addRenderAt:CGRectZero forIdentifier:identifier srcType:QAVVIDEO_SRC_TYPE_CAMERA];
                renderView.autoRotate = NO;
                if ([identifier isEqualToString:[[ILiveLoginManager getInstance] getLoginId]]) {
                    renderView.isMirror = YES;
                    renderView.rotateAngle = ILIVEROTATION_90;
                }
                [self.view addSubview:renderView];
                //                [self.view sendSubviewToBack:renderView]
                // 房间内上麦用户数量变化，重新布局渲染视图
                [self onCameraNumChange];
            }
                break;
            case QAV_EVENT_ID_ENDPOINT_NO_CAMERA_VIDEO: // 房间内有人关闭了摄像头
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

TICSDK 只是对`iLiveSDK`一些基础接口进行了封装，如果开发者需要用到`iLiveSDK`的其他高级功能，可直接调用`iLiveSDK`的接口，详情请参考 [ILiveSDK接口文档](https://cloud.tencent.com/document/product/647/16810)。

### 2.8 使用互动白板

> 使用白板前，需确认已开通 [白板服务](https://cloud.tencent.com/document/product/680/14782#2.-.E5.BC.80.E9.80.9A.E7.99.BD.E6.9D.BF.E6.9C.8D.E5.8A.A1)。

TICSDK 中只有添加一个白板视图对象的接口：

接口 | 说明
---|---
-addBoardView: | 添加白板到 TICManager

开发者使用时，只需创建一个 boardView 对象，并调用该接口将其添加到 TICManager 中，即可使用白板进行涂鸦并与各端互动了。

>!为保证数据的准确展示，各端白板视图的长宽比需保持一致，demo中为16：9。

关于白板的更多高级操作及文档功能，请参考 [TXBoardSDK 文档](/document/product/680/17890)。

### 2.9 收发消息

IM 相关的接口封装于腾讯云通信 SDK`IMSDK`，同样，TICSDK 中也只封装了一些常用接口：

接口 | 说明
---|---
-sendTextMessage:toUser:succ:failed: | 发送文本消息
-sendCustomMessage:toUser:succ:failed: | 发送自定义消息
-sendMessage:toUser:succ:failed: | 发送消息（可以发送所有类型的消息）


课堂内成员在调用以上方法发送消息时，会触发 IM 事件，如果在加入课堂前设置了 IM 事件监听代理 `id<TICClassroomIMListener> imListener;`，一端发送 IM 消息时，另一端就可以在对应的消息回调方法中得到通知。

接口 | 说明
---|---
-onRecvTextMsg:from:type: | 收到文本消息
-onRecvCustomMsg:from:type: | 收到自定义消息
-onRecvMessage: | 收到消息(所有类型的消息，自行解析)

这3个接口，分别对应了前面3个消息发送的方法，对应类型的消息会在对应类型的代理方法中回调，收到回调后可将消息展示在界面上。

TICSDK 只是对`IMSDK`一些基础接口进行了封装，如果开发者需要用到`IMSDK`的其他高级功能，可直接调用`IMSDK`的接口，详情请参考 [IMSDK接口文档](https://cloud.tencent.com/document/product/269/1566)。

### 2.10 课堂内其他事件监听

进入课堂的配置对象中的课堂事件监听代理`<TICClassroomEventListener>`还有一些其他的协议方法：

接口 | 说明
---|---
-onMemberJoin: | 有人加入课堂时的通知
-onMemberQuit: | 有人退出课堂时的通知
-onClassroomDestroy: | 课堂被解散通知

以上协议方法分别代表有人加入课堂，有人退出课堂和课堂被解散的回调，开发者可以根据自己的业务需求，对回调事件进行相应的处理，例如在收到课堂解散回调时（老师退出课堂即触发该回调），课堂内的学生端可以弹出一个提示框，提示学生课堂已经结束。


### 2.11 退出课堂

接口 | 说明
---|---
-quitClassroomSucc:failed: | 退出课堂

退出课堂方法只是退出了课堂，课堂并不会销毁。

### 2.12 销毁课堂

接口 | 说明
---|---
-destroyClassroom:succ:failed: | 销毁课堂（老师端调用）

调用销毁课堂接口才会销毁课堂，课堂被销毁后，课堂的历史消息将会被清空，课堂的`roomID`也会被回收，可再使用该`roomID`创建课堂。




