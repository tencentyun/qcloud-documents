## 1. API Description

This API (CreateDirectConnectGateway) is used to create Direct Connect gateway.
Domain for API request:<font style="color:red">vpc.api.qcloud.com</font>

1) Direct Connect gateway is used to connect virtual private cloud and your private Direct Connect. For more information, refer to <a href="https://cloud.tencent.com/doc/product/216/549" title="Direct Connect Gateway" >Direct Connect Gateway Product Overview</a>.
2) There are two types of Direct Connect gateway: NAT and non-NAT. The former supports the configuration of network address translation. Once specified, the type cannot be changed. You may create a NAT Direct Connect gateway and a non-NAT one gateway for a VPC.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is CreateDirectConnectGateway.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | VPC ID assigned by the system, e.g. vpc-dgd545 |
| directConnectGatewayName | Yes | String | Direct Connect gateway name, which has a length of 1-25 characters, and can contain Chinese characters, uppercase and lowercase English letters, numbers, and underscores |
| type | No | Int  | Type of Direct Connect gateway; 0: Non-NAT; 1: NAT. Default is non-NAT |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Succeeded, other values:  Failed |
| message | String | Error message |
| data.n.directConnectGatewayId | String | Direct Connect gateway ID, e.g. dcg-mmf0dp2b |

 ## 4. Error Code List
  The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error Code | Description |
|---------|---------|
| InvalidDirectConnectGatewayName | Invalid Direct Connect gateway name. Valid name has a length of 1-60 characters, and can contain Chinese characters, uppercase and lowercase English letters, numbers, and underscores |  |
| DirectConnectGatewayLimitExceeded | The limit of requested Direct Connect gateway resources for the specific region has been reached. Please contact customer service for more resources. For more information on VPC resource restrictions, refer to <a href="https://cloud.tencent.com/doc/product/215/537" title="VPC Usage Restrictions">VPC Usage Restrictions</a>.  |
| InvalidVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify that you have entered resource information correctly.  |

## 5. Example
Input

<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=CreateDirectConnectGateway
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&vpcId=vpc-dfgg190
&directConnectGatewayName=Direct Connect gateway
&type=0
</pre>

Output

```
{
    "code":"0",
    "message":"",
    "data":{
        "directConnectGatewayId":"dcg-mmf0dp2b"
    }
}
```


