## 1. API Description
 
This API (DescribeVpcs) is used to query VPC details.
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>

 
## 2. Input Parameters
 The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, please see <a href="/doc/api/372/4153" title="Common request parameters">Common request parameters</a>. The Action field for this API is DescribeVpcs.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | No | String | VPC ID assigned by the system. Only the vpcId before the upgrade is supported, e.g., gz_vpc_226.  |

 

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| totalCount | Int | Total number of VPCs of the developer account. |
| vpcSet.n | Array | VPC information array. |
| vpcSet.n.vpcId | String | vpcId assigned by the system, e.g., gz_vpc_266.
| vpcSet.n.vpcName | String | VPC name. |
| vpcSet.n.cidrBlock | String | VPC IP address range, for example: 192.168.0.1/24. |
| vpcSet.n.subnetSet | Array | Subnet information under the VPC. |

vpcSet::subnetSet Structure

| Parameter Name | Type | Description |
|---------|---------|---------|
| subnetId | String | Subnet ID assigned by the system. For example: gz_subnet_1195. |
| subnetName | String | Subnet name. |
| cidrBlock | String | Subnet CIDR, for example: 192.168.0.1/25. |
| zoneId | Int | ID of the availability zone of the subnet, e.g., 100001. |

Data structure returned when vpcId is passed

| Parameter Name | Type | Description |
|---------|---------|---------|
| vpcId | String | vpcId assigned by the system. For example: gz_vpc_266. |
| vpcName | String | VPC name. |
| cidrBlock | String | VPC IP address range, for example: 10.0.0.0/16. |
| vpcCreateTime | String | VPC creation time, for example: 2015-11-06 11:33:52. |
| subnetSet.n | Array | Subnet information, which is returned when a subnet is added. |
| subnetSet.n.subnetId | String | Subnet ID assigned by the system. For example: subnetId_GZ_23. |
| subnetSet.n.subnetName | String | Subnet name. |
| subnetSet.n.routeTableId | String | ID of the default routing table that is bound to the subnet. For example: gz_rtb_8751. |
| subnetSet.n.cidrBlock | String | Subnet IP address range, for example: 192.168.0.0/25. |
| subnetSet.n.zoneId | String | ID of the availability zone in which the subnet resides. For example: 200001. |
| subnetSet.n.subnetCreateTime | String | Subnet creation time, for example: 2015-01-20 16:38:27. |
| routeTableSet.n | Array | Routing table information. By default, a subnet is associated with the default routing table. |
| routeTableSet.n.routeTableId | String | Routing table ID assigned by the system. For example: gz_rtb_8751. |
| routeTableSet.n.routeTableType | Int | Routing table type. 0: ordinary routing table; 1: default routing table. |
| routeTableSet.n.routeTableName | String | Routing table name. |

## 4. Error Codes
 The following error code list only provides the business logic error codes for this API. For common error codes, please see <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | The VPC does not exist. Please check the information you entered.  |

## 5. Example
 
Input
<pre>

  https://vpc.api.qcloud.com/v2/index.php?Action=DescribeVpcs
	&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
	&vpcId=gz_vpc_64
</pre>

Output
```

{
    "code": 0,
    "message": "",
    "vpcId": "gz_vpc_64",
    "vpcName": "panpan-vpc1",
    "cidrBlock": "10.0.0.0/16",
    "vpcCreateTime": "2015-01-20 16:38:27",
    "subnetSet": [
        {
            "subnetId": "gz_subnet_2036",
            "subnetName": "subnet1",
            "routeTableId": "gz_rtb_359",
            "cidrBlock": "10.0.0.0/24",
            "zoneId": 800001,
            "subnetCreateTime": "2015-01-20 16:38:27"
        },
        {
            "subnetId": "gz_subnet_18700",
            "subnetName": "barryUniq2",
            "routeTableId": "gz_rtb_359",
            "cidrBlock": "10.0.120.0/24",
            "zoneId": 800001,
            "subnetCreateTime": "2015-10-23 19:55:54"
        },
        {
            "subnetId": "gz_subnet_18748",
            "subnetName": "tttt",
            "routeTableId": "gz_rtb_359",
            "cidrBlock": "10.0.200.0/24",
            "zoneId": 800001,
            "subnetCreateTime": "2015-11-13 12:06:26"
        },
        {
            "subnetId": "gz_subnet_18699",
            "subnetName": "barryUniq1",
            "routeTableId": "gz_rtb_359",
            "cidrBlock": "10.0.80.0/24",
            "zoneId": 800001,
            "subnetCreateTime": "2015-10-23 19:52:40"
        }
    ],
    "routeTableSet": [
        {
            "routeTableId": "gz_rtb_359",
            "routeTableType": 1,
            "routeTableName": "222"
        },
        {
            "routeTableId": "gz_rtb_8750",
            "routeTableType": 0,
            "routeTableName": "tttt"
        }
    ]
}

```


