## Event Name
ProcedureStateChanged

## Event Description
If an app is configured with event notification, when the task procedure state is changed, VOD backend will notify the app backend of the event.

For details about the way in which the app backend receives the event notification, refer to [introduction to server event notification](https://cloud.tencent.com/document/product/266/7829).

> Note:
> - Notification mode for task procedure state change is decided by the task procedure's initiating parameter notifyMode. When notifyMode is Finish: an event notification is initiated only after the task procedure is completely finished; when notifyMode is Change: event notification is initiated whenever the state of a subtask in the task procedure changes; notifyMode defaults to Finish.

### Parameter Description
| Parameter | Type | Description |
|---------|---------|---------|
| version | String | Event notification version number, which is always 4.0 |
| eventType | String | Event type, which is always ProcedureStateChanged |
| data | Object | Specific callback data |
| data.status | String | Task procedure state has two types: PROCESSING and FINISH|
| data.errCode | Integer | Error code. 0: successful, other values: failed. |
| data.message | String | Error message  |
| data.fileId | String | File ID  |
| data.metaData | Object | Video meta information. This field must exist. For field information, see [metaData (video meta information)](#metadata.EF.BC.88.E8.A7.86.E9.A2.91.E5.85.83.E4.BF.A1.E6.81.AF.EF.BC.89)  |
| data.drm | Object | File encryption information. After the user specifies the encryption at the [(control parameters for transcoding](https://cloud.tencent.com/document/product/266/9642#transcode.EF.BC.88.E8.BD.AC.E7.A0.81.E6.8E.A7.E5.88.B6.E5.8F.82.E6.95.B0.EF.BC.89), the field will exist. See [drm (video encryption information)](#drm.EF.BC.88.E8.A7.86.E9.A2.91.E5.8A.A0.E5.AF.86.E4.BF.A1.E6.81.AF.EF.BC.89) for field information  |
| data.processTaskList | Array | Task list contained in the task flow. For more information, please see [processTaskList (task list)](#processtasklist.EF.BC.88.E4.BB.BB.E5.8A.A1.E5.88.97.E8.A1.A8.EF.BC.89) for the field information  |

#### metaData (video meta information)

| **Parameter** | **Type** | **Description** |
|---------|---------|---------|
| size | Integer | Video size (in byte) |
| container | String | Container type, such as m4a, mp4 |
| bitrate | Integer | The sum of the average of the video stream bit rate and the average of the audio stream bit rate (in kbps) |
| height | Integer | The maximum video stream height (in px) |
| width | Integer | The maximum video stream width (in px) |
| md5 | String | Video md5 value |
| duration | Integer | Video duration (in second) |
| videoStreamList | Array | Video stream information |
| videoStreamList.bitrate | Integer | Bit rate of video stream (in kbps) |
| videoStreamList.height | Integer | Video stream height (in px) |
| videoStreamList.width | Integer | Video stream width (in px) |
| videoStreamList.codec | String | Encoding format of video stream, such as h264 |
| videoStreamList.fps | Integer | Frame rate (in hz) |
| audioStreamList | Array | Audio stream information |
| audioStreamList.bitrate | Integer | Bit rate of audio stream (in kbps). |
| audioStreamList.samplingRate | Integer | The sampling rate (in hz) of an audio stream. |
| audioStreamList.codec | String | Encoding format of audio stream, such as aac |

#### drm (video encryption information)

| **Parameter** | **Type** | **Description** |
|---------|---------|---------|
| definition | Integer | The encryption template ID |
| keySource | String | KMS type, there are three types: VodBuildInKMS: built-in KMS of Tencent Cloud VOD; QCloudKMS: Tencent Cloud KMS system (not supported currently); PrivateKMS: used for its own KMS system (not supported currently). |
| getKeyUrl | String | Obtaining the decryption key URL |
| edkList | Array | List of encrypted data keys |

#### processTaskList (task list)
Task information list currently contains [Trancode (transcoding task)](#trancode.EF.BC.88.E8.BD.AC.E7.A0.81.E4.BB.BB.E5.8A.A1.EF.BC.89), [SampleSnapshot (sampling screenshot task)](#samplesnapshot.EF.BC.88.E9.87.87.E6.A0.B7.E6.88.AA.E5.9B.BE.E4.BB.BB.E5.8A.A1.EF.BC.89), [CoverBySnapshot (screenshot image as video cover task)](#coverbysnapshot.EF.BC.88.E6.88.AA.E5.9B.BE.E5.9B.BE.E7.89.87.E4.BD.9C.E4.B8.BA.E8.A7.86.E9.A2.91.E5.B0.81.E9.9D.A2.E4.BB.BB.E5.8A.A1.EF.BC.89), [SnapshotByTimeOffset (screenshot task at specified time point)](#snapshotbytimeoffset.EF.BC.88.E6.8C.89.E6.97.B6.E9.97.B4.E7.82.B9.E6.88.AA.E5.9B.BE.E4.BB.BB.E5.8A.A1.EF.BC.89), [PullFile (pulling video files)](https://cloud.tencent.com/document/product/266/7817), [ImageSprites (screenshot task of image sprites)](#imagesprites.EF.BC.88.E9.9B.AA.E7.A2.A7.E5.9B.BE.E6.88.AA.E5.9B.BE.E4.BB.BB.E5.8A.A1.EF.BC.89).

#### Trancode (transcoding task)

| **Parameter** | **Type** | **Description** |
|---------|---------|---------|
| taskType | String | Task type, which is always Transcode |
| status | String | Task statuses. There are three types: PROCESSING, SUCCESS and FAIL. |
| errCode | Integer | Error code. 0: successful, other values: failed, where, 30009: failed by the exception in original file; 30010: failed by the system or unknown reason |
| message | String | Error message |
| input | Object | Input information of tasks |
| input.definition | Integer | Transcode template ID. |
| input.watermark | Integer | Whether to add watermark. 1: Yes, 0: No. Which is determined by users' transcoding configuration |
| output | Object | The output information of the task. If the task succeeds, the field will be displayed. If it fails, no field will be displayed |
| output.url | String | Video URL |
| output.size | Integer | Video size (in byte) |
| output.container | String | Container type, such as m4a, mp4 |
| output.bitrate | Integer | The sum of the video stream bit rate and the audio stream bit rate (in kbps) |
| output.height | Integer | The maximum video stream height (in px) |
| output.width | Integer | The maximum video stream width (in px) |
| output.md5 | String | Video md5 value |
| output.duration | Integer | Video duration (in second) |
| output.videoStreamList | Array | Video stream information, element field and meta information have the same videoStreamList |
| output.audioStreamList | Array | Audio stream information, element field and metadata have the same audioStreamList |

#### SampleSnapshot (sampling screenshot task)

| **Parameter** | **Type** | **Description** |
|---------|---------|---------|
| taskType | String | Task type, which is always SampleSnapshot |
| status | String | Task statua. There are three types of status: PROCESSING, SUCCESS and FAIL. |
| errCode | Integer | Error code. 0: successful, other values: failed, where, 30009: failed by the exception in original file; 30010: failed by the system or unknown reason |
| message | String | Error message |
| input | Object | Input information of tasks |
| input.definition | Integer | Sample screenshot template ID |
| output | Object | The output information of the task. If the task succeeds, the field will be displayed. If it fails, no field will be displayed |
| output.imageUrls | Array | String array, generated screenshot URL list |

#### SnapshotByTimeOffset (screenshot task at specified time point)
	
| **Parameter** | **Type** | **Description** |
|---------|---------|---------|
| taskType | String | Task type, which is always SnapshotByTimeOffset |
| status | String | Task statuses. There are three types: PROCESSING, SUCCESS and FAIL. |
| errCode | Integer | Error code. 0: successful, other values: failed, where, 30009: failed by the exception in original file; 30010: failed by the system or unknown reason |
| message | String | Error message |
| input | Object | Input information of tasks |
| input.definition | Integer | Sample screenshot template ID at specified time point |
| input.timeOffset | Array | An array of integers indicating the time offset of the screenshot (in millisecond). |
| output | Object | The output information of the task. If the task succeeds, the field will be displayed. If it fails, no field will be displayed |
| output.imgInfo | Array | Generated screenshot information list |
| output.imgInfo.timeOffset | Integer | Time offset of the screenshot (in millisecond) |
| output.imgInfo.url | String | Screenshot URL |



#### CoverBySnapshot (screenshot image as video cover task)

| **Parameter** | **Type** | **Description** |
|---------|---------|---------|
| taskType | String | Task type, which is always CoverBySnapshot |
| status | String | Task status. There are three types: PROCESSING, SUCCESS and FAIL. |
| errCode | Integer | Error code. 0: successful, other values: failed, where, 30009: failed by the exception in original file; 30010: failed by the system or unknown reason |
| message | String | Error message |
| input | Object | Input information of tasks |
| input.definition | Integer | Sample screenshot template ID |
| input.positionType | String | Screenshot method. Time: Take screenshot by time points; Percent: Take screenshot by percentage. |
| input.position | Integer | Screenshot position. When taking screenshot by time point, the value specifies when (indicated by the number of seconds into the video) to take a screenshot and use it as cover. When taking screenshot by percentage, the value specifies when (indicated by the progress percentage into the video) to take a screenshot and use it as cover. |
| output | Object | The output information of the task. If the task succeeds, the field will be displayed. If it fails, no field will be displayed |
| output.imageUrl | Array | URL of the screenshot as the video cover |

#### PullFile (pulling video file task)

| **Parameter** | **Type** | **Description** |
|---------|---------|---------|
| taskType | String | Task type, which is always PullFile |
| status | String | Task status. There are three types: PROCESSING, SUCCESS and FAIL. |
| errCode | Integer | Error code. 0: successful, other values: failed. |
| message | String | Error message |
| input | Object | Input information of tasks |
| input.url | String | The URL of the video to be pulled |
| input.fileName | String | Name of video file |
| input.md5 | Integer | MD5 of video file |
| output | Object | The output information of the task. If the task succeeds, the field will be displayed. If it fails, no field will be displayed |
| output.fileId | String | Video file ID |
| output.fileSize | String | Video file size |
| output.url | String | Playback URL of video file |

#### ImageSprites (screenshot task of image sprites)

| **Parameter** | **Type** | **Description** |
|---------|---------|---------|
| taskType | String | Task type, which is always ImageSprites |
| status | String | Task status. There are three types: PROCESSING, SUCCESS and FAIL. |
| errCode | Integer | Error code. 0: successful, other values: failed. |
| message | String | Error message |
| input | Object | The input information of the task. If the task succeeds, the field will be displayed. If it fails, no field will be displayed |
| input.definition | Integer | Image sprite screenshot template ID |
| output | Object | The output information of the task |
| output.totalCount | Integer | Total number of images in image sprite |
| output.urlList | Array | String array, generated image sprite URL list |
| output.webVttUrl | String | The image sprite' subgraph location-time relation WebVtt file URL |

## Example

- For [HTTP callback](https://cloud.tencent.com/document/product/266/7829#http.E5.9B.9E.E8.B0.83), the following is the HTTP Post Body;
- For [reliable notification based on message queue](https://cloud.tencent.com/document/product/266/7829#.E5.9F.BA.E4.BA.8E.E6.B6.88.E6.81.AF.E9.98.9F.E5.88.97.E7.9A.84.E5.8F.AF.E9.9D.A0.E9.80.9A.E7.9F.A5), the following is the content of eventList.eventContent in the returned packet of  API[PullEvent](https://cloud.tencent.com/document/product/266/7818).

### Example:

```javascript
{
    "version": "4.0",
    "eventType": "ProcedureStateChanged",
    "data": {
        "vodTaskId": "251000333-mango-c27bdf65ea06646171e714f25f5aac63",
        "status": "PROCESSING",
        "message": "",
        "errCode": 0,
        "fileId": "123123123",
        "metaData": {
            "size": 10556,
            "container": "m4a",
            "bitrate": 246035,
            "height": 480,
            "width": 640,
            "md5": "b3ae6ed07d9bf4efeeb94ed2d37ff3e3",
            "duration": 3601,
            "videoStreamList": [
                {
                    "bitrate": 246000,
                    "height": 480,
                    "width": 640,
                    "codec": "h264",
                    "fps": 22
                }
            ],
            "audioStreamList": [
                {
                    "codec": "aac",
                    "samplingRate": 44100,
                    "bitrate": 35
                }
            ]
        },
        "drm": {
            "definition": 10,
            "getKeyUrl": "https://123.xxx.com/getkey",
            "keySource": "VodBuildInKMS",
            "edkList": [
                "232abc30"
            ]
        },
        "processTaskList": [
            {
                "taskType": "Transcode",
                "status": "PROCESSING",
                "errCode": 0,
                "message": "",
                "input": {
                    "definition": 10,
                    "watermark": 1
                }
            },
            {
                "taskType": "Transcode",
                "status": "SUCCESS",
                "errCode": 0,
                "message": "",
                "input": {
                    "definition": 20,
                    "watermark": 1
                },
                "output": {
                    "url": "http://125xx.vod2.myqcloud.com/9fcd41e6vodgzp1251953760/7585975f9031868222912340/f20.mp4",
                    "size": 10556,
                    "container": "m4a",
                    "md5": "b3ae6ed07d9bf4efeeb94ed2d37ff3e3",
                    "bitrate": 246035,
                    "height": 480,
                    "width": 640,
                    "duration": 3601,
                    "videoStreamList": [
                        {
                            "bitrate": 246000,
                            "height": 480,
                            "width": 640,
                            "codec": "h264",
                            "fps": 222
                        }
                    ],
                    "audioStreamList": [
                        {
                            "codec": "aac",
                            "samplingRate": 44100,
                            "bitrate": 35
                        }
                    ]
                }
            },
            {
                "taskType": "SampleSnapshot",
                "status": "SUCCESS",
                "errCode": 0,
                "message": "",
                "input": {
                    "definition": 10
                },
                "output": {
                    "imageUrls": [
                        "http://125xx.vod2.myqcloud.com/vodtrans125xx/14508071098244929440/shotup/xx1.png",
                        "http://125xx.vod2.myqcloud.com/vodtrans125xx/14508071098244929440/shotup/xx2.png",
                        "http://125xx.vod2.myqcloud.com/vodtrans125xx/14508071098244929440/shotup/xx3.png",
                        "http://125xx.vod2.myqcloud.com/vodtrans125xx/14508071098244929440/shotup/xx4.png",
                        "http://125xx.vod2.myqcloud.com/vodtrans125xx/14508071098244929440/shotup/xx5.png",
                        "http://125xx.vod2.myqcloud.com/vodtrans125xx/14508071098244929440/shotup/xx6.png",
                        "http://125xx.vod2.myqcloud.com/vodtrans125xx/14508071098244929440/shotup/xx7.png",
                        "http://125xx.vod2.myqcloud.com/vodtrans125xx/14508071098244929440/shotup/xx8.png",
                        "http://125xx.vod2.myqcloud.com/vodtrans125xx/14508071098244929440/shotup/xx9.png",
                        "http://125xx.vod2.myqcloud.com/vodtrans125xx/14508071098244929440/shotup/xx10.png"
                    ]
                }
            },
            {
                "taskType": "CoverBySnapshot",
                "status": "SUCCESS",
                "errCode": 0,
                "message": "",
                "input": {
                    "definition": 10,
                    "position": 10,
                    "positionType": "Percent"
                },
                "output": {
                    "imageUrl": "http://125xx.vod2.myqcloud.com/vodtrans125xx/14508071098244929440/shotup/xx1.png"
                }
            },
            {
                "taskType": "SnapshotByTimeOffset",
                "status": "SUCCESS",
                "message": "",
                "errCode": 0,
                "input": {
                    "definition": 10,
                    "timeOffset": [
                        300,
                        400
                    ]
                },
                "output": {
                    "imgInfo": [
                        {
                            "timeOffset": 300,
                            "url": "http://125xx.vod2.myqcloud.com/42f909a8vodtransgzp251000333/dee2963524820810452267193/snapshot/1502280085_887773835.100_300.jpg"
                        },
                        {
                            "timeOffset": 400,
                            "url": "http://125xx.vod2.myqcloud.com/42f909a8vodtransgzp251000333/dee2963524820810452267193/snapshot/1502280085_887773835.100_400.jpg"
                        }
                    ]
                }
            },
            {
                "taskType": "ImageSprites",
                "status": "SUCCESS",
                "message": "SUCCESS",
                "errCode": 0,
                "input": {
                    "definition": 10
                },
                "output": {
                    "totalCount": 106,
                    "urlList": [
                        "http://125xx.vod2.myqcloud.com/vod125xx/14508071098244929440/1502280085_887773835.100_0.png",
                        "http://125xx.vod2.myqcloud.com/vod125xx/14508071098244929440/1502280085_887773835.100_1.png"
                    ],
                    "webVttUrl": "http://125xx.vod2.myqcloud.com/vod125xx/14508071098244929440/1502280085_887773835.vtt"
                }
            }
        ]
    }
}
```

### Error Codes

The errCode field in the event notification packet indicates the result of the video processing task. For more information, please see [error codes regarding video processing Ooerations](https://cloud.tencent.com/document/product/266/7783#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E6.93.8D.E4.BD.9C.E9.94.99.E8.AF.AF.E7.A0.81.E8.AF.B4.E6.98.8E).

