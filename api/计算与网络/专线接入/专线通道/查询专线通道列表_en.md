## Description
 
This API (DescribeDirectConnectTunnels) is used to query the Direct Connect tunnel list.
Domain name for API request: `dc.api.qcloud.com`

## Request Parameter

The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/377/4153) page. The Action field for this API is DescribeDirectConnectTunnels.

| Parameter  | Required | Type | Description |
|---------|---------|---------|---------|
| directConnectId | No | String | Direct Connect ID, such as dc-kd7d06of. | 
| directConnectTunnelId | No | String | Direct Connect tunnel ID, such as dcx-kd7d0125. | 

## Response Parameters

| Parameter  | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Successful; other values: Failed. |
| message | String | Error message. |
| data.n | Array | Returned array. |
| data.n.directConnectTunnelId | String | ID of the Direct Connect tunnel assigned by the system, such as dcx-kd7d0125. |
| data.n.directConnectTunnelName | String | Direct Connect tunnel name. |
| data.n.directConnectId | String | ID of the Direct Connect assigned by the system, such as dc-kd7d06of. |
| data.n.ownerAccount | String | Account ID of the Direct Connect developer. |
| networkType | Int | Network type. 0: BM; 1: VPC network.|
| data.n.region | String | Network region. |
| data.n.vpcId | String | Unified VPC ID or unified BM network ID. |
| directConnectGatewayId | String | Direct Connect gateway ID, such as dcg-d545ddf. |
| data.n.bandwidth | Int | Direct Connect bandwidth (in Mbps). |
| data.n.routeMode | Int | 0: BGP routing. 1: static. Default is BGP routing. |
| data.n.bgpPeers.asn | String | BGP asn. |
| data.n.bgpPeers.authKey | String | BGP key. |
| data.n.routeFilterPrefixes.n.cidr | String | Peer IP address range. |
| data.n.status | Int | Status of the Direct Connect tunnel. 0: Connected; 1: Requesting; 2: Configuring; 20: Waiting for connection; 21: Rejected. |
| data.n.vlan | Int | vlan Id.|
| data.n.localGatewayIp | String | Tencent Connect IP |
| data.n.peerGatewayIp | String | User Connect ip|
| data.n.peeringSubnetMask | String | Connect IP Mask |
| data.n.remark | String | Remarks. |

## Practical Case
 
### Request
```
  GET https://dc.api.qcloud.com/v2/index.php?Action=DescribeDirectConnectTunnels
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
  &directConnectId=dc-kd7d06of

```

### Response
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


