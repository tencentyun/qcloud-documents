## 1. API Description
 
This API (DescribeBmSubnetEx) is used to query the BM subnet list.
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font> 


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, please see <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is DescribeBmSubnetEx.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | No | String | ID of VPC to which the subnet belongs. It can be vpcId or unVpcId. unVpcId is recommended. For example: vpc-kd7d06of. It can be queried via the API <a href="http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  | 
| subnetId | No | String | Subnet ID assigned by the system. Both subnetId and unSubnetId are supported. unSubnetId is recommended. For example: subnet-3lzrkspo. |
| subnetName | No | String | Subnet name. Fuzzy query is supported.  |
| zoneIds | No | Array | Availability zone ID. For more information, please see <a href="">VPC Availability Zone Instruction</a>.  |
| offset | No | Int | Offset of initial line. Default is 0.  |
| limit | No | Int | Number of lines per page. Default is 20.  |
| orderField | No | String | Sort by a certain field. Currently, sorting by createTime (default) and subnetName is supported.  |
| orderDirection | No | String | Ascending order (asc) or descending order (desc). Default is asc.  |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded, other values: Failed.  |
| message | String | Error message.  |
| totalCount | Int | Total number of subnets.  |
| data | Array | Returned array.  |
| data.n.vpcId | String | vpcId assigned by the system, for example: gz_vpc_266. |
| data.n.unVpcId | String | The new vpcID assigned by the system, which is upgraded from the subnet ID. It is recommended to use the new vpcId, for example: vpc-5gu2jxf4. |
| data.n.subnetId | String | Subnet ID assigned by the system. For example: subnetId_GZ_23. |
| data.n.unSubnetId | String | The new subnet ID assigned by the system, which is upgraded from the subnet ID. It is recommended to use the new subnet ID, for example: subnet-5gu2jxf4. |
| data.n.subnetName | String | Subnet name. |
| data.n.cidrBlock | String | Subnet network segment, for example: 192.168.0.0/25. |
| data.n.zoneId | String | ID of the availability zone in which the subnet resides. For example: 200001. |

 ## 4. Error Codes
 
| Error Code | Error Message | Description |
|--------|---------|---------|
| -3047 | InvalidBmVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify whether the resource information entered is connect. You can query VPC through API <a href="http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeBmVpcEx</a>.  |
| -3030 | InvalidBmSubnet.NotFound | Invalid subnet. Subnet resource does not exist. Please verify that you have entered resource information correctly. It can be queried through API <a href="http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E5%AD%90%E7%BD%91%E5%88%97%E8%A1%A8" title="DescribeSubnetEx">DescribeBmSubnetEx</a>.  |

## 5. Example
 
Input
```
  https://vpc.api.qcloud.com/v2/index.php?Action=DescribeBmSubnetEx
  &<Common request parameters>
  &subnetName=tttt
```

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
            "cidrBlock": "10.0.200.0\/24",
            "zoneId": 800001
        }
    ]
}

```
