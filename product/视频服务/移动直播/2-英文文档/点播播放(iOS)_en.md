## Basics
This document describes the VOD playback feature of Tencent Video Cloud SDK. The following are the basics you must learn before getting started.

- **LVB and VOD**
<font color='blue'>The video source of LVB (LIVE)</font> is pushed by VJ in real time. When the VJ stops broadcasting, the video image on the playback device stops. In addition, the video is broadcasted in real time, no progress bar is displayed when the player is playing the LVB URL.

 <font color='blue'>The video source of Video On-demand (VOD) </font> is a video file on cloud, which can be played at any time as long as it has not been deleted from the cloud. You can control the playback position using the progress bar. The video playbacks on V.QQ.COM and Youku Tudou are typical VOD scenarios.

- **Supported Protocols**
 The following are the commonly used VOD protocols. Now, HLS-based VOD URLs are most popular (starting with "http" and ending with ".m3u8"):
![](//mc.qcloudimg.com/static/img/4b42a00bb7ce2f58f362f35397734177/image.jpg)

## Notes
Tencent Video Cloud SDK **does not** impose any limit on the source of playback URL, which means it is available for both Tencent Cloud and non-Tencent Cloud playback URLs. But the player in Tencent Video Cloud SDK only supports LVB URLs in FLV, RTMP and HLS (m3u8) formats and VOD URLs in MP4, HLS (m3u8), and FLV formats.

## Interfacing Guide

### Step 1: Create a player
The TXVodPlayer module in Tencent Video Cloud SDK is responsible for the VOD playback feature.

```objectivec
TXVodPlayer _txVodPlayer = [[TXVodPlayer alloc] init];
[_txVodPlayer setupVideoWidget:_myView insertIndex:0]
```

### Step 2: Render a view
Next, we need to find a place to display the video images in the player. In iOS system, a view is used as the basic rendering unit. Therefore you simply need to prepare a view and configure the layout.

```objectivec
[_txVodPlayer setupVideoWidget:_myView insertIndex:0]
```

Technically, the player does not directly render the video image to the view (\_myView in the sample code) you provided. Instead, it creates a subview used for OpenGL rendering on top of the view.

You can adjust the size of the rendered image by simply adjusting the size and position of the view. The SDK will automatically adapt the video images to the size and position of the view.

![](//mccdn.qcloud.com/static/img/75b41bd0e9d8a6c2ec8406dc706de503/image.png)
 
> **How to make an animation?**
> You can freely make animations for a view. But note that the target attribute modified for animations is **transform**, instead of frame.
```objectivec
  [UIView animateWithDuration:0.5 animations:^{
            _myView.transform = CGAffineTransformMakeScale(0.3, 0.3); //Shrink by 1/3
        }];
```

### Step 3: Start playback
TXVodPlayer can automatically recognize the playback protocol internally. You only need to pass your playback URL to the startPlay function.
```objectivec
NSString* url = @"http://1252463788.vod2.myqcloud.com/xxxxx/v.f20.mp4";
[_txVodPlayer startPlay:url ];
```

### Step 4: Image adjustment

- **view: size and position**
You can modify the size and position of the video image by adjusting the size and position of the parameter "view" of setupVideoWidget. The SDK will automatically adapt the video image to the size and position of the view.

- **setRenderMode: Full Screen or Self-Adaption**

| Option | Description  |
|---------|---------|
| RENDER_MODE_FILL_SCREEN | The image spreads across the entire screen proportionally, with the excess parts trimmed off. No black edges are left in this mode, but the image may not be displayed completely because of the trimmed-off areas. | 
| RENDER_MODE_FILL_EDGE | The image is scaled proportionally to adapt to the longest edge. Both the width and the height of the scaled image do not extend beyond the display area and the image is centered. In this mode, black edges may appear in the screen. | 

- **setRenderRotation: Rotation of video image**

| Option | Description  |
|---------|---------|
| RENDER_ROTATION_PORTRAIT | Normal playback (The Home button is located directly below the image) | 
| RENDER_ROTATION_LANDSCAPE | The image rotates 270° clockwise (the Home button is directly to the left of the image) | 

![](//mc.qcloudimg.com/static/img/ef948faaf1d62e8ae69e3fe94ab433dc/image.png)


### Step 5: Playback control
```objectivec
// Adjust progress
[_txVodPlayer seek:slider.value];
// Pause playback
[_txVodPlayer pause];
// Resume playback
[_txVodPlayer resume];
```

### Step 6: End playback
To push the current UI at the end of playback, be sure to terminate the view control using** removeVideoWidget**. Otherwise, memory leak or flickering screen can occur.

```objectivec
// Stop playback
[_txVodPlayer stopPlay];
[_txVodPlayer removeVideoWidget]; // Be sure to terminate the view control
```

### Step 7: Screenshot
You can capture the current image as a frame by calling **snapshot**. This feature can only capture the frames from the current live stream. To capture the entire UI, call the API of iOS system.

![](//mc.qcloudimg.com/static/img/f63830d29c16ce90d8bdc7440623b0be/image.jpg)

### Step 8: Playback speed control
The VOD player supports playback speed control. You can set the VOD playback speed, such as 0.5X, 1.0X, 1.2X, 2X, using the API `setRate` to speed up or slow down the playback.

![](//mc.qcloudimg.com/static/img/8666305d62167cfb7c1e670d14fbd689/image.png)

 ```objectivec
//Set the speed to 1.2X
[_txVodPlayer setRate:1.2]; 
// ...
//Start playback
[_txVodPlayer startPlay:url];
```

### Step 9: Local caching
In a short video playback scenario, the local caching of video files is a required feature. For viewers, replaying a video should not consume traffic.

- **Supported formats**
SDK supports caching for files in HLS(m3u8) and MP4 formats.

- **When to enable the feature?**
By default, caching feature is disabled in the SDK. It is not recommended to enable this feature for scenarios with low replay rates.

- **How to enable the feature?**
To enable this feature, you need to configure two parameters: local cache directory and the number of videos to be cached.

```objectivec
TXVodPlayConfig _config = [[TXVodPlayConfig alloc] init];

// Set the cache directory
_config.cacheFolderPath = 
[NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES) objectAtIndex:0];

// Set the maximum number of cached files to avoid too much data to be cached.
_config.maxCacheItems = 10;

[_txVodPlayer setConfig: _config];
// ...
//Start playback
[_txVodPlayer startPlay:playUrl];
```

### Step 10: Pre-loading
In the short video playback scenario, pre-loading helps to ensure a smooth viewing experience. The URL of the next video is loaded at background during the playback of the current video so that user can play the next video immediately after switching to it, without to need to load it from the start.

This feature allows the seamless switching in VOD, and can be enabled using the isAutoPlay of TXVodPlayer by performing the following operations:

![](//mc.qcloudimg.com/static/img/7331417ebbdfe6306fe96f4b76c8d0ad/image.jpg)

```objectivec
// Play video A: If isAutoPlay is set to YES, the video is loaded and played immediately when startPlay is called.
NSString* url_A = @"http://1252463788.vod2.myqcloud.com/xxxxx/v.f10.mp4";
_player_A.isAutoPlay = YES;
[_player_A startPlay:url_A];

// To pre-load video B while playing video A, set isAutoPlay to NO.
NSString* url_B = @"http://1252463788.vod2.myqcloud.com/xxxxx/v.f20.mp4";
_player_B.isAutoPlay = NO;
[_player_B startPlay:url_B];
```

When video A ends and is automatically or manually switched to video B, call the "resume" function to play video B immediately.
```objectivec
-(void) onPlayEvent:(int)EvtID withParam:(NSDictionary*)param
{
    // At the end of playback of video A, directly start the playback of video B for a seamless switching.
    if (EvtID == PLAY_EVT_PLAY_END) {
			[_player_A stopPlay];
			[_player_B setupVideoWidget:mVideoContainer insertIndex:0];
			[_player_B resume];
		}
}
```

### Step 11: Pre-roll Ads
autoPlay can also be used for pre-roll ads. If autoPlay is set to NO, the player loads the video immediately but does not play it immediately. Pre-roll ads can be presented during the delay between the loading and playback. When the ads end, the video is played using resume function.

### Step 12: Encrypted playback
Video encryption is mainly used in online education and other scenarios where video copyright needs to be protected. To encrypt video resources, you need to make changes to the player and encrypt and transcode the source video. The involvement of developers at both backend and terminals is needed. For more information, please see [Video Encryption Solution](https://cloud.tencent.com/document/product/266/9638). 

TXVodPlayer also supports encrypted playback. You can choose [URL-based Authentication](https://cloud.tencent.com/document/product/266/9638#.E8.A7.86.E9.A2.91.E6.92.AD.E6.94.BE.E6.96.B9.E6.A1.881.EF.BC.9A.E9.80.9A.E8.BF.87querystring.E4.BC.A0.E9.80.92.E8.BA.AB.E4.BB.BD.E8.AE.A4.E8.AF.81.E4.BF.A1.E6.81.AF), in which SDK is called in the same way as usual, or choose [Cookie-based Authentication](https://cloud.tencent.com/document/product/266/9638#.E8.A7.86.E9.A2.91.E6.92.AD.E6.94.BE.E6.96.B9.E6.A1.882.EF.BC.9A.E9.80.9A.E8.BF.87cookie.E4.BC.A0.E9.80.92.E8.BA.AB.E4.BB.BD.E8.AE.A4.E8.AF.81.E4.BF.A1.E6.81.AF), in which you need to configure the cookie information in the HTTP request head using the "headers" field in TXVodPlayConfig.

### Step 13: HTTP-REF
The headers in TXVodPlayConfig can be used to set HTTP request headers, such as the Referer field used to prevent URLs from being copied (Tencent Cloud can provide a more secure hotlink protection signature solution), and the cookie field used to verify client identity information.

### Step 14: Hardware acceleration
For blu-ray (1080p) quality, it is difficult to obtain smooth playback experience just by using software decoding. Therefore, if your scenario focuses on game LVB, it is recommended to enable hardware acceleration.

It is strongly recommended to perform **stopPlay** before the switching between software decoding and hardware decoding, and perform **startPlay** after switching. Otherwise serious blurred screen may occur.

```objectivec
  [_txLivePlayer stopPlay];
  _txLivePlayer.enableHWAcceleration = YES;
  [_txLivePlayer startPlay:_flvUrl type:_type];
```

## Progress Display

VOD progress is indicated with two indicators: **loading progress** and **playback progress**. SDK notifies the two progresses in real time by means of event notification.

You can bind a **TXLivePlayListener** listener to the TXVodPlayer object (the mismatch between the two names is caused by historical reasons) so that the progress notification is called back to your application via **PLAY_EVT_PLAY_PROGRESS** event. The two progress indicators are included in the additional information of this event.

![](//mc.qcloudimg.com/static/img/6ac5e2fe87e642e6c2e6342d72464f4a/image.png)

```objectivec
-(void) onPlayEvent:(int)EvtID withParam:(NSDictionary*)param {
    if (EvtID == PLAY_EVT_PLAY_PROGRESS) {
		    // Loading progress
		    float playable = [param[EVT_PLAYABLE_DURATION] floatValue];
				[_loadProgressBar setValue:playable];
				
		    // Playback progress
		    float progress = [param[EVT_PLAY_PROGRESS] floatValue];
				[_seekProgressBar setValue:progress];
				
			// Video duration
			float duration = [param[EVT_PLAYABLE_DURATION] floatValue];
			// Used to set duration display, etc.
	}
}
```

## Event Listening
In addition to PROGRESS information, SDK synchronizes many other information to your application via onPlayEvent (event notification) and onNetStatus (status feedback):

### 1. Playback Events
| Event ID               |   Value  |  Description                 |   
| :-------------------  |:-------- |  :------------------------ | 
| PLAY_EVT_PLAY_BEGIN    |  2004 |  Video playback begins. The "loading" icon stops flashing at this point | 
| PLAY_EVT_PLAY_PROGRESS | 2005 | The progress of video playback, including current playback progress, loading progress and overall duration. | 
| PLAY_EVT_PLAY_LOADING |  2007 | Video playback is being loaded. If video playback is resumed, this will be followed by a BEGIN event |  

### 2. Ending Events
| Event ID                 |    Value  |  Description                |   
| :-------------------  |:-------- |  :------------------------ | 
| PLAY_EVT_PLAY_END      |  2006 |  Video playback ends   | 
| PUSH_ERR_NET_DISCONNECT |  -2301  |  Network is disconnected, and reconnection attempts failed for multiple times. For more retries, restart playback manually. | 

### 3. Warning Events
You can ignore the following events, which are only used to notify you of some events inside SDK.

| Event ID                 |    Value  |  Description                    |   
| :-------------------  |:-------- |  :------------------------ | 
| PLAY_WARNING_VIDEO_DECODE_FAIL   |  2101  | Failed to decode the current video frame  |
| PLAY_WARNING_AUDIO_DECODE_FAIL   |  2102  | Failed to decode the current audio frame  |
| PLAY_WARNING_RECONNECT           |  2103  | Network is disconnected, and automatic reconnection has started (PLAY_ERR_NET_DISCONNECT event is thrown immediately after three failed reconnection attempts) |
| PLAY_WARNING_RECV_DATA_LAG       |  2104  | Unstable incoming packet from network: This may be caused by insufficient downstream bandwidth, or inconsistent outgoing stream at the VJ end |
| PLAY_WARNING_VIDEO_PLAY_LAG       |  2105  | Stutter occurred during the current video playback |
| PUSH_WARNING_HW_ACCELERATION_FAIL |  2106  | Failed to start hard-decoding; Soft-decoding is used |
| PLAY_WARNING_VIDEO_DISCONTINUITY |  2107  | Current video frames are discontinuous and frame loss may occur |
| PLAY_WARNING_DNS_FAIL            |  3001  | RTMP-DNS resolution failed (thrown only if the playback URL is in an RTMP format) |
| PLAY_WARNING_SEVER_CONN_FAIL     |  3002  | Failed to connect to RTMP server (thrown only if the playback URL is in an RTMP format) |
| PLAY_WARNING_SHAKE_FAIL          |  3003  | RTMP server handshaking failed (thrown only if the playback URL is in an RTMP format) |

### 4. Connection Events
In addition, there are several server connection events used to measure and calculate the time for server connections. Also, you don't have to care about them:

| Event ID                     |    Value  |  Description                    |   
| :-----------------------  |:-------- |  :------------------------ | 
| PLAY_EVT_CONNECT_SUCC     |  2001    | Connected to the server                |
| PLAY_EVT_RTMP_STREAM_BEGIN |  2002    | Connected to the server and started to pull stream (thrown only if the playback URL is in an RTMP format) |
| PLAY_EVT_RCV_FIRST_I_FRAME |  2003    | The network has received the first renderable video packet (IDR)  |

## Video Width and Height 
**What is the video resolution (in width and height)?**
This question cannot be answered if SDK only obtains a URL string. To know the width and height of video image (number of pixels), SDK needs to access the cloud server until enough information is loaded to analyze the size of the video image. Therefore, SDK can only notify your application of the video information by means of notification. 

 The **onNetStatus** notification is triggered once per second to provide real-time feedback on the current status of pusher. It is like a dashboard on the car, giving you a picture of what is going on inside the SDK, so that you can keep track of current network condition and video information.
  
|   Evaluation Parameter                   |  Description                   |   
| :------------------------  |  :------------------------ | 
| NET_STATUS_CPU_USAGE     | Current CPU utilization (instantaneous) | 
| **NET_STATUS_VIDEO_WIDTH**  | Video resolution - width |
| **NET_STATUS_VIDEO_HEIGHT** | Video resolution - height |
| NET_STATUS_NET_SPEED     | Current speed at which network data is received |
| NET_STATUS_VIDEO_FPS     | The video frame rate of the current stream media    |
| NET_STATUS_VIDEO_BITRATE | Video bitrate of the current stream media (in Kbps) |
| NET_STATUS_AUDIO_BITRATE | Audio bitrate of the current stream media (in Kbps) |
| NET_STATUS_CACHE_SIZE    | Buffer size (jitterbuffer). A buffer length of 0 means that stutter will occur in all probability |
| NET_STATUS_SERVER_IP | IP of the connected server | 


