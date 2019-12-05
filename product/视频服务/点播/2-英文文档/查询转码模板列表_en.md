## API Name
QueryTranscodeTemplateList

## Feature Description
This API is used to query a transcoding template list.

## Request Method

### Request Domain
vod.api.qcloud.com

### Max Calling Frequency
100/min

### Parameter Description
| Parameter | Required | Type | Description |
|---------|---------|---------|---------|
| COMMON_PARAMS | Yes |  | For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976) |

### Request Example
<pre>
https://vod.api.qcloud.com/v2/index.php?Action=QueryTranscodeTemplateList
&COMMON_PARAMS
</pre>

## API Response

### Parameter Description
| Parameter | Type | Description |
|---------|---------|---------|
| code | Integer | Error code. 0: Successful; other values: Failed. |
| definitionList | Array | List of transcoding template information |
| definitionList.definition | Integer | Transcoding template ID |
| definitionList.name | String | Transcoding template name |
| definitionList.comment | String | Description of the transcoding template |
| definitionList.createTime | Integer | Template creation time (Unix timestamp) |
| definitionList.updateTime | Integer | The latest update time of the template (Unix timestamp) |

### Error Codes
| Error Code | Description |
|---------|---------|
| 4000-7000 | For more information, please see [Common Error Codes](https://cloud.tencent.com/document/product/266/7783)  |
| 1000 | Invalid parameter  |
| 10702 | Internal error  |

### Response Example

```javascript
{
    "code": 0,
    "message": "",
    "definitionList": [
        {
            "definition": 1004,
            "name": "highDefinition",
            "comment": "commonDefinition",
            "createTime": 1485156352,
            "updateTime": 1485156352
        },
        {
            "definition": 1005,
            "name": "highDefinition",
            "comment": "commonDefinition",
            "createTime": 1485156352,
            "updateTime": 1485156352
        }
    ]
}
```
