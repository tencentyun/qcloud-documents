LVB Code Mode Only.

Multiple videos can be displayed in an ILVB room. However, for not-interactive broadcasting (automatic recording), videos are separated by default.


### Non-Interactive Broadcasting

When a non-interactive broadcasting is enabled automatically, all the videos in the room (VJs and viewers who join broadcasting) generate corresponding LVB video streams.

```
LVB Code=BIZID_MD5 (Room ID_User ID_Data Type)

Data type of camera is main
Data type of screen sharing is aux


Playback URL=Transmission protocol://BIZID.liveplay.myqcloud.com/live/LVB code[.format]
```
For more information, please see [Non-interactive Broadcasting under LVB Code Mode](https://cloud.tencent.com/document/product/268/8560).

### Stream Mixing API

Multiple video streams can be mixed into a new video stream (with which the original video stream can be replaced) using the API provided by Tencent Cloud Video backend according to a specified layout.

For more information, please see [Stream Mixing API](https://cloud.tencent.com/document/product/267/8832).

### Automatic Recording

When automatic recording is enabled, all video streams (including those after mixing) are automatically recorded as the video files for users to watch and download.

```
Recording File Name=LVB Code_Start Time_End Time
```

If the file is recorded successfully, this is notified to the callback URL using recording event (100). For more information, please see [Non-interactive Broadcasting under LVB Code Mode](https://cloud.tencent.com/document/product/268/8560).
