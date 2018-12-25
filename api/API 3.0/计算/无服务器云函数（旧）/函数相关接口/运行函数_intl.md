## 1. API Description
Domain for API request: scf.tencentcloudapi.com

This API (Invoke) is used to run functions. 

## 2. Input Parameters
The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/583/17238).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes |  String | Common parameter. Value used in this API: Invoke |
| Version | Yes |  String | Common parameter. Value used in this API: 2018-04-16 |
| FunctionName | Yes |  String | Function name. |
| InvocationType | No |  String | RequestResponse (synchronous) and Event (asynchronous). Default is synchronous. |
| Qualifier | No |  String | Version No. to trigger a function. |
| ClientContext | No |  String | Function execution parameter, which is passed in the JSON format. Maximum parameter size: 1 MB. |
| LogType | No |  String | This field is specified when using synchronous call. The returned value includes a log of 4 KB. Available values: None (default) and Tail. If the value is Tail, the logMsg field in the returned parameters will contain the corresponding function execution log. | 

## 3. Output Parameters


| Parameter Name | Type | Description |
|---------|---------|---------|
| Result | [Result](/document/api/583/17244#Result) | Function execution result |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating the problem. | 

## 4. Error Codes
The following error codes only include the business logic error codes for this API. For additional common error codes, please see [Common Error Codes](/document/api/583/17240#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).


| Error Code | Description |
|---------|---------|
| FailedOperation | Operation failed |
| InvalidParameterValue.Param | The parameter you specify is not in the standard JSON format. |
| ResourceNotFound.FunctionName | Function does not exist. |
| ResourceUnavailable.InsufficientBalance | Your balance is insufficient. Please top up first. |
| UnauthorizedOperation | Unauthorized operation | 

## 5. Example
### Example 1 Run a function
### Request parameters
```
https://scf.tencentcloudapi.com/?Action=Invoke
&FunctionName=xxxx
&<Common request parameters>
```
#### Response parameters
```
{
  "Response": {
    "RequestId": "c2af8a64-c922-4d55-aee0-bd86a5c2cd12",
    "Result": {
      "BillDuration": 100,
      "Duration": 0.826,
      "ErrMsg": "",
      "FunctionRequestId": "6add56fa-58f1-11e8-89a9-5254005d5fdb",
      "InvokeResult": 0,
      "Log": "",
      "MemUsage": 3207168,
      "RetMsg": "hello from scf"
    }
  }
}
```

