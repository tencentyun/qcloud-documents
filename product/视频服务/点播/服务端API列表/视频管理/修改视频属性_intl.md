## API Name
ModifyVodInfo

## Feature Description
1. This API is used to modify the description information of video files, including category, name, and description.
2. This API is used t modify the expiration time of the video file (supported only in VOD).  

## Request Method

### Request Domain
vod.api.qcloud.com

### Peak Calling Frequency
100 counts/min

##### Parameter Description
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| fileId | Yes | String | File ID |
| fileName | No | String | File name |
| fileIntro | No | String | File description |
| classId | No | Integer | Category ID |
| expireTime| No | String | Video expiration time, format:  Y-m-d H:i:s, e.g. 2017-10-01 00:00:00. After a video expires, the video and all its dependent objects (transcoding result, image sprite, etc.) will be deleted |
| COMMON_PARAMS | Yes |  | Refer to [Common Parameters](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### Request Example
```
https://vod.api.qcloud.com/v2/index.php?Action=ModifyVodInfo
&fileId=16092504232103571137
&fileName=newName
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
| 1 | Internal error  |
| 1000 | Invalid parameter  |
| 1016 | Internal error  |
| 10008 | The file does not exist  |

### Response Example
```javascript
{
    "code": 0,
    "message": ""
}
```

