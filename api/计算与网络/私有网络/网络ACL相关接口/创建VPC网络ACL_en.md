## 1. API Description

This API (CreateNetworkAcl) is used to create network ACL.
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>

1) A network ACL is a set of network security policies configured for a certain subnet, it is different from security groups in CVMs. A security group is a set of security policies configured for a certain CVM.
2) If security group policies have been configured for a CVM, and network ACL polices have been configured for the subnet in which the CVM resides, inbound requests of the CVM will match network ACL policies first, outbound requests will match security group policies first.
3) Security groups for CVMs are stateful, while network ACLs are stateless.
 

## 2. Input Parameters
 
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is CreateNetworkAcl.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | Virtual private cloud ID of the subnet, which can be vpcId or unVpcId. unVpcId is recommended. For example: vpc-4n9efgju. You can query this through API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| networkAclName | Yes | String | Network ACL name; you can specify any name you like, but its length should be limited to 60 characters. The name must be unique under the same VPC.  |

 

## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded, other values: Failed.  |
| message | String | Error message.  |
| data.networkAclId | String | Network ACL ID. For example: acl-4n9efgju.  |

## 4. Error Codes
 The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.

| Error code | Description |
|---------|---------|
| InvalidVpc.NotFound | The VPC does not exist. Please check the information you entered. You can query the VPC via the API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| InvalidNetworkAclName | Invalid network ACL name. It should be within 60 characters.  |
| NetworkAclLimitExceeded | Number of created network ACLs has exceeded the limit. Please contact customer service for more resources. For more information on VPC resource restrictions, see <a href="https://cloud.tencent.com/doc/product/215/537" title="VPC Usage Restrictions">VPC Usage Restrictions</a>.  |
 

## 5. Example
 
Input
<pre>
  https://vpc.api.qcloud.com/v2/index.php?Action=CreateNetworkAcl
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
  &vpcId=gz_vpc_266
  &networkAclName=dgdgadgd

</pre>

Output
```

{
    "code": 0,
    "message": "",
    "data": {
        "networkAclId": "acl-4n9efgju"
    }
}

```


