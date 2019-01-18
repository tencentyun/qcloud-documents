## Basics
**Push** means to collect, encode audio/video data and push the data to your specified cloud video platform. The process involves a large amount of basic audio/video-related knowledge, you can only achieve desired results after lots of refining and optimizing.

Tencent Video Cloud SDK mainly helps you push videos on smart phones. The SDK comes with easy-to-use APIs and can be driven by using a single push URL:
![](//mc.qcloudimg.com/static/img/ca7f200c31a9323c032e9e000831ea63/image.jpg)

## Notes
**You can push to non-Tencent Cloud addresses** using this SDK.

To solve the inaccurate DNS mapping problem within China, "Closest route selection" has been introduced starting from SDK 1.5.2. This feature selects the push route nearest to the VJ's location using Tencent Cloud's close route selection server, which significantly improves push quality. However this also means that the route selection results only include Tencent server addresses. In addition, since a large number of customers use dedicated push domain names, SDK cannot determine whether the target is Tencent Cloud simply by using the URL text.

Therefore, if you wish to push videos to addresses of other cloud providers, contact our customer service for help to disable closest route selection feature for your account. This can be done through cloud control, thus there is no need to release new client versions.

## Preparation

- **Acquiring SDK**
[Download](https://cloud.tencent.com/document/product/454/7873) SDK and follow the instructions in [Project Configuration](https://cloud.tencent.com/document/product/454/7877) to add the SDK into your APP development project.

- **Acquiring Test URL**
After [Activating](https://console.cloud.tencent.com/live) the LVB service, use the ["LVB Console" -> "LVB Code Access" -> "Push Generator"](https://console.cloud.tencent.com/live/livecodemanage) to generate push address. For more information, please see [Acquiring Push Playback URL](https://cloud.tencent.com/document/product/454/7915).

#### Code Interfacing
The guide mainly aims for **camera LVB** solution, which is mainly used for scenarios such as beauty show LVB, personal LVB, event LVB.

### Step 1:  Add Interface Elements
To display the camera preview image, you need to add the following codes to your layout xml file. These codes will insert a TXCloudVideoView control, which is a specialized control we use to display the camera image, to your UI.
```xml
<com.tencent.rtmp.ui.TXCloudVideoView
            android:id="@+id/video_view"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:layout_centerInParent="true"
            android:visibility="gone"/>
```

### Step 2:  Create a Pusher Object
Create a **TXLivePusher** object, which will be used later to complete the push task.

Before you create a LivePush object, you need to specify a **LivePushConfig** object to determine the configuration parameters of various LivePush aspects, such as push resolution, frames per second (FPS) and GOP (seconds per one I-frame).

The LivePushConfig object has been equipped with some parameters that we have repeatedly tuned upon creation. If you do not wish to customize these parameters, you can simply assign them to the LivePush object. If you have experience in the related field and want to adjust the default configuration, you can read the **Advance Guide**.

```java
TXLivePusher mLivePusher = new TXLivePusher(getActivity());
mLivePushConfig = new TXLivePushConfig();
mLivePusher.setConfig(mLivePushConfig);
```

### Step 3:  Launch Push
After the preparations in Step 1 and Step 2, you can use the following codes to start the push:
```java
String rtmpUrl = "rtmp://2157.livepush.myqcloud.com/live/xxxxxx";
mLivePusher.startPusher(rtmpUrl);

TXCloudVideoView mCaptureView = (TXCloudVideoView) view.findViewById(R.id.video_view);
mLivePusher.startCameraPreview(mCaptureView);
```
- **startPusher** is used to tell the SDK that which push URL the audio/video streams are being pushed to.
- **startCameraPreview** is used to associate the interface elements with the Pusher object, in order to render the picture captured by the mobile phone camera onto the screen.

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
The setBeautyFilter API can be used to configure beautify and whitening levels (0-9). 0 means to disable beautify feature. The beautify feature has been significantly improved since 1.9.1, now you can obtain optimal video quality if you use the feature together with 540 * 960 resolution (setVideoQuality - VIDEO_QUALITY_HIGH_DEFINITION).
```java
mLivePusher.setBeautyFilter(7, 3);
```

- **Filter**
The setFilter API can be used to configure filter effect. The filter is a histogram file, our designer group provided 8 materials which are packaged inside the Demo by default. You can use them as you like, without considering about copyright issues.
```java
Bitmap bmp = null;
bmp = decodeResource(getResources(), R.drawable.langman);
if (mLivePusher != null) {
       mLivePusher.setFilter(bmp);
}
```
![](//mc.qcloudimg.com/static/img/ad0711f3c35f2087d3520677bfd64391/image.png)
> Be sure to use PNG images if you wish to customize the filters. **Do NOT use JPG image.**

- **Exposure**
setExposureCompensation is used to adjust exposure value. This option is not available on the iOS end (where we use the auto-exposure feature of the system). Considering that Android models can be greatly different from each other and most inexpensive phones may have poor exposure mechanisms, we recommend that you add an auto-exposure slider on the UI to allow VJs to adjust exposure value on their own.
![](//mc.qcloudimg.com/static/img/b4c3fcc20a580347bb1360c5b59fd08c/image.png)
> The parameter of setExposureCompensation is a floating-point value between -1 and 1:  0 means no adjustment; -1 means lowest exposure and 1 means highest exposure.

### Step 6:  Camera Control
- **Switch front or rear camera** 
The **front** camera is used by default (this default value can be changed by modifying the configuration function setFrontCamera in TXLivePushConfig). The camera is switched each time switchCamera is called. Make sure both TXLivePushConfig and TXLivePusher objects have been initialized before switching camera.
```java
// The front camera is used by default
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
- **Auto or Manual Camera Focus**
In most cases, focusing is only supported for the rear camera. The SDK supports two focusing mode: **Manual Focus** and **Auto Focus**.
Auto Focus is a capability provided by the system, but some models do not support Auto Focus. Manual Focus and Auto Focus are mutually exclusive. If Auto Focus is enabled, Manual Focus will not work.
The SDK uses Manual Focus by default. You can switch it through the configuration function setTouchFocus API in TXLivePushConfig:
```java
mLivePushConfig.setTouchFocus(mTouchFocus);
mLivePusher.setConfig(mLivePushConfig);
```

### Step 7:  Set Logo Watermark
Recent policies require that LVB videos must be marked with watermarks. With that in mind, we will focus on this feature that had seemed insignificant before.
Tencent Video Cloud currently supports two watermark settings. One is to set watermark in the push SDK, where the videos are marked with watermarks in the SDK before being encoded. Another is applying watermarks in the cloud. That is, the cloud resolves videos and adds Logo watermarks to them.

We suggest that you **add watermarks with the SDK**, because there are three major problems when watermarking in the cloud:
 (1) This service increases the load on the cloud machine and is not free, which will increase your cost;
 (2) It is not ideally compatible with certain situations such as resolution switching during the push process. This may cause problems like blurred screen.
 (3) It may cause an additional 3-second video delay, which is caused by the transcode service.

SDK requires that watermark images are PNG format, because such images contain transparency information, which helps processes such as anti-aliasing. (Do not just change the extension of a JPG image to PNG in Windows and put it in. Professional PNG logos need to be processed by professional art designers)

```java
//Set video watermark
mLivePushConfig.setWatermark(BitmapFactory.decodeResource(getResources(),R.drawable.watermark), 10, 10);
mLivePusher.setConfig(mLivePushConfig);
```

### Step 8:  Hardware Encoding
The **setHardwareAcceleration** configuration API in TXLivePushConfig can be used to enable or disable hardware encoding.
```java
if (!HWSupportList.isHWVideoEncodeSupport()){
    Toast.makeText(getActivity().getApplicationContext(), 
                   "The current mobile phone model is not whitelisted or the API level is too low (the minimum level is 18). Please think carefully before enabling hardware encoding.", 
                   Toast.LENGTH_SHORT).show();
}
mLivePushConfig.setHardwareAcceleration(mHWVideoEncode);
mLivePusher.setConfig(mLivePushConfig);  
```

mHWVideoEncode includes the following options.

|  Hardware Encoding Option | Description |
| :-----------| :-----------|
| ENCODE_VIDEO_HARDWARE | Enable hardware acceleration |
| ENCODE_VIDEO_SOFTWARE | Disable hardware acceleration (default) |
| ENCODE_VIDEO_AUTO | Automatically determines whether to enable hardware acceleration |


- **Compatibility Assessment**
Android phones now provide better support for hardware acceleration, compared to previous years. However, certain models still have incompatibility problems. Currently, RTMP SDK controls the use of hardware acceleration by using an internal blacklist in order to prevent such problems on models with incompatibility issues. If you failed to use hardware encoding, the SDK will automatically switch to software encoding.

- **Differences**
If you enable hardware acceleration, the phone's battery consumption will significantly decrease, while maintaining an ideal temperature. But there will be more obvious mosaic when there are large movements in the image, compared to software encoding. The mosaic will get worse for earlier, low-end phones. Hardware acceleration is not recommended for users who require high video quality.

- **Recommended Design**
We recommend that you use software acceleration when setVideoQuality is configured as High Definition (recommended definition) or Standard Definition. If you're worrying about CPU usage and high temperature, you can create a simply protection logic: 
> If the **FPS** of the push process stays low for a certain period of time (this can be detected through the NET_STATUS_VIDEO_FPS event of TXLivePushListener), for example, FPS stays below 10 frames/sec in 30 seconds, which means the CPU is overloaded, switch to hardware encoding.

### Step 9:  Background Push
Usually, once the App switches to background, the camera's capture function will be disabled by the Android system, which means the SDK can no longer continue to capture and encode audio/video data. This is what happens if we don't do anything:
 - Phase 1 (from switching to background -> 10 seconds later) - CDN cannot provide video streams to viewers because it doesn't have any data, and the viewers will see a frozen display.
 - Phase 2 (10 seconds -> 70 seconds) - The player at the viewer side exits because it cannot receive LVB stream in a long time. Everyone leaves the studio.
 - Phase 3 (after 70 seconds) - The RTMP linkage of the push is disconnected by the server. The VJ needs to restart LVB to continue.

Even answering a short emergency call will cause all the viewers to leave the studio, with such an interaction experience. So how can we optimize it?

Actually, we can some irregular approaches, e.g., create a Service, and use a SurfaceView with 1\*1 pixel to collect Camera data continuously. However, if you are a VJ and find that the App can still access your camera after it is switched to background, are you really going to use it?

We need to achieve a perfect balance between privacy protection and the viewers' experience, thus we introduced a solution since SDK 1.6.1 version: 
![](//mc.qcloudimg.com/static/img/6325a9f7918602bd8db15228e6ffe189/image.png)


- **9.1) Set pauseImg**
Before the push, use the setPauseImg API in TXLivePushConfig to set a waiting picture. It is recommended to use a picture such as: "The VJ will come back soon".
- **9.2) Set setPauseFlag**
Before the push, use the setPauseFlag API in TXLivePushConfig to configure which collections are to be stopped when the push is paused. The default picture set with pauseImg will be pushed when video collection is stopped, while mute data will be pushed when audio collection is stopped.
>  setPauseFlag(PAUSE_FLAG_PAUSE_VIDEO|PAUSE_FLAG_PAUSE_AUDIO);// means to stop both video collection and audio collection, then push filler audio/video stream;
>         
>  setPauseFlag(PAUSE_FLAG_PAUSE_VIDEO);// means to stop camera video collection while the microphone still collects audio as usual. This is used for scenarios such as when VJ is dressing up;

- **9.3) Switch to background process**
If the App is switched to background during the push process and the pausePush API function in TXLivePusher is called, the SDK will no longer be able to collect camera video but you can still use the PauseImg you previously set to keep up the push.
```java
// onStop life cycle function of activity
@Override
public void onStop(){
    super.onStop();
    mCaptureView.onPause();  // mCaptureView is the image rendering view of the camera
    mLivePusher.pausePusher(); // To inform the SDK that "Background Push Mode" has started
}
```
- **9.4) Switch to foreground process**
After the App is switched back to the foreground and the resumePush API function of TXLivePusher is called, the SDK will continue to collect camera pictures to push.
```java
// onStop life cycle function of activity
@Override
public void onResume() {
    super.onResume();
    mCaptureView.onResume();     // mCaptureView is the image rendering view of the camera
    mLivePusher.resumePusher();  // Inform the SDK to return to foreground to push
}
```


### Step 10:  Remind the VJ "network is poor"
Step 13 will discuss how to handle SDK push events. **PUSH_WARNING_NET_BUSY** is very useful, it means: <font color='blue'>** the uplink network of the VJ is poor, and stutters have occurred in the viewer end.**</font>

When you receive this WARNING, you can use the UI to remind VJ to change network egress, or get closer to the WiFi. Or tell her to say something like this: "Hello dear, I'm streaming! Stop reading eBay! What? Not eBay? Then stop downloading movies!"

### Step 11:  Push in landscape mode
In most cases, VJs push videos in an LVB by holding the screen in a portrait orientation so that the viewers can get portrait images. However, sometimes VJs may need to hold the screen in a landscape orientation to allow the viewers to get landscape images with a wider view. In this case, push in landscape mode is required. The figures below show the difference between landscape mode and portrait mode in terms of the images at the viewer end.
![](//mc.qcloudimg.com/static/img/cae1940763d5fd372ad962ed0e066b91/image.png)
> **Note:** The aspect ratios of images at viewer end are different between landscape mode and portrait mode. In portrait mode, the aspect ratio is 9:16, while in landscape mode, 16:9.

#### Adjust Viewer-end Performance
This is done by configuring the **setHomeOrientation** option in LivePushConfig. It controls whether the video aspect ratio seen by the viewers is **16:9** or **6:19**, you can check the result by using your player to see if the aspect ratio is adjusted as expected.

| Settings | Description |
|:---------|---------|
| VIDEO_ANGLE_HOME_RIGHT | The Home key is on the right |
| VIDEO_ANGLE_HOME_DOWN | The Home key is at the bottom |
| VIDEO_ANGLE_HOME_LEFT | The Home key is on the left |
| VIDEO_ANGLE_HOME_UP | The Home key is at the top |

- **Adjust VJ-end Performance**
When viewers are able to see expected display, you can then adjust the preview display at the VJ side. Now, the picture seen by the VJ can be rotated through the setRenderRotation API in TXLivePusher. This API provides four parameters (**0, 90, 180 and 270**) for setting the rotation angle.

- **Activity Auto-rotation**
The Activity of Android system can rotate according to the feedback of the phone's gravity sensor (configure android:configChanges). How can we make the push switch between landscape mode and portrait mode based on gravity sensor feedback as shown below?
![](//mc.qcloudimg.com/static/img/7255ffae57f3e9b7d929a5cb11f85c79/image.png)
```java
    @Override
    public void onConfigurationChanged(Configuration newConfig) {
        // When auto-rotation is enabled, as Activity rotates with the mobile phone, you simply need to change the push direction
        int mobileRotation = this.getActivity().getWindowManager().getDefaultDisplay().getRotation();
        int pushRotation = TXLiveConstants.VIDEO_ANGLE_HOME_DOWN;
        switch (mobileRotation) {
            case Surface.ROTATION_0:
                pushRotation = TXLiveConstants.VIDEO_ANGLE_HOME_DOWN;
                break;
            case Surface.ROTATION_90:
                pushRotation = TXLiveConstants.VIDEO_ANGLE_HOME_RIGHT;
                break;
            case Surface.ROTATION_270:
                pushRotation = TXLiveConstants.VIDEO_ANGLE_HOME_LEFT;
                break;
            default:
                break;
        }
                
                //Make the configuration effective by setting "config" (there is no need to restart the push process because Tencent Cloud is one of the few cloud providers that support resolution hot-switch during LVB)
        mLivePusher.setRenderRotation(0); 
        mLivePushConfig.setHomeOrientation(pushRotation);
        mLivePusher.setConfig(mLivePushConfig);
    }
```

### Step 12:  Background Music Mix
Background music mixing is supported starting from SDK 1.6.1. The VJ can choose headset mode or no-headset mode. You can achieve background music mixing feature by using the following APIs in TXLivePusher:

| API | Description |
|---------|---------|
| playBGM | Send a song via path. In [Mini LVB Demo](https://cloud.tencent.com/doc/api/258/6164), we obtain music files from the iOS local media library |
| stopBGM | Stop background music |
| pauseBGM | Pause background music |
| resumeBGM | Resume background music |
| setMicVolume | Set the microphone volume when mixing music. It is recommended to add a slider in the UI to allow VJs to set volume on their own |
| setBGMVolume | Set the background music volume when mixing music. It is recommended to add a slider in the UI to allow VJs to set volume on their own |

### Step 13:  End Push
It is simple to end a push process, but proper cleaning work is required. Since only one TXLivePusher object (used for pushing) and only one TXCloudVideoView object (used for displaying image) can run at a time, improper cleaning work may adversely affect the next LVB.
```java
//End the push with proper cleanup work
public void stopRtmpPublish() {
    mLivePusher.stopCameraPreview(true); //End camera preview
    mLivePusher.stopPusher();            //End push
    mLivePusher.setPushListener(null);   //Unbind listener
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
The VJ's network is poor. If you need UI prompts, this warning is relatively more useful (Step 10).

- **WARNING_SERVER_DISCONNECT**
The push request is rejected by backend. This is usually caused by miscalculated txSecret in the push address, or because the push address is occupied by others (a push URL can only have one pushing end at a time).

| Event ID                 |    Value  |  Description                    |   
| :-------------------  |:-------- |  :------------------------ | 
| PUSH_WARNING_NET_BUSY            | 1101 | Bad network condition: data upload is blocked because uplink bandwidth is too small |
| PUSH_WARNING_RECONNECT           | 1102 | Network disconnected, automatic reconnection has started (auto reconnection will be stopped if it fails for three times) |
| PUSH_WARNING_HW_ACCELERATION_FAIL |  1103 | Failed to start hardware encoding. Software encoding is used |
| PUSH_WARNING_DNS_FAIL            |  3001 |  RTMP - DNS resolution failed (this will trigger retry process)        |
| PUSH_WARNING_SEVER_CONN_FAIL     |  3002 |  Failed to connect to the RTMP server (this will trigger retry process)  |
| PUSH_WARNING_SHAKE_FAIL          |  3003 |  RTMP server handshake failed (this will trigger retry process)  |
| PUSH_WARNING_SERVER_DISCONNECT      |  3004 |  The RTMP server actively disconnected (this will trigger retry process)  |

> For the definition of all events, please see the header file **"TXLiveConstants.java"**



