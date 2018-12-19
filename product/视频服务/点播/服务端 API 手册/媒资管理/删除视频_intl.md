## API Name
DeleteVodFile

## Feature Description
1. This API is used to delete video files;
2. After a video is deleted, all its dependent objects (transcoding result, image sprite, etc.) will also be deleted.

## Request Method

### Request Domain
vod.api.qcloud.com

### Peak Calling Frequency
100 counts/min

##### Parameter Description
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| fileId | Yes | string | File ID |
| priority | Yes | Integer | You may enter 0. Priority 0: Medium. 1: High. 2: Low |
| COMMON_PARAMS | Yes |  | Refer to [Common Parameters](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### Request Example
```
https://vod.api.qcloud.com/v2/index.php?Action=DeleteVodFile
&fileId=16092504232103571364
&priority=0
&COMMON_PARAMS
```
## API Response

##### Parameter Description
| Name | Type | Description |
|---------|---------|---------|
| code | Integer | Error code, 0:  Succeeded, other values:  Failed |
| message | String | Error message |

### Error Code Description
| Error Code | Description |
|---------|---------|
| 4000-7000 | Refer to [Common Error Codes](/document/product/266/7783)  |
| 1000 | Invalid parameter  |
| 1001 | Internal error  |
| 1050 | Internal error  |
| 1102 | Internal error  |
| 1702 | Internal error  |
| 10009 | Unexpected file status  |

### Response Example

```javascript
{
    "code": 0,
    "message": ""
}
```

