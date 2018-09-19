## 1. API Description

This API (ModifyNetworkAclEntry) is used to configure ACL rules.
Domain for API request:<font style="color:red">vpc.api.qcloud.com</font>

You can configure both inbound and outbound network ACL policies;

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is ModifyNetworkAclEntry.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | Virtual private cloud ID of the subnet, which can be vpcId or unVpcId. unVpcId is recommended. For example: vpc-jk7weyp2. You can query this through API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| networkAclId | Yes | String | Network ACL ID assigned by the system. For example: acl-jk7weyp2. Can be queried via the API <a href="https://cloud.tencent.com/doc/api/245/1441" title="DescribeNetworkAcl">DescribeNetworkAcl</a>.  | 
| ruleDirection | Yes | Int | Network ACL direction. 1: inbound, 0: outbound.  | 
| networkAclEntrySet.n | Yes | Array | Network ACL policy information array.  | 
| networkAclEntrySet.n.desc | Yes | String | Note.  |
| networkAclEntrySet.n.ipProtocol | Yes | String | Protocol, such as tcp.  |
| networkAclEntrySet.n.cidrIp | Yes | String | Source IP or source network segment (IP and CIDR are both supported). For example: 10.20.3.0 or 10.0.0.2/24.  |
| networkAclEntrySet.n.portRange | Yes | String | Source port (or source port range). For example: 80 or 90-100.  |
| networkAclEntrySet.n.action | Yes | Int | Policy. 0: Allow, 1: Reject.  |

 

## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Succeeded, other values:  Failed.  |
| message | String | Error message.  |

 ## 4. Error Code Table
  The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error code | Description |
|---------|---------|
| InvalidVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify that the resource information you entered is correct. You can query the VPC via the API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| InvalidNetworkAclID.NotFound | Invalid network ACL ID. Network ACL ID does not exist. Please verify that the resource information you entered is correct. You can query network ACL IDs via the API <a href="https://cloud.tencent.com/doc/api/245/1441" title="DescribeNetworkAcl">DescribeNetworkAcl</a>.  |
| NetworkAclInLimitExceeded | Number of created network ACL inbound rules has exceeded the limit. Please contact customer service for more resources. For more information on VPC resource restrictions, refer to <a href="https://cloud.tencent.com/doc/product/215/537" title="VPC Usage Restrictions">VPC Usage Restrictions</a>.  |
| NetworkAclOutLimitExceeded | Number of created network ACL outbound rules has exceeded the limit. Please contact customer service for more resources. For more information on VPC resource restrictions, see <a href="https://cloud.tencent.com/doc/product/215/537" title="VPC Usage Restrictions">VPC Usage Restrictions</a>.  |

## 5. Example
 
Input
<pre>
  https://vpc.api.qcloud.com/v2/index.php?Action=ModifyNetworkAclEntry
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
  &vpcId=vpc-erxok83l
  &networkAclId=acl-jk7weyp2
  &ruleDirection=1
  &networkAclEntrySet.0.desc=test
  &networkAclEntrySet.0.ipProtocol=all
  &networkAclEntrySet.0.cidrIp=0.0.0.0/0
  &networkAclEntrySet.0.portRange=ALL
  &networkAclEntrySet.0.action=1
</pre>

Output
```

{
    "code": 0,
    "message": ""
}

```


