## 1. API Description

This API (DescribeBmNatGateway) is used to query BM NAT gateway
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is DescribeNatGateway

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| natId | No | String | Unified ID of NAT gateway, for example: nat-xx454 |
| natName | No | String | NAT gateway name (supports fuzzy query) |
| vpcId | No | String | VPC ID, which can be vpcId or unVpcId. unVpcId is recommended. For example: vpc-kd7d06of. You can query this through API <a href="https://www.qcloud.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>. |
| offset | No | Int | Offset of initial line. Default is 0 |
| limit | No | Int | Number of lines per page. Default is 20. Maximum is 50. |
| orderField | No | String | Sort by a certain field. No sorting by default. <br>Available field: natId. |
| orderDirection | No | String | Ascending order (asc) or descending order (desc). Default is desc. |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | int | Error code, 0:  Successful; other values:  Failed |
| message | string | Error message |
| totalCount | int | Total number of queried NAT gateways |
| data.n | array | Information array of queried NAT gateways |

**data is composed as follows:**

| Parameter Name | Type | Description |
|---------|---------|---------|
| data.n.natId | string | Unified ID of NAT gateway, for example: nat-xx454 |
| data.n.vpcId | Int | VPC ID |
| data.n.unVpcId | string | Unified ID of VPC, for example: vpc-xgfd55d |
| data.n.natName | string | NAT gateway name |
| data.n.state | int | NAT gateway status, 1: Running, 0: Unavailable |
| data.n.maxConcurrent | int | Maximum gateway concurrent connections. Values: 1,000,000 (small), 3,000,000 (medium), 10,000,000 (large). For more information, please see <a href="">NAT Gateway Product Overview</a> |
| data.n.eipCount | string | Unified ID of NAT gateway, for example: nat-xx454 |
| data.n.eipSet | array | All of the EIP information of the gateway, for example:[183.60.249.11] |
| data.n.createTime | string | Creation time of NAT gateway, for example: 2016-06-21 12:01:23 |
| data.n.productionStatus | int | Production status of NAT gateway, 0:  Creating, 1:  Creation successful, 2:  Creation failed |
| data.n.subnetAll | int | Whether the option of "New subnet (including the subsequent ones)" is selected |
| data.n.subnets | array | List of subnets bound to NAT gateway |

 ## 4. Error Codes
 The following error codes only include the business logic error codes for this API. For additional common error codes, please see <a href="https://www.qcloud.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error Code | Error Message | Error Description |
|---------|---------|---------|
| -3047 | InvalidBmVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify whether the resource information entered is correct. You can query VPC through API <a href="https://www.qcloud.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>.  |
| 13014 | BmVpcNat.NotFound | Invalid NAT gateway. NAT gateway resource does not exist. Please verify whether the resource information entered is correct. You can query the NAT gateway through API DescribeBmNatGateway |  |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DescribeBmNatGateway
&<<a href="https://www.qcloud.com/doc/api/229/6976">Public Request Parameters</a>>
&vpcId=vpc-8e0ypm3z
</pre>
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "totalCount": 1,
    "data": [
        {
            "natId": "nat-787jwhek",
            "natName": "testnat",
            "unVpcId": "vpc-34cxlz7z",
            "vpcId": 4097,
            "vpcName": "test",
            "state": 0,
            "productionStatus": 1,
            "eipCount": 4,
            "eipSet": [
                "115.159.240.68",
                "115.159.240.83",
                "115.159.240.86",
                "115.159.240.96"
            ],
            "maxConcurrent": 1000000,
            "ntype": "small",
            "subnetAll": "0",
            "createTime": "2017-05-10 20:13:00",
            "subnets": [
                {
                    "name": "vm",
                    "unSubnetId": "subnet-jv24ivq0",
                    "subnetId": 8946
                }
            ]
        }
    ]
}
```


