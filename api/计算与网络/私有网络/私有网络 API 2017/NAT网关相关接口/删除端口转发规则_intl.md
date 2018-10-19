## 1. API Description
This API (DeleteDnaptRule) is used to delete NAT gateway port forwarding rules.
Domain for API request: vpc.api.qcloud.com

To use this API, please read <a href="https://cloud.tencent.com/doc/product/215/1682" title="NAT Gateway" >NAT Gateway Introduction</a> before you start

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to  [Common request parameters](https://intl.cloud.tencent.com/doc/api/229/6976). Action of this API is DeleteDnaptRule.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| vpcId | No | String | Virtual private cloud ID, for example: vpc-8e0ypm3z |
| natId | No | String | NAT gateway ID, for example: nat-dqbak2vy |
| dnatList | Yes | array | The list of port forwarding rules you want to delete |
| dnatList.N.proto | Yes | string | Protocol, the value can be `tcp` or `udp` |
| dnatList.N.eip | Yes | string | External IP (associated EIP) |
| dnatList.N.eport | Yes | string | External port number |

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
https://vpc.api.qcloud.com/v2/index.php?Action=DeleteDnaptRule
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameter</a>>
&vpcId=vpc-d8vg6rev
&natId=nat-k6npdayk
&dnatList.0.proto=tcp
&dnatList.0.eip=139.199.232.178
&dnatList.0.eport=303
</pre>
Output
```
{
    "code":"0",
    "message":"",
}
```
