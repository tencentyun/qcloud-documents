## Basics
**Push** means to collect, encode audio/video data and push the data to your specified cloud video platform. The process involves a large amount of basic audio/video-related knowledge, you can only achieve desired results after lots of refining and optimizing.

Tencent Video Cloud SDK mainly helps you push videos on smart phones. The SDK comes with easy-to-use APIs and can be driven by using a single push URL:
![](//mc.qcloudimg.com/static/img/ca7f200c31a9323c032e9e000831ea63/image.jpg)

## Notes
- **No restrictions on cloud providers**
> The SDK **does not prevent you from pushing to non-Tencent Cloud addresses**. So how do we make such pushes?
> 
> To solve the inaccurate DNS mapping problem within China, "Closest route selection" has been introduced starting from SDK 1.5.2. This feature selects the push route nearest to the VJ's location using Tencent Cloud's close route selection server, which significantly improves push quality. However this also means that the route selection results only include Tencent server addresses. In addition, since a large number of customers use dedicated push domain names, SDK cannot determine whether the target is Tencent Cloud simply by using the URL text.
> 
> Therefore, if you wish to push videos to addresses of other cloud providers, contact our customer service for help to disable closest route selection feature for your account. This can be done through cloud control, thus there is no need to release new client versions.

- **x86 simulator debugging**
> Since the SDK uses a great number of advanced features of the iOS system, we cannot ensure that all the features can function normally under the simulator in the x86 environment. Furthermore, audio and video are performance-sensitive features, the performance under the simulator will be greatly different from that on a real phone. Therefore, it is recommended to use an actual mobile phone for debugging if possible.

## Preparation

- **Acquiring SDK**
[Download](https://cloud.tencent.com/document/product/454/7873) SDK and follow the instructions in [Project Configuration](https://cloud.tencent.com/document/product/454/7876) to add the SDK into your APP development project.

- **Acquiring Test URL**
After [Activating](https://console.cloud.tencent.com/live) the LVB service, use the ["LVB Console" -> "LVB Code Access" -> "Push Generator"](https://console.cloud.tencent.com/live/livecodemanage) to generate push address. For more information, please see [Acquiring Push Playback URL](https://cloud.tencent.com/document/product/454/7915).


#### Code Interfacing
The guide mainly aims for **camera LVB** solution, which is mainly used for scenarios such as beauty show LVB, event LVB. Refer to game push documentation in the advanced feature section if you wish to achieve game screencap push features.

### Step 1:  Create Push Object
Create a **LivePush** object, which will be used later to complete the push task.

Before you create a LivePush object, you need to specify a **LivePushConfig** object to determine the configuration parameters of various LivePush aspects, such as push resolution, frames per second (FPS) and GOP (seconds per one I-frame).

The LivePushConfig object has been equipped with some parameters that we have repeatedly tuned upon "alloc". If you do not wish to customize these parameters, you can simply alloc and assign them to the LivePush object. If you have experience in the related field and want to adjust the default configuration, you can read the **Advance Guide**.

```objectivec   
// Create a LivePushConfig object, which is initialized with the basic configuration by default
 TXLivePushConfig* _config = [[TXLivePushConfig alloc] init];    
 //In _config, you can perform certain initialization operations on push parameters (e.g. whitening, hardware acceleration, front/rear camera, etc.). Note that _config cannot be nil  
 _txLivePush = [[TXLivePush alloc] initWithConfig: _config];
```

### Step 2:  Find a Place to Display Pictures
Next, we need to look for a place to display the images of camera. In iOS system, a view is used as the basic interface rendering unit. Therefore, you only need to prepare a **startPreview** API function transferred by view to the LivePush object.

- **Recommended layout**
> In fact the SDK does not directly render the picture to the view you provided. Instead, it creates a subView used for OpenGL rendering upon the view. However, the size of this subView used for rendering will be adjusted automatically according to the size change of the view you provided.
>![](//mccdn.qcloud.com/static/img/75b41bd0e9d8a6c2ec8406dc706de503/image.png)
>
> However, if you want to implement UI controls such as live commenting and flower gifting on top of the rendering screen, we recommend that you create another view at the same level, which helps avoid a lot of problems regarding screen overlay.

- **How to make animation?**
> You can freely make animations for a view. But note that the target attribute modified for animations is **transform**, but not frame.
>
```objectivec
  [UIView animateWithDuration:0.5 animations:^{
            _myView.transform = CGAffineTransformMakeScale(0.3, 0.3); //Shrink by 1/3
        }];
```

### Step 3:  Launch Push
After the preparations in Step 1 and Step 2, you can use the following codes to start the push: 

```objectivec 
NSString* rtmpUrl = @"rtmp://2157.livepush.myqcloud.com/live/xxxxxx";    
[_txLivePush startPreview:_myView];  //_myView is the view to be specified in Step 2    
[_txLivePush startPush:rtmpUrl];
```

- **startPush** is used to tell the SDK that which push URL the audio/video streams are being pushed to.
- The parameter of **startPreview** is the view you need to specify in Step 2; startPreview is used to associate the interface view control with the LivePush object, thus rendering the picture collected by the mobile phone camera onto the screen.

### Step 4:  Configure Video Definition

Configure video definition by using **setVideoQuality**, you can also configure by using the video quality options in TXLivePushConfig. However we still recommend that you use the options below:

| Definition   | Configuration Parameter | Resolution | Applicable Scenario | 
|:-------:|:-------:|:-----:|---------|
| **High Definition** | VIDEO_QUALITY_HIGH_DEFINITION |  **540P** | This is a recommended definition which allows most mainstream mobile phones to present clear pictures.  |
| **Standard Definition** | VIDEO_QUALITY_STANDARD_DEFINITION |  **360P** | Choose this definition if you have consideration about bandwidth cost.<br> It brings average video quality but reduces bandwidth cost by 60%, compared to high definition.  |
| **Dynamic** |  VIDEO_QUALITY_QOS_DEFINITION |  **Dynamic** | This will automatically adjust video resolution among three levels (192 \* 336 - 540 \* 960) based on network condition, in order to cope with network fluctuations. Suitable for scenarios with inconsistent network such as overseas LVB. <br>Note: This type of video streams may be incompatible with certain players.  |
| **Ultra High Definition** | VIDEO_QUALITY_SUPER_DEFINITION |  **720P** | Note: This is not recommended for scenarios where videos are mostly viewed in small screens. <br>You can consider using this definition if videos are viewed in large screens and the VJ has a great network.  |

### Step 5:  Beauty Filter
- **Beautify**
The setBeautyFilterDepth API can be used to configure beautify and whitening levels (0-9). 0 means to disable beautify feature. The beautify feature has been significantly improved since 1.9.1, now you can obtain optimal video quality if you use the feature together with 540 * 960 resolution (setVideoQuality - VIDEO_QUALITY_HIGH_DEFINITION).
```objectivec
[_txLivePush setBeautyFilterDepth:7 setWhiteningFilterDepth:3];
```

- **Filter**
The setFilter API can be used to configure filter effect. The filter is a histogram file, our designer group provided 8 materials which are packaged inside the Demo by default. You can use them as you like, without considering about copyright issues.
```objectivec
NSString * path = [[NSBundle mainBundle] pathForResource:@"FilterResource" ofType:@"bundle"];
if (path != nil && index != FilterType_None && _txLivePublisher != nil) {
        path = [path stringByAppendingPathComponent:lookupFileName];
        UIImage *image = [UIImage imageWithContentsOfFile:path];
        [_txLivePublisher setFilter:image];
} 
```
![](//mc.qcloudimg.com/static/img/ad0711f3c35f2087d3520677bfd64391/image.png)
> Be sure to use PNG images if you wish to customize the filters.** Do NOT use JPG image.**


### Step 6:  Camera Control
- **Switch front or rear camera** 
The **front** camera is used by default (this default value can be changed by modifying the configuration option frontCamera in LivePushConfig). The camera is switched each time switchCamera is called. Make sure both LivePushConfig and LivePush objects have been initialized before switching camera.  
  
```objectivec
// The front camera is used by default. This default value can be changed by modifying the configuration option frontCamera in LivePushConfig   
[_txLivePush switchCamera];
```

- **Turn the flashlight on or off** 
Flashlight is only available for the rear camera. (You can check whether the current camera is front or rear by looking at the frontCamera member in "TXLivePush.h")

```objectivec
if(!frontCamera) {
    BOOL bEnable = YES;
    //Flashlight is on when bEnable is YES; flashlight is off when bEnable is NO
    BOOL result = [_txLivePush toggleTorch: bEnable];
    //A result of YES means the flashlight is successfully turned on, while NO means failed to turn on flashlight
}
```

- **Customize manual focus**
Default manual focus logic is provided in the iOS version of the SDK. While there is no problem regarding its functionality, the logic usually fails to work when touch events of the screen are occupied. Meanwhile, as a principle, we cannot intervene with the free interface arrangement practice.
A setFocusPosition function API is added to the new version of TXLivePush. You can perform manual focus based on where your finger is touching.

```objectivec
// If the customer calls this API, the focus trigger logic in the SDK will stop, avoiding repeated trigger of the focus logic
- (void)setFocusPosition:(CGPoint)touchPoint;
```

### Step 7:  Set Logo Watermark
Recent policies require that LVB videos must be marked with watermarks. With that in mind, we will focus on this feature that had seemed insignificant before.
Tencent Video Cloud currently supports two watermark settings. One is to set watermark in the push SDK, where the videos are marked with watermarks in the SDK before being encoded. Another is applying watermarks in the cloud. That is, the cloud resolves videos and adds Logo watermarks to them.

We suggest that you **add watermarks with the SDK**, because there are three major problems when watermarking in the cloud:
 (1) This service increases the load on the cloud machine and is not free, which will increase your cost;
 (2) It is not ideally compatible with certain situations such as resolution switching during the push process. This may cause problems like blurred screen.
 (3) It may cause an additional 3-second video delay, which is caused by the transcode service.

SDK requires that watermark images are PNG format, because such images contain transparency information, which helps processes such as anti-aliasing. (Do not just change the extension of a JPG image to PNG in Windows and put it in. Professional PNG logos need to be processed by professional art designers)

```objectivec
//Set video watermark
_config.watermark = [UIImage imageNamed:@"watermark.png"];
_config.watermarkPos = (CGPoint){10, 10};
```

### Step 8:  Hardware Acceleration
The **enableHWAcceleration** API in LivePushConfig can be used to enable hardware encoding.
```objectivec
//Stop push (it is recommended to restart push during the enabling process, otherwise problems such as blurred/green screen may occur at the player end)
[_txLivePush stopPush]
//Enable hardware encoding
txLivePush.config.enableHWAcceleration = YES;
//Restart push
[_txLivePush startPush:rtmpUrl]
```

- **Compatibility Assessment**
The model quantity of iOS platform is not as large as that of Android platform, and its hardware quality is also highly reliable, so hardware acceleration is strongly recommended on the iOS platform and can be enabled safely. There is comprehensive protection mechanism in the SDK, which will help switch encoding mode to software encoding in case hardware encoding resources are occupied by other background Apps.

- **Differences**
If you enable hardware acceleration, the phone's battery consumption will significantly decrease, while maintaining an ideal temperature. But there will be more obvious mosaic when there are large movements in the image, compared to software encoding.
  
- **Avoid midway switching**
Avoid enabling/disabling hardware acceleration during push process. While this will not cause any problems in most cases, there are still various potential risks. The recommended approach is to enable hardware acceleration in the very beginning, instead of enabling it midway.

> A protection mechanism is provided in the SDK: If hardware acceleration resource is occupied by other Apps and cannot be enabled, the SDK will automatically switch back to software encoding.

### Step 9:  Background Push
Usually, once the App switches to background, the camera's capture function will be temporarily disabled by the iOS system, which means the SDK can no longer continue to capture and encode audio/video data. This is what happens if we don't do anything:
+ Phase 1 (from switching to background -> 10 seconds later) - CDN cannot provide video streams to viewers because it doesn't have any data, and the viewers will see a frozen display.
+ Phase 2 (10 seconds -> 70 seconds) - The player at the viewer side exits because it cannot receive LVB stream for a long time. Everyone leaves the studio.
+ Phase 3 (after 70 seconds) - The RTMP linkage of the push is disconnected by the server. The VJ needs to restart LVB to continue.

Even answering a short emergency call will cause all the viewers to leave the studio, with such an interaction experience. So how can we optimize it?
We introduced a solution since **SDK 1.6.1**. Below is the result achieved by using this solution, from viewers' view: 
![](//mc.qcloudimg.com/static/img/6325a9f7918602bd8db15228e6ffe189/image.png)

- **9.1) Set pauseImg**
Before the push, use the pauseImg API of LivePushConfig to set a waiting picture. It is recommended to use a picture such as: "The VJ will come back soon".

- **9.2) Set temporary background running for App**
The SDK cannot do anything if the App becomes completely dormant upon being switched to background. We can use the following code to allow the App to run for several minutes after it's switched to background, during which the VJ may go finish some "business", like answering an emergency call.

```objectivec
//Register, before pushing message notification
[[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(handleEnterBackground:) 
    name:UIApplicationDidEnterBackgroundNotification object:nil];

//Call beginBackgroundTaskWithExpirationHandler after receiving the notification
-(void)handleEnterBackground:(NSNotification *)notification
{
    [[UIApplication sharedApplication] beginBackgroundTaskWithExpirationHandler:^{
    }];
}
```
- **9.3) Switch to background process**
If the App is switched to background during push, that is, calling the pausePush API function of TXLivePush in handleEnterBackground mentioned in 8.2, you can still use the pauseImg you configured before to continue with the push, although the SDK can no longer collect camera image.

```
//Switch to background process:  Based on 8.2, add the following code
- (void)handleEnterBackground:(NSNotification *)notification
{
    [[UIApplication sharedApplication] beginBackgroundTaskWithExpirationHandler:^{
    }];
    [_txLivePush pausePush];
}
```

- **9.4) Switch to foreground process**
 After the App is switched back to the foreground and the resumePush API function of TXLivePush is called, the SDK will continue to collect camera pictures to push.
 
```objectivec
//Switch to foreground process
- (void)handleEnterForeground:(NSNotification *)notification
{
    [_txLivePush resumePush];
}
```

### Step 10:  Remind the VJ "network is poor"
Step 13 will discuss how to handle SDK push events. **PUSH_WARNING_NET_BUSY** is very useful, it means: <font color='blue'>** the uplink network of the VJ is poor, and stutters have occurred in the viewer end.**</font>

When you receive this WARNING, you can use the UI to remind VJ to change network egress, or get closer to the WiFi. Or tell him to say something like this: "Hello dear, I'm streaming! Stop reading eBay! What? Not eBay? Then stop downloading movies!"

### Step 11:  Push in landscape mode
In most cases, VJs push videos in an LVB by holding the screen in a portrait orientation so that the viewers can get portrait images. However, sometimes VJs may need to hold the screen in a landscape orientation to allow the viewers to get landscape images with a wider view. In this case, push in landscape mode is required. The figures below show the difference between landscape mode and portrait mode in terms of the images at the viewer end. 
![](//mc.qcloudimg.com/static/img/cae1940763d5fd372ad962ed0e066b91/image.png)
> **Note:** The aspect ratios of images at viewer end are different between landscape mode and portrait mode. In portrait mode, the aspect ratio is 9:16, while in landscape mode, 16:9.

To achieve a push in landscape mode, you need to make two configurations:
- **Adjust Viewer-end Performance**
Configure the **homeOrientation** option in LivePushConfig. It controls whether the video aspect ratio seen by the viewers is **16:9** or **6:19**, you can check the result by using your player to see if the aspect ratio is adjusted as expected.

| Settings | Description |
|:---------|---------|
| VIDEO_ANGLE_HOME_RIGHT     | The Home key is on the right |
| VIDEO_ANGLE_HOME_DOWN     | The Home key is at the bottom |
| VIDEO_ANGLE_HOME_LEFT       | The Home key is on the left |
| VIDEO_ANGLE_HOME_UP           | The Home key is at the top |

- **Adjust VJ-end Performance**
Next, we need to see whether the local rendering of the VJ is normal. Here, we can use the setRenderRotation API in TXLivePush to rotate the display seen by the VJ. This API provides four parameters (**0, 90, 180 and 270**) for setting the rotation angle.

### Step 12:  Background Music Mix
Background music mixing is supported starting from SDK 1.6.1. The VJ can choose headset mode or no-headset mode. You can achieve background music mixing feature by using the following APIs in TXLivePush:

| API | Description |
|:-------:|---------|
| playBGM | Send a music via path. In [Mini LVB Demo](https://cloud.tencent.com/doc/api/258/6164), we obtain music files from the iOS local media library |
| stopBGM | Stop background music |
| pauseBGM | Pause background music |
| resumeBGM | Resume background music |
| setMicVolume | Set the microphone volume when mixing music. It is recommended to add a slider in the UI to allow VJs to set volume on their own |
| setBGMVolume | Set the background music volume when mixing music. It is recommended to add a slider in the UI to allow VJs to set volume on their own |

### Step 13:  Microphone Feedback/Reverb
- **Microphone Feedback**
This means when VJ is singing with a headphone on, the headphone will feedback the VJ's voice in real time. This is because the VJ hears his or her own voice transmitted through bone structures in the skull (solid), while the viewers hear the voice transmitted through the air. These two voices can be very different, thus the VJ needs to hear the voice effect on the viewer's end.
![](//mc.qcloudimg.com/static/img/fca1094c93126ad5b61d962ec22ad0d5/image.png)

 You can enable microphone feedback with the enableAudioPreview API in TXLivePushConfig. In joint broadcasting scenarios, it is recommended that only the primary VJ enables this feature while secondary VJs do not, since microphone feedback will sound strange in real-time video/audio communications.

- **Reverb**
This means to add certain special effects when using microphone feedback, such as KTV, meeting hall, magnetic, metal and so on. The effect will also apply to the viewer's end and make the VJ's voice sound more interesting. You can configure reverb effects by using the setReverbType member function (supported since 1.9.2) of TXLivePush. The following reverb effects are currently supported:

| Reverb Type | Enumerated Value | Description |
|---------|:---------:|:---------:|
| REVERB_TYPE_0 | 0 | Disable |
| REVERB_TYPE_1 | 1 | KTV |
| REVERB_TYPE_2 | 2 | Small room |
| REVERB_TYPE_3 | 3 | Grand hall |
| REVERB_TYPE_4 | 4 | Low and deep |
| REVERB_TYPE_5 | 5 | Loud and clear |
| REVERB_TYPE_6 | 6 | Metal |
| REVERB_TYPE_7 | 7 | Magnetic |



### Step 14:  End Push
It is simple to end a push process, but proper cleaning work is required. Since only one TXLivePush object can run at a time, improper cleaning work may adversely affect the next LVB.
```objectivec
//End the push with proper cleanup work
- (void)stopRtmpPublish {
    [_txLivePush stopPreview];
    [_txLivePush stopPush];
    _txLivePush.delegate = nil;
}
```

## Event Handling
#### 1. Event Listening
SDK listens to push related events using the TXLivePushListener proxy. Note that the TXLivePushListener only listens to push events with prefix **PUSH_**.

### 2. Normal Events 
Events that are always prompted during a successful push. For example, receiving 1003 means that the system will start rendering the camera pictures

| Event ID                 |    Value  |  Description                    |   
| :-------------------  |:-------- |  :------------------------ | 
| PUSH_EVT_CONNECT_SUCC            |  1001 | Successfully connected to Tencent Cloud push server |
| PUSH_EVT_PUSH_BEGIN              |  1002 | Handshake with the server completed, everything is OK, ready to start push |
| PUSH_EVT_OPEN_CAMERA_SUCC    | 1003    | The pusher has successfully started the camera (this will take 1-2 seconds on some Android phones) | 

### 3. Error Notification 
The push cannot continue as the SDK detected critical problems. For example, the user disabled camera permission for the APP so the camera cannot be started.

| Event ID                 |    Value  |  Description                    |   
| :-------------------  |:-------- |  :------------------------ | 
| PUSH_ERR_OPEN_CAMERA_FAIL        | -1301 | Failed to start the camera |
| PUSH_ERR_OPEN_MIC_FAIL           | -1302 | Failed to start the microphone |
| PUSH_ERR_VIDEO_ENCODE_FAIL       | -1303 | Video encoding failed |
| PUSH_ERR_AUDIO_ENCODE_FAIL        -1304 | Audio encoding failed |
| PUSH_ERR_UNSUPPORTED_RESOLUTION  | -1305 | Unsupported video resolution |
| PUSH_ERR_UNSUPPORTED_SAMPLERATE | -1306 | Unsupported audio sampling rate |
| PUSH_ERR_NET_DISCONNECT          | -1307 | Network disconnected. Reconnection attempts have failed for three times, thus no more retries will be performed. Please restart the push manually |

### 4. Warning Events 
SDK detected some reparable problems. Most warning events will trigger protection logics or recovery logics that involve retrying, and in most of the cases the problems can be recovered. Don't make a fuss.

- **WARNING_NET_BUSY**
The VJ's network is busy. If you need UI prompts, this warning is relatively more useful (Step 10).

- WARNING_SERVER_DISCONNECT
The push request is rejected by the backend. This is usually caused by miscalculated txSecret in the push address, or because the push address is occupied by others (a push URL can only have one pushing end at a time).

| Event ID                 |    Value  |  Description                    |   
| :-------------------  |:-------- |  :------------------------ | 
| PUSH_WARNING_NET_BUSY            |  1101 | Bad network condition: data upload is blocked because uplink bandwidth is too small |
| PUSH_WARNING_RECONNECT           | 1102 | Network disconnected, automatic reconnection has started (auto reconnection will be stopped if it fails for three times) |
| PUSH_WARNING_HW_ACCELERATION_FAIL |  1103 | Failed to start hardware encoding. Software encoding is used |
| PUSH_WARNING_DNS_FAIL            |  3001 |  RTMP - DNS resolution failed (this will trigger retry process)        |
| PUSH_WARNING_SEVER_CONN_FAIL     |  3002 |  Failed to connect to the RTMP server (this will trigger retry process)  |
| PUSH_WARNING_SHAKE_FAIL          |  3003 |  RTMP server handshake failed (this will trigger retry process)  |
| PUSH_WARNING_SERVER_DISCONNECT      |  3004 |  The RTMP server actively disconnected (this will trigger retry process)  |

