## Description
 
This API (CreateDirectConnectTunnel) is used to create a Direct Connect tunnel.
Domain name for API request: dc.api.qcloud.com 

## Request

Syntax:
```
GET https://dc.api.qcloud.com/v2/index.php?Action=CreateDirectConnectTunnel
  &<Common request parameters>
  &directConnectId=dc-kd7d06of
  &directConnectTunnelName=baytest
  regionion=gz
  &vpcId=vpc-df3dfdf
  &directConnectGatewayId=dcg-34drdere
```

### Request Parameter

The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is CreateDirectConnectTunnel.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| directConnectId | Yes | String | Direct Connect ID, such as: dc-kd7d06of. | 
| directConnectTunnelName | Yes | String | Direct Connect tunnel name. | 
| ownerAccount | No | String | Physical Direct Connect owner. Default is the current customer (physical Direct Connect owner). You need to enter a developer account ID of the shared Direct Connect when sharing a Direct Connect. |
| networkType | No | Int | Network type. 1: VPC; 0: BM network. Default is 1. |
| region | Yes | String | Network region. |
| vpcId | Yes | String | Unified VPC ID or unified BM network ID. |
| directConnectGatewayId | Yes | String | Direct Connect gateway ID, such as dcg-d545ddf. |
| bandwidth | No | Int | Direct connect bandwidth (in Mbps). 0 indicates no limit. |
| routeMode | No | Int | 0:BGP routing. 1: static. Default is BGP routing. |
| bgpPeers.asn | No | String | BGP asn. |
| bgpPeers.authKey | No | String | BGP key. |
| routeFilterPrefixes.n.cidr | No | String | Peer IP address range. |
| vlanId | Yes | Int | vlanId, 0: Do not enable sub API. Value range: 0-3000. |
| localGatewayIp | No | String | Tencent Ip |
| peerGatewayIp | No | String | user's Idc Ip |
| peeringSubnetMask | No | String | ip mask, eg, 255.255.255.252|
| remark | No | String | Remarks. |


## Response
Response Example:
```
{
    "code": 0,
    "message": ""
}
```
### Response Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Successful; other values: Failed. |
| message | String | Error message. |


### Response Error Codes
The following error codes only include the business logic error codes for this API. For additional common error codes, please see <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error Code | Description |


## Practical Case
 
### Request
```
  GET https://dc.api.qcloud.com/v2/index.php?Action=CreateDirectConnectTunnel
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
  &directConnectId=dc-kd7d06of
  &directConnectTunnelName=baytest
  &region=gz
  &vpcId=vpc-df3dfdf
  &directConnectGatewayId=dcg-34drdere
  &vlanId=400
```
### Response

```
{
    "code": 0,
    "message": ""
}
```


