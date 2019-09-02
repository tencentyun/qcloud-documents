## Deleting Tasks
This API is used to delete offline messages for group push tasks with task IDs (push IDs) and for tasks that have been sent.
This feature is only available in [XGPush Console](https://xg.qq.com). Log in to the console and click the **Stop** button in Task Management.

## Canceling Tasks
This API is used to cancel scheduled group push tasks not triggered. The task ID is required for tasks that have not been sent.
URL path: `http://domain name for API/v2/push/cancel_timing_task?params`

### Request Parameters
In addition to the [common parameters](https://cloud.tencent.com/document/product/548/14705), the following parameters are needed:

| Parameter Name | Type | Required | Default | Description |
|-|-|-|-|-|
| push_id | String | Yes | None | ID of the task to be canceled |

### Response Parameters
In the common response parameters, the json format of the field result is as follows:
```
{
"status": 0, //0: successful, others: failed
}
```
### Example
Before MD5 encryption, URL is used to generate sign, and Rest API URL is the URL of the final request. The following is an example of push to Android, in which the common parameters need to be replaced.
#### Before MD5 encryption:
```
GETopenapi.xg.qq.com/v2/push/cancel_timing_taskaccess_id=2100240957push_id=2853333945timestamp=1502700856f255184d160bad51b88c31627bbd9530
```

#### Rest API URL:
```
http://openapi.xg.qq.com/v2/push/cancel_timing_task?access_id=2100240957&push_id=2853333945&timestamp=1502700856&sign=1fb3b7846f79d0027542acd05effb4a3
```


