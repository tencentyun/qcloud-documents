## 1. API Description
 
This API (ResetDevicePasswd) is used to reset the root password of CPM.

Domain for API request: bm.api.cloud.tencent.com

 * This API is asynchronous task. You need to query operation completion status by using another API: [Query Status of Asynchronous Task (DescriptionOperationResult)](/doc/api/456/6644).
 * You can batch modify CPM passwords by using this API.
 

## 2. Input Parameters

The following request parameter list only provides API request parameters. For additional parameters, see [Common Request Parameters](/doc/api/456/6718) page.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| instanceIds.n | Yes | String | ID of the CPM to be operated on. You can acquire the IDs from the returned values of instanceId of the [Query Servers (DescribeDeviceList)](/doc/api/456/6728) API (You may pass multiple IDs when using this API. For the detailed format of this parameter, please see the `id.n` section in the API [Introduction](/doc/api/456/6628)). |
| passwd | Yes | String | Password. The password must contain 8-16 characters, with at least two types of characters out of three (letters, numbers or symbols !@#$%&^*()) |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, please see [Common Error Codes](/doc/api/456/6725) in the Error Codes page. |
| message | String | Module error message description depending on API. |
| data | Obj | Returned asynchronous operation ID

## 4. Module Error Codes

| code | codeDesc | Description |
|------|------| -----|
| 9001 | InternalError.DbError | Error occurred when operating the database |
| 9005 | InternalError.RbmqError | Operating system queue error |
| 9008 | InternalError.TscRequestFail | Request internal backend API error |
| 10001 | InvalidParameter | Invalid parameter |
| 12002 | OperationDenied.IncorrectInstanceStatus | Cannot reset password for the device |
| 12006 | OperationDenied.TsysAgentNotAlive | Cannot perform this operation, agent does not exist |

 

## 4. Example
 
Input

<pre>`https://domain/v2/index.php?Action=ResetDevicePasswd`
  &instanceIds.1=cpm-34xs43xs
  &instanceIds.2=cpm-3xwssdfx
  &passwd=abce1234
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
</pre>
Output

```
{
  "code": 0,
  "message": "OK",
  "data": {
       "taskId": 101
   }
}

```





