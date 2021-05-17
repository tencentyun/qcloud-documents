

## 1. 接口描述
接口请求域名： `iot.cloud.tencent.com/api/exploreropen/tokenapi`
本接口（AppCreateDeviceBindToken）用于生成 Wi-Fi 配网任务的随机 Token。

## 2. 输入参数

|名称|类型|必选|描述|
|---|---|---|---|
|Action|String|是|公共参数，本接口取值：AppCreateDeviceBindToken|
|RequestId|String|是|公共参数，唯一请求 ID，可自行生成，推荐使用 uuid。定位问题时，需要提供该次请求的 RequestId|
|AccessToken|String|是|公共参数，用户通过微信号、手机或邮箱账号登录成功后，获取的访问 Token|

## 3. 输出参数

|名称|类型|描述|
|---|---|---|
|RequestId|String|RequestId|
|Token|String|生成的配网 Token|

## 4. 示例
#### 示例1 生成 Wi-Fi 设备配网 Token
**输入示例**
```HTTP
POST https://iot.cloud.tencent.com/api/exploreropen/tokenapi HTTP/1.1
content-type: application/json
{
  "Action": "AppCreateDeviceBindToken",
  "AccessToken":"adf*******3ks",
  "RequestId": "f92406b3-5a9a-4fe8-bc43-45e3d794bb68"
}
```
**输出示例：成功**
```json
{
  "Response": {
    "Data": {
    "Token": "d7*************1b3b",
    "RequestId": "f92406b3-5a9a-4fe8-bc43-45e3d794bb68"
  }
}
```
**输出示例：失败**
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
|InvalidParameterValue.TokenInfoSaveError|Token 保存失败|


