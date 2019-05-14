## 1. How to Perform Push
Tencent Cloud's RTMP SDK internal state machine works as shown in the figure below :
- **Step1 - Start the call**: After TXLivePush object's startPush is called, the push process starts.

- **Step2 - Connect to the server: **The first step of push is attempting to connect to the push server. If the connection fails, an NET_DISCONNECT error is thrown and the process is suspended.

- - **Step3 - Start push: **PUSH_EVT_PUSH_BEGIN indicates the start of push in a true sense. Many customers believe the calling of startPush indicates the start of push. This is not the case.

- **Step4 - Main loop of push: **LVB push is an ongoing process driven by a main loop engine in the SDK. The loop can be broken out of only when the process is stopped actively with stopPush or suffers an irrecoverable error.

![How does SDK work](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/tencent_cloud_rtmp_sdk_pusher_status_14.jpg)

## 2. Quality Monitor
From the very beginning of design, we tried not to make the RTMP SDK too closed and look like a black box. Therefore, we provide a **status feedback mechanism** that reports various status parameters from inside every 1 to 2 seconds.

![](//mc.qcloudimg.com/static/img/48fd46af4e17b0299fd00a0e661a16f0/image.png)

All you need to do is providing a **TXLivePushListener** listener for the TXLivePush object. The RTMP SDK will report all the internal status parameters through onNetStatus callback.
  
|  Push Status                   |  Description                    |   
| :------------------------  |  :------------------------ | 
| NET_STATUS_CPU_USAGE | The CPU utilization for current process and the overall CPU utilization for the machine |
| NET_STATUS_VIDEO_WIDTH | Width of the current video (in pixels) |
| NET_STATUS_VIDEO_HEIGHT | Height of the current video (in pixels) |
| NET_STATUS_NET_SPEED | Current transmission speed (in kbps) |
| NET_STATUS_VIDEO_BITRATE | The output bitrate of the current video encoder, i.e., the number of video data bits produced by the encoder per second  (in kbps) |
| NET_STATUS_AUDIO_BITRATE | The output bitrate of the current audio encoder, i.e., the number of audio data bits produced by the encoder per second  (in kbps) |
| NET_STATUS_VIDEO_FPS | Current video frame rate, that is, the number of frames produced by video encoder per second |
| NET_STATUS_CACHE_SIZE | Accumulated audio/video data size. A value ≥ 10 indicates the current uplink bandwidth is not enough to consume the audio/video data produced |
| NET_STATUS_CODEC_DROP_CNT | The number of global packet drops. To avoid a vicious accumulation of delays, the SDK can actively drop packets when the accumulated data exceeds the threshold. A higher number of packet drops means a more severe network problem. |
| NET_STATUS_SERVER_IP | IP of the connected push server |
| NET_STATUS_NET_JITTER    | Network jitter status (not recommended for reference) |

### 2.1 Determining the Push Quality
With the above status information, how to verify whether the push quality is OK? The following are the frequently used quality metrics. **You're recommended to have an understanding of them**:

**1. Relationship between BITRATE and NET_SPEED**
> BITRATE (= VIDEO_BITRATE + AUDIO_BITRATE) refers to the number of audio/video data bits produced by the encoder for push per second; NET_SPEED refers to the number of data bits pushed actually per second. A long duration of BITRATE == NET_SPEED means a good push quality.
>
>But a long duration of BITRATE >= NET_SPEED means an unsatisfactory push quality.

**2. CACHE_SIZE and DROP_CNT Values**
> Once BITRATE >= NET_SPEED, the audio/video data produced by the encoder will build up on VJ's phone, with the severity indicated by the CACHE_SIZE value. When the CACHE_SIZE value exceeds the threshold, SDK will actively drop some audio/video data, thus triggering an increment of DROP_CNT.
>
>The fact that CACHE_SIZE value is always greater than 10 (10 inclusive) or an increase of DROP_CNT value means the VJ's network is not OK and the push quality cannot be ensured.
>
>The following figure shows a typical case where<font color='blue'> the insufficient uplink bandwidth causes continuous stutter </font>on viewer end:
>![](//mc.qcloudimg.com/static/img/319d6197da603ca15ffc6e2afd778e48/image.png)

**3. CPU_USAGE Value** 
> In a normal scenario, the CPU utilization for RTMP SDK push on various platforms is required to remain below 50%, especially when hardware encoding is enabled. For example, on the Xiaomi Mi 3 phone, when hardware acceleration is enabled, 720 p UHD push requires no more than 30% of CPU utilization.
>
>However, on an LVB APP, in addition to RTMP SDK, many other features such as on-screen comments, floating stars, and interactive text messages can consume some CPU resources.
>
>If the overall CPU utilization of the system exceeds 80%, video capture and encoding may be affected; if the CPU utilization reaches 100%, the VJ end will be terribly stuck and it is impossible for the viewers to have a smooth viewing experience.

**4. Ping value of SERVER_IP**
> If the Ping value from VJ to the IP given by SERVER_IP is very high (for example, exceeding 500ms), the push quality will be unsatisfactory. ** Tencent Cloud has been providing services on an "Access to the Closest** basis. In case of the above situation, please contact us. Our OPS team will optimize the service.

### 2.2 SDK Push Quality

The charts shown in 2.1 are derived from our internal data analysis system for experimental testing. If you want to perform the same analysis, you can refer to the similar charts in the quality control system of [LVB Console](https://console.cloud.tencent.com/live). Those charts are more simple and accessible, allowing you to understand without the need of having much professional knowledge about audio/video.
![](//mc.qcloudimg.com/static/img/4bf231da79ec8e45bdc4c16c927da47f/image.png)

## 3. Parameter Tuning
You can customize video/audio encoding parameters by setting the Config object. Currently, the following setting APIs are supported:

| Parameter Name           |    Description                                          |   Default Value  | 
| :-------------- | :-----------------------------------------------| :------: |
| audioSampleRate |   Audio sampling rate: count of audio signal captures by the recording device per second   |  44100   |  
| enableNAS          |   Noise suppression: When this is enabled, background noises can be filtered out (applicable when the sampling rate is below 32,000) |  Off     |
| enableHWAcceleration|   Video hard-coding: When this is enabled, video capture up to 720 p, 30 fps is supported.   |  On   |  
| videoFPS     |   Video frame rate: Number of frames produced by the video encoder per second. Most of the phones don't support encoding above 30 FPS, so you're recommended to set FPS to 20.           |  20      |
| videoResolution |   Video resolution: Four types of 16:9 resolutions are available      |  640 * 360 |
| videoBitratePIN |   Video bitrate: Number of data bits produced by the video encoder per second (in kbps) |  800 |
| enableAutoBitrate |   bitrate adaptation: Adjust the video bitrate automatically based on the network condition |   Off |
| videoBitrateMax | Maximum output bitrate: This option takes effect only when bitrate adaption is enabled. |   1,200 |
| videoBitrateMin | Minimum output bitrate: This option takes effect only when bitrate adaption is enabled. |   800 |
| videoEncodeGop | Keyframe interval (in second): The interval at which one I frame is output | 3 seconds |
| homeOrientation | Set the rotation angle of video image, e.g., whether to push in a landscape mode  |   0: home is on the right; 1: home is at the bottom; 2: home is on the left; 3: home is at the top   |
| beautyFilterDepth | Beauty filter level: levels 1 to 9 are supported; the higher the level, the more obvious the effect.  0 means Off  |   Off   |
| FrontCamera | Front or rear camera by default | Front |
| Watermark | Watermark image (UIImage object) | Tencent Cloud Logo (demo)  |    
| watermarkPos | The position of the watermark image relative to the coordinate in the upper-left corner | (0, 0)  |                                                                        

You are recommended to set these parameters before enabling push, since most of them only take effect when the push is restarted. The reference codes are as follows:

```objectivec
//Declare _config and _pusher in member variables
....
//Initialize _config
_config = [[TXLivePushConfig alloc] init];

// Modify the audio sampling rate to 44100 and fixed video bitrate to 800
_config.audioSampleRate = 44100;
_config.enableAutoBitrate = NO;
_config.videoBitratePIN = 800;

//Initialize _pusher
_pusher = [[TXLivePush alloc] initWithConfig: _config];
```

## 4. Intelligent Speed Control
### 4.1 Background
RTMP push quality is crucial to the viewing experience. A poor push quality at VJ end will cause the stutter at all the viewer ends. According to the statistics, over 80% of LVB stutters among Video Cloud customers are caused by a poor RTMP push quality.

![](//mc.qcloudimg.com/static/img/4bf231da79ec8e45bdc4c16c927da47f/image.png)

Among the push quality issues, the biggest issue is caused by unsatisfactory uplink network at VJ end. Insufficient uplink bandwidth can make audio/video data build up and then be dropped at VJ end, thus leading to the stutter or even long freezing of video images at viewer end.

Therefore, dealing with the stutter of uplink network at VJ end can effectively improve the push quality, thus delivering a better viewing experience, especially in the domestic environment where uplink bandwidth is restricted widely by ISPs.

But network condition does not hinge on our will. If a VJ uses a 4-Mbps broadband package at home, it is not impossible to change it to 8Mbps just because the VJ installs a new App. Therefore, we can choose to**actively adapt to the uplink network**.


### 4.2 Solutions
RTMP SDK has provided solutions for three scenarios since Ver.1.7.0 :

#### [Live Show]
- **Characteristics**
Typically, a Live Show scenario uses a resolution of 360\*640 and a bitrate of 800 Kbps. In this mode, we are generally more concerned about the image clarity and sound smoothness. In case of a network condition fluctuation at VJ end, trading off image quality to ensure the smoothness is not a good choice.

 In a Live Show mode which has an already low bitrate, reducing bitrate can bring about a very limited effect. A little decrease of bitrate will not result in substantial improvement, while too much decrease will inevitably lead to localized mosaics and compromise the saturation of image color.

- ** Stream Control Solution**
Given the above characteristics of the scenario, **stream control is not recommended**. In case of a fluctuation of network condition at VJ end, RTMP SDK can notify this to your App through **PUSH_WARNING_NET_BUSY** event. In this case, you can, as instructed by the UI, remind the VJ that the WiFi is not good and suggest sitting closer to the router.
```
TXLivePushConfig* _config;
_config.videoBitratePIN	  = 700;  // 700kbps
_config.enableAutoBitrate = NO;   //Push at a fixed bitrate
_config.videoResolution   = VIDEO_RESOLUTION_TYPE_360_640;//Set push resolution
```

#### [Mobile Game LVB]
- **Characteristics**
Unlike the Live Show mode, Mobile Game LVB uses a high resolution and bitrate. A resolution like 540 p or even 720 p is very common, and the bitrate is often greater than 1.5 Mbps. Some games with dramatically changing images (such as TempleRun) even requires an uplink bandwidth of 2.5 Mbps to ensure a smooth playing experience.

 At the same time, the VJs of Mobile Game LVB are generally more professional and focused, tending to choose the scenes with a better network condition for a longer broadcasting, during which most of the network condition fluctuations are occasional and temporary.

- ** Stream Control Solution**
Given the above characteristics, we recommend using **AUTO_ADJUST_BITRATE_STRATEGY_2** strategy to automatically adjust the bitrate. Featuring rapid detection and adjustment, this solution is suitable for the mobile game LVB scenarios with a large bitrate.
```
TXLivePushConfig* _config;
_config.videoBitrateMin   = 500;//Minimum bitrate for dynamic adjustment
_config.videoBitrateMax   = 1000;//Maximum bitrate for dynamic adjustment
_config.videoBitratePIN   = 800;//Initial default bitrate
_config.enableAutoBitrate = YES;//Whether to enable dynamic adjustment of bitrate
_config.videoResolution   = VIDEO_RESOLUTION_TYPE_360_640;//Default resolution 
_config.autoAdjustStrategy= AUTO_ADJUST_BITRATE_STRATEGY_2;
```

- **Advanced Application**
Each bitrate has a matching resolution. For example, if using a bitrate of 600 Kbps with a resolution of 360 p, you can get a satisfactory effect in terms of both color and clarity. But for a combination of 600 Kbps bitrate and 720 p resolution, the image quality will be reduced greatly, because you need to trade off more image quality for a higher resolution.

 For this reason, in a 720 p scenario, if the bitrate is simply reduced from 1.5 Mbps to 500 Kbps, a dynamic image will produce more mosaics than in a scenario with a resolution of 360 p and a bitrate of 500 Kbps.

 Therefore, for a high-definition game push, **AUTO_ADJUST_BITRATE_RESOLUTION_STRATEGY_2** is recommended, which will reduce the bitrate while adjusting the resolution accordingly to keep a balance between bitrate and resolution.
 ```
 TXLivePushConfig* _config;
 _config.videoBitrateMin      = 800;//Minimum bitrate for dynamic adjustment
 _config.videoBitrateMax      = 3000;//Maximum bitrate for dynamic adjustment
 _config.videoBitratePIN      = 1800;//Initial default bitrate
 _config.enableAutoBitrate    = YES;//Whether to enable dynamic adjustment of bitrate
 _config.videoResolution      = VIDEO_RESOLUTION_TYPE_720_1280;//Default resolution 
_ config.autoAdjustStrategy  = AUTO_ADJUST_BITRATE_RESOLUTION_STRATEGY_2;
```
 
#### [Mobile Scenario]
- **Characteristics**
Mobile Scenario is a very broad concept. All scenarios with inconsistent bandwidth are collectively referred to as "Mobile Scenario" by us. In such a scenario, the uplink network condition at VJ end often changes, varying from 1 Mbps to 300 Kbps at different time periods.

- ** Stream Control Solution**
For this scenario, **AUTO_ADJUST_BITRATE_STRATEGY_1** is recommended, which allows the bandwidth to adapt to the change of network condition. The benefit of this strategy is an adaptive and elastic push quality in case of unstable bandwidth. The disadvantage is that the variable bitrate causes more fluctuations than a fixed bitrate even in a stable network environment.
 ```
 TXLivePushConfig* _config;
 _config.videoBitrateMin   = 500;//Minimum bitrate for dynamic adjustment
 _config.videoBitrateMax   = 1000;//Maximum bitrate for dynamic adjustment
 _config.videoBitratePIN   = 800;//Initial default bitrate
 _config.enableAutoBitrate = YES;//Whether to enable dynamic adjustment of bitrate
 _config.videoResolution   = VIDEO_RESOLUTION_TYPE_360_640;//Default resolution 
 _config.autoAdjustStrategy= AUTO_ADJUST_BITRATE_STRATEGY_1;
```

## 5. Customize Video Data
Some customers with a strong R&D capability want to customize image processing (e.g., adding captions) while reusing the overall process of RTMP SDK. If so, you can follow the steps below.

- **Set Video Processing Callback**
You can customize video images by setting **videoProcessDelegate** proxy point for **TXLivePush**.

```objectivec
@protocol TXVideoCustomProcessDelegate <NSObject>

/**
 * Perform a callback in the OpenGL thread, where you can conduct the secondary processing of captured images
 * @param textureId  Texture ID
 * @param width      Texture width
 * @param height     Texture height
 * @return           Texture returned to SDK
 * Note: The texture type called back from the SDK is GL_TEXTURE_2D, and the one returned by the API to the SDK must also be GL_TEXTURE_2D.
 */
-(GLuint)onTextureCustomProcess:(GLuint)texture width:(CGFloat)width height:(CGFloat)height;
 
/**
 * Perform a callback in the OpenGL thread, where you can release the OpenGL resources created
 */
-(void)onTextureDestoryed;

@end
```

- **Process the video data in a callback function**
Implement onTextureCustomProcess function of TXVideoCustomProcessDelegate to achieve the customized processing of video images. The texture specified by textureId is a texture of type GLES20.GL_TEXTURE_2D.

 > To work with texture data, you need to have some basic knowledge about OpenGL. In addition, a huge calculation amount is not recommended. This is because onTextureCustomProcess has the same call frequency as FPS, and too heavy processing is likely to cause the GPU overheating.


## 6. Replace the Data Source
If you only want to use RTMP SDK to push and bring the audio and video capture and preprocessing (such as beauty filter, filter) under the control of your own codes, follow the steps below:

- - **Step1. Do not call TXLivePusher's startPreview API any longer**
In this way, SDK itself will not capture video and audio data any more, but only start preprocessing, coding, stream control, sending data and other push-related operations.

- - **Step2. Use sendVideoSampleBuffer to populate SDK with Video data**
SendVideoSampleBuffer is used to populate the SDK with the captured and processed video data. RGBA and NV12 formats are supported currently.

- - **Step3. Use sendAudioSampleBuffer to populate SDK with Audio data**
SendAudioSampleBuffer is used to populate the SDK with the captured and processed audio data. Please use 16-bit, 48000Hz PCM mono audio data.

