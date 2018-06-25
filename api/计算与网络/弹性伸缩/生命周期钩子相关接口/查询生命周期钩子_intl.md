## 1. API Description
This API (DescribeLIfeCycleHook) is used to query the lifecycle hook configuration.
Domain for API request: <font style="color:red">scaling.api.qcloud.com</font>

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is DescribeLIfeCycleHook.

| Parameter Name | Required  | Type | Description | 
|---------|---------|---------|---------|
| scalingGroupId | No | String | ID of the scaling group to which the lifecycle hook to be queried belongs. It can be queried by calling API <a href="/doc/api/372/查询伸缩组列表" title="Query Scaling Group List">Query Scaling Group List</a> (DescribeScalingGroup). |
| lifeCycleHookId | No | String | ID of the lifecycle hook to be queried. |
| lifeCycleHookName | No | String | Name of the lifecycle hook to be queried. |
| lifeCycleHookTimeout | No | Int | Timeout of the lifecycle hook to be queried. |
| transition | No | Int | Callback condition of the lifecycle hook to be queried. |
| defaultResult | No | Int | Default timeout action for a lifecycle hook to be queried. |
| offset | No | Int | Offset; default is 0 |
| limit | No | Int | The maximum of scaling configurations that can be queried at a time. |

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="http://intl.cloud.tencent.com/document/product/377/8946" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code. |
| data | Array | Notification list information returned for the query. |

Parameter data is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| lifeCycleHookSet | Array | Set containing notification information.  |

The lifeCycleHookSet contains a number of notification information, and each is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| autoScalingGroupId | String | Returned ID of the scaling group to which the lifecycle hook belongs. | 
| lifeCycleHookId | String | ID of the lifecycle hook returned for the query. | 
| lifeCycleHookName | String | Notification type corresponding to the lifecycle hook returned for the query. | 
| notifyIds | String | Notification group ID corresponding to the lifecycle hook returned for the query. | 
| transition | Int | Callback condition corresponding to the lifecycle hook returned for the query. | 
| defaultResult | Int | Default timeout action for a lifecycle hook returned for the query. | 

## 4. Error Codes
For common errors on this API, refer to [AS Error Code](http://intl.cloud.tencent.com/document/product/377/8946).

## 5. Example
```
https://scaling.api.qcloud.com/v2/index.php?
&<Common request parameters>
```
Example of returned result is as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success"
    "data":{
        "lifeCycleHookSet":[
            {
                "lifeCycleHookTimeout":10,
                "lifeCycleHookName":"xxx",
                "autoScalingGroupId":"asg-7awqgwmv",
                "transition":1,
                "defaultResult":1,
                "lifeCycleHookId":"lfh-2maknjbc"
            },
        ]
    }
}
```


