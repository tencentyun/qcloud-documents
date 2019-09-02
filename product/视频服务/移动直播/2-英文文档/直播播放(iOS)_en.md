## Basics
RTMP SDK includes two features, Push and Playback. Push works at the VJ side, while Playback, including Live Video Broadcasting (LVB) and Video On Demand (VOD), functions at the viewer side. Before getting started with the code interfacing, let's learn some basic facts:

- **LVB and VOD**
LVB video source is generated in real time, and only makes sense when someone pushes the LVB stream. Therefore, once the VJ stops broadcasting, the LVB URL will become invalid. Since the video is played in real time, no progress bar is displayed on the player during the LVB.

VOD's video source is a file on cloud, which can be played at any time as long as it has not been deleted by the provider. Since the entire video file is stored on the server, a progress bar will be displayed during playback.

- **Supported Protocols**
Commonly used LVB protocols are as follows. It is recommended to use LVB URL based on FLV protocol (starting with "http" and ending with ".flv") on APPs:
![](//mc.qcloudimg.com/static/img/94c348ff7f854b481cdab7f5ba793921/image.jpg)

 Commonly used VOD protocols are as follows. Currently, HLS VOD addresses are most commonly used (starting with "http" and ending with ".m3u8"):
![](//mc.qcloudimg.com/static/img/4b42a00bb7ce2f58f362f35397734177/image.jpg)

## Notes
Tencent Cloud RTMP SDK **DOES NOT ** impose any restrictions on the source of playback URLs, which means you can use the SDK to play videos from both Tencent Cloud and non-Tencent Cloud addresses. But the player in RTMP SDK only supports three LVB video address formats (FLV, RTMP and HLS (m3u8)) and three VOD address formats (MP4, HLS (m3u8) and FLV).

## Interfacing Guide

### Step 1:  Create a Player
```objectivec
_txLivePlayer = [[TXLivePlayer alloc] init];
[_txLivePlayer setupVideoWidget:[UIScreen mainScreen].bounds containView:_myView insertIndex:0]
```

### Step 2:  Find a Place to Display Pictures
Next, we need to look for a place to display the video pictures in a player. In iOS systems, a view is used as the basic picture rendering unit. Therefore you simple need to prepare a view and adjust the layout.

- **Recommended layout**
> In fact, RTMP SDK player 
>  directly render the picture to the view you provided. Instead, it creates a subView used for OpenGL rendering upon the view. However, the size of this subView used for rendering will be adjusted automatically according to the size change of the view you provided, which means you do not need to worry about configuring the size.
>![](//mccdn.qcloud.com/static/img/75b41bd0e9d8a6c2ec8406dc706de503/image.png)
>
> If you want to implement UI controls such as live commenting and flower gifting on top of the rendering screen, we recommend that you create another view at the same level. This is a common design style which helps avoid a lot of problems regarding screen overlay.

- **How to make animation?**
> You can freely make animations for a view. But note that the target attribute modified for animations is **transform**, but not frame.
>
```objectivec
  [UIView animateWithDuration:0.5 animations:^{
            _myView.transform = CGAffineTransformMakeScale(0.3, 0.3); //Shrink by 1/3
        }];
```

### Step 3:  Start Playback
```objectivec
NSString* flvUrl = @"http://2157.liveplay.myqcloud.com/live/2157_xxxx.flv";
//Use setupVideoWidget to bind the view used to determine render area for the player. The first parameter "frame" has been deprecated since 1.5.2
[_txLivePlayer setupVideoWidget:CGRectMake(0, 0, 0, 0) containView:_myView insertIndex:0];
//Use startPlay to start the playback. FLV protocol is recommended for LVB
[_txLivePlayer startPlay:flvUrl type:PLAY_TYPE_LIVE_FLV];
```

- **setupVideoWidget** 
The parameter "frame" has been deprecated since 1.5.2. The size of the image is change to "always fills up the view provided by user". You can directly adjust the view if you wish to change the size or position of the image.

- **startPlay** 
Parameter type supports the following options. According to the feedback from some customers, **"fast forward" sometimes occurs during playback**. This is because they confused LIVE_FLV and VOD_FLV.

| Option | Enumerated Value | Description |
|---------|---------|---------|
| PLAY_TYPE_LIVE_RTMP | 0 | The input URL is an RTMP-based LVB URL |
| PLAY_TYPE_LIVE_FLV| 1 | The input URL is an FLV-based LVB URL |
| PLAY_TYPE_VOD_FLV | 2 | The input URL is an RTMP-based VOD URL |
| PLAY_TYPE_VOD_HLS | 3 | The input URL is an HLS (m3u8)-based VOD URL |
| PLAY_TYPE_VOD_MP4 |4 | The input URL is an MP4-based VOD URL |
| PLAY_TYPE_LIVE_RTMP_ACC | 5 | Low-latency joint broadcasting LVB URL (for joint broadcasting scenarios only) |
| PLAY_TYPE_LOCAL_VIDEO | 6 | Local video file on mobile phone |

### Step 4:  Adjust View

- **View: Size and Position**
You can modify the size and position of the view by directly adjusting the size and position of the parameter "view" of setupVideoWidget.

- **setRenderMode: Full Screen or Self-Adaption**

| Option | Description  |
|---------|---------|
| RENDER_MODE_FILL_SCREEN | The entire screen is filled with the view which is spread proportionally, with the excess parts cut out. There will be no black edges in this mode, but certain sections may not be displayed completely because some areas are cut out.  | 
| RENDER_MODE_FILL_EDGE | The view is scaled proportionally to adapt to the longest edge. The width and height of the scaled view will not extend beyond the display area and the view is centered. In this mode, black edges may appear on the screen.  | 

- **setRenderRotation: Screen Rotation**

| Option | Description |
|---------|---------|
| RENDER_ROTATION_PORTRAIT | Normal playback (The Home button is located directly below the video) | 
| RENDER_ROTATION_LANDSCAPE | The video rotates 270° clockwise (the Home button is directly to the left of the video) | 

![](//mc.qcloudimg.com/static/img/ef948faaf1d62e8ae69e3fe94ab433dc/image.png)


### Step 5:  Adjust Progress
Adjusting playback progress ** is only applicable to VOD**. You cannot adjust the video progress during LVB because the video source is in real-time.
```objectivec
// Adjust progress
[_txLivePlayer seek:slider.value];
```

### Step 6:  Pause Playback
- **VOD**
Pausing the video during VOD is of course, a common practice.

- **LVB**
For LVB, calling pause function means temporarily stopping stream-pull. The player will not be terminated, but will display the last frame.

```objectivec
// Pause
[_txLivePlayer pause];
// Resume
[_txLivePlayer resume];
```

### Step 7:  End Playback
At the end of the playback, **be sure to terminate the View control**, especially before the next startPlay. Otherwise a lot of memory leaks and splash screen issues will occur.

```objectivec
// Stop playback
[_txLivePlayer stopPlay];
[_txLivePlayer removeVideoWidget]; // Be sure to terminate the view control
```

### Step 8:  Hardware Acceleration
For blu-ray (1080p) quality, it is difficult to obtain smooth playback experience just by using software decoding. Therefore, if your scenario focuses on gaming LVB, it is recommended to enable hardware acceleration.

It is strongly recommended to perform **stopPlay** before the switching between software decoding and hardware decoding, and perform **startPlay** after switching. Otherwise serious blurred screen problems may occur.

```objectivec
  [_txLivePlayer stopPlay];
  _txLivePlayer.enableHWAcceleration = YES;
  [_txLivePlayer startPlay:_flvUrl type:_type];
```

### Step 9:  Stream capture recording (for LVB only)
Stream capture recording is an extended feature in LVB playback scenarios. It means that during the LVB, the viewer can capture and record a segment of the video by clicking the "Record" button and publish the recorded content via video delivery platforms (e.g. Tencent Cloud VOD system) so that the content can be shared on social platforms (such as WeChat Moments) in the form of UGC messages.

![](//mc.qcloudimg.com/static/img/2963b8f0af228976c9c7f2b11a514744/image.png)

```objectivec
//The following code is used to show how to record videos in LVB scenarios
//
//Specify a TXVideoRecordListener used to synchronize the progress and result of the recording process
_txLivePlayer.recordDelegate = recordListener;
//Start recording. It can be placed in the response function of the "Record" button. Currently you can only record the video source, but not the other contents such as the live comments
[_txLivePlayer startRecord: RECORD_TYPE_STREAM_SOURCE]; 
// ...
// ...
//End the recording. It can be placed in the response function of the "End" button
[_txLivePlayer stopRecord];                             
```
- The progress of recording process is indicated as a time value by the onRecordProgress of TXVideoRecordListener.
- The recorded file is in the format of MP4, and is informed by onRecordComplete of TXVideoRecordListener.
- TXUGCPublish is used to upload and publish videos. For details on how to use TXUGCPublish, refer to [Short Video-Publish Files](https://cloud.tencent.com/document/product/584/9367#6.-.E6.96.87.E4.BB.B6.E5.8F.91.E5.B8.8310).
 
## Status Monitor
Tencent Cloud RTMP SDK is always designed on a basis of White Box. You can bind a **TXLivePlayListener** for the TXLivePlayer object so that you can receive notifications regarding the internal status of SDK through onPlayEvent (Event Notification) and onNetStatus (Quality Feedback).

### 1. Playback Events
| Event ID                 |    Value  |  Description                    |   
| :-------------------  |:-------- |  :------------------------ | 
| PLAY_EVT_PLAY_BEGIN    |  2004 |  Video playback begins. The "loading" icon stops flashing at this point | 
| PLAY_EVT_PLAY_PROGRESS |  2005 |  Video playback progress, including current progress and overall progress. ** This is only applicable to VOD**      | 
| PLAY_EVT_PLAY_LOADING |  2007 | Video playback is being loaded. If video playback is resumed, this will be followed by a BEGIN event |  

- **Do not hide the playback view after receiving PLAY_LOADING**
The time length between PLAY_LOADING and PLAY_BEGIN can be different (sometimes 5 seconds, sometimes 5 milliseconds). Some customers consider hiding the view upon LOADING and displaying the view upon BEGIN, which will cause serious flickering (especially in LVB scenarios). It is recommended to place a translucent Loading animation on top of the video view.

- **The frequency of LOADING is determined by cacheTime**
You can configure the player's cacheTime attribute in TXLivePlayConfig. A small cacheTime value can cause a high LOADING frequency. If this happens, please make adjustments while referring to [Stutter & Latency](#.E5.8D.A1.E9.A1.BF.26amp.3B.E5.BB.B6.E8.BF.9F).

- **Work with PLAY_PROGRESS playback progress**
If you have no idea about​how to handle the PLAY_EVT_PLAY_PROGRESS event during VOD, refer to the sample code - [Work with Playback Progress](https://cloud.tencent.com/document/product/454/7896).

### 2. Ending Events
| Event ID                 |    Value  |  Description                    |   
| :-------------------  |:-------- |  :------------------------ | 
| PLAY_EVT_PLAY_END      |  2006 |  Video playback ends      | 
| PUSH_ERR_NET_DISCONNECT          |  -2301  | Network disconnected. Reconnection attempts have failed for multiple times, thus no more retries will be performed. Please restart playback manually | 

- How to check whether the LVB has ended?
For **VOD**, we can check whether the playback has ended through the PLAY_EVT_PLAY_END event.

 For **LVB**, we can't determine if the VJ has ended the push only by using the SDK. It is expected that when the VJ stops pushing stream, RTMP SDK will soon find the data stream pull fails (WARNING_RECONNECT), and then retry it again until the PLAY_ERR_NET_DISCONNECT event is thrown after three failed attempts.

 The reason for this is that the standard playback protocol itself does not have a generic STOP standard, so it is recommended to achieve your purpose by broadcasting a system message such as **"LVB has ended"** in the chat room.


### 3. Warning Events
You don't need to consider the following events. We listed the information of these events for synchronization purposes, according to the SDK white-box design concept

| Event ID                 |    Value  |  Description                    |   
| :-------------------  |:-------- |  :------------------------ | 
| PLAY_WARNING_VIDEO_DECODE_FAIL   |  2101  | Failed to decode the current video frame  |
| PLAY_WARNING_AUDIO_DECODE_FAIL   |  2102  | Failed to decode the current audio frame  |
| PLAY_WARNING_RECONNECT           |  2103  | Network disconnected, automatic reconnection has started (the PLAY_ERR_NET_DISCONNECT event will be thrown after three failed attempts) |
| PLAY_WARNING_RECV_DATA_LAG       |  2104  | Unstable incoming packet from network: This may be caused by insufficient downstream bandwidth, or unstable outgoing stream at the VJ end |
| PLAY_WARNING_VIDEO_PLAY_LAG       |  2105  | Stutter occurred during the current video playback |
| PUSH_WARNING_HW_ACCELERATION_FAIL |  2106  | Failed to start hard-decoding; Soft-decoding is used |
| PLAY_WARNING_VIDEO_DISCONTINUITY |  2107  | Current video frames are discontinuous and frame loss may occur |
| PLAY_WARNING_DNS_FAIL            |  3001  | RTMP-DNS resolution failed (thrown only if the playback address is RTMP) |
| PLAY_WARNING_SEVER_CONN_FAIL     |  3002  | Failed to connect to RTMP server (thrown only if the playback address is RTMP) |
| PLAY_WARNING_SHAKE_FAIL          |  3003  | RTMP server handshaking failed (thrown only if the playback address is RTMP) |

### 4. Connection Events
In addition, there are several server connection events used to measure and calculate the time for server connections. Also, you don't have to be concerned:

| Event ID                     |    Value  |  Description                    |   
| :-----------------------  |:-------- |  :------------------------ | 
| PLAY_EVT_CONNECT_SUCC     |  2001    | Connected to the server                |
| PLAY_EVT_RTMP_STREAM_BEGIN |  2002    | Connected to the server and started to pull stream (thrown only if the playback address is RTMP) |
| PLAY_EVT_RCV_FIRST_I_FRAME |  2003    | The network has received the first renderable video packet (IDR)  |


### 5. Status Callback 
 The **onNetStatus** notification is triggered once per second to provide real-time feedback on the current status of the pusher. Like a car dashboard, it can offer you a picture about what is happening inside the SDK, so that you can keep track of current network condition and video quality.
  
|   Evaluation Parameter                   |  Description                   |   
| :------------------------  |  :------------------------ | 
| NET_STATUS_CPU_USAGE     | Current CPU utilization (instantaneous) | 
| NET_STATUS_VIDEO_WIDTH  | Video resolution - Width |
| NET_STATUS_VIDEO_HEIGHT | Video resolution - Height |
| NET_STATUS_NET_SPEED     | Current network data receiving speed |
| NET_STATUS_NET_JITTER    | Network jitter status. A bigger jitter means a more unstable network |
| NET_STATUS_VIDEO_FPS     | The video frame rate of the current stream media    |
| NET_STATUS_VIDEO_BITRATE | Video bitrate of the current stream media (in kbps) |
| NET_STATUS_AUDIO_BITRATE | Audio bitrate of the current stream media (in kbps) |
| NET_STATUS_CACHE_SIZE    | Buffer size (jitterbuffer). A buffer length of 0 means that stutter will occur in all probability |
| NET_STATUS_SERVER_IP | IP of the connected server | 

## Stutter & Latency
In LVB scenarios, the occurrence frequency of stutters and latency level are critical indicators used to measure the user experience of an App product.

**The player itself plays an important role in these measurements**. With the same network environment and playback address, different players may yield completely different latency and stutter occurrence. (For example, commonly used flash players on PC browsers may have increasing latency because the playback policies are too simple)

Therefore, once you have finished the functional code interfacing listed in previous sections of this document, make sure you read the [Stutter Optimization-Player Optimization](https://cloud.tencent.com/document/product/454/7946#5.-.E6.92.AD.E6.94.BE.E7.AB.AF.E7.9A.84.E4.BC.98.E5.8C.969) and make adjustments until you've achieved the best playback mode for your business scenario.

- **Performance comparison among the three modes**

![](//mc.qcloudimg.com/static/img/1d5a860ff74f9d026a36c04dd8bb27ef/image.jpg)

- **Interface codes of the three modes**

```objectivec
TXLivePlayConfig*  _config = [[TXLivePlayConfig alloc] init];
//Auto mode
_config.bAutoAdjustCacheTime   = YES;
_config.minAutoAdjustCacheTime = 1; 
_config.maxAutoAdjustCacheTime = 5;
//Speedy mode
_config.bAutoAdjustCacheTime   = YES;
_config.minAutoAdjustCacheTime = 1;
_config.maxAutoAdjustCacheTime = 1;
//Smooth mode
_config.bAutoAdjustCacheTime   = NO;
_config.cacheTime              = 5;

[_txLivePlayer setConfig:_config];

//Launch the playback once configuration is completed

```

Note: Cloud providers usually introduce a latency of **1.5-2 seconds** on their CDN. This is unavoidable, thus the **total latency = CDN latency + CacheTime.**


