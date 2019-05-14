## API Name
ConvertVodFile

## Feature Description
1. Transcode the video file according to the transcoding configuration in the console;
2. After the transcoding task is finished, if the APP is configured with server event notification, a transcoding completion event notification is generated.

**Note:**

The setup method of transcoding configuration in the console: Log in to Tencent Cloud VOD console -> Select "Global Configuration" in the left menu bar -> Select "Transcoding Settings" in the TAB page.

## Event Notification
Completion of file upload can trigger [Event Notification - Video Transcoding Completed](/document/product/266/7832). It can be used by the APP backend server to monitor the video transcoding action in the VOD system.

For details, refer to [Introduction to Server Event Notification](/document/product/266/7829).

## Request Method

### Request Domain
vod.api.qcloud.com

### Peak Calling Frequency
100 counts/min

##### Parameter Description

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| fileId | Yes | string | File |
| isScreenshot | No | Integer | Whether to take screenshot. 0: No, 1: Yes |
| isWatermark | No | Integer | Whether to add watermark. 0: No. 1: Yes |
| COMMON_PARAMS | Yes |  | Refer to [Common Parameters](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### Request Example

```
https://vod.api.qcloud.com/v2/index.php?Action=ConvertVodFile
&fileId=96000077184630899
&isScreenshot=1
&isWatermark=1
&COMMON_PARAMS
```

## API Response

##### Parameter Description
| Name | Type | Description |
|---------|---------|---------|
| code | Integer | Error code, 0:  Succeeded; other values:  Failed |
| message | String | Error message |

### Error Code Description
| Error Code | Description |
|---------|---------|
| 4000-7000 | Refer to [Common Error Codes](/document/product/266/7783)  |
| 1 | Internal error |
| 1000 | Invalid parameter |
| 1108 | Internal error |
| 1152 | Internal error |
| 1801 | Internal error |
| 1802 | Internal error |
| 2000 | Internal error |
| 2001 | Internal error |
| 10009 | Unexpected file status |
| 10010 | Internal error |
| 10012 | Internal error |

### Response Example
```javascript
{
    "code": 0,
    "message": ""
}
```
