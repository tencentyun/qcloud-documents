## 1. API Description
This API is used to trigger and execute specified function. Two trigger methods are currently supported: synchronous and asynchronous. For synchronous calls, the returned values will contain an additional field `payLoad` which indicates the returned values of the function.

Domain name for API access: scf.api.qcloud.com

## 2. Request Parameter
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see [Common Request Parameters](/doc/api/244/4183). The Action field for this API is InvokeFunction.

| Parameter Name | Required | Type | Description |
|-----------|--------|----------|----------|
| functionName | Yes | String | Name of the function to be executed. |
| invokeType | No | String | Trigger method. Available values: `RequestResponse (synchronous)`, `Event (asynchronous)`. Default is synchronous. |
| param | No | String | Function execution parameter, which is passed in JSON format. Max parameter length: `1 MB`. |
| logType | No | String | This field is specified when using synchronous call. Returned values will include `4K` log. Available values: `None` (default), `Tail`. When the value is `Tail`, the `logMsg` field in the returned parameters will contain the corresponding function execution log. |

## 3. Response Parameters
| Parameter Name | Type | Description |
|-------|---|---------------|
| code | Int | Common error code. 0: Successful; other values: Failed. |
| message | String | Module error message description depending on API |
| codeDesc | String | Error code. For a successful operation, "Success" will be returned. For a failed operation, a message describing the failure will be returned. |
| data | String | This field contains relevant information of the function execution (in JSON format). |

Data structure of the "data" field is as follows:

| Parameter Name | Type | Description |
|-------|---|---------------|
| requestId | String | request_id of the function execution process. |
| payLoad | String | Returned values of the function execution process. This is only returned for synchronous calls. |
| logMsg | String | Log output during the function execution process. This is only returned for synchronous calls. |
| memSize | Int | Memory size during the function execution process (in bytes). This is only returned for synchronous calls. |
| duration | Float | Time cost for the function execution process (in milliseconds). This is only available for synchronous calls. |


## 4. Example
#### Asynchronous Request
Input
```
https://scf.api.qcloud.com/v2/index.php?Action=InvokeFunction
&<Common request parameters>
&functionName=hell
&param={"aa":3}
&invokeType=Event
```

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "requestId": "141c9b47-2b19-11e7-9a9b-5254007d2563",
    }
}
```
#### Synchronous Request
Input:

```
https://scf.api.qcloud.com/v2/index.php?Action=InvokeFunction
&<Common request parameters>
&functionName=hell
&param={"aa":3}
&invokeType=RequestResponse
&logType=Tail
```

Output:
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "duration": 0.422,
        "memUsage": 126976,
        "log": "log in func\n",
        "requestId": "c471ac84-2f15-11e7-8501-5254007d2563",
        "retMsg": "Hello from Lambda"
        "billDuration": 100
    }
}

```

