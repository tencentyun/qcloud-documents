
## 概述

录屏功能是 iOS 10 新推出的特性，苹果在 iOS 9 的 ReplayKit 保存录屏视频的基础上，增加了视频流实时直播功能，官方介绍见 [Go Live with ReplayKit](http://devstreaming.apple.com/videos/wwdc/2016/601nsio90cd7ylwimk9/601/601_go_live_with_replaykit.pdf)。iOS 11 新增的 ReplayKit2，进一步提升了 Replaykit 的易用性和通用性，可以对整个手机实现屏幕录制，而非某些做了支持ReplayKit功能的App，因此录屏推流建议直接使用iOS11的屏幕录制方式。扩展程序有单独的进程，iOS 系统为了保证系统流畅，给扩展程序的资源相对较少，扩展程序内存占用过大也会被 Kill 掉。腾讯云 RTMP SDK 在原有直播的高质量、低延迟的基础上，进一步降低系统消耗，保证了扩展程序稳定。

>注：本文主要介绍 iOS 11 上使用 SDK 的方法，更具体的使用可参考 Demo 里 ReplaykitUpload 文件夹中的示例代码; 涉及UI扩展的介绍主要适用于iOS 10。

## 功能体验

体验iOS录屏可以单击安装 [视频云工具包](https://itunes.apple.com/cn/app/%E8%A7%86%E9%A2%91%E4%BA%91%E5%B7%A5%E5%85%B7%E5%8C%85/id1152295397?mt=8) 
或 扫码安装
![扫码安装](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/1529471216.png)

使用步骤：
1. 打开控制中心，长按屏幕录制按钮，选择【视频云工具包】。
2. 打开【视频云工具包】->【录屏幕推流】，输入推流地址或单击【New】自动获取推流地址，单击【开始推流】。

![ScreenRecord](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/out.png)

推流设置成功后，顶部通知栏会提示推流开始，此时您可以在其它设备上看到该手机的屏幕画面。单击手机状态栏的红条，即可停止推流。

## 开发环境准备

### Xcode 准备

Xcode 9 及以上的版本，手机也必须升级至 iOS 11 以上，模拟器无法使用录屏特性。

### 创建直播扩展

在现有工程选择【New】->【Target…】，选择【Broadcast Upload Extension】，如图所示。

![4](//mc.qcloudimg.com/static/img/9d18eb52c817ba14bbd707be56adb84c/image.png)

配置好Product Name。如果iOS 10的App内录屏方式，可勾选【Include UI Extension】。如果勾选上，点【Finish】后可以看到，工程多了两个目录，并且target也多了两个，分别是直播扩展和UI扩展。
> 注：iOS 11的录屏直播只需要Upload直播扩展


![5](//mc.qcloudimg.com/static/img/6712032a19170ea7725ae8b445c7dddc/image.png)

iOS 10 的 Replay Kit 支持两种直播方式：

1. 将视频和音频编码为一小段 mp4 文件，交给直播扩展。
2. 将屏幕和声音的原始数据交给扩展。

方式 1 延迟高，不灵活，优点是扩展 app 无须关心编码问题；方式 2 可以自定义发送的内容，可配置性高。目前 SDK 仅支持第二种方式。由于 Xcode 默认使用了方式 1，因此需要修改直播扩展 Info.plist 到如图所示。

![6](//mc.qcloudimg.com/static/img/bc86b68eb7c88ceb989c8b059ce41472/image.png)

### 导入 LiteAV SDK

直播扩展需要导入 TXLiteAVSDK.framework。扩展导入 framework 的方式和主 App 导入方式相同，SDK 的系统依赖库也没有区别。具体可参考腾讯云官网 [工程配置(iOS)](https://cloud.tencent.com/document/product/454/7876)。


## 对接流程

### Step 1: 编写 UI 扩展[可选, ReplayKit2的录屏不需要]

游戏 App 发起直播，首先进入的是 UI 扩展。这里可以根据您产品需要定制界面。如果您的直播软件需要登录，最好在这里先检查登录态，因为在直播过程中不能显示任何界面。

当用户确认发起直播，UI 扩展就可以把启动直播扩展，而且可以带上一些自定义的参数。启动直播扩展示例代码如下。

```objective-c
// Called when the user has finished interacting with the view controller and a broadcast stream can start
- (void)userDidFinishSetup {
    
    // Broadcast url that will be returned to the application
    NSURL *broadcastURL = [NSURL URLWithString:@"http://broadcastURL_example/stream1"];
    
    // Service specific broadcast data example which will be supplied to the process extension during broadcast
    NSString *userID = @"user1";
    NSString *endpointURL = @"rtmp://2157.livepush.myqcloud.com/live/xxxxxx";
    NSDictionary *setupInfo = @{ @"userID" : userID, @"endpointURL" : endpointURL };
    
    // Set broadcast settings
    RPBroadcastConfiguration *broadcastConfig = [[RPBroadcastConfiguration alloc] init];
    broadcastConfig.clipDuration = 5.0; // deliver movie clips every 5 seconds
    
    // Tell ReplayKit that the extension is finished setting up and can begin broadcasting
    [self.extensionContext completeRequestWithBroadcastURL:broadcastURL
                broadcastConfiguration:broadcastConfig setupInfo:setupInfo];
}
```

### Step 2: 创建推流对象

工程模版已经为我们创建好直播扩展的基本框架。只需要在 SampleHandler.m 前添加下面代码。

```objective-c
#import "SampleHandler.h"
#import "TXRTMPSDK/TXLiveSDKTypeDef.h"
#import "TXRTMPSDK/TXLivePush.h"
#import "TXRTMPSDK/TXLiveBase.h"
static TXLivePush *s_txLivePublisher;
```

s_txLivePublisher 是我们用于推流的对象。实例化 s_txLivePublisher 的最佳位置是在`-[SampleHandler broadcastStartedWithSetupInfo:]`方法中，UI 扩展启动推流后会回调这个函数开始直播。如果是ReplayKit2的屏幕录制直播扩展，这里的setupInfo为nil，需要与主App数据传递与通信来获取推流信息等，请参考[扩展与宿主App之间的通信与数据传递]。

```objective-c
- (void)broadcastStartedWithSetupInfo:(NSDictionary<NSString *,NSObject *> *)setupInfo {
    if (s_txLivePublisher) {
        [s_txLivePublisher stopPush]; // 开始推流前先结束上一次推流
    }
    
    TXLivePushConfig* config = [[TXLivePushConfig alloc] init];
    config.customModeType |= CUSTOM_MODE_VIDEO_CAPTURE;
    config.autoSampleBufferSize = YES;
    
    config.customModeType |= CUSTOM_MODE_AUDIO_CAPTURE;
    config.audioSampleRate = 44100;
    config.audioChannels   = 1;
//				CGSize screenSize = [[UIScreen mainScreen] currentMode].size;
//				config.sampleBufferSize = CGSizeMake(720, 720 * screenSize.height / screenSize.width)
//        config.videoBitrateMin = 1500;
//        config.videoBitratePIN = 2000;
//        config.videoBitrateMax = 2500;
//        config.videoFPS = 30;

    s_txLivePublisher = [[TXLivePush alloc] initWithConfig:config];
    NSString *pushUrl = setupInfo[@"endpointURL"]; // setupInfo 来自于 UI 扩展， 如果是replaykit2屏幕录制，setupInfo为nil，需要与主App数据传递与通信来获取推流信息
    [s_txLivePublisher startPush:pushUrl]; 
		
		//推流开始后发送一帧
		 if (s_lastSampleBuffer) {
           [s_txLivePublisher sendVideoSampleBuffer:s_lastSampleBuffer];
    }
}
```
s_txLivePublisher 的 config 不能使用默认的配置，需要设置自定义采集视频和音频。

视频启用 autoSampleBufferSize，开启此选项后，您不需要关心推流的分辨率，SDK 会自动根据输入的分辨率设置编码器；如果您关闭此选项，那么代表您需要自定义分辨率

> 注1：ReplayKit2上不建议使用autoSampleBufferSize，因为会根据机型不一样有不一样的推流分辨率，在Plus的手机时可达1080*1920,容易触发系统内存限制而被强制停止
> 注2: 推流开始后建议发送一帧画面采集帧。因为系统只有在界面有变化时才会采集画面，有可能在开始推流后没有新的画面采集即没有数据发送而推流失败。

#### *扩展与宿主App之间的通信与数据传递
ReplayKit2录屏只唤起upload直播扩展，直播扩展不能进行UI操作或不适于做复杂的业务逻辑，因此通常宿主App负责鉴权及其它业务逻辑，直播扩展只负责进行屏幕的音画采集与推流发送，扩展经常需要与宿主App进行数据传递与通信。
**1. 发本地通知**
扩展的推流状态需要反馈给用户，有时宿主App并未启动，此时可通过发送本地通知的方式进行状态反馈给用户与激活宿主App进行逻辑交互，如在直播扩展启动时通知宿主App：

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

**2.进程间的通知CFNotificationCenter**
扩展与宿主App之间经常需要实时的交互处理，本地通知需要用户点知横幅才能触发代码处理，因此不能通过本地通知的方式。而NSNotificationCenter不能跨进程，因此可以利用CFNotificationCenter在宿主App与扩展之前通知发送，但此通知不能通过其中的userInfo字段进行数据传递，需要通过配置App Group方式使用NSUserDefault进行数据传递(也可以使用剪贴板，但剪贴板有时不能实时在进程间获取数据，需要通知后加些延迟规避), 如宿主App在获取好推流URL等后，通知扩展可以进行推流时，可使用因此需要通过CFNotificationCenter进行通知发送直播扩展开始推流：

```
                CFNotificationCenterPostNotification(CFNotificationCenterGetDarwinNotifyCenter(),kDarvinNotificationNamePushStart,NULL,nil,YES);

```
扩展中可通过监听此开始推流通知，由于此通知是在CF层，需要通过NSNotificationCenter发送到Cocoa类层方便处理：

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
//转到cocoa层框架处理
    [[NSNotificationCenter defaultCenter] postNotificationName:@"Cocoa_ReplayKit2_Push_Start" object:nil];
}

- (void)handleReplayKit2PushStartNotification:(NSNotification*)noti
{
//通过NSUserDefault或剪贴板拿到宿主要传递的数据
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
//    [self sendLocalNotificationToHostAppWithTitle:@"腾讯云录屏推流" msg:[NSString stringWithFormat:@"推流地址:%@", s_rtmpUrl] userInfo:nil];
    [self start];
}
```

### Step 3: 横竖屏与自定义分辨率

如果您不想用屏幕输出的分辨率，也可以指定任意一个分辨率，SDK 内部将根据您指定的分辨率进行缩放。homeOrientation可以设置横竖屏推流，分辨率需要同时设置为对应的横竖屏比例。

```objective-c
// 指定 720P，默认竖屏
CGSize screenSize = [[UIScreen mainScreen] currentMode].size;
config.sampleBufferSize = CGSizeMake(720, 720 * screenSize.height / screenSize.width); //建议不超过720P，否则容易触发系统限制
//config.homeOrientation = HOME_ORIENTATION_DOWN; 

//横屏
if (s_landScape) {
		config.sampleBufferSize = CGSizeMake(config.sampleBufferSize.height, config.sampleBufferSize.width);
		config.homeOrientation = HOME_ORIENTATION_RIGHT;
}
```
> 注1：设置的分辨率需与屏幕分辨率比例一致，否则会引起画面变形。一般手机上为9:16，而在iPhoneX上画面比例为1125:2436。
> 注2：在ReplayKit2上采集的都是竖屏的分辨率，因此如果分辨率指定为横屏分辨率，需要配合指定homeOrientation为横屏推流，否则会引起画面变形。

### Step 4: 发送视频

Replaykit 会将音频和视频都以回调的方式传给`-[SampleHandler processSampleBuffer:withType]`

```objective-c
- (void)processSampleBuffer:(CMSampleBufferRef)sampleBuffer withType:(RPSampleBufferType)sampleBufferType {
    switch (sampleBufferType) {
        case RPSampleBufferTypeVideo:
            // Handle audio sample buffer
        {
                if (!CMSampleBufferIsValid(sampleBuffer))
                    return;
										                //保存一帧在startPush时发送,防止推流启动后或切换横竖屏因无画面数据而推流不成功
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

系统分发视频 sampleBuffer 的频率并不固定，如果画面静止，可能很长时间才会有一帧数据过来。SDK 考虑到这种情况，内部会做补帧逻辑，使其达到 config 所设置的帧率（默认为 20fps）。
> 注：建议保存一帧给推流启动时使用，防止推流启动或切换横竖屏时因无新的画面数据采集发送而推流不成功

### Step 5: 发送音频

音频也是通过`-[SampleHandler processSampleBuffer:withType]`给到直播扩展，区别在于音频有两路数据：一路来自 App 内部，一路来自麦克风。

```objective-c
    switch (sampleBufferType) {
        case RPSampleBufferTypeAudioApp:
            // 来自 App 内部的音频
            [s_txLivePublisher sendAudioSampleBuffer:sampleBuffer withType:sampleBufferType];
            break;
        case RPSampleBufferTypeAudioMic:
        {
            // 发送来着 Mic 的音频数据
            [s_txLivePublisher sendAudioSampleBuffer:sampleBuffer withType:sampleBufferType];
        }
            break;
    }
```

SDK 支持同时发送两路数据，内部会对两路数据进行混音处理。通常情况，只有当用户插上耳机时才有必要发送两路数据，否则建议只发送 Mic 的声音数据。

> 注：在ReplayKit2的屏幕录制中，请同时发两路声音数据。因为用户可能中途关闭麦克风音频，此时 RPSampleBufferTypeAudioMic 数据不能收到。

### Step 6: 暂停与恢复

游戏 App 可以暂停当前直播，扩展程序不会收到数据，直到用户恢复直播。在自定义采集模式下，SDK 需要外部持续提供数据源，否则服务器会因长时间得不到数据而断开直播。

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

### Step 7: SDK 事件处理

#### 事件监听

SDK 事件监听需要设置`TXLivePush`的 delegate 属性，该 delegate 遵循`TXLivePushListener`协议。底层的事件会通过`-(void) onPushEvent:(int)EvtID withParam:(NSDictionary*)param`接口回调过来。

直播扩展由于系统限制，不能触发界面动作，但可以通过发本地通知的方式告知用户推流异常。录屏过程中，一般会收到以下事件。

#### 常规事件

| 事件 ID                  | 数值   | 含义说明                 |
| --------------------- | ---- | -------------------- |
| PUSH_EVT_CONNECT_SUCC | 1001 | 已经成功连接到腾讯云推流服务器      |
| PUSH_EVT_PUSH_BEGIN   | 1002 | 与服务器握手完毕,一切正常，准备开始推流 |

可在PUSH_EVT_PUSH_BEGIN事件时通知用户推流成功。

####  错误事件

| 事件 ID                            | 数值    | 含义说明                             |
| ------------------------------- | ----- | -------------------------------- |
| PUSH_ERR_VIDEO_ENCODE_FAIL      | -1303 | 视频编码失败                           |
| PUSH_ERR_AUDIO_ENCODE_FAIL      | -1304 | 音频编码失败                           |
| PUSH_ERR_UNSUPPORTED_RESOLUTION | -1305 | 不支持的视频分辨率                        |
| PUSH_ERR_UNSUPPORTED_SAMPLERATE | -1306 | 不支持的音频采样率                        |
| PUSH_ERR_NET_DISCONNECT         | -1307 | 网络断连,且经三次抢救无效,可以放弃治疗,更多重试请自行重启推流 |

可在PUSH_ERR_NET_DISCONNECT事件时通知用户推流失败。 视频编码失败并不会直接影响推流，SDK 会做处理以保证后面的视频编码成功。

#### 警告事件

| 事件 ID                              | 数值   | 含义说明                            |
| --------------------------------- | ---- | ------------------------------- |
| PUSH_WARNING_NET_BUSY             | 1101 | 网络状况不佳：上行带宽太小，上传数据受阻            |
| PUSH_WARNING_RECONNECT            | 1102 | 网络断连, 已启动自动重连 (自动重连连续失败超过三次会放弃) |
| PUSH_WARNING_HW_ACCELERATION_FAIL | 1103 | 硬编码启动失败，采用软编码                   |
| PUSH_WARNING_DNS_FAIL             | 3001 | RTMP -DNS 解析失败（会触发重试流程）          |
| PUSH_WARNING_SEVER_CONN_FAIL      | 3002 | RTMP 服务器连接失败（会触发重试流程）            |
| PUSH_WARNING_SHAKE_FAIL           | 3003 | RTMP 服务器握手失败（会触发重试流程）            |
| PUSH_WARNING_SERVER_DISCONNECT      |  3004|  RTMP 服务器主动断开连接（会触发重试流程）  |

警告事件表示内部遇到了一些问题，但并不影响推流。建议在PUSH_WARNING_NET_BUSY事件时通知用户网络状态不佳。

> 全部事件定义请参阅头文件**“TXLiveSDKEventDef.h”**

### Step 8: 结束推流

结束推流 Replay Kit 会调用`-[SampleHandler broadcastFinished]`，示例代码。

```objective-c
- (void)broadcastFinished {
    // User has requested to finish the broadcast.
    if (s_txLivePublisher) {
        [s_txLivePublisher stopPush];
        s_txLivePublisher = nil;
    }
}
```

结束推流后，直播扩展进程可能会被系统回收，所以务必在此做好清理工作。
## 常见问题
ReplayKit2屏幕录制在iOS11新推出功能，比较少官方文档并且存在着一些问题每个版本的系统都在不断修复完善中。以下是一些使用中的常见现象或问题:
1. 系统有声音在播放但观众端无法听到声音
系统在做屏幕音频采集时，在从home界面切到有声音播放的App时才会采集声音，从有声音播放的App切换到无声音播放的App时，即使原App还在播放声音系统也不会进行音频采集，此时需要从home界面重新进入到有声音播放的App时系统才会重新采集。

2. 收到推送信息观众端有时听不到声音
这个是ReplayKit2在早期系统中存在的问题，收到推送消息后会停止屏幕录制的声音采集或采集到的是静音数据，需要重新从home界面切回到有时间的App才能恢复音频采集。在11.3之后的版本系统修复了这个问题。

3. 打开麦克风录制时系统播放声音会变小
这个是属于系统机制：打开麦克风采集时系统音频处于录制模式，会自动将其它的App播放的声音变为听筒模式，中途关闭麦克风采集也不会恢复，只有关闭或重新启动无麦克风录制时才会恢复为扬声器的播放。这个机制不影响App那路声音的录制，即观众端声音听到的声音大小不受影响。

4. 屏幕录制何时自动会停止
系统在锁屏或有电话打入时，会自动停止屏幕录制，此时SampleHandler里的broadcastFinished函数会被调用，可在此函数发通知提示用户。

5. 采集推流过程中有时屏幕录制会自动停止问题
通常是因为设置的推流分辨率过高时在做横竖屏切换过程中容易出现。ReplayKit2的直播扩展目前是有50M的内存使用限制，超过此限制系统会直接杀死扩展进程，因此ReplayKit2上建议推流分辨率不高于720P。另外不建议使用autoSampleBufferSize时做横竖屏切换，因为Plus的手机的分辨率可达1080*1920,容易触发系统内存限制而被强制停止

6. iphoneX手机的兼容性与画面变形问题
iphoneX手机因为有刘海，屏幕采集的画面分辨率不是9:16，如果设了推流输出分辨率为9:16的比例如高清里是为960*540的分辨率，这时因为源分辨率不是9:16的，推出去的画面就会稍有变形。建议设置分辨率时根据屏幕分辨率比例来设置，拉流端用AspectFit显示模式iPhoneX的屏幕采集推流会有黑边是正常现象，AspectFill看画面会不全。
