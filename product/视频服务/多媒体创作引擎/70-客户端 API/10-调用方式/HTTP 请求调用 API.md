当客户端用户需要访问多媒体创作引擎相关资源时，为简化开发者的工作，多媒体创作引擎提供了客户端 API 以及配套的 SDK。客户端 API 的调用方式如下所示：
![](https://qcloudimg.tencent-cloud.cn/raw/bb2dd0dfc11a62a1a8aa2df26251f0ca.png)
1. 客户端请访问签名。
2. 服务端生成签名并返回给客户端。
3. 客户端发起登录，换取长期票据。
4. 调用 [客户端 API](https://cloud.tencent.com/document/product/1156/50861)。

具体流程如下。
>! 如非必要，建议您使用 [客户端 SDK](https://cloud.tencent.com/document/product/1156/50899) 访问客户端 API，而非通过 HTTP 请求直接裸调接口。

## 步骤1：申请访问签名[](id:step1)
客户端携带用户身份标识（UserId）向自身后台申请访问签名。

## 步骤2：获取生成签名[](id:step2)
开发者服务端在对客户端请求进行必要验证之后，生成客户端访问签名（Signature），并返回给客户端。签名中`action`字段值为`Login`，详情请参见 [签名算法](https://cloud.tencent.com/document/product/1156/43777) 及 [签名示例](https://cloud.tencent.com/document/product/1156/43778)。

## 步骤3：通过签名换取票据[](id:step3)
客户端使用使用服务端返回的 Signature，调用如下接口换取长期鉴权票据，请求方式为 HTTP GET。请求结构如下：
```bash
GET https://open.cme.qcloud.com?signature=<Signature> HTTP/1.1
```
如果 Signature 校验成功，应答结果如下：
```javascript
{
  "Code": "Success",
  "Message": "成功",
  "EnglishMessage": "OK",
  "Data": {
    "AppId": 123,
    "Platform": "<Platform>",
    "UserId": "<UserId>",
    "Authorization": "<Authorization>"
  }
}
```
如果 Signature 校验失败，应答结果如下：
```javascript
{
  "Code": "SignatureVerifyFail",
  "Message": "签名校验失败",
  "EnglishMessage": "Signature Verify Fail"
}
```

## 步骤4：调用客户端 API[](id:step4)
- 以 HTTP POST 方式发起请求，格式如下：
```bash
POST https://web-paas-api.cme.qcloud.com/PaaS/<ActionClass>/<ActionName>?auth=<Authorization> HTTP/1.1

{
    <RequestBody>
}
```
其中：
	- `ActionClass`为接口分类。
	- `ActionName`为接口名称。
	- `Authorization`为 [步骤3](#step3) 获取的长期票据。
	- `RequestBody`为具体请求内容，格式为 JSON。
	
接口应答内容为 JSON，形式如下：
```bash
{
    "Code": "<Code>",
    "Message": "<Message>",
    "EnglishMessage": "<EnglishMessage>",
    "Data" : {
        <Data>
        }
}
```

其中：
	- `Code`为错误码。Success 为成功，其余为失败。详情请参见 [错误码](https://cloud.tencent.com/document/product/1156/40361)。<!-- 具体参见 TODO。 -->
	- `Message`为中文错误信息。
	- `EnglishMessage`为英文错误信息。
	- `Data`为接口具体应答内容。

以删除媒体接口为例，其请求如下：
```bash
POST https://web-paas-api.cme.qcloud.com/PaaS/Material/DeleteMaterial?auth=<Authorization> HTTP/1.1
{
    "MaterialId": "38192156030633420589"
}
```

如果请求成功，应答如下：
```json
{
    "Code": "Success",
    "EnglishMessage": "success",
    "Message": "成功"
}
```

