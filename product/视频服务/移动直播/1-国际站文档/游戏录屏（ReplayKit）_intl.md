
## Overview

Screencap is a feature newly introduced in iOS 10. Based on the ReplayKit screencap video save feature on iOS 9, Apple added real-time video stream LVB feature. For official introduction, see [Go Live with ReplayKit](http://devstreaming.apple.com/videos/wwdc/2016/601nsio90cd7ylwimk9/601/601_go_live_with_replaykit.pdf).
The ReplayKit2 newly introduced in iOS 11 further enhances the ease of use and allows recording any screen on your phone instead of screens of certain apps.

The extension has its own process. To ensure system performance, iOS systems allocate less resource to extensions, and extensions that occupy too much memory will be killed. Based on the high quality, low latency of the original LVB feature, Tencent Cloud RTMP SDK further reduced system resource usage to ensure extension stability.

> There is no difference in extension programming for iOS 11 and iOS 10. This article introduces how to use SDK on iOS 11. The code also can be used with iOS 10.

## Try out the Feature

You can download our test demo [RPLiveStream] (http://dldir1.qq.com/hudongzhibo/xiaozhibo/RPLiveStream-master.zip) to try the iOS screencap.

![Scan to install](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/er.png)

Run it on your device after downloading, and click **Start LVB**. Enter the correct push URL to try screencap features.

![RPLiveStream](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/RPLiveStream.png)

To try the system screen recording, open the control center, long press the screen recording button, and select the LVB application to start LVB.

![ScreenRecord](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ScreenRecord.png)

> Note: During the system screen recording, the UI extension will not pop up, so you cannot enter the push URL through RPLiveStream. In this case, you need to start LVB in the App first. As the Upload extension can remember the push URL you entered, the streaming data is then sent to there if you start system screen recording later.

## Development Environment Preparation

### Xcode Preparation

The version of Xcode 9 or higher is required, and your phone system must be upgraded to iOS 11 or above. Screencap is not supported for a simulator.

### Create an LVB extension

In the current project, select **New** -> **Target...**, and then **Broadcast Upload Extension**, as shown below:

![4](//mc.qcloudimg.com/static/img/9d18eb52c817ba14bbd707be56adb84c/image.png)

Configure Product Name. Remember to check **Include UI Extension**. Click **Finish** and you will see two more directories and two more targets, LVB extension and UI extension, added to the project.

![5](//mc.qcloudimg.com/static/img/6712032a19170ea7725ae8b445c7dddc/image.png)

The Replay Kit of iOS 10 supports two LVB modes:

1. The video and audio are encoded into a short mp4 file and handed over to the LVB extension.
2. The original screen and audio data is handed over to the extension.

The first mode has high latency and poor flexibility but the extension App doesn't have to be concerned with encoding issues; while the second mode allows you to customize what you send and has high configurability. The SDK now only supports the second mode. Since Xcode uses the first mode by default, you need to modify the Info.plist of the LVB extension as shown below:

![6](//mc.qcloudimg.com/static/img/bc86b68eb7c88ceb989c8b059ce41472/image.png)

### Import RTMP SDK

TXRTMPSDK.framework needs to be imported to the LVB extension. The framework is imported to the extension in the same way as it is to the master App, so is the system dependency library of SDK. For details, see Project Configuration (iOS) on the Tencent Cloud official website.

> https://cloud.tencent.com/doc/api/258/5320


## Interfacing Process

### Step 1: Program a UI extension

When the game App initializes LVB process, we first enter into the UI extension. Here, you can customize the interface according to your product demand. If you are required to log in to the LVB software, you'd better first check the login status here, because interfaces cannot be displayed during LVB.

When users confirm to initialize LVB, the UI extension can launch the LVB extension and attach certain custom parameters. Sample code for launching LVB extension is provided below

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

### Step 2: Create a push object

The project template has already provided a basic framework for the LVB extension. You simply need to add the following code before SampleHandler.m

```objective-c
#import "SampleHandler.h"
#import "TXRTMPSDK/TXLiveSDKTypeDef.h"
#import "TXRTMPSDK/TXLivePush.h"
#import "TXRTMPSDK/TXLiveBase.h"
static TXLivePush *s_txLivePublisher;
```

s_txLivePublisher is the object we use for the push. The best location for instantiating s_txLivePublisher is in the `-[SampleHandler broadcastStartedWithSetupInfo:]` method. After starting the pusher, the UI extension will call back this function and start LVB process.

```objective-c
- (void)broadcastStartedWithSetupInfo:(NSDictionary<NSString *,NSObject *> *)setupInfo {
    if (s_txLivePublisher) {
        [s_txLivePublisher stopPush]; // End the previous push before starting the next one
    }
    
    TXLivePushConfig* config = [[TXLivePushConfig alloc] init];
    config.customModeType |= CUSTOM_MODE_VIDEO_CAPTURE;
    config.autoSampleBufferSize = YES;
    
    config.customModeType |= CUSTOM_MODE_AUDIO_CAPTURE;
    config.audioSampleRate = 44100;
    config.audioChannels   = 1;
    
    s_txLivePublisher = [[TXLivePush alloc] initWithConfig:config];
    NSString *pushUrl = setupInfo[@"endpointURL"]; // setupInfo is from the UI extension
    [s_txLivePublisher startPush:pushUrl];  
}
```

You cannot use default configuration for the "config" of s_txLivePublisher. You need to customize video and audio capture configuration. For more information on how to set custom capture and how it works, see the "RTMP Push - Advanced Application" section in Tencent Cloud documentation.

> https://cloud.tencent.com/doc/api/258/6458

Enable autoSampleBufferSize for videos. Once this option is enabled, you will not need to worry about the resolution of the push, and the SDK will set the encoder automatically based on the input resolution. If you disable this option, you will need to customize the resolution.

> It is recommended to enable autoSampleBufferSize to achieve optimal performance. This also eliminates your need to select landscape or portrait mode.

### Step 3: Customize resolution

You can specify any resolution if you don't want to use the output resolution of the screen. The SDK will adjust the video size based on the resolution you specified

```objective-c
// Specify 640*360
config.autoSampleBufferSize = NO;
config.sampleBufferSize = CGSizeMake(640, 360);
```

### Step 4: Send a video

ReplayKit transfers both the audio and video to`-[SampleHandler processSampleBuffer:withType]` though callback

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

Video sampleBuffer can be sent simply by calling the `-[TXLivePush sendVideoSampleBuffer:]`.

The distribution frequency of sampleBuffer by the system is not fixed. If the screen remains static, it will probably take a long time before a frame of data is sent. Given this situation, the SDK implements the frame interpolation logic internally to reach the frame rate (20 fps by default) set in config.

### Step 5: Send an audio

Audio is also sent to LVB extension through `-[SampleHandler processSampleBuffer:withType]`. The difference is that there are two channels of data for audio. One channel comes from inside the App, and the other comes from the microphone.

```objective-c
    switch (sampleBufferType) {
        case RPSampleBufferTypeAudioApp:
            // Audio from inside the App
            [s_txLivePublisher sendAudioSampleBuffer:sampleBuffer withType:sampleBufferType];
            break;
        case RPSampleBufferTypeAudioMic:
        {
            // Send the audio data from Mic
            [s_txLivePublisher sendAudioSampleBuffer:sampleBuffer withType:sampleBufferType];
        }
            break;
    }
```

Sending two channels of data at the same time is supported by the SDK. The data will be mixed internally. Generally, sending two channels of data is needed only when the user plugs in the earphone. Otherwise, it is recommended that only the voice data of Mic is to be sent.

You may disable the microphone during screen recording. The RPSampleBufferTypeAudioMic data cannot be received in this case.

### Step 6: Pause and resume

The current LVB can be paused in game Apps. The extension program will not receive data until the user resumes the LVB. In custom capture mode, the SDK requires continuous external data source; otherwise the server will disconnect the LVB due to not receiving data for a long time.

The frame interpolation logic for video is provided in the SDK. The last frame of data will be resent when there is no video. Calling `-[TXLivePush setSendAudioSampleBufferMuted:]` is needed to pause audio. The SDK will send mute data automatically.

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

### Step 7: SDK event handling

#### Event listening

You need to configure the "delegate" attribute of `TXLivePush` for SDK event listening. This delegate follows `TXLivePushListener` protocol. Underlying events will be called back through the `-(void) onPushEvent:(int)EvtID withParam:(NSDictionary*)param` API.

Due to system restrictions, LVB extension cannot trigger interface action, and thus cannot actively inform the user of a push exception. Usually, the following events will be received during screencap.

#### Normal events

| Event ID | Value | Description |
| --------------------- | ---- | -------------------- |
| PUSH_EVT_CONNECT_SUCC | 1001 | Successfully connected to Tencent Cloud push server      |
| PUSH_EVT_PUSH_BEGIN   | 1002 | Handshake with the server completed, everything is OK, ready to start push |

Usually no action is needed for normal events.

#### Error events

| Event ID | Value | Description |
| ------------------------------- | ----- | -------------------------------- |
| PUSH_ERR_VIDEO_ENCODE_FAIL | -1303 | Video encoding failed |
| PUSH_ERR_AUDIO_ENCODE_FAIL | -1304 | Audio encoding failed |
| PUSH_ERR_UNSUPPORTED_RESOLUTION | -1305 | Unsupported video resolution |
| PUSH_ERR_UNSUPPORTED_SAMPLERATE | -1306 | Unsupported audio sampling rate |
| PUSH_ERR_NET_DISCONNECT | -1307 | Network disconnected. Three failed reconnection attempts have been made. Restart the push for more retries. |

Video encoding failure does not affect push process directly. The SDK will handle it to ensure success of the subsequent video encoding.

#### Warning events

| Event ID | Value | Description |
| --------------------------------- | ---- | ------------------------------- |
| PUSH_WARNING_NET_BUSY | 1101 | Poor network connection: data upload is blocked because upstream bandwidth is too small |
| PUSH_WARNING_RECONNECT | 1102 | Network disconnected, automatic reconnection has started (auto reconnection will be stopped if it fails for three successive times) |
| PUSH_WARNING_HW_ACCELERATION_FAIL | 1103 | Failed to start hardware encoding. Software encoding is used |
| PUSH_WARNING_DNS_FAIL | 3001 | RTMP - DNS resolution failed (this will trigger retry process) |
| PUSH_WARNING_SEVER_CONN_FAIL | 3002 | Failed to connect to the RTMP server (this will trigger retry process) |
| PUSH_WARNING_SHAKE_FAIL | 3003 | RTMP server handshake failed (this will trigger retry process) |
| PUSH_WARNING_SERVER_DISCONNECT | 3004 | The RTMP server disconnected automatically (this will trigger retry process) |

A warning event indicates that the server has encountered some internal problems, but they will not affect the push.

> For the definition of all events, see the header file: **"TXLiveSDKEventDef.h"**

### Step 8: End push

To end the push, Replay Kit will call the `-[SampleHandler broadcastFinished]`. Sample code is provided below

```objective-c
- (void)broadcastFinished {
    // User has requested to finish the broadcast.
    if (s_txLivePublisher) {
        [s_txLivePublisher stopPush];
        s_txLivePublisher = nil;
    }
}
```

The LVB extension process may be recovered by the system after a push, make sure to perform proper cleanup work.
