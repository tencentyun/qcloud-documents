## API Name
DeleteVodTags

## Feature Description
1. This API is used to delete video tags;
2. This API can be used to delete multiple tags of a single video at one time.

## Request Method

### Request Domain
vod.api.qcloud.com

### Peak Calling Frequency
100 counts/min

##### Parameter Description
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| fileId | Yes | String | Video ID |
| tags.n | Yes | String | Tag list (English letters and numbers). Each tag is limited to 8 characters |
| COMMON_PARAMS | Yes |  | Refer to [Common Parameters](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### Request Example
```
https://vod.api.qcloud.com/v2/index.php?Action=DeleteVodTags
&fileId=2721945854681023354
&tags.1=testTag1
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
| 1 | Internal error |
| 1000 | Invalid parameter  |
| 10008 | The file does not exist  |

### Response Example
```javascript
{
    "code": 0,
    "message": ""
}
```

