## Event Name
ProcedureStateChanged

## Event Description
If an App is configured with event notification, when the task flow status is changed, VOD backend notifies the App backend of the event.

For more information on how the App backend receives the event notification, please see [Overview of Server Event Notifications](/document/product/266/7829).

> Note:
> - Notification mode for the task flow status change depends on the parameter notifyMode specified when the task flow is initiated. If notifyMode is Finish (default): an event notification is initiated only after the task procedure is completely finished. If notifyMode is Change: event notification is initiated whenever the status of a subtask in the task flow changes.

### Parameter Description
| Name | Type | Description |
|---------|---------|---------|
| version | String | Event notification version number, which is always 4.0 |
| eventType | String | Event type, which is always ProcedureStateChanged |
| data | Object | Specific callback data |
| data.status | String | Task flow status, including PROCESSING and FINISH |
| data.errCode | Integer | Error code. 0: Successful; other values: Failed. |
| data.message | String |　Error message  |
| data.fileId | String | File ID  |
| data.metaData | Object | Video meta information, which must be specified. For more information, please see [metaData (video meta information)](#metadata.EF.BC.88.E8.A7.86.E9.A2.91.E5.85.83.E4.BF.A1.E6.81.AF.EF.BC.89)  |
| data.aiReview | Object | AI porn detection result. This field exists after users apply for porn detection feature from the backend. For more information, please see [metaData (video meta information)](#metadata.EF.BC.88.E8.A7.86.E9.A2.91.E5.85.83.E4.BF.A1.E6.81.AF.EF.BC.89) |
| data.drm | Object | File encryption information. This field exists after users specify the encryption in the [Control Parameters for Transcoding](/document/product/266/9642#transcode.EF.BC.88.E8.BD.AC.E7.A0.81.E6.8E.A7.E5.88.B6.E5.8F.82.E6.95.B0.EF.BC.89) when they initiate the task flow. For more information, please see [drm (video encryption information)](#drm.EF.BC.88.E8.A7.86.E9.A2.91.E5.8A.A0.E5.AF.86.E4.BF.A1.E6.81.AF.EF.BC.89)  |
| data.processTaskList | Array | Task list contained in the task flow. For more information, please see [processTaskList (task list)](#processtasklist.EF.BC.88.E4.BB.BB.E5.8A.A1.E5.88.97.E8.A1.A8.EF.BC.89)  |

#### metaData (Video Meta Information)

| **Parameter Name** | **Type** | **Description** |
|---------|---------|---------|
| size | Integer | Video size (in byte) |
| container | String | Container type, such as M4A, MP4 |
| bitrate | Integer | The sum of the average video stream bitrate and the average audio stream bitrate (in Kbps) |
| height | Integer | The maximum video stream height (in px) |
| width | Integer | The maximum video stream width (in px) |
| md5 | String | Video MD5 value |
| duration | Integer | Video duration (in sec) |
| videoStreamList | Array | Video stream information |
| videoStreamList.bitrate | Integer | Video stream bitrate (in Kbps) |
| videoStreamList.height | Integer | Video stream height (in px) |
| videoStreamList.width | Integer | Video stream width (in px) |
| videoStreamList.codec | String | Encoding format of video stream, such as h264 |
| videoStreamList.fps | Integer | Frame rate (in Hz) |
| audioStreamList | Array | Audio stream information |
| audioStreamList.bitrate | Integer | Audio stream bitrate (in Kbps) |
| audioStreamList.samplingRate | Integer | Sampling rate of audio stream (in Hz) |
| audioStreamList.codec | String | Encoding format of audio stream, such as AAC |

#### aiReview (AI Porn Detection Result)

| **Parameter Name** | **Type** | **Description** |
|---------|---------|---------|
| definition | Integer | ID of AI porn detection template |
| riskType | Array | An array of strings for specifying the type of risks identified by AI porn detection. Porn is the only type |
| imgInfo.url | String | The URL of screenshot identified as risky |
| imgInfo.riskType | String | Screenshot risk type. Porn is the only type |

#### drm (Video Encryption Information)

| **Parameter Name** | **Type** | **Description** |
|---------|---------|---------|
| definition | Integer | Encryption template ID |
| keySource | String | KMS type, including: VodBuildInKMS: Built-in KMS of Tencent Cloud VOD; QCloudKMS: Tencent Cloud KMS system (not supported); PrivateKMS: Self-built KMS system (not supported). |
| getKeyUrl | String | Get the decryption key URL |
| edkList | Array | List of encrypted data keys |

#### processTaskList (Task List)
Task information list, including [Trancode (transcoding task)](#trancode.EF.BC.88.E8.BD.AC.E7.A0.81.E4.BB.BB.E5.8A.A1.EF.BC.89), [SampleSnapshot (sampling screenshot task)](#samplesnapshot.EF.BC.88.E9.87.87.E6.A0.B7.E6.88.AA.E5.9B.BE.E4.BB.BB.E5.8A.A1.EF.BC.89), [CoverBySnapshot (task of using screenshot image as video cover)](#coverbysnapshot.EF.BC.88.E6.88.AA.E5.9B.BE.E5.9B.BE.E7.89.87.E4.BD.9C.E4.B8.BA.E8.A7.86.E9.A2.91.E5.B0.81.E9.9D.A2.E4.BB.BB.E5.8A.A1.EF.BC.89), [SnapshotByTimeOffset (task of taking screenshot by time points)](#snapshotbytimeoffset.EF.BC.88.E6.8C.89.E6.97.B6.E9.97.B4.E7.82.B9.E6.88.AA.E5.9B.BE.E4.BB.BB.E5.8A.A1.EF.BC.89), [PullFile (pulling video files)](/document/product/266/7817), [ImageSprites (task of taking screenshot of image sprites)](#imagesprites.EF.BC.88.E9.9B.AA.E7.A2.A7.E5.9B.BE.E6.88.AA.E5.9B.BE.E4.BB.BB.E5.8A.A1.EF.BC.89).

#### Trancode (Transcoding Task)

| **Parameter Name** | **Type** | **Description** |
|---------|---------|---------|
| taskType | String | Task type, which is always Transcode |
| status | String | Task status, including PROCESSING, SUCCESS and FAIL |
| errCode | Integer | Error code. 0: Successful; other values: Failed. Note: 30009: Failed due to original file exception; 30010: System failure or unknown |
| message | String | Error message |
| input | Object | Input information of task |
| input.definition | Integer | Transcoding template ID |
| input.watermark | Integer | Whether to add watermark (1: Yes, 0: No), which depends on transcoding configuration |
| output | Object | Output information of task. This field is returned if the task is successful. Otherwise, it is not returned |
| output.url | String | Video URL |
| output.size | Integer | Video size (in byte) |
| output.container | String | Container type, such as M4A, MP4 |
| output.bitrate | Integer | The sum of the video stream bitrate and the audio stream bitrate (in Kbps) |
| output.height | Integer | The maximum video stream height (in px) |
| output.width | Integer | The maximum video stream width (in px) |
| output.md5 | String | Video MD5 value |
| output.duration | Integer | Video duration (in sec) |
| output.videoStreamList | Array | Video stream information. "videoStreamList " in the element field is the same as that in the meta information |
| output.audioStreamList | Array | Audio stream information. "audioStreamList" in the element field is the same as that in the meta information |

#### SampleSnapshot (Sampling Screenshot Task)

| **Parameter Name** | **Type** | **Description** |
|---------|---------|---------|
| taskType | String | Task type, which is always SampleSnapshot |
| status | String | Task status, including PROCESSING, SUCCESS and FAIL |
| errCode | Integer | Error code. 0: Successful; other values: Failed. Note: 30009: Failed due to original file exception; 30010: System failure or unknown |
| message | String | Error message |
| input | Object | Input information of task |
| input.definition | Integer | Sampling screenshot template ID |
| output | Object | Output information of task. This field is returned if the task is successful. Otherwise, it is not returned |
| output.imageUrls | Array | String array, indicating the generated screenshot URL list |

#### SnapshotByTimeOffset (Task of Taking Screenshot by Time Points)
	
| **Parameter Name** | **Type** | **Description** |
|---------|---------|---------|
| taskType | String | Task type, which is always SnapshotByTimeOffset |
| status | String | Task status, including PROCESSING, SUCCESS and FAIL |
| errCode | Integer | Error code. 0: Successful; other values: Failed. Note: 30009: Failed due to original file exception; 30010: System failure or unknown |
| message | String | Error message |
| input | Object | Input information of task |
| input.definition | Integer | Template ID of taking screenshot by time points |
| input.timeOffset | Array | Integer array, indicating the time offset of the screenshot (in ms) |
| output | Object | Output information of task. This field is returned if the task is successful. Otherwise, it is not returned |
| output.imgInfo | Array | Generated screenshot information list |
| output.imgInfo.timeOffset | Integer | Time offset of the screenshot (in ms) |
| output.imgInfo.url | String | Screenshot URL |



#### CoverBySnapshot (Task of Using Screenshot Image as Video Cover)

| **Parameter Name** | **Type** | **Description** |
|---------|---------|---------|
| taskType | String | Task type, which is always CoverBySnapshot |
| status | String | Task status, including PROCESSING, SUCCESS and FAIL |
| errCode | Integer | Error code. 0: Successful; other values: Failed. Note: 30009: Failed due to original file exception; 30010: System failure or unknown |
| message | String | Error message |
| input | Object | Input information of task |
| input.definition | Integer | Sampling screenshot template ID |
| input.positionType | String | Method for taking screenshot. Time: Take screenshot by time points; Percent: Take screenshot by percentage |
| input.position | Integer | Screenshot position. When taking screenshot by time point, the value specifies when (indicated by the number of seconds into the video) to take a screenshot and use it as cover. When taking screenshot by percentage, the value specifies when (indicated by the progress percentage into the video) to take a screenshot and use it as cover. |
| output | Object | Output information of task. This field is returned if the task is successful. Otherwise, it is not returned |
| output.imageUrl | Array | URL of the screenshot used as the video cover |

#### PullFile (Task of Pulling Video File)

| **Parameter Name** | **Type** | **Description** |
|---------|---------|---------|
| taskType | String | Task type, which is always PullFile |
| status | String | Task status, including PROCESSING, SUCCESS and FAIL |
| errCode | Integer | Error code. 0: Successful; other values: Failed. |
| message | String | Error message |
| input | Object | Input information of task |
| input.url | String | URL of the video to be pulled |
| input.fileName | String | Name of video file |
| input.md5 | Integer | MD5 of video file |
| output | Object | Output information of task. This field is returned if the task is successful. Otherwise, it is not returned |
| output.fileId | String | Video file ID |
| output.fileSize | String | Video file size |
| output.url | String | Playback URL of video file |

#### ImageSprites (Task of Taking Screenshot of Image Sprites)

| **Parameter Name** | **Type** | **Description** |
|---------|---------|---------|
| taskType | String | Task type, which is always ImageSprites |
| status | String | Task status, including PROCESSING, SUCCESS and FAIL |
| errCode | Integer | Error code. 0: Successful; other values: Failed. |
| message | String | Error message |
| input | Object | Input information of task. This field is returned if the task is successful. Otherwise, it is not returned |
| input.definition | Integer | Image sprite template ID |
| output | Object | Output information of task |
| output.totalCount | Integer | Total number of images in image sprite |
| output.urlList | Array | String array, indicating the generated image sprite URL list |
| output.webVttUrl | String | URL of WebVtt file indicating the relation of location and time between image sprite and sub-image |

## Example

- For [HTTP Callback](/document/product/266/7829#http.E5.9B.9E.E8.B0.83), the following is the HTTP Post Body.
- For [Reliable Notification Based on Message Queue](/document/product/266/7829#.E5.9F.BA.E4.BA.8E.E6.B6.88.E6.81.AF.E9.98.9F.E5.88.97.E7.9A.84.E5.8F.AF.E9.9D.A0.E9.80.9A.E7.9F.A5), the following is the content of eventList.eventContent in the returned packet of [PullEvent API](/document/product/266/7818).

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
			"videoStreamList": [{
				"bitrate": 246000,
				"height": 480,
				"width": 640,
				"codec": "h264",
				"fps": 22
			}],
			"audioStreamList": [{
				"codec": "aac",
				"samplingRate": 44100,
				"bitrate": 35
			}]
		},
		"aiReview": {
			"definition": 1,
			"riskType": ["Porn"],
			"imgInfo": [{
				"url": "http://125xxx.vod2.myqcloud.com/vodtransgzp1251132654/5284699061540709797/1516089296_21x9179645.100_525000.jpg",
				"riskType": ["Porn"]
			}, {
				"url": "http://125xxx.vod2.myqcloud.com/vodtransgzp1251132654/5284699061540709797/1516089296_2x19179645.100_1020000.jpg",
				"riskType": ["Porn"]
			}, {
				"url": "http://125xxx.vod2.myqcloud.com/vodtransgzp1251132654/5284699061540709797/1516089296_2x19179645.100_1110000.jpg",
				"riskType": ["Porn"]
			}]
		},
		"drm": {
			"definition": 10,
			"getKeyUrl": "https://123.xxx.com/getkey",
			"keySource": "VodBuildInKMS",
			"edkList": [
				"232abc30"
			]
		},
		"processTaskList": [{
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
					"videoStreamList": [{
						"bitrate": 246000,
						"height": 480,
						"width": 640,
						"codec": "h264",
						"fps": 222
					}],
					"audioStreamList": [{
						"codec": "aac",
						"samplingRate": 44100,
						"bitrate": 35
					}]
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
					"imgInfo": [{
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

The errCode field in the event notification packet indicates the result of the video processing task. For more information, please see [Error Codes Regarding Video Processing Operations](/document/product/266/7783#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E6.93.8D.E4.BD.9C.E9.94.99.E8.AF.AF.E7.A0.81.E8.AF.B4.E6.98.8E).

