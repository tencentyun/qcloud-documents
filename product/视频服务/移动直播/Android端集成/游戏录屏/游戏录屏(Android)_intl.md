
## Mobile Phone Screencap
RTMP SDK 1.6.1 has begun to support screencap LVB on mobile phones, that is, the VJ's mobile phone screen can be used as the LVB source. Meanwhile, camera preview can be overlaid and used for scenarios that require mobile phone screens such as game LVB and mobile APP demo.

![](//mc.qcloudimg.com/static/img/bf82394c56c13298f322df25c5de4e16/image.png)

Implementation solutions to screencap are distinctly different on iOS and Android:
- **Android Platform**
The feature is supported by Android 5.0 and later versions. The VJ only needs to install and start the LVB App before broadcasting, and then press the Home key to switch the App to the background. After that, all the contents on the VJ's screen can be used as LVB contents. This is how it works internally: The screencap API provided in the Android system is used to capture the screen, and the RTMP SDK underlying module performs encoding and RTMP push.

- **iOS platform**
The feature is supported by iOS 10.0 and later versions, and is implemented based on the extension mode of iOS, that is, when a game LVB starts, the iOS will evoke the system extension (installed by the LVB App) which supports Screencap LVB, and transmit the screen images to this system extension which will in turn perform encoding and LVB push.

## Try out the Feature
In the Mini LVB Demo, we provide screencap on both mobile phone platforms based on Tencent Cloud RTMP SDK. You can scan the QR code below to install and try it out.
![](//mc.qcloudimg.com/static/img/3939152d7b9a6fd0812b886ea049dc83/image.png)

## Interfacing Guide

### Step 1:  Add Activity
Paste an activity as follows to the manifest file
```xml
<activity 
    android:name="com.tencent.rtmp.video.TXScreenCapture$TXScreenCaptureAssistantActivity" 
    android:theme="@android:style/Theme.Translucent"/>
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
mLivePusher.startScreenCapture();
```
- **startPusher** is used to tell the RTMP SDK that which push URL the audio/video streams are being pushed to.
- **startScreenCapture** is used to start screencap. Since screencap is implemented based on the native capabilities of the Android system, for security reasons, Android will warn the user before the screencap is initiated by displaying a prompt: "an App will capture all the contents on your screen".

### Step 4:  Privacy Mode
The privacy mode is a basic feature of screencap LVB: During the screencap LVB, if the VJ does not want certain operations (e.g., entering game account and password) to be seen by the audience, he/she can enable the **Privacy Mode**. While in privacy mode, the VJ's push stays available, and the screen keeps being visible to the audience, only showing a waiting screen with prompt indicating that "the VJ is busy".
![](//mc.qcloudimg.com/static/img/558efb32484da9813253620c0c4b1165/image.png)

To realize such a feature, you can complete the interfacing process as follows:
- **4.1) Set pauseImg**
Before the push, use the setPauseImg API of TXLivePushConfig to set a waiting image, e.g., "The VJ will switch back the screen soon...".

- **4.2) Privacy mode switch**
On the floating window serving as the toolbar, add a button to enable/disable the privacy mode. The response logic of enabling the privacy mode is calling the TXLivePusher##pausePush API function; and the response logic of disabling the privacy mode is calling the TXLivePusher##resumePush API function.
```java
public void triggerPrivateMode() {
        if (mInPrivacy) {
            Toast.makeText(getApplicationContext(), "Privacy mode enabled", Toast.LENGTH_SHORT).show();
            mTVPrivateMode.setText(getString(R.string.private_mode_off));
            mTVPrivateMode.setCompoundDrawables(mDrawableLockOn,null,null,null);
            mPrivateBtn.setImageResource(R.mipmap.lock_off);
            mTXLivePusher.resumePusher();
        } else {
            Toast.makeText(getApplicationContext(), "Privacy mode disabled", Toast.LENGTH_SHORT).show();
            mTXLivePusher.pausePusher();
            mPrivateBtn.setImageResource(R.mipmap.lock_on);
            mTVPrivateMode.setText(getString(R.string.private_mode_on));
            mTVPrivateMode.setCompoundDrawables(mDrawableLockOff,null,null,null);
        }
        mInPrivacy = !mInPrivacy;
    }
```
 
### Step 5:  Set Logo Watermark
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

### Step 6:  Recommended Definition
Three major factors affect video quality: **resolution**, **frame rate** and **bitrate**.
- **Resolution**
Screencap LVB on mobile phones provides resolutions at three levels: 360\*640, 540\*960, and 720\*1280. The API for relevant settings is setVideoResolution in TXLivePushConfig.
- **Frame Rate**
You will feel significant stutter if FPS <=10. It is recommended to set the frame rate to 20 - 25 FPS for screencap LVB on mobile phones. API for this configuration is setVideoFPS in TXLivePushConfig.
- **BitRate**
It refers to the size of data encoded by the encoder in each second (in kbps). For example, 800 kbps indicates that the encoder produces 800 KB (or 100 KB) of data per second. The API for this configuration is setVideoBitrate in TXLivePushConfig.

Compared to camera LVB, screencap LVB has many more uncertainties, the most significant one of which is the screencap scenario.
(1) At one extreme, the mobile phone screen remains unchanged, e.g., the desktop. In this case, the encoder can complete the task with very low bitrate output.

(2) At the other extreme, the mobile phone screen changes dramatically at all times, e.g., when the VJ is playing Temple Run. In this case, the bitrate must be at least 2 Mbps to ensure that there is no mosaic even for a resolution as ordinary as 540 * 960.

| Level   | Resolution | FPS |  Bitrate-Game Screencap (Fishing Joy) | Bitrate-Game Screencap (Temple Run) |
|---------|---------|---------|---------|
| SD | VIDEO_RESOLUTION_TYPE_360_640 | 20   | 800kbps |  1200kbps|
| HD | VIDEO_RESOLUTION_TYPE_540_960 | 20   | 1200kbps | 2000kbps|
| UHD | VIDEO_RESOLUTION_TYPE_720_1280 | 20 | 1600kbps | 3000kbps|

### Step 7:  Remind the VJ "network is poor"
Step 9 will discuss how to handle RTMP SDK push events. **PUSH_WARNING_NET_BUSY** is very useful, it means: <font color='blue'>** the uplink network of the VJ is poor, and stutters have occurred in the viewer end.**</font>

When you receive this WARNING, you can use the UI to remind VJ to change network egress, or get closer to the WiFi. Or tell him to say something like this: "Hello dear, I'm streaming! Stop reading eBay! What? Not eBay? Then stop downloading movies!"

### Step 8:  Landscape/portrait screen adaption
Dynamic video switching logic between landscape/portrait screen has been realized in Tencent Cloud RTMP SDK, so there is no need to worry about this issue when using screencap LVB. When the VJ's mobile phone switches between landscape mode and portrait mode, the images seen at the viewer end stay consistent with the VJ end.

### Step 9:  Add Custom Audio Data to SDK
If you wish to replace audio capture with your own logic, you need to add CUSTOM_MODE_AUDIO_CAPTURE to the CustomMode settings. Meanwhile, you also need to specify key information such as audio sampling rate and number of channels.
```java
// (1) Set CustomMode as follows: Capture audio data by yourself; the SDK is responsible for encoding and sending data only
_config.customModeType |= CUSTOM_MODE_AUDIO_CAPTURE;
//
// (2) Set audio encoding parameters: Audio sampling rate and number of channels
_config.audioSampleRate = 44100;
_config.audioChannels   = 1;
```
Next, call **sendCustomPCMData** to insert your own PCM data to the SDK.

### Step 10:  Event Handling
#### Event Listening
RTMP SDK listens to push related events using the TXLivePushListener proxy. Note that the TXLivePushListener only listens to push events with prefix **PUSH_**.

#### Normal Events 
Events that are always prompted during a successful push. For example, receiving 1003 means that the system will start rendering the camera pictures

| Event ID                 |    Value  |  Description                    |   
| :-------------------  |:-------- |  :------------------------ | 
| PUSH_EVT_CONNECT_SUCC            |  1001 | Successfully connected to Tencent Cloud push server |
| PUSH_EVT_PUSH_BEGIN              |  1002 | Handshake with the server completed, everything is OK, ready to start push |
| PUSH_EVT_OPEN_CAMERA_SUCC  | 1003 | The pusher has successfully started the camera (this will take 1-2 seconds on some Android phones) | 

####  Error Notification 
The push cannot continue as the SDK detected critical problems. For example, the user disabled camera permission for the APP so the camera cannot be started.

| Event ID                 |    Value  |  Description                    |   
| :-------------------  |:-------- |  :------------------------ | 
| PUSH_ERR_OPEN_CAMERA_FAIL        | -1301 | Failed to start the camera |
| PUSH_ERR_OPEN_MIC_FAIL           | -1302 | Failed to start the microphone |
| PUSH_ERR_VIDEO_ENCODE_FAIL       | -1303 | Video encoding failed |
| PUSH_ERR_AUDIO_ENCODE_FAIL        -1304 | Audio encoding failed |
| PUSH_ERR_UNSUPPORTED_RESOLUTION  | -1305 | Unsupported video resolution |
| PUSH_ERR_UNSUPPORTED_SAMPLERATE  | -1306 | Unsupported audio sampling rate|
| PUSH_ERR_NET_DISCONNECT          | -1307 | Network disconnected. Reconnection attempts have failed for three times, thus no more retries will be performed. Please restart the push manually |

#### Warning Events 
SDK detected some reparable problems. Most warning events will trigger protection logics or recovery logics that involve retrying, and in most of the cases the problems can be recovered. Don't make a fuss.

- PUSH_WARNING_NET_BUSY
The VJ's network is busy. If you need UI prompts, this warning is relatively more useful (Step 10).

- PUSH_WARNING_SERVER_DISCONNECT
The push request is rejected by the backend. This will trigger retry logic for a limited number of times and the push may succeed in a certain attempt. But in most cases, it is because the txSecret in the push address is miscalculated, or because the test address is occupied by others. Therefore, this warning is more conducive to your debugging.

| Event ID                 |    Value  |  Description                    |   
| :-------------------  |:-------- |  :------------------------ | 
| PUSH_WARNING_NET_BUSY            | 1101 | Bad network condition: data upload is blocked because uplink bandwidth is too small |
| PUSH_WARNING_RECONNECT           | 1102 | Network disconnected, automatic reconnection has started (auto reconnection will be stopped if it fails for three times) |
| PUSH_WARNING_HW_ACCELERATION_FAIL |  1103 | Failed to start hardware encoding. Software encoding is used |
| PUSH_WARNING_DNS_FAIL			  |  3001 |  RTMP - DNS resolution failed (this will trigger retry process)        |
| PUSH_WARNING_SEVER_CONN_FAIL     |  3002 |  Failed to connect to the RTMP server (this will trigger retry process)  |
| PUSH_WARNING_SHAKE_FAIL          |  3003 |  RTMP server handshake failed (this will trigger retry process)  |
| PUSH_WARNING_SERVER_DISCONNECT      |  3004 |  The RTMP server actively disconnected (this will trigger retry process)  |

> For the definition of all events, please see the header file **"TXLiveConstants.java"**

### Step 11:  End Push
It is simple to end a push process, but proper cleaning work is required. Since only one TXLivePusher object can run at a time, improper cleaning work may adversely affect the next LVB.
```java
//End the screencap LVB and perform proper cleanup work
public void stopPublish() {
    mTXLivePusher.stopScreenCapture();
    mTXLivePusher.setPushListener(null);
    mTXLivePusher.stopPusher();
}
```

