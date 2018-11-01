## 1. API Description
This API (GetDnaptRule) is used to query NAT gateway port forwarding rules.
Domain for API request: vpc.api.qcloud.com

To use this API, please read <a href="https://cloud.tencent.com/doc/product/215/1682" title="NAT Gateway" >NAT Gateway Introduction</a> before you start

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to  [Common request parameters](https://intl.cloud.tencent.com/doc/api/229/6976). Action of this API is GetDnaptRule.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| vpcId | No | String | Virtual private cloud ID, for example: vpc-8e0ypm3z |
| natId | No | String | NAT gateway ID, for example: nat-dqbak2vy |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | int | Error code, 0:  Succeeded, other values:  Failed |
| message | string | Error message |

## 4. Error Codes
No specific error codes for this API. Please see <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a> to learn more about common error codes.

## 5. Sample Codes
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=GetDnaptRule
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameter</a>>
&vpcId=vpc-7zi2kcul
&natId=nat-2ro4wllo
</pre>
Output
```
{
  "code": 0,
  "message": "",
  "data": {
    "totalNum": 2,
    "detail": [
      {
        "eip": "139.199.230.14",
        "natId": 6792,
        "description": "test",
        "uniqVpcId": "vpc-7zi2kcul",
        "proto": "tcp",
        "pport": "6666",
        "eport": "8888",
        "owner": "1254332373",
        "vpcId": 533625,
        "pipType": 0,
        "pip": "10.0.0.6",
        "uniqNatId": "nat-2ro4wllo",
        "createTime": "2018-06-25 17:13:13"
      },
      {
        "eip": "118.126.105.102",
        "natId": 6792,
        "description": "test",
        "uniqVpcId": "vpc-7zi2kcul",
        "proto": "tcp",
        "pport": "1234",
        "eport": "1234",
        "owner": "1254332373",
        "vpcId": 533625,
        "pipType": 0,
        "pip": "10.0.1.4",
        "uniqNatId": "nat-2ro4wllo",
        "createTime": "2018-06-25 17:12:52"
      }
    ]
  }
}
```
