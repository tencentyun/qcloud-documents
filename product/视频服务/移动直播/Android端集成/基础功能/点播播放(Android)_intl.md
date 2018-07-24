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

### Step 1: Add a view
To display the video views in a player, you first need to add the following code into the layout xml file:
```xml
<com.tencent.rtmp.ui.TXCloudVideoView
            android:id="@+id/video_view"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:layout_centerInParent="true"
            android:visibility="gone"/>
```

### Step 2: Create a Player
Next, create a **TXVodPlayer** object, and then use API setPlayerView to associate it with the **video_view** control we just added to the interface.
```java
//mPlayerView is the view added in step 1.
TXCloudVideoView mView = (TXCloudVideoView) view.findViewById(R.id.video_view);
//Create a player object
TXVodPlayer mVodPlayer = new mVodPlayer(getActivity());
//Key player object and interface view
mVodPlayer.setPlayerView(mView);
```

### Step 3: Start playback
TXVodPlayer supports two playback modes from which you may choose.
1. By URL
TXVodPlayer can automatically recognize the playback protocol internally. You only need to pass your playback URL to the startPlay function.
```java
String url = "http://1252463788.vod2.myqcloud.com/xxxxx/v.f20.mp4";
mVodPlayer.startPlay(url); 
```
2. By fileID
```objectivec
TXPlayerAuthBuilder authBuilder = new TXPlayerAuthBuilder();
authBuilder.setAppId(1252463788);
authBuilder.setFileId("4564972819220421305");
mVodPlayer.startPlay(authBuilder); 
```
Find the file in [Video Management](https://console.cloud.tencent.com/video/videolist). The appID and fileID are shown in the video details on the right of the page that opens.

![Video Management](https://mc.qcloudimg.com/static/img/fcad44c3392b229f3a53d5f8b2c52961/image.png)

By using fileID for playback, the player sends request to the backend for the real playback address. You will receive `TXLiveConstants.PLAY_ERR_GET_PLAYINFO_FAIL` event if the network is exceptional or fileID does not exist. Otherwise, the request is successful and you will receive `TXLiveConstants.PLAY_EVT_GET_PLAYINFO_SUCC`.

### Step 4: Adjust the view

- **View: Size and Position**
You can modify the size and position of the view by directly adjusting the size and position of the "video_view" control added in step 1.

- **setRenderMode: Full Screen or Self-Adaption**

| Option | Description  |
|---------|---------|
| RENDER_MODE_FILL_SCREEN | The image spread across the entire screen proportionally, with the excess parts cut out. There are no black edges in this mode, but the image may not be displayed completely because of the cut-out areas. | 
| RENDER_MODE_ADJUST_RESOLUTION | The image is scaled proportionally to adapt to the longest edge. Both the width and the height of the scaled image will not extend beyond the display area and the image is centered. In this mode, black edges maybe appear in the screen. | 

- **setRenderRotation: Screen rotation**

| Option | Description |
|---------|---------|
| RENDER_ROTATION_PORTRAIT | Normal playback (The Home button is located directly below the image) | 
| RENDER_ROTATION_LANDSCAPE | The image rotates 270° clockwise (the Home button is directly to the left of the image) | 

![](//mc.qcloudimg.com/static/img/ef948faaf1d62e8ae69e3fe94ab433dc/image.png)


### Step 5: Control the playback
```java
// Adjusts progress
mVodPlayer.seek(seekBar.getProgress());
// Pauses playback
mVodPlayer.pause();
// Resumes playback
mVodPlayer.resume();
```

### Step 6: End Playback
At the end of the playback, <font color='red'>**be sure to terminate the View control**</font>, especially before the next startPlay. Otherwise a number of memory leak and splash screen issues will occur.

At the same time, when exiting the playback interface, be sure to call the `onDestroy()` function of the rendering View, otherwise memory leak and the warning message <font color='red'>"Receiver not registered"</font> may occur.
```java
@Override
public void onDestroy() {
    super.onDestroy();
    mVodPlayer.stopPlay(true); // "true" means to clear the last frame
    mView.onDestroy(); 
}
```

The boolean parameter of stopPlay means whether to clear the last frame. The LVB players in the earlier versions of RTMP SDK did not have the concept of Pause, so the boolean value is used to control whether to clear the last frame.

If you want to stop the video at the last frame after the VOD playback ends, do nothing after receiving the playback end event, and it defaults to stop at the last frame.

### Step 7: Screencap
You can capture the current image as a frame by calling **snapshot**. This feature can only capture the frames from the current live stream. To capture the entire UI, call the API of Android system.

![](//mc.qcloudimg.com/static/img/f63830d29c16ce90d8bdc7440623b0be/image.jpg)

```java
mVodPlayer.snapshot(new ITXSnapshotListener() {
    @Override
    public void onSnapshot(Bitmap bmp) {
        if (null != bmp) {
           //Acquire screenshot bitmap
        }
    }
});
```

### Step 8: Control the playback speed
The VOD player supports playback speed control. You can set the VOD playback speed, such as 0.5X, 1.0X, 1.2X, 2X, using the API `setRate` to speed up or slow down the playback.

![](//mc.qcloudimg.com/static/img/8666305d62167cfb7c1e670d14fbd689/image.png)

 ```java
//The following code is used to display multi-speed VOD playback.
//Set the speed to 1.2X
mVodPlayer.setRate(1.2); 
// ...
//Start the playback
mVodPlayer.startPlay(playUrl,_playType);
```

### Step 9: Local Cache
In a short video playback scenario, the local caching of video files is a required feature. For viewers, replaying a video should not consume traffic.

- **Supported formats**
SDK supports caching for files in HLS (m3u8) and MP4 formats.

- **When do I enable the feature?**
By default, caching feature is disabled in the SDK. It is not recommended to enable this feature for scenarios with low replay rates.

- **How do I enable the feature?**
To enable this feature, you need to configure two parameters: local cache directory and the number of videos to be cached.

```java
//Specify a local mp4 cache directory
TXVodPlayConfig mConfig = new TXVodPlayConfig();
mConfig.setCacheFolderPath(
         Environment.getExternalStorageDirectory().getPath(); +"/txcache");
                 
//Specify the maximum number of cached files to avoid caching too much data.
mConfig.setMaxCacheItems(10);
mVodPlayer.setConfig(mConfig); 
// ...
//Start the playback
mVodPlayer.startPlay(playUrl);                         
```

> The cached files may be scanned by the system gallery. If you don't want them to be appear at the gallery, create an empty file named ".nomedia" under the cache directory. The system gallery will stop scanning this directory once it finds this file.

### Step 10: Preloading
In the short video playback scenario, pre-loading helps to ensure a smooth viewing experience. The URL of the next video is loaded at the background during the playback of the current video so that users can play the next video immediately when switching to it, without needing to load it from the start.

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
public void onPlayEvent(TXVodPlayer player, int event, Bundle param) {
    // At the end of playback of video A, directly start the playback of video B for a seamless switching
    if (event == PLAY_EVT_PLAY_END) {
           playerA.stop();
           playerB.setPlayerView(mPlayerView);
           playerB.resume();
        }
}
```

### Step 11: Pre-roll ads
autoPlay can also be used for pre-roll ads. If autoPlay is set to false, the player loads the video immediately but does not play it immediately. Pre-roll ads can be presented during the delay between the loading and playback. When the ads end, the video is played using resume function.

### Step 12: Encrypted playback
Video encryption is mainly used for online education and other scenarios in need of video copyright protection. To encrypt video resources, you not only need to make changes on the player, but also to encrypt and transcode the source video. The engagement of backend and terminal R&D engineers is also required. For more information, please see [Video Encryption Solution](https://cloud.tencent.com/document/product/266/9638).

TXVodPlayer also supports encrypted playback. You can use the solution where identity verification information is carried in [URL](https://cloud.tencent.com/document/product/266/9638#.E8.A7.86.E9.A2.91.E6.92.AD.E6.94.BE.E6.96.B9.E6.A1.881.EF.BC.9A.E9.80.9A.E8.BF.87querystring.E4.BC.A0.E9.80.92.E8.BA.AB.E4.BB.BD.E8.AE.A4.E8.AF.81.E4.BF.A1.E6.81.AF). With this solution, you can call the SDK as you would for any other scenario. You can also use the solution where identity verification information is carried in [Cookie](https://cloud.tencent.com/document/product/266/9638#.E8.A7.86.E9.A2.91.E6.92.AD.E6.94.BE.E6.96.B9.E6.A1.882.EF.BC.9A.E9.80.9A.E8.BF.87cookie.E4.BC.A0.E9.80.92.E8.BA.AB.E4.BB.BD.E8.AE.A4.E8.AF.81.E4.BF.A1.E6.81.AF). With this solution, you need to configure the cookie information in the HTTP request head using the headers field of TXVodPlayConfig.

### Step 13: HTTP-REF
The headers in TXVodPlayConfig can be used to set HTTP request headers, such as the Referer field commonly used to prevent URLs from being copied (Tencent Cloud can provide a more secure hotlink protection signature solution), and the cookie field used to verify client identity information.

### Step 14: Hardware acceleration
For blu-ray (1080p) quality, it is difficult to obtain smooth playback experience just by using software decoding. Therefore, if your scenario focuses on gaming LVB, it is recommended to enable hardware acceleration.

It is strongly recommended to perform **stopPlay** before the switching between software decoding and hardware decoding, and perform **startPlay** after switching. Otherwise serious blurred screen problems may occur.

```java
 mVodPlayer.stopPlay(true);
 mVodPlayer.enableHardwareDecode(true);
 mVodPlayer.startPlay(flvUrl, type);
```

### Step 15: Multi-bitrate files
The SDK supports hls in multiple bitrates, allowing users to switch between streams in different bitrates. After receiving the PLAY_EVT_PLAY_BEGIN event, you can obtain the array of supported bitrates using the following method:
```java
ArrayList<TXBitrateItem> bitrates = mVodPlayer.getSupportedBitrates(); //Obtain the array of supported bitrates
```

You can switch between different bitrates using `mVodPlayer.setBitrateIndex(int)` at any time during the playback. Another stream of data will be pulled during the switch, which may lead to minor stuttering. The SDK has been optimized for Tencent Cloud's multi-bitrate files, which enables the switch between bitrates without any stutter.


## Progress Display

VOD progress is indicated in two metrics: the **loading progress** and **playback progress**. Now, SDK uses event notification to notify the two metrics.

You can bind a **TXVodPlayerListener** listener to the TXVodPlayer object. Then the progress notification calls back your application via the **PLAY_EVT_PLAY_PROGRESS** event whose additional information contains the two progress metrics above.

![](//mc.qcloudimg.com/static/img/6ac5e2fe87e642e6c2e6342d72464f4a/image.png)

```java
public void onPlayEvent(TXVodPlayer player, int event, Bundle param) {
    
    if (event == PLAY_EVT_PLAY_PROGRESS) {
            // Loading progress (in sec)
            int duration = param.getInt(TXLiveConstants.EVT_PLAYABLE_DURATION);
                mLoadBar.setProgress(duration);

            // Playback progress (in sec)
            int progress = param.getInt(TXLiveConstants.EVT_PLAY_PROGRESS);
                mSeekBar.setProgress(progress);
                
            // Video duration (in sec)
            int duration = param.getInt(TXLiveConstants.EVT_PLAY_DURATION);
            // Used to set duration display, etc.
    }
}
```

If your VOD playback scenario requires obtaining millisecond timestamp for loading subtitles, use the following callbacks.
```java
public void onPlayEvent(TXVodPlayer player, int event, Bundle param) {
    
    if (event == PLAY_EVT_PLAY_PROGRESS) {
            // Loading progress (in milliseconds)
            int duration_ms = param.getInt(TXLiveConstants.EVT_PLAYABLE_DURATION_MS);
                mLoadBar.setProgress(duration_ms);

            // Playback progress (in milliseconds)
            int progress_ms = param.getInt(TXLiveConstants.EVT_PLAY_PROGRESS_MS);
                mSeekBar.setProgress(progress_ms);
                
            // Video duration (in milliseconds)
            int duration_ms = param.getInt(TXLiveConstants.EVT_PLAY_DURATION_MS);
            // Used to set duration display, etc.
    }
}
```



## Event Listening
Besides PROGRESS information, SDK synchronizes much other information for your applications through onPlayEvent (event notification) and onNetStatus (status feedback):

### 1. Playback events
| Event ID | Value | Description |   
| :-------------------  |:-------- |  :------------------------ | 
|PLAY_EVT_PLAY_BEGIN    | 2004 | Video playback begins. The "loading" icon stops flashing at this point | 
|PLAY_EVT_PLAY_PROGRESS | 2005 | This refers to the progress of video playback, including current playback progress, loading progress and overall duration. | 
|PLAY_EVT_PLAY_LOADING  | 2007 | The video is being loaded. If video playback is resumed, this will be followed by a BEGIN event |  

### 2. Ending events
| Event ID | Value | Description |   
| :-------------------  |:-------- |  :------------------------ | 
|PLAY_EVT_PLAY_END      | 2006 | Video playback ended | 
|PLAY_ERR_NET_DISCONNECT |  -2301 | Network is disconnected. Too many failed reconnection attempts. Restart the playback for more retries | 
|PLAY_ERR_HLS_KEY       | -2305 | Failed to get the HLS decoding key |

### 3. Warning events
You can ignore the following events. They are only used to tell you the internal SDK events.

| Event ID | Value | Description |   
| :-------------------  |:-------- |  :------------------------ | 
| PLAY_WARNING_VIDEO_DECODE_FAIL   |  2101  | Failed to decode the current video frame |
| PLAY_WARNING_AUDIO_DECODE_FAIL   |  2102 | Failed to decode the current audio frame |
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
| PLAY_EVT_RTMP_STREAM_BEGIN|  2002    |  Connected to the server. Pull started. (thrown only if the playback address is RTMP) |
| PLAY_EVT_RCV_FIRST_I_FRAME|  2003    |  The network has received the first renderable video packet (IDR) |


### 5. Resolution events
The following events are used to obtain image change information. You don't have to be concerned about them.

| Event ID | Value | Description |   
| :-----------------------  |:-------- |  :------------------------ | 
| PLAY_EVT_CHANGE_RESOLUTION|  2009    | Video resolution changed |
| PLAY_EVT_CHANGE_ROATION   |  2011    |  MP4 video rotation angle |


## Video Width and Height 
**What is the video resolution (in width and height)?**
This question cannot be figured out if SDK only obtains one URL string. To know the width and the height of a video image in pixels, SDK needs to access the cloud server until enough information is loaded to analyze the size of the video image. Therefore, SDK can only tell the video information to your application by notification. 

 The **onNetStatus** notification is triggered once per second to provide real-time feedback on the current status of the pusher. Like a car dashboard, it can offer you a picture about what is happening inside the SDK, so that you can keep track of current network conditions and video information.
  
| Evaluation parameter | Description |   
| :------------------------  |  :------------------------ | 
| NET_STATUS_CPU_USAGE     | Current (instant) CPU utilization | 
| **NET_STATUS_VIDEO_WIDTH**  | Video resolution - width |
| **NET_STATUS_VIDEO_HEIGHT**| Video resolution - height |
|   NET_STATUS_NET_SPEED     | Current speed at which network data is received |
   NET_STATUS_VIDEO_FPS     |  Video frame rate of the current stream media |
|   NET_STATUS_VIDEO_BITRATE | Video bitrate of the current stream media (in Kbps) |
|   NET_STATUS_AUDIO_BITRATE | Audio bitrate of the current stream media (in Kbps) |
|   NET_STATUS_CACHE_SIZE    | Buffer size (jitterbuffer). A buffer with the length of 0 means that stutter will occur. |
| NET_STATUS_SERVER_IP | IP of the connected server | 

You can call `TXVodPlayer.getWidth()` and `TXVodPlayer.getHeight()` to obtain current width and height.

## Video information
If the video is played via fileID and the request is successful, SDK will inform the upper layer of the request information. You need to resolve the information in param after receiving the `TXLiveConstants.PLAY_EVT_GET_PLAYINFO_SUCC` event.

| Video information | Description |   
| :------------------------  |  :------------------------ | 
| EVT_PLAY_COVER_URL     | Video cover URL | 
| EVT_PLAY_URL  | Video playback URL |
| EVT_PLAY_DURATION | Video duration |


## Offline Download

Offline VOD playback is a commonly needed feature. Users can download videos where there is network connection, and replay the videos where no network connection is available. The SDK supports playing local files, but this is limited to single file formats of mp4 and flv. HLS stream media files cannot be played locally, because they cannot be saved locally. To play HLS offline, you can download HLS locally using `TXVodDownloadManager`.

### Step 1: Preparations

`TXVodDownloadManager` is designed as a singleton. Therefore, you cannot create multiple download objects. The following describes how it is used:

```java
TXVodDownloadManager downloader = TXVodDownloadManager.getInstance();
downloader.setDownloadPath("<Specify a download directory>");
```

### Step 2: Start download

Start download by either url or fileID. To download via url, simply pass in the download url.

```java
downloader.startDownloadUrl("http://1253131631.vod2.myqcloud.com/26f327f9vodgzp1253131631/f4bdff799031868222924043041/playlist.m3u8");
```

To download via fileID, you need to pass in appID and fileID at least.

```java
TXPlayerAuthBuilder auth = new TXPlayerAuthBuilder();
auth.setAppId(1252463788);
auth.setFileId("4564972819220421305");
TXVodDownloadDataSource source = new TXVodDownloadDataSource(auth, QUALITY_OD);
downloader.startDownload(source);
```

> For more information on obtaining fileID, please see https://cloud.tencent.com/document/product/454/12148#step-3.3A-.E5.90.AF.E5.8A.A8.E6.92.AD.E6.94.BE.

### Step 3: Query task information 

You need to configure callback listener before receiving task information.

```java
downloader.setListener(this);
```

Possible task callback results are as follows:

1. void onDownloadStart(TXVodDownloadMediaInfo mediaInfo)
   The task is started, indicating that the SDK has started downloading the video.
2. void onDownloadProgress(TXVodDownloadMediaInfo mediaInfo)
   Task progress. The SDK calls this API frequently during the download. You can update progress display here.
3. void onDownloadStop(TXVodDownloadMediaInfo mediaInfo)
   The task is stopped. After you call `stopDownload` to stop the download, this message indicates that the task has been stopped successfully.
4. void onDownloadFinish(TXVodDownloadMediaInfo mediaInfo)
   The download is finished, indicating that the video is downloaded completely. The downloaded file can be played by TXVodPlayer.
5. void onDownloadError(TXVodDownloadMediaInfo mediaInfo, int error, String reason)
   Download error. This API is called back when the network is disconnected during the download. The download is stopped at the same time. Error code is in `TXVodDownloadManager`.

The callback API contains the `TXVodDownloadMediaInfo` object, because downloader can execute multiple download tasks simultaneously. You can access url or dataSource to determine the download source, and to obtain information such as download progress and file size.

### Step 4: Stop download

To stop the download, call the `downloader.stopDownload()` method, with the object returned via `downloader.startDownload()` as the parameter. The SDK supports resuming download from breakpoint. If the download directory is not changed, you can download the file again from the point where the download is suspended.

If you do not need to resume the download, call the `downloader.deleteDownloadFile()` method to delete the file and free the storage.
