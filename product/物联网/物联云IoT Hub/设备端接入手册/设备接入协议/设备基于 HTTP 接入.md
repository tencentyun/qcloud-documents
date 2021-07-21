## 参数说明

设备上报消息时需携带 ProductId、DeviceName 和 TopicName 向平台发起 `http/https` 请求，请求接口及说明参数如下：

- 请求的 URL 为：
  ``
  https://ap-guangzhou.gateway.tencentdevices.com/device/publish
  ``
  ``
  http://ap-guangzhou.gateway.tencentdevices.com/device/publish
  ``

- 请求方式：Post

### 请求参数

| 参数名称        | 必选 | 类型    | 描述                                                         |
| --------------- | ---- | ------- | ------------------------------------------------------------ |
| ProductId       | 是   | String  | 产品 Id                                                     |
| DeviceName      | 是   | String  | 设备名称                                                     |
| TopicName       | 是   | String  | 发布消息的 Topic 名称                                          |
| Payload         | 是   | String  | 发布消息的内容                                               |
| PayloadEncoding | 否   | String  | 发布消息的编码。目前只支持base64编码，不传默认发送原始的消息内容 |
| Qos             | 是   | Integer | 消息 Qos 等级                                                  |

>? 接口只支持 application/json 格式。

### 签名生成

对请求报文进行签名分为两种，密钥认证使用 HMAC-sha256 算法，证书认证使用 RSA_SHA256 算法，详情请参见 [签名方法](https://cloud.tencent.com/document/product/634/56319)。

### 平台返回参数

| 参数名称  | 类型   | 描述   |
| --------- | ------ | ------ |
| RequestId | String | 请求 Id |

## 示例代码

#### 请求包

```
POST https://ap-guangzhou.gateway.tencentdevices.com/device/publish
Content-Type: application/json
Host: ap-guangzhou.gateway.tencentdevices.com
X-TC-Algorithm: HmacSha256
X-TC-Timestamp: 155****065
X-TC-Nonce: 5456
X-TC-Signature: 2230eefd229f582d8b1b891af7107b915972407****78ab3738f756258d7652c
{"DeviceName":"AAAAAA","Payload":"123","ProductId":"G8N****AHB","Qos":1,"TopicName":"G8N****AHB/AAAAAA/data"}
```

#### 返回包
<dx-codeblock>
:::  json
{
  "Response": {
    "RequestId": "f4da4f1f-d72e-40f1-****-349fc0072ba0"
  }
}
:::
</dx-codeblock>







