# Push and Playback

## Product Description

Tencent Video Cloud SDK is an audio/video SDK component that integrates **standard push and pull** and **real-time video call**. This document mainly introduces the integration solution of C# version.

Compared with Obs Studio (a commonly used push software) and Flash player (a common playback plug-in for PC browsers), the significant advantages of the Video Cloud SDK are:

- Low-delay optimization: Real-time audio/video calls.
- UDP protocol acceleration: Better push stability.

![img](https://mc.qcloudimg.com/static/img/82391e1dccd97d0496b2a357f9239044/image.png)



## Preparations

- **Acquiring SDK**
  [Download](https://cloud.tencent.com/document/product/454/7873#Windows) SDK and follow the instructions in [Project Configuration](https://cloud.tencent.com/document/product/454/13625) to add the SDK into your application development project.

- **Push URL for testing**
  The Demo supports getting the push URL for testing automatically from the backend. Click the **New** button in the above figure to get the push URL.

  You can also manually generate a push URL for testing. After [activating](https://console.cloud.tencent.com/live) the LVB service, use the [LVB Console -> LVB Code Access -> Push Generator](https://console.cloud.tencent.com/live/livecodemanage) to generate a push URL. For more information, please see [Acquiring Push/Playback URL](https://cloud.tencent.com/document/product/454/7915).

- **Playback URL for testing**
  Push URL `rtmp://8888.livepush.myqcloud.com/live/8888_teststream?bizid=8888&txSecret=6e18e8db0ff2070a339ab739ff46b957&txTime=5A3E7D7F`
  The playback URL is: `rtmp://8888.liveplay.myqcloud.com/live/8888_teststream`



## Push

### Code interfacing

#### Step 1: Create a Pusher object

Create a **ManageLiteAV.TXLivePusher** object, which will be used later for pushing.

After the creation, you can call the configuration API of ManageLiteAV.TXLivePusher to set the mirror effect, bitrate, resolution and fill mode before pushing.

```c#
pusher.setRenderYMirror(true);
pusher.setOutputYMirror(true);
pusher.setVideoBitRate(900);
pusher.setVideoBitRateMin(300);
pusher.setVideoBitRateMax(1200);
pusher.setVideoResolution(ManageLiteAV.TXEVideoResolution.TXE_VIDEO_RESOLUTION_640x480);
pusher.setRenderMode(ManageLiteAV.TXERenderMode.TXE_RENDER_MODE_FILLSCREEN);
...
```

#### Step 2: Set the preview area

We need a place to display the camera images. For Windows, HWND window handle is used as the basic rendering unit. In a C# form application, each control can call its Handle to get the HWND. Therefore, you simply need to prepare a **startPreview** API passed by HWND to the ManageLiteAV.TXLivePusher object.

```c#
// Set the callback for audio/video data and internal SDK events.
pusher.setCallback(this, (IntPtr)UserDataFlag.PusherFlag);
// Enable the camera, and the index value can be obtained via the enumCameras API of the ManageLiteAV.TXLivePusher object.
pusher.startPreview(pushRenderPanel.Handle, 0, 0, pushRenderPanel.Width, pushRenderPanel.Height, cameraIndex);

```

#### Step 3: Start push

After the preparations in Step 1 and Step 2, you can use the following codes to start the push:

```c#
string rtmpURL = "rtmp://2157.livepush.myqcloud.com/live/xxxxxx";
pusher.startPush(rtmpURL);

```

#### Step 4: Control the camera

If there are multiple cameras in a computer, you can switch between different cameras simply by calling the **switchCamera** API of ManageLiteAV.TXLivePusher object and passing the index value of the camera.

```c#
// Pass the index value of camera to be switched to
pusher.switchCamera(cameraComboBox.SelectedIndex);

```

- The enumCameras function of TXLivePusher can get the index value of the camera.
- Enabling a USB camera under Windows takes a long time for circuit and drive startup. You can set the last parameter of the startPreview of TXLivePusher the last parameter of the startPreview of TXLivePusher to -1, which means to enable all cameras. At this time, the response time for switching cameras will be much shorter.
- SDK supports virtual cameras, whose enabling method is the same as that of normal cameras. If your PC does not have a physical camera, you can install virtual camera software such as VCam to assist debugging.

#### Step 5: End push

Ending a push is simple, but proper cleanup work is required. Since only one ManageLiteAV.TXLivePusher object can run at a time, improper cleanup may adversely affect the next LVB.

```c#
// Set callback as null
pusher.setCallback(null, (IntPtr)null);
// Stop camera preview
pusher.stopPreview();
// Stop push
pusher.stopPush();

```

#### Step 6: More features

For more information on such features of the local camera as screen mirroring, mute and sharpness settings, please see [API List](https://cloud.tencent.com/document/product/454/13626).

### Event handling

The SDK listens for push-related events using the setListener API of the ManageLiteAV.TXLivePusher object.

#### 1. Normal events

A notification event is prompted after each successful push. For example, receiving 1003 means that the system will start rendering the camera pictures.

| Event ID | Value | Description |
| ------------------------------ | ---- | --------------- |
| PUSH_EVT_CONNECT_SUCC | 1001 | Successfully connected to push server |
| PUSH_EVT_PUSH_BEGIN | 1002 | Handshake with the server completed, and ready to start push |
| PUSH_EVT_OPEN_CAMERA_SUCC | 1003 | Camera is enabled |
| PUSH_EVT_CHANGE_RESOLUTION | 1005 | Dynamic push resolution adjustment |
| PUSH_EVT_CHANGE_BITRATE | 1006 | Dynamic push bitrate adjustment |
| PUSH_EVT_FIRST_FRAME_AVAILABLE | 1007 | The first frame is captured |
| PUSH_EVT_START_VIDEO_ENCODER | 1008 | Encoder is started |
| PUSH_EVT_CAMERA_REMOVED | 1009 | Camera device has been removed |
| PUSH_EVT_CAMERA_AVAILABLE | 1010 | Camera device is available again |
| PUSH_EVT_CAMERA_CLOSED | 1011 | Camera is disabled |

#### 2. Error notification

The push cannot continue as the SDK detected critical problems. For example, the camera has been occupied by other programs so the camera cannot be started.

| Event ID | Value | Description |
| ------------------------------- | ----- | ---------------------------------- |
| PUSH_ERR_OPEN_CAMERA_FAIL | -1301 | Failed to start the camera |
| PUSH_ERR_OPEN_MIC_FAIL | -1302 | Failed to start the microphone |
| PUSH_ERR_VIDEO_ENCODE_FAIL | -1303 | Video encoding failed |
| PUSH_ERR_AUDIO_ENCODE_FAIL | -1304 | Audio encoding failed |
| PUSH_ERR_UNSUPPORTED_RESOLUTION | -1305 | Unsupported video resolution |
| PUSH_ERR_UNSUPPORTED_SAMPLERATE | -1306 | Unsupported audio sampling rate |
| PUSH_ERR_NET_DISCONNECT | -1307 | Network disconnected. Reconnection attempts have failed for many times, thus no more retries will be performed. Please restart the push manually |
| PUSH_ERR_CAMERA_OCCUPY | -1308 | The camera is being occupied. Enable another camera. |

#### 3. Warning events

Compared with the error message, issues represented by WARNING events usually do not interrupt the push process, and SDK generally initiates automatic repair logic internally. You don't need to care about most WARNING events, but the following two events are important and meaningful:

**WARNING_NET_BUSY**
Poor upstream network speed. It represents that the user's current audio/video data cannot be pushed smoothly to the server. In this case, generally the user can be given some UI prompts, for example, "Your network speed is not good" so as to allow the user to prepare for the lag on the other end.

**WARNING_SERVER_DISCONNECT**
The push request is rejected by the backend. This is usually because that txSecret in the push address is calculated incorrectly, or the push address is occupied by others (push URL is exclusive and a push URL can only be used by one user at a time).

| Event ID | Value | Description |
| ---------------------------------------- | ---- | ------------------------------- |
| PUSH_WARNING_NET_BUSY | 1101 | Bad network connection: data upload is blocked because upstream bandwidth is too small |
| PUSH_WARNING_RECONNECT | 1102 | Network disconnected. Auto reconnection has been initiated (no more attempts will be made after three failed attempts) |
| PUSH_WARNING_HW_ACCELERATION_FAIL | 1103 | Failed to start hard-encoding. Soft-encoding is used. |
| PUSH_WARNING_VIDEO_ENCODE_FAIL | 1104 | Video encoding failed. Non-fatal error. Encoder will be restarted internally. |
| PUSH_WARNING_BEAUTYSURFACE_VIEW_INIT_FAIL | 1105 | Warning of video encoding bitrate error |
| PUSH_WARNING_VIDEO_ENCODE_BITRATE_OVERFLOW | 1106 | Warning of video encoding bitrate error |
| PUSH_WARNING_DNS_FAIL | 3001 | RTMP - DNS resolution failed (this will trigger retry process) |
| PUSH_WARNING_SEVER_CONN_FAIL | 3002 | Failed to connect to the RTMP server (this will trigger retry process) |
| PUSH_WARNING_SHAKE_FAIL | 3003 | Handshake with RTMP server failed (this triggers a retry) |
| PUSH_WARNING_SERVER_DISCONNECT | 3004 | RTMP server disconnected automatically. Check the validity of push URL or the validity period of hotlink protection |
| PUSH_WARNING_SERVER_NO_DATA | 3005 | Actively disconnected for no data is sent for more than 30s. |



## Playback Feature

### Code interfacing

#### Step 1: Create a Player object

Create a **ManageLiteAV.TXLivePlayer** object, which will be used later for pushing.

```c#
player = new ManageLiteAV.TXLivePlayer();

```

#### Step 2: Set the rendering area

We need a place to display the player's video image. For Windows, HWND window handle is used as the basic rendering unit. In a C# form application, each control can call its Handle to get the HWND.

```c#
//Set callback
player.setListener(this, (IntPtr)UserDataFlag.PlayerFlag);
// Pass HWND window handle, rendering position and size
player.setRenderFrame(pullRenderPanel.Handle, 0, 0, pullRenderPanel.Width, pullRenderPanel.Height);

```

#### Step 3: CDN playback

To start the playback feature, simply call the startPlay API of ManageLiteAV.TXLivePlayer, where PLAY_TYPE_LIVE_RTMP is the RTMP URL of the regular CDN. The advantage is that the bandwidth price is very low, but the delay is usually high.

```c#
string rtmpURL = "rtmp://2157.liveplay.myqcloud.com/live/xxxxxx";
player.startPlay(rtmpURL,ManageLiteAV.TXEPlayType.PLAY_TYPE_LIVE_RTMP);

```

#### Step 3': Ultra-low delay playback

Ultra-low delay playback can pull the end-to-end delay down to about 400ms. In this mode, the internal mechanism of SDK is completely different from that in the normal mode. Meanwhile, the audio/video lines used by SDK are not regular CDN lines. Compared with CDN, the unit price is higher. It is generally applicable to audio/video calls and scenarios that highly requiring low delay.

```c#
string rtmpURL = "rtmp://2157.liveplay.myqcloud.com/live/xxxxxxbizid=2157&
                  txSecret=6e18e8db0ff2070a339ab739ff46b957&txTime=5A3E7D7F";
player.startPlay(rtmpURL,ManageLiteAV.TXEPlayType.PLAY_TYPE_LIVE_RTMP_ACC);

```

- This feature does not need to be enabled in advance, but it requires that LVB stream be located in Tencent Cloud. Implementing low-latency linkage across cloud providers is not just a technical difficulty.
- The playback URL cannot be a normal CDN URL. It must have a hotlink protection signature. For more information about the computing method of hotlink protection signature, please see [**txTime&txSecret**](https://cloud.tencent.com/document/product/454/9875).
- When calling the startPlay API, specify type as **PLAY_TYPE_LIVE_RTMP_ACC** for SDK to pull an ultra-low delay LVB stream.
- It supports concurrence playback of 10 channels simultaneously at most. So you can only use it in interactive scenarios (such as the channel of joint broadcasting VJ or the operator in Prize Claw LVB).
- The RTMP stream launched by Obs Studio introduces a delay of more than 1s on the client. Therefore, use the video cloud SDK for pushing.

#### Step 4: Adjust the image

- **updateRenderFrame**
  When the window size specified by the HWND changes, the video rendering area can be rescaled via the **updateRenderFrame** function.
- **setRenderMode**

| Option | Description |
| -------------------------- | ---------------------------------------- |
| TXE_RENDER_MODE_ADAPT | Adaption. The video image is displayed in full on the screen, possibly with black edges around it. |
| TXE_RENDER_MODE_FILLSCREEN | Filling. No black edge exists, but the parts beyond the rendering area are trimmed off, so that the image is centered on the screen. |

#### Step 5: End playback

To exit the current UI at the end of playback, call the stopPlay API of ManageLiteAV.TXLivePlayer.

```c#
// Set callback as null
player.setCallback(null, (IntPtr)null);
// Stop pull playback
player.stopPlay();

```

#### Step 6: More features

For more information, please see [API List](https://cloud.tencent.com/document/product/454/13626).



### Event handling

Listen on push-related events using the setListener API of the ManageLiteAV.TXLivePlayer object.

#### 1. Normal events

| Event ID | Value | Description |
| ---------------------------- | ---- | -------------- |
| PLAY_EVT_CONNECT_SUCC | 2001 | Connected to the server |
| PLAY_EVT_RTMP_STREAM_BEGIN | 2002 | Connected to the server and started to pull stream |
| PLAY_EVT_RCV_FIRST_I_FRAME | 2003 | Render the first video packet (IDR) |
| PLAY_EVT_PLAY_BEGIN | 2004 | Video playback starts |
| PLAY_EVT_PLAY_PROGRESS | 2005 | Video playback progress |
| PLAY_EVT_PLAY_END | 2006 | Video playback ends |
| PLAY_EVT_PLAY_LOADING | 2007 | Video playback loading |
| PLAY_EVT_START_VIDEO_DECODER | 2008 | Decoder starts |
| PLAY_EVT_CHANGE_RESOLUTION | 2009 | Video resolution changes |

#### 2. Error notification

Some fatal errors occurred with SDK, such as network disconnection, can cause the failure to continue playback. In this case, you need to deal with these errors accordingly.

| Event ID | Value | Description |
| ------------------------------ | ----- | --------------------- |
| PLAY_ERR_NET_DISCONNECT | -2301 | The network is disconnected and reconnection attempts failed, which will result in playback failure. |
| PLAY_ERR_GET_RTMP_ACC_URL_FAIL | -2302 | Failed to acquire pull accelerating address, which will result in playback failure |

#### 3. Warning events

Non-fatal errors with SDK generally do not cause the stop of playback, so you can ignore the following events.

**PLAY_WARNING_VIDEO_PLAY_LAG** is an event that SDK throws to indicate the playback stutter. It means the lag between video images (the refresh time between two frames) exceeds 500 ms.

| Event ID | Value | Description |
| ------------------------------------- | ---- | ------------------------------- |
| PLAY_WARNING_VIDEO_DECODE_FAIL | 2101 | Failed to decode the current video frame |
| PLAY_WARNING_AUDIO_DECODE_FAIL | 2102 | Failed to decode the current audio frame |
| PLAY_WARNING_RECONNECT | 2103 | Network disconnected. Auto reconnection has been initiated (no more attempts will be made after three failed attempts) |
| PLAY_WARNING_RECV_DATA_LAG | 2104 | Unstable incoming packet from network: This may be caused by insufficient downstream bandwidth, or unstable outgoing stream at the VJ end |
| PLAY_WARNING_VIDEO_PLAY_LAG | 2105 | Stutter occurred during the current video playback (intuitive user experience) |
| PLAY_WARNING_HW_ACCELERATION_FAIL | 2106 | Failed to start hard-decoding; Soft-decoding is used (not supported for now) |
| PLAY_WARNING_VIDEO_DISCONTINUITY | 2107 | Current video frames are discontinuous and frame loss may occur |
| PLAY_WARNING_FIRST_IDR_HW_DECODE_FAIL | 2108 | Hard decoding of Frame I for the current stream fails, and SDK automatically switches to soft decoding |
| PLAY_WARNING_DNS_FAIL | 3001 | RTMP - DNS resolution failed |
| PLAY_WARNING_SEVER_CONN_FAIL | 3002 | Failed to connect to the RTMP server |
| PLAY_WARNING_SHAKE_FAIL | 3003 | Handshake with RTMP server failed |
| PLAY_WARNING_SERVER_DISCONNECT | 3004 | The RTMP server is actively disconnected |

