## API Name
QueryTranscodeTemplate

## Feature Description
This API is used to query the details of a transcoding template.

## Request Method

### Request Domain
vod.api.qcloud.com

### Max Calling Frequency
100/min

### Parameter Description
| Parameter | Required | Type | Description |
|---------|---------|---------|---------|
| definition | Yes | Integer | Transcoding template ID |
| COMMON_PARAMS | Yes |  | For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976) |

### Request Example
<pre>
https://vod.api.qcloud.com/v2/index.php?Action=QueryTranscodeTemplate
&definition=1003
&COMMON_PARAMS
</pre>

## API Response

### Parameter Description
| Parameter | Type | Description |
|---------|---------|---------|
| code | Integer | Error code, 0: successful; other values: failed. |
| message | String | Error message |
| name | String | Name of the transcoding template |
| container | String | Container type, such as m4a, mp4 |
| comment | String | Description of the transcoding template |
| createTime | Integer | Template creation time (Unix timestamp) |
| updateTime | Integer | The latest update time of the template (Unix timestamp) |
| isFiltrateVideo | Integer | Remove video data. 1: remove. 0: reserve. The default is 0. |
| isFiltrateAudio | Integer | Remove audio data. 1: remove. 0: reserve. The default is 0. |
| video | Object | Configuration information of a video stream. When isFiltrateVideo is 1, this field is ignored. |
| video.codec | Integer | Encoding format of a video stream. The available values are libx264 (H264 encoding) and libx265 (H265 encoding). |
| video.fps | Float | Frame rate (in Hz) |
| video.resolutionSelfAdapting | Integer | Whether to enable resolution adaption. 1: Enable. 0: Disable. If 1 is selected, the value of width is used for the longer side, and the value of height is for the shorter side. The default is 1. |
| video.width | Integer | The maximum video stream width (in px). If it is 0, and the video.height is not 0, the video stream is scaled proportionally. If both video.width and video.height are 0, the video stream is same with the source file. |
| video.height | Integer | The maximum video stream height (in px). If it is 0, and the video.width is not 0, the video stream is scaled proportionally. If both video.width and video.height are 0, the video stream is same with the source file. |
| video.bitrate | Integer | Video stream bitrate (in Kbps) |
| video.minGop | Integer | Minimum interval of video key frames, whose range is from 1 to 10. |
| video.maxGop | Integer | Maximum interval of video key frames, whose range is from 1 to 10. |
| video.videoProfile | String | Video encoding grade: baseline, main, high |
| video.colorSpace | String | Video color space: yuv420p, yuv420p10le |
| video.deinterlaced | Integer | Video deinterlacing mode. 1: deinterlaced. 0: interlaced. |
| video.videoRateControl | Integer | Video encoding mode. 0: one pass. 1: two pass. |
| denoise | Object | Video denoising parameter |
| denoise.enable | Integer | Whether to enable video denoising. 1: Enable. 0: Disable. |
| audio | Object | Configuration information of an audio stream. When isFiltrateAudio is 1, this field is ignored. |
| audio.codec | String | Encoding format of an audio stream. The available values are libfdk_aac (for mp4 and hls) and libmp3lame (for flv). |
| audio.bitrate | Integer | Audio stream bitrate (in Kbps) |
| audio.soundSystem | String | Audio channel mode. |
| audio.sampleRate | Integer | Sampling rate of an audio stream (in Hz) |
| audio.audioResampler | string | Audio resampling parameter. If the number of audio channels is greater than 2, two channels are used for resampling. Only soxr is supported now. |
| audio.audioDownmixMode | Integer | If the value is 1 and the number of channels is greater than 4, besides resampling, you can further perform gain compensation for the central channel. |

> Note:
> - For more information on descriptions and values of fields relating to video and audio, please see [Transcoding Capability Overview](https://cloud.tencent.com/document/product/266/11701#.E8.BD.AC.E7.A0.81.E8.83.BD.E5.8A.9B.E7.BB.BC.E8.BF.B0).

### Error Codes
| Error Code | Description |
|---------|---------|
| 4000-7000 | For more information, please see [Common Error Codes](https://cloud.tencent.com/document/product/266/7783)  |
| 1000 | Invalid parameter  |
| 10702 | Internal error  |
| 10704 | The template does not exist |

### Response Example

```javascript
{
    "code": 0,
    "message": "",
    "name": "highDefinition",
    "container": "mp4",
    "comment": "commonDefinition",
    "isFiltrateVideo": 0,
    "isFiltrateAudio": 0,
    "createTime": 1485156352,
    "updateTime": 1485156352,
    "video": {
        "codec": "libx264",
        "fps": 40,
        "resolutionSelfAdapting": 1,
        "width": 123,
        "height": 554,
        "bitrate": 256000
    },
    "audio": {
        "codec": "libfdk_aac",
        "bitrate": 512000,
        "soundSystem": 2,
        "sampleRate": 200
    }
}
```

