>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 1. API Description

This API (RebootDevice) is used to reboot a CPM.
Domain for API request: <font style="color:red">bm.api.qcloud.com</font>




## 2. Input Parameters
| Parameter Name | Required | Type | Description |
| --------| ----| -----| ----|
| instanceIds | Yes | Array | List of unique device IDs |
| opUin | Yes | String | Operator's QQ number |


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
| 10001 | InvalidParameter | Invalid parameter |
| 12002 | OperationDenied.IncorrectInstanceStatus | Cannot reboot the device |


## 5. Example
Input
<pre>
  https://bm.api.qcloud.com/v2/index.php?Action=RebootDevice
  &instanceIds.1=cpm-34xs43xs
  &instanceIds.2=cpm-34xs43ab
  &opUin=23234234
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


