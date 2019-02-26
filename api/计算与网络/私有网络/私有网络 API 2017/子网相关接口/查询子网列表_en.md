## 1. API Description
 
This API (DescribeSubnetEx) is used to query the list of subnets.
Domain for API request:<font style="color:red">vpc.api.qcloud.com</font> 


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is DescribeSubnetEx.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | No | String | Virtual private cloud ID of the subnet, which can be vpcId or unVpcId. unVpcId is recommended. For example: vpc-kd7d06of. Can be queried via the API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  | 
| subnetId | No | String | Subnet ID assigned by the system. Both subnetId and unSubnetId are supported. unSubnetId is recommended. For example: subnet-3lzrkspo. |
| subnetName | No | String | Subnet name. Fuzzy query is supported.  |
| zoneIds | No | Array | Availability zone ID. Refer to <a href="https://cloud.tencent.com/doc/product/215/4927#.E5.8F.AF.E7.94.A8.E5.8C.BA.EF.BC.88zone.EF.BC.89">VPC Availability Zone Instruction</a> for details.  |
| offset | No | Int | Offset of initial line. Default is 0.  |
| limit | No | Int | Number of lines per page. Default is 20.  |
| orderField | No | String | Sort by a certain field. Currently, sorting by createTime (default) and subnetName is supported.  |
| orderDirection | No | String | Ascending (asc) or descending (desc). Default is desc.  |
| getAclIdFlag | No | Int | (Optional) Indicate whether display network Acl. 1: display. Default is 0.  |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Succeeded, other values:  Failed.  |
| message |  String | Error message.  |
| totalCount |  Int | Total number of subnets.  |
| data | Array  | Returned array.  |
| data.n.vpcId | String | vpcId assigned by the system, e.g. gz_vpc_266. |
| data.n.unVpcId | String | The new vpcID assigned by the system, which is upgraded from the subnet ID. It is recommended to use the new vpcId, for example: vpc-5gu2jxf4. |
| data.n.subnetId | String | Subnet ID assigned by the system. For example: subnetId_GZ_23. |
| data.n.unSubnetId | String | The new subnet ID assigned by the system, which is upgraded from the subnet ID. It is recommended to use the new subnet ID, for example: subnet-5gu2jxf4. |
| data.n.subnetName | String | Subnet name. |
| data.n.cidrBlock | String | Subnet network segment, for example: 192.168.0.0/25. |
| data.n.routeTableId | String | ID of the default routing table that is bound to the subnet. For example: gz_rtb_8751. |
| data.n.zoneId | String | ID of the availability zone in which the subnet resides. For example: 200001. |
| data.n.networkAclId | String | ID of the network ACL that is bound to the subnet (0 if there is no ACL bound to the subnet). For example: acl-e9dbyl8s. Refer to <a href="https://cloud.tencent.com/doc/api/245/1441" title="查询网络ACL"> Network ACL related APIs</a> for details. |
| data.n.vpcDevices | Int | Number of CVMs within the subnet. |
| data.n.totalIPNum | Int | Number of IPs within the subnet. |
| data.n.availableIPNum | Int | Number of available IPs within the subnet. |
| data.n.broadcast | Bool | Indicate whether broadcast is enabled. true: enabled; false: disabled. |

## 4. Error Code Table
The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error code | Description |
|---------|---------|
| InvalidVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify that the resource information you entered is correct. You can query the VPC via the API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| InvalidSubnet.NotFound | Invalid subnet. Subnet resource does not exist. Please verify that the resource information you entered is correct. You can query subnets via the API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E5%AD%90%E7%BD%91%E5%88%97%E8%A1%A8" title="DescribeSubnetEx">DescribeSubnetEx</a>.  |

## 5. Example
 
Input
<pre>
  https://vpc.api.qcloud.com/v2/index.php?Action=DescribeSubnetEx
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
  &subnetName=tttt
</pre>

Output

```
{
    "code": 0,
    "message": "",
    "totalCount": 1,
    "data": [
        {
            "vpcId": "gz_vpc_64",
            "unVpcId": "vpc-kd7d06of",
            "vpcName": "panpan-vpc1",
            "vpcCidrBlock": "10.0.0.0\/16",
            "subnetId": "gz_subnet_18748",
            "unSubnetId": "subnet-3lzrkspo",
            "subnetName": "tttt",
            "subnetCreateTime": "2015-11-13 12:06:26",
            "routeTableId": "gz_rtb_359",
            "unRouteTableId": "rtb-85alck92",
            "routeTableName": "222",
            "cidrBlock": "10.0.200.0\/24",
            "zoneIds": [800001],
            "vpcDevices": 0,
            "networkAclId": 0,
            "totalIPNum": 253,
            "availableIPNum": 253,
            "broadcast":false
        }
    ]
}
```


