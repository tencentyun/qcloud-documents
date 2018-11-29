## 1. API Description
This API is used to create functions. You must specify function name, code and handling method when calling this API. The other parameters (function description, runtime memory size, time out and so on) are optional.     

Domain name for API access: scf.api.qcloud.com

## 2. Request Parameter
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see [Common Request Parameters](/doc/api/244/4183). The Action field for this API is CreateFunction.

| Parameter Name | Required | Type | Description |
|-----------|--------|----------|----------|
| functionName | Yes | String | Name of the created Lambda function, which can only include letters (upper case or lower case), numbers, en dashes (-) and underscores. The name must start with a letter and cannot end with en dash or underscore. Length: 2-60 characters. |
| code | Yes | String | This includes the function and zip files containing the dependent elements. When using the API, you need to encode the content of the zip files using base64 and prefix the encoded characters with `@`. Max size: `5 MB`. Note: this string will not be used for authentication. |
| handler | Yes | String | Name of function handling method. Format: "<file name>.<method name>", file name and function name are separated with ".". File name and function name may contain letters, numbers, underscores and en dashes (-) but must start and end with letters. Length for file name and function name: 2-60 characters. |
| description | No | String | Function description, which can contain a maximum of 1,000 characters (letters, numbers, spaces, commas, line breaks and periods). |
| memorySize | No | Int | Memory size when the function runs. Default: 128 MB. Available range: 128 MB - 1536 MB |
| timeout | No | Int | Maximum function operation time (in seconds). Available range: 1 - 300 seconds. Default is 3 seconds. |

**Note**: an account can have at most 20 Lambda functions in a region, and each Lambda function can have up to 2 timer triggers and 2 COS triggers.



## 3. Response Parameters
| Parameter Name | Type | Description |
|-------|---|---------------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see [Common Error Codes](/doc/api/244/1530) in the Error Codes page. |
| message | String | Module error message description depending on API |
| codeDesc | String | Error code. For a successful operation, "Success" will be returned. For a failed operation, a message describing the failure will be returned. |


## 4. Example
Input
```
https://scf.api.qcloud.com/v2/index.php?Action=CreateFunction
&<Common request parameters>
&functionName=myFunction
&code=Corresponding string when the zip file containing the code is encoded using base64
&hander=lambda_function.lambda_handler
&description=helloWorld Lambda function
&memorySize=128
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

