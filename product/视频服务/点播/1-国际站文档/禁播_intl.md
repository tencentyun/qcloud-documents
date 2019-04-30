## API Name
BanningVod

## Feature Description
Disabled the Video, and make the video playback address invalid.

## Request Method

### Request Domain
vod.api.qcloud.com

### Peak Calling Frequency
100 counts/min

##### Parameter Description
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| fileId | Yes | String | File ID |
| refreshCdn | No | Int | whether to refresh Cdn, 0: not refresh, 1: refresh, default 0 |
| COMMON_PARAMS | Yes |  | Refer to [Common Parameters](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### Request Example
<pre>
https://vod.api.qcloud.com/v2/index.php?Action=BanningVod
&fileId=12345
&refreshCdn=1
&COMMON_PARAMS
</pre>

## API Response

##### Parameter Description
| Name | Type | Description |
|---------|---------|---------|
| code | Integer | Error code, 0:  Succeeded, other values:  Failed |
| message | String | Error message |
| replayUrl | String | Look back at the video playback address. After the original video playback address expires, you can use this address to play the forbidden video. |


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
    "message": "",
    "replayUrl": "http://251000333.vod2.myqcloud.com/xxxxxx/xxxxxx/f0.mp4"
}
```
