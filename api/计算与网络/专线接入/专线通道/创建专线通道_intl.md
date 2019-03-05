## API Description
This API (CreateDirectConnectTunnel) is used to create a direct connect tunnel.
Domain Name: `dc.api.qcloud.com`


## Request Parameters
The following request parameter list only provides API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/doc/api/229/6976). The Action field for this API is `CreateDirectConnectTunnel`.

| Parameter  | Required   | Type  | Description  |
|---------|---------|---------|---------|
| directConnectId | Yes | String | Direct connect ID, for example: dc-kd7d06of | 
| directConnectTunnelName | Yes | String | Direct connect tunnel name | 
| ownerAccount | No | String | Physical direct connect owner. Default is the current customer (physical direct connect owner).</br>To share the direct connect, please enter the account ID of the developer who shares the direct connect. |
| networkType | No | Int | Network type. Default is 1.</br>1: VPC</br>0: BM network |
| region | Yes | String | Network region |
| vpcId | Yes | String | Unified ID of VPC/BM network |
| directConnectGatewayId | Yes | String | Direct connect gateway ID, for example: dcg-d545ddf |
| bandwidth | No | Int | Direct connect bandwidth (in Mbps)</br>0: Unlimited |
| routeMode | No | Int | 0: BGP routing</br>1: Static routing</br>Default is BGP routing. |
| bgpPeers.asn | No | String | BGP asn |
| bgpPeers.authKey | No | String | BGP key |
| routeFilterPrefixes.n.cidr | No | String | Peer IP address range |
| vlanId | Yes | Int | vlanId. Value range: 0-3000</br>0: Disable sub-API |
| localGatewayIp | No | String | localGatewayIp, Tencent's IP |
| peerGatewayIp | No | String | peerGatewayIp, user's IP |
| peeringSubnetMask | No | String | The mask of interconnection IP, which must be defined in the same subnet. It supports **24-30** bits, and is represented in dotted decimal notation, for example: 255.255.255.252 |
| remark | No | String | Notes |
 
## Response Parameters
| Parameter | Type | Description |
|---------|---------|---------|
| code| Int | Error code</br>0: Successful</br>Other values: Failed |
| message | String | Error message |
|directConnectTunnelId| String | Direct connect tunnel ID |

## Sample Code
### Request example
```
  GET https://dc.api.qcloud.com/v2/index.php?Action=CreateDirectConnectTunnel
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">common request parameters</a>>
  &directConnectId=dc-kd7d06of
  &directConnectTunnelName=baytest
  &region=gz
  &vpcId=vpc-abcdefg
  &directConnectGatewayId=dcg-abcdefg
  &vlanId=400
  &routeMode=1
  &routeFilterPrefixes.0.cidr=172.256.12.0/24
  &routeFilterPrefixes.1.cidr=172.256.13.0/24
  &localGatewayIp=169.254.64.1
  &peerGatewayIp=169.254.64.2
  &peeringSubnetMask=255.255.255.252
  &remark=create
```
### Response example

```
{
    "code": 0,
    "message": ""
    "directConnectTunnelId":""
}
```


