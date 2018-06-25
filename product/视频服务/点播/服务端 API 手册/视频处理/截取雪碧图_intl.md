## API Name
CreateImageSprite

## Feature Description
1. This API is used to capture the screenshots of a video file and generate image sprites. For specifications of image sprite, refer to [Image Sprite Screenshot Specifications](/document/product/266/8099);
1. After the image sprites are captured, if the APP is configured with server event notification, an event notification of completion of capturing the image sprites is generated.

## Event Notification
Completion of capturing the image sprites can trigger [Event Notification - Image Sprite Capture Completed](/document/product/266/8104). It can be used by the APP backend server to monitor the video image sprite capturing action in the VOD system.

For details, refer to [Introduction to Server Event Notification](/document/product/266/7829).

## Request Method

### Request Domain
vod.api.qcloud.com

### Peak Calling Frequency
100 counts/min

##### Parameter Description

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| fileId | Yes | String | File ID |
| definition | Yes | Integer | Specifications of image sprite screenshot, refer to [Image Sprite Screenshot Specifications](/document/product/266/8099) |
| COMMON_PARAMS | Yes |  | Refer to [Common Parameters](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### Request Example

```
https://vod.api.qcloud.com/v2/index.php?Action=CreateImageSprite
&fileId=96000077184630899
&definition=10
&COMMON_PARAMS
```

## API Response

##### Parameter Description
| Name | Type | Description |
|---------|---------|---------|
| code | Integer | Error code, 0:  Succeeded; other values:  Failed |
| message | String | Error message |
| vodTaskId | String | Task id, which can be used to query the task status |

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
    "message": "",
    "vodTaskId": ""
}
```

