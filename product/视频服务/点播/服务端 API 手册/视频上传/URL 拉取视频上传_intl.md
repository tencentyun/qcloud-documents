<!-- TODO:
API functions that need to be perfected:
When the API is called, you can query the status of the pull operation with the API that is used to query task status (TODO);
If server callback is configured, the VOD backend will initiate URL pulling completion callback when the pull operation is finished (TODO).
Skip or reset a pulling task that already exists?
Callback URLs and callback methods are read from configurations and cannot be specified-->

## API Name
MultiPullVodFile

## Feature Description
1. Pull a batch of video files to Tencent Cloud from existing resource library, accordibang to URLs passed by the user;
2. This API is able to batch pull multiple video files. The order of each video is determined based on the value of "n" from the input parameter.

> Note:
> Please ensure that the URL is the video file, but not the web page address that contains the video file.

## Event Notification
Completion of file upload operation will trigger [Event Notification - URL Pulling Completed](/document/product/266/7831). The APP backend can use this to monitor URL pulling actions performed in the VOD system.

For details, refer to [Introduction to Server Event Notification](/document/product/266/7829).

## Request Method

### Request Domain
vod.api.qcloud.com

### Peak Calling Frequency
100 counts/min

##### Parameter Description
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| pullset.n.url | Yes | String | URLs of the videos to be pulled. "n" is an integer,"1" for the first video,"2" for the second video and so on |
| pullset.n.fileName | Yes | String | Name of video file |
| pullset.n.fileMd5 | No | string | MD5 of video file |
| pullset.n.isTranscode | No | Integer | Whether to perform transcode. 0: No (default), 1: Yes. If the video is not transcoded, you can do it from Video File Management in the Management Console after the video has been uploaded |
| pullset.n.isScreenshot | No | Integer | Whether to take screenshot. 0: No (default), 1: Yes |
| pullset.n.isWatermark | No | Integer | Whether to add watermark. 0: No (default), 1: Yes. Be sure to select watermark file and determine watermark location in advance if you choose to add watermark. Otherwise the upload process may fail; |
| pullset.n.classId | No | Integer | ID of the video category |
| pullset.n.tags | No | String | Tag of the video. Multiple tags are separated by commas |
| pullset.n.priority | No | Integer | Priority. 0: Medium. 1: High. 2: Low |
| COMMON_PARAMS | Yes |  | Refer to [Common Parameters](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### Request Example

```
https://vod.api.qcloud.com/v2/index.php?Action=MultiPullVodFile
&pullset.1.url=http%3A%2F%2Fv.qq.com%2Fcover%2Ft%2Ftofg0ynqvcjac58.html%3Fvid%3Dc0152uievii
&pullset.1.fileName=test
&pullset.1.isTranscode=1
&pullset.1.priority=1
&pullset.1.isScreenshot=1
&pullset.1.isWatermark=1
&pullset.1.classId=0
&COMMON_PARAMS
```

## API Response

##### Parameter Description
| Name | Type | Description |
|---------|---------|---------|
| code | Integer | Error code |
| message | String | Error message description  |

### Error Code Description
| Error Code | Description |
|---------|---------|
| 4000-7000 | Refer to [Common Error Codes](/document/product/266/7783)  |
| 1 | Internal error  |
| 1000 | Invalid parameter  |
| 1001 | User information error |
| 1010 | Internal error  |
| 1011 | Internal error  |
| 1018 | Too many tasks to be pulled. Please try again later |
| 1100 | Internal error |
| 1159 | Internal error |
| 1163 | No available watermark, but it was specified in the request to set watermark |
| 10003 | Internal error |

### Response Example
```javascript
{
    "code": 0,
    "message": ""
}
```

