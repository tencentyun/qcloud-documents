## 简介
通用 OCR 技术提供图片整体文字的检测和识别服务，返回文字框位置与文字内容。支持多场景、任意版面下整图文字的识别，以及中英文、字母、数字的识别。被广泛应用于印刷文档识别、广告图文字识别、街景店招识别、菜单识别、视频标题识别、互联网头像文字识别等。

## 计费说明
通用印刷体识别目前正处于免费公测阶段，会在11月1日开始计费，第一次扣费为12月份3~5日。
请查看[计费说明](/document/product/460/6970)。
## 说明
| 概念    | 解释              |
| ----- | --------------- |
| appid | 项目ID, 接入项目的唯一标识 |
><font color="#0000cc">**注意：** </font>
> 如果开发者使用的是 V1 版本，则 appid 为其当时生成的 appid。

## 调用URL
`http://recognition.image.myqcloud.com/ocr/general`

## 请求包header
接口采用 http 协议，支持指定图片 URL 和上传本地图片文件两种方式。
所有请求都要求含有下表列出的头部信息：

| 参数名            | 值                                        | 描述                                       |
| -------------- | ---------------------------------------- | ---------------------------------------- |
| Host           | recognition.image.myqcloud.com           | 万象优图服务器域名                                |
| Content-Length | 包体总长度                                    | 整个请求包体内容的总长度，单位：字节（Byte）                 |
| Content-Type   | application/json  或者  multipart/form-data | 根据不同接口选择                                 |
| Authorization  | 鉴权签名                                     | 用于[**鉴权**](https://cloud.tencent.com/doc/product/275/3805)的签名 |

><font color="#0000cc">**注意：** </font>
> (1) 每个请求的包体大小限制为 6MB。
> (2) 所有接口都为 POST 方法。
> (3) 不支持 .gif 这类的动图。



## 请求参数

使用image则使用 multipart/form-data格式

不使用image则使用 application/json格式

| 参数名    | 是否必须 | 类型     | 参数说明                                     |
| ------ | ---- | ------ | ---------------------------------------- |
| appid  | 必须   | string | 项目ID                                     |
| bucket | 必须   | string | 空间名称                                     |
| image  | 可选   | binary | 图片内容                                     |
| url    | 可选   | string | 图片的 url , image 和 url 只提供一个即可，如果都提供，只使用 url |

## 返回内容

| 字段              | 类型          | 说明                |
| --------------- | ----------- | ----------------- |
| data.session_id | string      | 相应请求的 session 标识符 |
| data.items      | array(item) | 识别出的所有字段信息        |
| code            | int         | 错误码               |
| message         | string      | 错误描述              |

Item说明

| 字段         |        | 类型          | 说明          |
| ---------- | ------ | ----------- | ----------- |
| itemstring |        | string      | 字段内容        |
| itemcoord  | x      | int         | item 框左上角 x |
|            | y      | int         | item 框左上角 y |
|            | width  | int         | item 框宽度    |
|            | height | int         | item 框高度    |
| words      |        | array(word) | 每个字的信息      |

word说明

| 字段         | 类型     | 说明                      |
| ---------- | ------ | ----------------------- |
| character  | string | 单字的内容                   |
| confidence | float  | 这个字的置信度,取值范围[0.0,100.0] |

## 示例

### 使用 url 的请求包

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
```

### 使用 image 的请求包

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

### 回包

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
| 3     | 错误的请求                      |
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
| -9003 | OCR 识别失败                   |

更多其他 API 错误码请看[**错误码说明**](/document/product/460/8523) 。