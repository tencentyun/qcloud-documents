## API Description
Domain name: `lb.api.qcloud.com`
API name: `DescribeRewrite`

## Input Parameters
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerIds | No | Array | ID of load balancer instance. It can be queried by entering 1 or -1 in input parameter "forward" field through the API <a href="https://cloud.tencent.com/document/api/214/1261" title="DescribeLoadBalancers">DescribeLoadBalancers</a>. |
| listenerIds | No | Array | Unique ID of listener. |
| locationIds | No | Array | Unique ID of forwarding rule. |

## Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0: Successful; other values: Failed. |
| message | String | Error message. |
| codeDesc | String | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. |
| data | Array | Output result that contains the information of returned scheduled task list. |

"data" is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| RewriteSet | Array | Redirect relationship set of forwarding rules |

Each element of RewriteSet contains the following fields: 

| Parameter Name | Type | Description |
|---------|---------|---------|
| uListenerId | String | Unique ID of source listener. |
| uLocationId | String | Unique ID of source forwarding rule |
| targetuListenerId | String | Unique ID of target listener |
| targetuLocationId | String | Unique ID of target forwarding rule |


## Example
Input
```
https://lb.api.qcloud.com/v2/index.php?Action=DescribeRewrite
&<Common request parameters>
&loadBalancerIds.0=lb-6efswuxa
&listenerIds.0=lbl-20cxbf40
&locationIds.0=loc-sdadasmd
```
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "RewriteSet": [
            {
                "uListenerId": "lbl-jb2kkehy",
                "uLocationId": "loc-n68ar3hi",
                "domain": "clue.cn",
                "url": "/",
                "httpGzip": true,
                "httpHash": "wrr",
                "keep_time": 900,
                "targetuListenerId": "lbl-jb2kkehy",
                "targetuLocationId": "loc-9wo2gh66",
                "bAutoCreated": 0,
                "health": {
                    "healthNum": 3,
                    "httpCheckPath": "/",
                    "httpCode": 31,
                    "intervalTime": 5,
                    "switch": 1,
                    "timeOut": 2,
                    "unhealthNum": 3
                }
            }
        ]
    }
}
```

