## Description
This API (ModifyDirectConnectTunnel) is used to modify the parameters of a direct connect tunnel.
Domain name: `dc.api.qcloud.com`


## Request Parameters
| Parameter | Type | Required | Description |
| --------------------| ------| --------| -----------  | 
| directConnectTunnelId | String | Yes | Direct connect tunnel ID</br>For example: dcx-abcdefgh | 
| directConnectTunnelName | String | No | Direct connect tunnel name | 
| peerAsn | Int | No | Customer's BGP asn |
| authKey | String | No | Customer's BGP key |
| routeFilterPrefixes.n.cidr | String | No | Customer's peer IP address range</br>For example: 169.254.0.0/28 |
| localGatewayIp | String | No | localGatewayIp, Tencent's interconnection IP |
| peerGatewayIp | String | No | peerGatewayIp, customer's interconnection IP |
| peeringSubnetMask | String | No | The mask of interconnection IP, which must be defined in the same subnet. It supports **24-30** bits, and is represented in dotted decimal notation, for example: 255.255.255.252 |

## Response Parameters
| Parameter | Type | Description |
|---------|---------|---------|
| code| Int | Error code</br>0: Successful</br>Other values: Failed |
| message |  String | Error message |

## Sample Code
 
### Request example
```
  GET https://dc.api.qcloud.com/v2/index.php?Action=DeleteDirectConnectTunnel
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">common request parameters</a>>
  &directConnectTunnelId=dcx-abcdefgh
  &bandwidth=10
  &routeFilterPrefixes.0.cidr=172.256.12.0/24
  &routeFilterPrefixes.1.cidr=172.256.13.0/24
  &localGatewayIp=169.254.64.1
  &peerGatewayIp=169.254.64.2
  &peeringSubnetMask=255.255.255.252
```
### Response example
```
{
    "code": 0,
    "message": ""
}
```


