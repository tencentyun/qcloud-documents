## 1. API Description

This API (DescribeRouteTable) is used to query routing table.
Domain for API request:<font style="color:red">vpc.api.qcloud.com</font>


## 2. Input Parameters
 
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>.  The Action field for this API is DescribeRouteTable.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| vpcId | No | String | ID of VPC to which the subnet belongs. This can be vpcId or unVpcId. unVpcId is recommended. For example, vpc-0ox8fuhw.  It can be queried through API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.   |
| routeTableId | No | String | The routing table ID assigned by the system, which can be routeTableId or unRouteTableId. unRouteTableId is recommended. For example, rtb-0ox8fuhw. It can be queried through API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E8%B7%AF%E7%94%B1%E8%A1%A8" title="DescribeRouteTable">DescribeRouteTable</a>.  |
| routeTableName | No | String | Routing table name. Fuzzy query is supported.   |
| offset | No | Int | Offset of initial line. Default is 0.   |
| limit | No | Int | Number of lines per page. Default is 20, maximum is 50.  |
| orderField | No | String | Sort by a certain field. Currently, sorting by createTime (default) and routeTableName is supported.   |
| orderDirection | No | String | Ascending order (asc) or descending order (desc). Default is desc.   |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:   Succeeded, other values:   Failed.   |
| message |  String | Error message.   |
| totalCount | Int | Total number of routes in the query result.   |
| data.n | Array | Returned array.   |
| data.n.vpcId | String | VPC ID assigned by the system, for example, gz_vpc_8849.   |
| data.n.unVpcId | String | New VPC ID assigned by the system. New ID is recommended, for example, vpc-0ox8fuhw.   |
| data.n.routeTableId | String | The routing table ID assigned by the system, for example, gz_rtb_8849.   |
| data.n.unRouteTableId | String | New routing table ID assigned by the system. New ID is recommended. For example, rtb-0ox8fuhw.   |
| data.n.routeTableName | String  | Routing table name.   |
| data.n.routeTableType | Int  | Type of routing table. 0: ordinary routing table; 1: default routing table. For details on the differences between default routing table and ordinary routing table, refer to <a href="" title="Routing Table Product Overview">Routing Table Product Overview</a>.   |
| data.n.routeTableCreateTime | String  | Creation time of routing table, for example: 2015-11-06 17:50:21.   |
| data.n.subnetNum | Int  | Number of associated subnets.   |
| data.n.routeTableSet.n | Array  | An array of routing policy information.   |

routeTableSet Routing Policy Information Array 

| Parameter Name | Type | Description |
|---------|---------|---------|
| routeTableSet.n.destinationCidrBlock | string  | Destination network segment, which cannot be within VPC network segment. For example, 112.20.51.0/24.   |
| routeTableSet.n.nextType | string  | Type of next hop. Supported types: 0: public network gateway; 1: VPN gateway; 3: Direct Connect gateway; 4: peering connection; 7: sslvpn; 8: NAT gateway; 9: general cvm.   |
| routeTableSet.n.nextHub | string  | Next hop address. You just need to specify gateway IDs (new ID is recommended) of different next hop types and the system will automatically match to the next hop address.  |
| routeTableSet.n.unNextHub | string  | Unique ID of next hop address. It is recommended to use the unified ID.   |
| routeTableSet.n.description | string  | Route description.   |
 
## 4. Error Codes
 The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>. 

| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound |VPC not exist. Please check the information you entered. You can query VPC through API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  | 
| InvalidRouteTableId.NotFound | Routing table ID not exist. Please check the information you entered. It can be queried through API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E8%B7%AF%E7%94%B1%E8%A1%A8" title="DescribeRouteTable">DescribeRouteTable</a>.  | 
 
## 5. Example
 
Input
<pre>
  https://vpc.api.qcloud.com/v2/index.php?Action=DescribeRouteTable
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
  &vpcId=vpc-amhnnao5
  &routeTableName=tttt111
</pre>

Output
```

{
    "code": 0,
    "message": "",
    "totalCount": 114,
    "data": [
        {
            "vpcId": "gz_vpc_99",
            "unVpcId": "vpc-amhnnao5",
            "vpcName": "pan-vpc25",
            "vpcCidrBlock": "10.100.25.0\/24",
            "routeTableName": "tttt111",
            "routeTableId": "gz_rtb_8755",
            "unRouteTableId": "rtb-rqndayhs",
            "routeTableType": 0,
            "subnetNum": 1,
            "routeTableCreateTime": "2015-11-06 17:50:21",
            "routeSet": [
                {
                    "destinationCidrBlock": "Local",
                    "nextType": 2,
                    "nextHub": "Local"
                },
                {
                    "destinationCidrBlock": "121.0.0.0\/16",
                    "nextType": 1,
                    "nextHub": "548"
                }
            ]
        },
        {
            "vpcId": "gz_vpc_266",
            "unVpcId": "vpc-2ari9m7h",
            "vpcName": "bbbtest",
            "vpcCidrBlock": "192.168.0.0\/24",
            "routeTableName": "default",
            "routeTableId": "gz_rtb_8751",
            "unRouteTableId": "rtb-ggovmles",
            "routeTableType": 1,
            "subnetNum": 0,
            "routeTableCreateTime": "2015-11-06 11:33:52",
            "routeSet": [
                {
                    "destinationCidrBlock": "Local",
                    "nextType": 2,
                    "nextHub": "Local"
                }
            ]
        },
        {
            "vpcId": "gz_vpc_64",
            "unVpcId": "vpc-kd7d06of",
            "vpcName": "panpan-vpc1",
            "vpcCidrBlock": "10.0.0.0\/16",
            "routeTableName": "tttt",
            "routeTableId": "gz_rtb_8750",
            "unRouteTableId": "rtb-dy09eb46",
            "routeTableType": 0,
            "subnetNum": 0,
            "routeTableCreateTime": "2015-11-02 16:58:53",
            "routeSet": [
                {
                    "destinationCidrBlock": "Local",
                    "nextType": 2,
                    "nextHub": "Local"
                }
            ]
        },
        {
            "vpcId": "gz_vpc_265",
            "unVpcId": "vpc-ktom9wg5",
            "vpcName": "yunapitest",
            "vpcCidrBlock": "10.100.100.0\/24",
            "routeTableName": "default",
            "routeTableId": "gz_rtb_8747",
            "unRouteTableId": "rtb-fdyy7v1o",
            "routeTableType": 1,
            "subnetNum": 1,
            "routeTableCreateTime": "2015-10-30 16:10:49",
            "routeSet": [
                {
                    "destinationCidrBlock": "Local",
                    "nextType": 2,
                    "nextHub": "Local"
                }
            ]
        },
        {
            "vpcId": "gz_vpc_260",
            "unVpcId": "vpc-r4wc72kt",
            "vpcName": "oplogtest",
            "vpcCidrBlock": "10.100.180.0\/24",
            "routeTableName": "default",
            "routeTableId": "gz_rtb_8738",
            "unRouteTableId": "rtb-cfqwtvs4",
            "routeTableType": 1,
            "subnetNum": 1,
            "routeTableCreateTime": "2015-10-23 19:47:54",
            "routeSet": [
                {
                    "destinationCidrBlock": "Local",
                    "nextType": 2,
                    "nextHub": "Local"
                }
            ]
        },
        {
            "vpcId": "gz_vpc_180",
            "unVpcId": "vpc-cor5n2a5",
            "vpcName": "test",
            "vpcCidrBlock": "10.100.181.0\/24",
            "routeTableName": "default",
            "routeTableId": "gz_rtb_8730",
            "unRouteTableId": "rtb-hrjfw07c",
            "routeTableType": 1,
            "subnetNum": 1,
            "routeTableCreateTime": "2015-10-22 12:11:22",
            "routeSet": [
                {
                    "destinationCidrBlock": "Local",
                    "nextType": 2,
                    "nextHub": "Local"
                },
                {
                    "destinationCidrBlock": "10.0.0.0\/8",
                    "nextType": 3,
                    "nextHub": "4245"
                },
                {
                    "destinationCidrBlock": "10.100.2.0\/24",
                    "nextType": 3,
                    "nextHub": "4245"
                },
                {
                    "destinationCidrBlock": "172.0.0.0\/8",
                    "nextType": 3,
                    "nextHub": "4245"
                }
            ]
        },
        {
            "vpcId": "gz_vpc_248",
            "unVpcId": "vpc-ali73gtr",
            "vpcName": "pan-vpc180",
            "vpcCidrBlock": "10.100.180.0\/24",
            "routeTableName": "default",
            "routeTableId": "gz_rtb_8729",
            "unRouteTableId": "rtb-m5es14q4",
            "routeTableType": 1,
            "subnetNum": 1,
            "routeTableCreateTime": "2015-10-22 11:25:51",
            "routeSet": [
                {
                    "destinationCidrBlock": "Local",
                    "nextType": 2,
                    "nextHub": "Local"
                }
            ]
        },
        {
            "vpcId": "gz_vpc_231",
            "unVpcId": "vpc-erxok83l",
            "vpcName": "barry-uniqVpci",
            "vpcCidrBlock": "10.20.80.0\/24",
            "routeTableName": "apollolan121",
            "routeTableId": "gz_rtb_8724",
            "unRouteTableId": "rtb-5qaib2em",
            "routeTableType": 0,
            "subnetNum": 0,
            "routeTableCreateTime": "2015-10-19 19:50:38",
            "routeSet": [
                {
                    "destinationCidrBlock": "Local",
                    "nextType": 2,
                    "nextHub": "Local"
                }
            ]
        },
        {
            "vpcId": "gz_vpc_231",
            "unVpcId": "vpc-erxok83l",
            "vpcName": "barry-uniqVpci",
            "vpcCidrBlock": "10.20.80.0\/24",
            "routeTableName": "default",
            "routeTableId": "gz_rtb_8720",
            "unRouteTableId": "rtb-3jdtm2uk",
            "routeTableType": 1,
            "subnetNum": 1,
            "routeTableCreateTime": "2015-10-19 11:36:00",
            "routeSet": [
                {
                    "destinationCidrBlock": "Local",
                    "nextType": 2,
                    "nextHub": "Local"
                }
            ]
        },
        {
            "vpcId": "gz_vpc_174",
            "unVpcId": "vpc-gaep0rmx",
            "vpcName": "pan-vpc99",
            "vpcCidrBlock": "10.100.99.0\/24",
            "routeTableName": "default",
            "routeTableId": "gz_rtb_481",
            "unRouteTableId": "rtb-d1voj30m",
            "routeTableType": 1,
            "subnetNum": 1,
            "routeTableCreateTime": "2015-01-30 14:21:19",
            "routeSet": [
                {
                    "destinationCidrBlock": "Local",
                    "nextType": 2,
                    "nextHub": "Local"
                }
            ]
        }
    ]
}

```


