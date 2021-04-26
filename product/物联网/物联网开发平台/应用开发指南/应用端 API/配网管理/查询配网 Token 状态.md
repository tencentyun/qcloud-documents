## 1. 接口描述
接口请求域名：`iot.cloud.tencent.com/api/exploreropen/tokenapi`
本接口（AppGetDeviceBindTokenState）用于查询配网 Token 的当前状态。

## 2. 输入参数
|名称|类型|必选|描述|
|---|---|---|---|
|Action|String|是|公共参数，本接口取值：AppGetDeviceBindTokenState|
|RequestId|String|是|公共参数，唯一请求 ID，可自行生成，推荐使用 uuid。定位问题时，需提供该次请求的 RequestId|
|AccessToken|String|是|公共参数，用户通过微信号、手机或邮箱账号登录成功后，获取的访问 Token|
|Token|String|是|由 AppCreateDeviceBindToken 接口生成的配网 Token|

## 3. 输出参数
|名称|类型|描述|
|---|---|---|
|RequestId|String|RequestId|
|State|Uint|Token 状态，1：初始生产，2：可使用状态|

## 4. 示例
#### 示例1 查询配网 Token 状态
**输入示例**
```HTTP
POST https://iot.cloud.tencent.com/api/exploreropen/tokenapi HTTP/1.1
content-type: application/json
{
  "Action": "AppCreateDeviceBindToken",
  "AccessToken":"********",
  "RequestId": "f92406b3-5a9a-4fe8-bc43-45e3d794bb68",
  "Token": "d7a1**********a861b3b"
}
```

**输出示例：成功**
```json
{
  "Response": {
    "Data": {
    "State": 1,
    "RequestId": "f92406b3-5a9a-4fe8-bc43-45e3d794bb68"
  }
}
```

**输出示例：失败**
```json
{
  "Response": {
    "Error": {
      "Code": "InvalidParameterValue.TokenNotExist",
      "Message": "Token不存在"
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


