## 1. 接口描述
接口请求域名： `iot.cloud.tencent.com/api/exploreropen/tokenapi`。
本接口（AppSendShareFamilyInvite）用于发送家庭分享邀请。

## 2. 输入参数

|名称|类型|必选|描述|
|---|---|---|---|
|AccessToken|String|是|公共参数，AccessToken 用于对一个已经登录的用户鉴权。|
|RequestId|String|是|公共参数，唯一请求 ID，可自行生成，推荐使用 uuId。定位问题时，需提供该次请求的 RequestId。|
|Action|String|是|公共参数，本接口取值：AppSendShareFamilyInvite|
|FamilyId|String|是|家庭 ID|
|ToUserID|String|是|被分享用户 ID|

## 3. 输出参数

|名称|类型|描述|
|---|---|---|
|RequestId|String|公共参数，唯一请求 ID，与入参相同，定位问题时，需提供该次请求的 RequestId。|

## 4. 示例
#### 示例1
**输入示例**
```HTTP
POST https://iot.cloud.tencent.com/api/exploreropen/tokenapi HTTP/1.1
content-type: application/json
{
  "Action": "AppSendShareFamilyInvite",
  "AccessToken": "8b4a70dd16105f******************18edd4e78a3bb8ec",
  "RequestId": "1555507435215",
  "FamilyId":"e0e23a2b33a24652b606ef9107c9a1cf",
  "ToUserID":"123456"
}
```
**输出示例:  成功**
```json
{
"Response": {
  "RequestId": "1555507435215",
  }
}
```
**输出示例:  失败**
```json
{
  "Response": {
    "Error": {
      "Code": "InvalidParameterValue.InvalidAccessToken",
      "Message": "Token无效"
    },
    "RequestId": "1555507435215"
 }
}
```


## 5. 错误码

|错误码|描述|
|---|---|
|InternalError|内部错误|
|InvalidParameterValue|参数取值错误|
|InvalidParameterValue.InvalidAccessToken|Token 无效|
|InvalidParameterValue.NoPermission|用户对该家庭无权限|
