## API Name
AddKeyFrameDesc

## Feature Description
This API (AddKeyFrameDesc) is used to add video keyframe description. A maximum of 100 keyframe descriptions can be added for each video file.

## Request Method

### Request Domain Name
vod.api.qcloud.com

### Max Calling Frequency
100/min

### Parameter Description
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| fileId | Yes | String | Video ID |
| keyFrameDesc.n.timeOffset | Yes | Integer | The time offset of a video keyframe description in milliseconds. If a video keyframe description already exists at this time offset, it will be overwritten. n starts from 0 and increases progressively. n only indicates the sequence number of keyframe description in this request, but not the number of existing keyframe descriptions in the video. |
| keyFrameDesc.n.content | Yes | String | The text information (not URL Encoded) carried in this keyframe description, which must be less than 1,024 bytes. |
| COMMON_PARAMS | Yes |  | For more information, please see [Common Request Parameters](/document/api/213/6976). |

### Request Example
```
https://vod.api.qcloud.com/v2/index.php?Action=AddKeyFrameDesc
&fileId=2721945854681023354
&keyFrameDesc.0.timeOffset=1000
&keyFrameDesc.0.content=content1
&keyFrameDesc.1.timeOffset=42000
&keyFrameDesc.1.content=content2
&COMMON_PARAMS
```
## API Response

### Parameter Description
| Name | Type | Description |
|---------|---------|---------|
| code | Integer | Error code, 0: Successful; other values: Failed |
| message | String | Error message |

### Error Code Description
| Error Code | Description |
|---------|---------|
| 4000-7000 | For more information, please see [Common Error Codes](/document/product/266/7783). |
| 1 | Internal error |
| 1000 | Invalid parameter |
| 1013 | Internal error |
| 10008 | The file does not exist |

### Response Example

```javascript
{
    "code": 0,
    "message": ""
}
```

