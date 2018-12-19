## 1. API Description

This API (DescribeScalingActivity) is used to query scaling activity logs of scaling groups.
Domain name for API request: scaling.api.qcloud.com

## 2. Input Parameters

The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="https://cloud.tencent.com/document/api/377/4153" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is DescribeScalingActivity.

| Parameter | Required | Type | Description |
|---------|---------|---------|---------|
| scalingGroupId | Yes | String | ID of the scaling group you want to query|
| scalingActivityIds.n | No | Array | IDs of the scaling activity ID you want to query|
| offset | No | Int | Offset; default is 0 |
| limit | No | Int | Number of returned results. Default is 20 |
| startTime | No | datetime | Specify a start time |
| endTime | No | datetime | Specify an end time |


## 3. Output Parameters

| Parameter| Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the error codes page |
| codeDesc | String | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. |
| message | String | Module error message description depending on API |
| data | Array | Query detailed information on returned scaling activities |
| data.scalingActivitySet | Array | Specific scaling activity details |
| data.totalCount | int | Number of the recorded scaling activities upon query |

Each element in the `scalingActivitySet` array is a scaling activity log in json format.

| Parameter| Type | Description |
|---------|---------|---------|
| autoScalingGroupId | String | ID of the scaling group to which the current scaling activity belongs | 
| status | Int | Execution result of a scaling activity. Specific mapping relationship is shown in the following table | 
| type | Int | Type of the current scaling activity. Specific mapping relationship is shown in the following table | 
| errorCode | Int | Error code of the execution result for the scaling activity. Specific mapping relationship is shown in the following table | 
| succInsList | Int | ID of the server on which a scaling activity is successfully executed | 
| failInsList | Int | ID of the server on which a scaling activity fails to be executed | 
| cause | String | The reason why a scaling activity is triggered |  
| desciption | String | Description of a scaling activity | 
| msg | String | Description of the execution result for the scaling activity | 
| scalingActivityId | String | ID of the current scaling activity | 
| startTime | String | Start time of the current scaling activity | 
| endTime | String | End time of the current scaling activity | 

The mapping relationship is shown as follows:

1) `status`:

| Code | Description |
|----|----|
| 0 | Initializing |
| 1 | Executing |
| 2 | Successful |
| 3 | Partially successful |
| 4 | Failed |
| 5 | Canceled |

2) `type`:

| Code | Description |
|----|----|
| 0 | Scale up |
| 1 | Scale down |
| 2 | Add a server |
| 3 | Remove a server |
| 10 | Replace an unhealthy server |

3) `errorCode`:

| Code | Description | Suggested Operation |
|----|----|--------|
| 0 | Succeed | Succeed |
| 10000 | Image is deleted | Change launch configuration |
| 10001 | LB is deleted | Modify LB|
| 10002 | Data snapshot is deleted | Change launch configuration |
| 10003 | Security group is deleted | Change launch configuration |
| 10004 | Subnet is deleted | Modify the subnet |
| 20000 | Sold out | Stop scale-up activities |
| 20001 | Model does not exist | Stop scale-down activities|
| 20002 | Insufficient backend resources | Stop scale-up activities |
| 30000 | Insufficient quota | Decrease the number of servers to scale up, or send a ticket to increase quota |
| 30001 | Insufficient account balance | Top up |
| 40000 | Scaling group is performing a scaling activity | Try again later |
| 40001 | Scaling group is in cooldown period | Try again later |
| 50000 | Key is deleted | Change launch configuration |

## 4. Error Codes

For common errors on this API, please see [AS Error Codes](https://cloud.tencent.com/doc/api/372/4173).


## 5. Example

Input
```
https://scaling.api.qcloud.com/v2/index.php?
&<Common request parameters>
&scalingGroupId=asg-xxxxx
&limit=1
```

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "totalCount": 8,
        "scalingActivitySet": [
            {
                "autoScalingGroupId": "asg-pixbyldg",
                "status": 2,
                "cause": "Users are removed from the CVM [ins-5u97n5re]",
                "desciption": "Users are removed from the CVM [ins-5u97n5re]",
                "startTime": "2017-04-15 20:54:57",
                "msg": "success",
                "scalingActivityId": "asa-b51zb5i4",
                "endTime": "2017-04-15 20:54:59",
                "type": 3,
                "succInsList": [
                    "ins-5u97n5re"
                ],
                "failInsList": [],
                "errorCode": 0
            }
        ]
    }
}
```


