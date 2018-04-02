<!-- TODO:
API functions that need to be perfected:
When the API is called, you can query the status of the pull operation with the API that is used to query task status (TODO);
If server callback is configured, the VOD backend will initiate URL pulling completion callback when the pull operation is finished (TODO).
Skip or reset a pulling task that already exists?
Callback URLs and callback methods are read from configurations and cannot be specified -->

## API Name
MultiPullVodFile

## Feature Description
1. Pull a batch of video files to Tencent Cloud from existing resource library, according to URLs passed by the user;
2. Batch pull multiple video files. The order of each video is determined based on the value of "n" from the input parameter.

> Note:
> Make sure that the URL is the video file, but not the web page address that contains the video file.

## Event Notification
Completion of file upload operation will trigger [Event Notification - URL Pulling Completed](/document/product/266/7831). The app backend can use this to monitor URL pulling actions performed in the VOD system.

For more information, please see [Server Event Notification Introduction](/document/product/266/7829).

## Request Method

### Request Domain
vod.api.qcloud.com

### Max Calling Frequency
100/min

### Parameter Description
| Parameter | Required | Type | Description |
|---------|---------|---------|---------|
| pullset.n.url | Yes | String | URL of the nth video to be pulled. n starts from 0 and increases progressively. The same below. |
| pullset.n.fileName | Yes | String | Name of a video file |
| pullset.n.fileMd5 | No | string | MD5 of a video file |
| pullset.n.isTranscode | No | Integer | Whether to transcode. 0: No (default), 1: Yes. If the video is not transcoded here, you can transcode it from Video File Management in the management console after the video is uploaded |
| pullset.n.isScreenshot | No | Integer | Whether to take screenshot. 0: No (default), 1: Yes |
| pullset.n.isWatermark | No | Integer | Whether to add watermark. 0: No (default), 1: Yes. Be sure to select a watermark file and locate the watermark position in the management console before watermarking. Otherwise, the upload process may fail; |
| pullset.n.classId | No | Integer | Video category ID|
| pullset.n.tags | No | String | Tag of a video. Multiple tags are separated by commas |
| pullset.n.priority | No | Integer | Priority. 0: Medium. 1: High. 2: Low |
| COMMON_PARAMS | Yes |  | For more information, please see [Common Request Parameters](/document/api/213/6976) |

### Request example

```
https://vod.api.qcloud.com/v2/index.php?Action=MultiPullVodFile
&pullset.0.url=http%3A%2F%2Fv.qq.com%2Fcover%2Ft%2Ftofg0ynqvcjac58.html%3Fvid%3Dc0152uievii
&pullset.0.fileName=test
&pullset.0.isTranscode=1
&pullset.0.priority=1
&pullset.0.isScreenshot=1
&pullset.0.isWatermark=1
&pullset.0.classId=0
&COMMON_PARAMS
```

## API Response

### Parameter Description
| Parameter | Type | Description |
|---------|---------|---------|
| code | Integer | Error code |
| message | String | Error message description  |

### Error Codes
| Error Code | Description |
|---------|---------|
| 4000-7000 | For more information, please see [Common Error Codes](/document/product/266/7783)  |
| 1 | Internal error  |
| 1000 | Invalid parameter  |
| 1001 | User information error |
| 1010 | Internal error |
| 1011 | Internal error |
| 1018 | Too many tasks to be pulled. Try again later |
| 1100 | Internal error |
| 1159 | Internal error |
| 1163 | No available watermark. But it was specified in the request to set watermark |
| 10003 | Internal error |

### Response Example
```javascript
{
    "code": 0,
    "message": ""
}
```

