## 1. API Description
This API (CreateLifeCycleHook) is used to modify the configuration of an existing lifecycle hook.
Domain for API request: <font style="color:red">scaling.api.qcloud.com</font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is ModifyLifeCycleHook.

| Parameter Name       | Required | Type   | Description                                                  |
| -------------------- | -------- | ------ | ------------------------------------------------------------ |
| scalingGroupId       | Yes      | String | ID of the scaling group of a lifecycle hook to be modified. It can be queried by calling API [Query Scaling Group List](https://intl.cloud.tencent.com/doc/api/372/%E6%9F%A5%E8%AF%A2%E4%BC%B8%E7%BC%A9%E7%BB%84%E5%88%97%E8%A1%A8)(DescribeScalingGroup). |
| lifeCycleHookId      | Yes      | String | ID of the lifecycle hook to be modified.                     |
| lifeCycleHookName    | No       | String | Name of the lifecycle hook to be modified.                   |
| lifeCycleHookTimeout | No       | Int    | Timeout of the lifecycle hook to be modified (in seconds).   |
| defaultResult        | No       | Int    | Default timeout action for a lifecycle hook task to be modified; 0: continue, 1: disable |
| transition           | No       | Int    | Callback condition of the life cycle hook to be modified; 0: sub-machine is being created, 1: sub-machine is being terminated |
| notifyIds.n          | No       | String | Notification group ID of the lifecycle hook to be modified, that is, the collection of user group ID (groupID). The Array subscript is started with 0. It can be queried by calling API "Obtain User Group List" (DescribeUserGroup). |

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="http://intl.cloud.tencent.com/document/product/377/8946" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code. |
| data | Array | It is empty if returned successfully. |


## 4. Error Codes
The following error codes only include the business logic error codes for this API. For additional common error codes, refer to [AS Error Code](http://intl.cloud.tencent.com/document/product/377/8946).

| Error Code | Description |
|----|------|
| HookParameterError.Transition | Incorrect transition value in the hook (only 0 or 1) |
| HookParameterError.DefaultResult | Incorrect defaultResult value in the hook (only 0 or 1) |
| NameDuplicate.LifeCycleHook | The hook name already exists |
| InvalidParameter.GroupIdInHook | Invalid notification group groupId |
| InvalidParameter.ScalingGroupIdError | Incorrect scalingGroupId |


## 5. Example

```
https://scaling.api.qcloud.com/v2/index.php?
&<Common request parameters>
&scalingGroupId=asg-xxxxxx
&lifeCycleHookId=lfh-xxxxxx
&lifeCycleHookTimeout=10
```
Example of returned result is as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc": "Success",
    "data":[]
}
```


