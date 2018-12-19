## API Name
DeleteWatermarkTemplate

## Feature Description
1. This API is used to remove watermark screenshot templates.

## Request Method

### Request Domain
vod.api.qcloud.com

### Max Calling Frequency
100/min

### Parameter Description
| Parameter| Required | Type | Description |
|---------|---------|---------|---------|
| definition | Yes | Integer | Watermark template ID |
| COMMON_PARAMS | Yes |  | For more information, please see [Common Request Parameters](/document/api/213/6976) |

## Request Example
<pre>
https://vod.api.qcloud.com/v2/index.php?Action=DeleteWatermarkTemplate
&definition=10010
&COMMON_PARAMS
</pre>

## API Response

### Parameter Description
| Parameter | Type | Description |
|---------|---------|---------|
| code | Integer | Error code, 0: successful; other values: failed. |
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

### Response Example

```javascript
{
    "code": 0,
    "message": ""
}
```
