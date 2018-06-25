## Description
 
This API (DescribeDirectConnects) is used to query the list of direct connects.
Domain name for API request: dc.api.qcloud.com 

## Request

Syntax:
```
GET https://dc.api.qcloud.com/v2/index.php?Action=DescribeDirectConnects
    &<Common request parameters>
    &directConnectId=dc-kd7d06of
```

### Request parameters
The following request parameter list only provides API request parameters. Common request parameters are required when the API is called. For more information, please see <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is DescribeDirectConnects.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| directConnectId | No |  String | Direct connect ID, for example: dc-kd7d06of. All direct connects created by the developer are returned if this parameter is not specified. | 


## Response

Response example:
```
{
    "code": 0,
    "message": "",
    "data": [
        {
        }
    ]
}
```

### Response parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code| Int | Error code. 0: Successful; other values: Failed. |
| message |  String | Error message. |
| data.n | Array  | Returned array. |
| data.n.directConnectId | String | Direct connect ID assigned by the system, for example: dc-kd7d06of. |
| data.n.directConnectName | String | Direct connect name. |
| data.n.status | String | Direct connect status. 0: Running; 1: Expired; 2: Deleting; 3: Deleted; 11: Requesting; 12: Rejected; 13: To be paid; 14: Paid; 15: Building; 16: Building stopped. |
| data.n.provider | String | Direct connect provider. |
| data.n.portType | int | Interface type. 1: 100Base-T 100 MB electric interface; 2: 1000Base-T 1 GB electric interface; 3: 1000Base-LX 1 GB single-mode optical port (10 km); 4: 10GBase-LR 1 TB single-mode optical port (10 km) |
| data.n.accessPoints | String | Access point. |
| data.n.bandwidth | String | Direct connect bandwidth (in Mbps). |
| data.n.loaIssueTime | String | Direct Connect expiration time. |

### Response error codes
The following error codes only include the business logic error codes for this API. For additional common error codes, please see <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error Code | Description |



## Example

### Request
```
GET https://dc.api.qcloud.com/v2/index.php?Action=DescribeDirectConnects
    &<<a href="https://cloud.tencent.com/doc/api/229/6976">common request parameters</a>>
    &directConnectId=dc-kd7d06of
```

### Response
```
{
    "code": 0,
    "message": "",
    "data": [
        {
            "directConnectId": "dc-3cavza1z",
            "directConnectName": "Li Hao Test Direct Connect @123112",
            "status": 15,
            "provider": "China Telecom",
            "portType": 8,
            "accessPoints": "1",
            "bandwidth": 200,
            "loaIssueTime": "2017-09-02 15:41:00"
        }
    ]
}
```


