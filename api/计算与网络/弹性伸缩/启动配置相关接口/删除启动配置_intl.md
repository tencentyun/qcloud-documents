## 1. API Description
This API (DeleteScalingGroup) is used to delete scaling configurations.
Domain for API request: <font style="color:red">scaling.api.qcloud.com</font>

1) If a scaling configuration in the scaling group is in active status, then it cannot be deleted.

2) If a CVM instance created by the scaling configuration still exists in the scaling group, then it cannot be deleted.


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is DeleteScalingGroup.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| scalingConfigurationId | Yes | String | Scaling configuration ID to be deleted. It can be queried by calling <a href="/doc/api/372/查询启动配置" title="Query Scaling Configuration">Query Scaling Configuration</a> (DescribeScalingConfiguration) API. |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="http://intl.cloud.tencent.com/document/product/377/8946" title="Common Error Codes ">Common Error Codes</a> on the Error Code page. |
| codeDesc | String | Error code at business side. If the task succeeds, it will return "Success"; if the task fails, the specific business error reason will be returned. |
| message | String | Module error message description depending on API. |

## 4. Error Codes 
The following error codes only include the business logic error codes for this API. For additional common error codes, refer to [AS Error Code](http://intl.cloud.tencent.com/document/product/377/8946).

| Error Code | Description |
|----|------|
|Conflict.ScallingConfigurationUse| Scaling configuration is in use |

## 5. Example

```
https://scaling.api.qcloud.com/v2/index.php?
&<Common request parameters>
&scalingConfigurationId=xxx
```
Example of returned result is as follows. The code is 0, indicating that the scaling configuration has been deleted successfully.
```
{
    "code":"0",
    "message":"",  
    "codeDesc":"Success",  
    "data":[]
```
