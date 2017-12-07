## 1. API Description
 
This API (DeleteVpc) is used to delete VPCs.
Domain for API request:<font style="color:red">vpc.api.qcloud.com</font>

1) Before deleting a VPC, please make sure that there is no relevant resource in the VPC, such as CVMs, Cloud Databases, NoSQL, VPN gateways, Direct Connect gateways, cloud load balancers, peering connections, and linked basic network devices.
2) Once deleted, the VPC CANNOT be recovered. Please be careful.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is DeleteVpc.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | VPC ID assigned by the system. Support both vpcId before the upgrade and unVpcId after the upgrade.  |

 

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href="https://intl.cloud.tencent.com/document/product/215/4781" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
 
## 4. Error Codes
 The following error code list only provides the business logic error codes for this API. For common error codes, please see <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.

| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound |The VPC does not exist. Please check the information you entered.  |
| InvalidVpc.CannotDelete | The VPC cannot be deleted because there are still resources under the VPC. |

## 5. Example
 
Input
<pre>

  https://vpc.api.qcloud.com/v2/index.php?Action=DeleteVpc
	&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
  &vpcId=vpc-2ari9m7h
</pre>

Output
```

{
    "code": 0,
    "message": ""
}

```


