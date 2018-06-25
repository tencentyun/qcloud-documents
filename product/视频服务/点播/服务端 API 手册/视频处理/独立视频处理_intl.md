## API Name
ProcessCosMedia

## Feature Description

This API (ProcessCosMedia) is used to initiate tasks for processing audios and videos stored in COS (Cloud Object Storage), including:
* Transcoding (including watermark, encryption and re-wrapper)
* Converting video to dynamic image (e.g. gif)
* Taking screenshots by time
* Using screenshot as cover
* Taking image sprite screenshots
* Porn detection

When the task is initiated, the system obtains the source video file from the input file bucket specified in the API, and writes the processing result to the specified output file bucket.

**Note**: You must complete the [configurations](/document/product/266/16923) of the input file bucket and output file bucket first.

## Task Result
This API is an asynchronous API. The task execution result can be obtained through either event notification or task query.

### Event notification
Processing and end of a task will trigger [Event Notification - Notification for Task Flow Status Changes](/document/product/266/9636), according to which the App backend can monitor the execution status of the task flow. For more information, please see [Server Event Notifications](/document/product/266/7829).

### Task query
After the task processing request is submitted, you can obtain a task ID (vodTaskId). The task execution status and result can be queried through the API [Query Task Details](/document/product/266/11724).

## Request Method

### Request domain name:
vod.api.qcloud.com

### Maximum calling frequency
100/min

### Request parameters

| Name | Required | Type | Description |
|---------|---------|---------|---------|
| input | Yes | Object | See [Input File Information Parameters](#input.EF.BC.88.E8.BE.93.E5.85.A5.E6.96.87.E4.BB.B6.E4.BF.A1.E6.81.AF.E5.8F.82.E6.95.B0.EF.BC.89) |
| output | Yes | Object | See [Output File Information Parameters](#output.EF.BC.88.E8.BE.93.E5.87.BA.E6.96.87.E4.BB.B6.E4.BF.A1.E6.81.AF.E5.8F.82.E6.95.B0.EF.BC.89) |
| mediaCheck | No | Object | See [Porn Detection Parameters](#mediacheck.EF.BC.88.E8.A7.86.E9.A2.91.E9.89.B4.E9.BB.84.E5.8F.82.E6.95.B0.EF.BC.89) |
| mediaProcess | No | Object | See [Video Processing Parameters](#mediaprocess.EF.BC.88.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E5.8F.82.E6.95.B0.EF.BC.89) |
| taskAttribute | No | Object | See [Task Attribute Configuration Parameters](#taskattribute.EF.BC.88.E4.BB.BB.E5.8A.A1.E5.B1.9E.E6.80.A7.E9.85.8D.E7.BD.AE.E5.8F.82.E6.95.B0.EF.BC.89) |
| COMMON_PARAMS | Yes | | See [Common Parameters](/document/api/213/6976) |

#### input (input file information parameters)
| Name | Required | Type | Description |
|---------|---------|---------|---------|
| bucket | Yes | String | Input file bucket (complete [configurations](/document/product/266/16923) first) |
| path | Yes | String | Input file path |

#### output (output file information parameters)
| Name | Required | Type | Description |
|---------|---------|---------|---------|
| bucket | Yes | String | Output file bucket (complete [configurations](/document/product/266/16923) first) |
| dir | Yes | String | Output file directory |

#### mediaCheck (porn detection parameters)
| Name | Required | Type | Description |
|---------|---------|---------|---------|
| pornCheckDefinition | No | Integer | Porn detection template No. |

#### mediaProcess (video processing parameters)
| Name | Required | Type | Description |
|---------|---------|---------|---------|
| transcode | No | Object | See [Control Parameters for Transcoding](#transcode.EF.BC.88.E8.BD.AC.E7.A0.81.E6.8E.A7.E5.88.B6.E5.8F.82.E6.95.B0.EF.BC.89) |
| animatedGraphics | No | Object | See [Control Parameters for Converting Video to Dynamic Image](#animatedgraphics.EF.BC.88.E8.BD.AC.E5.8A.A8.E5.9B.BE.E6.8E.A7.E5.88.B6.E5.8F.82.E6.95.B0.EF.BC.89) |
| sampleSnapshot | No | Object | See [Control Parameters for Sampling Screenshot](#samplesnapshot.EF.BC.88.E9.87.87.E6.A0.B7.E6.88.AA.E5.9B.BE.E5.8F.82.E6.95.B0.EF.BC.89) |
| snapshotByTimeOffset | No | Object | See [Control Parameters for Taking Screenshots at Specified Time Point](#snapshotbytimeoffset.EF.BC.88.E6.8C.87.E5.AE.9A.E6.97.B6.E9.97.B4.E7.82.B9.E6.88.AA.E5.9B.BE.E6.8E.A7.E5.88.B6.E5.8F.82.E6.95.B0.EF.BC.89) |
| coverBySnapshot | No | Object | See [Control Parameters for Setting Screenshot as Cover](#coverbysnapshot.EF.BC.88.E4.BD.BF.E7.94.A8.E6.88.AA.E5.9B.BE.E8.AE.BE.E7.BD.AE.E8.A7.86.E9.A2.91.E5.B0.81.E9.9D.A2.E6.8E.A7.E5.88.B6.E5.8F.82.E6.95.B0.EF.BC.89) |
| imageSprite | No | Object | See [Control Parameters for Image Sprite](#imagesprite.EF.BC.88.E9.9B.AA.E7.A2.A7.E5.9B.BE.E6.8E.A7.E5.88.B6.E5.8F.82.E6.95.B0.EF.BC.89) |

#### transcode (control parameters for transcoding)
| Name | Required | Type | Description |
|---------|---------|---------|---------|
| definition | Yes | Array | Video transcoding template list |
| definition.n | Yes | Integer | The video transcoding template No. See [Transcoding Parameter Template](/document/product/266/11701#.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF) |
| hlsMasterPlaylistDefinition | No | Array | HLS Master Playlist template list |
| hlsMasterPlaylistDefinition.n | No | Integer | HLS Master Playlist template No. |
| watermarkDefinition | No | Array | Watermark template list |
| watermarkDefinition.n | No | Integer | Watermark template No. See [Watermark Parameter Template](/document/product/266/11701#.E6.B0.B4.E5.8D.B0.E6.A8.A1.E6.9D.BF) |
| disableHigherBitrate | No | Integer | Whether to prohibit converting from low bitrate to high bitrate.<br/> 0: No. 1: Yes.<br/> Default is "No". |

#### animatedGraphics (control parameters for converting video to dynamic image)
| Name | Required | Type | Description |
|---------|---------|---------|---------|
| definition | Yes | Array | List of templates for converting video to dynamic image |
| definition.n | Yes | Integer | No. of template for converting video to dynamic image. See [Parameter Template for Converting Video to Dynamic Image](/document/product/266/11701#.E9.A2.84.E7.BD.AE.E8.BD.AC.E5.8A.A8.E5.9B.BE.E6.A8.A1.E6.9D.BF) |
| startTime | No | Integer | The start time of the dynamic image in the video (in sec) |
| endTime | No | Integer | The end time of the dynamic image in the video (in sec) |


#### sampleSnapshot (control parameters for sampling screenshot)
| Name | Required | Type | Description |
|---------|---------|---------|---------|
| definition | Yes | Array | Sampling screenshot template No. See [Sampling Screenshot Parameter Template](/document/product/266/11702#.E9.87.87.E6.A0.B7.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF). |
| definition.n | Yes | Integer | Sampling screenshot template ID |

#### snapshotByTimeOffset (control parameters for taking screenshots at specified time point)
| Name | Required | Type | Description |
|---------|---------|---------|---------|
| definition | Yes | Array | List of templates for taking screenshots by time |
| definition.n | Yes | Integer | No. of template for taking screenshots by time. See [Parameter Template for Taking Screenshots by Time](/document/product/266/11702#.E6.8C.87.E5.AE.9A.E6.97.B6.E9.97.B4.E7.82.B9.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF). |
| timeOffset | Yes | Array | List of time points for taking screenshots by time |
| timeOffset.n | Yes | Integer | Time for taking screenshots by time (in ms) |

#### coverBySnapshot (control parameters for setting screenshot as cover)
| Name | Required | Type | Description |
|---------|---------|---------|---------|
| definition | Yes | Integer | No. of template for taking screenshots by time. See [Parameter Template for Taking Screenshots by Time](/document/product/266/11702#.E6.8C.87.E5.AE.9A.E6.97.B6.E9.97.B4.E7.82.B9.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF) |
| positionType | Yes | String | Methods for taking screenshots (Time or Percent).<ul><li>Time: Take screenshots by time.</li><li>Percent: Take screenshots by percentage.</li></ul> |
| position | Yes | Integer | Time when a screenshot is taken.<ul><li>When taking screenshots by time, the value specifies when (indicated by the number of seconds in the video) to take a screenshot and use it as cover.</li><li>When taking screenshots by percentage, the value specifies where (indicated by the progress percentage in the video) to take a screenshot and use it as cover.</li></ul> |


#### imageSprite (control parameters for image sprite)
| Name | Required | Type | Description |
|---------|---------|---------|---------|
| definition | Yes | Integer | List of templates for taking image sprite screenshots |
| definition.n | Yes | Integer | The parameter template for taking image sprite screenshots. See [Image Sprite Screenshot Parameter Template](/document/product/266/11702#.E9.9B.AA.E7.A2.A7.E5.9B.BE.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF) |

#### taskAttribute (task attribute configuration parameters)
| Name | Required | Type | Description |
|---------|---------|---------|---------|
| priority | No | Integer | Priority |
| notifyMode | No | String | Notification mode for task flow status changes. Default is Finish.<ul><li> Finish: An event notification is initiated only after the task flow is completely finished.</li><li>Change: Event notification is initiated whenever the status of a subtask in the task flow changes.</li><li>None: Do not receive callbacks of this task flow. </li></ul> |
| notifyDefinition | No | Integer | Callback template No. |

### Request example
The input file resides in the bucket named as **myinputbucket**. The absolute path is **/input/F62A55F5-C4D6-4AEA-934F-7A6BFF3D8BCF.MOV**.
Perform transcoding for the input file. The transcoding template IDs include **210**, **220** and **230**.
The transcoded file is output to the **/output/test/** directory of the **myoutputbucket** bucket.
<pre>
https://vod.api.qcloud.com/v2/index.php?Action=ProcessCosMedia
&ampinput.bucket=myinputbucket
&ampinput.path=/input/F62A55F5-C4D6-4AEA-934F-7A6BFF3D8BCF.MOV
&ampoutput.bucket=myoutputbucket
&ampoutput.dir=/output/test/
&ampmediaProcess.transcode.definition.0=210
&ampmediaProcess.transcode.definition.1=220
&ampmediaProcess.transcode.definition.2=230
&ampCOMMON_PARAMS
</pre>

## API Response
### Parameters
| Name | Type | Description |
|---------|---------|---------|
| code | Integer | Error code. 0: Successful; other values: Failed. |
| message | String | Error message |
| codeDesc | String | Error code description |
| vodTaskId | String | Task ID |

### Error codes
| Error Code | Description |
|---------|---------|
| 4000-7000 | See [Common Error Codes](/document/product/266/7783) |
| 1000 | Invalid parameter |
| 10009 | Unexpected file status |
| Others | Internal error |

### Response example
```javascript
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "vodTaskId": "1256244234-procedurev2-63653704847be7b43e0f38bf2f86f54b"
}
```
