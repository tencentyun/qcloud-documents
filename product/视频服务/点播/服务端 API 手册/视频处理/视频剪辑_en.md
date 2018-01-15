## API Name
ClipVideo

## Feature Description
1. Clip the source video file based on the specified time offset to generate a new video file (target file) with a new file ID;
2. The clipped file (in mp4) has very similar resolution and bitrate with the source file.

## Event Notification
Clipping completion event.

## Request Method
### Request Domain
vod.api.qcloud.com

### Max Calling Frequency
100/min

### Parameter Description
| Parameter | Required | Type | Description |
|---------------|----------|---------|---------|
| fileId | Yes | String | The unique ID of the source file |
| newFileName | Yes | String | Target file name |
| startTimeOffset | No | Integer | The time offset that specifies when to start clipping the source file, in seconds. The value greater than or equal to 0 means to calculate from the beginning, and that less than 0 means from the end. The default is 0 if it is left empty. |
| endTimeOffset | No | Integer | The time offset that specifies when to end clipping the source file, in seconds. The value greater than or equal to 0 means to calculate from the beginning, and that less than 0 means from the end. If this parameter is left empty, it means to stop clipping at the end of the source file. |
| COMMON_PARAMS | Yes |  | For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976) |

### Request Example 1: Clipping range
The expected target file starts from the 2nd second of the source file, and ends at the 10th second. The request example is as follows:
```
https://vod.api.qcloud.com/v2/index.php?Action=ClipVideo
&fileId=16092504232103571364
&newFileName=cutFileName
&startTimeOffset=2
&endTimeOffset=10
&COMMON_PARAMS
```

### Request Example 2: Clip off both ends
The expected target file starts from the 2nd second of the source file and ends at 5 seconds before the source file ends.
```
https://vod.api.qcloud.com/v2/index.php?Action=ClipVideo
&fileId=16092504232103571364
&newFileName=cutFileName
&startTimeOffset=2
&endTimeOffset=-5
&COMMON_PARAMS
```

### Request Example 3: Clip from the beginning
The expected target file starts from the beginning of the source file and ends at 10 seconds before the source file ends. The request example is as follows:
```
https://vod.api.qcloud.com/v2/index.php?Action=ClipVideo
&fileId=16092504232103571364
&newFileName=cutFileName
&startTimeOffset=0
&endTimeOffset=-10
&COMMON_PARAMS
```

### Request Example 4: Clip till the end
The expected target file starts from the 2nd second and ends at the end of the source file.
```
https://vod.api.qcloud.com/v2/index.php?Action=ClipVideo
&fileId=16092504232103571364
&newFileName=cutFileName
&startTimeOffset=2
&COMMON_PARAMS
```

## API Response

### Parameter Description
| Parameter | Type | Description |
|---------|---------|---------|
| code | Integer | Error code, 0: Successful; other values: Failed. |
| message | String | Error message |
| vodTaskId | String | Clipping task Id |

### Error Codes
| Error Code | Description |
|---------|---------|
| 4000-7000 | For more information, please see [Common Error Codes](https://cloud.tencent.com/document/product/266/7783)  |
| 1000 | Invalid parameter  |
| 1001 | User information error  |
| 10009 | File status exception |

### Response Example

```javascript
{
    "code": 0,
    "message": "",
    "vodTaskId": "clipVideo-0a78cf44c4285026a4c"
}
```

