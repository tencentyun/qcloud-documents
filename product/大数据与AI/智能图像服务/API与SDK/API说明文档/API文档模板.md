## 简介
介绍这个API的作用是什么，如： 本接口用于识别图片内容信息，并以标签的形式显示。

## 计费说明
请查看[计费说明](/document/product/460/6970)。


## 说明
解释某些用户需要了解的名词概念，如：

| 概念     | 解释               |
| ------ | ---------------- |
| appid  | 项目ID, 接入项目的唯一标识 |
><font color="#0000cc">**注意：** </font>
 如果开发者使用的是 V1 版本，则 appid 为其当时生成的 appid。

## 调用URL
完整的 url ，如：`http://xxx.xxx.xxx.xx`

## 请求方式（如果多个请求方式，则分子项；如果没有，则直接到请求包header项）
### 请求包header
如果需要介绍header，或者有些特殊介绍，如：
人脸核身接口采用 http 协议，支持指定图片 URL 和上传本地图片文件两种方式。

所有请求都要求含有下表列出的头部信息：

| 参数名            | 值                                        | 描述                                       |
| -------------- | ---------------------------------------- | ---------------------------------------- |
| Host           | service.image.myqcloud.com               | 万象优图服务器域名                                |
| Content-Length | 包体总长度                                    | 整个请求包体内容的总长度，单位：字节（Byte）                 |
| Content-Type   | application/json  或者  multipart/form-data | 根据不同接口选择                                 |
| Authorization  | 鉴权签名                                     | 用于[**鉴权**](document/product/641/12409)的签名 |

><font color="#0000cc">**注意：** </font>
 (1) 每个请求的包体大小限制为 6MB；
 (2) 所有接口都为 POST 方法；
 (3) 不支持 .gif 这类的动图。

### 请求参数
介绍API使用的请求参数，如：使用 application/json 格式。

| 参数名    | 是否必须 | 类型     | 说明    |
| ------ | ---- | ------ | ------- |
| appid  | 必须   | string | 项目ID    |
| seq    | 可选   | string | 标识请求序列号 |

### 返回内容
介绍API使用的返回内容，如：

| 字段                 | 类型     | 说明      |
| ------------------ | ------ | ------- |
| data.validate_data | string | 唇语验证字符串 |
| code               | int    | 错误码   |
| message            | string | 错误描述  |

## 示例
介绍该API的示例，如：
### 使用url的请求包:

```
POST /face/idcardcompare HTTP/1.1
Authorization: FCHXdPTEwMDAwMzc5Jms9QUtJRGVRZDBrRU1yM2J4ZjhRckJi==
Host: service.image.myqcloud.com
Content-Length: 187
Content-Type: application/json

{
  "appid":"123456",
  "idcard_number":"110110199909090909",
  "idcard_name":"张三",
  "url":"http://test-123456.image.myqcloud.com/test.jpg"
}
```

### 使用image的请求包:

```
POST /face/idcardcompare HTTP/1.1
Authorization: FCHXdPTEwMDAwMzc5Jms9QUtJRGVRZDBrRU1yM2J4ZjhRckJi==
Host: service.image.myqcloud.com
Content-Length: 735
Content-Type: multipart/form-data;boundary=--------------acebdf13572468

----------------acebdf13572468
Content-Disposition: form-data; name="appid";

123456
----------------acebdf13572468
Content-Disposition: form-data; name="idcard_number";

110110199909090909
----------------acebdf13572468
Content-Disposition: form-data; name="idcard_name";

张三
----------------acebdf13572468
Content-Disposition: form-data; name="image"; filename="test.jpg"
Content-Type: image/jpeg

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
----------------acebdf13572468--
```

### 回包:

```
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 204
Content-Type: application/json

{
  "data":{
    "similarity":100.0,
    "session_id":"",
  },
  "code":0,
  "message":"OK"
}
```


## 错误码
介绍该API对应的错误码，如：

| **错误码** | **含义**                              |
| ------- | ----------------------------------- |
| 3       | 错误的请求                               |
| 4       | 签名为空                                |
| 5       | 签名串错误                               |
| 6       |  APPID /存储桶/ url 不匹配                 |
| 7       | 签名编码失败（内部错误）                        |
| 8       | 签名解码失败（内部错误）                        |
| 9       | 签名过期                                |
| 10      |  APPID 不存在                            |

更多其他 API 错误码请看[**错误码说明**](/document/product/460/8523) 。

## 要注意的地方
1. 英文与非标点的中文之间需要有一个空格。如“使用 CVM 构建和部署应用环境”而不是“使用CVM构建和部署应用环境”；
2. 尽可能使用中文数词，特别是当前后都是中文时。例如：“我们发布了五个产品”；
3. 所有的名词解释请尽量保持一致，比如在返回内容中，code的说明是错误码，message的描述是错误描述。







