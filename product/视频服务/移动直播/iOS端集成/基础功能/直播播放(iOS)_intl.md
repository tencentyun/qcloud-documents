## Basics
This document describes the LVB playback feature of Tencent Video Cloud SDK. The following are the basics you must learn before getting started.

- **LVB and VOD**
The video source of <font color='blue'>LVB (LIVE)</font> is pushed by VJ in real time. When the VJ stops broadcasting, the video image on the playback device stops. In addition, the video is broadcasted in real time, no progress bar is displayed when the player is playing the LVB URL.

 The video source of <font color='blue'>Video On-demand (VOD)</font> is a video file on cloud, which can be played at any time as long as it has not been deleted from the cloud. You can control the playback progress using the progress bar. The video playbacks on Tencent Video and Youku Tudou are typical VOD scenarios.

- **Supported Protocols**
Commonly used LVB protocols are as follows. It is recommended to use an LVB URL based on the FLV protocol (starting with "http" and ending with ".flv") on Apps:
![](//mc.qcloudimg.com/static/img/94c348ff7f854b481cdab7f5ba793921/image.jpg)

## Notes
- **Is there any restriction?**
Tencent Cloud SDK <font color='red'>**does not**</font> impose any restrictions on the source of playback URLs, which means you can use the SDK to play videos from both Tencent Cloud and non-Tencent Cloud addresses. But the player in Tencent Video Cloud SDK only supports three LVB video address formats (FLV, RTMP and HLS (m3u8)) and three VOD address formats (MP4, HLS (m3u8) and FLV).

- **Historical factors**
In earlier versions of the SDK, TXLivePlayer works as the only Class carrying both LVB and VOD features. With the expansion of the VOD features, we have made VOD a separate set of features carried by TXVodPlayer starting from SDK 3.5. For the compilation to be successful, VOD features such as seek are still visible in TXLivePlayer.

## Interfacing

### Step 1: Create a player
The TXLivePlayer module in Tencent Video Cloud SDK is responsible for the LVB playback feature.
```objectivec
TXLivePlayer _txLivePlayer = [[TXLivePlayer alloc] init];
```

### Step 2: Render a view
Next, we need to find a place to display the video images in the player. In iOS system, a view is used as the basic rendering unit. Therefore you simply need to prepare a view and configure the layout.

```objectivec
//Use setupVideoWidget to bind the view used to determine render area for the player. The first parameter "frame" has been deprecated since 1.5.2
[_txLivePlayer setupVideoWidget:CGRectMake(0, 0, 0, 0) containView:_myView insertIndex:0];
```

Technically, the player does not directly render the video image to the view (\_myView in the sample code) you provided. Instead, it creates a subView used for OpenGL rendering on top of the view.

You can adjust the size of the rendered image by simply adjusting the size and position of the view. The SDK will automatically adapt the video images to the size and position of the view.

![](//mccdn.qcloud.com/static/img/75b41bd0e9d8a6c2ec8406dc706de503/image.png)
 
> **How to make an animation?**
> You can freely make animations for a view. But note that the target attribute modified for animations is <font color='red'>transform</font>, instead of frame.
```objectivec
  [UIView animateWithDuration:0.5 animations:^{
            _myView.transform = CGAffineTransformMakeScale(0.3, 0.3); //Shrink by 1/3
        }];
```

### Step 3: Start playback
```objectivec
NSString* flvUrl = @"http://2157.liveplay.myqcloud.com/live/2157_xxxx.flv";
[_txLivePlayer startPlay:flvUrl type:PLAY_TYPE_LIVE_FLV];
```

| Option | Enumerated Value | Description |
|---------|---------|---------|
| PLAY_TYPE_LIVE_RTMP | 0 | The URL passed in is an RTMP-based LVB URL |
| PLAY_TYPE_LIVE_FLV | 1 | The URL passed in is an FLV-based LVB URL |
| PLAY_TYPE_LIVE_RTMP_ACC | 5 | Low-latency URL (only for joint broadcasting scenarios) |
| PLAY_TYPE_VOD_HLS | 3 | The URL passed in is an HLS (m3u8)-based playback URL |

> **About HLS (m3u8)**
> Considering its high latency, HLS is not recommended as the playback protocol for playing LVB videos on your App (although it is suitable for playing VOD videos). Recommended playback protocols include LIVE_FLV and LIVE_RTMP.


### Step 4: Adjust the view

- **view: size and position**
You can modify the size and position of the video images by adjusting the size and position of the parameter "view" of setupVideoWidget. The SDK will automatically adapt the video images to the size and position of the view.

- **setRenderMode: Full Screen or Self-Adaption**

| Option | Description |
|---------|---------|
| RENDER_MODE_FILL_SCREEN | The image spread across the entire screen proportionally, with the excess parts cut out. There are no black edges in this mode, but the image may not be displayed completely because of the cut-out areas. | 
| RENDER_MODE_FILL_EDGE | The image is scaled proportionally to adapt to the longest edge. Both the width and the height of the scaled image will not extend beyond the display area and the image is centered. In this mode, black edges maybe appear in the screen. | 

- **setRenderRotation: Screen rotation**

| Option | Description |
|---------|---------|
| RENDER_ROTATION_PORTRAIT | Normal playback (The Home button is located directly below the image) | 
| RENDER_ROTATION_LANDSCAPE | The image rotates 270° clockwise (the Home button is directly to the left of the image) | 

![](//mc.qcloudimg.com/static/img/ef948faaf1d62e8ae69e3fe94ab433dc/image.png)


### Step 5: Pause playback
Strictly speaking, you cannot pause LVB playback. The so-called pausing LVB playback means **freezing the image** and **turning off the sound**, but the video source keeps updating on the cloud. When you call resume, the video is resumed from the latest time, which works quite differently from VOD videos that are paused and resumed in the same way as local video files).

```objectivec
// Pause
[_txLivePlayer pause];
// Resume
[_txLivePlayer resume];
```

### Step 6: End playback
To exit the current UI at the end of playback, be sure to terminate the view control using <font color='red'>**removeVideoWidget**</font>. Otherwise, memory leak or flickering screen will occur.

```objectivec
// Stop playback
[_txLivePlayer stopPlay];
[_txLivePlayer removeVideoWidget]; // Be sure to terminate the view control
```

<h3 id="Message"> Step 7: Receive messages</h3>
This feature is used to deliver certain custom messages from the pusher end to the viewer end via audio/video lines. It is applicable to the following scenarios:
(1) Online quiz: The pusher end delivers the **questions** to the viewer end. Perfect "sound-image-question" synchronization can be achieved.
(2) Live show: The pusher end delivers **lyrics** to the viewer end. The lyric effect can be displayed on the viewer end in real time and its image quality is not affected by video encoding.
(3) Online education: The pusher end delivers the operations of **Laser pointer** and **Doodle pen** to the viewer end. The drawing can be performed at the viewer end in real time.

You can use this feature as follows:
- Switch the **enableMessage** toggle button in TXLivePlayConfig to **YES**.
- TXLivePlayer listens into messages by **TXLivePlayListener**, message No.: **PLAY_EVT_GET_MESSAGE (2012)**.

```objectiveC
 -(void) onPlayEvent:(int)EvtID withParam:(NSDictionary *)param {
    [self asyncRun:^{
        if (EvtID == PLAY_EVT_GET_MESSAGE) {
            dispatch_async(dispatch_get_main_queue(), ^{
                if ([_delegate respondsToSelector:@selector(onPlayerMessage:)]) {
                    [_delegate onPlayerMessage:param[@"EVT_GET_MSG"]];
                }
            });
        }
    }];
}
```

### Step 8: Screencap
You can capture the current image as a frame by calling **snapshot**. This feature can only capture the frames from the current live stream. To capture the entire UI, call the API of iOS system.

![](//mc.qcloudimg.com/static/img/f63830d29c16ce90d8bdc7440623b0be/image.jpg)

### Step 9: Recode the captured stream
As an extension in LVB playback scenarios, Recording Captured Stream means that during the LVB, the viewer can capture and record a segment of video by clicking the "Record" button and publish the recorded content via the video delivery platform (e.g. Tencent Cloud's VOD system) so that the content can be shared through UGC message on social platforms such as the "Moment" of WeChat.

![](//mc.qcloudimg.com/static/img/2963b8f0af228976c9c7f2b11a514744/image.png)

```objectivec
//The following code is used to show how to record videos in LVB scenarios
//
//Specify a TXVideoRecordListener used to synchronize the progress and result of the recording process
_txLivePlayer.recordDelegate = recordListener;
//Start the recording. It can be placed in the response function of the "Record" button. You can only record the video source, but not the other contents such as the on-screen comments.
[_txLivePlayer startRecord: RECORD_TYPE_STREAM_SOURCE]; 
// ...
// ...
//End the recording. It can be placed in the response function of the "End" button
[_txLivePlayer stopRecord];                             
```
- The progress of recording process is indicated as a time value by the onRecordProgress of TXVideoRecordListener.
- The recorded file is in the format of MP4, and is informed by onRecordComplete of TXVideoRecordListener.
- TXUGCPublish is used to upload and publish videos. For more information on how to use TXUGCPublish, please see [Short Video - Publish Files](https://cloud.tencent.com/document/product/584/9367#6.-.E6.96.87.E4.BB.B6.E5.8F.91.E5.B8.8310).


<h2 id="Delay">Adjusting delay</h2>
The LVB feature of Tencent Cloud SDK, equipped with the self-developed playback engine, is not developed based on ffmpeg. Compared with open source players, it performs better in terms of LVB delay control. We provide three delay adjusting modes, suitable for Live show, game LVB, and combined scenarios.

- **Performance comparison among the three modes**

| Control mode | Stutter rate | Average delay | Applicable scenarios | Principle description |
|---------|---------|---------| ------ | ----- |
| Speedy mode | High (relatively smooth) | 2s - 3s | Live show (online quiz) | It has the upper hand in delay control and is suitable for delay-sensitive scenarios. |
| Smooth mode | Lowest | >= 5s | Game LVB (Penguin e-Sports) | It is suitable for the LVB of ultra-high-bitrate games (such as battle royale games) |
| Auto mode | Network adaption | 2s - 8s | Combined scenarios | The better the viewers' network condition, the lower the latency, and vice versa. |


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

//Launch the playback after the configuration
```

> For more technical information on how to deal with stutter and delay problems, please see [How to Deal with Stutter](https://cloud.tencent.com/document/product/454/7946) <**ECI**>

<h2 id="RealTimePlay">Ultra-low latency playback</h2>
Tencent Cloud LVB player supports ultra-low delay playback with a delay of about <font color='red'>**400ms**</font>, which can be used in scenarios that have high requirement for delay, such as **remote prize claw** and **joint broadcasting**. Notes about this feature:

- **You don't need to activate this feature**
This feature does not need to be enabled in advance, but it requires that LVB streams reside in Tencent Cloud. Implementing low-delay linkage across cloud providers is difficult, in more than just technical terms.

- **Hotlink protection must be included in the URL**
The playback URL cannot be a normal CDN URL. It must have a hotlink protection signature. For more information on how to calculate the hotlink protection signature, please see [**txTime&txSecret**](https://cloud.tencent.com/document/product/454/9875).

- **Specify the playback type as ACC**
Specify the type as <font color='red'>**PLAY_TYPE_LIVE_RTMP_ACC**</font> when calling the startPlay function. The SDK pulls LVB streams using the RTMP-UDP protocol.

- **This feature has restrictions on concurrent playback**
It supports <font color="red">10 channels</font> of concurrent playback at most. Instead of being set due to limited technical capabilities, this restriction is intended to encourage you to use this feature in interaction scenarios only (for example, for VJs only in joint broadcasting and for players only in prize claw scenarios), so that you do not incur any unnecessary costs in the mere pursuit of low delay (The price of low latency lines is higher than that of CDN lines).

- **The delay performance of OBS is unsatisfactory**
If the push end is [TXLivePusher](https://cloud.tencent.com/document/product/454/7879), set `quality` to MAIN_PUBLISHER or VIDEO_CHAT using [setVideoQuality](https://cloud.tencent.com/document/product/454/7879#step-4.3A-.E8.AE.BE.E5.AE.9A.E6.B8.85.E6.99.B0.E5.BA.A6). If the push end is Windows, use [Windows SDK](https://cloud.tencent.com/document/product/454/7873#Windows). Pushing with OBS leads to unsatisfactory delay due to the excessive accumulated data at the pusher end.

## Listening to SDK Events
You can bind a **TXLivePlayListener** to the TXLivePlayer object to receive notifications about the internal status of SDK through onPlayEvent (Event Notification) and onNetStatus (Quality Feedback).

### 1. Playback events
| Event ID | Value | Description |   
| :-------------------  |:-------- |  :------------------------ | 
| PLAY_EVT_CONNECT_SUCC     |  2001    | Connected to the server                |
| PLAY_EVT_RTMP_STREAM_BEGIN |  2002    | Connected to the server and started to pull stream (thrown only if the playback address is RTMP) |
| PLAY_EVT_RCV_FIRST_I_FRAME |  2003    | The network has received the first renderable video packet (IDR)  |
| PLAY_EVT_PLAY_BEGIN    |  2004 |  Video playback begins. The "loading" icon stops flashing at this point | 
| PLAY_EVT_PLAY_LOADING |  2007 | Video playback is being loaded. If video playback is resumed, this will be followed by a BEGIN event |  
| PLAY_EVT_GET_MESSAGE |  2012 | Used to receive messages inserted into the audio/video stream. For more information, please see [Message Reception](#Message) |  

- **Do not hide the playback view after receiving PLAY_LOADING**
The time length between PLAY_LOADING and PLAY_BEGIN can be different (sometimes 5 seconds, sometimes 5 milliseconds). Some customers consider hiding the view upon LOADING and displaying the view upon BEGIN, which will cause serious flickering (especially in LVB scenarios). It is recommended to place a translucent Loading animation on top of the video view.

### 2. Ending events
| Event ID | Value | Description |   
| :-------------------  |:-------- |  :------------------------ | 
| PLAY_EVT_PLAY_END      |  2006 |  Video playback ends      | 
| PLAY_ERR_NET_DISCONNECT |  -2301  |  Network is disconnected. Too many failed reconnection attempts. Restart the playback for more retries | 

- **<font color='red'>How do I tell whether the LVB is over?</font>**
Because of the varying implementation principles of different standards, many LVB streams usually don't throw end events (2006) and it is expected that when the VJ stops pushing stream, the SDK will soon find that data stream pull fails (WARNING_RECONNECT) and attempt to retry until the PLAY_ERR_NET_DISCONNECT event is thrown after three failed attempts.

 Therefore, you need to listen to both 2006 and -2301 and use the result as the events to determine the end of LVB.


### 3. Warning events
You don't need to consider the following events. We listed the information of these events for synchronization purposes, according to the SDK white-box design concept

| Event ID | Value | Description |   
| :-------------------  |:-------- |  :------------------------ | 
| PLAY_WARNING_VIDEO_DECODE_FAIL   |  2101  | Failed to decode the current video frame  |
| PLAY_WARNING_AUDIO_DECODE_FAIL   |  2102  | Failed to decode the current audio frame  |
| PLAY_WARNING_RECONNECT           |  2103  | Network disconnected, automatic reconnection has started (the PLAY_ERR_NET_DISCONNECT event will be thrown after three failed attempts) |
| PLAY_WARNING_RECV_DATA_LAG       |  2104  | Unstable incoming packet from network: This may be caused by insufficient downstream bandwidth, or unstable outgoing stream at the VJ end |
| PLAY_WARNING_VIDEO_PLAY_LAG       |  2105  | Stutter occurred during the current video playback |
| PLAY_WARNING_HW_ACCELERATION_FAIL |  2106  | Failed to start hard-decoding; Soft-decoding is used |
| PLAY_WARNING_VIDEO_DISCONTINUITY |  2107  | Current video frames are discontinuous and frame loss may occur |
| PLAY_WARNING_DNS_FAIL            |  3001  | RTMP-DNS resolution failed (thrown only if the playback address is RTMP) |
| PLAY_WARNING_SEVER_CONN_FAIL     |  3002  | Failed to connect to RTMP server (thrown only if the playback address is RTMP) |
| PLAY_WARNING_SHAKE_FAIL          |  3003  | RTMP server handshaking failed (thrown only if the playback address is RTMP) |



## Video Width and Height 

**What is the video resolution (in width and height)?**
This question cannot be figured out if SDK only obtains one URL string. To know the width and the height of a video image in pixels, SDK needs to access the cloud server until enough information is loaded to analyze the size of the video image. Therefore, SDK can only tell the video information to your application by notification. 

 The **onNetStatus** notification is triggered once per second to provide real-time feedback on the current status of the pusher. Like a car dashboard, it can offer you a picture about what is happening inside the SDK, so that you can keep track of current network conditions and video information.
  
| Evaluation parameter | Description |   
| :------------------------  |  :------------------------ | 
| NET_STATUS_CPU_USAGE     | Current CPU utilization (instantaneous) | 
| **NET_STATUS_VIDEO_WIDTH**  | Video resolution - Width |
| **NET_STATUS_VIDEO_HEIGHT** | Video resolution - Height |
| NET_STATUS_NET_SPEED     | Current speed at which network data is received |
| NET_STATUS_NET_JITTER    | Network jitter status. A bigger jitter means a more unstable network |
| NET_STATUS_VIDEO_FPS     | The video frame rate of the current stream media    |
| NET_STATUS_VIDEO_BITRATE | Video bitrate of the current stream media (in Kbps) |
| NET_STATUS_AUDIO_BITRATE | Audio bitrate of the current stream media (in Kbps) |
| NET_STATUS_CACHE_SIZE    | Buffer size (jitterbuffer). A buffer length of 0 means that stutter will occur in all probability |
| NET_STATUS_SERVER_IP | IP of the connected server | 


