## Basics
This document describes the VOD playback feature of Tencent Video Cloud SDK. The following are the basics you must learn before getting started.

- **LVB and VOD**
<font color='blue'>The video source of LVB (LIVE)</font> is pushed by VJ in real time. When the VJ stops broadcasting, the video image on the playback device stops. In addition, the video is broadcasted in real time, no progress bar is displayed when the player is playing the LVB URL.

 <font color='blue'>The video source of Video On-demand (VOD)</font> is a video file on cloud, which can be played at any time as long as it has not been deleted from the cloud. You can control the playback position using the progress bar. The video playbacks on V.QQ.COM and Youku Tudou are typical VOD scenarios.

- **Supported Protocols**
 The following are the commonly used VOD protocols. Now, HLS-based VOD URLs are most popular (starting with "http" and ending with ".m3u8"):
![](//mc.qcloudimg.com/static/img/4b42a00bb7ce2f58f362f35397734177/image.jpg)

## Notes
Tencent Video Cloud SDK **does not** impose any limit on the source of playback URL, which means it is available for both Tencent Cloud and non-Tencent Cloud playback URLs. But the player in Tencent Video Cloud SDK only supports LVB URLs in FLV, RTMP and HLS (m3u8) formats and VOD URLs in MP4, HLS (m3u8), and FLV formats.

## Interfacing Guide

### Step 1: Add a View
To display the video views in a player, we first need to add the following codes into the layout xml file:
```xml
<com.tencent.rtmp.ui.TXCloudVideoView
            android:id="@+id/video_view"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:layout_centerInParent="true"
            android:visibility="gone"/>
```

### Step 2: Create a player
Next, create a **TXVodPlayer** object, and then use API setPlayerView to associate it with the **video_view** control we just added to the interface.
```java
//mPlayerView is the interface View added in Step 1
TXCloudVideoView mView = (TXCloudVideoView) view.findViewById(R.id.video_view);
//Create a player object
TXVodPlayer mVodPlayer = new TXLivePlayer(getActivity());
//Key player object and interface view
mVodPlayer.setPlayerView(mView);
```

### Step 3: Start playback
TXVodPlayer can automatically recognize the playback protocol internally. You only need to pass your playback URL to the startPlay function.
```java
String url = "http://1252463788.vod2.myqcloud.com/xxxxx/v.f20.mp4";
mVodPlayer.startPlay(url); 
```

### Step 4: Adjust image

- **view: size and position**
You can modify the size and position of the view by directly adjusting the size and position of the "video_view" control added in step 1.

- **setRenderMode: Full Screen or Self-Adaption**

| Option | Description |
|---------|---------|
| RENDER_MODE_FILL_SCREEN | The image spread across the entire screen proportionally, with the excess parts trimed off. No black edges are left in this mode, but the image may not be displayed completely because of the trimmed-off areas. | 
| RENDER_MODE_ADJUST_RESOLUTION | The image is scaled proportionally to adapt to the longest edge. Both the width and the height of the scaled image will not extend beyond the display area and the image is centered. In this mode, black edges maybe appear in the screen. | 

- **setRenderRotation: Rotation of video image**

| Option | Description |
|---------|---------|
| RENDER_ROTATION_PORTRAIT | Normal playback (The Home button is located directly below the image) | 
| RENDER_ROTATION_LANDSCAPE | The image rotates 270° clockwise (the Home button is directly to the left of the image) | 

![](//mc.qcloudimg.com/static/img/ef948faaf1d62e8ae69e3fe94ab433dc/image.png)


### Step 5: Playback control
```java
// Adjust progress
mVodPlayer.seek(seekBar.getProgress());
// Pause playback
mVodPlayer.pause();
// Resume playback
mVodPlayer.resume();
```

### Step 6: End playback
At the end of the playback, **be sure to terminate the View control**, especially before the next startPlay. Otherwise, a lot of memory leaks and splash screen issues will occur.

At the same time, when exiting the playback interface, be sure to call the `onDestroy()` function of the rendering View, otherwise memory leak and the warning message ##"Receiver not registered"## may occur.
```java
@Override
public void onDestroy() {
    super.onDestroy();
    mVodPlayer.stopPlay(true); // true means to clear the last frame
    mView.onDestroy(); 
}
```

The Boolean parameter of stopPlay means **whether to clear the last frame**. The LVB players in the earlier versions of RTMP SDK did not have the concept of Pause, so the boolean value is used to control whether to clear the last frame.

If you want to stop the video at the last frame after the VOD playback ends, do nothing after receiving the playback end event, and it defaults to stop at the last frame.

### Step 7: Screenshot
You can capture the current image as a frame by calling **snapshot**. This feature can only capture the frames from the current live stream. To capture the entire UI, call the API of iOS system.

![](//mc.qcloudimg.com/static/img/f63830d29c16ce90d8bdc7440623b0be/image.jpg)

```java
mLivePlayer.snapshot(new ITXSnapshotListener() {
    @Override
    public void onSnapshot(Bitmap bmp) {
        if (null != bmp) {
           //Acquire screenshot bitmap
        }
    }
});
```

### Step 8: Playback speed control
The VOD player supports playback speed control. You can set the VOD playback speed, such as 0.5X, 1.0X, 1.2X, 2X, using the API `setRate` to speed up or slow down the playback.

![](//mc.qcloudimg.com/static/img/8666305d62167cfb7c1e670d14fbd689/image.png)

 ```java
//The following code is used to show variable speed playback of VOD.
//Set the speed to 1.2X
mLivePlayer.setRate(1.2); 
// ...
//Start playback
mLivePlayer.startPlay(playUrl,_playType);
```

### Step 9: Local caching
In a short video playback scenario, the local caching of video files is a required feature. For viewers, replaying a video should not consume traffic.

- **Supported formats**
SDK supports caching for files in HLS (m3u8) and MP4 formats.

- **When to enable the feature?**
By default, caching feature is disabled in the SDK. It is not recommended to enable this feature for scenarios with low replay rates.

- **How to enable the feature?**
To enable this feature, you need to configure two parameters: local cache directory and the number of videos to be cached.

```java
//Specify a local mp4 cache directory
TXVodPlayConfig mConfig = new TXVodPlayConfig();
mConfig.setCacheFolderPath(
         Environment.getExternalStorageDirectory().getPath(); +"/txcache");
				 
//Specify the maximum number of cached files to avoid too much data to be cached.
mConfig.setMaxCacheItems(10);
mVodPlayer.setConfig(mConfig); 
// ...
//Start playback
mVodPlayer.startPlay(playUrl);                         
```

### Step 10: Pre-loading
In the short video playback scenario, pre-loading helps to ensure a smooth viewing experience. The URL of the next video is loaded at background during the playback of the current video so that users can play the next video immediately when switch to it, without to need to load it from the start.

This feature allows the seamless switching in VOD, and can be enabled using the setAutoPlay of TXVodPlayer by performing the following operations:

![](//mc.qcloudimg.com/static/img/7331417ebbdfe6306fe96f4b76c8d0ad/image.jpg)

```java
// Play video A: If autoPlay is set to true, the video is loaded and played immediately when startPlay is called.
String urlA = "http://1252463788.vod2.myqcloud.com/xxxxx/v.f10.mp4";
playerA.setAutoPlay(true);
playerA.startPlay(urlA);

// To pre-load video B while playing video A, set true to false.
String urlB = @"http://1252463788.vod2.myqcloud.com/xxxxx/v.f20.mp4";
playerB.setAutoPlay(false);
playerB.startPlay(urlB); // The player loads the video immediately but does not play it immediately.
```

When video A ends and is automatically or manually switched to video B, call the "resume" function to play video B immediately.
```java
public void onPlayEvent(int event, Bundle param) {
    // At the end of playback of video A, directly start the playback of video B for a seamless switching
    if (event == PLAY_EVT_PLAY_END) {
           playerA.stop();
           playerB.setPlayerView(mPlayerView);
		   playerB.resume();
		}
}
```

### Step 11: Pre-roll Ads
autoPlay can also be used for pre-roll ads. If autoPlay is set to false, the player loads the video immediately but does not play it immediately. Pre-roll ads can be presented during the delay between the loading and playback. When the ads end, the video is played using resume function.

### Step 12: Encrypted playback
Video encryption is mainly used for online education and other scenarios in need of video copyright protection. To encrypt video resources, you need not only to make changes on the player, but also to encrypt and transcode the source video itself, and engagement of backend and terminal R&D engineers are also required. For more information, please see [Video Encryption Solution](https://cloud.tencent.com/document/product/266/9638).

TXVodPlayer also supports encrypted playback. You can use [URL](https://cloud.tencent.com/document/product/266/9638#.E8.A7.86.E9.A2.91.E6.92.AD.E6.94.BE.E6.96.B9.E6.A1.881.EF.BC.9A.E9.80.9A.E8.BF.87querystring.E4.BC.A0.E9.80.92.E8.BA.AB.E4.BB.BD.E8.AE.A4.E8.AF.81.E4.BF.A1.E6.81.AF) to carry the identity verification information. In this case, SDK's calling method has no difference from the ordinary scenarios. You can also use [Cookie](https://cloud.tencent.com/document/product/266/9638#.E8.A7.86.E9.A2.91.E6.92.AD.E6.94.BE.E6.96.B9.E6.A1.882.EF.BC.9A.E9.80.9A.E8.BF.87cookie.E4.BC.A0.E9.80.92.E8.BA.AB.E4.BB.BD.E8.AE.A4.E8.AF.81.E4.BF.A1.E6.81.AF) to carry the identity verification information. In this case, you need to configure the cookie information in the HTTP request head using the headers field of TXVodPlayConfig.

### Step 13: HTTP-REF
The headers in TXVodPlayConfig can be used to set HTTP request headers, such as the Referer field commonly used to prevent URLs from being copied (Tencent Cloud can provide a more secure hotlink protection signature solution), and the cookie field used to verify client identity information.

### Step 14: Hardware Acceleration
For blu-ray (1080p) quality, it is difficult to obtain smooth playback experience just by using software decoding. Therefore, if your scenario focuses on gaming LVB, it is recommended to enable hardware acceleration.

It is strongly recommended to perform **stopPlay** before the switching between software decoding and hardware decoding, and perform **startPlay** after switching. Otherwise serious blurred screen problems may occur.

```java
 mLivePlayer.stopPlay(true);
 mLivePlayer.enableHardwareDecode(true);
 mLivePlayer.startPlay(flvUrl, type);
```

## Progress Display

VOD progress is indicated in two metrics: the **loading progress** and **playback progress**. Now, SDK uses event notification to notify the two metrics.

You can bind a **TXVodPlayerListener** listener to the TXVodPlayer object. Then the progress notification calls back your application via the **PLAY_EVT_PLAY_PROGRESS** event whose additional information contains the two progress metrics above.

![](//mc.qcloudimg.com/static/img/6ac5e2fe87e642e6c2e6342d72464f4a/image.png)

```java
public void onPlayEvent(int event, Bundle param) {
    if (event == PLAY_EVT_PLAY_PROGRESS) {
		    // Loading progress
		    int duration = param.getInt(TXLiveConstants.EVT_PLAYABLE_DURATION);
				mLoadBar.setProgress(duration);

		    // Playback progress
		    int progress = param.getInt(TXLiveConstants.EVT_PLAY_PROGRESS);
				mSeekBar.setProgress(progress);
				
				// Video duration
		    int duration = param.getInt(TXLiveConstants.EVT_PLAY_DURATION);
			  // Used to set duration display, etc.
	}
}
```

## Event Listening
In addition to PROGRESS information, SDK synchronizes many other information for your applications through onPlayEvent (event notification) and onNetStatus (status feedback):

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
| PLAY_WARNING_RECONNECT           |  2103  | Network is disconnected, and automatic reconnection has started (the PLAY_ERR_NET_DISCONNECT event is thrown immediately after three failed reconnection attempts) |
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
  
|   Evaluation parameter                   |  Description                   |   
| :------------------------  |  :------------------------ | 
| NET_STATUS_CPU_USAGE     | Current CPU utilization (instantaneous) | 
| **NET_STATUS_VIDEO_WIDTH**  | Video resolution - Width |
| **NET_STATUS_VIDEO_HEIGHT** | Video resolution - Height |
| NET_STATUS_NET_SPEED     | Current speed at which network data is received |
| NET_STATUS_VIDEO_FPS     | The video frame rate of the current stream media    |
| NET_STATUS_VIDEO_BITRATE | Video bitrate of the current stream media (in Kbps) |
| NET_STATUS_AUDIO_BITRATE | Audio bitrate of the current stream media (in Kbps) |
| NET_STATUS_CACHE_SIZE    | Buffer size (jitterbuffer). A buffer length of 0 means that stutter will occur in all probability |
| NET_STATUS_SERVER_IP | IP of the connected server | 
