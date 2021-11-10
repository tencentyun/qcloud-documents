## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | &#10003;  | &#10003;                                                            | -  | -  | -  | &#10003;  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。

## 概述

录屏功能是 iOS 10 新推出的特性，苹果在 iOS 9 的 ReplayKit 保存录屏视频的基础上，增加了视频流实时直播功能，官方介绍见 [Go Live with ReplayKit](https://developer.apple.com/videos/play/wwdc2016/601/)。iOS 11 增强为 [ReplayKit2](https://developer.apple.com/videos/play/wwdc2017/606/)，进一步提升了 Replaykit 的易用性和通用性，并且可以对整个手机实现屏幕录制，并非只是支持 ReplayKit 功能，因此录屏推流建议直接使用 iOS 11 的 ReplayKit2 屏幕录制方式。系统录屏采用的是扩展方式，扩展程序有单独的进程，iOS 系统为了保证系统流畅，给扩展程序的资源相对较少，扩展程序内存占用过大也会被 Kill 掉。腾讯云 LiteAV SDK 在原有直播的高质量、低延迟的基础上，进一步降低系统消耗，保证了扩展程序稳定。

>!本文主要介绍 iOS 11 的 ReplayKit2 录屏使用 SDK 推流的方法，涉及 SDK 的使用介绍同样适用于其它方式的自定义推流。更详细的使用说明可以参考 [Demo](https://github.com/tencentyun/MLVBSDK/tree/master/iOS/MLVB-API-Example-OC/Basic/LivePushScreen) 里 TXReplayKit_Screen 文件夹示例代码。

## 功能体验

体验 iOS 录屏可以单击安装 [腾讯云视立方 App](https://itunes.apple.com/cn/app/%E8%A7%86%E9%A2%91%E4%BA%91%E5%B7%A5%E5%85%B7%E5%8C%85/id1152295397?mt=8) 或通过扫码进行安装。
![](https://main.qcloudimg.com/raw/386c06636b522fbd0f85714acf73209b.png)
>!录屏推流功能仅11.0以上系统可体验。

## 示例代码
针对开发者的接入反馈的高频问题，腾讯云提供有更加简洁的 API-Example 工程，方便开发者可以快速的了解相关 API 的使用，欢迎使用。

| 所属平台 |                         GitHub 地址                          |
| :------: | :----------------------------------------------------------: |
|   iOS    | [Github](https://github.com/tencentyun/MLVBSDK/tree/master/iOS/MLVB-API-Example) |
| Android  | [Github](https://github.com/tencentyun/MLVBSDK/tree/master/Android/MLVB-API-Example) |

#### 使用步骤
1. 打开控制中心，长按屏幕录制按钮，选择 **视频云工具包**。
2. 打开 **视频云工具包** > **推流演示（录屏推流）**，输入推流地址或单击 **New** 自动获取推流地址，单击 **开始推流**。

![](https://main.qcloudimg.com/raw/822ccd7c5acbcbf25e8fb148a6db74d7.png)

推流设置成功后，顶部通知栏会提示推流开始，此时您可以在其它设备上看到该手机的屏幕画面。单击手机状态栏的红条，即可停止推流。

## 开发环境准备

### Xcode 准备

Xcode 9 及以上的版本，手机也必须升级至 iOS 11 以上，否则模拟器无法使用录屏特性。

### 创建直播扩展
在现有工程选择 **New** > **Target…**，选择 **Broadcast Upload Extension**，如图所示。
![](https://main.qcloudimg.com/raw/c4c0b0ee049c733640f813a318a25adb.png)
配置好 Product Name。单击 **Finish** 后可以看到，工程多了所输 Product Name 的目录，目录下有个系统自动生成的 SampleHandler 类，这个类负责录屏的相关处理。

### 导入 LiteAV SDK
直播扩展需要导入 TXLiteAVSDK.framework。扩展导入 framework 的方式和主 App 导入方式相同，SDK 的系统依赖库也没有区别。具体请参见腾讯云官网 [工程配置（iOS）](https://cloud.tencent.com/document/product/1449/56986)。


## 对接流程
[](id:step1)
### 步骤1：创建推流对象

在 SampleHandler.m 中添加下面代码：
<dx-codeblock>
::: objective objective
#import "SampleHandler.h"
#import "V2TXLivePusher.h"

static V2TXLivePusher *s_txLivePublisher;
static NSString *s_rtmpUrl;
:::
</dx-codeblock>
<dx-codeblock>
::: objective objective
 - (void)initPublisher {
         if (s_txLivePublisher) {
             [s_txLivePublisher stopPush];
    }
    s_txLivePublisher = [[V2TXLivePusher alloc] initWithLiveMode:V2TXLiveMode_RTMP];
    [s_txLivePublisher setObserver:self];
    [s_txLivePublisher startPush:s_rtmpUrl];
}
:::
</dx-codeblock>

- s_txLivePublisher 是我们用于推流的对象，因为系统录屏回调的 sampleHandler 实例有可能不只一个，因此对变量采用静态声明，确保录屏推流过程中使用的是同一个推流器。
- 实例化 s_txLivePublisher 的最佳位置是在 `-[SampleHandler broadcastStartedWithSetupInfo:]` 方法中，直播扩展启动后会回调这个函数，就可以进行推流器初始化开始推流。但在 ReplayKit2 的屏幕录制扩展启动时，回调给 s_txLivePublisher 的 setupInfo 为 nil，无法获取启动推流所需要的推流地址等信息，因此通常回调此函数时发通知给主 App，在主 App 中设置好推流地址，横竖屏清晰度等信息后再传递给扩展并通知扩展启动推流。
- 扩展与主 App 间的通信请参见 [扩展与宿主 App 之间的通信与数据传递方式](#accessory) 。

[](id:step2)
### 步骤2：横屏推流与分辨率设置

手机录屏直播提供了多个级别的分辨率可供选择。[setVideoQuality](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#a0b08436c1e14a8d7d9875fae59ac6d84) 方法用来设置分辨率及横竖屏推流，以下录屏推流分辨率与横屏推流设置示例：

```objective-c
  static BOOL s_landScape; //YES:横屏， NO:竖屏
  [s_txLivePublisher setVideoQuality:V2TXLiveVideoResolution960x540 
                      resolutionMode:s_landScape ? V2TXLiveVideoResolutionModeLandscape : V2TXLiveVideoResolutionModePortrait];
  [s_txLivePublisher startPush:s_rtmpUrl];
```

[](id:step3)
### 步骤3：发送视频
Replaykit 会将视频以回调的方式传给 `-[SampleHandler processSampleBuffer:withType]`。

```objective-c
- (void)processSampleBuffer:(CMSampleBufferRef)sampleBuffer withType:(RPSampleBufferType)sampleBufferType {
    switch (sampleBufferType) {
        case RPSampleBufferTypeVideo:
            // Handle video sample buffer
        {
                if (!CMSampleBufferIsValid(sampleBuffer))
                    return;
            //保存一帧在 startPush 时发送,防止推流启动后或切换横竖屏因无画面数据而推流不成功
                if (s_lastSampleBuffer) {
                    CFRelease(s_lastSampleBuffer);
                    s_lastSampleBuffer = NULL;
                }
                s_lastSampleBuffer = sampleBuffer;
                CFRetain(s_lastSampleBuffer);
                V2TXLiveVideoFrame *videoFrame = [V2TXLiveVideoFrame new];
                videoFrame.bufferType = V2TXLiveBufferTypePixelBuffer;
                videoFrame.pixelFormat = V2TXLivePixelFormatNV12;
                videoFrame.pixelBuffer = CMSampleBufferGetImageBuffer(sampleBuffer);
                videoFrame.rotation = V2TXLiveRotation0;
                [s_txLivePublisher sendCustomVideoFrame:videoFrame];
        }
}
```
视频 sampleBuffer 只需要调用 `-[V2TXLivePusher sendCustomVideoFrame:]` 发送即可。

系统分发视频 sampleBuffer 的频率并不固定，如果画面静止，可能很长时间才会有一帧数据过来。SDK 考虑到这种情况，内部会做补帧逻辑。
>!建议保存一帧给推流启动时使用，防止推流启动或切换横竖屏时因无新的画面数据采集发送，因为画面没有变化时系统可能会很长时间才采集一帧画面。

[](id:step4)
### 步骤4：设置 Logo 水印
**据相关政策规定，直播视频必须加上水印。**腾讯视频云目前支持两种水印设置方式：一种是在推流 SDK 进行设置，原理是在 SDK 内部进行视频编码前就给画面打上水印。另一种方式是在云端打水印，也就是云端对视频进行解析并添加水印 Logo。

这里我们特别建议您使用 SDK 添加水印，因为在云端打水印有三个明显的问题：
 - 这是一种很耗云端机器的服务，而且不是免费的，会拉高您的费用成本。
 - 在云端打水印对于推流期间切换分辨率等情况的兼容并不理想，会有很多花屏的问题发生。
 - 在云端打水印会引入额外的3s以上的视频延迟，这是转码服务所引入的。

SDK 所要求的水印图片格式为 PNG，因为 PNG 这种图片格式有透明度信息，因而能够更好地处理锯齿等问题（建议您不要在 Windows 下将 JPG 格式的图片修改后缀名就直接使用，因为专业的 PNG 图标都是需要由专业的美工设计师处理的）。

```objective-c
//设置视频水印
[s_txLivePublisher setWatermark:image x:0 y:0 scale:1];
```

[](id:step5)
### 步骤5：结束推流
结束推流 ReplayKit 会调用 `-[SampleHandler broadcastFinished]`，示例代码：

```objective-c
- (void)broadcastFinished {
    // User has requested to finish the broadcast.
    if (s_txLivePublisher) {
        [s_txLivePublisher stopPush];
        s_txLivePublisher = nil;
    }
}
```
因为用于推流的 `V2TXLivePusher`对象同一时刻只能有一个在运行，所以结束推流时要做好清理工作。


## 事件处理
###  事件监听
SDK 通过 [V2TXLivePusherObserver](http://doc.qcloudtrtc.com/group__V2TXLivePusherObserver__android.html) 代理来监听推流相关的事件通知和错误通知，详细的事件表和错误码表请参见 [错误码表](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLiveCode__android.html)。

### 错误通知
SDK 发现部分严重问题，推流无法继续

| 事件 ID                              | 数值 | 含义说明                        |
| :------------------------------------ | :---- | :------------------------------- |
| V2TXLIVE_ERROR_FAILED                | -1   | 暂未归类的通用错误。            |
| V2TXLIVE_ERROR_INVALID_PARAMETER     | -2   | 调用 API 时，传入的参数不合法。 |
| V2TXLIVE_ERROR_REFUSED               | -3   | API 调用被拒绝。                |
| V2TXLIVE_ERROR_NOT_SUPPORTED         | -4   | 当前 API 不支持调用。           |
| V2TXLIVE_ERROR_INVALID_LICENSE       | -5   | license 不合法，调用失败。      |
| V2TXLIVE_ERROR_REQUEST_TIMEOUT       | -6   | 请求服务器超时。                |
| V2TXLIVE_ERROR_SERVER_PROCESS_FAILED | -7   | 服务器无法处理您的请求。        |

### 警告事件
SDK 发现部分警告问题，但 WARNING 级别的事件都会触发一些尝试性的保护逻辑或者恢复逻辑，而且有很大概率能够恢复。

| 事件 ID                                       | 数值  | 含义说明                                                     |
| :-------------------------------------------- | :---- | :----------------------------------------------------------- |
| V2TXLIVE_WARNING_NETWORK_BUSY                 | 1101  | 网络状况不佳：上行带宽太小，上传数据受阻。                   |
| V2TXLIVE_WARNING_VIDEO_BLOCK                  | 2105  | 当前视频播放出现卡顿                                         |
| V2TXLIVE_WARNING_CAMERA_START_FAILED          | -1301 | 摄像头打开失败。                                             |
| V2TXLIVE_WARNING_CAMERA_OCCUPIED              | -1316 | 摄像头正在被占用中，可尝试打开其他摄像头。                   |
| V2TXLIVE_WARNING_CAMERA_NO_PERMISSION         | -1314 | 摄像头设备未授权，通常在移动设备出现，可能是权限被用户拒绝了。 |
| V2TXLIVE_WARNING_MICROPHONE_START_FAILED      | -1302 | 麦克风打开失败。                                             |
| V2TXLIVE_WARNING_MICROPHONE_OCCUPIED          | -1319 | 麦克风正在被占用中，例如移动设备正在通话时，打开麦克风会失败。 |
| V2TXLIVE_WARNING_MICROPHONE_NO_PERMISSION     | -1317 | 麦克风设备未授权，通常在移动设备出现，可能是权限被用户拒绝了。 |
| V2TXLIVE_WARNING_SCREEN_CAPTURE_NOT_SUPPORTED | -1309 | 当前系统不支持屏幕分享。                                     |
| V2TXLIVE_WARNING_SCREEN_CAPTURE_START_FAILED  | -1308 | 开始录屏失败，如果在移动设备出现，可能是权限被用户拒绝了。   |
| V2TXLIVE_WARNING_SCREEN_CAPTURE_INTERRUPTED   | -7001 | 录屏被系统中断。                                             |


[](id:accessory)
### 附: 扩展与宿主 App 之间的通信与数据传递方式参考
ReplayKit2 录屏只唤起 upload 直播扩展，直播扩展不能进行 UI 操作，也不适于做复杂的业务逻辑，因此通常宿主 App 负责鉴权及其它业务逻辑，直播扩展只负责进行屏幕的音画采集与推流发送，扩展就经常需要与宿主 App 之间进行数据传递与通信。

#### 1. 发本地通知
扩展的状态需要反馈给用户，有时宿主 App 并未启动，此时可通过发送本地通知的方式进行状态反馈给用户与激活宿主 App 进行逻辑交互，如在直播扩展启动时通知宿主 App：
<dx-codeblock>
::: code 
- (void)broadcastStartedWithSetupInfo:(NSDictionary<NSString *,NSObject *> *)setupInfo {
    [self sendLocalNotificationToHostAppWithTitle:@"腾讯云录屏推流" msg:@"录屏已开始，请从这里单击回到Demo->录屏幕推流->设置推流URL与横竖屏和清晰度" userInfo:@{kReplayKit2UploadingKey: kReplayKit2Uploading}];
    }

- (void)sendLocalNotificationToHostAppWithTitle:(NSString*)title msg:(NSString*)msg userInfo:(NSDictionary*)userInfo
{
    UNUserNotificationCenter* center = [UNUserNotificationCenter currentNotificationCenter];
  
    UNMutableNotificationContent* content = [[UNMutableNotificationContent alloc] init];
    content.title = [NSString localizedUserNotificationStringForKey:title arguments:nil];
    content.body = [NSString localizedUserNotificationStringForKey:msg  arguments:nil];
    content.sound = [UNNotificationSound defaultSound];
    content.userInfo = userInfo;
  
    // 在设定时间后推送本地推送
    UNTimeIntervalNotificationTrigger* trigger = [UNTimeIntervalNotificationTrigger
                                                  triggerWithTimeInterval:0.1f repeats:NO];
  
    UNNotificationRequest* request = [UNNotificationRequest requestWithIdentifier:@"ReplayKit2Demo"
                                                                          content:content trigger:trigger];
  
    //添加推送成功后的处理！
    [center addNotificationRequest:request withCompletionHandler:^(NSError * _Nullable error) {
        
    }];
}
:::
</dx-codeblock>

通过此通知可以提示用户回到主 App 设置推流信息、启动推流等。

#### 2. 进程间的通知 CFNotificationCenter
扩展与宿主 App 之间还经常需要实时的交互处理，本地通知需要用户点击横幅才能触发代码处理，因此不能通过本地通知的方式。而 NSNotificationCenter 不能跨进程，因此可以利用 CFNotificationCenter 在宿主 App 与扩展之前通知发送，但此通知不能通过其中的 userInfo 字段进行数据传递，需要通过配置 App Group 方式使用 NSUserDefault 进行数据传递（也可以使用剪贴板，但剪贴板有时不能实时在进程间获取数据，需要加些延迟规避），如主 App 在获取好推流 URL 等后，通知扩展可以进行推流时，可通过 CFNotificationCenter 进行通知发送直播扩展开始推流：
<dx-codeblock>
::: code 
CFNotificationCenterPostNotification(CFNotificationCenterGetDarwinNotifyCenter(),
                                    kDarvinNotificationNamePushStart,
                                    NULL,
                                    nil,
                                    YES);
:::
</dx-codeblock>
扩展中可通过监听此开始推流通知，由于此通知是在 CF 层，需要通过 NSNotificationCenter 发送到 Cocoa 类层方便处理：
<dx-codeblock>
::: code 
CFNotificationCenterAddObserver(CFNotificationCenterGetDarwinNotifyCenter(),
                                    (__bridge const void *)(self),
                                    onDarwinReplayKit2PushStart,
                                    kDarvinNotificationNamePushStart,
                                    NULL,
                                    CFNotificationSuspensionBehaviorDeliverImmediately);
                                                                        
[[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(handleReplayKit2PushStartNotification:) name:@"Cocoa_ReplayKit2_Push_Start" object:nil];


static void onDarwinReplayKit2PushStart(CFNotificationCenterRef center,
                                        void *observer, CFStringRef name,
                                        const void *object, CFDictionaryRef
                                        userInfo)
{
    //转到 cocoa 层框架处理
    [[NSNotificationCenter defaultCenter] postNotificationName:@"Cocoa_ReplayKit2_Push_Start" object:nil];
}

- (void)handleReplayKit2PushStartNotification:(NSNotification*)noti
{
    //通过  NSUserDefault 或剪贴板拿到宿主要传递的数据
    //  NSUserDefaults *defaults = [[NSUserDefaults alloc] initWithSuiteName:kReplayKit2AppGroupId];
  
    UIPasteboard* pb = [UIPasteboard generalPasteboard];
    NSDictionary* defaults = [self jsonData2Dictionary:pb.string];
  
    s_rtmpUrl = [defaults objectForKey:kReplayKit2PushUrlKey];
    s_resolution = [defaults objectForKey:kReplayKit2ResolutionKey];
    if (s_resolution.length < 1) {
        s_resolution = kResolutionHD;
    }
    NSString* rotate = [defaults objectForKey:kReplayKit2RotateKey];
    if ([rotate isEqualToString:kReplayKit2Portrait]) {
        s_landScape = NO;
    }
    else {
        s_landScape = YES;
    }
    [self start];
}
:::
</dx-codeblock>

## 常见问题
ReplayKit2 屏幕录制在 iOS 11 新推出功能，相关的官方文档比较少，且存在着一些问题，使得每个版本的系统都在不断修复完善中。以下是一些使用中的常见现象或问题：

1. **屏幕录制何时自动会停止？**
系统在锁屏或有电话打入时，会自动停止屏幕录制，此时 SampleHandler 里的 broadcastFinished 函数会被调用，可在此函数发通知提示用户。

2. **采集推流过程中有时屏幕录制会自动停止问题？**
通常是因为设置的推流分辨率过高时在做横竖屏切换过程中容易出现。ReplayKit2 的直播扩展目前是有50M的内存使用限制，超过此限制系统会直接杀死扩展进程，因此 ReplayKit2 上建议推流分辨率不高于720P。

3. **iPhoneX 手机的兼容性与画面变形问题？**
iPhoneX 手机因为有刘海，屏幕采集的画面分辨率不是 9:16。如果设了推流输出分辨率为 9:16 的比例，如高清里是为 960 × 540 的分辨率，这时因为源分辨率不是 9:16 的，推出去的画面就会稍有变形。建议设置分辨率时根据屏幕分辨率比例来设置，拉流端用 AspectFit 显示模式 iPhoneX 的屏幕采集推流会有黑边是正常现象，AspectFill 看画面会不全。
