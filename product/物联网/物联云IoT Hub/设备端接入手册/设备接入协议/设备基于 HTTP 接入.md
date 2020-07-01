## 接口描述
- 接口域名：`device-iot.tencentcloudapi.com/pub`（支持 HTTP 和 HTTPS）。
- 设备可以使用本接口通过 HTTP 协议，向指定 Topic 上报消息。
- HTTP 请求仅支持 POST 方法。



## 输入参数

| 参数名称 | 必选 | 类型    |  描述     |
| -------- | ---- | ----- | ----------- |
| deviceName| 是  | string  | 设备名称，驼峰命名   |
| productId | 是 | string | 产品 ID，驼峰命名       |
| topicName | 是 | string | topic 名称，驼峰命名   |
| message   | 是 | string | 消息内容，大小限制16KB     |
| qos       | 是 | int32 | mqtt 消息的 qos |
| nonce     | 是 | int64 | 随机数        |
| timestamp | 是 | int64 | 时间戳（时间误差不超过3600）|
| signature | 是 | string | 签名信息     |

## 签名生成方法

####  通过密钥方式
1. 客户端对参数（deviceName、message、nonce、productId、qos、timestamp、topicName）按字典序升序排序。
2. 客户端对上面参数，按“参数名称 = 参数值 & 参数名称 = 参数值”拼接成字符串。
3. 客户端使用 HMAC-sha256 算法对上一步中获得的字符串进行计算，密钥为 deviceSecret。 
4. 将生成的结果使用 Base64 进行编码，即可获得最终的签名串放入 signature。

####  通过证书方式
1. 客户端对参数（deviceName、message、nonce、productId、requestId、qos、timestamp、topicName）按字典序升序排序。
2. 客户端对上面参数，按“参数名称 = 参数值 & 参数名称 = 参数值”拼接成字符串，对字符串进行 md5 计算，得到信息摘要。
3. 使用私钥（控制台下载）对信息摘要用 RFC 5208（pkcs8）进行数据签名得到签名串，用 Base64 进行编码放入 signature。

## 错误码

| 参数 | 说明             |
| ---- | --------------   |
| 1012 | 参数错误         |
| 2000 | 产品 ID 或设备名错误 |
| 1017 | 签名错误         |
| 1003 | 上报错误         |


## 示例代码

```
curl -i -d 'deviceName=devpublish_test1&productId=W9GMG550YD&topicName=topic-59pw61lo&message={"c":66666666}&nonce=5577006791947779410&timestamp=1561465061&qos=1&signature=2ZV6sRmert0M7Dy%2BTaBYWObs4JCpfblP29B0HMscC3E%3D' http://device-iot.tencentcloudapi.com/pub
```

#### 正确返回
```
{"returnCode":0,"returnMessage":"ok"}
```

#### 错误返回
```
{"returnCode":2000,"returnMessage":"code:ResourceNotFound.ProductNotExist msg:产品不存在。"}
```

