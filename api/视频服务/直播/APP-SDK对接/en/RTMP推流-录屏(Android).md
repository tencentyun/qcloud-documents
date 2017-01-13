
## Mobile screencap
RTMP SDK 1.6.1 supports LVB of mobile screencap, that is, the VJ's mobile phone screen can be used as the live source. Meanwhile, the camera preview can be overlaid and used for scenarios that require mobile phone screens such as game LVB and mobile APP demo.

![](//mc.qcloudimg.com/static/img/bf82394c56c13298f322df25c5de4e16/image.png)

Implementation solutions to the screencap function are distinctly different on iOS and Android:
-**Android platform**
The function is supported by Android 5.0 and later versions. The VJ only needs to install and start the LVB App before LVB, and then press the Home key to switch the App to the background. After that, all the contents on the VJ's screen can be used as LVB contents. The internal principle is as follows: The screencap API provided by the Android system is used for screen collection, and the RTMP SDK bottom module is responsible for encoding and RTMP push.

-**iOS platform**
The function is supported by iOS 10.0 and later versions, and is implemented based on the extension mode of iOS, that is, when a game LVB starts, the iOS will evoke the system extension (installed by the LVB App) supporting LVB of screencap, and transmit the screen images to this system extension so it can complete encoding and LVB push.

## Experiencing Functions
In the Little Live Demo, we implemented the mobile phone screencap function on two platforms based on the RTMP SDK of Tencent Cloud. You can scan the QR code below to install and experience it.
![](//mc.qcloudimg.com/static/img/3939152d7b9a6fd0812b886ea049dc83/image.png)

## Interworking Guide

### Step 1:  Adding an activity
Paste an activity as follows in the manifest file
```xml
<activity 
    android:name="com.tencent.rtmp.video.TXScreenCapture$TXScreenCaptureAssistantActivity" 
    android:theme="@android:style/Theme.Translucent"/>
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
mLivePusher.startScreenCapture();
```
-**startPusher** is to tell which URL RTMP SDK audio/video streams are pushed to.
- **startScreenCapture** is used to start screen recording. Since screencap is implemented based on the native capabilities of the Android system, for security, Android will display a prompt before screencap to warn the user: "an App will capture all the contents on your screen".

### Step 4:  Privacy mode
The privacy mode is a basic function of LVB of screencap: During the LVB screencap, if the VJ does not want certain operations (e.g., entering the game account and password) to be seen by the audience, he/she can enable **Privacy Mode**. In privacy mode, the VJ's push will be ongoing, but the screen always visible to the audience will be a prompt indicating that "the VJ is busy".
![](//mc.qcloudimg.com/static/img/558efb32484da9813253620c0c4b1165/image.png)

To implement such a function, you can complete interconnection as follows:
-**4.1) Set pauseImg**
Before push, use the setPauseImg API of TXLivePushConfig to set a waiting image, e.g., "The VJ will switch back the screen soon...".

- **4.2) Privacy mode switch**
On the floating window serving as the toolbar, add a button to enable/disable privacy mode. The response logic of enabling the privacy mode is invoking of the TXLivePusher##pausePush API function; and the response logic of disabling the privacy mode is invoking of the TXLivePusher##resumePush API function.
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
 
### Step 5: Set logo watermarks
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

### Step 6:  Recommended definition
The video quality is affected by **resolution**, **frame rate** and **bit rate**.
- **Resolution**
LVB of mobile phone screencap provides resolutions at three levels for selection: 360\*640, 540\*960, and 720\*1280. The API for relevant settings is setVideoResolution in TXLivePushConfig.
- **Frame Rate**
Significant frame freezing will be felt if FPS <= 10. It is recommended to set the frame rate of 20 - 25 FPS for LVB of mobile phone screencap, and set the API to setVideoFPS in TXLivePushConfig.
- **Bit Rate**
It refers to the size of data encoded by the encoder each second, in the unit of kbps, e.g., 800 kbps indicates that the encoder produces 800 kb (or 100 KB) data per second. Set the API to setVideoBitrate in TXLivePushConfig.

In comparison with LVB of camera, LVB of screencap has much more uncertainties, among which the primary uncertainty is the screencap scenario.
(1) At one extreme, the mobile phone screen is unchanged, e.g., always on the home screen. In this case, the encoder can use very little bit rate output to complete the task.

(2) At the other extreme, the mobile phone screen changes dramatically at all times, e.g., when the VJ is playing Temple Run. In this case, the bit rate must be 2 Mbps at least to ensure that there is no mosaic even for the ordinary resolution 540 * 960.

| Step   | Resolution | FPS |  Bit Rate-Game Screencap (Fishing Joy) | Bit Rate-Game Screencap (Temple Run) |
|---------|---------|---------|---------|
| Standard Definition | VIDEO_RESOLUTION_TYPE_360_640 | 20   | 800kbps |  1200kbps|
| High Definition | VIDEO_RESOLUTION_TYPE_540_960 | 20   | 1200kbps | 2000kbps|
| Super Definition | VIDEO_RESOLUTION_TYPE_720_1280 | 20 | 1600kbps | 3000kbps|

### Step 7:  Remind the VJ of "Busy network"
Step 9 will introduce solving RTMP SDK push events. **PUSH_WARNING_NET_BUSY** is very useful, which means: <font color = 'blue'>** the uplink network of the VJ is busy, and lagging occurs in the viewer end.** </font>

When you receive this WARNING, you can remind through the UI the VJ of changing the network egress, or moving closer to the WiFi. Or you say to him: "Dear, I am using LVB. Do not visit the Taobao website!" What? Not visit Taobao? Then you must be watching Korean TV dramas. "

### Step 8:  Horizontal and vertical screen adaptation
The video logic of dynamic horizontal and vertical screen switching has been realized in the RTMP SDK of Tencent Cloud, so this issue does not need to be noted when LVB of screencap is used. When the VJ's mobile phone switches between the horizontal and vertical screens, the images seen by the audience are consistent with the visual angle of the VJ.

### Step 9:  Event processing
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

### Step 10:  Push ends
It is very simple to end push, but proper cleaning work is needed. Since only one TXLivePusher object used for push can run at a time, improper cleaning work will lead to adverse effect on the next LVB.
```java
//End LVB of screencap and complete the cleaning work properly
public void stopPublish() {
    mTXLivePusher.stopScreenCapture();
    mTXLivePusher.setPushListener(null);
    mTXLivePusher.stopPusher();
}
```