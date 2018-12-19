
## 概述

录屏功能是iOS 10新推出的特性，苹果在 iOS 9 的 ReplayKit 保存录屏视频的基础上，增加了视频流实时直播功能，官方介绍见 [Go Live with ReplayKit](http://devstreaming.apple.com/videos/wwdc/2016/601nsio90cd7ylwimk9/601/601_go_live_with_replaykit.pdf)。

录屏的整个流程分为游戏App和直播App两个部分。iOS录屏时并没有让直播App直接运行，而是以扩展程序的形式为游戏App服务。扩展程序也分为两个，一个是用于显示自定义界面，这个界面可以让用户输入标题、显示用户信息等，用户点击确定后转到另一个扩展程序中发送屏幕数据，这个扩展并没有显示UI的能力。整个录屏直播的结构如下图所示。

![1](//mc.qcloudimg.com/static/img/8e2f3b74b9c1f2d93feb8ef403042fd8/image.png)

Broadcast Upload作为一个扩展程序，有单独的进程。iOS系统为了保证系统流畅，给扩展程序的资源相对较少，扩展程序内存占用过大也会被Kill掉。腾讯云RTMP SDK在原有直播的高质量、低延迟的基础上，进一步降低系统消耗，保证了扩展程序稳定。

## 功能体验

由于录屏功能需要游戏和直播软件都支持，才能完成录制的流程。直播软件推荐使用我们的“小直播”，下载地址
![2](//mc.qcloudimg.com/static/img/721f68e5ebb0779d2b14a97de40b0121/image.png)

随着iOS 10普及，支持录屏的游戏也在普及。如果您没有可录屏的游戏，可下载“坦克之战”这款游戏，点击上方的直播，选择小直播即可开始录屏。
![3](//mc.qcloudimg.com/static/img/84ded1555fb546da6652491f4ef71183/image.png)


## 开发环境准备

### Xcode 准备

录屏直播是iOS 10提供的新特性，所以需要Xcode 8及以上的版本，手机也必须升级至iOS 10以上，模拟器无法使用录屏特性。

### 创建直播扩展

在现有工程选择“New”->"Target…"，选择“Broadcast Upload Extension"，如图所示

![4](//mc.qcloudimg.com/static/img/9d18eb52c817ba14bbd707be56adb84c/image.png)

配置好Product Name，注意勾选"Include UI Extension"。点“Finish“后可以看到，工程多了两个目录，并且target也多了两个，分别是直播扩展和UI扩展。

![5](//mc.qcloudimg.com/static/img/6712032a19170ea7725ae8b445c7dddc/image.png)

iOS 10的Replay Kit支持两种直播方式

1. 将视频和音频编码为一小段mp4文件，交给直播扩展
2. 将屏幕和声音的原始数据交给扩展

方式1延迟高，不灵活，优点是扩展app无须关心编码问题；方式2可以自定义发送的内容，可配置性高。目前SDK仅支持第二种方式。由于Xcode默认使用了方式1，因此需要修改直播扩展Info.plist到如图所示

![6](//mc.qcloudimg.com/static/img/bc86b68eb7c88ceb989c8b059ce41472/image.png)

### 导入RTMP SDK

直播扩展需要导入TXRTMPSDK.framework。扩展导入framework的方式和主App导入方式相同，SDK的系统依赖库也没有区别，具体可参考腾讯云官网《[工程配置(iOS)](https://cloud.tencent.com/document/product/454/7876)》。


## 对接流程

### Step 1: 编写UI扩展

游戏App发起直播，首先进入的是UI扩展。这里可以根据您产品需要订制界面。如果您的直播软件需要登录，最好在这里先检查登录态，因为在直播过程中不能显示任何界面。

当用户确认发起直播，UI扩展就可以把启动直播扩展，而且可以带上一些自定义的参数。启动直播扩展示例代码如下

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

工程模版已经为我们创建好直播扩展的基本框架。只需要在SampleHandler.m前添加下面代码

```objective-c
#import "SampleHandler.h"
#import "TXRTMPSDK/TXLiveSDKTypeDef.h"
#import "TXRTMPSDK/TXLivePush.h"
#import "TXRTMPSDK/TXLiveBase.h"
static TXLivePush *s_txLivePublisher;
```

s_txLivePublisher是我们用于推流的对象。实例化s_txLivePublisher的最佳位置是在`-[SampleHandler broadcastStartedWithSetupInfo:]`方法中，UI扩展启动推流后会回调这个函数开始直播。

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
    
    s_txLivePublisher = [[TXLivePush alloc] initWithConfig:config];
  	NSString *pushUrl = setupInfo[@"endpointURL"]; // setupInfo来自于UI扩展
    [s_txLivePublisher startPush:pushUrl];  
}
```

s_txLivePublisher的config不能使用默认的配置，需要设置自定义采集视频和音频。关于自定义采集的设置的原理和工作方式，参见腾讯云文档《[RTMP推流－深度使用](https://cloud.tencent.com/document/product/454/7884)》。

视频启用autoSampleBufferSize，开启此选项后，您不需要关心推流的分辨率，SDK会自动根据输入的分辨率设置编码器；如果您关闭此选项，那么代表您需要自定义分辨率

> 推荐开启autoSampleBufferSize，这样可以得到最佳性能。同时，您也不必关心横屏或竖屏

### Step 3: 自定义分辨率

如果您需不想用屏幕输出的分辨率，也可以指定任意一个分辨率，SDK内部将根据您指定的分辨率进行缩放

```objective-c
// 指定640*360
config.autoSampleBufferSize = NO;
config.sampleBufferSize = CGSizeMake(640, 360);
```

### Step 4: 发送视频

Replay Kit会将音频和视频都以回调的方式传给`-[SampleHandler processSampleBuffer:withType]`

```objective-c
- (void)processSampleBuffer:(CMSampleBufferRef)sampleBuffer withType:(RPSampleBufferType)sampleBufferType {
    switch (sampleBufferType) {
        case RPSampleBufferTypeVideo:
            // Handle audio sample buffer
        {
            [s_txLivePublisher sendVideoSampleBuffer:sampleBuffer];
            return;
        }
}
```

视频sampleBuffer只需要调用`-[TXLivePush sendVideoSampleBuffer:]`发送即可。

系统分发视频sampleBuffer的频率并不固定，如果画面静止，可能很长时间才会有一帧数据过来。SDK考虑到这种情况，内部会做补帧逻辑，使其达到config所设置的帧率（默认为20fps）。

### Step 5: 发送音频

音频也是通过`-[SampleHandler processSampleBuffer:withType]`给到直播扩展，区别在于音频有两路数据：一路来自App内部，一路来自麦克风。

```objective-c
    switch (sampleBufferType) {
        case RPSampleBufferTypeAudioApp:
            // 来自App内部的音频
            
            break;
        case RPSampleBufferTypeAudioMic:
            // 来自Mic的音频。
        {
        	// 发送来着Mic的音频数据
            [s_txLivePublisher sendAudioSampleBuffer:sampleBuffer];
        }
            break;
	}
```

SDK不支持同时发送两路数据，您需要跟进情况自己选择使用那一份音频。

### Step 6: 暂停与恢复

游戏App可以暂停当前直播，此时Samples buffer不再分发到直播扩展，直到用户恢复直播。在自定义采集模式下，SDK需要外部持续提供数据源，否则服务器会因长时间得不到数据而断开直播。

SDK内部对视频有补帧逻辑，没有视频时会重发最后一帧数据，而音频没有补帧逻辑，不向SDK提供数据会导致音画不同步的现象发生。您可以用下面的简单代码，在暂停时向SDK发送静音数据。

```objective-c
static dispatch_source_t s_audioTimer;

- (void)pause {
    if (s_audioTimer) {
        return;
    }
    
    dispatch_queue_t queue = dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
    s_audioTimer = dispatch_source_create(DISPATCH_SOURCE_TYPE_TIMER, 0, 0, queue);
    dispatch_source_set_timer(s_audioTimer,DISPATCH_TIME_NOW,20*NSEC_PER_MSEC, 0);
    dispatch_source_set_event_handler(s_audioTimer, ^{
        static uint8_t _audioData[2048] = {0};
        [s_txLivePublisher sendCustomPCMData:_audioData len:sizeof(_audioData)];
    });
    dispatch_resume(s_audioTimer);
}

- (void)resume {
    if (s_audioTimer) {
        dispatch_cancel(s_audioTimer);
        s_audioTimer = 0;
    }
}

- (void)broadcastPaused {
    // User has requested to pause the broadcast. Samples will stop being delivered.
    [self pause];
}

- (void)broadcastResumed {
    // User has requested to resume the broadcast. Samples delivery will resume.
    [self resume];
}
```

### Step 7: SDK事件处理

#### 事件监听

SDK事件监听需要设置`TXLivePush`的delegate属性，该delegate遵循`TXLivePushListener`协议。底层的事件会通过`-(void) onPushEvent:(int)EvtID withParam:(NSDictionary*)param`接口回调过来。

直播扩展由于系统限制，不能触发界面动作，因此也不能主动通知用户推流异常。录屏过程中，一般会收到以下事件。

#### 常规事件

| 事件ID                  | 数值   | 含义说明                 |
| --------------------- | ---- | -------------------- |
| PUSH_EVT_CONNECT_SUCC | 1001 | 已经成功连接到腾讯云推流服务器      |
| PUSH_EVT_PUSH_BEGIN   | 1002 | 与服务器握手完毕,一切正常，准备开始推流 |

常规事件通常无须处理。

####  错误事件

| 事件ID                            | 数值    | 含义说明                             |
| ------------------------------- | ----- | -------------------------------- |
| PUSH_ERR_VIDEO_ENCODE_FAIL      | -1303 | 视频编码失败                           |
| PUSH_ERR_AUDIO_ENCODE_FAIL      | -1304 | 音频编码失败                           |
| PUSH_ERR_UNSUPPORTED_RESOLUTION | -1305 | 不支持的视频分辨率                        |
| PUSH_ERR_UNSUPPORTED_SAMPLERATE | -1306 | 不支持的音频采样率                        |
| PUSH_ERR_NET_DISCONNECT         | -1307 | 网络断连,且经三次抢救无效,可以放弃治疗,更多重试请自行重启推流 |

视频编码失败并不会直接影响推流，SDK会做处理以保证后面的视频编码成功。

#### 警告事件

| 事件ID                              | 数值   | 含义说明                            |
| --------------------------------- | ---- | ------------------------------- |
| PUSH_WARNING_NET_BUSY             | 1101 | 网络状况不佳：上行带宽太小，上传数据受阻            |
| PUSH_WARNING_RECONNECT            | 1102 | 网络断连, 已启动自动重连 (自动重连连续失败超过三次会放弃) |
| PUSH_WARNING_HW_ACCELERATION_FAIL | 1103 | 硬编码启动失败，采用软编码                   |
| PUSH_WARNING_DNS_FAIL             | 3001 | RTMP -DNS解析失败（会触发重试流程）          |
| PUSH_WARNING_SEVER_CONN_FAIL      | 3002 | RTMP服务器连接失败（会触发重试流程）            |
| PUSH_WARNING_SHAKE_FAIL           | 3003 | RTMP服务器握手失败（会触发重试流程）            |
| PUSH_WARNING_SERVER_DISCONNECT      |  3004|  RTMP服务器主动断开连接（会触发重试流程）  |

警告事件表示内部遇到了一些问题，但并不影响推流。

> 全部事件定义请参阅头文件**“TXLiveSDKEventDef.h”**

### Step 8: 结束推流

结束推流Replay Kit会调用`-[SampleHandler broadcastFinished]`，示例代码

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