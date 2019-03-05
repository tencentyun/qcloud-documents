
## 概述

录屏功能是iOS 10新推出的特性，苹果在 iOS 9 的 ReplayKit 保存录屏视频的基础上，增加了视频流实时直播功能，官方介绍见 [Go Live with ReplayKit](http://devstreaming.apple.com/videos/wwdc/2016/601nsio90cd7ylwimk9/601/601_go_live_with_replaykit.pdf)。
iOS 11新增的ReplayKit2，进一步提升了Replaykit的易用性，可以对整个手机实现屏幕录制，而非某些特定App。

扩展程序有单独的进程。iOS系统为了保证系统流畅，给扩展程序的资源相对较少，扩展程序内存占用过大也会被Kill掉。腾讯云RTMP SDK在原有直播的高质量、低延迟的基础上，进一步降低系统消耗，保证了扩展程序稳定。

> iOS 11和iOS 10的扩展程序编写并无区别，本文将介绍iOS 11上使用SDK的方法，代码同样适用于iOS 10

## 功能体验

体验iOS录屏可下载我们的测试demo：[RPLiveStream](http://dldir1.qq.com/hudongzhibo/xiaozhibo/RPLiveStream-master.zip)。

![扫码安装](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/er.png)

下载后真机运行，点击“开始直播”。填写正确推流地址即可体验录屏功能。

![RPLiveStream](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/RPLiveStream.png)

体验系统屏幕录制，打开控制中心，长按屏幕录制按钮，选择好直播的程序，开始直播。

![ScreenRecord](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ScreenRecord.png)

> 注意：系统屏幕录制不会弹出扩展UI，因此RPLiveStream不能输入推流地址。此时需要在App里先开播，扩展Upload会记下您输入的推流地址，再来系统屏幕录制，流数据就会发送到上一个推流地址。

## 开发环境准备

### Xcode 准备

Xcode 9及以上的版本，手机也必须升级至iOS 11以上，模拟器无法使用录屏特性。

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

直播扩展需要导入TXLiteAVSDK.framework。扩展导入framework的方式和主App导入方式相同，SDK的系统依赖库也没有区别。具体可参考腾讯云官网《工程配置(iOS)》

> https://cloud.tencent.com/doc/api/258/5320


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

s_txLivePublisher的config不能使用默认的配置，需要设置自定义采集视频和音频。关于自定义采集的设置的原理和工作方式，参见腾讯云文档《RTMP推流－进阶应用》

> https://cloud.tencent.com/doc/api/258/6458

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

Replaykit会将音频和视频都以回调的方式传给`-[SampleHandler processSampleBuffer:withType]`

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
            [s_txLivePublisher sendAudioSampleBuffer:sampleBuffer withType:sampleBufferType];
            break;
        case RPSampleBufferTypeAudioMic:
        {
        	// 发送来着Mic的音频数据
            [s_txLivePublisher sendAudioSampleBuffer:sampleBuffer withType:sampleBufferType];
        }
            break;
	}
```

SDK支持同时发送两路数据，内部会对两路数据进行混音。通常情况，只有当用户插上耳机时，才有必要发送两路数据。否者建议只发送Mic的声音数据。

在屏幕录制时，用户可能关闭麦克风音频，此时RPSampleBufferTypeAudioMic数据不能收到。

### Step 6: 暂停与恢复

游戏App可以暂停当前直播，扩展程序不会收到数据，直到用户恢复直播。在自定义采集模式下，SDK需要外部持续提供数据源，否则服务器会因长时间得不到数据而断开直播。

SDK内部对视频有补帧逻辑，没有视频时会重发最后一帧数据。音频暂停需要调用`-[TXLivePush setSendAudioSampleBufferMuted:]` ，此时SDK自动发送静音数据。

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