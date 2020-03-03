## 1. API Description
This API (CreateLifeCycleHook) is used to create new lifecycle hook configurations.
Domain for API request: <font style="color:red">scaling.api.qcloud.com</font>

1) When a sub-machine is created or terminated, there's a time window provided after its creation and before its termination for users to complete the initialization or saving of sub-machine data.

2) You can create up to 10 lifecycle hooks in each scaling group, but only one life cycle hook can be bound at a time. When using a lifecycle hook, you need to call the bound scaling group and the callback hook API to activate the currently active lifecycle hook.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is CreateLifeCycleHook.

| Parameter Name | Required  | Type | Description | 
|---------|---------|---------|---------|
| scalingGroupId | Yes | String | ID of the scaling group of a lifecycle hook to be created. It can be queried by calling API <a href="/doc/api/372/查询伸缩组列表" title="Query Scaling Group List">Query Scaling Group List</a> (DescribeScalingGroup).
| lifeCycleHookName | Yes | String | Name defined by the user for the lifecycle hook to be created. | 
| lifeCycleHookTimeout | Yes | Int | Timeout (in seconds) defined by the user for the life cycle hook, during which the user can complete the initialization or saving of sub-machine data. | 
| defaultResult | No | Int | Default timeout action for a lifecycle hook task; 0: continue, 1: disable; The default is 0.  | 
| transition | No | Int | Callback condition of the life cycle hook; 0: sub-machine is being created, 1: sub-machine is being terminated. The default is 0.  | 
| notifyIds.n | No | String | ID of the notification group, that is, the collection of user group ID (groupID). The array subscript is started with 0. It can be queried by calling API "Obtain User Group List" (DescribeUserGroup). | 



## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="http://intl.cloud.tencent.com/document/product/377/8946" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code. |
| data | Array | It contains the list information of the scheduled tasks that were created successfully. |

Parameter data is composed of the following parameters, and contains only one element lifeCycleHookId.

| Parameter Name | Type | Description |
|---------|---------|---------|
| lifeCycleHookId | String | New lifecycle hook ID.  |

## 4. Error Codes
The following error codes only include the business logic error codes for this API. For additional common error codes, refer to [AS Error Code](http://intl.cloud.tencent.com/document/product/377/8946).

| Error Code | Description |
|---|---|
| HookParameterError.Transition | Incorrect transition value in the hook (only 0 or 1) |
| HookParameterError.DefaultResult | Incorrect defaultResult value in the hook (only 0 or 1) |
| NameDuplicate.LifeCycleHook | The hook name already exists |
| InvalidParameter.GroupIdInHook | Invalid notification group groupId |
| QuotaExceeded.HookLimit | Hook limit exceeded |
| InvalidParameter.ScalingGroupIdError | Incorrect scalingGroupId |

## 5. Example

```
https://scaling.api.qcloud.com/v2/index.php?
&<Common request parameters>
&scalingGroupId=asg-xxxxxx
&lifeCycleHookName=xxxxx
&lifeCycleHookTimeout=10
&notifyIds.0=1844
```
Example of returned result is as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc": "Success",
    "data":{
        "lifeCycleHookId":[
            "lfh-xxxxxx"
        ]
    }
}
```


