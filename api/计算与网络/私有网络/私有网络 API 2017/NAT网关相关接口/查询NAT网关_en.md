## 1. API Description

This API (DescribeNatGateway) is used to query NAT gateway
Domain for API request:vpc.api.qcloud.com


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| natId | No | String | Unified ID of NAT gateway, for example: nat-xx454 |
| natName | No | String | NAT gateway name (supports fuzzy query) |
| vpcId | No | String | Virtual private cloud ID or unified ID (unified ID is recommended), for example: vpc-dfdg42d |
| offset | No | Int | Offset of initial line. Default is 0 |
| limit | No | Int | Number of lines per page. Default is 20, maximum is 50. |
| orderField | No | String | Sorting by a certain field. No sorting by default. <br>Support field: natId |
| orderDirection | No | String | Ascending (asc) or descending (desc). Default is desc |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | int | Error code, 0:  Succeeded, other values:  Failed |
| message | string | Error message |
| totalCount | int | Total number of queried NAT gateways |
| data.n | array | Information array of queried NAT gateways |

**Details of `data.n`:**

| Parameter Name | Type | Description |
|---------|---------|---------|
| data.n.natId | string | Unified ID of NAT gateway, for example: nat-xx454 |
| data.n.vpcId | string | VPC unified ID, for example: vpc-xgfd55d |
| data.n.natName | string | NAT gateway name |
| data.n.state | int | NAT gateway status, 0: Running, 1: Unavailable, 2: Be in arrears and out of service |
| data.n.maxConcurrent | int | The limit of concurrent connection of NAT gateway. 1 million: small-sized; 300 million: medium-sized; 10 million: large-sized. For more information, refer to <a href="">Introduction to NAT Gateway</a> |
| data.n.bandwidth | int | The maximum public network output bandwidth of the gateway (unit: Mbps). For more information, refer to <a href="">Introduction to NAT Gateway</a> |
| data.n.eipCount | string | Unified ID of NAT gateway, for example: nat-xx454 |
| data.n.eipSet | array | All of the EIP information of the gateway, for example:[183.60.249.11] |
| data.n.createTime | string | Creation time of NAT gateway, for example: 2016-06-21 12:01:23 |
| data.n.productionStatus | int | Production status of NAT gateway, 0:  Creating, 1:  Created successfully, 2:  Failed to create, 3:  Changing, 4:  Failed to change, 5:  Deleting, 6:  Failed to delete |

## 4. Error Codes
 The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify that the resource information you entered is correct. You can query the VPC via the <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a> API |
| InvalidNatGatewayId.NotFound | Invalid NAT gateway, NAT gateway resource does not exist. Please verify that the resource information you entered is correct. You can query the NAT gateway via the <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2NAT%e7%bd%91%e5%85%b3?viewType=preview" title="DescribeNatGateway">DescribeNatGateway</a> API |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DescribeNatGateway
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&vpcId=vpc-8e0ypm3z
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "totalCount":1
    "data": [
        {
            "appId": "1351000042",
            "vpcId": "vpc-8e0ypm3z",
            "vpcName": "alblack.bbb1",
            "natId": "nat-dhfpwhtm",
            "natName": "apollan",
            "maxConcurrent": 0,
            "eipCount": 1,
            "createTime": "2016-06-21 12:01:23",
            "state": 1,
            "bandwidth": 90000,
            "productionStatus": 1,
            "eipSet": [
                "183.60.249.11"
            ]
        }
     ]
}
```


