## 1. API Description
 
This API (DescriptionOperationResult) is used to acquire the completion status of asynchronous tasks.

Domain for API request: bm.api.cloud.tencent.com


## 2. Input Parameters

The following request parameter list only provides API request parameters. For additional parameters, see [Common Request Parameters](/doc/api/456/6718) page.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| taskId | Yes | Int | Asynchronous task ID.  |



## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, please see [Common Error Codes](/doc/api/456/6725) in the Error Codes page. |
| message | String | Module error message description depending on API. |
| data | obj | Returned completion status of the asynchronous task |

data is the json information of the completion status. It contains the following fields

| Parameter Name | Type | Description |
|---------|---------|---------|
| status | Int | Overall status of the task.<br/> 1 Succeeded<br/> 2 Failed<br/> 3 Partially succeeded, partially failed<br/> 4 Incomplete<br/> 5 Partially succeeded, partially incomplete<br/> 6 Partially incomplete, partially failed<br/> 7 Partially incomplete, partially failed, partially succeeded |
| resourceIds | Obj | Operation completion status of each CPM | 


## 4. Module Error Codes

| code | codeDesc | Description |
|------|------|------|
| 9001 | InternalError.DbError | An error occurred when operating the database |
| 10001 | InvalidParameter | Invalid parameter |

## 5. Example
 
Input

<pre>`https://domain/v2/index.php?`
	Action=DescriptionOperationResult
	&taskId=1000800001
	&<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>
</pre>
Output

```
{
  "code": 0,
  "message": "OK",
  "data": {
       "status": 1,
       "instanceIds": [
             {
                 "instanceId": "cpm-3dw234",
                 "status" : 1
             },
             {
                 "instanceId": "cpm-sdf343x",
                 "status" : 1
             }
         ]
   }
}

```
