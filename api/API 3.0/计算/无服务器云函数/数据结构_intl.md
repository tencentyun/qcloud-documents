## **Code**

Function code

Referenced by the following API: CreateFunction.

| Name | Type | Required | Description |
|------|------|----------|------|
| CosBucketName | String | No | Name of the object bucket |
| CosObjectName | String | No | Path of the COS object |
| ZipFile | String | No | This contains a .zip file of the function code file and its dependencies. When using this API, the content of the .zip file needs to be encoded with Base64. It can be up to 20MB |
| CosBucketRegion | String | No | Region of the COS. For the Beijing region, you need to pass in ap-beijing; for the Beijing Region One, you need to pass in ap-beijing-1; for other regions, this parameter can be left blank |

## **Environment**

Environment variable of the function

Referenced by the following APIs: CreateFunction, GetFunction, UpdateFunctionConfiguration.

| Name | Type | Required | Description |
|------|------|----------|------|
| Variables | Array of [Variable](#Variable) | No | Environment variable array |

## **Filter**

Log filtering conditions for distinguishing between logs for successes and logs for errors

Referenced by the following API: GetFunctionLogs.

| Name | Type | Required | Description |
|------|------|----------|------|
| RetCode | String | No | filter.retCode=not0 indicates that only the logs for errors are returned, while filter.retCode=is0 indicates that only the logs for successes are returned; if this parameter is not passed in, all logs are returned | |

## **Function**

Function list

Referenced by the following API: ListFunctions.

| Name | Type | Description |
|------|------|-------|
| ModTime | String | Modified time |
| AddTime | String | Created time |
| Runtime | String | Runtime |
| FunctionName | String | Name of the function |
| FunctionId | String | Function ID |
| Namespace | String | Namespace |

## **FunctionLog**

Log information

Referenced by the following API: GetFunctionLogs.

| Name | Type | Description |
|------|------|-------|
| FunctionName | String | Name of the function |
| RetMsg | String | Return value after function execution |
| RequestId | String | The requestId that executes this function |
| StartTime | Timestamp | Time point when the function starts executing |
| RetCode | Integer | Function execution result; 0 for success and other values for failure |
| InvokeFinished | Integer | This indicates whether the function call is ended; 1 for ended call and other values for exceptional call |
| Duration | Float | Duration of function execution in ms |
| BillDuration | Integer | Duration for function billing in ms, rounded upwards to the nearest 100 ms |
| MemUsage | Integer | The actual memory size consumed by function execution in bytes |
| Log | String | Log output during function execution |

## **Result**

Return of the executed function

Referenced by the following API: Invoke.

| Name | Type | Description |
|------|------|-------|
| Log | String | Log output during function execution; null for async call |
| RetMsg | String | This indicates the return of the executed function; null for async call |
| ErrMsg | String | This indicates the error message returned for the executed function; null for async call |
| MemUsage | Integer | The memory size consumed by function execution in bytes; null for async call |
| Duration | Float | This indicates the duration of function execution in ms; null for async call |
| BillDuration | Integer | This indicates the duration for function billing in ms; null for async call |
| FunctionRequestId | String | ID of this function execution |
| InvokeResult | Integer | 0 for successes; null for async call |

## **Trigger**

Trigger type

Referenced by the following API: GetFunction.

| Name | Type | Description |
|------|------|-------|
| ModTime | Timestamp | Last modified time of the trigger |
| Type | String | Type of the trigger |
| TriggerDesc | String | Detailed configuration of the trigger |
| TriggerName | String | Name of the trigger |
| AddTime | Timestamp | Created time of the trigger |

## **Variable**

Variable parameters

Referenced by the following APIs: CreateFunction, GetFunction, UpdateFunctionConfiguration.

| Name | Type | Required | Description |
|------|------|----------|------|
| Key | String | No | Name of the variable |
| Value | String | No | Value of the variable |

## **VpcConfig**

VPC parameter configuration

Referenced by the following APIs: CreateFunction, GetFunction, UpdateFunctionConfiguration.

| Name | Type | Required | Description |
|------|------|----------|------|
| VpcId | String | No | ID of the VPC |
| SubnetId | String | No | ID of the subnet |

