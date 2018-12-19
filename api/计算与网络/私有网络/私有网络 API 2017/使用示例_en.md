This document provides an exmple of creating a VPC.

Before creating a VPC, you should have a plan about your CIDR block. Once a VPC is created, its cidrBlock cannot be changed. For other details about creating a VPC, please see the related document.

To create a VPC, the Action field in common request parameter should be CreateVpc. The API request parameters include:

| Parameter | Description | Value |
|---------|---------|---------|
| vpcName | VPC name | 1-60 letters (upper-/lower-case), numbers and underlines |
| cidrBlock | VPC CIDR block | VPC IP address range. It can be 10.0.0.0/16, 172.16.0.0/16, 192.168.0.0/16 and their subnets. For details, please see VPC network segment planning introduction. |
| subnetSet.n |Subnet array | Optional |
| subnetSet.n.subnetName | Subnet name | 1-60 letters (upper-/lower-case), numbers and underlines |
| subnetSet.n.cidrBlock | Subnet segment | The subnet segment must be within the VPC network segment|
| subnetSet.n.zoneId | ID of availability zone | Refer to the introduction of availability zone |

The final request should be:

<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=CreateVpc
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
  &vpcName=bbbtest
  &cidrBlock=192.168.0.0/16
  &subnetSet.0.subnetName=wikitest
  &subnetSet.0.cidrBlock=192.168.1.0/24
  &subnetSet.0.zoneId=800001
</pre>

Result of the above request is as below, indicating that the ID of new created VPC is vpc-2ari9m7h.

```
{
    "code": 0,
    "message": "",
    "vpcId": "gz_vpc_266",
    "uniqVpcId": "vpc-2ari9m7h",
    "vpcCreateTime": "2015-11-06 11:33:52",
    "subnetSet": [
        {
            "subnetId": "gz_subnet_18720",
            "unSubnetId": "subnet-5gu2jxf4",
            "routeTableId": "gz_rtb_8751",
            "subnetName": "wikitest",
            "cidrBlock": "192.168.1.0/24",
            "zoneId": 800001
        }
    ],
    "routeTableSet": [
        {
            "routeTableId": "gz_rtb_8751",
            "routeTableType": 1,
            "routeTableName": "Default"
        }
    ]
}
```