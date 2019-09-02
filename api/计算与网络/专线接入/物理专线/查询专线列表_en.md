## Description
 
This API (DescribeDirectConnects) is used to query the Direct Connect list.
Domain name for API request: dc.api.qcloud.com 

## Request

Syntax:
```
GET https://dc.api.qcloud.com/v2/index.php?Action=DescribeDirectConnects
    &<Common request parameters>
    &directConnectId=dc-kd7d06of
```

### Request Parameter
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="https://cloud.tencent.com/document/api/377/4153" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is DescribeDirectConnects.

| Parameter | Required | Type | Description |
|---------|---------|---------|---------|
| directConnectId | No | String | Direct Connect ID, such as dc-kd7d06of. All Direct Connects created by the developer are returned if this parameter is not specified. | 


## Response

Response Example:
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

## Response Parameters

| Parameter | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Successful; other values: Failed. |
| message | String | Error message. |
| data.n | Array | Returned array. |
| data.n.directConnectId | String | ID of the Direct Connect assigned by the system, such as dc-kd7d06of. |
| data.n.directConnectName | String | Direct Connect name. |
| data.n.status | String | Direct Connect status. 0: Running; 1: Expired; 2: Deleting; 3: Deleted; 11: Requesting; 12: Rejected; 13: To be paid; 14: Paid; 15: Building; 16: Stop building. |
| data.n.provider | String | Direct Connect provider |
| data.n.portType | int | Interface type. 1: 100Base-T 100MB electric port; 2: 100Base-T 1GB electric port; 3: 100Base-T 1GB single-mode optical port (10km); 4: 10GBase-LR 1TB single-mode optical port (10km). |
| data.n.accessPoints | String | Access point. |
| data.n.bandwidth | String | Direct Connect bandwidth (in Mbps). |
| data.n.loaIssueTime | String | Direct Connect expiration time |

### Response Error Codes
The following error codes only include the business logic error codes for this API. For additional common error codes, please see <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error Code | Description |



## Example

### Request
```
GET https://dc.api.qcloud.com/v2/index.php?Action=DescribeDirectConnects
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


