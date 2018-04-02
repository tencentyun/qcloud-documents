## API Name
GetTaskList

## Feature Description
1. Query the task list;
2. When the list data is too much to be pulled by a single API calling, you can pull the data in batches with the parameter "next";
3. Only tasks within the last three days (72 hours) can be queried.

## Request Method

### Request Domain
vod.api.qcloud.com

### Max Calling Frequency
100/min

### Parameter Description
| Parameter | Required | Type | Description |
|---------|---------|---------|---------|
| fileId | No | String | File ID. If this field is entered, only the task list of this file can be queried. |
| status | Yes | String | Task status: There are 3 types of status (WAITING, PROCESSING, FINISH). |
| maxCount | No | Integer | The amount of data returned in this query. The value range is between 10 and 100, and the default is 10 if it is left empty. |
| next | No | String | Used for pulling in batches: when the list data is too much to be pulled by a single API calling, the ID of the last data is returned. The next request will carry the ID, and data from the next ID will be pulled. |
| COMMON_PARAMS | Yes |  | For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976). |

### Request Example
```
https://vod.api.qcloud.com/v2/index.php?Action=GetTaskList
&next=59b61160f78939626efd644b
&startTime=1505294672
&endTime=1505295672
&status=Processing
&COMMON_PARAMS
```
## API Response

### Parameter Description
| Parameter | Type | Description |
|---------|---------|---------|
| code | Integer | Error code, 0: Successful; other values: Failed. |
| message | Integer | Error message. |
| data | Object | Task data. |
| data.next | String | When the list data is too much to be pulled by a single API calling, the ID of the last data will be returned. The next request will carry the ID, and data from the next ID will be pulled. If the parameter is empty, it means that all the data has been pulled. |
| data.status | String | Task statues: WAITING, PROCESSING, or FINISH. |
| data.taskList | Array | Task data list. |
| data.taskList.vodTaskId | String | Task ID. |
| data.taskList.type | String | Task type. |
| data.taskList.createTime | Integer | Task creation time (Unix timestamp). |
| data.taskList.beginProcessTime | Integer | The time when the task is executed (Unix timestamp). The value is 0 if the task is still in queue. |
| data.taskList.finishTime | Integer | The latest update time of the task data (Unix timestamp). The value is 0 if the task is still in process. |
| COMMON_PARAMS |  | For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0). |

### Error Codes
| Error Code | Description |
|---------|---------|
| 4000-7000 | For more information, please see [Common Error Codes](https://cloud.tencent.com/document/product/266/7783).  |
| 1000 | Invalid parameter. |
| 10027 | System internal error. |

### Response Example

```javascript
{
    "code": 0,
    "message": "",
    "data": {
        "status": "PROCESSING",
        "next": "68bfa4c7b3244d1c3acb5b70",
        "taskList": [
            {
                "vodTaskId": "1251132654-Procedure-d7c9631c15ecf653b1ff67e34cb046ff",
                "type": "procedure",
                "createTime": 1485156352,
                "beginProcessTime": 1485156354,
                "finishTime": 1485156352
            },
            {
                "type": "transcode",
                "vodTaskId": "1251132654-Procedure-d7c9631c15ecf653b1ff67e34cb046bb",
                "createTime": 1485156352,
                "beginProcessTime": 1485156354,
                "finishTime": 1485156352
            }
        ]
    }
}
```
