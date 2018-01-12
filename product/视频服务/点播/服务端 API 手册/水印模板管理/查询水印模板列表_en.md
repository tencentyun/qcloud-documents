## API Name
QueryWatermarkTemplateList

## Feature Description
1. This API is used to query the watermark template list.

## Request Method

### Request Domain
vod.api.qcloud.com

### Max Calling Frequency
100/min

### Parameter Description
| Parameter| Required | Type | Description |
|---------|---------|---------|---------|
| COMMON_PARAMS | Yes |  | For more information, please see [Common Request Parameters](/document/api/213/6976) |

## Request Example
<pre>
https://vod.api.qcloud.com/v2/index.php?Action=QueryWatermarkTemplateList
&COMMON_PARAMS
</pre>
## API Response

### Parameter Description
| Parameter | Type | Description |
|---------|---------|---------|
| code | Integer | Error code, 0: successful; other values: failed. |
| definitionList | Array | List of watermark template information |
| definitionList.definition | Integer | Watermark template ID |
| definitionList.name | String | Watermark template name |
| definitionList.comment | String | Description of the watermark template |
| definitionList.createTime | Integer | Template creation time (Unix timestamp) |
| definitionList.updateTime | Integer | Template update time (Unix timestamp) |

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
    "message": "",
    "definitionList": [
        {
            "definition": 10010,
            "name": "normal",
            "comment": "test",
            "createTime": 1485156352,
            "updateTime": 1485156352
        },
        {
            "definition": 10011,
            "name": "special",
            "comment": "test",
            "createTime": 1485156362,
            "updateTime": 1485156362
        }
    ]
}
```
