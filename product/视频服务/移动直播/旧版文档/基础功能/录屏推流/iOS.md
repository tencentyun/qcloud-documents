
## 概述

录屏功能是 iOS 10 新推出的特性，苹果在 iOS 9 的 ReplayKit 保存录屏视频的基础上，增加了视频流实时直播功能。iOS 11 增强为 [ReplayKit2](https://developer.apple.com/videos/play/wwdc2017/606/)，进一步提升了 Replaykit 的易用性和通用性，并且可以对整个手机实现屏幕录制，并非只是支持 ReplayKit 功能，因此录屏推流建议直接使用 iOS 11 的 ReplayKit2 屏幕录制方式。系统录屏采用的是扩展方式，扩展程序有单独的进程，iOS 系统为了保证系统流畅，给扩展程序的资源相对较少，扩展程序内存占用过大也会被 Kill 掉。腾讯云 LiteAV SDK 在原有直播的高质量、低延迟的基础上，进一步降低系统消耗，保证了扩展程序稳定。

>!本文主要介绍 iOS 11 的 ReplayKit2 录屏使用 SDK 推流的方法，涉及 SDK 的使用介绍同样适用于其它方式的自定义推流。更详细的使用可参考 [Demo](https://github.com/tencentyun/MLVBSDK/tree/master/iOS/Demo) 里 ReplaykitUpload 文件夹的示例代码。

## 功能体验

体验 iOS 录屏可以单击安装 [视频云工具包](https://itunes.apple.com/cn/app/%E8%A7%86%E9%A2%91%E4%BA%91%E5%B7%A5%E5%85%B7%E5%8C%85/id1152295397?mt=8) 或通过扫码进行安装。
![](https://main.qcloudimg.com/raw/386c06636b522fbd0f85714acf73209b.png)
>!录屏推流功能仅11.0以上系统可体验。

使用步骤：
1. 打开控制中心，长按屏幕录制按钮，选择【视频云工具包】。
2. 打开【视频云工具包】>【推流演示（录屏推流）】，输入推流地址或单击【New】自动获取推流地址，单击【开始推流】。

![](https://main.qcloudimg.com/raw/822ccd7c5acbcbf25e8fb148a6db74d7.png)

推流设置成功后，顶部通知栏会提示推流开始，此时您可以在其它设备上看到该手机的屏幕画面。单击手机状态栏的红条，即可停止推流。

## 开发环境准备

### Xcode 准备

Xcode 9 及以上的版本，手机也必须升级至 iOS 11 以上，否则模拟器无法使用录屏特性。

### 创建直播扩展

在现有工程选择【New】>【Target…】，选择【Broadcast Upload Extension】，如图所示。
![](https://main.qcloudimg.com/raw/c4c0b0ee049c733640f813a318a25adb.png)
配置好 Product Name。单击【Finish】后可以看到，工程多了所输 Product Name 的目录，目录下有个系统自动生成的 SampleHandler 类，这个类负责录屏的相关处理。

### 导入 LiteAV SDK

直播扩展需要导入 TXLiteAVSDK.framework。扩展导入 framework 的方式和主 App 导入方式相同，SDK 的系统依赖库也没有区别。具体可参见腾讯云官网 [工程配置（iOS）](https://cloud.tencent.com/document/product/454/7876)。



## 对接流程

### 步骤 1：创建推流对象

在 SampleHandler.m 中添加下面代码

```objective-c
#import "SampleHandler.h"
#import "TXRTMPSDK/TXLiveSDKTypeDef.h"
#import "TXRTMPSDK/TXLivePush.h"
#import "TXRTMPSDK/TXLiveBase.h"

static TXLivePush *s_txLivePublisher;
static NSString *s_rtmpUrl;
```

```objective-c
 - (void)initPublisher {
     if (s_txLivePublisher) {
        [s_txLivePublisher stopPush];
    }
    TXLivePushConfig* config = [[TXLivePushConfig alloc] init];
    config.customModeType |= CUSTOM_MODE_VIDEO_CAPTURE; //自定义视频模式
    config.enableAutoBitrate = YES;
    config.enableHWAcceleration = YES;
    
    config.customModeType |= CUSTOM_MODE_AUDIO_CAPTURE; //自定义音频模式
    config.audioSampleRate = AUDIO_SAMPLE_RATE_44100;   //系统录屏的音频采样率为44100
    config.audioChannels   = 1;
        
        //config.autoSampleBufferSize = YES;
        config.autoSampleBufferSize = NO;
        config.sampleBufferSize = CGSizeMake(544， 960);
    config.homeOrientation = HOME_ORIENTATION_DOWN;
    
    s_txLivePublisher = [[TXLivePush alloc] initWithConfig:config];
    s_txLivePublisher.delegate = self;
    //[s_txLivePublisher startPush:s_rtmpUrl];
}

```
- s_txLivePublisher 是我们用于推流的对象，因为系统录屏回调的 sampleHandler 实例有可能不只一个，因此对变量采用静态声明，确保录屏推流过程中使用的是同一个推流器。
- s_txLivePublisher 的 config 默认的配置为摄像头推流配置，因此需要额外配置为自定义采集视频和音频模式，视频开启 autoSampleBufferSize，SDK 会自动根据输入的分辨率设置编码器，您不需要关心推流的分辨率；如果您关闭此选项，那么代表您需要自定义分辨率。
- 因为系统录制对不同机型屏幕所得到的分辨率不一致，所以录屏推流不建议您开启 autoSampleBufferSize，使用自定义分辨率设置。
- 实例化 s_txLivePublisher 的最佳位置是在`-[SampleHandler broadcastStartedWithSetupInfo:]`方法中，直播扩展启动后会回调这个函数，就可以进行推流器初始化开始推流。但在 ReplayKit2 的屏幕录制扩展启动时，回调给 s_txLivePublisher 的 setupInfo 为  nil，无法获取启动推流所需要的推流地址等信息，因此通常回调此函数时发通知给主 App，在主 App 中设置好推流地址，横竖屏清晰度等信息后再传递给扩展并通知扩展启动推流。
- 扩展与主 App 间的通信请参见后面所附的 [扩展与宿主 App 之间的通信与数据传递方式](#accessory) 。


### 步骤 2：横屏推流与自定义分辨率

您可以指定任意一个分辨率，SDK 内部将根据您指定的分辨率进行缩放，但设置的分辨率比例应与源画面分辨率比例一致，否则会引起画面变形。`homeOrientation` 属性用来设置横竖屏推流，分辨率需要同时设置为对应的横竖屏比例。以下录屏推流常用的三种清晰度与横屏推流设置示例：

```objective-c
  static NSString* s_resolution; //SD(标清), HD(高清), FHD(超清)
  static BOOL s_landScape; //YES:横屏， NO:竖屏
    
  CGSize screenSize = [[UIScreen mainScreen] currentMode].size;
    config.autoSampleBufferSize = NO;
        config.homeOrientation = HOME_ORIENTATION_DOWN;

    if ([s_resolution isEqualToString:@"SD"]) { //标清
        config.sampleBufferSize = CGSizeMake(368, (uint)(360 * screenSize.height / screenSize.width));
        config.videoBitrateMin = 400;
        config.videoBitratePIN = 800;
        config.videoBitrateMax = 1200;
        config.videoFPS = 20;
    }
    else if ([s_resolution isEqualToString:@"FHD"]) { //超清
        config.sampleBufferSize = CGSizeMake(720, (uint)(720 * screenSize.height / screenSize.width)); //建议不超过720P
        config.videoBitrateMin = 1200;
        config.videoBitratePIN = 1800;
        config.videoBitrateMax = 2400;
        config.videoFPS = 30;
        
    }
    else {  //高清
        config.sampleBufferSize = CGSizeMake(544, (uint)(540 * screenSize.height / screenSize.width));
        config.videoBitrateMin = 1000;
        config.videoBitratePIN = 1400;
        config.videoBitrateMax = 1800;
        config.videoFPS = 24;
    }
    
    if (s_landScape) { //横屏推流
        config.sampleBufferSize = CGSizeMake(config.sampleBufferSize.height, config.sampleBufferSize.width);
        config.homeOrientation = HOME_ORIENTATION_RIGHT;
    }
    [s_txLivePublisher setConfig:config];
```
>!
>- 一般手机上为9：16，而在 iPhoneX 上画面比例为1125：2436，因此此处使用屏幕比例进行计算分辨率。
>- 在 ReplayKit2 上采集的都是竖屏的分辨率，如果需要推送横屏分辨率，除了设置横屏分辨率外还需同时指定 homeOrientation 为横屏推流，否则会引起画面变形。


### 步骤 3：发送视频

Replaykit 会将音频和视频都以回调的方式传给`-[SampleHandler processSampleBuffer:withType]`。

```objective-c
- (void)processSampleBuffer:(CMSampleBufferRef)sampleBuffer withType:(RPSampleBufferType)sampleBufferType {
    switch (sampleBufferType) {
        case RPSampleBufferTypeVideo:
            // Handle audio sample buffer
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

                [s_txLivePublisher sendVideoSampleBuffer:sampleBuffer];
        }
}


```

视频 sampleBuffer 只需要调用`-[TXLivePush sendVideoSampleBuffer:]`发送即可。

系统分发视频 sampleBuffer 的频率并不固定，如果画面静止，可能很长时间才会有一帧数据过来。SDK 考虑到这种情况，内部会做补帧逻辑，使其达到 config 所设置的帧率（默认为20fps）。
>!建议保存一帧给推流启动时使用，防止推流启动或切换横竖屏时因无新的画面数据采集发送，因为画面没有变化时系统可能会很长时间才采集一帧画面。

### 步骤 4：发送音频

音频也是通过`-[SampleHandler processSampleBuffer:withType]`给到直播扩展，区别在于音频有两路数据：一路来自 App 内部，一路来自麦克风。

```objective-c
        case RPSampleBufferTypeAudioApp:
            // 来自 App 内部的音频
            [s_txLivePublisher sendAudioSampleBuffer:sampleBuffer withType:sampleBufferType];
            break;
        case RPSampleBufferTypeAudioMic:
            // 发送来着 Mic 的音频数据
            [s_txLivePublisher sendAudioSampleBuffer:sampleBuffer withType:sampleBufferType];
            break;
    
```

SDK 支持同时发送两路数据，内部会对两路数据进行混音处理。

### 步骤 5：暂停与恢复

SDK 内部对视频有补帧逻辑，没有视频时会重发最后一帧数据。音频暂停需要调用`-[TXLivePush setSendAudioSampleBufferMuted:]` ，此时 SDK 自动发送静音数据。

```objective-c
- (void)broadcastPaused {
    // User has requested to pause the broadcast. Samples will stop being delivered.
    [s_txLivePublisher setSendAudioSampleBufferMuted:YES];
}

- (void)broadcastResumed {
    // User has requested to resume the broadcast. Samples delivery will resume.
    [s_txLivePublisher setSendAudioSampleBufferMuted:NO];
}
```

### 步骤 6：SDK 事件处理

#### 事件监听

SDK 事件监听需要设置`TXLivePush`的 delegate 属性，该 delegate 遵循`TXLivePushListener`协议。底层的事件会通过 `-(void) onPushEvent:(int)EvtID withParam:(NSDictionary*)param` 接口回调过来。录屏推流过程中，一般会收到以下事件：

#### 常规事件

| 事件 ID                  | 数值   | 含义说明                 |
| --------------------- | ---- | -------------------- |
| PUSH_EVT_CONNECT_SUCC | 1001 | 已经成功连接到腾讯云推流服务器      |
| PUSH_EVT_PUSH_BEGIN   | 1002 | 与服务器握手完毕，一切正常，准备开始推流 |

可在 PUSH_EVT_PUSH_BEGIN 事件时通知用户推流成功。

####  错误事件

| 事件 ID                            | 数值    | 含义说明                             |
| ------------------------------- | ----- | -------------------------------- |
| PUSH_ERR_VIDEO_ENCODE_FAIL      | -1303 | 视频编码失败                           |
| PUSH_ERR_AUDIO_ENCODE_FAIL      | -1304 | 音频编码失败                           |
| PUSH_ERR_UNSUPPORTED_RESOLUTION | -1305 | 不支持的视频分辨率                        |
| PUSH_ERR_UNSUPPORTED_SAMPLERATE | -1306 | 不支持的音频采样率                        |
| PUSH_ERR_NET_DISCONNECT         | -1307 | 网络断连，且经三次重试无效，可以放弃，更多重试请自行重启推流 |

可在 PUSH_ERR_NET_DISCONNECT 事件时通知用户推流失败。 视频编码失败并不会直接影响推流，SDK 会做处理以保证后面的视频编码成功。

#### 警告事件

| 事件 ID                              | 数值   | 含义说明                            |
| --------------------------------- | ---- | ------------------------------- |
| PUSH_WARNING_NET_BUSY             | 1101 | 网络状况不佳：上行带宽太小，上传数据受阻            |
| PUSH_WARNING_RECONNECT            | 1102 | 网络断连，已启动自动重连 （自动重连连续失败超过三次会放弃） |
| PUSH_WARNING_HW_ACCELERATION_FAIL | 1103 | 硬编码启动失败，采用软编码                   |
| PUSH_WARNING_DNS_FAIL             | 3001 | RTMP -DNS 解析失败（会触发重试流程）          |
| PUSH_WARNING_SEVER_CONN_FAIL      | 3002 | RTMP 服务器连接失败（会触发重试流程）            |
| PUSH_WARNING_SHAKE_FAIL           | 3003 | RTMP 服务器握手失败（会触发重试流程）            |
| PUSH_WARNING_SERVER_DISCONNECT      |  3004|  RTMP 服务器主动断开连接（会触发重试流程）  |

警告事件表示内部遇到了一些问题，但并不影响推流。建议在 PUSH_WARNING_NET_BUSY 事件时通知用户网络状态不佳。
>?全部事件定义请参阅头文件 **“TXLiveSDKEventDef.h”**。

直播扩展由于系统限制，不能触发界面动作，但可以通过发本地通知的方式告知用户推流异常。
事件处理示例：

```
-(void) onPushEvent:(int)EvtID withParam:(NSDictionary*)param {
    NSLog(@"onPushEvent %d", EvtID);
    if (EvtID == PUSH_ERR_NET_DISCONNECT) {
        [self sendLocalNotificationToHostAppWithTitle:@"腾讯云录屏推流" msg:@"推流失败!请重新启动推流" userInfo:nil];
    }  else if (EvtID == PUSH_EVT_PUSH_BEGIN) {
        [self sendLocalNotificationToHostAppWithTitle:@"腾讯云录屏推流" msg:@"连接成功！开始推流" userInfo:nil];
    } else if (EvtID == PUSH_WARNING_NET_BUSY) {
        [self sendLocalNotificationToHostAppWithTitle:@"腾讯云录屏推流" msg:@"网络上行带宽不足" userInfo:nil];
    }
}
```

### 步骤 7：结束推流

结束推流 ReplayKit 会调用`-[SampleHandler broadcastFinished]`，示例代码：

```objective-c
- (void)broadcastFinished {
    // User has requested to finish the broadcast.
    if (s_txLivePublisher) {
        [s_txLivePublisher stopPush];
        s_txLivePublisher = nil;
    }
}
```
结束推流后，直播扩展进程可能会被系统回收，所以需要在此处做好清理工作。


[](id:accessory)
### 附: 扩展与宿主 App 之间的通信与数据传递方式参考
ReplayKit2 录屏只唤起 upload 直播扩展，直播扩展不能进行 UI 操作，也不适于做复杂的业务逻辑，因此通常宿主 App 负责鉴权及其它业务逻辑，直播扩展只负责进行屏幕的音画采集与推流发送，扩展就经常需要与宿主 App 之间进行数据传递与通信。

**1. 发本地通知**
扩展的状态需要反馈给用户，有时宿主 App 并未启动，此时可通过发送本地通知的方式进行状态反馈给用户与激活宿主 App 进行逻辑交互，如在直播扩展启动时通知宿主 App：

```
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
```
通过此通知可以提示用户回到主 App 设置推流信息、启动推流等。

**2. 进程间的通知 CFNotificationCenter**
扩展与宿主 App 之间还经常需要实时的交互处理，本地通知需要用户点击横幅才能触发代码处理，因此不能通过本地通知的方式。而 NSNotificationCenter 不能跨进程，因此可以利用 CFNotificationCenter 在宿主 App 与扩展之前通知发送，但此通知不能通过其中的 userInfo 字段进行数据传递，需要通过配置 App Group 方式使用 NSUserDefault 进行数据传递（也可以使用剪贴板，但剪贴板有时不能实时在进程间获取数据，需要加些延迟规避），如主 App 在获取好推流 URL 等后，通知扩展可以进行推流时，可通过 CFNotificationCenter 进行通知发送直播扩展开始推流：

```
 CFNotificationCenterPostNotification(CFNotificationCenterGetDarwinNotifyCenter(),kDarvinNotificationNamePushStart,NULL,nil,YES);

```
扩展中可通过监听此开始推流通知，由于此通知是在 CF 层，需要通过 NSNotificationCenter 发送到 Cocoa 类层方便处理：

```
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
//通过 NSUserDefault 或剪贴板拿到宿主要传递的数据
//    NSUserDefaults *defaults = [[NSUserDefaults alloc] initWithSuiteName:kReplayKit2AppGroupId];
    
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
```

## 常见问题
ReplayKit2 屏幕录制在 iOS 11 新推出功能，比较少官方文档，并且存在着一些问题每个版本的系统都在不断修复完善中。以下是一些使用中的常见现象或问题：
1. **系统有声音在播放但观众端无法听到声音？**
系统在做屏幕音频采集时，在从 home 界面切到有声音播放的 App 时才会采集声音，从有声音播放的 App 切换到无声音播放的 App 时，即使原 App 还在播放声音系统也不会进行音频采集，此时需要从 home 界面重新进入到有声音播放的 App 时系统才会重新采集。

2. **收到推送信息观众端有时听不到声音？**
这个是 ReplayKit2 在早期系统中存在的问题，收到推送消息后会停止屏幕录制的声音采集或采集到的是静音数据，需要重新从 home 界面切回到有时间的 App 才能恢复音频采集。在11.3之后的版本系统修复了这个问题。

3. **打开麦克风录制时系统播放声音会变小？**
这个是属于系统机制：打开麦克风采集时系统音频处于录制模式，会自动将其它的 App 播放的声音变为听筒模式，中途关闭麦克风采集也不会恢复，只有关闭或重新启动无麦克风录制时才会恢复为扬声器的播放。这个机制不影响 App 那路声音的录制，即观众端声音听到的声音大小不受影响。

4. **屏幕录制何时自动会停止？**
系统在锁屏或有电话打入时，会自动停止屏幕录制，此时 SampleHandler 里的 broadcastFinished 函数会被调用，可在此函数发通知提示用户。

5. **采集推流过程中有时屏幕录制会自动停止问题？**
通常是因为设置的推流分辨率过高时在做横竖屏切换过程中容易出现。ReplayKit2 的直播扩展目前是有50M的内存使用限制，超过此限制系统会直接杀死扩展进程，因此 ReplayKit2 上建议推流分辨率不高于720P。另外不建议使用 autoSampleBufferSize 时做横竖屏切换，因为 Plus 的手机的分辨率可达1080 \* 1920，容易触发系统内存限制而被强制停止。

6. **iPhoneX 手机的兼容性与画面变形问题？**
iPhoneX 手机因为有刘海，屏幕采集的画面分辨率不是9：16，如果设了推流输出分辨率为9 : 16的比例如高清里是为960 \* 540的分辨率，这时因为源分辨率不是9：16的，推出去的画面就会稍有变形。建议设置分辨率时根据屏幕分辨率比例来设置，拉流端用 AspectFit 显示模式 iPhoneX 的屏幕采集推流会有黑边是正常现象，AspectFill 看画面会不全。
