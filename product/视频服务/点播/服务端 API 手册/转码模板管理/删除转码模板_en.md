## API Name
DeleteTranscodeTemplate

## Feature Description
This API is used to delete a transcoding template.

## Request Method

### Request Domain
vod.api.qcloud.com

### Max Calling Frequency
100/min

### Parameter Description
| Parameter | Required | Type | Description |
|---------|---------|---------|---------|
| definition | Yes | Integer | Transcoding template ID |
| COMMON_PARAMS | Yes |  | For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976) |

### Request Example
<pre>
https://vod.api.qcloud.com/v2/index.php?Action=DeleteTranscodeTemplate
&definition=40
&COMMON_PARAMS
</pre>

## API Response

### Parameter Description
| Parameter | Type | Description |
|---------|---------|---------|
| code | Integer | Error code. 0: Successful; other values: Failed. |
| message | String | Error message |

### Error Codes
| Error Code | Description |
|---------|---------|
| 4000-7000 | For more information, please see [Common Error Codes](https://cloud.tencent.com/document/product/266/7783)  |
| 1000 | Invalid parameter  |
| 1001 | Internal error  |
| 1050 | Internal error  |
| 1102 | Internal error  |
| 1702 | Internal error  |

### Response Example

```javascript
{
    "code": 0,
    "message": ""
}
```
