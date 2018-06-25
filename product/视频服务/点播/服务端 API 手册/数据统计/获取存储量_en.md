## API Name
DescribeVodStorage

## Feature Description
1. This API is used to obtain your billed VOD storage till the last 23:59:59. As your billed VOD storage information is collected between 0:00 and 7:00, you are advised to call this API between 7:00 and 24:00 (Beijing time) to get an accurate data.

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
```
https://vod.api.qcloud.com/v2/index.php?Action=DescribeVodStorage
&COMMON_PARAMS
```
## API Response

### Parameter Description
| Parameter | Type | Description |
|---------|---------|---------|
| code | Integer | Error code, 0: Successful; other values: Failed. |
| message | String | Error message |
| data | Object | Returned data |

data (VOD storage data)

| **Parameter** | **Type** | **Description** |
|---------|---------|---------|
| used_space | Integer | Storage (in byte) |

### Error Codes
| Error Code | Description |
|---------|---------|
| 4000-7000 | For more information, please see [Common Error Codes](https://cloud.tencent.com/document/product/266/7783)  |
| 1 | Internal error  |
| 1000 | Invalid parameter  |
| 1001 | Internal error  |
| 1003 | Internal error  |
| 2000 | Internal error  |
| 10022 | Internal error |

### Response Example
```javascript
{
    "code": 0,
    "message": "",
    "data": {
        "used_space":1024
    }
}
```

