
## Overview

The screencap function is a feature newly launched by iOS 10. Apple added the real-time LVB function of video streaming based on screencap video saving of ReplayKit on iOS 9. For the official introduction, see [Go Live with ReplayKit](http://devstreaming.apple.com/videos/wwdc/2016/601nsio90cd7ylwimk9/601/601_go_live_with_replaykit.pdf).

The entire screencap flow consists of two parts: game App and LVB App. The LVB App does not run directly during iOS screencap, but serves the game App in the form of extender. Two extenders are available. One is used to display the custom interface, on which the user can enter the title and display the user information. After the user touches for confirmation, the system switches to the other extender to send screen data. This extension does not have the capability of displaying UI. The figure below shows the entire LVB structure of screencap.

![1](//mc.qcloudimg.com/static/img/8e2f3b74b9c1f2d93feb8ef403042fd8/image.png)

As an extender, Broadcast Upload has an independent process. To ensure system smoothness, the iOS allocates relatively few resources to extenders. If the memory occupancy is too high, the extender will be killed. On the basis of high quality and low delay of the original LVB, the RTMP SDK of Tencent Cloud further reduces system consumption and ensures extender stability.

## Experiencing Functions

The recording flow can be completed provided that the screencap function is supported by both the games and LVB software. For the LVB software, it is recommended to use our "Little Live". URL for downloading:
![2](//mc.qcloudimg.com/static/img/721f68e5ebb0779d2b14a97de40b0121/image.png)

As the iOS 10 gets popular, the games supporting screencap also become common. If you have no games for screencap, you can download the game called "War of Tanks", touch the LVB option in the above, and select "Little Live" to start screencap.
![3](//mc.qcloudimg.com/static/img/84ded1555fb546da6652491f4ef71183/image.png)


## Development Environment Preparations

### Xcode Preparations

LVB of screencap is a new feature provided by iOS 10, so the version Xcode 8 or above is needed, and the mobile phone must be also upgraded to iOS 10 or above. The simulator cannot use the screencap feature.

### Creating LVB Extension

In the current project, select "New" -> "Target…", and then "Broadcast Upload Extension", as shown in the figure.

![4](//mc.qcloudimg.com/static/img/9d18eb52c817ba14bbd707be56adb84c/image.png)

After Product Name is configured, note to select "Include UI Extension". After you click "Finish", you can find that two more directories and two more targets are added to the project. The two targets are LVB extension and UI extension respectively.

![5](//mc.qcloudimg.com/static/img/6712032a19170ea7725ae8b445c7dddc/image.png)

The Replay Kit of iOS 10 supports two LVB modes

1. The video and audio are encoded into a short mp4 file and handed over to the LVB extension.
2. The original data of screen and audio is handed to the extension.

Mode 1 has a high delay and is not flexible, while the advantage is that the issue of encoding does not need to be considered during app extension. For mode 2, the sent content can be customized and provides a high degree of configurability. At present, the SDK supports the second mode only. Since Xcode uses mode 1 by default, the LVB extension Info.plist needs to be modified, as shown in the figure.

![6](//mc.qcloudimg.com/static/img/bc86b68eb7c88ceb989c8b059ce41472/image.png)

### Importing RTMP SDK

The LVB extension requires importing TXRTMPSDK.framework. The framework importing mode of extension is the same as the main App importing mode, and the system dependency library of SDK is also the same. For details, see Engineering Configuration (iOS) on the official website of Tencent Cloud.

> https://www.qcloud.com/doc/api/258/5320


## Interworking Process

### Step 1:  Compiling UI extension

After initiating LVB, the game App first enters the UI extension. Here, you can customize interfaces according to your product requirements. If you are required to log in to the LVB software, you'd better first check the login status here, because no interface can be displayed during LVB.

When the user confirms initialization of LVB, the UI extension can start LVB extension and attach some custom parameters. Example code for starting LVB extension is provided below:

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

### Step 2:  Creating a push object

The engineering template has already created a basic framework of LVB extension for us. Only the following code needs to be added before SampleHandler.m:

```objective-c
#import "SampleHandler.h"
#import "TXRTMPSDK/TXLiveSDKTypeDef.h"
#import "TXRTMPSDK/TXLivePush.h"
#import "TXRTMPSDK/TXLiveBase.h"
static TXLivePush *s_txLivePublisher;
```

s_txLivePublisher is the object used for push. The best position of instantiating s_txLivePublisher is in the `-[SampleHandler broadcastStartedWithSetupInfo:]` method. After starting push, the UI extension will call back this function to start LVB.

```objective-c
- (void)broadcastStartedWithSetupInfo:(NSDictionary<NSString *,NSObject *> *)setupInfo {
    if (s_txLivePublisher) {
        [s_txLivePublisher stopPush]; //End the last push before a push is started
    }
    
    TXLivePushConfig* config = [[TXLivePushConfig alloc] init];
    config.customModeType |= CUSTOM_MODE_VIDEO_CAPTURE;
    config.autoSampleBufferSize = YES;
    
    config.customModeType |= CUSTOM_MODE_AUDIO_CAPTURE;
    config.audioSampleRate = 44100;
    config.audioChannels   = 1;
    
    s_txLivePublisher = [[TXLivePush alloc] initWithConfig:config];
  	NSString *pushUrl = setupInfo[@"endpointURL"]; // setupInfo comes from the UI extension
    [s_txLivePublisher startPush:pushUrl];  
}
```

config of s_txLivePublisher cannot use the default configuration and requires setting the custom collection of video and audio. For the principle and working mode of custom collection settings, see RTMP Push - Advanced Application.

> https://www.qcloud.com/doc/api/258/6458

autoSampleBufferSize is enabled for video. After this option is enabled, there is no need to care the resolution of push, and the SDK will set the encoder automatically according to the entered resolution. If you disable this option, you need to customize the resolution.

> It is recommended to enable autoSampleBufferSize. In this way, the optimal performance can be achieved. Meanwhile, horizontal screen or vertical screen also does not need to be taken into account.

### Step 3:  Customizing resolution

If you don't want to use the output resolution of the screen, you can also specify any resolution, and zooming will be performed in the SDK according to the resolution you specified.

```objective-c
// Specify 640*360
config.autoSampleBufferSize = NO;
config.sampleBufferSize = CGSizeMake(640, 360);
```

### Step 4:  Sending video

Replay Kit will adopt the callback mode to transfer both the audio and video to`-[SampleHandler processSampleBuffer:withType]`

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

Video sampleBuffer can be sent by simply invoking `-[TXLivePush sendVideoSampleBuffer:]`.

The distribution frequency of sampleBuffer by the system is not fixed. If the screen is static, possibly a frame of data will be received after a long time. In consideration of this situation, the SDK implements the frame interpolation logic inside to reach the frame rate (20 fps by default) set for config.

### Step 5: Sending audio

Audio is also given to LVB extension through `-[SampleHandler processSampleBuffer:withType]`. The difference is that audio has two channels of data: one channel comes from the inside of App, and the other comes from the microphone.

```objective-c
    switch (sampleBufferType) {
        case RPSampleBufferTypeAudioApp:
            // Audio from the inside of App
            
            break;
        case RPSampleBufferTypeAudioMic:
            // Audio from Mic
        {
        	// Send the audio data from Mic
            [s_txLivePublisher sendAudioSampleBuffer:sampleBuffer];
        }
            break;
	}
```

SDK does not support simultaneous sending of two channels of data. You need to select the audio according to the actual condition.

### Step 6:  Pausing and resuming

The game App can pause the current LVB. Now, Samples buffer will not be distributed to the LVB extension, till the user resumes LVB. In custom collection mode, the SDK requires continuous providing of external data source; otherwise the server will disconnect LVB because data cannot be obtained for a long time.

The frame interpolation logic for video is provided in the SDK. When there is no video, the last frame of data will be resent. However, no frame interpolation logic is provided for audio. When no data is provided to the SDK, audio and video will be out of synchronization. You can use the following simple code to send mute data to the SDK in the pausing period.

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

### Step 7:  SDK event processing

#### Event Listening

SDK event listening requires setting the delegate attribute of `TXLivePush`. This delegate observes the `TXLivePushListener` protocol. The bottom-layer event will be called back through the `-(void) onPushEvent:(int)EvtID withParam:(NSDictionary*)param` API.

Due to system restriction, LVB extension cannot trigger interface action, so the user cannot be actively informed of push exception. Usually, the following events will be received during screencap.

#### Conventional Events

| Event ID                  | Value   | Description                 |
| --------------------- | ---- | -------------------- |
| PUSH_EVT_CONNECT_SUCC | 1001 | The push server of Tencent Cloud has been connected successfully      |
| PUSH_EVT_PUSH_BEGIN   | 1002 | Handshake with the server is completed with no error occurs, ready for push |

Usually the conventional event does not need to be processed.

#### Error Events

| Event ID                            | Value    | Description                             |
| ------------------------------- | ----- | -------------------------------- |
| PUSH_ERR_VIDEO_ENCODE_FAIL      | -1303 |Video encoding failure                           |
| PUSH_ERR_AUDIO_ENCODE_FAIL      | -1304 |Audio encoding failure                           |
| PUSH_ERR_UNSUPPORTED_RESOLUTION | -1305 |Video resolution not supported                        |
| PUSH_ERR_UNSUPPORTED_SAMPLERATE | -1306 |Audio sampling rate not supported                        |
| PUSH_ERR_NET_DISCONNECT         | -1307| The network is disconnected and still fails after three attempts of reconnection. Hope that this problem will be solved can be abandoned. For more retries, restart push by yourself. |

Video encoding failure will not affect push directly. The SDK will handle it to ensure success of the subsequent video encoding.

#### Warning Events

| Event ID                              | Value   | Description                            |
| --------------------------------- | ---- | ------------------------------- |
| PUSH_WARNING_NET_BUSY             | 1101 |Network conditions are poor: The uplink bandwidth is too small and the uploaded data is blocked.            |
| PUSH_WARNING_RECONNECT            | 1102 |The network is disconnected and automatic reconnection has started (up to three automatic reconnection attempts are supported). |
| PUSH_WARNING_HW_ACCELERATION_FAIL | 1103 |Hard encoding startup fails, and soft encoding is adopted.                   |
| PUSH_WARNING_DNS_FAIL             | 3001 | RTMP -DNS resolution fails (the retry flow will be triggered).          |
| PUSH_WARNING_SEVER_CONN_FAIL      | 3002 |Connection to the RTMP server fails (the retry flow will be triggered).            |
| PUSH_WARNING_SHAKE_FAIL           | 3003 |Handshake with the RTMP server fails (the retry flow will be triggered).            |
| PUSH_WARNING_SERVER_DISCONNECT      |  3004|  The RTMP server disconnects the connection actively (the retry flow will be triggered).  |

The warning event indicates that some problems occur inside, but push is not affected.

> For the definitions of all events, please refer to the header file: **"TXLiveSDKEventDef.h"**.

### Step 8: Push ends

To terminate push, Replay Kit will invoke `-[SampleHandler broadcastFinished]`. Example code is provided below:

```objective-c
- (void)broadcastFinished {
    // User has requested to finish the broadcast.
    if (s_txLivePublisher) {
        [s_txLivePublisher stopPush];
        s_txLivePublisher = nil;
    }
}
```

After push is terminated, the LVB extension process may be recovered by the system, so clearing work must be properly implemented here.