## 接口概述

### 服务简介
通用 OCR 技术提供图片整体文字的检测和识别服务，返回文字框位置与文字内容。支持多场景、任意版面下整图文字的识别，以及中英文、字母、数字的识别。
应用场景：印刷文档识别、广告图文字识别、街景店招识别、菜单识别、视频标题识别、互联网头像文字识别等。

### 计费说明
本接口按实际使用量计费，具体定价请查看 [计费说明](/document/product/641/12399)。

### url 说明
支持 http 和 https 两种协议：

`http://recognition.image.myqcloud.com/ocr/general`

`https://recognition.image.myqcloud.com/ocr/general`

## 请求方式

### 请求头 header
所有请求都要求含有以下头部信息：

| 参数名            |必选| 值                                        | 描述                                       |
| -------------- | -----|----------------------------------- | ---------------------------------------- |
| host           |  是   | recognition.image.myqcloud.com        | 腾讯云文字识别服务器域名                       |
| content-length |  否   | 包体总长度                          | 每个请求的包体大小限制为 6MB，不支持 .gif 类型的动图 |
| content-type   | 是|application/json  或者  multipart/form-data | 根据不同接口选择：<br/>1. 使用图片 url，选择 application/json；<br/>2. 使用图片 image，选择 multipart/form-data。      |
| authorization  | 是| 鉴权签名                         | 多次有效签名，用于鉴权，生成方式见 [鉴权签名方法](/document/product/641/12409) |

>**注意：**
如选择 multipart/form-data，请使用 http 框架/库推荐的方式设置请求的 content-type，不推荐直接调用 setheader 等方法设置，否则可能导致 boundary 缺失引起请求失败。

### 请求参数

| 参数名    | 必选 | 类型     | 参数说明                                     |
| ------ | ---- | ------ | ---------------------------------------- |
| appid  | 是   | string | 接入项目的唯一标识，可在 [账号信息](https://console.cloud.tencent.com/developer) 或 [云 API 密钥](https://console.cloud.tencent.com/cam/capi) 中查看                   |
| image  | 否   | binary | 图片内容                                     |
| url    | 否   | string | image 和 url 只提供一个即可；如果都提供，只使用 url |

## 返回内容

| 字段              | 类型          | 说明                |
| --------------- | ----------- | ----------------- |
| data.session_id | string      | 相应请求的 session 标识符 |
| data.items      | array(item) | 识别出的所有字段信息        |
| code            | int         | 错误码               |
| message         | string      | 错误描述              |

item 说明：

| 字段         |   &nbsp;     | 类型          | 说明          |
| ---------- | ------ | ----------- | ----------- |
| itemstring | &nbsp;       | string      | 字段内容        |
| itemcoord  | x      | int         | item 框左上角 x |
|     &nbsp;       | y      | int         | item 框左上角 y |
|     &nbsp;       | width  | int         | item 框宽度    |
|    &nbsp;        | height | int         | item 框高度    |
| words      |    &nbsp;    | array(word) | 每个字的信息      |

words 说明：

| 字段         | 类型     | 说明                      |
| ---------- | ------ | ----------------------- |
| character  | string | 单字的内容                   |
| confidence | float  | 这个字的置信度,取值范围[0,100] |

## 请求示例

### 使用 url 的请求示例

```
POST /ocr/general HTTP/1.1
Authorization: FCHXdPTEwMDAwMzc5Jms9QUtJRGVRZDBrRU1yM2J4ZjhRckJi==
Host: recognition.image.myqcloud.com
Content-Length: 187
Content-Type: application/json

{
  "appid":"123456",
  "bucket":"test",
  "url":"http://test-123456.image.myqcloud.com/test.jpg"
  }
```

### 使用 image 的请求示例

```
POST /ocr/general HTTP/1.1
Authorization: FCHXdPTEwMDAwMzc5Jms9QUtJRGVRZDBrRU1yM2J4ZjhRckJi==
Host: recognition.image.myqcloud.com
Content-Length: 735
Content-Type: multipart/form-data;boundary=--------------acebdf13572468

----------------acebdf13572468
Content-Disposition: form-data; name="appid";

123456
----------------acebdf13572468
Content-Disposition: form-data; name="bucket";

test
----------------acebdf13572468
Content-Disposition: form-data; name="image"; filename="test.jpg"
Content-Type: image/jpeg

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
----------------acebdf13572468--
```

### 返回示例

```
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 404
Content-Type: application/json

{
  "data":{
"items":[
  {
    "itemstring":"手机",
    "itemcoord":{"x":0,"y":100,"width":40,"height":20},
    "words":[
      {"character":"手","confidence":90.9},
      {"character":"机","confidence":93.9}
    ]
  }
],
    "session_id":"",
  },
  "code":0,
  "message":"OK"
}
```

## 错误码

| 错误码   | 含义                         |
| ----- | -------------------------- |
| 3     | 错误的请求；其中 message:account abnormal,errorno is:2 为账号欠费停服                       |
| 4     | 签名为空                       |
| 5     | 签名串错误                      |
| 6     | 签名中的 appid/bucket 与操作目标不匹配 |
| 9     | 签名过期                       |
| 10    | appid 不存在                  |
| 11    | secretid 不存在               |
| 12    | appid 和 secretid 不匹配       |
| 13    | 重放攻击                       |
| 14    | 签名校验失败                     |
| 15    | 操作太频繁，触发频控                 |
| 16    | Bucket不存在                  |
| 21    | 无效参数                       |
| 23    | 请求包体过大                     |
| 24    | 没有权限                       |
| 25    | 您购买的资源已用完                  |
| 107   | 鉴权服务内部错误                   |
| 108   | 鉴权服务不可用                    |
| 213   | 内部错误                       |
| -1102 | 图片解码失败                     |
| -1300 | 图片为空                       |
| -1301 | 参数为空                       |
| -1304 | 参数过长                       |
| -1308 | 图片下载失败                     |
| -9003 | OCR 识别失败                   |

更多其他 API 错误码请看[**错误码说明**](/document/product/641/12410) 。
