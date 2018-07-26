## 1. API Description
This API (AddDnaptRule) is used to add NAT gateway port forwarding rules.
Domain for API request: vpc.api.qcloud.com

To use this API, please read <a href="https://cloud.tencent.com/doc/product/215/1682" title="NAT Gateway" >NAT Gateway Introduction</a> before you start

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to  [Common request parameters](https://intl.cloud.tencent.com/doc/api/229/6976). Action of this API is AddDnaptRule.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| vpcId | No | String | Virtual private cloud ID, for example: vpc-8e0ypm3z |
| natId | No | String | NAT gateway ID, for example: nat-dqbak2vy |
| proto | Yes | string | Protocol, the value can be`tcp` or `udp` |
| eip | Yes | string | External IP (associated EIP)|
| eport | Yes | string | External port number |
| pip | Yes | string | Internal IP |
| pport | Yes | string | Internal port number |
| description | Yes | string | Rule description |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | int | Error code, 0:  Succeeded, other values:  Failed |
| message | string | Error message |


## 4. Error Codes
Only error codes for this API are listed below. Please see <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a> to learn more about common error codes.

| Code | Description |
|---------|---------|
| 29151 | The rule description is too long|
| 29152 | This EIP already exists|
| 29153 | The internal IP is not associated with any instance|
| -3325 | The EIP does not exsit|
| -3326 | The internal IP is not in the VPC|
| -3327 | This internal IP already exists|
| -3328 | Reached the upper limit of port forwarding rules|
| -3344 | The internal IP is not associated with the server|

## 5. Sample Codes
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=AddDnaptRule
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common Request Parameters</a>>
&vpcId=vpc-d8vg6rev
&natId=nat-k6npdayk
&proto=tcp
&eip=139.199.232.178
&eport=303
&pip=10.90.90.10
&pport=303
&description=aaa
</pre>
Output
```
{
    "code":"0",
    "message":"",
}
```
