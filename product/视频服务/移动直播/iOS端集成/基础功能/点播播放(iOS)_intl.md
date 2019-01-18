## Basics
This document describes the VOD playback feature of Tencent Video Cloud SDK. The following are the basics you must learn before getting started.

- **LVB and VOD**
The video source of <font color='blue'>LVB (LIVE)</font> is pushed by VJ in real time. When the VJ stops broadcasting, the video image on the playback device stops. In addition, the video is broadcasted in real time, no progress bar is displayed when the player is playing the LVB URL.

 The video source of <font color='blue'>Video On-demand (VOD)</font> is a video file on cloud, which can be played at any time as long as it has not been deleted from the cloud. You can control the playback progress using the progress bar. The video playbacks on Tencent Video and Youku Tudou are typical VOD scenarios.

- **Supported Protocols**
 The following are the commonly used VOD protocols. Now, HLS-based VOD URLs are most popular (starting with "http" and ending with ".m3u8"):
![](//mc.qcloudimg.com/static/img/4b42a00bb7ce2f58f362f35397734177/image.jpg)

## Notes
Tencent Cloud SDK <font color='red'>**does not**</font> impose any restrictions on the source of playback URLs, which means you can use the SDK to play videos from both Tencent Cloud and non-Tencent Cloud addresses. But the player in Tencent Video Cloud SDK only supports three LVB video address formats (FLV, RTMP and HLS (m3u8)) and three VOD address formats (MP4, HLS (m3u8) and FLV).

## Interfacing

### Step 1: Create a player
The TXVodPlayer module in Tencent Video Cloud SDK is responsible for the VOD playback feature.

```objectivec
TXVodPlayer *_txVodPlayer = [[TXVodPlayer alloc] init];
[_txVodPlayer setupVideoWidget:_myView insertIndex:0]
```

### Step 2: Render a view
Next, we need to find a place to display the video images in the player. In iOS system, a view is used as the basic rendering unit. Therefore you simply need to prepare a view and configure the layout.

```objectivec
[_txVodPlayer setupVideoWidget:_myView insertIndex:0]
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
TXVodPlayer supports two playback modes from which you may choose.
1. By URL
TXVodPlayer can automatically recognize the playback protocol internally. You only need to pass your playback URL to the startPlay function.
```objectivec
NSString* url = @"http://1252463788.vod2.myqcloud.com/xxxxx/v.f20.mp4";
[_txVodPlayer startPlay:url ];
```
2. By fileID
```objectivec
TXPlayerAuthParams *p = [TXPlayerAuthParams new];
p.appId = 1252463788;
p.fileId = @"4564972819220421305";
[_txVodPlayer startPlayWithParams:p];
```
Find the file in [VOD Video Management](https://console.cloud.tencent.com/video/videolist). The appID and fileID are shown in the video details on the right of the page that opens.

![Video Management](https://mc.qcloudimg.com/static/img/fcad44c3392b229f3a53d5f8b2c52961/image.png)

By using fileID for playback, the player sends request to the backend for the real playback address. You will receive `PLAY_ERR_GET_PLAYINFO_FAIL` event if the network is exceptional or fileID does not exist. Otherwise, the request is successful and you will receive `PLAY_EVT_GET_PLAYINFO_SUCC`.

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
| HOME_ORIENTATION_RIGHT | Home button on the right | 
| HOME_ORIENTATION_DOWN | Home button at the bottom | 
| HOME_ORIENTATION_LEFT |  Home button on the left | 
| HOME_ORIENTATION_UP | Home button at the top | 

![](//mc.qcloudimg.com/static/img/ef948faaf1d62e8ae69e3fe94ab433dc/image.png)


### Step 5: Control the playback
```objectivec
// Adjusts progress
[_txVodPlayer seek:slider.value];
// Pauses playback
[_txVodPlayer pause];
// Resumes playback
[_txVodPlayer resume];
```

### Step 6: End playback
To exit the current UI at the end of playback, be sure to terminate the view control using <font color='red'>**removeVideoWidget**</font>. Otherwise, memory leak or flickering screen will occur.

```objectivec
// Stops playback
[_txVodPlayer stopPlay];
[_txVodPlayer removeVideoWidget]; // Be sure to terminate the view control
```

### Step 7: Screencap
You can capture the current image as a frame by calling **snapshot**. This feature can only capture the frames from the current live stream. To capture the entire UI, call the API of iOS system.

![](//mc.qcloudimg.com/static/img/f63830d29c16ce90d8bdc7440623b0be/image.jpg)

### Step 8: Control the playback speed
The VOD player supports playback speed control. You can set the VOD playback speed, such as 0.5X, 1.0X, 1.2X, 2X, using the API `setRate` to speed up or slow down the playback.

![](//mc.qcloudimg.com/static/img/8666305d62167cfb7c1e670d14fbd689/image.png)

 ```objectivec
//Set the speed to 1.2X
[_txVodPlayer setRate:1.2]; 
// ...
//Start the playback
[_txVodPlayer startPlay:url];
```

### Step 9: Local Cache [UGC version not supported]
In a short video playback scenario, the local caching of video files is a required feature. For viewers, replaying a video should not consume traffic.

- **Supported Formats**
SDK supports caching for files in HLS (m3u8) and MP4 formats.

- **When do I enable the feature?**
By default, caching feature is disabled in the SDK. It is not recommended to enable this feature for scenarios with low replay rates.

- **How do I enable the feature?**
To enable this feature, you need to configure two parameters: local cache directory and the number of videos to be cached.

```objectivec
TXVodPlayConfig _config = [[TXVodPlayConfig alloc] init];

// Set the cache directory
_config.cacheFolderPath = 
[NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES) objectAtIndex:0];

// Set the maximum number of cached files to avoid caching too much data.
_config.maxCacheItems = 10;

[_txVodPlayer setConfig: _config]; 
// ...
//Start the playback
[_txVodPlayer startPlay:playUrl];                            
```

### Step 10: Preloading
In the short video playback scenario, pre-loading helps to ensure a smooth viewing experience. The URL of the next video is loaded at the background during the playback of the current video so that users can play the next video immediately when switching to it, without needing to load it from the start.

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
-(void) onPlayEvent:(TXVodPlayer *)player event:(int)EvtID withParam:(NSDictionary*)param
{
// At the end of playback of video A, directly start the playback of video B for a seamless switching
    if (EvtID == PLAY_EVT_PLAY_END) {
			[_player_A stopPlay];
			[_player_B setupVideoWidget:mVideoContainer insertIndex:0];
			[_player_B resume];
		}
}
```

### Step 11: Pre-roll ads
autoPlay can also be used for pre-roll ads. If autoPlay is set to NO, the player loads the video immediately but does not play it immediately. Pre-roll ads can be presented during the delay between the loading and playback. When the ads end, the video is played using resume function.

### Step 12: Encrypted Playback [UGC version not supported]
Video encryption is mainly used for online education and other scenarios in need of video copyright protection. To encrypt video resources, you not only need to make changes on the player, but also to encrypt and transcode the source video. The engagement of backend and terminal R&D engineers is also required. For more information, please see [Video Encryption Solution](https://cloud.tencent.com/document/product/266/9638) .

TXVodPlayer also supports encrypted playback. You can use the solution where identity verification information is carried in [URL](https://cloud.tencent.com/document/product/266/9638#.E8.A7.86.E9.A2.91.E6.92.AD.E6.94.BE.E6.96.B9.E6.A1.881.EF.BC.9A.E9.80.9A.E8.BF.87querystring.E4.BC.A0.E9.80.92.E8.BA.AB.E4.BB.BD.E8.AE.A4.E8.AF.81.E4.BF.A1.E6.81.AF) . With this solution, you can call the SDK as you would for any other scenario. You can also use the solution where identity verification information is carried in [Cookie](https://cloud.tencent.com/document/product/266/9638#.E8.A7.86.E9.A2.91.E6.92.AD.E6.94.BE.E6.96.B9.E6.A1.882.EF.BC.9A.E9.80.9A.E8.BF.87cookie.E4.BC.A0.E9.80.92.E8.BA.AB.E4.BB.BD.E8.AE.A4.E8.AF.81.E4.BF.A1.E6.81.AF). With this solution, you need to configure the cookie information in the HTTP request head using the headers field of TXVodPlayConfig.

### Step 13: HTTP-REF [UGC version not supported]
The headers in TXVodPlayConfig can be used to set HTTP request headers, such as the Referer field commonly used to prevent URLs from being copied (Tencent Cloud can provide a more secure hotlink protection signature solution), and the cookie field used to verify client identity information.

### Step 14: Hardware acceleration
For blu-ray (1080p) quality, it is difficult to obtain smooth playback experience just by using software decoding. Therefore, if your scenario focuses on gaming LVB, it is recommended to enable hardware acceleration.

It is strongly recommended to perform **stopPlay** before the switching between software decoding and hardware decoding, and perform **startPlay** after switching. Otherwise serious blurred screen problems may occur.

```objectivec
  [_txVodPlayer stopPlay];
  _txVodPlayer.enableHWAcceleration = YES;
  [_txVodPlayer startPlay:_flvUrl type:_type];
```

### Step 15: Multi-bitrate File [UGC version not supported]
The SDK supports hls in multiple bitrates, allowing users to switch between streams in different bitrates. After receiving the PLAY_EVT_PLAY_BEGIN event, you can obtain the array of supported bitrates using the following method:
```objectivec
NSArray *bitrates = [_txVodPlayer supportedBitrates]; //Obtain the array of supported bitrates
```

You can switch between different bitrates using `-[TXVodPlayer setBitrateIndex:]` at any time during the playback. Another stream of data will be pulled during the switch, which may lead to minor stuttering. The SDK has been optimized for Tencent Cloud's multi-bitrate files, which enables the switch between bitrates without any stutter.

## Progress Display

VOD progress is indicated in two metrics: the **loading progress** and **playback progress**. Now, SDK uses event notification to notify the two metrics.

You can bind a **TXVodPlayerListener** listener to the TXVodPlayer object. Then the progress notification calls back your application via the **PLAY_EVT_PLAY_PROGRESS** event whose additional information contains the two progress metrics above.

![](//mc.qcloudimg.com/static/img/6ac5e2fe87e642e6c2e6342d72464f4a/image.png)

```objective
-(void) onPlayEvent:(TXVodPlayer *)player event:(int)EvtID withParam:(NSDictionary*)param {
    if (EvtID == PLAY_EVT_PLAY_PROGRESS) {
		    // Loading progress, in seconds, milliseconds for digits after decimal point
		    float playable = [param[EVT_PLAYABLE_DURATION] floatValue];
				[_loadProgressBar setValue:playable];
				
		    // Playback progress, in seconds, milliseconds for digits after decimal point
		    float progress = [param[EVT_PLAY_PROGRESS] floatValue];
				[_seekProgressBar setValue:progress];
				
			// Video duration, in seconds, milliseconds for digits after decimal point
			float duration = [param[EVT_PLAY_DURATION] floatValue];
			// Used to set duration display, etc.
	}
}
```

## Event Listening
Besides PROGRESS information, SDK synchronizes much other information for your applications through onPlayEvent (event notification) and onNetStatus (status feedback):

### 1. Playback events
| Event ID | Value | Description |   
| :-------------------  |:-------- |  :------------------------ | 
|PLAY_EVT_PLAY_BEGIN    |  2004| Video playing begins. The "loading" icon stops flashing at this point. | 
|PLAY_EVT_PLAY_PROGRESS |  2005|  This refers to the progress of video playback, including current playback progress, loading progress and overall duration. | 
|PLAY_EVT_PLAY_LOADING	|  2007| The video is being loaded. If video playback is resumed, this will be followed by a BEGIN event. |  

### 2. Ending events
| Event ID | Value | Description |   
| :-------------------  |:-------- |  :------------------------ | 
|PLAY_EVT_PLAY_END      |  2006| Video playback ended | 
|PLAY_ERR_NET_DISCONNECT |  -2301  | Network is disconnected. Too many failed reconnection attempts. Restart the playback for more retries | 
|PLAY_ERR_HLS_KEY		| -2305 | Failed to get the HLS decoding key |

### 3. Warning events
You can ignore the following events. They are only used to tell you the internal SDK events.

| Event ID | Value | Description |   
| :-------------------  |:-------- |  :------------------------ | 
| PLAY_WARNING_VIDEO_DECODE_FAIL   |  2101  | Failed to decode the current video frame |
| PLAY_WARNING_AUDIO_DECODE_FAIL   |  2102  | Failed to decode the current audio frame |
| PLAY_WARNING_RECONNECT           |  2103  | Network disconnected and auto reconnection has started (the PLAY_ERR_NET_DISCONNECT event will be thrown after three failed attempts) |
| PLAY_WARNING_RECV_DATA_LAG       |  2104  | Unstable inbound packet: This may be caused by insufficient downstream bandwidth, or inconsistent outbound stream from the VJ end. |
| PLAY_WARNING_VIDEO_PLAY_LAG      |  2105  | Stutter occurred during the video playback |
| PLAY_WARNING_HW_ACCELERATION_FAIL|  2106  | Failed to start hard decoding. Soft decoding is used instead. |
| PLAY_WARNING_VIDEO_DISCONTINUITY |  2107  | Discontinuous sequence of video frames. Some frames may be dropped. |
| PLAY_WARNING_DNS_FAIL            |  3001  | RTMP-DNS resolution failed (thrown only if the playback address is RTMP) |
| PLAY_WARNING_SEVER_CONN_FAIL     |  3002  | Failed to connect to the RTMP server (thrown only if the playback address is RTMP) |
| PLAY_WARNING_SHAKE_FAIL          |  3003  | Handshake with the RTMP server failed (thrown only if the playback address is RTMP) |

### 4. Connection events
In addition, there are several server connection events used to measure and calculate the time for server connections. Also, you don't have to be concerned:

| Event ID | Value | Description |   
| :-----------------------  |:-------- |  :------------------------ | 
| PLAY_EVT_CONNECT_SUCC     |  2001    | Connected to the server |
| PLAY_EVT_RTMP_STREAM_BEGIN|  2002    | Connected to the server. Pull started. (thrown only if the playback address is RTMP) |
| PLAY_EVT_RCV_FIRST_I_FRAME|  2003    | The network has received the first renderable video packet (IDR) |

### 5. Resolution events
The following events are used to obtain image change information. You don't have to be concerned about them.

| Event ID | Value | Description |   
| :-----------------------  |:-------- |  :------------------------ | 
| PLAY_EVT_CHANGE_RESOLUTION|  2009    | Video resolution changed |
| PLAY_EVT_CHANGE_ROATION	|  2011    | MP4 video rotation angle |


## Video Width and Height 
**What is the video resolution (in width and height)?**
This question cannot be figured out if SDK only obtains one URL string. To know the width and the height of a video image in pixels, SDK needs to access the cloud server until enough information is loaded to analyze the size of the video image. Therefore, SDK can only tell the video information to your application by notification. 

 The **onNetStatus** notification is triggered once per second to provide real-time feedback on the current status of the pusher. Like a car dashboard, it can offer you a picture about what is happening inside the SDK, so that you can keep track of current network conditions and video information.
  
| Evaluation parameter | Description |   
| :------------------------  |  :------------------------ | 
| NET_STATUS_CPU_USAGE     | Current (instant) CPU utilization | 
| **NET_STATUS_VIDEO_WIDTH**  | Video resolution - width |
| **NET_STATUS_VIDEO_HEIGHT**| Video resolution - height |
|	NET_STATUS_NET_SPEED     | Current speed at which network data is received |
|	NET_STATUS_VIDEO_FPS     | Video frame rate of the current stream media |
|	NET_STATUS_VIDEO_BITRATE | Video bitrate of the current stream media (in Kbps) |
|	NET_STATUS_AUDIO_BITRATE | Audio bitrate of the current stream media (in Kbps) |
|	NET_STATUS_CACHE_SIZE    | Buffer size (jitterbuffer). A buffer with the length of 0 means that stutter will occur. |
| NET_STATUS_SERVER_IP | IP of the connected server | 

You can call `-[TXVodPlayer width]` and `-[TXVodPlayer height]` to obtain the current width and height.

## Video information
If the video is played via fileID and the request is successful, SDK will inform the upper layer of the request information. You need to resolve the information in param after receiving the `PLAY_EVT_GET_PLAYINFO_SUCC` event.

| Video information | Description |   
| :------------------------  |  :------------------------ | 
| EVT_PLAY_COVER_URL     | Video cover URL | 
| EVT_PLAY_URL  | Video playback URL |
| EVT_PLAY_DURATION | Video duration |

## Offline Download

Offline VOD playback is a commonly needed feature. Users can download videos where there is network connection, and replay the videos where no network connection is available. The SDK supports playing local files, but this is limited to single file formats of mp4 and flv. HLS stream media files cannot be played locally, because they cannot be saved locally. To play HLS offline, you can download HLS locally using `TXVodDownloadManager`.

### Step 1: Preparations

`TXVodDownloadManager` is designed as a singleton. Therefore, you cannot create multiple download objects. The following describes how it is used:

```objective-c
TXVodDownloadManager *downloader = [TXVodDownloadManager shareInstance];
[downloader setDownloadPath:"<Specify a download directory>"];
```

### Step 2: Start download

Start download by either url or fileID. To download via url, simply pass in the download url.

```objective-c
[downloader startDownloadUrl:@"http://1253131631.vod2.myqcloud.com/26f327f9vodgzp1253131631/f4bdff799031868222924043041/playlist.m3u8"]
```

To download via fileID, you need to pass in appID and fileID at least.

```objective-c
TXPlayerAuthParams *auth = [TXPlayerAuthParams new];
auth.appId = 1252463788;
auth.fileId = @"4564972819220421305";
TXVodDownloadDataSource *dataSource = [TXVodDownloadDataSource new];
dataSource.auth = auth;
[downloader startDownload:dataSource];
```

> See https://cloud.tencent.com/document/product/454/12147#step-3.3A-.E5.90.AF.E5.8A.A8.E6.92.AD.E6.94.BE for how to obtain fileID

### Step 3: Query task information 

You need to configure callback delegate before receiving task information.

```objective-c
downloader.delegate = self;
```

Possible task callback results are as follows:

1. -[TXVodDownloadDelegate onDownloadStart:]
   The task is started, indicating that the SDK has started downloading the video.
2. -[TXVodDownloadDelegate onDownloadProgress:]
   Task progress. The SDK calls this API frequently during the download. You can update progress display here.
3. -[TXVodDownloadDelegate onDownloadStop:] 
   The task is stopped. After you call `stopDownload` to stop the download, this message indicates that the task has been stopped successfully.
4. -[TXVodDownloadDelegate onDownloadFinish:] 
   The download is finished, indicating that the video is downloaded completely. The downloaded file can be played by TXVodPlayer.
5. -[TXVodDownloadDelegate onDownloadError:errorMsg:]
   Download error. This API is called back when the network is disconnected during the download. The download is stopped at the same time. See `TXDownloadError` for a full list of error codes.

The callback API contains the `TXVodDownloadMediaInfo` object, because downloader can execute multiple download tasks simultaneously. You can access url or dataSource to determine the download source, and to obtain information such as download progress and file size.

### Step 4: Stop download

To stop the download, call the `-[TXVodDownloadManager stopDownload:]` method, with the object returned via `-[TXVodDownloadManager sartDownloadUrl:]` as the parameter.** The SDK supports resuming download from breakpoint. If the download directory is not changed, you can download the file again from the point where the download is suspended.

If you do not need to resume the download, call the `-[TXVodDownloadManager deleteDownloadFile:]` method to delete the file and free the storage.


