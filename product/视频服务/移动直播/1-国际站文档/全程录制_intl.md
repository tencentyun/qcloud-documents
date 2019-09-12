

<h2>Feature Description</h2>

You can record a user's entire LVB process as a video file for replay. It is applicable to online loss assessment, interactive classroom, remote court hearing, and other scenarios.

<video src="
http://1252463788.vod2.myqcloud.com/e12fcc4dvodgzp1252463788/c490bab57447398155981625642/TwA4JteAe40A.mp4" controls="controls">
Your browser does not support video tags.
</video>

## Enabling Recording

Recording & Replay is built on Tencent Cloud's **VOD service**. To use this feature, you need to [Activate VOD Service](http://console.cloud.tencent.com/video) on Tencent Cloud console. After the service is enabled, you can find the new recorded files in [Video Management](http://console.cloud.tencent.com/video/videolist) on VOD console.

How to enable recording? Two methods are available:

### 1. Enable recording globally
You can enable or disable recording for all LVB streams in [**LVB Console** -> **Access Management** -> **LVB Code Access** -> **Access Configuration**](https://console.cloud.tencent.com/live/livecodemanage), as shown below:

![](https://main.qcloudimg.com/raw/85760a7589c6bff42a061f138f1bd438.png)

Notes:

- The video wrapper formats supported by the global recording feature are MP4, HLS and FLV.
- You can specify multiple formats in which the video is recorded at a time (mobile browsers only support playback of MP4 and HLS videos).
- Changing resolution or switching between landscape/portrait modes during LVB is not supported for MP4 videos. If you need the screen sharing feature (screen resolution may change during push) without stream mixing enabled, HLS format is recommended.
- If the specified recording format is FLV or MP4, the length of a video fragment for global recording defaults to 30 minutes. Submit a ticket if you need to configure the length of a video fragment for global recording.
- HLS (m3u8) file is on a fragmentation basis in essence, so you can always get a single m3u8 file as long as no push interruption occurs during LVB. But in case of a push interruption during LVB, fragmentation will occur in the process of recording, which means you will get multiple m3u8 files. One of the common problems is switching of App to background. To solve this problem, you're recommended to allow push at the background.

### 2. Specify a room for recording

If global recording is not enabled, you can still enable recording for some important video streams by setting the record parameter in custom to true when calling the API createExeAsRoom in the EXEStarter.js of Web end.

Sample code:

```
EXEStarter.createExeAsRoom({
            userdata: {
                userID: accountInfo.userID,
                userName: accountInfo.userName,
                sdkAppID: accountInfo.sdkAppID,
                accType: accountInfo.accountType,
                userSig: accountInfo.userSig,
            },
            roomdata: {
                serverDomain: "https://room.qcloud.com/",
                roomAction: object.data.roomAction,
                roomID: object.data.roomID,
                roomName: object.data.roomName,
                roomTitle: object.data.roomTitle,
                roomLogo: "http://liteav.myqcloud.com/windows/logo/liveroom_logo.png",
                type: EXEStarter.StyleType.LiveRoom,
                template: EXEStarter.Template.Template1V3,
            },
            custom: {   //Optional
     			record:  true,  //Record the current video stream at the background
  			},
            success: function (ret) {
               console.log('EXEStarter.openExeRoomLocal application launched successfully');
            },
            fail: function (ret) {
               console.log('EXEStarter.openExeRoom Failed to launch local application');
               if (ret.errCode == -1) {
                  //Local application is not installed
               }
            },
        })
```

Notes:
- The video wrapper format used by the recording feature is MP4 by default (convenient for playback, download and transmission).
- The length of a video fragment of an MP4 file is 2 hours by default. The LVB content within 2 hours will be recorded into an MP4 file as long as no push interruption occurs.


You can choose either one of these two methods based on your business needs. If you need to record every video stream, global recording is recommended. If you want to record mixing images into a file, you are recommended to specify a room for recording.


## Getting Files
When a new recorded video file is generated, a playback URL will be generated. You can implement many extensions based on your business scenarios. For example, you can add the URL to historical information for archiving, or put it in the replay list to recommend a high-quality video to your App users after manual filtering.

You can get the URL of the recorded file by the following three ways:

### 1. Listen to notification passively
You can use Tencent Cloud **[Event Notification Service](https://cloud.tencent.com/document/product/267/5957)**: Register a **callback URL** for your server on Tencent Cloud which will notify you of the generation of a new recorded file using this URL.

![](https://main.qcloudimg.com/raw/b50c901fb4d529daf3405e78bc69908d.png)

The following is a typical notification message, which indicates: a new FLV recorded file with ID 9192487266581821586 has been generated, and the playback URL is: `http://200025724.vod.myqcloud.com/200025724_ac92b781a22c4a3e937c9e61c2624af7.f0.flv`.
```json
{
    "channel_id": "2121_15919131751",
    "end_time": 1473125627,
    "event_type": 100,
    "file_format": "flv",
    "file_id": "9192487266581821586",
    "file_size": 9749353,
    "sign": "fef79a097458ed80b5f5574cbc13e1fd",
    "start_time": 1473135647,
    "stream_id": "2121_15919131751",
    "t": 1473126233,
    "video_id": "200025724_ac92b781a22c4a3e937c9e61c2624af7",
    "video_url":        "http://200025724.vod.myqcloud.com/200025724_ac92b781a22c4a3e937c9e61c2624af7.f0.flv"
}
```

> Note: The time information sent from the App client is important. If you want to define that all the files recorded during this time period belong to an LVB, you just need to retrieve the recording notifications you received using LVB code and time information (each recording notification event comes with stream_id, start_time and end_time).

### 2. Query files actively

You can check if any new recorded file is generated on a regular basis using Tencent Cloud's query API (**[Live_Tape_GetFilelist](https://cloud.tencent.com/document/product/267/5960)**). However, this method is not recommended for frequent use due to its unsatisfactory real-timeness and reliability since it has a slow response in case of a query for a large number of channels and cannot be called at a high frequency (only suitable for the channels that have just finished).

### 3. View files in video management

All recorded videos can be queried in [Video Management](http://console.cloud.tencent.com/video/videolist) on VOD console, where you can retrieve the content of video files. You can also search for specified videos by prefix, as shown below:

![](https://main.qcloudimg.com/raw/d1fe5bf5aecf7e3ee32fb2516e1029b6.png)

Select a video file in the video list, and you can find its details at the right side. Switch to the **Video Publishing** tab, and click **Display source address** to get the file URL. See the figure below:

![](https://main.qcloudimg.com/raw/a7b1e0543b222b8eaa028433a2527a33.png)



## FAQ

### 1. How does LVB recording work?

![](https://main.qcloudimg.com/raw/cbb2aae6b5e767db1d30cb51d147948d.png)

When you enable the recording for an LVB stream, the audio/video data is bypassed to the recording system. Every frame pushed from VJ's mobile phone is written into the recorded file by the recording system.

If an LVB push is interrupted, the access layer will immediately notify the recording server to record the file being written, store it into the VOD system and generate an index. Then you can find the new recorded file in the VOD system. If you have configured recording event notification on a server, the recording system will send the **index ID** and **online playback URL** to the server.


### 2. How many recorded files are generated in an LVB process?
- If the duration of an LVB is too short (for example, shorter than 1 second), no recorded file is generated.

- If the duration of an LVB is not long (shorter than 7 days or the length of an MP4/FLV fragment), and the push is not interrupted during LVB, only one recorded file is generated.

- If the duration of an LVB is very long (longer than 7 days (HLS format) or the length of an MP4/FLV fragment), the video is forcibly fragmented to avoid the time uncertainty of the flow of the file with a longer duration in a distributed system.

- If the push is interrupted during an LVB (SDK will re-push later), a new fragment is generated every time the interruption occurs.


### 3. How to stitch fragments?
Tencent Cloud supports stitching video fragments with cloud API. For more information on how to use this API, please see [Video Stitching](/document/product/266/7821).

