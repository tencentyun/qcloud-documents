## Basics
**Push** means pushing the collected and encoded audio/video data to your specified cloud video platform. Since the process involves a large amount of basic audio/video knowledge, you can only achieve desired results after lots of refinements and optimizations.

Tencent Video Cloud SDK mainly helps you push streams on smart phones. The SDK comes with easy-to-use APIs which can be driven by a single push URL.
![](//mc.qcloudimg.com/static/img/ca7f200c31a9323c032e9e000831ea63/image.jpg)

## Notes
- **<font color='red'>Not bound to Tencent Cloud</font>**
> The SDK is not bound to Tencent Cloud. If you want to push streams to non-Tencent Cloud addresses, please set enableNearestIP in TXLivePushConfig to NO first. If you want to push streams to Tencent Cloud addresses, set enableNearestIP to Yes. Otherwise the push quality may be affected due to inaccurate ISP DNS.

- **x86 simulator debugging**
> Since the SDK uses a great number of advanced features of the iOS system, we cannot ensure that all the features can function normally under the simulator in the x86 environment. Furthermore, audio and video are performance-sensitive features, the performance under the simulator will be greatly different from that on a real phone. Therefore, it is recommended to use an actual mobile phone for debugging if possible.

## Preparations

- **Acquiring SDK**
[Download](https://cloud.tencent.com/document/product/454/7873) SDK and follow the instructions in [Project Configuration](https://cloud.tencent.com/document/product/454/7876) to add the SDK into your application development project.

- **Acquiring a test URL**
After [activating](https://console.cloud.tencent.com/live) the LVB service, you can use [**LVB Console** -> **LVB Code Access** -> **Push Generator**](https://console.cloud.tencent.com/live/livecodemanage) to generate a push URL. For more information, please see [Acquiring Push/ Playback URL](https://cloud.tencent.com/document/product/454/7915).
![](https://mc.qcloudimg.com/static/img/64342b926e05da462a54b8ce4f8c526f/image.png)

## Code Interfacing
>This guide is specific to **camera LVB** and is mainly used for scenarios such as beauty show LVB and event LVB. For information on game LVB, please see relevant documents under this directory.

### Step 1: Create a Pusher object
Create a **LivePush** object, which will be used later to complete the push task.

Before creating a LivePush object, you need to specify a **LivePushConfig** object to determine the configuration parameters for various LivePush push phases, such as push resolution, frames per second (FPS) and GOP (seconds between I frames).

The LivePushConfig is already equipped with some parameters we have repeatedly tuned as a result of calling alloc. If you do not wish to customize these parameters, you can simply alloc and assign them to the LivePush object. If you have experience in the related field and want to adjust the default configuration, you can read the **Advanced Guide**.

```objectivec   
// Create a LivePushConfig object, which is initialized with the basic configuration by default.
 TXLivePushConfig* _config = [[TXLivePushConfig alloc] init];    
 //In _config, you can perform certain initialization operations on push parameters (e.g. whitening, hardware acceleration, and front/rear camera). Note that _config cannot be nil.  
 _txLivePush = [[TXLivePush alloc] initWithConfig: _config];
```

### Step 2: Rendering view
Next, we need to find a place to display the camera images. In iOS systems, a view is used as the basic interface rendering unit. Therefore, all you need to do is to prepare a view and pass it to the **startPreview** API function of the LivePush object.

- **Recommended layout!**
> In fact, the SDK does not directly render the images on the view you provided. Instead, it creates a subView used for OpenGL rendering upon the view. The size of this subView will be adjusted automatically according to that of the view you provided.
>![](//mccdn.qcloud.com/static/img/75b41bd0e9d8a6c2ec8406dc706de503/image.png)
>
> However, if you want to implement UI controls such as on-screen comment and flower presenting on the rendered screen, we recommend that you create another view at the same level to avoid screen overlay.

- **How to make an animation?**
> You can freely make animations for a view. But note that the target attribute modified for animations is <font color='red'>transform</font>, instead of frame.
>
```objectivec
  [UIView animateWithDuration:0.5 animations:^{
            _myView.transform = CGAffineTransformMakeScale(0.3, 0.3); //Shrink by 1/3
        }];
```

### Step 3: Start push
After completing Step 1 and Step 2, you can use the following code to start the push: 

```objectivec 
NSString* rtmpUrl = @"rtmp://2157.livepush.myqcloud.com/live/xxxxxx";    
[_txLivePush startPreview:_myView];  //_myView is the view to be specified in Step 2    
[_txLivePush startPush:rtmpUrl];
```

- **startPush** is used to tell the SDK to which push URL the audio/video streams are being pushed.
- The parameter of **startPreview** is the view you need to specify in Step 2; startPreview is used to associate the interface view control with the LivePush object, thus rendering the images collected by the mobile phone camera onto the screen.

### Step 3+: Audio-only push
For audio-only LVB scenarios, you need to update the push configuration. Perform Step 1 and Step 2 as described above. Configure audio-only push using the following code and start the push.

```objectivec
//The API only takes effect if it is called before push starts.
txLivePush.config.enablePureAudioPush = YES;   // "YES" means enabling audio-only push. Default is "NO".
[_txLivePublisher setConfig:_config];          // Reset config.

NSString* rtmpUrl = @"rtmp://2157.livepush.myqcloud.com/live/xxxxxx";      
[_txLivePush startPush:rtmpUrl];
```
If you cannot pull streams from playback URLs in rtmp, flv and hls format after enabling audio-only push, it is because the line configuration is incorrect. Submit a ticket to us and we will help you modify the configuration.

### Step 4: Configure video definition

If this is your first time to use audio-video streams, you are <font color='red'>**not recommended**</font> to set video parameters such as resolution and bitrate by yourself. This is because improper parameter configuration may have a negative effect on the final video quality. You can configure image definition for push using TXLivePusher::setVideoQuality API.

![](https://main.qcloudimg.com/raw/6e66be90ff14bb8f0603c70668a27ec8.png)

- **Recommended parameter settings**

| Application Scenario | quality |  adjustBitrate | adjustResolution |
|:-------:|:-------:|:-------:|
| Live show | VIDEO_QUALITY_HIGH_DEFINITION or <br> VIDEO_QUALITY_SUPER_DEFINITION | NO | NO |
| Mobile game LVB | VIDEO_QUALITY_SUPER_DEFINITION  | YES | YES |
| Joint broadcasting (primary screen) | VIDEO_QUALITY_LINKMIC_MAIN_PUBLISHER | YES | YES | 
| Joint broadcasting (secondary screen) | VIDEO_QUALITY_LINKMIC_SUB_PUBLISHER  | NO | NO |
| Video chat | VIDEO_QUALITY_REALTIEM_VIDEOCHAT | YES | YES | 

- **Internal data metrics**

| quality | adjustBitrate | adjustResolution | Bitrate Range | Resolution Range | 
|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
| STANDARD | YES | YES | 300~800kbps| 270x480 ~ 360x640| 
| STANDARD | YES | NO |300~800kbps|360x640| 
| STANDARD | NO | NO | 800kbps | 360x640| 
| HIGH | YES | YES |600~1500kbps| 360x640~540x960| 
| HIGH | YES | NO |600~1500kbps| 540x960| 
| HIGH | NO | NO |1200kbps| 540x960| 
| SUPER | YES | YES | 600~1800kbps|360x640~720x1280|
| SUPER | YES | NO |600~1800kbps|720x1280|
| SUPER | NO | NO |1800kbps|720x1280|
| MAIN_PUBLISHER | YES | YES |600~1500kbps| 360x640~540x960| 
| SUB_PUBLISHER | NO | NO |350kbps| 320x480| 
| VIDEOCHAT | YES | YES | 200~800kbps| 190x320~360x640| 

### Step 5: Beauty filter

![](//mc.qcloudimg.com/static/img/aac647073cf0641141900e775e929418/image.png)
- **Beauty filter**
You can set beauty filter style, dermabrasion level, whitening level, and blushing level using setBeautyStyle API. You can obtain the best video quality using beauty filter with 540 * 960 resolution (setVideoQuality - VIDEO_QUALITY_HIGH_DEFINITION):
```objectivec
//     beautyStyle     : Dermabrasion style. Smooth and Natural are supported.
//     beautyLevel     : Dermabrasion level. The values range from 0 to 9. 0 means disabling dermabrasion. A higher value means a stronger effect.
//     whitenessLevel  : Whitening level. The values range from 0 to 9. 0 means disabling whitening. A higher value means a stronger effect.
//     ruddinessLevel  : Blushing level. The values range from 0 to 9. 0 means disabling blushing. A higher value means a stronger effect.
(void)setBeautyStyle:(int)beautyStyle beautyLevel:(float)beautyLevel 
          whitenessLevel:(float)whitenessLevel ruddinessLevel:(float)ruddinessLevel;
```

- **Filter**
The setFilter API can be used to configure filter effects. A filter is actually a histogram file. Our designer group provides 8 materials which are packaged inside the Demo by default. You can use them as you like, without considering about copyright issues.

 The setSpecialRatio API is used to configure the effect level of a filter (0-1). A higher value means a stronger effect. Default is 0.5.
```objectivec
NSString * path = [[NSBundle mainBundle] pathForResource:@"FilterResource" ofType:@"bundle"];
if (path != nil && index != FilterType_None && _txLivePublisher != nil) {
        path = [path stringByAppendingPathComponent:lookupFileName];
        UIImage *image = [UIImage imageWithContentsOfFile:path];
        [_txLivePublisher setFilter:image];
} 
```
> Use PNG images if you need to customize the filters. <font color='red'> Do NOT use JPG images.</font>


### Step 6: Control the camera
- **Switch between front and rear cameras** 
The **front** camera is used by default (this can be changed by modifying the configuration option frontCamera in LivePushConfig). The camera is switched each time switchCamera is called. Make sure both LivePushConfig and LivePush objects have been initialized before you switch the camera.  
  
```objectivec
//The front camera is used by default. This can be changed by modifying the configuration option frontCamera in LivePushConfig.   
[_txLivePush switchCamera];
```

- **Turn the flashlight on or off** 
Flashlight is only available for the rear camera. (You can find out whether the front or the rear camera is used now by checking the frontCamera member in "TXLivePush.h")

```objectivec
if(!frontCamera) {
    BOOL bEnable = YES;
    //Flashlight is on when bEnable is YES; flashlight is off when bEnable is NO
    BOOL result = [_txLivePush toggleTorch: bEnable];
    //A result of YES means the flashlight is successfully turned on, while NO means the flashlight fails to be turned on
}
```

- **Customize manual focus**
Default manual focus logic is provided in the iOS version of the SDK. Although there is no problem regarding its functionality, the logic usually fails to work when touch events of the screen are occupied. Meanwhile, as a principle, we cannot intervene with the free interface arrangement practice.
A setFocusPosition function API is added to the new version of TXLivePush. You can perform manual focus based on where your finger is touching.

```objectivec
//If the customer calls this API, the focus trigger logic in the SDK will stop, avoiding repeated trigger of the focus logic
- (void)setFocusPosition:(CGPoint)touchPoint;
```

### Step 7: Set Logo watermark
Recent policies require that LVB videos must be marked with watermarks. With that in mind, we will focus on this feature that had seemed insignificant before.
Tencent Video Cloud supports two watermark setting methods. One is to set watermark in the push SDK, where the videos are marked with watermarks in the SDK before being encoded. Another is to apply watermarks in the cloud. That is, the cloud resolves videos and adds Logo watermarks to them.

We suggest that you <font color='red'>add watermarks with the SDK</font>, because there are three major problems when watermarking in the cloud:
 (1) This service increases load on the cloud machine and is not free, which will increase your cost.
 (2) It is not ideally compatible with certain situations such as resolution switching during the push process. This may cause problems like blurred screen.
 (3) It may bring about an extra 3-second video delay, which is caused by the transcode service.

The SDK requires that watermark images are in PNG format, because such images contain transparency information, which helps better solve issues like jagged screen. (Do not just change the extension of a JPG image to PNG in Windows and use it as a watermark image. Professional PNG logos need to be processed by professional art designers)

```objectivec
//Set video watermark
_config.watermark = [UIImage imageNamed:@"watermark.png"];
_config.watermarkPos = (CGPoint){10, 10};
```

### Step 8: Local recording
You can start local recording using startRecord API. The recording format is MP4. You can specify the storage path for the MP4 files using videoPath.
- Do not change resolution and soft/hard encoding during recording. Otherwise, exceptions may exist in the generated videos.
- For cloud recording, you only need to concatenate &record=mp4 to the end of the push URL. For more information, please see [Cloud Recording](https://cloud.tencent.com/document/product/454/7917).
- You will be notified of the generation of a recorded file through TXLiveRecordListener after stopRecord is called.

```objectivec
-(int) startRecord:(NSString *)videoPath;
-(int) stopRecord;
```

### Step 9: Push at the backend
Usually, once the App switches to the backend, the camera's capture function will be temporarily disabled by the iOS system, which means the SDK cannot continue capturing and encoding audio/video data. This is what happens if we don't do anything:
+ Phase 1 (from switching to the backend -> 10 seconds later) - CDN cannot provide video streams to viewers because it doesn't have any data, and the viewers will see a frozen display.
+ Phase 2 (10 seconds -> 70 seconds) - The player at the viewer end exits because it haven't received LVB streams for a long time. Everyone leaves the room.
+ Phase 3 (after 70 seconds) - The RTMP linkage of the push is disconnected by the server. The VJ needs to restart LVB to continue.

Sometimes a VJ may have to answer a phone call which will cause a pause. But even a short pause can bring unsatisfactory interaction experience as described above that leads to exit of viewers from the room. So, how can we optimize this?
We introduced a solution since **SDK 1.6.1**. Below is the result achieved at the viewer end when this solution is used: 
![](https://mc.qcloudimg.com/static/img/6325a9f7918602bd8db15228e6ffe189/image.png)

- **9.1) Adjust XCode configuration**
![](https://main.qcloudimg.com/raw/64e1d95634ebed1de71ad3b84492f37e.jpg)

- **9.2) Set pauseImg**
Before push starts, you can use the pauseImg API of LivePushConfig to set a waiting picture saying like "The VJ will come back soon".

```objectivec
    // 300 is the maximum duration of the image displayed at the pause of backend push (in sec).
    _config.pauseTime = 300;
    // 10 is the frame rate of the image displayed at the pause of backend push. The minimum is 5 and the maximum is 20.
    _config.pauseFps = 10;
    // The size of the image displayed at the pause of backend push cannot exceed 1920*1920.
    _config.pauseImg = [UIImage imageNamed:@"pause_publish.jpg"];
    [_txLivePublisher setConfig:_config];
```

- **9.3) Set temporary running of App at the backend**
The App goes into sleep mode when it is switched to the backend, and consequently the SDK stops pushing streams. As a result, viewers can only see a black screen or frozen screen of the live room. The following code enables the App to run for a few minutes after it is switched to the backend, which is long enough for a VJ to answer a short phone call.

```objectivec
//Register before pushing message notification
[[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(handleEnterBackground:) 
    name:UIApplicationDidEnterBackgroundNotification object:nil];

//Call beginBackgroundTaskWithExpirationHandler after receiving the notification
-(void)handleEnterBackground:(NSNotification *)notification
{
    [[UIApplication sharedApplication] beginBackgroundTaskWithExpirationHandler:^{
    }];
}
```
- **9.4) Switch to the backend**
In handleEnterBackground mentioned in the last step, call the API function pausePush of TXLivePush. The SDK cannot capture camera images, but it can keep pushing streams via pauseImg you just configured.

```
//Switch to the backend: Add the following to the code from the last step
- (void)handleEnterBackground:(NSNotification *)notification
{
    [[UIApplication sharedApplication] beginBackgroundTaskWithExpirationHandler:^{
    }];
    [_txLivePush pausePush];
}
```

- **9.5) Switch to the frontend**
 After the App is switched to the frontend, (in handleEnterForeground), call the API function resumePush of TXLivePush to resume capturing camera images. Note: pausePush and resumePush need to be used <font color='red'>in pairs</font>, because they are closely related to SDK internal state. Otherwise, many bugs will be introduced.
 
```objectivec
//Switch to the frontend
- (void)handleEnterForeground:(NSNotification *)notification
{
    [_txLivePush resumePush];
}
```

### Step 10: Stutter alert

- What should we do if the network quality is poor at the VJ end? 
- Should we lower the definition to ensure the smoothness? It will lead to blurry video images with many mosaics at the viewer end.
- Should we drop some of the video frames to maintain the image definition? It will lead to continuous stutter at the viewer end.
- Since neither of the above is satisfactory, what should we do?
- We all know that it's impossible to "eat your cake and have it."

You can capture the **PUSH_WARNING_NET_BUSY** event by using onPlayEvent in TXLivePushListener. This event indicates that the VJ's network is extremely poor and stutters occur at the viewer end.

You can prompt the VJ with a message indicating **"Poor network quality. Please move closer to your WiFi, and make sure the signal isn't blocked by any wall or obstacle"**.

### Step 11: Push in landscape mode
In most cases, VJs push videos in an LVB by holding the screen in a portrait orientation so that the viewers can get portrait images. However, sometimes VJs may need to hold the screen in a landscape orientation to allow the viewers to get landscape images with a wider view. In this case, push in landscape mode is required. The figures below show the difference between landscape mode and portrait mode in terms of the images at the viewer end.
![](//mc.qcloudimg.com/static/img/cae1940763d5fd372ad962ed0e066b91/image.png)
> <font color='red'>**Note:**</font> The aspect ratios of images at viewer end are different between landscape mode and portrait mode. In portrait mode, the aspect ratio is 9:16, while in landscape mode, 16:9.

To implement landscape mode, you need to make two configurations:
- **Adjust image display at the viewer end**
Configure the **homeOrientation** option in LivePushConfig. It controls whether the aspect ratio of images at the viewer end is **16:9** or **6:19**. You can check whether the aspect ratio is adjusted as expected by using your player.

- **Adjust image display at the VJ end**
Next, you need to see whether the local rendering at the VJ end is normal. You can use the setRenderRotation API in TXLivePush to set the rotation of the images at the VJ end. This API provides four parameters (**0, 90, 180 and 270**) for setting the rotation angle.

### Step 12: Background audio mixing
SDK 1.6.1 and later versions support background audio mixing, and VJs can choose to wear or not wear a headset. You can implement background audio mixing by using the following APIs in TXLivePush:

| API | Description |
|:-------:|---------|
| playBGM | Passes a piece of music via path. In [Mini LVB Demo](https://cloud.tencent.com/doc/api/258/6164), we obtain music files from the iOS local media library |
| stopBGM | Stops background music |
| pauseBGM | Pauses background music |
| resumeBGM | Resumes background music |
| setMicVolume | Sets microphone volume for audio mixing. It is recommended to add a slider in the UI to allow VJs to set volume on their own |
| setBGMVolume | Sets background music volume for audio mixing. It is recommended to add a slider in the UI to allow VJs to set volume on their own |

### Step 13: In-ear monitoring/Reverb
- **In-ear monitoring**
This means when a VJ is singing with a headset on, the headset will feed back the VJ's voice in real time. This is because the VJ hears his or her own voice transmitted through bone structures in the skull (solid), while the viewers hear the voice transmitted through the air. These two voices can be very different, thus the VJ needs to hear the voice effect at the viewer end.
![](//mc.qcloudimg.com/static/img/fca1094c93126ad5b61d962ec22ad0d5/image.png)

 In-ear monitoring can be enabled through the enableAudioPreview API in TXLivePushConfig. In joint broadcasting scenarios, it is recommended that only the primary VJ enables this feature while secondary VJs do not, because it sounds strange in real-time video/audio chats when in-ear monitoring is enabled.

- **Reverb**
This means adding certain special effects when using in-ear monitoring, such as KTV, Grand Hall, Magnetic and Metallic, to make VJs' voice more impressive to viewers. Reverb effects can be set through setReverbType (supported by version 1.9.2 and later), the member function of TXLivePush.

 The following reverb effects are supported: KTV, Small Room, Grand Hall, Low-pitched, Sonorous, Metallic and Magnetic.

### Step 14: End push
Ending a push is simple, but proper cleanup is required. Since only one TXLivePush object can run at a time, improper cleanup may adversely affect the next LVB.
```objectivec
//End a push with proper cleanup
- (void)stopRtmpPublish {
    [_txLivePush stopPreview];
    [_txLivePush stopPush];
    _txLivePush.delegate = nil;
}
```

<h2 id="Message"> Send messages </h2>
This feature is used to deliver certain custom messages from the pusher end to the viewer end via audio/video lines. It is applicable to the following scenarios:
(1) Online quiz: The pusher end delivers the **questions** to the viewer end. Perfect "sound-image-question" synchronization can be achieved.
(2) Live show: The pusher end delivers **lyrics** to the viewer end. The lyric effect can be displayed on the viewer end in real time and its image quality is not affected by video encoding.
(3) Online education: The pusher end delivers the operations of **Laser pointer** and **Doodle pen** to the viewer end. The drawing can be performed at the viewer end in real time.

```objectiveC
[_answerPusher sendMessage:[mesg dataUsingEncoding:NSUTF8StringEncoding]];
```

> onPlayEvent (PLAY_EVT_GET_MESSAGE) of TXLivePlayer can be used to receive messages.

## Event Handling
### 1. Event listening
SDK listens to push related events using the TXLive<font color='red'>Push</font>Listener proxy. Note that the TXLive<font color='red'>Push</font>Listener only listens to push events with prefix <font color='red'>PUSH_</font>.

### 2. Normal events 
A notification event is prompted after each successful push. For example, receiving 1003 means that the system will start rendering the camera pictures.

| Event ID | Value | Description |   
| :-------------------  |:-------- |  :------------------------ | 
| PUSH_EVT_CONNECT_SUCC | 1001 | Successfully connected to Tencent Cloud push server |
| PUSH_EVT_PUSH_BEGIN | 1002 | Handshake with the server completed, everything is OK, ready to start push |
| PUSH_EVT_OPEN_CAMERA_SUCC | 1003 | The pusher has successfully started the camera (this will take 1-2 seconds on some Android phones) | 

### 3. Error notifications 
The push cannot continue as the SDK detected critical problems. For example, the user disabled camera permission for the App so the camera cannot be started.

| Event ID | Value | Description |   
| :-------------------  |:-------- |  :------------------------ | 
| PUSH_ERR_OPEN_CAMERA_FAIL | -1301 | Failed to enable camera | 
| PUSH_ERR_OPEN_MIC_FAIL | -1302 | Failed to enable microphone | 
| PUSH_ERR_VIDEO_ENCODE_FAIL | -1303 | Video encoding failed |
| PUSH_ERR_AUDIO_ENCODE_FAIL | -1304 | Audio encoding failed |
| PUSH_ERR_UNSUPPORTED_RESOLUTION | -1305 | Unsupported video resolution |
| PUSH_ERR_UNSUPPORTED_SAMPLERATE | -1306 | Unsupported audio sampling rate |
| PUSH_ERR_NET_DISCONNECT | -1307 | Network disconnected. Three failed reconnection attempts have been made. Restart the push for more retries. |

### 4. Warning events 
Some non-fatal errors occurred with SDK can be solved in most cases by throwing warning events to trigger protection or recovery logics.

- **WARNING_NET_BUSY**
VJ's network is busy. This warning can be used as a UI message for users (Step 10).

- <font color='red'>**WARNING_SERVER_DISCONNECT**</font>
Push request rejected by backend. This is usually caused by the miscalculated txSecret in the push URL, or because the push URL is already in use (a push URL can only be used by one pusher at a time).

| Event ID | Value | Description |   
| :-------------------  |:-------- |  :------------------------ | 
| PUSH_WARNING_NET_BUSY | 1101 | Bad network condition: data upload is blocked because upstream bandwidth is too small. |
| PUSH_WARNING_RECONNECT | 1102 | Network disconnected. Auto reconnection has been initiated (no more attempts will be made after three failed attempts). |
| PUSH_WARNING_HW_ACCELERATION_FAIL | 1103 | Failed to start hard encoding. Soft encoding is used instead. |
| PUSH_WARNING_DNS_FAIL | 3001 | RTMP - DNS resolution failed (this triggers a retry) |
| PUSH_WARNING_SEVER_CONN_FAIL | 3002 | Failed to connect to the RTMP server (this triggers a retry) |
| PUSH_WARNING_SHAKE_FAIL | 3003 | Handshake with RTMP server failed (this triggers a retry) |
| PUSH_WARNING_SERVER_DISCONNECT | 3004 | The RTMP server disconnected automatically (this triggers a retry) |

