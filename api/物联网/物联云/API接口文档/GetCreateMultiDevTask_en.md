### 1. API Description
This API (GetCreateMultiDevTask) is used to query the execution status of creating device tasks in batches.

Domain name for API request: `iotcloud.api.qcloud.com`


### 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/doc/api/229/6976).

| Parameter Name | Required | Type | Description |
| ------ | ---- | ------ | ----------------- |
| taskID | Yes | String | Task ID. It is returned via the API for creating devices in batches. |



### 3. Output Parameters

| Parameter Name | Type | Description |
| ---------- | ------ | ---------------------------------------- |
| code | Int | Common error code. 0: successful; other values: failed. For more information, please see [Common Error Codes](https://cloud.tencent.com/document/product/634/12279). |
| message | String | Module error message description in the format of "(module error code) module error message". For more information, please see [Module Error Codes](#module_error_info) of this page. |
| codeDesc | String | Description of module error code |
| taskStatus | Int | Whether the task is completed. 0: The task has not been started; 1: The task is being executed; 2: The task has been completed. |
| taskID | String | Task ID |



### 4. Example

Input

<pre>
  https://iotcloud.qcloud.com/v2/index.php?Action=GetCreateMultiDevTask
  &taskID=abcdedf123456789
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
</pre>

Output

```
{       
    "message": "",
    "codeDesc": "Success",
    "code": 0,
    "taskStatus":1,
    "taskID":"abcdedf123456789"
}
```
<span id = "module_error_info"></span>
### 5. Module Error Codes

| Module Error Code | Description |
| ----- | --------------- |
| 2006 | The task does not exist. |
| 2100 | Internal server error. Please contact technicians. |
| 2101 | Invalid request parameter |






