## API Name
UnbanningVod

## Feature Description
Resume the Video Play, and make the video playback address valid.

## Request Method

### Request Domain
vod.api.qcloud.com

### Peak Calling Frequency
100 counts/min

##### Parameter Description
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| fileId | Yes | String | File ID |
| COMMON_PARAMS | Yes |  | Refer to [Common Parameters](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### Request Example
<pre>
https://vod.api.qcloud.com/v2/index.php?Action=BanningVod
&fileId=12345
&COMMON_PARAMS
</pre>

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
