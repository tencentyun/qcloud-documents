## 1. API Description

This API (DescribeNetworkAcl) is used to query network ACL.
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>
 

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is DescribeNetworkAcl.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | No | String | Virtual private cloud ID of the subnet, which can be vpcId or unVpcId. unVpcId is recommended. For example: vpc-0ox8fuhw. Can be queried via the API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| networkAclId | No | String | Network ACL ID assigned by the system. For example: acl-0ox8fuhw. Can be queried via the API <a href="https://cloud.tencent.com/doc/api/245/1441" title="DescribeNetworkAcl">DescribeNetworkAcl</a>.  |
| offset | No | Int | Offset of initial line. Default is 0.  |
| limit | No | Int | Number of lines per page. Default is 20 (maximum is 50).  |
| orderField | No | String | Sort by a certain field. Currently, sorting by createTime (default) and networkAclName is supported.  |
| orderDirection | No | String | Ascending (asc) or descending (desc). Default is desc.  |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Succeeded, other values:  Failed.  |
| message | String | Error message.  |
| totalCount |  Int | Return the total number of network ACLs in the result.  |
| data.n | array  | Returned array.  |
| data.n.vpcId | String | Virtual private cloud ID assigned by the system, for example: gz_vpc_8849.  |
| data.n.unVpcId | String | Virtual private cloud ID assigned by the system, new ID is recommended. For example: vpc-0ox8fuhw.  |
| data.n.networkAclId | String | Network ACL ID assigned by the system. For example: acl-e9dbyl8s.  |
| data.n.networkAclName | String | Network name.  |
| data.n.subnetNum | Int | Number of bound subnets.  |
| data.n.createTime | String | Creation time of network ACL, for example: 2015-11-06 20:55:12.  |
| data.n.networkAclEntrySet | Array | Network ACL policy information array.  |


**Structure of networkAclEntrySet network ACL policy array:**

| Parameter Name | Type | Description |
|---------|---------|---------|
| networkAclEntrySet.ingress.n | Array | Network ACL inbound rule.  |
| networkAclEntrySet.ingress.n.desc | String | Note.  |
| networkAclEntrySet.ingress.n.ipProtocol | String | Protocol, such as tcp.  |
| networkAclEntrySet.ingress.n.cidrIp | String | Source IP or source network segment (IP and CIDR are both supported). For example: 10.20.3.0 or 10.0.0.2/24.  |
| networkAclEntrySet.ingress.n.portRange | String | Source port (or source port range). For example: 80 or 90-100.  |
| networkAclEntrySet.ingress.n.action | Int | Policy. 1: Allow, 0: Reject.  |
| networkAclEntrySet.egress.n | Array | Network ACL outbound rule.  |
| networkAclEntrySet.egress.n.desc | String | Note.  |
| networkAclEntrySet.egress.n.ipProtocol | String | Protocol, such as tcp.  |
| networkAclEntrySet.egress.n.cidrIp | String | Source IP or source network segment (IP and CIDR are both supported). For example: 10.20.3.0 or 10.0.0.2/24.  |
| networkAclEntrySet.egress.n.portRange | String | Source port (or source port range). For example: 80 or 90-100.  |
| networkAclEntrySet.egress.n.action | Int | Policy. 1: Allow, 0: Reject.  |

## 4. Error Code Table
  The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error code | Description |
|---------|---------|
| InvalidVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify that the resource information you entered is correct. You can query the VPC via the API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>. |
| InvalidNetworkAclID.NotFound | Invalid network ACL ID. Network ACL ID does not exist. Please verify that the resource information you entered is correct. You can query network ACL IDs via the API <a href="https://cloud.tencent.com/doc/api/245/1441" title="DescribeNetworkAcl">DescribeNetworkAcl</a>.  |

## 5. Example
 
Input
<pre>
  https://vpc.api.qcloud.com/v2/index.php?Action=DescribeNetworkAcl
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
  &vpcId=vpc-erxok83l
  &networkAclId=acl-jk7weyp2

</pre>

Output
```

{
    "code": 0,
    "message": "",
    "totalCount": 3,
    "data": [
        {
            "vpcId": "gz_vpc_231",
            "unVpcId": "vpc-erxok83l",
            "networkAclName": "tttssass",
            "networkAclId": "acl-e9dbyl8s",
            "vpcName": "barry-uniqVpci",
            "vpcCidrBlock": "10.20.80.0\/24",
            "subnetNum": 0,
            "createTime": "2015-11-06 20:55:12",
            "networkAclEntrySet": {
                "egress": [
                    {
                        "desc": "",
                        "ipProtocol": "all",
                        "cidrIp": "0.0.0.0\/0",
                        "portRange": "ALL",
                        "action": 1
                    }
                ],
                "ingress": [
                    {
                        "desc": "",
                        "ipProtocol": "all",
                        "cidrIp": "0.0.0.0\/0",
                        "portRange": "ALL",
                        "action": 1
                    }
                ]
            }
        },
        {
            "vpcId": "gz_vpc_265",
            "unVpcId": "vpc-ktom9wg5",
            "networkAclName": "barrytt",
            "networkAclId": "acl-cva92t60",
            "vpcName": "yunapitest",
            "vpcCidrBlock": "10.100.100.0\/24",
            "subnetNum": 0,
            "createTime": "2015-11-04 10:37:07",
            "networkAclEntrySet": {
                "egress": [
                    {
                        "desc": "",
                        "ipProtocol": "all",
                        "cidrIp": "0.0.0.0\/0",
                        "portRange": "ALL",
                        "action": 1
                    }
                ],
                "ingress": [
                    {
                        "desc": "",
                        "ipProtocol": "all",
                        "cidrIp": "0.0.0.0\/0",
                        "portRange": "ALL",
                        "action": 1
                    }
                ]
            }
        },
        {
            "vpcId": "gz_vpc_76",
            "unVpcId": "vpc-03vihbk9",
            "networkAclName": "dddddUniq",
            "networkAclId": "acl-7gvd06dq",
            "vpcName": "pan-vpc2",
            "vpcCidrBlock": "10.100.2.0\/24",
            "subnetNum": 0,
            "createTime": "2015-10-22 18:23:29",
            "networkAclEntrySet": {
                "egress": [
                    {
                        "desc": "",
                        "ipProtocol": "all",
                        "cidrIp": "0.0.0.0\/0",
                        "portRange": "ALL",
                        "action": 1
                    }
                ],
                "ingress": [
                    {
                        "desc": "",
                        "ipProtocol": "all",
                        "cidrIp": "0.0.0.0\/0",
                        "portRange": "ALL",
                        "action": 1
                    }
                ]
            }
        }
    ]
}

```


