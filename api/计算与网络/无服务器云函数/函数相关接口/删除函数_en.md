## 1. API Description
This API is used to delete function, along with the triggers that are bound to this function.

Domain name for API access: scf.api.qcloud.com
## 2. Request Parameter
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see [Common Request Parameters](/doc/api/244/4183). The Action field for this API is DeleteFunction.

| Parameter Name | Required | Type | Description |
|-----------|--------|----------|----------|
| functionName | Yes | String | Name of the function to be deleted. |

## 3. Response Parameters
| Parameter Name | Type | Description |
|-------|---|---------------|
| code | Int | Common error code. 0: Successful; other values: Failed. |
| message | String | Module error message description depending on API |
| codeDesc | String | Error code. For a successful operation, "Success" will be returned. For a failed operation, a message describing the failure will be returned. |

## 4. Example
Input
```
https://scf.api.qcloud.com/v2/index.php?Action=DeleteFunction
&<Common request parameters>
&functionName=hell
```
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success"
}
```

