## API Name
ProcessFile

## Feature Description
This VOD task flow related API is used by developers to initiate various processing tasks for a single video, including:
1. Video transcoding (including watermark, encryption, and re-wrapping);
2. Sample screenshot;
3. Using screenshot as cover.

This asynchronous API is called only to initiate a series of video processing tasks. Task status changes (including end of tasks) in the task flow can be perceived via the [Event Notification](#.E4.BA.8B.E4.BB.B6.E9.80.9A.E7.9F.A5) mechanism.

After a task is completed, the execution result (e.g. URL of the transcoded output file) of each asynchronous task can be obtained through API [GetVideoInfo](https://cloud.tencent.com/document/product/266/8586).

**Note: This API is only supported for VOD 4.0.**

## Event Notification

Task status changes (or end of tasks) in the task flow will trigger [Event Notification-Notification for Task Flow Status Changes](https://cloud.tencent.com/document/product/266/9636). The backend of app can monitor the execution status of task flow according to this.

For more information, please see [Server Event Notification Introduction](https://cloud.tencent.com/document/product/266/7829).

## Request Method

### Request Domain
vod.api.qcloud.com

### Max Calling Frequency
100/min

### Request Parameters

| Parameter | Required | Type | Description |
|---------|---------|---------|---------|
| fileId | Yes | String | File ID |
| transcode | No | Object | See [Control Parameters for Transcoding](#transcode.EF.BC.88.E8.BD.AC.E7.A0.81.E6.8E.A7.E5.88.B6.E5.8F.82.E6.95.B0.EF.BC.89) |
| sampleSnapshot | No | Object | See [Control Parameters for Sample Screenshot](#samplesnapshot.EF.BC.88.E9.87.87.E6.A0.B7.E6.88.AA.E5.9B.BE.E5.8F.82.E6.95.B0.EF.BC.89) |
| coverBySnapshot | No | Object | See [Control Parameters for Setting Screenshot as Cover](#coverbysnapshot.EF.BC.88.E4.BD.BF.E7.94.A8.E6.88.AA.E5.9B.BE.E8.AE.BE.E7.BD.AE.E8.A7.86.E9.A2.91.E5.B0.81.E9.9D.A2.E6.8E.A7.E5.88.B6.E5.8F.82.E6.95.B0.EF.BC.89) |
| snapshotByTimeOffset | No | Object | See [Control Parameters for Taking Screenshot at Specified Time Point](#snapshotbytimeoffset.EF.BC.88.E6.8C.87.E5.AE.9A.E6.97.B6.E9.97.B4.E7.82.B9.E6.88.AA.E5.9B.BE.E6.8E.A7.E5.88.B6.E5.8F.82.E6.95.B0.EF.BC.89) |
| imageSprite | No | Object | See [Control Parameters For Image Sprite)](#imagesprite.EF.BC.88.E9.9B.AA.E7.A2.A7.E5.9B.BE.E6.8E.A7.E5.88.B6.E5.8F.82.E6.95.B0.EF.BC.89) |
| notifyMode | No | String | Notification mode for task flow status changes. Finish: An event notification is initiated only after the task flow is completely finished; Change: Event notification is initiated whenever the status of a subtask in the task flow changes; None: Do not receive callbacks of this task flow. The default is Finish. | 
| COMMON_PARAMS | Yes |  | For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976) |

#### transcode (Control Parameters for Transcoding)

| **Parameter** | **Required** | **Type** | **Description** |
|---------|---------|---------|---------|
| definition | Yes | Array | The No. of transcoding output template, see [Transcoding Parameter Template](https://cloud.tencent.com/document/product/266/11701#.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF). |
| watermark | No | Integer | See [Watermark Parameter Template](https://cloud.tencent.com/document/product/266/11701#.E6.B0.B4.E5.8D.B0.E6.A8.A1.E6.9D.BF). For now, the only available value is 1, which indicates the default template. Empty value means no watermark is used. |
| hlsMasterPlaylist | No | Integer | If the specified transcode output parameter contains multiple HLS specifications, and hlsMasterPlaylist=1, a multi-bitrate HLS file containing HLS Master Playlist will be generated after transcoding is finished. The "definition" of this file is a fixed value (10000). The player that supports HLS standard can adaptively choose video stream according to bitrate to play the file. |
| disableHigherBitrate | No | Integer | Whether to prohibit converting from low bitrate to high bitrate. 0: No. 1: Yes. The default is "No". (Note 1) |
| drm | No | Object | Control parameter for video encryption. See [Video Encryption Solution](https://cloud.tencent.com/document/product/266/9638). | 
| drm.definition | Yes | Integer | Encryption method. See [Video Encryption Parameter Template](https://cloud.tencent.com/document/product/266/9645). |

After the task flow is completed, the transcoding result can be obtained from the [transcodeInfo](https://cloud.tencent.com/document/product/266/8586#transcodeinfo.EF.BC.88.E8.A7.86.E9.A2.91.E8.BD.AC.E7.A0.81.E7.BB.93.E6.9E.9C.E4.BF.A1.E6.81.AF.EF.BC.89) object in the response packet of API [GetVideoInfo](https://cloud.tencent.com/document/product/266/8586).

> Note 1:
> Converting a low bitrate video file to a high bitrate file can lead to unnecessary bandwidth usage. When this option is enabled, the target template will be ignored if the bitrate of the target transcoding template is higher than the bitrate of the source video. Suppose the bitrate of the source video is 800 Kbps, the No. of the target transcoding output templates are 10, 20, 30 and 40, with respective bitrates of 256 Kbps, 512 Kbps, 1,024 Kbps and 2,500 Kbps. Then the transcoding templates 30 and 40 are ignored, and only the templates 10 and 20 are transcoded.

#### sampleSnapshot (Control Parameters for Sample Screenshot)

| **Parameter** | **Required** | **Type** | **Description** |
|---------|---------|---------|---------|
| definition | Yes | Integer | The no. of sampling screenshot template. See [Sampling Screenshot Parameter Template](https://cloud.tencent.com/document/product/266/11702#.E9.87.87.E6.A0.B7.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF). |

After the task flow is completed, the screenshot URL can be obtained from the sampleSnapshotInfo.imageUrls field in the response packet of API [GetVideoInfo](https://cloud.tencent.com/document/product/266/8586).

#### snapshotByTimeOffset (Control Parameters for Taking Screenshot at Specified Time Point)

| **Parameter** | **Required** | **Type** | **Description** |
|---------|---------|---------|---------|
| definition | Yes | Integer | The template no. of the screenshot at a specified time point. See [Screenshot Parameter Template at a Specified Time Point](https://cloud.tencent.com/document/product/266/11702#.E6.8C.87.E5.AE.9A.E6.97.B6.E9.97.B4.E7.82.B9.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF). |
| timeOffset | Yes | Array | An array of integers indicating the time offset of the screenshot (in millisecond). |

After the task flow is completed, the screenshot information at a fixed time point can be obtained from the snapshotByTimeOffsetInfo field in the response packet of API [GetVideoInfo](https://cloud.tencent.com/document/product/266/8586).

#### coverBySnapshot (Control Parameters for Setting Screenshot as Cover)

| **Parameter** | **Required** | **Type** | **Description** |
|---------|---------|---------|---------|
| definition | Yes | Integer | The template no. of the screenshot at a specified time point. See [Screenshot Parameter Template at a Specified Time Point](https://cloud.tencent.com/document/product/266/11702#.E6.8C.87.E5.AE.9A.E6.97.B6.E9.97.B4.E7.82.B9.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF). |
| positionType | Yes | String | Screenshot method. Time: Take screenshot by time points; Percent: Take screenshot by percentage. |
| position | Yes | Integer | Screenshot position. When taking screenshot by time point, the value specifies when (indicated by the number of seconds in the video) to take a screenshot and use it as cover. When taking screenshot by percentage, the value specifies when (indicated by the progress percentage in the video) to take a screenshot and use it as cover. |

After the task flow is completed, the screenshot URL can be obtained from the basicInfo.coverUrl field in the response packet of API [GetVideoInfo](https://cloud.tencent.com/document/product/266/8586).


#### imageSprite (Control Parameters For Image Sprite)

| **Parameter** | **Required** | **Type** | **Description** |
|---------|---------|---------|---------|
| definition | Yes | Integer | The template no. of the image sprite screenshot. See [Image Sprite Screenshot Parameter Template](https://cloud.tencent.com/document/product/266/11702#.E9.9B.AA.E7.A2.A7.E5.9B.BE.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF).|

After the task flow is completed, the result image sprite can be obtained from the imageSpriteInfo field in the response packet of API [GetVideoInfo](https://cloud.tencent.com/document/product/266/8586).


### Request Example

#### General Video Transcoding Example
The following example indicates:
1. Transcode video. The output templates of the transcoding process are 10, 20, 30 and 40, while converting from low bitrate video to high bitrate video is disabled;
2. Watermark needs to be applied during the transcoding process. The watermark template number is 1 (the default template);
3. Take sample screenshot for the video. The template number of the sample screenshot is 10;
An event notification is initiated whenever the status of a subtask in the task flow changes.


<pre>
https://vod.api.qcloud.com/v2/index.php?Action=ProcessFile
&fileId=24961954183381008
&transcode.definition.0=210
&transcode.definition.1=220
&transcode.definition.3=230
&transcode.definition.4=240
&transcode.disableHigherBitrate=1
&transcode.watermark=1
&sampleSnapshot.definition=10
&notifyMode=Change
&COMMON_PARAMS
</pre>

#### Video Encryption Transcoding Example

The following example indicates:
1. Transcode video file. The target output templates of the transcoding process are 210, 220, 230 and 240, while converting from low bitrate video to high bitrate video is disabled;
2. During transcoding, the video file needs to be encrypted using encryption policy with a template no. of 10;
3. Event notification is initiated only after the entire task flow is completed.

```
https://vod.api.qcloud.com/v2/index.php?Action=ProcessFile
&fileId=24961954183381008
&transcode.definition.0=210
&transcode.definition.1=220
&transcode.definition.3=230
&transcode.definition.4=240
&transcode.disableHigherBitrate=1
&transcode.drm.definition=10
&notifyMode=Finish
&COMMON_PARAMS
```

#### Example of Generating Multi-bitrate HLS Video File

The following example indicates:
1. Transcode video file. The target output templates of the transcode process are 210, 220, 230 and 240, while converting from low bitrate video to high bitrate video is disabled;
2. Generate HLS file containing four bitrates: 210, 220, 230, 240;
3. Event notification is initiated only after the entire task flow is completed.

```
https://vod.api.qcloud.com/v2/index.php?Action=ProcessFile
&fileId=24961954183381008
&transcode.definition.0=210
&transcode.definition.1=220
&transcode.definition.3=230
&transcode.definition.4=240
&transcode.disableHigherBitrate=1
&transcode.hlsMasterPlaylist=1
&notifyMode=Finish
&COMMON_PARAMS
```

## API Response

### Parameter Description
| Parameter | Type | Description |
|---------|---------|---------|
| code | Integer | Error code, 0: Successful; other values: Failed. |
| message | String | Error message |
| vodTaskId | String | Task ID |

### Error Codes
| Error Code | Description |
|---------|---------|
| 4000-7000 | For more information, please see [Common Error Codes](https://cloud.tencent.com/document/product/266/7783)  |


### Response Example
```javascript
{
    "code": 0,
    "message": "",
    "vodTaskId": "125xx-Procedure-6a651e8d148c512af27f3b5f3d60f43a"
}
```

