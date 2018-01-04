## API Name
RedoTask

## Feature Description
1. Retry the task without changing the task ID. Data will be overwritten if the retry succeeds;
2. Only the finished tasks can be retried;
3. Only tasks within the last three days (72 hours) can be retried.

## Request Method

### Request Domain
vod.api.qcloud.com

### Max Calling Frequency
100/min

### Parameter Description
| Parameter | Required | Type | Description |
|---------|---------|---------|---------|
| vodTaskId | Yes | String | Task ID. |
| COMMON_PARAMS | Yes |  | For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976). |

### Request Example
```
https://vod.api.qcloud.com/v2/index.php?Action=RedoTask
&vodTaskId=1251132654-Procedure-d7c9631c15ecf653b1ff67e34cb04692
&COMMON_PARAMS
```
## API Response

### Parameter Description
| Parameter | Type | Description |
|---------|---------|---------|
| code | Integer | Error code, 0: Successful; other values: Failed. |
| message | String | Error message. |

### Error Codes
| Error Code | Description |
|---------|---------|
| 4000-7000 | For more information, please see [Common Error Codes](https://cloud.tencent.com/document/product/266/7783)  |
| 1000 | Invalid parameter. |
| 70014 | The task does not exist. |
| 10027 | System internal error. |
| 70034 | The task is still in process. |

### Response Example

```javascript
{
    "code": 0,
    "message": ""
}
```
