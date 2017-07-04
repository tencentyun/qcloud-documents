## 1. 说明

开发者使用功能之前，需要先注册腾讯云账号，添加密钥，并在万象优图创建bucket。

## 2. 接口概述

OCR接口采用http协议，支持指定图片URL和上传本地图片文件两种方式。

限制说明

(1) 每个请求的包体大小限制为6MB。

(2) 所有接口都为POST方法。

(3) 不支持 .gif这类的多帧动图。

协议头部

所有请求都要求含有下表列出的头部信息

| 参数名            | 值                                        | 描述                                       |
| -------------- | ---------------------------------------- | ---------------------------------------- |
| Host           | recognition.image.myqcloud.com           | 万象优图服务器域名                                |
| Content-Length | 包体总长度                                    | 整个请求包体内容的总长度，单位：字节（Byte）                 |
| Content-Type   | Application/json  或者  Multipart/form-data | 根据不同接口选择                                 |
| Authorization  | 鉴权签名                                     | 用于鉴权的签名，使用多次有效签名。[详情](https://www.qcloud.com/doc/product/275/3805) |

## 3.接口描述

1) 接口
http://recognition.image.myqcloud.com/ocr/drivinglicence

2) 描述
根据用户上传的图像，返回识别出行驶证&驾驶证各字段信息。

目前支持的字段为：

| 行驶证  | 驾驶证  |
| ---- | ---- |
| 车牌号码 | 证号   |
| 车辆类型 | 姓名   |
| 所有人  | 性别   |
| 住址   | 国籍   |
| 使用性质 | 住址   |
| 品牌型号 | 出生日期 |
| 识别代码 | 领证日期 |
| 发动机号 | 准驾车型 |
| 注册日期 | 起始日期 |
| 发证日期 | 有效日期 |

3) 参数

使用image则使用 multipart/form-data格式

不使用image则使用 application/json格式

| 参数名    | 是否必须 | 类型     | 参数说明                                  |
| ------ | ---- | ------ | ------------------------------------- |
| appid  | 必须   | String | 项目ID                                  |
| bucket | 必须   | string | 空间名称                                  |
| type   | 必选   | Int    | 识别类型，0表示行驶证，1表示驾驶证                    |
| image  | 可选   | Binary | 图片内容                                  |
| url    | 可选   | String | 图片的url, image和url只提供一个即可,如果都提供,只使用url |

4) 返回值说明

| 字段              | 类型          | 说明              |
| --------------- | ----------- | --------------- |
| data.session_id | String      | 相应请求的session标识符 |
| data.items      | Array(Item) | 识别出的所有字段信息      |
| code            | Int         | 返回码             |
| message         | String      | 返回错误消息          |

Item说明

| 字段         |        | 类型     | 说明        |
| ---------- | ------ | ------ | --------- |
| item       |        | String | 字段名称      |
| itemstring |        | String | 字段内容      |
| itemconf   |        | Float  | 字段识别结果置信度 |
| itemcoord  | x      | Int    | item框左上角x |
|            | y      | Int    | item框左上角y |
|            | width  | Int    | item框宽度   |
|            | height | Int    | item框高度   |

5) 样例

使用url的请求包:

```
POST /ocr/drivinglicence HTTP/1.1
Authorization: FCHXdPTEwMDAwMzc5Jms9QUtJRGVRZDBrRU1yM2J4ZjhRckJi==
Host: recognition.image.myqcloud.com
Content-Length: 187
Content-Type: application/json

{
  "appid":"123456",
  "bucket":"test",
  "type":1,
  "url":"http://test-123456.image.myqcloud.com/test.jpg"
}
```

使用image的请求包:

```
POST /ocr/drivinglicence HTTP/1.1
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
Content-Disposition: form-data; name="type";

1
----------------acebdf13572468
Content-Disposition: form-data; name="image"; filename="test.jpg"
Content-Type: image/jpeg

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
----------------acebdf13572468--
```

回包:

```
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 404
Content-Type: application/json

{
  "data":{
"items":[
  {
    "item":"姓名",
    "itemstring":"张三",
    "itemconf":0.9,
    "itemcoord":{"x":0,"y":100,"width":40,"height":20},
  },
  {
    "item":"性别",
    "itemstring":"男",
    "itemconf":0.8,
    "itemcoord":{"x":0,"y":80,"width":40,"height":20},
  }

],
    "session_id":"",
  },
  "code":0,
  "message":"OK"
}

```

 

## 3.  返回码

| 错误码   | 含义                       |
| ----- | ------------------------ |
| 3     | 错误的请求                    |
| 4     | 签名为空                     |
| 5     | 签名串错误                    |
| 6     | 签名中的appid/bucket与操作目标不匹配 |
| 9     | 签名过期                     |
| 10    | appid不存在                 |
| 11    | secretid不存在              |
| 12    | appid和secretid不匹配        |
| 13    | 重放攻击                     |
| 14    | 签名校验失败                   |
| 15    | 操作太频繁，触发频控               |
| 16    | Bucket不存在                |
| 21    | 无效参数                     |
| 23    | 请求包体过大                   |
| 24    | 没有权限                     |
| 25    | 您购买的资源已用完                |
| 107   | 鉴权服务不可用                  |
| 108   | 鉴权服务不可用                  |
| 213   | 内部错误                     |
| -1102 | 图片解码失败                   |
| -1300 | 图片为空                     |
| -1301 | 参数为空                     |
| -1304 | 参数过长                     |
| -1308 | 图片下载失败                   |
| -9002 | OCR识别失败                  |

 

 