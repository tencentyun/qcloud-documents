## API Name
UpdateTranscodeTemplate

## Feature Overview
This API is used to update a transcoding template.


## Request Method

### Request Domain
vod.api.qcloud.com

### Max Calling Frequency
100/min

### Parameter Description
| Parameter | Required | Type | Description |
|---------|---------|---------|---------|
| definition | Yes | Integer | Transcoding template ID. |
| name | No | String | Name of the transcoding template, which must be less than 64 bytes. |
| container | No | String | Container format: mp4, flv, hls. |
| comment | No | String | Description of the transcoding template, which must be less than 256 bytes. |
| isFiltrateVideo | No | Integer | Remove video data. 1: Remove. 0: Reserve. |
| isFiltrateAudio | No | Integer | Remove audio data. 1: Remove. 0: Reserve. |
| video | No | Object | Configuration information of a video stream. When isFiltrateVideo is 1, this field is ignored. |
| video.codec | No | Integer | Encoding format of the video stream. The available values are libx264 (H264 encoding) and libx265 (H265 encoding). A resolution smaller than 640*480 must be specified for H265 encoding. |
| video.fps | No | Float | Frame rate (in Hz). Values: 24, 25, 30, etc. |
| video.width | No | Integer | The maximum video stream width (in px). If it is 0, and the video height value is not 0, the video stream is scaled proportionally. If both the values of the video width and height are 0, the video stream is same with the source file. The minimum value is 128, and the maximum value is 1,920. |
| video.height | No | Integer | The maximum video stream height (in px). If it is 0, and the video width value is not 0, the video stream is scaled proportionally. If both the values of the video width and height are 0, the video stream is same with the source file. The minimum value is 128, and the maximum value is 1,920. |
| video.bitrate | No | Integer | Video stream bitrate (in Kbps) |
| video.minGop | No | Integer | Minimum interval of video key frames, whose range is from 1 to 10. |
| video.maxGop | No | Integer | Maximum interval of video key frames, whose range is from 1 to 10. |
| video.videoProfile | No | String | Video encoding grade. H.264 encoding can choose one of the above three grades, and the default is High. H.265 encoding grade can only be Main by default. |
| video.colorSpace | No | String | Video color space. H.264 supports only yuv420p, and H.265 supports yuv420p or yuv420p10le. |
| video.deinterlaced | No | Integer | Video deinterlacing mode. 1: deinterlaced. 0: interlaced. |
| video.videoRateControl | No | Integer | Video encoding mode. 0: one pass. 1: two pass. |
| audio | No | Object | Configuration information of an audio stream. When isFiltrateAudio is 1, this field is ignored. |
| audio.codec | No | String | Encoding format of an audio stream. The available values are libfdk_aac and libmp3lame. |
| audio.bitrate | No | Integer | Audio stream bitrate (in Kbps), whose range is from 26 to 256. |
| audio.soundSystem | No | String | Audio channel mode. 1: Single channel. 2: Dual channel. The default is 2. |
| audio.sampleRate | No | Integer | Sampling rate of an audio stream (in Hz) |
| COMMON_PARAMS | Yes |  | For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976). |

> Notes:
> - For more information on descriptions and values of fields relating to video and audio, please see [Transcoding Capability Overview](https://cloud.tencent.com/document/product/266/11701#.E8.BD.AC.E7.A0.81.E8.83.BD.E5.8A.9B.E7.BB.BC.E8.BF.B0).
> - If resolution adaptation is enabled, the value of the longer side (width) must not be smaller than that of the shorter side (height).
> - You can enter negative numbers in video.fps, video.bitrate, video.width, video.height, audio.bitrate and audio.sampleRate to prohibit converting from a low value to a high value. For example, if the video.bitrate of a template is -512, the transcoded bitrate will not be greater than 512k. That is, if the original video bitrate is 256k, the transcoded one will still be 256k, and if the original one is 1024k, the transcoded one is 512k.

### Request Example
<pre>
https://vod.api.qcloud.com/v2/index.php?Action=UpdateTranscodeTemplate
&definition=1003
&container=mp4
&comment=comm_definition
&video.codec=libx264
&video.fps=45
&video.width=564
&video.height=123
&video.bitrate=256
&audio.codec=libfdk_aac
&audio.bitrate=512
&audio.soundSystem=dual-channel
&audio.sampleRate=200
&COMMON_PARAMS
</pre>

## API Response

### Parameter Description
| Parameter | Type | Description |
|---------|---------|---------|
| code | Integer | Error code. 0: Successful; other values: Failed. |
| message | String | Error message |

### Error Codes
| Error Code | Description |
|---------|---------|
| 4000-7000 | For more information, please see [Common Error Codes](https://cloud.tencent.com/document/product/266/7783)  |
| 1000 | Invalid parameter  |
| 10701 | Internal error  |
| 10702 | Internal error  |
| 10704 | The template does not exist |
| 10730 | The container parameter in the request is invalid |
| 10731 | The video.fps parameter in the request is invalid |
| 10732 | The video.codec parameter in the request is invalid |
| 10733 | The video.bitrate parameter in the request is invalid |
| 10734 | Resolution is invalid |
| 10735 | The definition parameter in the request is invalid |
| 10754 | The audio.codec parameter in the request is invalid |
| 10755 | The audio.sampleRate parameter in the request is invalid |
| 10756 | The audio.bitrate parameter in the request is invalid |
| 10757 | The audio.soundSystem parameter in the request is invalid |
| 10736 | The isFiltrateVideo parameter in the request is invalid |
| 10737 | The isFiltrateAudio parameter in the request is invalid |
| 10738 | The video.minGop parameter in the request is invalid |
| 10739 | The video.maxGop parameter in the request is invalid |
| 10740 | The video.profile parameter in the request is invalid |
| 10741 | The video.colorSpace parameter in the request is invalid |
| 10742 | The video.deinterlaced parameter in the request is invalid |
| 10743 | The video.videoRateControl parameter in the request is invalid |
| 10745 | The denoise parameter in the request is invalid |
| 10758 | The audio.audioResampler parameter in the request is invalid |
| 10759 | The audio.audioDownmixMode parameter in the request is invalid |

### Response Example

```javascript
{
    "code": 0,
    "message": ""
}
```

