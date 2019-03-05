## 1. API Description
 
This API (DescribeBmSubnetEx) is used to query the list of BM subnets.  
Domain name for API request: bmvpc.api.qcloud.com


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is DescribeBmSubnetEx.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | No | String | ID of VPC to which the subnet belongs, which can be vpcId or unVpcId. unVpcId is recommended. For example: vpc-kd7d06of. You can query this through API <a href="https://cloud.tencent.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>.  |
| subnetId | No | String | Subnet ID assigned by the system. Both subnetId and unSubnetId are supported. unSubnetId is recommended. For example: subnet-3lzrkspo. |
| subnetName | No | String | Subnet name. Fuzzy query is supported.  |
| zoneIds | No | Array | Availability zone ID. For more information, please see <a href="https://cloud.tencent.com/document/api/386/6633">VPC Availability Zone Overview</a>.  |
| offset | No | Int | Offset of initial line. Default is 0.  |
| limit | No | Int | Number of lines per page. Default is 20.  |
| orderField | No | String | Sort by a certain field. Currently, sorting by createTime (default) and subnetName is supported.  |
| orderDirection | No | String | Ascending (asc) or descending (desc). Default is asc.  |
| vlanId | No | Int | Subnet VLAN ID.  |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Successful; other values:  Failed.  |
| message |  String | Error message.  |
| totalCount |  Int | Total number of subnets.  |
| data | Array  | Returned array.  |
| data.n.vpcId | Int | The VPC ID assigned by the system, e.g. 10001. |
| data.n.unVpcId | String | The new VPC ID assigned by the system, which is upgraded from the subnet ID. It is recommended to use the new VPC ID, for example: vpc-5gu2jxf4. |
| data.n.subnetId | int | Subnet ID assigned by the system. For example: 23. |
| data.n.unSubnetId | String | The new subnet ID assigned by the system, which is upgraded from the subnet ID. It is recommended to use the new subnet ID, for example: subnet-5gu2jxf4. |
| data.n.subnetName | String | Subnet name. |
| data.n.cidrBlock | String | Subnet IP address range, for example: 192.168.0.0/25. |
| data.n.zoneId | String | ID of the availability zone in which the subnet resides. For example: 200001. |
| data.n.vlanId | Int | Subnet VLAN ID. |

## 4. Error Codes
 
| Error Code | Error Message | Description |
|--------|---------|---------|
| -3047 | InvalidBmVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify whether the resource information entered is correct. You can query the VPC through API <a href="https://cloud.tencent.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>.  |
| -3030 | InvalidBmSubnet.NotFound | Invalid subnet. Subnet resource does not exist. Please verify whether the resource information entered is correct. You can query the subnet through API <a href="https://cloud.tencent.com/document/api/386/6648" title="DescribeBmSubnetEx">DescribeBmSubnetEx</a>.  |

## 5. Example
 
Input
```
  https://vpc.api.qcloud.com/v2/index.php?Action=DescribeBmSubnetEx
  &<Common Request Parameters>
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
            "vpcId": 10001,
            "unVpcId": "vpc-kd7d06of",
            "vpcName": "panpan-vpc1",
            "vpcCidrBlock": "10.0.0.0\/16",
            "subnetId": "18748",
            "unSubnetId": "subnet-3lzrkspo",
            "subnetName": "tttt",
            "subnetCreateTime": "2015-11-13 12:06:26",
            "cidrBlock": "10.0.200.0\/24",
            "zoneId": 800001,
            "vlanId":5
        }
    ]
}

```
