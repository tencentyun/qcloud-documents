## Result

Response from running functions

| Name | Type | Required | Description |
|------|------|----------|------|
| Log | String | Yes | Indicates the log output during the function execution. Null is returned for asynchronous calls. |
| RetMsg | String | Yes | Indicates the response from the running function. Null is returned for asynchronous calls. |
| ErrMsg | String | Yes | Indicates the error message of the running function. Null is returned for asynchronous calls. |
| MemUsage | Integer | Yes | Indicates the memory size when the function is running (in bytes). Null is returned for asynchronous calls. |
| Duration | Float | Yes | Indicates the duration required for running the function (in milliseconds). Null is returned for asynchronous calls. |
| BillDuration | Integer | Yes | Indicates the bill duration for the function (in milliseconds). Null is returned for asynchronous calls. |
| FunctionRequestId | String | Yes | ID of the running function |
| InvokeResult | Integer | Yes | 0 means true. Null is returned for asynchronous calls. |

