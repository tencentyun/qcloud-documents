## API Name
DescribeAllClass

## Feature Description
1. Used to acquire all category class relationships of the current user

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
https://vod.api.qcloud.com/v2/index.php?Action=DescribeAllClass
&COMMON_PARAMS
```
## API Response

##### Parameter Description
| Name | Type | Description |
|---------|---------|---------|
| code | Integer | Error code, 0:  Succeeded, other values:  Failed |
| message | String | Error message |
| data | Array | List of category class relationships of the current user |
| data.info | Array | Information of the first level category |
| data.subclass | Array | Information of sub-categories under the first level category |

### Error Code Description
| Error Code | Description |
|---------|---------|
| 4000-7000 | Refer to [Common Error Codes](/document/product/266/7783)  |
| 1000 | Invalid parameter  |
| 1905 | Users have no category |
| 1907 | Internal error |
| 2000 | Internal error  |

### Response Example
```javascript
{
    "code": 0,
    "message": "",
    "data": [
        {
            "info": {
                "id": 149,
                "parent_id": -1,
                "name": "Test",
                "level": 0,
                "file_num": 0
            },
            "subclass": [
                {
                    "info": {
                        "id": 213,
                        "parent_id": 149,
                        "name": "New second level category",
                        "level": 1,
                        "file_num": 0
                    },
                    "subclass": []
                },
                {
                    "info": {
                        "id": 215,
                        "parent_id": 149,
                        "name": "New second level category (1)",
                        "level": 1,
                        "file_num": 0
                    },
                    "subclass": []
                }
            ]
        }
    ]
}
```

