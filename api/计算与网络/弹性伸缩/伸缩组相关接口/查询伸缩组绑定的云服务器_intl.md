## 1. API Description
This API (DescribeScalingInstance) is used to query CVMs bound to the scaling groups.
Domain for API request: <font style="color:red">scaling.api.qcloud.com</font>

1) You can filter the results based on the scaling group ID, CVM ID, instance health status, instance creation type, and so on.

2) There are two types of CVM instances added to the scaling group: automatically created CVM instance and manually added CVM instance.
"Automatically created CVM instance" refers to a CVM instance that is automatically created by an auto scaling service according to the user's scaling configuration and scaling rule.
"Manually added CVM instance" refers to a CVM instance that is not created by an auto scaling service but is manually added by the user to the scaling group.

3) The life cycle of the CVM instance in the scaling group is described by the following statuses:
Creating (Creating) - Indicates that a CVM instance is being created.
Running (InService) - Indicates that an instance is running.
Removing (Removing) - Indicates that an instance is being removed from the scaling group.
Binding (Attaching) - Indicates that an instance is being bound to the scaling group.
Unbinding (Detaching) - Indicates that an instance is being unbound from the scaling group.
Backuping (Backuping) - Indicates that an instance is being backed up.
UnBackuping (UnBackuping) - Indicates that the backup instance is being deleted.
Binding LB (AttachLb) - Indicates that a cloud load balance is being bound.
Unbinding LB (DetachLb) - Indicates that a cloud load balance is being unbound.
Prefetching (Preheating) - Indicates that the instance is being prefetched.

4) The health status of the CVM instance in the scaling group is:
Healthy
Unhealthy
The AS will automatically remove the unhealthy CVM instances from the scaling group. For "automatically created CVM instance", CVM will stop and release the CVM instance. For "manually added CVM instance", CVM will not stop and release the CVM instance.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is DescribeScalingInstance.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| scalingGroupId | Yes | String | Scaling group ID to be queried. It can be queried by calling <a href="/doc/api/372/查询伸缩组列表" title="Query Scaling Group List">Query Scaling Group List</a> (DescribeScalingGroup) API. |
| instanceIds.n | No | String | CVM instance ID to be queried. All CVM instances bound to the scaling group are displayed by default. To specify a CVM instance, please fill in the unInstanceId (unified ID of CVM) field returned in the API <a href="/doc/api/229/831" title="DescribeInstances">Query Instance List (DescribeInstances)</a>, and up to 20 CVM instances can be specified. |
| creationType | No | String | The type of CVM instance to be queried that bound to the scaling group. Only two values are available: Auto means that the instance is automatically created by the scaling group; Manual means that the instance is manually created by the user. |
| healthStatus | No | String | The health status of CVM instance to be queried that bound to the scaling group. Only two values are available: Healthy means that the instance is healthy; UnHealthy means that the instance is unhealthy. |
| offset | No | Int | Offset; default is 0. |
| limit | No | Int | The maximum number of CVM instances allowed to be displayed at a time. Default is 20.  |

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="http://intl.cloud.tencent.com/document/product/377/8946" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| codeDesc | String | Error code at business side. If the task succeeds, it will return "Success"; if the task fails, the specific business error reason will be returned. |
| message | String | Module error message description depending on API. |
| data | Array | Output results. CVM instance list returned for the query.  |

Parameter data is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| totalCount | Int | The number of CVM instances returned for the query.  |
| scalingInstancesSet | Array | Set of CVM instance information.  |

scalingInstancesSett contains information about a number of several CVM instances, and the information about each CVM instance is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| instanceId | String | ID of the CVM instance. | 
| healthStatus | String | Health status of the instance. Healthy means that the instance is healthy; UnHealthy means that the instance is unhealthy.  | 
| creationType | String |  Instance type. Auto means that the instance is automatically created by the scaling group; Manual means that the instance is manually created by the user. | 
| lifeCycleState | String | The lifecycle statuses of an instance in the scaling group includes the following cases: <br>Creating (Creating)<br>Running (InService)<br>Removing (Removing)<br>Binding (Attaching)<br>Unbinding (Detaching)<br>Backuping (Backuping)<br>UnBackuping (UnBackuping)<br>Binding LB (AttachLb)<br>Unbinding LB (DetachLb)<br>Prefetching (Preheating) |
| protectedFromScaleIn | Int | Flag bit of removal protection. 1: In removal protection; 0: Not in removal protection. | 
| addTime | String | The time at which this instance is added to the scaling group. | 

## 4. Error Codes
For common errors on this API, refer to [AS Error Code](http://intl.cloud.tencent.com/document/product/377/8946).

## 5. Example
```
https://scaling.api.qcloud.com/v2/index.php?
&<Common request parameters>
&scalingGroupId=asg-xxxxx
```
Example of returned result is as follows. The scalingInstancesSet contains only one element, indicating that there is only one CVM instance bound to the scaling group.
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",     
    "data":{
        "totalCount":1,
        "scalingInstancesSet":[
            {
                "instanceId":"ins-xxxx",
                "healthStatus":"Healthy",
                "creationType":"Manual",
                "lifeCycleState":"InService",
                "addTime":"2016-03-17 11:48:31"
            }
        ]
    }
}
```

