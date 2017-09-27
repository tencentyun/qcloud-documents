## 1. API Description
This API is used to delete trigger according to specified function name and trigger name.

Domain name for API access: scf.api.qcloud.com
## 2. Request Parameter
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see [Common Request Parameters](/doc/api/244/4183). The Action field for this API is DeleteTrigger.

| Parameter Name | Required | Type | Description |
|-----------|--------|----------|----------|
| functionName | Yes | String | Function name. |
| triggerName | Yes | String | Name of the trigger to be deleted. Name for a COS trigger should always be in the format of `<bucketName>-<UID>.<Region>.myqcloud.com`, while name for a timer trigger is a user-defined name. |
| type | Yes | String | Type of the trigger to be deleted. Two types are currently supported: cos and timer. |
| triggerDesc | Yes | String | This field is mandatory if the trigger to be deleted is a COS trigger, in which case this field shares the same format in `{"event":"cos:ObjectCreated:*"}` where JSON data is stored, in the data content and in the SetTrigger API. This field is optional if the trigger to be deleted is a timer trigger. |

## 3. Response Parameters
| Parameter Name | Type | Description |
|-------|---|---------------|
| code | Int | Common error code. 0: Successful; other values: Failed. |
| message | String | Module error message description depending on API |
| codeDesc | String | Error code. For a successful operation, "Success" will be returned. For a failed operation, a message describing the failure will be returned. |

## 4. Example
Input
```
https://scf.api.qcloud.com/v2/index.php?Action=DeleteTrigger
&<Common request parameters>
&functionName=hell
&type=timer
&triggerName=test2
```
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success"
}
```

