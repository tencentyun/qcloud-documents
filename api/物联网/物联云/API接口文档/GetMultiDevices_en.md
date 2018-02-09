### 1. API Description
This API (GetMultiDevices) is used to query the execution result of creating devices in batches.

Domain name for API request: `iotcloud.api.qcloud.com`


### 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/doc/api/229/6976).

| Parameter Name | Required | Type | Description |
| -------- | ---- | ------ | ----------------- |
| taskID | Yes | String | Task ID. It is returned via the API for creating devices in batches. |
| pageNum | Yes | Int | The number of pages |
| pageSize | Yes | Int | Page size, i.e. the number of devices returned per page |



### 3. Output Parameters

| Parameter Name | Type | Description |
| -------------------- | --------------- | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see [Common Error Codes](https://cloud.tencent.com/document/product/634/12279). |
| message | String | Module error message description in the format of "(module error code) module error message". For more information, please see [Module Error Codes](#module_error_info) on this page. |
| codeDesc | String | Description of module error code |
| totalDevNum | Int | The total number of devices to be created by this task |
| listCreateDeviceInfo | Array of Object | Device details |

The listCreateDeviceInfo contains the following parameters:

| Parameter Name | Type | Description |
| ---------------- | ------ | ----------------------------- |
| deviceName | String | Device name |
| deviceCert | String | Device certificate |
| devicePrivateKey | String | Private key of the device |
| result | Int | Execution result. It is defined according to error codes returned by the API CreateDevice. |
| errMsg | String | Error message |



### 4. Example

Input

<pre>
  https://iotcloud.qcloud.com/v2/index.php?Action=GetMultiDevices
  &taskID=abcdedf123456789&pageNum=1&pageSize=10
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
</pre>

Output

```json
{       
    "message": "",
    "codeDesc": "Success",
    "code": 0,
	"taskID":"abcdedf123456789",
	"totalDevNum":2,
	"listCreateDeviceInfo":[
      {
        "deviceName":"test_device1",
        "deviceCert":"-----BEGIN CERTIFICATE-----\n-----END CERTIFICATE-----",
        "devicePrivateKey":"-----BEGIN PRIVATE KEY-----\n-----END PRIVATE KEY-----\n",
        "result":0
      },
      {
        "deviceName":"test_device2",
        "result":2001
      }
	]
}
```
<span id = "module_error_info"></span>
### 5. Module Error Codes

| Module Error Code | Description |
| ----- | --------------- |
| 2006 | The task does not exist. |
| 2100 | Internal server error. Please contact technicians. |
| 2101 | Invalid request parameter |
