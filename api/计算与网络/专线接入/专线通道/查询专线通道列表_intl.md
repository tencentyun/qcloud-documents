## Description
This API (DescribeDirectConnectTunnels) is used to query the list of direct connect tunnels.
Domain name: `dc.api.qcloud.com`


## Request Parameters
The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see the [Common Request Parameters](https://cloud.tencent.com/doc/api/229/6976) page. The Action field for this API is `DescribeDirectConnectTunnels`.

| Parameter | Required | Type | Description |
|---------|---------|---------|---------|
| directConnectId | No |  String | Direct connect ID</br>For example: dc-kd7d06of | 
| directConnectTunnelId | No | String | Direct connect tunnel ID</br>For example: dcx-kd7d0125 | 

## Response Parameters

| Parameter | Type | Description |
|---------|---------|---------|
| code| Int | Error code</br>0: Successful</br>Other values: Failed |
| message |  String | Error message |
| data.n | Array  | Returned array |
| data.n.directConnectTunnelId | String | Direct connect tunnel ID assigned by the system</br>For example: dcx-kd7d0125 |
| data.n.directConnectTunnelName | String | Direct connect tunnel name |
| data.n.directConnectId | String | Direct connect ID assigned by the system</br>For example: dc-kd7d06of |
| data.n.ownerAccount | String | Developer account ID of the direct connect |
| data.n.networkType | Int | Network type. Default is 0.</br>0: VPC</br>1: BM network |
| data.n.region | String | Network region |
| data.n.vpcId | String | Unified ID of VPC/BM network |
| data.n.directConnectGatewayId | String | Direct connect gateway ID, for example: dcg-d545ddf |
| data.n.bandwidth | Int | Direct connect bandwidth (in Mbps) |
| data.n.routeMode | Int | 0: BGP routing</br>1: Static routing</br>Default is BGP routing. |
| data.n.bgpPeers.asn | string | BGP ASN |
| data.n.bgpPeers.authKey | String | BGP key |
| data.n.routeFilterPrefixes.n.cidr | String | Peer IP address range |
| data.n.status | Int | Status of the direct connect tunnel</br>0: Connected</br>1: Requesting</br>2: Configuring</br>6: Configured</br>20: Waiting for connection</br>21: Rejected |
| data.n.vlan | Int | vlan Id |
| data.n.localGatewayIp | String | Tencent's IP |
| data.n.peerGatewayIp | String | Customer's IP |
| data.n.peeringSubnetMask | String | The mask of interconnection IP</br>For example: 255.255.255.252 |
| data.n.remark | String | Notes |

## Sample Code
 
### Request example
```
  GET https://dc.api.qcloud.com/v2/index.php?Action=DescribeDirectConnectTunnels
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">common request parameters</a>>
  &directConnectId=dc-kd7d06of

```

### Response example
```
{
    "code": 0,
    "message": "",
    "data": [
        {
            "directConnectTunnelId": "dcx-2nakhj58",
            "directConnectTunnelName": "barrytest2",
            "directConnectId": "dc-5e8ak079",
            "networkType": 1,
            "ownerAccount": "",
            "region": "gz",
            "vpcId": "vpc-kx49lmyv",
            "bandwidth": 0,
            "routeMode": 0,
            "bgpPeers": {
                "asn": "10",
                "authKey": "124545d"
            },
            "routeFilterPrefixes": [
                {
                    "cidr": ""
                }
            ],
            "status": 1,
            "vlan": 0,
            "localGatewayIp":"169.254.64.1",
            "peerGatewayIp":"169.254.64.2",
            "peeringSubnetMask":"255.255.255.252",
            "remark": ""
        }
    ]
}
```


