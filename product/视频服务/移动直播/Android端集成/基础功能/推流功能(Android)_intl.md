## Basics
**Push** means pushing the collected and encoded audio/video data to your specified cloud video platform. Since the process involves a large amount of basic audio/video knowledge, you can only achieve desired results after lots of refinements and optimizations.

Tencent Video Cloud SDK mainly helps you push streams on smart phones. The SDK comes with easy-to-use APIs which can be driven by a single push URL.
![](//mc.qcloudimg.com/static/img/ca7f200c31a9323c032e9e000831ea63/image.jpg)

## Notes
- **<font color='red'>Not bound to Tencent Cloud</font>**
> The SDK is not bound to Tencent Cloud. If you want to push streams to non-Tencent Cloud addresses, please set enableNearestIP in TXLivePushConfig to False first. If you want to push streams to Tencent Cloud addresses, set enableNearestIP to True. Otherwise the push quality may be affected due to inaccurate ISP DNS.

## Preparations

- **Acquiring SDK**
[Download](https://cloud.tencent.com/document/product/454/7873) SDK and follow the instructions in [Project Configuration](https://cloud.tencent.com/document/product/454/7877) to add the SDK into your application development project.

- **Acquiring a test URL**
After [activating](https://console.cloud.tencent.com/live) the LVB service, you can use [**LVB Console** -> **LVB Code Access** -> **Push Generator**](https://console.cloud.tencent.com/live/livecodemanage) to generate a push URL. For more information, please see [Acquiring Push/Playback URL](https://cloud.tencent.com/document/product/454/7915).

## Code Interfacing
This guide is specific to **camera LVB** and is mainly used for scenarios such as beauty show LVB, personal LVB and event LVB.

### Step 1: Add interface elements
To display camera preview images, you need to add the following code to your layout xml file. The code will insert a TXCloudVideoView control, which is a specialized control we use to display camera images, to your UI.
```xml
<com.tencent.rtmp.ui.TXCloudVideoView
            android:id="@+id/video_view"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:layout_centerInParent="true"
            android:visibility="gone"/>
```

### Step 2: Create a Pusher object
Create a **TXLivePusher** object, which will be used later to complete the push task.

Before creating a LivePush object, you need to specify a **LivePushConfig** object to determine the configuration parameters for various LivePush push phases, such as push resolution, frames per second (FPS) and GOP (seconds between I frames).

The LivePushConfig is already equipped with some parameters that we have repeatedly tuned as a result of calling new. If you do not wish to customize these parameters, you can simply assign them to the LivePush object. If you have experience in the related field and want to adjust the default configuration, you can read the **Advanced Guide**.

```java
TXLivePusher mLivePusher = new TXLivePusher(getActivity());
mLivePushConfig = new TXLivePushConfig();
mLivePusher.setConfig(mLivePushConfig);
```

### Step 3: Start push
After completing Step 1 and Step 2, you can use the following code to start the push:
```java
String rtmpUrl = "rtmp://2157.livepush.myqcloud.com/live/xxxxxx";
mLivePusher.startPusher(rtmpUrl);

TXCloudVideoView mCaptureView = (TXCloudVideoView) view.findViewById(R.id.video_view);
mLivePusher.startCameraPreview(mCaptureView);
```
- **startPusher** is used to tell the SDK to which push URL the audio/video streams are being pushed.
- **startCameraPreview** is used to associate the interface elements with the Pusher object, in order to render the picture captured by the mobile phone camera onto the screen.


### Step 3+: Audio-only push
For audio-only LVB scenarios, you need to update the push configuration. Perform Step 1 and Step 2 as described above. Configure audio-only push using the following code and start the push.

```java
//The API only takes effect if it is called before push starts.
mLivePushConfig.enablePureAudioPush(true);   // "true" means enabling audio-only push. Default is "false".
mLivePusher.setConfig(mLivePushConfig);      // Reset config.

String rtmpUrl = "rtmp://2157.livepush.myqcloud.com/live/xxxxxx";
mLivePusher.startPusher(rtmpUrl);
```
If you cannot pull streams from URLs in rtmp, flv and hls format after enabling audio-only push, submit a ticket to us.


### Step 4: Configure video definition

You can configure image definition for push using setVideoQuality API.

![](https://main.qcloudimg.com/raw/6e66be90ff14bb8f0603c70668a27ec8.png)

- **Recommended parameter settings**

| Application Scenario | quality |  adjustBitrate | adjustResolution |
|:-------:|:-------:|:-------:|
| Live Show | VIDEO_QUALITY_HIGH_DEFINITION or <br> VIDEO_QUALITY_SUPER_DEFINITION | false | false |
| Mobile game LVB | VIDEO_QUALITY_SUPER_DEFINITION | true | true |
| Joint broadcasting (primary screen) | VIDEO_QUALITY_LINKMIC_MAIN_PUBLISHER | true | true | 
| Joint broadcasting (secondary screen) | VIDEO_QUALITY_LINKMIC_SUB_PUBLISHER | false | false |
| Video chat | VIDEO_QUALITY_REALTIEM_VIDEOCHAT | true | true | 

- **Internal data metrics**

| quality | adjustBitrate | adjustResolution | Bitrate Range | Resolution Range | 
|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
| STANDARD | true | true | 300~800kbps| 270x480 ~ 360x640| 
| STANDARD | true | false |300~800kbps|360x640| 
| STANDARD | true | false | 800kbps | 360x640| 
| HIGH | true | true |600~1500kbps| 360x640~540x960| 
| HIGH | true | false |600~1500kbps| 540x960| 
| HIGH | false | false |1200kbps| 540x960| 
| SUPER | true | true | 600~1800kbps|360x640~720x1280|
| SUPER | true | false |600~1800kbps|720x1280|
| SUPER | false | false |1800kbps|720x1280|
| MAIN_PUBLISHER | true | true |600~1500kbps| 360x640~540x960| 
| SUB_PUBLISHER | false | false |350kbps| 320x480| 
| VIDEOCHAT | true | true | 200~800kbps| 190x320~360x640| 

### Step 5: Beauty filter
![](//mc.qcloudimg.com/static/img/aac647073cf0641141900e775e929418/image.png)
- **Beauty filter**
You can set beauty filter style, dermabrasion level, whitening level, and blushing level using setBeautyFilter API. You can obtain the best video quality using beauty filter with 540*960 resolution (setVideoQuality - VIDEO_QUALITY_HIGH_DEFINITION):
```java
 //style             Dermabrasion style: 0: Smooth 1: Natural 2: Hazy
 //beautyLevel       Dermabrasion level: Value range: 0-9. 0 means disabling beauty filter. Default is 0, i.e., disabling beauty filter.
 //whiteningLevel    Whitening level: Value range: 0-9. 0 means disabling whitening. Default is 0, i.e., disabling whitening.
 //ruddyLevel        Blushing level: Value range: 0-9. 0 means disabling blushing. Default is 0, i.e., disabling blushing. 
 //
 public boolean setBeautyFilter(int style, int beautyLevel, int whiteningLevel, int ruddyLevel);
```
 
- **Filter**
The setFilter API can be used to configure filter effects. A filter is actually a histogram file. Our designer group provides 8 materials which are packaged inside the Demo by default. You can use them as you like, without considering about copyright issues.

 The setSpecialRatio API is used to configure the effect level of a filter (0-1). A higher value means a stronger effect. Default is 0.5.
```java
Bitmap bmp = null;
bmp = decodeResource(getResources(), R.drawable.langman);
if (mLivePusher != null) {
       mLivePusher.setFilter(bmp);
}
```
> Use PNG images if you need to customize the filters. <font color='red'>Do NOT use JPG images.</font>

- **Exposure**
setExposureCompensation is used to adjust exposure value. This option is not available for iOS devices (auto-exposure is adopted). But Android devices are significantly different from iOS ones, and some low-end Android phones have an unsatisfactory auto-exposure effect. Therefore, it is recommended to provide a slider on the page for VJs to adjust exposure value manually.
> The parameter of setExposureCompensation is a floating-point value between -1 and 1: 0 - no adjustment; -1 - minimum exposure; 1 - maximum exposure.

### Step 6: Control the camera
- **Switch between front and rear cameras** 
The **front** camera is used by default (this default value can be changed by modifying the configuration function setFrontCamera in TXLivePushConfig). The camera is switched each time switchCamera is called. Make sure both TXLivePushConfig and TXLivePusher objects have been initialized before switching camera.
```java
//The front camera is used by default
mLivePusher.switchCamera();
```
- **Turn the flashlight on or off** 
Flashlight is only available for the rear camera. In addition, this API needs to be called after preview is started.
```java
//Flashlight is turned on if mFlashTurnOn is set to true; otherwise it is turned off
if (!mLivePusher.turnOnFlashLight(mFlashTurnOn)) {
        Toast.makeText(getActivity().getApplicationContext(),
            "Failed to turn on flashlight: Most mobile phones do not support a front flashlight!", Toast.LENGTH_SHORT).show();
}
```
- **Auto or manual focus of camera**
In most cases, focusing is only supported for the rear camera. The SDK supports two focusing modes: **Manual Focus** and **Auto Focus**.
Auto Focus is a capability provided by the system, but some models do not support Auto Focus. Manual Focus and Auto Focus are mutually exclusive. If Auto Focus is enabled, Manual Focus will not work.
The SDK uses Manual Focus by default. You can switch it through the configuration function setTouchFocus API in TXLivePushConfig:
```java
mLivePushConfig.setTouchFocus(mTouchFocus);
mLivePusher.setConfig(mLivePushConfig);
```

- **Set mirroring effect**
VJs usually use the front camera in LVBs. As a result, the images displayed at the viewer end are horizontally reversed from the preview images at the VJ end. It is the same as how you look in a mirror and see your reflection. To keep the image displayed at the viewer end consistent with that at the VJ end, you need to set horizontal mirroring at the viewer end.
```Java
//After mLivePusher.setConfig(mLivePushConfig), call 
mLivePusher.setMirror(true);
```


### Step 7: Set Logo watermark
Recent policies require that LVB videos must be marked with watermarks. With that in mind, we will focus on this feature that had seemed insignificant before.
Tencent Video Cloud supports two watermark setting methods. One is to set watermark in the push SDK, where the videos are marked with watermarks in the SDK before being encoded. Another is to apply watermarks in the cloud. That is, the cloud resolves videos and adds Logo watermarks to them.

We suggest that you <font color='red'>add watermarks with the SDK</font>, because there are three major problems when watermarking in the cloud:
 (1) This service increases load on the cloud machine and is not free, which will increase your cost.
 (2) It is not ideally compatible with certain situations such as resolution switching during the push process. This may cause problems like blurred screen.
 (3) It may bring about an extra 3-second video delay, which is caused by the transcode service.

The SDK requires that watermark images are in PNG format, because such images contain transparency information, which helps better solve issues like jagged screen. (Do not just change the extension of a JPG image to PNG in Windows and use it as a watermark image. Professional PNG logos need to be processed by professional art designers)

```java
//Set video watermark
mLivePushConfig.setWatermark(BitmapFactory.decodeResource(getResources(),R.drawable.watermark), 10, 10);
//The last two parameters are the X and the Y coordinates of the watermark position.
mLivePusher.setConfig(mLivePushConfig);
```

Call the watermark normalization API if you need to adjust the position of the watermark image to the model.
```java
//Set video watermark
mLivePushConfig.setWatermark(mBitmap, 0.02f, 0.05f, 0.2f);
//The parameters are the Bitmap of the watermark image, the X and the Y coordinates of the watermark position, and the watermark width. The available value range for the last three parameters is [0, 1].
//The last two parameters are the X and the Y coordinates of the watermark position.
mLivePusher.setConfig(mLivePushConfig);
```

### Step 8: Hardware encoding
The **setHardwareAcceleration** configuration API in TXLivePushConfig can be used to enable or disable hardware encoding.
```java
if (mHWVideoEncode){
    if (mLivePushConfig != null) {
        if(Build.VERSION.SDK_INT < 18){
            Toast.makeText(getApplicationContext(), "Hardware acceleration failed. API level of this phone is too low (the minimum level is 18).", 
                Toast.LENGTH_SHORT).show();
            mHWVideoEncode = false;
        }
    }
}

mLivePushConfig.setHardwareAcceleration(mHWVideoEncode ? 
    TXLiveConstants.ENCODE_VIDEO_HARDWARE : TXLiveConstants.ENCODE_VIDEO_SOFTWARE);
mLivePusher.setConfig(mLivePushConfig);  

//It is recommended to use ENCODE_VIDEO_AUTO if you don't know when to enable hardware encoding.
// Software encoding is enabled by default. However, the SDK will switch to hardware encoding automatically when the CPU usage of your phone exceeds 80% or the frame rate is <= 10.
```

Options for mHWVideoEncode  are as below:

|  Hardware Acceleration Option | Description |
| :-----------| :-----------|
| ENCODE_VIDEO_HARDWARE | Enables hardware acceleration |
| ENCODE_VIDEO_SOFTWARE | Disables hardware acceleration (default) |
| ENCODE_VIDEO_AUTO | Automatically selects whether to enable hardware acceleration |


- **Compatibility assessment**
Android phones now provide better support for hardware acceleration than previous years. However, certain models still have incompatibility problems. The RTMP SDK controls the use of hardware acceleration by using an internal blacklist to avoid problems on models with poor compatibility. If you failed to use hardware encoding, the SDK will automatically switch to software encoding.

- **Differences**
After hardware acceleration is enabled, the phone's battery consumption will be significantly lowered, and the phone will be maintained at an ideal temperature. However, dynamic images will contain more mosaics under hardware acceleration than under software encoding, which is worse in earlier low-end phones. Hardware acceleration is not recommended for users who require high video quality.

- **Recommended design**
We recommend that you use software encoding when setVideoQuality is configured as High Definition (recommended definition) or Standard Definition. If you're worrying about CPU usage and high temperature, you can create a simply protection logic: 
> If the **FPS** of the push stays low for a certain period of time (this can be detected through the NET_STATUS_VIDEO_FPS event of TXLivePushListener), for example, the FPS stays below 10 frames/sec in 30 seconds, it means the CPU is overloaded, and you can switch to hard encoding.

### Step 9: Local recording
You can start local recording using startRecord API. The recording format is MP4. You can specify the storage path for the MP4 files using videoFilePath.
- Do not change resolution and soft/hard encoding during recording. Otherwise, exceptions may exist in the generated videos.
- For cloud recording, you only need to concatenate &record=mp4 to the end of the push URL. For more information, please see [Cloud Recording](https://cloud.tencent.com/document/product/454/7917).
- You can configure TXRecordCommon.ITXVideoRecordListener listener for TXLivePusher through the setVideoRecordListener API to get recording event notifications.

```java
// Start recording: If the recording starts successfully, "0" is returned. If the recording is already in progress and the new recording request is ignored, "-1" is returned. If the push has not started and the recording fails to start, "-2" is returned.
public int startRecord(final String videoFilePath) 
// End recording
public void stopRecord() 
//
// Video recording callback
public interface ITXVideoRecordListener {
        void onRecordEvent(final int event, final Bundle param);
        void onRecordProgress(long milliSecond);
        void onRecordComplete(TXRecordResult result);
}
```

### Step 10: Push at the backend
Usually, once the App switches to the backend, the camera's capture feature will be disabled by the Android system, which means the SDK cannot continue capturing and encoding audio/video data. This is what happens if we don't do anything:
 - Phase 1 (from switching to the backend -> 10 seconds later) - CDN cannot provide video streams to viewers because it doesn't have any data, and the viewers will see a frozen display.
 - Phase 2 (10 seconds -> 70 seconds) - The player at the viewer end exits because it haven't received LVB streams for a long time. Everyone leaves the room.
 - Phase 3 (after 70 seconds) - The RTMP linkage of the push is disconnected by the server. The VJ needs to restart LVB to continue.
Even a short pause caused by an emergency phone call for the VJ may lead to early end of the LVB due to cloud service providers' security measures.

You can avoid this problem by following the steps below:
![](//mc.qcloudimg.com/static/img/6325a9f7918602bd8db15228e6ffe189/image.png)

- **10.1 Set pauseImg**
Before push starts, you can use the setPauseImg API of TXLivePushConfig to set a waiting picture saying like "The VJ will come back soon".
```java
    mLivePushConfig.setPauseImg(300,5);
    // 300 is the maximum duration of the image displayed at the pause of backend push (in sec).
    // 10 is the frame rate of the image displayed at the pause of backend push. The minimum is 5 and the maximum is 20.
    Bitmap bitmap = decodeResource(getResources(), R.drawable.pause_publish);
    mLivePushConfig.setPauseImg(bitmap);
    // The size of the image displayed at the pause of backend push cannot exceed 1920*1920.
    mLivePusher.setConfig(mLivePushConfig);  
```

- **10.2 Set setPauseFlag**
Before push starts, you can use the setPauseFlag API in TXLivePushConfig to configure to stop collecting which streams when the App is switched to the backend and the push is paused. The default picture set with pauseImg will be pushed if video collection is stopped, while mute data will be pushed if audio collection is stopped.
>  setPauseFlag(PAUSE_FLAG_PAUSE_VIDEO|PAUSE_FLAG_PAUSE_AUDIO);// It means stopping both video collection and audio collection, and pushing the filler audio/video stream;
>         
>  setPauseFlag(PAUSE_FLAG_PAUSE_VIDEO);// It means stopping the camera from collecting video images but leaving the microphone open. This is used for scenarios such as when a VJ changes clothes;

- **10.3 Switch to the backend**
If the App is switched to the backend during push and the pausePush API function in TXLivePusher is called, the SDK will be unable to collect camera images, but it can keep pushing streams via pauseImg you just configured.
```java
// onStop lifecycle function of activity
@Override
public void onStop(){
    super.onStop();
    mCaptureView.onPause();  // mCaptureView is the image rendering view of the camera
    mLivePusher.pausePusher(); // Inform the SDK that "Backend Push Mode" has started
}
```
- **10.4 Switch to the frontend**
After the App is switched back to the frontend and the resumePush API function of TXLivePusher is called, the SDK will resume collecting camera pictures to push.
```java
// onStop lifecycle function of activity
@Override
public void onResume() {
    super.onResume();
    mCaptureView.onResume();     // mCaptureView is the image rendering view of the camera
    mLivePusher.resumePusher();  // Inform the SDK that the App is switched to the frontend
}
```

### Step 10+: Push captured camera images at the backend
To allow viewers to see camera images when the VJ switches to the backend or other pages, configure as follows:
1. Skip step 10.1 and step 10.2.
2. In step 10.3, annotate mLivePusher.pausePusher().
3. In step 10.4, annotate mLivePusher.resumePusher().

**<font color='red'>Note</font>**: Pay attention to the protection of VJs' privacy when this feature is enabled.

### Step 11: Network condition warning
- What should we do if the network quality is poor at the VJ end? 
- Should we lower the definition to ensure the smoothness? It will lead to blurry video images with many mosaics at the viewer end.
- Should we drop some of the video frames to maintain the image definition? It will lead to continuous stutter at the viewer end.
- Since neither of the above is satisfactory, what should we do?
- We all know that it's impossible to "eat your cake and have it."

You can capture the **PUSH_WARNING_NET_BUSY** event by using onPlayEvent in TXLivePushListener. This event indicates that the VJ's network is extremely poor and stutters occur at the viewer end.

You can prompt the VJ with a message indicating **"Poor network quality. Please move closer to your WiFi, and make sure the signal isn't blocked by any wall or obstacle"**.

### Step 12: Push in landscape mode
Sometimes VJs may need to hold the screen in a landscape orientation to allow the viewers to get landscape images with a wider view. In this case, push in landscape mode is required. The figures below show the difference between landscape mode and portrait mode in terms of the images at the viewer end:
![](//mc.qcloudimg.com/static/img/cae1940763d5fd372ad962ed0e066b91/image.png)

- **Adjust image display at the viewer end**
The **setHomeOrientation** in LivePushConfig can be used to **set phone rotation angle to 0, 90, 180 or 270**. You can check whether the rotation angle of video images is set as expected by using the player Demo.
```java
// Your phone is in portrait mode and its Home button is at the bottom. Rotate 0 degrees.
 mLivePushConfig.setHomeOrientation(TXLiveConstants.VIDEO_ANGLE_HOME_DOWN); 
 // Your phone is in landscape mode and its Home button is to the right. Rotate 270 degrees.
 mLivePushConfig.setHomeOrientation(TXLiveConstants.VIDEO_ANGLE_HOME_RIGHT); 
```

- **Adjust image display at the VJ end**
After the video image display at the viewer end meets your expectations, you need to adjust the preview image display at the VJ end. You can set the image rotation, i.e., the aspect ratio of video images at the VJ end to be **16:9** or **6:19** using setRenderRotation API in TXLivePusher.
```Java
// Your phone is in portrait mode, and local rendering is done with 0 degree offset to the vertical line.
mLivePusher.setRenderRotation(0);
// Your phone is in landscape mode, and local rendering is done with 90 degree offset to the vertical line.
mLivePusher.setRenderRotation(90);
```


- **Activity auto-rotation**
The Activity of Android systems can rotate according to the feedback of the phone's gravity sensor (configure android:configChanges). For more information on how to achieve Activity auto-rotation as shown below, please see [CODE](https://cloud.tencent.com/document/product/454/9876).
![](//mc.qcloudimg.com/static/img/7255ffae57f3e9b7d929a5cb11f85c79/image.png)


### Step 13: Background audio mixing
SDK 1.6.1 and later versions support background audio mixing, and VJs can choose to wear or not wear a headset. You can implement background audio mixing by using the following APIs in TXLivePusher:

| API | Description |
|---------|---------|
| playBGM | Passes a piece of music via path. In [Mini LVB Demo](https://cloud.tencent.com/doc/api/258/6164), we obtain music files from the iOS local media library |
| stopBGM | Stops background music |
| pauseBGM | Pauses background music |
| resumeBGM | Resumes background music |
| setMicVolume | Sets microphone volume for audio mixing. It is recommended to add a slider in the UI to allow VJs to set volume on their own |
| setBGMVolume | Sets background music volume for audio mixing. It is recommended to add a slider in the UI to allow VJs to set volume on their own |

### Step 14: End push
Ending a push is simple, but proper cleanup work is required. Since only one TXLivePusher object (used for pushing streams) and only one TXCloudVideoView object (used for displaying images) can run at a time, improper cleanup may adversely affect the next LVB.
```java
//End a push with proper cleanup
public void stopRtmpPublish() {
    mLivePusher.stopCameraPreview(true); //Stop camera preview
    mLivePusher.stopPusher();            //Stop push
    mLivePusher.setPushListener(null);   //Unbind listener
}
```


<h2 id="Message"> Send messages </h2>
This feature is used to deliver certain custom messages from the pusher end to the viewer end via audio/video lines. It is applicable to the following scenarios:
1. Online quiz: The pusher end delivers the **questions** to the viewer end. Perfect "sound-image-question" synchronization can be achieved.
2. Live show: The pusher end delivers **lyrics** to the viewer end. The lyric effect can be displayed on the viewer end in real time and its image quality is not affected by video encoding.
3. Online education: The pusher end delivers the operations of **Laser pointer** and **Doodle pen** to the viewer end. The drawing can be performed at the viewer end in real time.

```java
//Android sample code
mTXLivePusher.sendMessage(questionInfo.getBytes("UTF-8"));
```

> onPlayEvent (PLAY_EVT_GET_MESSAGE) in TXLivePlayer can be used for the viewer end to receive messages. For more information, please see [playback document](https://cloud.tencent.com/document/product/454/7886#Message)


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
| PUSH_EVT_CHANGE_RESOLUTION | 1005 | Resolution is changed dynamically during push |
| PUSH_EVT_CHANGE_BITRATE | 1006 | Bitrate is changed dynamically during push |

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
The VJ's network is poor. This warning can be used as a UI message for users (Step 10).

- <font color='red'>**WARNING_SERVER_DISCONNECT**</font>
The push request is rejected by backend. This is usually caused by miscalculated txSecret in the push URL, or because the push URL is already in use (a push URL can only be used by one pusher at a time).

| Event ID | Value | Description |   
| :-------------------  |:-------- |  :------------------------ | 
| PUSH_WARNING_NET_BUSY | 1101 | Bad network condition: data upload is blocked because upstream bandwidth is too small. |
| PUSH_WARNING_RECONNECT | 1102 | Network disconnected. Auto reconnection has been initiated (no more attempts will be made after three failed attempts). |
| PUSH_WARNING_HW_ACCELERATION_FAIL | 1103 | Failed to start hard encoding. Soft encoding is used instead. |
| PUSH_WARNING_DNS_FAIL | 3001 | RTMP - DNS resolution failed (this triggers a retry) |
| PUSH_WARNING_SEVER_CONN_FAIL | 3002 | Failed to connect to the RTMP server (this triggers a retry) |
| PUSH_WARNING_SHAKE_FAIL | 3003 | Handshake with RTMP server failed (this triggers a retry) |
| PUSH_WARNING_SERVER_DISCONNECT | 3004 | The RTMP server disconnected automatically (this triggers a retry) |

> For the definitions of all events, please see the header file **"TXLiveConstants.java"**.



