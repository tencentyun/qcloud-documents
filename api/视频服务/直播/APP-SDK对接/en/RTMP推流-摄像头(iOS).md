
## Introduction to RTMP SDK
Tencent Cloud RTMP SDK is a set of RTMP standard LVB solutions developed and launched by Tencent, providing three features, **RTMP Push**, **LVB** and **VOD**. They incorporate years of technical accumulation of the Tencent audio/video team, and many optimizations in video compression, hardware acceleration, beauty filters, audio noise reduction, bit rate control, and so on.

For users new to LVB, it takes only a few lines of codes to complete the interworking process. For users with enough technical knowledge, the rich configuration APIs that the SDK provides also allow you to customize the configuration that best satisfies your demands.

![rtmp sdk push](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/tx_cloud_push_sdk_struct.jpg)

## Downloading RTMP SDK
Go to [SDK Download](https://www.qcloud.com/doc/api/258/6172#.E7.A7.BB.E5.8A.A8.E7.AB.AFsdk), and find the SDK package for your platform. The package contains the SDK body and Demo code. Run it on Xcode ([Engineering Configuration (iOS)](https://www.qcloud.com/doc/api/258/5320)) and you'll see the following.
![demo](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/pusher_demo_introduction_2.jpg)

> **x86 Simulator Debugging**
> Since the RTMP SDK uses a lot of advanced features of iOS, we cannot ensure that all the features can run normally under the simulator in the x86 environment. Furthermore, audio and video are performance sensitive features, the performance under the simulator will be greatly different from that under a real phone. Therefore, it is recommended to preferably use a real phone for debugging if possible.

## Interworking Guide
The guide mainly targets the **camera LVB**solution, which is mainly used for beauty show LVB, personal LVB and event LVB and other scenarios.

### Step 1:  Creating a Push object
At first, we need to create a **LivePush** object.

But before you create a LivePush object, you need to specify a **LivePushConfig**object, which is used to determine the configuration parameters of various LivePush aspects, such as push resolution, frames per second (FPS) and GOP (seconds per one I-frame).

After alloc, LivePushConfig is equipped with some parameters that we have repeatedly adjusted. If you do not need to customize these configurations, allocate them simply and insert them into the LivePush object.  If you have experience on relevant fields and want to adjust the default configuration, you can read the content of **Advanced**.

```objectivec   
// Create the LivePushConfig object, which is initialized to the basic configuration by default
 TXLivePushConfig* _config = [[TXLivePushConfig alloc] init];    
 //In _config, you can perform some initialization operations on push parameters (e.g., whitening, hardware acceleration, front/rear camera, etc.). Note that _config cannot be nil  
 _txLivePush = [[TXLivePush alloc] initWithConfig:  _config];
```

### Step 2:  "Looking for a piece of land" for the picture
Next we need to look for a place to display the video frames of camera. In the iOS, view is used as the basic interface rendering unit. Therefore, you only need to prepare a **startPreview** API function transferred by view to the LivePush object.

- **Recommended layout!**
> Actually, in the RTMP SDK, the picture is not directly rendered to the view provided by you, but a subView used for OpenGL rendering is created on this view. However, the size of this subView used for rendering will be adjusted automatically according to the size change of the view provided by you.
>![](//mccdn.qcloud.com/static/img/75b41bd0e9d8a6c2ec8406dc706de503/image.png)
>
> But even so, if you want to implement UI controls like bullet screen and flower presenting on the rendering picture, we recommend you to recreate a view at the same level so as to avoid a lot of problems of picture covering.

- **How to make animation?**
> Animation can be made for view freely, but note that the target attribute modified for the animation here should be the <font color='red'>transform</font> attribute, instead of the frame attribute.
>
```objectivec
  [UIView animateWithDuration:0.5 animations:^{
            _myView.transform = CGAffineTransformMakeScale (0.3, 0.3); // Shrinks by 1/3
        }];
```

### Step 3:  Start push
After the preparations in Step 1 and Step 2, you can start push with the following codes: 

```objectivec 
NSString* rtmpUrl = @"rtmp://2157.livepush.myqcloud.com/live/xxxxxx";    
[_txLivePush startPreview:_myView];  //_myView is the view to be specified by you in step 2    
[_txLivePush startPush:rtmpUrl];
```

- **startPush** aims to inform the RTMP SDK of the URL to which the audio and video stream will be pushed.
- The parameter of **startPreview** is the view you need to specify in step 2; startPreview is used to associate the interface view control with the LivePush object, thus rendering the picture collected by the mobile phone camera to the screen.

### Step 4:  Beauty filters
For the camera LVB scenario, the beauty filter is an essential function. The SDK provides a simple version of implementation, including retouching (level 1 -> level 10) and whitening (level 1 -> level 3) two features.

You can use the slider and other controllers in the user interface of your APP to allow users to choose beauty effects. Or it is recommended that you first use the slider in the Demo to achieve your desired results, and then fix these values to your App's parameters.

The API function setBeautyFilterDepth can adjust the beauty and whitening levels dynamically:

```objectivec
[_txLivePush setBeautyFilterDepth:_beauty_level setWhiteningFilterDepth:_whitening_level];
```

### Step 5:  Camera control
-**Switch front or rear camera** 
The **front** camera is used by default (this default value can be changed by modifying the configuration option frontCamera of LivePushConfig), and it is switched each time switchCamera is invoked. Note to ensure that both the LivePushConfig and LivePush objects have been initialized before the camera is switched.  
  
```objectivec
//The front camera is used by default (this default value can be changed by modifying the configuration option frontCamera of LivePushConfig)   
[_txLivePush switchCamera];
```

-**Turn on or off the flash** 
The flashlight can be turned on for the rear camera only (you can confirm whether the current camera is the front one or rear one according to the frontCamera member in "TXLivePush.h").

```objectivec
if(!frontCamera) {
	BOOL bEnable = YES;
	//When bEnable is YES, the flashlight is turned on; when bEnable is NO, the flashlight is turned off
	BOOL result = [_txLivePush toggleTorch: bEnable];
	//when result is YES, it is turned on successfully; when result is NO, it cannot be turned on
}
```

- **Customize Manual Focus**
The default manual focus logic is provided in the iOS version of RTMP SDK. Although no problem is found with this function, it cannot work frequently because the touch event of the screen is preempted. Meanwhile, we must not intervene in free interface arrangement in principle.
A setFocusPosition function API is added to TXLivePush of the new version. You can perform manual focus according to the finger touch position.

```objectivec
// If the customer invokes this API, the focus trigger logic in the SDK will stop, avoiding repeated trigger of the focus logic
- (void)setFocusPosition:(CGPoint)touchPoint;
```

### Step 6:  Set logo watermarks
Recently related policies require that LVB videos must be marked with watermarks. We now focus on this function that does not seem particularly important before:
Tencent Cloud supports two watermark settings: one is set in the push SDK settings. The principle is that videos are marked with watermarks in the SDK before being encoded. Another way is to mark watermarks at the cloud end. That is, the cloud end resolves videos and add Logo watermarks.

We suggest that you </font>add watermarks with the SDK<font color = 'red'>, because there are three obvious problems with watermarking at the cloud end:
 (1) This is a cloud machine-consuming service and is not free, which will increase your cost.
 (2) It is not ideally compatible with resolution switching in the push process and other situations and blurred screen may occur.
 (3) It may cause an additional 3s of video delay, which is the result of transcoding.

The SDK requires png watermark pictures, because they have transparency information, which conduces to solving jagged pictures and other problems. (Do not just change the extension of jpg pictures to png in Windows. Professional png pictures need to be processed by professional art designer)

```objectivec
//Set video watermarks
_config.watermark = [UIImage imageNamed:@"watermark.png"];
_config.watermarkPos = (CGPoint){10, 10};
```

### Step 7:  Hardware acceleration
Hardware encoding can be enabled through the **enableHWAcceleration** API in LivePushConfig.
```objectivec
//Stop push (it is recommended to restart push in the enabling process, otherwise problems such as blurred/green screen may occur at the play end)
[_txLivePush stopPush]
//Enable hardware encoding
txLivePush.config.enableHWAcceleration = YES;
//Restart push
[_txLivePush startPush:rtmpUrl]
```

- **Recommended to Enable Hardware Encoding**
The model quantity of iOS platform is not as large as that of Android platform, and its hardware quality is also highly reliable, so hardware acceleration is strongly recommended on the iOS platform and can be enabled safely.

- **The Latest Beauty Effect**
A lot of customers are unsatisfied with the beauty effect of the SDK of old version, so we started to use the new beauty solution from SDK 1.6.2, but the new beauty algorithm requires slightly more computation. Since the test team has very strict and rigorous performance standard requirements, we finally determined as follows: <font color='red'>The new beauty effect will be enabled only when hardware acceleration is enabled</font>.
  
- **Avoid Midway Switching**
Avoid enabling/disabling hardware acceleration during push. Although no problem occurs in most cases, various hidden troubles of exceptions exist. One recommended method is to enable hardware acceleration in the very beginning, instead of enabling it midway.

> A protection mechanism is provided in the RTMP SDK: If the hardware acceleration resource is occupied by other Apps and cannot be enabled, it will be switched back to software encoding automatically.

### Step 8:  Backend push
In the conventional mode, once the App switches to the Backend, the camera's capture ability is disabled by the Android system, which means that the SDK can no longer continue to capture and encode audio/video data. If we do nothing, then the following will happen:
+ Phase 1 (from background switching -> within 10s after that) - Since the CDN does not have data, it cannot provide video streaming to the audience, and the picture seen by the audience does not response.
+ Phase 2 (10s -> 70s) - The player at the audience side exits because it cannot receive the live stream continuously, and nobody is in the studio.
+ Phase 3 (70s later) - The RTMP link of push is directly disconnected by the server. The VJ needs to restart LVB to continue.

Even when the VJ answer a short emergency call, the interactive experience will obviously make all viewers to leave the studio. How can we optimize it?
We introduced a solution from **SDK 1.6.1**. Set out below is the effect that can be achieved by this solution from the visual angle of the audience end: 
![](//mc.qcloudimg.com/static/img/6325a9f7918602bd8db15228e6ffe189/image.png)

-**8.1) Set pauseImg**
Before push, use the  pauseImg API of LivePushConfig to set a waiting picture. The recommended meaning of the picture is as follows: "The VJ will leave for a while and come back later".

- **8.2) Setting Background Running (momently) of App**
The App will become dormant thoroughly if it is switched to the background, and the RTMP SDK is helpless despite the powerful function. Therefore, we use the following code to enable the App to run for several more minutes after being switched to the background. Our purpose is basically achieved if the VJ can cope with the emergency call in the short period of time.

```objectivec
//Withdraw the message notification after registration
[[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(handleEnterBackground:) 
    name:UIApplicationDidEnterBackgroundNotification object:nil];

//Invoke beginBackgroundTaskWithExpirationHandler after receiving the notification
-(void)handleEnterBackground:(NSNotification *)notification
{
    [[UIApplication sharedApplication] beginBackgroundTaskWithExpirationHandler:^{
    }];
}
```
-**8.3) Switch to backend processing**
If the App is switched to the background during push,namely, the pausePush API function of TXLivePush is invoked in handleEnterBackground of 8.2, pauseImg you set just now can be used to continue push although the RTMP SDK cannot collect the camera pictures after that.

```
//Switch to the background for handling:  Supplement one sentence on the basis of 8.2
- (void)handleEnterBackground:(NSNotification *)notification
{
    [[UIApplication sharedApplication] beginBackgroundTaskWithExpirationHandler:^{
    }];
	[_txLivePush pausePush];
}
```

-**8.4) Switch to frontend processing**
 After the App is switched back to the frontend and the resumePush API function of TXLivePush is invoked, the RTMP SDK will continue to collect camera pictures to implement push.
 
```objectivec
//Switch to the frontend for handling
- (void)handleEnterForeground:(NSNotification *)notification
{
    [_txLivePush resumePush];
}
```

### Step 9:  Recommended definition
The video quality is affected by **resolution**, **frame rate** and **bit rate**.
-**Resolution**: The camera LVB has three options of 9:16 conventional resolution: 360\*640, 540\*960, 720\*1280.
-**Frame rate**: If FPS <= 10, viewers will obviously feel lagging. 20 FPS is recommended for camera LVB.
-**Bit rate**: Means the data volume coded by the encoder every second, in units of kbps. For example, 800 kbps means that the encoder will generate 800 kb (or 100 KB) data per second.

Good quality is the result of balance between resolution, frame rate and bit rate. The following are recommended settings for several definition options. Here, the corresponding setting option of LivePushConfig is marked in the brackets:

| Step   | Resolution (videoResolution) | FPS(videoFPS) | Bit Rate (videoBitratePIN) |
|---------|---------|---------|---------|
| SD | VIDEO_RESOLUTION_TYPE_360_640 | 20 | 700 kbps |
| HD | VIDEO_RESOLUTION_TYPE_540_960 | 20 | 1000 kbps | 
| Super definition | VIDEO_RESOLUTION_TYPE_720_1280 | 20 | 1500 kbps |

For beauty show LVB, our clients generally choose **HD**, because it is rather balanced: 720p super definition is wasteful for human figures, while 360p cannot make it stand out from other competing products in terms of definition.

### Step 10:  Remind the VJ of "Busy network"
Step 13 will introduce solving RTMP SDK push events. **PUSH_WARNING_NET_BUSY** is very useful, which means: <font color = 'blue'>** the uplink network of the current VJ is busy, and lagging occurs in the viewer end.** </font>

When you receive this WARNING, you can remind through the UI the VJ of changing the network egress, or moving closer to the WiFi. Or you say to him: "Dear, I am using LVB. Do not visit the Taobao website!" What? Not visit Taobao? Then you must be watching Korean TV dramas. "

### Step 11:  Landscape push
In most cases, users often shoot portrait LVB programs and watch portrait videos. Sometimes LVB may need a wider angle, users have to shoot landscape videos and viewers are expected to watch landscape videos. Then portrait push is required. The following two sketches show the effects of landscape shooting and portrait shooting at the viewer end.
![](//mc.qcloudimg.com/static/img/cae1940763d5fd372ad962ed0e066b91/image.png)
><Font color = 'red'>**Note:**</font> In landscape push and portrait push, viewers see pictures of different aspect ratios: 9:16 for portrait and 16: 9 for landscape.

To implement push of horizontal screen, set two places:
#### Adjusting performance at the viewer end
The **homeOrientation** setting option in LivePushConfig needs to be configured. It controls the video aspect ratio seen at the audience end to **16:9** or **6:19**. The adjusted result can be viewed using the player to see whether it meets the expectation.

| Configuration item | Description |
|:---------|---------|
| VIDEO_ANGLE_HOME_RIGHT | Home key on the right
| VIDEO_ANGLE_HOME_DOWN | Home key at the bottom |
| VIDEO_ANGLE_HOME_LEFT | Home key on the left |
| VIDEO_ANGLE_HOME_UP | Home key at the top |

#### Adjusting performance at the VJ end
Next we need to see whether the local rendering of the VJ is normal. Here, the setRenderRotation API in TXLivePush can be used to set the rotation direction of the picture seen by the VJ.  This API provides the four parameters of ** 0, 90, 180, and 270** used to set the rotation angle.

### Step 12:  Background mixing
Background remix was supported from RTMP SDK 1.6.1. The VJ may wear a headset or not wear it. The background remix function can be implemented through the following group of APIs in TXLivePush:

| API | Description |
|---------|---------|
| playBGM | Sends a song via the path. In [Small LVB Demo](https://www.qcloud.com/doc/api/258/6164), we obtain a music file from the iOS local media library |
| stopBGM | Stops playing background music
| pauseBGM | Suspends playing background music
| resumeBGM | Resumes playing background music |
| setMicVolume | Sets the volume of the microphone when mixing. It is recommended to implement a slider in the corresponding UI, for the VJ to set the volume |
| setBGMVolume | Set the volume of the background music when mixing. It is recommended to implement a slider in the corresponding UI, for the VJ to set the volume |

### Step 13:  Solve the problem
#### Event listening
The RTMP SDK listens push related events using the TXLive <font color = 'red'> Push </font> Listener proxy. Note that the TXLive <font color = 'red'> Push </font> Listener only listens the push events with the <font color = 'Red'> PUSH_ </font> prefix.

#### Regular events 
Events notified for every successful push task. For example, event 1003 means that the system is about to render the camera pictures

| Event ID                 ||    Value  |  Description                    |   
| :-------------------  |:-------- |  :------------------------ | 
| PUSH_EVT_CONNECT_SUCC | 1001 | Successfully connected to Tencent Cloud push server |
| PUSH_EVT_PUSH_BEGIN              |  1002 | Handshaking with the server completed, everything is OK, ready to start push |
| PUSH_EVT_OPEN_CAMERA_SUCC | 1003 | The pusher has successfully started the camera (it takes 1-2 seconds on some Android phones) | 

####  Error Codes 
The push task cannot continue for the SDK found some serious problems: for example, you disable the APP's camera permission and the camera does not start.

| Event ID                 ||    Value  |  Description                    |   
| :-------------------  |:-------- |  :------------------------ | 
| PUSH_ERR_OPEN_CAMERA_FAIL        | -1301 | Failed to start the camera |
| PUSH_ERR_OPEN_MIC_FAIL           | -1302 | Failed to start the microphone |
| PUSH_ERR_VIDEO_ENCODE_FAIL       | -1303 | Video coding failed |
| PUSH_ERR_AUDIO_ENCODE_FAIL        -1304 | Audio coding failed |
| PUSH_ERR_UNSUPPORTED_RESOLUTION  | -1305 | Video resolution not supported |
| PUSH_ERR_UNSUPPORTED_SAMPLERATE  | -1306 | Audio sampling rate not supported |
| PUSH_ERR_NET_DISCONNECT          | -1307 | Disconnected from the network, and 3 reconnection attempts fail. Please push again |

#### Warning events 
SDK found some problems which is not incurable. Most warning events will trigger some retrial protection logics or recovery logics, and in most cases the problems can be recovered. Do not make a fuss.

- PUSH_WARNING_NET_BUSY
The VJ network is busy. If you want to remind the VJ via the UI, this warning event is relatively useful (step10).

- PUSH_WARNING_SERVER_DISCONNECT
The push request is rejected by the backend, which will trigger a limited number of retrial logics. The push task may succeed in a retrial. But the truth is that in most scenarios it is because the txSecret in the push address is miscalculated, or because the test address is occupied by others. This warning event is conducive to your debugging.

| Event ID                 ||    Value  |  Description                    |   
| :-------------------  |:-------- |  :------------------------ | 
| PUSH_WARNING_NET_BUSY            | 1101 | Busy network: too small uplink bandwidth, uploading data blocked |
| PUSH_WARNING_RECONNECT           | 1102 | Disconnected from the network, automatic reconnection has started (no retrial after three consecutive automatic reconnections) |
| PUSH_WARNING_HW_ACCELERATION_FAIL |  1103 | Failed to start hard coding, so soft coding is used |
|PUSH_WARNING_DNS_FAIL			  |  3001 |  RTMP -DNS resolution failed (it will trigger the retrial process) |
|PUSH_WARNING_SEVER_CONN_FAIL     |  3002|  Failed to connect the RTMP server (it will trigger the retrial process) |
|PUSH_WARNING_SHAKE_FAIL          |  3003|  RTMP Server Handshaking failed (it will trigger the retrial process) |
|PUSH_WARNING_SERVER_DISCONNECT      |  3004|  The RTMP server is actively disconnected (it will trigger the retrial process) |

>For the definitions of all events, please refer to the header file: **"TXLiveSDKTypeDef.h"**.

### Step 14:  Push ends
It is very simple to end push, but proper cleaning work is needed. Since only one TXLivePush object used for push can run at the same moment, improper cleaning work will lead to adverse effect on the next time of LVB.
```objectivec
/ / The push task is completed. Do clearing work
- (void)stopRtmpPublish {
    [_txLivePush stopPreview];
    [_txLivePush stopPush];
    _txLivePush.delegate = nil;
}
```

