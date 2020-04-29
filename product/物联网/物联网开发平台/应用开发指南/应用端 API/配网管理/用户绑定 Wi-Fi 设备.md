## 1. 接口描述
接口请求域名：`iot.cloud.tencent.com/api/exploreropen/tokenapi`
本接口（AppTokenBindDeviceFamily）用于小程序或 App 用户绑定 Wi-Fi 类设备。

## 2. 输入参数

|名称|类型|必选|描述|
|---|---|---|---|
|Action|String|是|公共参数，本接口取值：AppTokenBindDeviceFamily|
|RequestId|String|是|公共参数，唯一请求 ID，可自行生成，推荐使用 uuid。定位问题时，需要提供该次请求的 RequestId|
|AccessToken|String|是|公共参数，用户通过微信号、手机或邮箱账号登录成功后，获取的访问 Token|
|Token|String|是|配网 Token|
|ProductId|String|是|产品 ID
|DeviceName|String|是|设备名称|
|FamilyId|String|是|家庭 ID|
|RoomId|String|是|房间 ID|

## 3. 输出参数

|名称|类型|描述|
|---|---|---|
|RequestId|String|公共参数，唯一请求 ID，可自行生成，推荐使用 uuid。定位问题时，需提供该次请求的 RequestId|

## 4. 示例
#### 示例1 用户绑定 Wi-Fi 设备
**输入示例**
```HTTP
POST https://iot.cloud.tencent.com/api/exploreropen/tokenapi HTTP/1.1
content-type: application/json
{
  "Action": "AppTokenBindDeviceFamily",
  "AccessToken":"tesetoken",
  "Token": "d7a12d######**********861b3b",
  "ProductId": "*******",
  "DeviceName": "*******",
  "FamilyId": "f************cc1",
  "RoomId": "0"
  "RequestId": "f92406b3-5a9a-4fe8-bc43-45e3d794bb68"
}
```

**输出示例 成功**
```json
{
  "Response": {
    "Data": {
    "RequestId": "f92406b3-5a9a-4fe8-bc43-45e3d794bb68"
  }
}
```

**输出示例 失败**
```json
{
  "Response": {
    "Error": {
      "Code": "InvalidParameterValue.InvalidAccessToken",
      "Message": "Token无效"
    },
    "RequestId": "f92406b3-5a9a-4fe8-bc43-45e3d794bb68"
  }
}
```


## 5. 错误码

|错误码|描述|
|---|---|
|InvalidParameter|无效参数|
|InvalidParameterValue|参数取值错误|
|InvalidParameterValue.TokenNotExist|Token 不存在|
|InvalidParameterValue.TokenIsExpire|Token 已过期|
|InvalidParameterValue.ReadTokenInfoError|Token 读错误|
|InvalidParameterValue.TokenNotBind|Token 未绑定|
|InvalidParameterValue.FamilyDeviceCountReadError|读设备数量错误|
|UnauthorizedOperation|无操作权限|
|UnauthorizedOperation.APPNoPermissionToStudioProduct|App 对操作该产品无权限|
|UnauthorizedOperation.NoPermissionToFamily|操作该家庭无权限|
|ResourceNotFound|资源部存在|
|ResourceNotFound.StudioFamilyNotExist|家庭未创建或是已删除|
|ResourceNotFound.StudioProductNotExist|产品尚未创建或已被删除|
|ResourceNotFound.DeviceNotExist|设备未创建或是已删除|
|LimitExceeded|数量限制|
|LimitExceeded.FamilyDeviceExceedLimit|设备数量超出限制|
|InternalError|内部错误|
|InternalError.InternalServerException|内部错误|
|InternalError.InternalServerExceptionDB|内部 DB 错误|
|UnsupportedOperation|不支持的操作|
|UnsupportedOperation.CannotBindSameFamily|该设备已经绑定，请勿重复绑定|
