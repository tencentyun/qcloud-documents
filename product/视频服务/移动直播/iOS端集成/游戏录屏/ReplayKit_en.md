
## Overview

Screencap is a feature newly introduced in iOS 10. Based on the ReplayKit screencap video save feature on iOS 9, Apple added real-time video stream LVB feature. For official introduction, see [Go Live with ReplayKit](http://devstreaming.apple.com/videos/wwdc/2016/601nsio90cd7ylwimk9/601/601_go_live_with_replaykit.pdf).

The screencap process is divided into two sections: Game App and LVB App. When screen capping on iOS, the system does not directly run the LVB App. Instead, the LVB App provides service for the game App in the form of an extension. There are two extensions. One is used to display custom interface, which displays user information and allows the user to enter titles and so on. When the user taps on the OK button, the system switches to the other extension to send screen data. This extension cannot display UI. The structure of the entire screencap LVB process is shown below.

![1](//mc.qcloudimg.com/static/img/8e2f3b74b9c1f2d93feb8ef403042fd8/image.png)

As an extension, Broadcast Upload has its own process. To ensure system performance, iOS systems allocate less resource to extensions, and extensions that occupy too much memory will be killed. Based on the high quality, low latency of the original LVB feature, Tencent Cloud RTMP SDK further reduced system resource usage to ensure extension stability.

## Try out the Feature

The recording process can only be completed when screencap is supported by both the game and LVB software. For the LVB software, it is recommended that you use our "Mini LVB". Download link
![2](//mc.qcloudimg.com/static/img/721f68e5ebb0779d2b14a97de40b0121/image.png)

As iOS 10 becomes widely used, the number of games that support screencap is increasing as well. If you have no games that support screencap, you can download the game called "War of Tanks", touch the LVB option above and select "Mini LVB" to start screencap.
![3](//mc.qcloudimg.com/static/img/84ded1555fb546da6652491f4ef71183/image.png)


## Development Environment Preparation

### Xcode Preparation

Screencap LVB is a new feature provided by iOS 10, so you'll need Xcode 8 or higher version, and the mobile phone must be upgraded to iOS 10 or above. Screencap is not supported on a simulator.

### Create LVB Extension

In the current project, select "New" -> "Target...", and then "Broadcast Upload Extension", as shown in the figure

![4](//mc.qcloudimg.com/static/img/9d18eb52c817ba14bbd707be56adb84c/image.png)

Configure Product Name. Remember to check "Include UI Extension". Click "Finish" and you will see two more directories and two more targets, LVB extension and UI extension, added to the project.

![5](//mc.qcloudimg.com/static/img/6712032a19170ea7725ae8b445c7dddc/image.png)

The Replay Kit of iOS 10 supports two LVB modes

1. The video and audio are encoded into a short mp4 file and handed over to the LVB extension
2. The original screen and audio data is handed over to the extension

The first mode has high latency and poor flexibility but the extension App doesn't have to be concerned with encoding issues; while the second mode allows you to customize what you send and has high configurability. Currently, the SDK only supports the second mode. Since Xcode uses the first mode by default, you need to modify the Info.plist of the LVB extension as shown in the figure

![6](//mc.qcloudimg.com/static/img/bc86b68eb7c88ceb989c8b059ce41472/image.png)

### Import RTMP SDK

You need to import TXRTMPSDK.framework for the LVB extension. Importing framework to extension is the same as importing framework to main App, and dependent system libraries for the SDK are also the same. For more information, please see "[Project Configuration (iOS)](https://cloud.tencent.com/document/product/454/7876)" on the official Tencent Cloud website.


## Interfacing Process

### Step 1:  Write UI Extension

When the game App initializes LVB process, we first enter the UI extension. Here, you can customize the interface according to your product demand. If you are required to log in to the LVB software, you'd better first check the login status here, because interfaces cannot be displayed during LVB.

When the user confirms to initialize LVB, the UI extension can launch the LVB extension and attach certain custom parameters. Sample code for launching LVB extension is provided below

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

### Step 2:  Create Push Object

The project template has already provided a basic framework for the LVB extension. You simply need to add the follow code before SampleHandler.m

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

You cannot use default configuration for the "config" of s_txLivePublisher. You need to customize video and audio capture configuration. For more information on how to set custom capture and how it works, please see the "[RTMP Push - Advanced Operation](https://cloud.tencent.com/document/product/454/7884)" section in Tencent Cloud documentation.

Enable autoSampleBufferSize for videos. Once this option is enabled, you will not need to worry about the resolution of the push, and the SDK will set the encoder automatically based on the input resolution. If you disable this option, you will need to customize the resolution

> It is recommended to enable autoSampleBufferSize to achieve optimal performance. This also eliminates your need to select landscape or portrait mode.

### Step 3:  Customize Resolution

You can specify any resolution if you don't want to use the output resolution of the screen. The SDK will adjust the video size based on the resolution you specified

```objective-c
// Specify 640*360
config.autoSampleBufferSize = NO;
config.sampleBufferSize = CGSizeMake(640, 360);
```

### Step 4:  Send Video

Replay Kit transfers both the audio and video to`-[SampleHandler processSampleBuffer:withType]` though callback

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

### Step 5:  Send Audio

Audio is also sent to LVB extension through `-[SampleHandler processSampleBuffer:withType]`. The difference is that there are two channels of data for audio. One channel comes from inside the App, and the other comes from the microphone.

```objective-c
    switch (sampleBufferType) {
        case RPSampleBufferTypeAudioApp:
            // Audio from inside the App
            
            break;
        case RPSampleBufferTypeAudioMic:
            // Audio from Mic.
        {
        	// Send the audio data from Mic
            [s_txLivePublisher sendAudioSampleBuffer:sampleBuffer];
        }
            break;
	}
```

Sending two channels of data at the same time is not supported by the SDK. You need to select which audio to use as needed.

### Step 6:  Pause and Resume

The current LVB can be paused in game Apps, which will prevent Samples buffer from being distributed to the LVB extension, till the user resumes the LVB. In custom capture mode, the SDK requires continuous external data source; otherwise the server will disconnect the LVB due to not receiving data for a long time.

The frame interpolation logic for video is provided in the SDK. The last frame of data will be resent when there is no video. However, no frame interpolation logic is provided for audio, video and audio will go out of sync if no data is provided for SDK. You can use the following simple code to send mute data to the SDK during a pause.

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

### Step 7:  SDK Event Handling

#### Event Listening

You need to configure the "delegate" attribute of `TXLivePush` for SDK event listening. This delegate follows `TXLivePushListener` protocol. Underlying events will be called back through the `-(void) onPushEvent:(int)EvtID withParam:(NSDictionary*)param` API.

Due to system restrictions, LVB extension cannot trigger interface action, and thus cannot actively inform the user of a push exception. Usually, the following events will be received during screencap.

#### Normal Events

| Event ID                  | Value   | Description                 |
| --------------------- | ---- | -------------------- |
| PUSH_EVT_CONNECT_SUCC | 1001 | Successfully connected to Tencent Cloud push server      |
| PUSH_EVT_PUSH_BEGIN   | 1002 | Handshake with the server completed, everything is OK, ready to start push |

Usually no action is needed for normal events.

#### Error Events

| Event ID                            | Value    | Description                             |
| ------------------------------- | ----- | -------------------------------- |
| PUSH_ERR_VIDEO_ENCODE_FAIL      | -1303 | Video encoding failed                           |
| PUSH_ERR_AUDIO_ENCODE_FAIL      | -1304 | Audio encoding failed                           |
| PUSH_ERR_UNSUPPORTED_RESOLUTION | -1305 | Unsupported video resolution                        |
| PUSH_ERR_UNSUPPORTED_SAMPLERATE | -1306 | Unsupported audio sampling rate                        |
| PUSH_ERR_NET_DISCONNECT          | -1307 | Network disconnected. Reconnection attempts have failed for three times, thus no more retries will be performed. Please restart the push manually |

Video encoding failure does not affect push process directly. The SDK will handle it to ensure success of the subsequent video encoding.

#### Warning Events

| Event ID                              | Value   | Description                            |
| --------------------------------- | ---- | ------------------------------- |
| PUSH_WARNING_NET_BUSY            | 1101 | Bad network condition: data upload is blocked because uplink bandwidth is too small            |
| PUSH_WARNING_RECONNECT           | 1102 | Network disconnected, automatic reconnection has started (auto reconnection will be stopped if it fails for three times) |
| PUSH_WARNING_HW_ACCELERATION_FAIL | 1103 | Failed to start hardware encoding. Software encoding is used                   |
| PUSH_WARNING_DNS_FAIL            | 3001 |  RTMP - DNS resolution failed (this will trigger retry process)        |
| PUSH_WARNING_SEVER_CONN_FAIL     | 3002 | Failed to connect to the RTMP server (this will trigger retry process)            |
| PUSH_WARNING_SHAKE_FAIL          | 3003 | RTMP server handshake failed (this will trigger retry process)            |
| PUSH_WARNING_SERVER_DISCONNECT      |  3004 |  The RTMP server actively disconnected (this will trigger retry process)  |

A warning event indicates that the server has encountered some internal problems, but they will not affect the push.

> For the definition of all events, see the header file: **"TXLiveSDKEventDef.h"**

### Step 8:  End Push

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
