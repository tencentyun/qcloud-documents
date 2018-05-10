## 1. API Description

This API (DeleteNetworkAcl) is used to delete network ACL.
Domain for API request:<font style="color:red">vpc.api.qcloud.com</font>

Network ACLs with bound subnets cannot be deleted. You need to unbind any subnets from the network ACL before you can delete it. 

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. See the<a href="/doc/api/372/4153" title="Common request parameters"> Common Request Parameters</a> page for details. The Action field for this API is DeleteNetworkAcl.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | Virtual private cloud ID of the subnet, which can be vpcId or unVpcId. unVpcId is recommended. For example: vpc-erxok83l. You can query this through API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| networkAclId | Yes | String | Network ACL ID assigned by the system. For example: acl-jk7weyp2. Can be queried via the <a href="https://cloud.tencent.com/doc/api/245/1441" title="DescribeNetworkAcl">DescribeNetworkAcl</a> API.  |
 

## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded, other values: failed |
| message |  String | Error message |

## 4. Error Codes
  The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error code | Description |
|---------|---------|
| InvalidVpc.NotFound | The VPC does not exist. Please check the information you entered. You can query the VPC via the <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a> API.  |
| InvalidNetworkAclID.NotFound | The network ACL ID does not exist. Please check the information you entered. You can query network ACL IDs via the <a href="https://cloud.tencent.com/doc/api/245/1441" title="DescribeNetworkAcl">DescribeNetworkAcl</a> API.  |
| NetworkAclID.InUse | There are subnets associated with the network ACL. ACLs with associated subnets cannot be deleted.  |

## 5. Example
 
Input
<pre>
  https://vpc.api.qcloud.com/v2/index.php?Action=DeleteNetworkAcl
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
  &vpcId=vpc-erxok83l
  &networkAclId=acl-jk7weyp2
</pre>

Output
```

{
    "code": 0,
    "message": ""
}

```


