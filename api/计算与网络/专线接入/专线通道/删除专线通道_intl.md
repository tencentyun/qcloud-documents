## Description
This API (DeleteDirectConnectTunnel) is used to delete a direct connect tunnel.
Domain name: `dc.api.qcloud.com`


## Request Parameters
| Parameter | Type | Required | Description |
| --------------------| ------| --------| -----------  | 
| directConnectTunnelId | String | Yes | Direct connect tunnel ID</br>For example: dcx-abcdefgh | 

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
```

### Response example
```
{
    "code": 0,
    "message": ""
}
```


