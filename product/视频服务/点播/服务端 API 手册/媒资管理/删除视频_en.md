## API Name
DeleteVodFile

## Feature Description
1. This API is used to delete video files.
2. After a video is deleted, all its dependent objects (transcoding result, image sprite, etc.) will also be deleted.
3. CDN cache needs to be refreshed each time when the files are deleted. Specify 1 for isFlushCdn, and the upper limit is 10,000 times per day by default.

## Event Notification

When files have been deleted, Event Notification-Notification on File Deletion is triggered, based on which the App backend monitors the execution status of task flow.

For more information, please see Server Event Notifications.

## Request Method

### Request Domain
vod.api.qcloud.com

### Max Calling Frequency
100/min

### Parameters
| Name | Required | Type | Description |
|---------|---------|---------|---------|
| fileId | Yes | string | File ID |
| isFlushCdn | No | int | Whether to refresh CDN cache each time when files are deleted. It is not refreshed by default. When the value is 1, it is refreshed. |
| priority | Yes | Integer | Priority. You can enter 0. (0: Medium; 1: High; 2: Low.) |
| COMMON_PARAMS | Yes |  | For more information, please see [Common Request Parameters](/document/api/213/6976) |

### Request Example
```
https://vod.api.qcloud.com/v2/index.php?Action=DeleteVodFile
&fileId=16092504232103571364
&priority=0
&COMMON_PARAMS
```
## API Response

### Parameters
| Name | Type | Description |
|---------|---------|---------|
| code | Integer | Error code. 0: Successful; other values: Failed. |
| message | String | Error message |

### Error Codes
| Error Code | Description |
|---------|---------|
| 4000-7000 | For more information, please see [Common Error Codes](/document/product/266/7783)  |
| 1000 | Invalid parameter  |
| 1001 | Internal error  |
| 1050 | Internal error  |
| 1102 | Internal error  |
| 1702 | Internal error  |
| 10009 | File status exception |

### Response Example

```javascript
{
    "code": 0,
    "message": ""
}
```

