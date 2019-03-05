## API Name
CreateClass

## Feature Description
1. Used to create categories to manage video files;
2. This operation is considered global, category association of specific files is not involved. To modify the file category, please use [Modify Video Attributes](/document/product/266/7828) API.

## Request Method

### Domain for API Request
vod.api.qcloud.com

### Peak Calling Frequency
100 counts/min

##### Parameter Description
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| className | Yes | String | Category information |
| parentId | No | Integer | ID number of the parent category. A level-1 category will be created if this is left empty |
| COMMON_PARAMS | Yes |  | Refer to [Common Parameters](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### Request Example
```
https://vod.api.qcloud.com/v2/index.php?Action=CreateClass
&className=test
&parentId=-1
&COMMON_PARAMS
```
## API Response

##### Parameter Description
| Name | Type | Description |
|---------|---------|---------|
| code | Integer | Error code, 0:  Succeeded, other values:  Failed |
| newClassId | String | ID of the created category. ID for the top category is -1 |
| message | String | Error message |

### Error Code Description
| Error Code | Description |
|---------|---------|
| 4000-7000 | Refer to [Common Error Codes](/document/product/266/7783)  |
| 1000 | Invalid parameter  |
| 1903 | A directory can not be created under default category |

### Response Example
```javascript
{
    "code": 0,
    "message": "",
    "newClassId": "250"
}
```

