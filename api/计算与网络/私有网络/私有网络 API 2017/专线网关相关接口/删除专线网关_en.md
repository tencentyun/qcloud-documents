## 1. API Description

This API (DeleteDirectConnectGateway) is used to delete Direct Connect gateway.
Domain for API request:<font style="color:red">vpc.api.qcloud.com</font>

1) For a NAT gateway, NAT and ACL rules will be cleaned upon the deletion of Direct Connect gateway.
2) When the Direct Connect gateway is deleted, the routing policy associated with the gateway in the routing table will also be deleted.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is DeleteDirectConnectGateway.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | VPC ID assigned by the system, e.g. vpc-7t9nf3pu. |
| directConnectGatewayId | Yes | String | Direct Connect gateway ID assigned by the system, e.g. dcg-7t9nf3pu. |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Succeeded, other values:  Failed. |
| message | String | Error message. |
| taskId | Int | Task ID. The operation result can be queried with taskId. For more information, refer to <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%bb%bb%e5%8a%a1%e6%89%a7%e8%a1%8c%e7%bb%93%e6%9e%9c%e6%8e%a5%e5%8f%a3">API for Querying Task Execution Result</a>.  |

 ## 4. Error Code List
  The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify that you have entered resource information correctly.  |
| InvalidDirectConnectGateway.NotFound | Invalid Direct Connect gateway. Direct Connect gateway resource does not exist. Please verify that you have entered resource information correctly.  |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DeleteDirectConnectGateway
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&vpcId=vpc-dfgg190
&directConnectGatewayId=dcg-ddf14d
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "taskId":16284
}
```


