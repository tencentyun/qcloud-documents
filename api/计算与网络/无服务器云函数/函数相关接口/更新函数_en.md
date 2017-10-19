## 1. API Description
This API is used to update relevant fields of a function, including code, handling method, description, runtime memory size, time out and so on.   

Domain name for API access: scf.api.qcloud.com

## 2. Request Parameter
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see [Common Request Parameters](/doc/api/244/4183). The Action field for this API is UpdateFunction.

| Parameter Name | Required | Type | Description |
|-----------|--------|----------|----------|
| functionName | Yes | String | Name of the function to be modified. |
| code | No | String | This includes the code files for the function and zip files containing the dependent elements. When using the API, you need to encode the content of the zip files using base64 and prefix the encoded characters with `@`. Max size: `5 MB`.<span style="color:red"> Note: this string will not be used for authentication.</span> |
| handler | No | String | Name of function handling method. Format: "<file name>.<function name>", file name and function name are separated with ".". File name and function name may contain letters, numbers, underscores and en dashes (-) but must start and end with letters. Length for file name and function name: 2-60 characters. |
| description | No | String | Function description. Description can contain a maximum of 1,000 characters (letters, numbers, spaces, commas and periods). |
| memorySize | No | Int | Memory size when the function runs. Default: 128 MB. Available range: 128 MB - 1536 MB |
| timeout | No | Int | Maximum function operation time (in seconds). Available range: 1 - 300 seconds. Default is 3 seconds. |

## 3. Response Parameters
| Parameter Name | Type | Description |
|-------|---|---------------|
| code | Int | Common error code. 0: Successful; other values: Failed. |
| message | String | Module error message description depending on API |
| codeDesc | String | Error code. For a successful operation, "Success" will be returned. For a failed operation, a message describing the failure will be returned. |

## 4. Example
Input
```
https://scf.api.qcloud.com/v2/index.php?Action=UpdateFunction
&<Common request parameters>
&functionName=hell
&memorySize=130
&timeout=2
```
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success"
}
```

