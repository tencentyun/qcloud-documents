## PushEvent

### Normal events 

A notification event is prompted after each successful push. For example, receiving 1003 means that the system will start rendering the camera pictures.

| code | Event | Description |
| -------------------  | -------- |  ------------------------ |
| 1001 | PUSH_EVT_CONNECT_SUCC | Connected to the CVM |
| 1002 | PUSH_EVT_PUSH_BEGIN | Handshake with the server completed; everything is OK; ready to start upstream push |
| 1003 | PUSH_EVT_OPEN_CAMERA_SUCC | Camera enabled. Cannot enable the camera if the camera has been occupied or you have limited permission to the camera. |
| 1004 | PUSH_EVT_SCREEN_CAPTURE_SUCC | Screencap started successfully (for Android SDK) |
| 1005 | PUSH_EVT_CHANGE_RESOLUTION | Dynamic push resolution change |
| 1006 | PUSH_EVT_CHANGE_BITRATE | Dynamic push bitrate change |
| 1007 | PUSH_EVT_FIRST_FRAME_AVAILABLE | The first frame is captured |
| 1008 | PUSH_EVT_START_VIDEO_ENCODER | Encoder is started |
| 1009 | PUSH_EVT_CAMERA_REMOVED | Camera has been removed (for Windows SDK) |
| 1010 | PUSH_EVT_CAMERA_AVAILABLE | Camera is available again (for Windows SDK) |
| 1011 | PUSH_EVT_CAMERA_CLOSED | Camera is disabled (for Windows SDK) |
| 1012 | PUSH_EVT_SNAPSHOT_RESULT | Error code of screencap snapshot (for Windows SDK) |
| 1018 | PUSH_EVT_ROOM_IN | Already in the webrtc room and will be notified after successful entry into the room |
| 1019 | PUSH_EVT_ROOM_OUT | Not in the webrtc room and will be notified after failure to enter the room or in the process of exiting the room |
| 1020 | PUSH_EVT_ROOM_USERLIST | Issue the webrtc room member list (excluding the user him/herself) |
| 1021 | PUSH_EVT_ROOM_NEED_REENTER | Switching Wi-Fi to 4G will trigger disconnection and reconnection, which requires you to re-enter the webrtc room (pull the optimal server address) |

### Critical errors

The push cannot continue as the SDK detected critical problems. For example, the user disabled camera permission for the App so the camera cannot be started.

> Note: A video encoding failure does not affect push process directly. The SDK will handle it automatically to ensure success of the subsequent video encoding.


| code | Event | Description |
| --- | --- | --- |
| -1301 | PUSH_ERR_OPEN_CAMERA_FAIL | Failed to enable the camera |
| -1302 | PUSH_ERR_OPEN_MIC_FAIL | Failed to enable the microphone |
| -1303 | PUSH_ERR_VIDEO_ENCODE_FAIL | Video encoding failed |
| -1304 | PUSH_ERR_AUDIO_ENCODE_FAIL | Audio encoding failed |
| -1305 | PUSH_ERR_UNSUPPORTED_RESOLUTION | Unsupported video resolution |
| -1306 | PUSH_ERR_UNSUPPORTED_SAMPLERATE | Unsupported audio sampling rate |
| -1307 | PUSH_ERR_NET_DISCONNECT | The network is disconnected and fails to be reconnected after three attempts, so the push needs to be restarted |
| -1308 | PUSH_ERR_CAMERA_OCCUPY<br><br>PUSH_ERR_AUDIO_SYSTEM_NOT_WORK<br><br>PUSH_ERR_SCREEN_CAPTURE_START_FAILED | Camera is in use and you may try enabling a different camera (Windows)<br><br>System exception and recording failed (iOS)<br><br>Failed to start screencap, which is possibly rejected by the user (Android) |
| -1309 | PUSH_ERR_SCREEN_CAPTURE_UNSURPORT | Screencap failed due to unsupported Android OS version; 5.0 or above is required (for Android SDK) |

### Warning events 

Most warning events will trigger protection logics or recovery logics that involve retrying, and in most cases the problems can be recovered by the SDK itself. Some warning events need to be handled by developer.

- **WARNING_NET_BUSY:**If the VJ has poor network connections, the user can be notified through UI.

- **WARNING_SERVER_DISCONNECT:** The push request is rejected by the backend. This is usually caused by miscalculated txSecret in the push address, or because the push address is occupied by others (a push URL can only have one pushing end at a time).

| code | Event | Description |
| -------------------  | -------- |  -----------------------|
| 1101 | PUSH_WARNING_NET_BUSY | The upstream network is poor. It is recommended to remind users of improving the current network environment. |
| 1102 | PUSH_WARNING_RECONNECT | Network disconnected and auto reconnection has started (auto reconnection will be stopped after three failed attempts) |
| 1103 | PUSH_WARNING_HW_ACCELERATION_FAIL | Failed to start hardware encoding. Use software encoding instead. |
| 1104 | PUSH_WARNING_VIDEO_ENCODE_FAIL | Video encoding failed. Non-fatal error. Encoder will be restarted internally. |
| 1107 | PUSH_WARNING_VIDEO_ENCODE_SW_SWITCH_HW | Automatically switch to hardware encoding due to machine performance issues (for Android SDK) |
| 3001 | PUSH_WARNING_DNS_FAIL | DNS resolution failed and trigger retry process. |
| 3002 | PUSH_WARNING_SEVER_CONN_FAIL | Failed to connect to the server and trigger retry process. |
| 3003 | PUSH_WARNING_SHAKE_FAIL | Server handshake failed and trigger retry process. |
| 3004 | PUSH_WARNING_SERVER_DISCONNECT | The RTMP server is actively disconnected. Check the validity of the push address or the validity period of hotlink protection |
| 3005 | PUSH_WARNING_READ_WRITE_FAIL | RTMP failed to read/write and will be disconnected |


## PlayEvent

### Key events

| code | Event | Description |
| --- | --- | --- |
| 2001 | PLAY_EVT_CONNECT_SUCC | Connected to the server |
| 2002 | PLAY_EVT_RTMP_STREAM_BEGIN | Connected to the server and started to pull streams |
| 2003 | PLAY_EVT_RCV_FIRST_I_FRAME | Render the first video packet (IDR) |
| 2004 | PLAY_EVT_PLAY_BEGIN | Video playback starts |
| 2005 | PLAY_EVT_PLAY_PROGRESS | Video playback progress (for VOD) |
| 2006 | PLAY_EVT_PLAY_END | Video playback ends |
| 2007 | PLAY_EVT_PLAY_LOADING | Video playback loading |
| 2008 | PLAY_EVT_START_VIDEO_DECODER | Decoder starts |
| 2009 | PLAY_EVT_CHANGE_RESOLUTION | Video resolution changes |
| 2010 | PLAY_EVT_GET_PLAYINFO_SUCC<br><br>PLAY_EVT_SNAPSHOT_RESULT | VOD file information obtained successfully (Android iOS) <br><br> The error code of screencap snapshot (Windows) |
| 2011 | PLAY_EVT_CHANGE_ROATION | MP4 video rotation angle (Android, iOS) |
| 2012 | PLAY_EVT_GET_MESSAGE | Used to receive messages inserted into the audio/video stream. For details, please see [iOS Message Reception](https://cloud.tencent.com/document/product/454/7880#Message) and [Android Message Reception](https://cloud.tencent.com/document/product/454/7886#Message) |
| 2013 | PLAY_EVT_PREPARED | Video loaded (Android, iOS) |
| 2014 | PLAY_EVT_VOD_LOADING_END | Loading ends (Android, iOS) |
| -2301 | PLAY_ERR_NET_DISCONNECT | The network is disconnected and fails to be reconnected after three attempts, so the push needs to be restarted. |
| -2302 | PLAY_ERR_GET_RTMP_ACC_URL_FAIL | Failed to get the accelerated pull address |
| -2303 | PLAY_ERR_FILE_NOT_FOUND | No playback file exists (Android, iOS) |
| -2304 | PLAY_ERR_HEVC_DECODE_FAIL | H265 decoding failed (Android, iOS) |
| -2305 | PLAY_ERR_HLS_KEY | Failed to get the HLS decoding key (Android, iOS) |
| -2306 | PLAY_ERR_GET_PLAYINFO_FAIL | Failed to get VOD file information (Android, iOS) |

> **Note:**
>- **Determine whether the LVB is over:** Because of the varying implementation principles of different standards, many LVB streams usually don't throw end events (2006) and it is expected that when the VJ stops pushing stream, the SDK will soon find that data stream pull fails (WARNING_RECONNECT) and attempt to retry until the PLAY_ERR_NET_DISCONNECT event is thrown after three failed attempts. Therefore, judgment needs to be made for both 2006 and -2301, which are used as the events to determine the end of LVB.
>
>- **Do not hide the playback view after receiving PLAY_LOADING**, because the time length between PLAY_LOADING and PLAY_BEGIN can be different (sometimes 5 seconds, sometimes 5 milliseconds). Some customers consider hiding the view upon LOADING and displaying the view upon BEGIN, which will cause serious flickering (especially in LVB scenarios). It is recommended to place a translucent loading animation on top of the video view.

### Warning events

Errors in internal warnings are recoverable. The SDKs initiate appropriate recovery measures. The purpose of the warning is mainly to prompt developers or end users of the error.

| code | Event | Description |
| -------------------  | -------- |  ------------------------ |
| 2101 | PLAY_WARNING_VIDEO_DECODE_FAIL | Failed to decode the current video frame |
| 2102 | PLAY_WARNING_AUDIO_DECODE_FAIL | Failed to decode the current audio frame |
| 2103 | PLAY_WARNING_RECONNECT | Network disconnected and auto reconnection has started (the PLAY_ERR_NET_DISCONNECT event will be thrown after three failed attempts) |
| 2104 | PLAY_WARNING_RECV_DATA_LAG | Video stream is not stable. This may be caused by bad network connection. |
| 2105 | PLAY_WARNING_VIDEO_PLAY_LAG | Stutter occurred during the current video playback |
| 2106 | PLAY_WARNING_HW_ACCELERATION_FAIL | Failed to start hardware decoding. Use software decoding instead. |
| 2107 | PLAY_WARNING_VIDEO_DISCONTINUITY | Current video frames are discontinuous. This may be caused by frame loss. Blurred screen may occur. |
| 2108 | PLAY_WARNING_FIRST_IDR_HW_DECODE_FAIL | Hard decoding of the first I-frame of current stream failed. Switched to soft decoding automatically |
| 3001 | PLAY_WARNING_DNS_FAIL | DNS resolution failed (thrown only if the playback URL starts with "RTMP://") |
| 3002 | PLAY_WARNING_SEVER_CONN_FAIL | Server connection failed (thrown only if the playback URL starts with "RTMP://") |
| 3003 | PLAY_WARNING_SHAKE_FAIL | Server handshake failed (thrown only if the playback URL starts with "RTMP://") |
| 3004 | PLAY_WARNING_SERVER_DISCONNECT | The RTMP server is actively disconnected |

