## Description
This API (DescribeBmNatBindSubnets) is used to query the information of the subnet bound to BM NAT gateway.

Domain name for API request: bmvpc.api.qcloud.com


## Request

### Request Example
```
GET https://bmvpc.api.qcloud.com/v2/index.php/?Action=DescribeBmNatBindSubnets
    &<Common request parameters>
    &natId=<NAT gateway ID>

```
### Request Parameter
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/document/product/386/6718" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is DescribeBmNatBindSubnets.

| Parameter | Description | Type | Required |
|---------|---------|---------|---------|
| natId | Unified NAT gateway ID, such as nat-xx454| String | Yes |



## Response
### Response Example
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": [
        {
            "natId": <Unified NAT gateway ID>,
            "unVpcId": <Unified VPC ID>,
            "vpcId": <VPC network ID>,
            "subnets.n.name": <Subnet name>,
			"subnets.n.unSubnetId": <Unified subnet ID>,
            "subnets.n.subnetId": <Subnet ID>,
            "subnets.n.subnetNatType": <Type of subnet bound>,
            "subnets.n.cidrBlock": <Information of subnet IP address range>
        }
    ]
}
```

## Response Parameters

| Parameter| Description | Type |
|---------|---------|---------|
| code | Error code. 0: Successful; other values: Failed | Int |
| message | Error message | String |
| data.n | Query the array of the information on the subnet bound to NAT gateway | Array |

`data` is composed as follows:

| Parameter  | Description | Type |
|---------|---------|---------|
| data.n.natId | Unified NAT gateway ID, such as nat-xx454 | String |
| data.n.unVpcId | Unified VPC ID, such as vpc-xgfd55d | String |
| data.n.vpcId | VPC ID | Int |
| data.n.subnets.n.name | Subnet name | String |
| data.n.subnets.n.name | Unified subnet ID | String |
| data.n.subnets.n.subnetId | Subnet ID | Int |
| data.n.subnets.n.subnetNatType | The type of subnet bound. 0: The subnet bound with partial IPs; 1: The subnet bound with all IPs | Int |
| data.n.subnets.n.cidrBlock | Information of subnet IP address range | String |



## Error Codes
 
| Error Code | Error Message | Error Description |
|---------|---------|---------|
| -3047 | InvalidBmVpc.NotFound | Invalid VPC. VPC resource does not exist. Verify whether the resource information you entered is correct. You can query the VPC via the API <a href="/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>. |
| 13014 | BmVpcNat.NotFound | Invalid NAT gateway. The NAT gateway resource does not exist. Verify whether the resource information you entered is correct. |

## Example

### Input
```
GET https://bmvpc.api.qcloud.com/v2/index.php?
	Action=DescribeBmNatBindSubnets
	&SecretId=AKID1ub7R1JoyBF7nHqjk7IH8nGWaR6Yezwd
	&Nonce=4557
	&Timestamp=1507692902
	&Region=gz
	&natId=nat-axd6t16w
	&Signature=4dq8JXWTyg9n8FuVckaIhg8Pnbw%3D
```

### Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "natId": "nat-axd6t16w",
        "unVpcId": "vpc-221ibyxt",
        "vpcId": 101211,
        "subnets": [
            {
                "name": "test",
                "unSubnetId": "subnet-5n0j08b2",
                "subnetId": 858,
                "subnetNatType": 1,
                "cidrBlock": "172.16.128.0/18"
            },
            {
                "name": "nat-test-123",
                "unSubnetId": "subnet-jbrwcpe6",
                "subnetId": 857,
                "subnetNatType": 0,
                "cidrBlock": "172.16.0.0/24"
            }
        ]
    }
}
```

