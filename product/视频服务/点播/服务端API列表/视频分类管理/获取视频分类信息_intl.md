## API Name
DescribeClass
	
## Feature Description
1. Used to acquire global category list, as well as detailed information of each category;
2. To obtain the hierarchy between categories, please use [Obtain Video Category Hierarchy](/document/product/266/7813) API.

## Request Method

### Domain for API Request
vod.api.qcloud.com

### Peak Calling Frequency
100 counts/min

##### Parameter Description
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| COMMON_PARAMS | Yes |  | Refer to [Common Parameters](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### Request Example
```
https://vod.api.qcloud.com/v2/index.php?Action=DescribeClass
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
| 1000 | Invalid parameter  |
| 1023 | Internal error  |

### Response Example
```javascript
{
    "code": 0,
    "message": "",
    "data": [
        {
            "id": "0",
            "name": "Others",
            "create_time": "2014-11-27 10:22:37",
            "update_time": "2014-11-27 17:52:13"
        },
        {
            "id": "98",
            "name": "Movie",
            "create_time": "2015-04-08 09:52:20",
            "update_time": "2015-04-08 09:52:20"
        }
    ]
}
```

