## API Name
ModifyClass

## Feature Description
1. Modify the attributes of the video category, including the name.

## Request Method

### Domain for API Request
vod.api.qcloud.com

### Peak Calling Frequency
100 counts/min

##### Parameter Description
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| classId | Yes | Integer | ID of the category to be modified |
| className | Yes | String | New category name |
| COMMON_PARAMS | Yes |  | Refer to [Common Parameters](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### Request Example
```
https://vod.api.qcloud.com/v2/index.php?Action=ModifyClass
&classId=100
&className=test
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
| 1021 | Internal error |
| 1905 | Category does not exist |
| 1907 | Internal error |

### Response Example
```javascript
{
    "code": 0,
    "message": ""
}
```

