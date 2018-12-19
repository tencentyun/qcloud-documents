## 1. API Description

This API (ModifyDirectConnectGateway) is used to modify the attributes of Direct Connect gateway.
Domain for API request:<font style="color:red">vpc.api.qcloud.com</font>

Currently, only modification to the name in the attributes of Direct Connect gateway is supported.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is ModifyDirectConnectGateway.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | VPC ID assigned by the system, e.g. vpc-7t9nf3pu. |
| directConnectGatewayId | Yes | String | Direct Connect gateway ID assigned by the system, e.g. dcg-7t9nf3pu. |
| directConnectGatewayName | Yes | String | Direct Connect gateway name, which has a length of 1-25 characters, and can contain Chinese characters, uppercase and lowercase English letters, numbers, and underscores. |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0:  Succeeded, other values:  Failed. |
| message | String | Error message. |
| taskId | Int | Task ID. The operation result can be queried with taskId. For more information, refer to API for Querying Task Execution Result. |

 ## 4. Error Code List
  The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error Code | Description |
|---------|---------|
| InvalidDirectConnectGatewayName | Invalid Direct Connect gateway name. Direct Connect gateway name, which has a length of 1-60 characters, and can contain Chinese characters, uppercase and lowercase English letters, numbers, and underscores.  |
| InvalidVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify that you have entered resource information correctly.  |
| InvalidDirectConnectGateway.NotFound | Invalid Direct Connect gateway. Direct Connect gateway resource does not exist. Please verify that you have entered resource information correctly.  |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=ModifyDirectConnectGateway
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&vpcId=vpc-dfgg190
&directConnectGatewayId=dcg-ddf14d
&directConnectGatewayName=Direct Connect Gateway1
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "taskId":16284
}
```


