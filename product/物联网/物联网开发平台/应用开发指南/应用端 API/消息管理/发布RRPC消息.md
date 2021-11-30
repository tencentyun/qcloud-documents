## 1. 接口描述

接口请求域名：`iot.cloud.tencent.com/api/exploreropen/tokenapi`。

本接口(AppPublishRRPCMessage)用于向设备发布 RRPC 消息进行远程配置。

## 2. 输入参数

| 名称        | 类型   | 必选 | 描述                                                         |
| ----------- | ------ | ---- | ------------------------------------------------------------ |
| AccessToken | String | 是   | 公共参数，用户通过微信号、手机或邮箱账号登录成功后,获取的访问 Token |
| RequestId   | String | 是   | 公共参数，唯一请求ID，可自行生成，推荐使用 uuId。定位问题时，需提供该次请求的 RequestId |
| Action      | String | 是   | 公共参数，本接口取值：AppPublishRRPCMessage                  |
| ProductId   | String | 是   | 产品 ID                                                      |
| DeviceName  | String | 是   | 设备名                                                       |
| Payload     | String | 是   | 消息内容，utf8 编码                                           |

## 3. 输出参数

| 名称          | 类型   | 描述                               |
| ------------- | ------ | ---------------------------------- |
| RequestId     | String | 公共参数，唯一请求 ID，与入参相同   |
| MessageId     | Int64  | RRPC 消息 ID                         |
| PayloadBase64 | String | 设备回复的消息内容，采用 base64 编码 |

## 4. 示例

#### 示例1

**输入示例**

```HTTP
  POST https://iot.cloud.tencent.com/api/exploreropen/tokenapi HTTP/1.1
  content-type: application/json
  {
    "Action": "AppPublishRRPCMessage",
    "RequestId": "f92406b3-5a9a-4fe8-bc43-45e3d794bb68",
    "AccessToken": "8b4a70dd16105f******************18edd4e78a3bb8ec",
    "ProductId": "ASBHKN",
    "DeviceName": "dev",
    "Payload": "1234561"
  }
```

**输出示例:  成功**

```json
  {
    "Response": {
      "MessageId": 74,
      "PayloadBase64": "QUJDRA==",
      "RequestId": "f92406b3-5a9a-4fe8-bc43-45e3d794bb68"
    }
  }

```

## 5. 错误码

| 错误码                                   | 描述         |
| ---------------------------------------- | ------------ |
| InternalError                            | 内部错误     |
| InvalidParameterValue                    | 参数取值错误 |
| InvalidParameterValue.InvalidAccessToken | Token 无效    |
