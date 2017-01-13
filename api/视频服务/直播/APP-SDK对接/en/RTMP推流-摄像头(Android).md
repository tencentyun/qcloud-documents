
## Introduction to RTMP SDK
Tencent Cloud RTMP SDK is a set of RTMP standard LVB solutions developed and launched by Tencent, providing three features, **RTMP Push**, **LVB** and **VOD**. They incorporate years of technical accumulation of the Tencent audio/video team, and many optimizations in video compression, hardware acceleration, beauty filters, audio noise reduction, bit rate control, and so on.

For users new to LVB, it takes only a few lines of codes to complete the interworking process. For users with enough technical knowledge, the rich configuration APIs that the SDK provides also allow you to customize the configuration that best satisfies your demands.

![rtmp sdk push](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/tx_cloud_push_sdk_struct.jpg)

## Downloading RTMP SDK
Find the SDK compressed package of the specified platform in [SDK Download](https://www.qcloud.com/doc/api/258/6172#.E7.A7.BB.E5.8A.A8.E7.AB.AFsdk). The compressed package contains the SDK body and Demo code. Please refer to [Engineering Configuration (Android)](https://www.qcloud.com/doc/api/258/5319) to run it in Xcode. The following interface can be seen if everything proceeds smoothly.
![demo](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/pusher_demo_introduction_2.jpg)

## Interworking Guide
The guide mainly targets the **camera LVB**solution, which is mainly used for beauty show LVB, personal LVB and event LVB and other scenarios.

### Step 1:  Add interface elements
To display the camera preview image, you need to add the following code section in your layout xml file. It will insert a TXCloudVideoView control in your UI. This is the special control used by us to display the camera image:
```xml
<com.tencent.rtmp.ui.TXCloudVideoView
            android:id="@+id/video_view"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:layout_centerInParent="true"
            android:visibility="gone"/>
```

### Step 2:  Create a Pusher object
Create a**TXLivePusher**object, which is use later to complete the push task.

But before you create a LivePush object, you need to specify a **LivePushConfig**object, which is used to determine the configuration parameters of various LivePush aspects, such as push resolution, frames per second (FPS) and GOP (seconds per one I-frame).

Some parameters that we have repeatedly tried have been assigned before a new LivePushConfig object is created. If you do not want to customize the configuration, you can simply assign them to the LivePush object. If you have experience on relevant fields and want to adjust the default configuration, you can read the content of **Advanced**.

```java
TXLivePusher mLivePusher = new TXLivePusher(getActivity());
mLivePushConfig = new TXLivePushConfig();
mLivePusher.setConfig(mLivePushConfig);
```

### Step 3:  Start push
After the preparations in Step 1 and Step 2, you can start push with the following codes:
```java
String rtmpUrl = "rtmp://2157.livepush.myqcloud.com/live/xxxxxx";
mLivePusher.startPusher(rtmpUrl);

TXCloudVideoView mCaptureView = (TXCloudVideoView) view.findViewById(R.id.video_view);
mLivePusher.startCameraPreview(mCaptureView);
```
-**startPusher** is to tell which URL RTMP SDK audio/video streams are pushed to.
- **startCameraPreview** associates the interface element with the Pusher object, thus rendering the image collected by the mobile phone camera to the screen.

### Step 4:  Beauty filters
For the camera LVB scenario, the beauty filter is an essential function. The SDK provides a simple version of implementation, including retouching (level 1 -> level 10) and whitening (level 1 -> level 3) two features.

You can use the slider and other controllers in the user interface of your APP to allow users to choose beauty effects. Or it is recommended that you first use the slider in the Demo to achieve your desired results, and then fix these values to your App's parameters.

```java
mLivePusher.setBeautyFilter(mBeautyLevel, mWhiteningLevel);
```

### Step 5:  Camera control
-**Switch front or rear camera** 
The **front** camera is used by default (this default value can be changed by modifying the configuration function setFrontCamera of TXLivePushConfig), and it is switched each time switchCamera is invoked. Care to be taken to ensure that both the TXLivePushConfig and TXLivePusher objects have been initialized before the camera is switched.
```java
//The front camera is used by default
mLivePusher.switchCamera();
```
-**Turn on or off the flash** 
The flashlight can be turned on for the rear camera only. Besides, this API needs to be invoked after preview starts.
```java
//It is turned on when mFlashTurnOn is set to true; otherwise it is turned off.
if (!mLivePusher.turnOnFlashLight(mFlashTurnOn)) {
        Toast.makeText(getActivity().getApplicationContext(),
            "Failed to turn on the flashlight: Most mobile phones do not support the front flashlight!", Toast.LENGTH_SHORT).show();
}
```
- **Auto or Manual Focus of Camera**
Most rear cameras support focusing. The RTMP SDK supports two focusing mode: **Manual Focus** and **Auto Focus**. 
Auto Focus is a capability provided by the system, but some models do not support Auto Focus.  Manual Focus and Auto Focus are mutually exclusive. After Auto Focus is enabled, Manual Focus will not take effect. 
The RTMP SDK sets Manual Focus by default. You can switch it through the configuration function setTouchFocus API of TXLivePushConfig:
```java
mLivePushConfig.setTouchFocus(mTouchFocus);
mLivePusher.setConfig(mLivePushConfig);
```

### Step 6:  Set logo watermarks
Recently related policies require that LVB videos must be marked with watermarks. We now focus on this function that does not seem particularly important before:
Tencent Cloud supports two watermark settings: one is set in the push SDK settings. The principle is that videos are marked with watermarks in the SDK before being encoded. Another way is to mark watermarks at the cloud end. That is, the cloud end resolves videos and add Logo watermarks.

We suggest that you </font>add watermarks with the SDK<font color = 'red'>, because there are three obvious problems with watermarking at the cloud end:
 (1) This is a cloud machine-consuming service and is not free, which will increase your cost.
 (2) It is not ideally compatible with resolution switching in the push process and other situations and blurred screen may occur.
 (3) It may cause an additional 3s of video delay, which is the result of transcoding.

The SDK requires png watermark pictures, because they have transparency information, which conduces to solving jagged pictures and other problems. (Do not just change the extension of jpg pictures to png in Windows. Professional png pictures need to be processed by professional art designer)

```java
//Set video watermarks
mLivePushConfig.setWatermark(BitmapFactory.decodeResource(getResources(),R.drawable.watermark), 10, 10);
mLivePusher.setConfig(mLivePushConfig);
```

### Step 7:  Hardware encoding
The **setHardwareAcceleration** setting API in TXLivePushConfig can be used to enable or disable hardware encoding.
```java
if (!HWSupportList.isHWVideoEncodeSupport()){
    Toast.makeText(getActivity().getApplicationContext(), 
				   "The current mobile phone model is not whitelisted or the API level is too low (the minimum level is 16). Please enable hardware encoding with caution." , 
				   Toast.LENGTH_SHORT).show();
}
mLivePushConfig.setHardwareAcceleration(true);
mLivePusher.setConfig(mLivePushConfig);  
```

- **Model Whitelist**
> The first sentence in the above example code is invoked by HWSupportList.isHWVideoEncodeSupport. This function is not provided by the RTMP SDK, but is located in the HWSupportList.java file of Demo.
> 
> HWSupportList is a [Whitelist](https://mc.qcloudimg.com/static/archive/a1e796c150ea60246e07947b679e0662/archive.xls) processed by our professional test team. The model in the list is the Android model for which hardware acceleration can be enabled safely. Subsequently we will add more models to this list continuously.

- **Recommended Design**
> The model not whitelisted <font color='red'>** does not necessarily have problems**</font>. The only reason is that there are a lot of Android models and we have no energy to test all. Therefore, if you hope to ** enable hardware acceleration on a model not whitelisted, you'd better add some security mechanisms. For example, a recommended method is as follows:
>  
>  Two or more definition options are provided, e.g., the two steps of standard definition (360\*640) and high definition (540\*960). Here, standard definition can adopt soft encoding because the encoding calculation pressure is not large; high definition adopts hardware encoding.
>  
>  In this way, if hardware acceleration of the high definition step fails, the standard definition step can be used as a guarantee solution.


### Step 8:  Backend push
In the conventional mode, once the App switches to the Backend, the camera's capture ability is disabled by the Android system, which means that the SDK can no longer continue to capture and encode audio/video data. If we do nothing, then the following will happen:
 - Phase 1 (from background switching -> within 10s after that) - Since the CDN does not have data, it cannot provide video streaming to the audience, and the picture seen by the audience does not response.
 - Phase 2 (10s -> 70s) - The player at the audience side exits because it cannot receive the live stream continuously, and nobody is in the studio.
 - Phase 3 (70s later) - The RTMP link of push is directly disconnected by the server. The VJ needs to restart LVB to continue.

Even when the VJ answer a short emergency call, the interactive experience will obviously make all viewers to leave the studio. How can we optimize it?

Actually some speculative approaches can be used, e.g., create a Service, and use SurfaceView of 1\*1 pixel to collect Camera data continuously. However, if you are a VJ and find that an App can still access the camera after the station is switched, do you really dare to use this App?

We need to achieve a perfect balance between privacy protection and ensuring the the audience's experience: We introduced a solution from SDK 1.6.1: 
![](//mc.qcloudimg.com/static/img/6325a9f7918602bd8db15228e6ffe189/image.png)


-**8.1) Set pauseImg**
Before push, use the setPauseImg API of TXLivePushConfig to set a waiting picture. The recommended meaning of the picture is as follows: "The VJ will leave for a while and come back later".
- **8.2) Set setPauseFlag**
>         

- **8.3) Switch to backend process**
If the App is switched to the background during push, although the RTMP SDK cannot collect the camera pictures after the pausePush API function in TXLivePusher is invoked, PauseImg you set just now can be used to continue push.
```java
// activity onStop life cycle function
@Override
public void onStop(){
    super.onStop();
    mCaptureView.onPause();  // mCaptureView is the image rendering view of camera
    mLivePusher.pausePusher(); //Inform the SDK of entry of the "background push mode"
}
```
- **8.4) Switch to front-end process**
After the App is switched back to the frontend and the resumePush API function of TXLivePusher is invoked, the RTMP SDK will continue to collect camera pictures to implement push.
```java
// activity onStop life cycle function
@Override
public void onResume() {
    super.onResume();
    mCaptureView.onResume();     // mCaptureView is the image rendering view of camera
    mLivePusher.resumePusher();  // Notify SDK back to front-end pushing
}
```

### Step 9:  Recommended definition
The video quality is affected by **resolution**, **frame rate** and **bit rate**.
-**Resolution**: The camera LVB has three options of 9:16 conventional resolution: 360\*640, 540\*960, 720\*1280.
-**Frame rate**: If FPS <= 10, viewers will obviously feel lagging. 20 FPS is recommended for camera LVB.
-**Bit rate**: Means the data volume coded by the encoder every second, in units of kbps. For example, 800 kbps means that the encoder will generate 800 kb (or 100 KB) data per second.

Good quality is the result of balance between resolution, frame rate and bit rate. The following are recommended settings for several definition options. Here, the corresponding setting function of TXLivePushConfig is marked in the brackets:

|Step|Resolution (setVideoResolution)| FPS (setVideoFPS)|Bit Rate (setVideoBitrate)|
|---------|---------|---------|---------|
| SD | VIDEO_RESOLUTION_TYPE_360_640 | 20 | 700 kbps |
| HD | VIDEO_RESOLUTION_TYPE_540_960 | 20 | 1000 kbps | 
| Super definition | VIDEO_RESOLUTION_TYPE_720_1280 | 20 | 1500 kbps |

For beauty show LVB, our clients generally choose **HD**, because it is rather balanced: 720p super definition is wasteful for human figures, while 360p cannot make it stand out from other competing products in terms of definition.

### Step 10:  Remind the VJ of "Busy network"
Step 13 will introduce solving RTMP SDK push events. **PUSH_WARNING_NET_BUSY** is very useful, which means: <font color = 'blue'>** the uplink network of the current VJ is busy, and lagging occurs in the viewer end.** </font>

When you receive this WARNING, you can remind through the UI the VJ of changing the network egress, or moving closer to the WiFi. Or you say to him: "Dear, I am using LVB. Do not visit the Taobao website!" What? Not visit Taobao? Then you must be watching Korean TV dramas. "

### Step 11:  Landscape push
In most cases, users often shoot portrait LVB programs and watch portrait videos. Sometimes LVB may need a wider angle, users have to shoot landscape videos and viewers are expected to watch landscape videos. Then portrait push is required. The following two sketches show the effects of landscape shooting and portrait shooting at the viewer end.
![](//mc.qcloudimg.com/static/img/cae1940763d5fd372ad962ed0e066b91/image.png)
><Font color = 'red'>**Note:**</font> In landscape push and portrait push, viewers see pictures of different aspect ratios: 9:16 for portrait and 16: 9 for landscape.

#### Adjusting performance at the viewer end
The **setHomeOrientation** setting option in LivePushConfig needs to be configured. It controls the video aspect ratio seen at the audience end to **16:9** or **6:19**. The adjusted result can be viewed using the player to see whether it meets the expectation.

| Configuration item | Description |
|:---------|---------|
| VIDEO_ANGLE_HOME_RIGHT | Home key on the right
| VIDEO_ANGLE_HOME_DOWN | Home key at the bottom |
| VIDEO_ANGLE_HOME_LEFT | Home key on the left |
| VIDEO_ANGLE_HOME_UP | Home key at the top |

#### Adjusting performance at the VJ end
After the picture performance at the audience end meets the expectation, the remaining work is to adjust the preview picture at the VJ end. Now, the picture rotation direction seen at the VJ end can be rotated through the setRenderRotation API in TXLivePusher. This API provides the four parameters of ** 0, 90, 180 and 270** used to set the rotation angle.

#### Activity Autorotation
The Activity of Android system supports rotation along with the gravity sensing of mobile phone (set android:configChanges). How to achieve the following effect that push of horizontal/vertical screen changes along with the gravity sensing?
![](//mc.qcloudimg.com/static/img/7255ffae57f3e9b7d929a5cb11f85c79/image.png)

```java
    @Override
    public void onConfigurationChanged(Configuration newConfig) {
        // Autorotation is enabled, and only the push direction needs to be changed after Activity rotates along with the mobile phone direction
        int mobileRotation = this.getActivity().getWindowManager().getDefaultDisplay().getRotation();
        int pushRotation = TXLiveConstants.VIDEO_ANGLE_HOME_DOWN;
        switch (mobileRotation) {
            case Surface.ROTATION_0:
                pushRotation = TXLiveConstants.VIDEO_ANGLE_HOME_DOWN;
                break;
            case Surface.ROTATION_90:
                pushRotation = TXLiveConstants.VIDEO_ANGLE_HOME_RIGHT;
                break;
            case Surface.ROTATION_270:、
                pushRotation = TXLiveConstants.VIDEO_ANGLE_HOME_LEFT;
                break;
            default:
                break;
        }
				
				//Set config to validate the setting (push may not be performed again; Tencent Cloud is one of few cloud providers that support hot switching resolution during LVB)
        mLivePusher.setRenderRotation(0); 
        mLivePushConfig.setHomeOrientation(pushRotation);
        mLivePusher.setConfig(mLivePushConfig);
    }
```



### Step 12:  Background mixing
Background remix was supported from RTMP SDK 1.6.1. The VJ may wear a headset or not wear it. The background remix function can be implemented through the following group of APIs in TXLivePusher:

| API | Description |
|---------|---------|
| playBGM | Sends a song via the path. In [Small LVB Demo](https://www.qcloud.com/doc/api/258/6164), we obtain a music file from the iOS local media library |
| stopBGM | Stops playing background music
| pauseBGM | Suspends playing background music
| resumeBGM | Resumes playing background music |
| setMicVolume | Sets the volume of the microphone when mixing. It is recommended to implement a slider in the corresponding UI, for the VJ to set the volume |
| setBGMVolume | Set the volume of the background music when mixing. It is recommended to implement a slider in the corresponding UI, for the VJ to set the volume |

### Step 13:  Solve the problem
#### Event listening
The RTMP SDK listens push related events using the TXLive <font color = 'red'> Push </font> Listener proxy. Note that the TXLive <font color = 'red'> Push </font> Listener only listens the push events with the <font color = 'Red'> PUSH_ </font> prefix.

#### Regular events 
Events notified for every successful push task. For example, event 1003 means that the system is about to render the camera pictures

| Event ID                 ||    Value  |  Description                    |   
| :-------------------  |:-------- |  :------------------------ | 
| PUSH_EVT_CONNECT_SUCC | 1001 | Successfully connected to Tencent Cloud push server |
| PUSH_EVT_PUSH_BEGIN              |  1002 | Handshaking with the server completed, everything is OK, ready to start push |
| PUSH_EVT_OPEN_CAMERA_SUCC | 1003 | The pusher has successfully started the camera (it takes 1-2 seconds on some Android phones) | 

####  Error Codes 
The push task cannot continue for the SDK found some serious problems: for example, you disable the APP's camera permission and the camera does not start.

| Event ID                 ||    Value  |  Description                    |   
| :-------------------  |:-------- |  :------------------------ | 
| PUSH_ERR_OPEN_CAMERA_FAIL        | -1301 | Failed to start the camera |
| PUSH_ERR_OPEN_MIC_FAIL           | -1302 | Failed to start the microphone |
| PUSH_ERR_VIDEO_ENCODE_FAIL       | -1303 | Video coding failed |
| PUSH_ERR_AUDIO_ENCODE_FAIL        -1304 | Audio coding failed |
| PUSH_ERR_UNSUPPORTED_RESOLUTION  | -1305 | Video resolution not supported |
| PUSH_ERR_UNSUPPORTED_SAMPLERATE  | -1306 | Audio sampling rate not supported |
| PUSH_ERR_NET_DISCONNECT          | -1307 | Disconnected from the network, and 3 reconnection attempts fail. Please push again |

#### Warning events 
SDK found some problems which is not incurable. Most warning events will trigger some retrial protection logics or recovery logics, and in most cases the problems can be recovered. Do not make a fuss.

- PUSH_WARNING_NET_BUSY
The VJ network is busy. If you want to remind the VJ via the UI, this warning event is relatively useful (step10).

- PUSH_WARNING_SERVER_DISCONNECT
The push request is rejected by the backend, which will trigger a limited number of retrial logics. The push task may succeed in a retrial. But the truth is that in most scenarios it is because the txSecret in the push address is miscalculated, or because the test address is occupied by others. This warning event is conducive to your debugging.

| Event ID                 ||    Value  |  Description                    |   
| :-------------------  |:-------- |  :------------------------ | 
| PUSH_WARNING_NET_BUSY            | 1101 | Busy network: too small uplink bandwidth, uploading data blocked |
| PUSH_WARNING_RECONNECT           | 1102 | Disconnected from the network, automatic reconnection has started (no retrial after three consecutive automatic reconnections) |
| PUSH_WARNING_HW_ACCELERATION_FAIL |  1103 | Failed to start hard coding, so soft coding is used |
|PUSH_WARNING_DNS_FAIL			  |  3001 |  RTMP -DNS resolution failed (it will trigger the retrial process) |
|PUSH_WARNING_SEVER_CONN_FAIL     |  3002|  Failed to connect the RTMP server (it will trigger the retrial process) |
|PUSH_WARNING_SHAKE_FAIL          |  3003|  RTMP Server Handshaking failed (it will trigger the retrial process) |
|PUSH_WARNING_SERVER_DISCONNECT      |  3004|  The RTMP server is actively disconnected (it will trigger the retrial process) |

> For the definition of all events, see the header file**"TXLiveConstants.java"**

### Step 14:  Push ends
It is very simple to end push, but proper cleaning work is needed. Since neither TXLivePusher used for stream push nor TXCloudVideoView used for displaying image can implement parallel operation of multiple instances, improper cleaning work will lead to adverse effect on the next time of LVB.
```java
/ / The push task is completed. Do clearing work
public void stopRtmpPublish() {
    mLivePusher.stopCameraPreview(true); //Stop camera preview
	mLivePusher.stopPusher();            //Stop push
    mLivePusher.setPushListener(null);   //Unbind the listener
}
```



