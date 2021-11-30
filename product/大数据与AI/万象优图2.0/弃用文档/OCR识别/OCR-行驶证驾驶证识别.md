## 简介
本接口用于根据用户上传的图像，识别出行驶证或驾驶证的各字段信息。

开发者使用功能之前，需要先注册腾讯云账号，添加密钥，并在万象优图创建bucket。

## 计费说明
通用 OCR 目前正处于免费公测阶段，会在12月1日开始计费，第一次扣费为2018年1月3~5日。
请查看[计费说明](/document/product/460/6970)。


## 说明
| 概念    | 解释              |
| ----- | --------------- |
| appid | 项目ID, 接入项目的唯一标识 |
><font color="#0000cc">**注意：** </font>
> 如果开发者使用的是 V1 版本，则 appid 为其当时生成的 appid。

## 调用URL
`http://recognition.image.myqcloud.com/ocr/drivinglicence`

## 请求包header
接口采用 http 协议，支持指定图片 URL 和上传本地图片文件两种方式。
所有请求都要求含有下表列出的头部信息：

| 参数名            | 值                                        | 描述                                       |
| -------------- | ---------------------------------------- | ---------------------------------------- |
| Host           | service.image.myqcloud.com               | 万象优图服务器域名                                |
| Content-Length | 包体总长度                                    | 整个请求包体内容的总长度，单位：字节（Byte）                 |
| Content-Type   | application/json  或者  multipart/form-data | 根据不同接口选择                                 |
| Authorization  | 鉴权签名                                     | 用于[**鉴权**](https://cloud.tencent.com/doc/product/275/3805)的签名 |

><font color="#0000cc">**注意：** </font>
> (1) 每个请求的包体大小限制为 6MB。
> (2) 所有接口都为 POST 方法。
> (3) 不支持 .gif 这类的动图。

## 请求参数
使用 image 则使用 multipart/form-data 格式，不使用 image 则使用 application/json 格式。

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
|      | 红章   |


| 参数名    | 是否必须 | 类型     | 说明                                       |
| ------ | ---- | ------ | ---------------------------------------- |
| appid  | 必须   | string | 项目ID                                     |
| bucket | 必须   | string | 空间名称                                     |
| type   | 必选   | int    | 识别类型，0 表示行驶证，1 表示驾驶证识别                   |
| image  | 可选   | binary | 图片内容                                     |
| url    | 可选   | string | 图片的 url, image 和 url 只提供一个即可，如果都提供，只使用 url |

## 返回内容

| 字段              | 类型          | 说明                |
| --------------- | ----------- | ----------------- |
| data.session_id | string      | 相应请求的 session 标识符 |
| data.items      | array(Item) | 识别出的所有字段信息        |
| code            | int         | 返回码               |
| message         | string      | 返回错误消息            |

Item说明

| 字段         |        | 类型     | 说明                    |
| ---------- | ------ | ------ | --------------------- |
| item       |        | string | 字段名称                  |
| itemstring |        | string | 字段内容                  |
| itemconf   |        | float  | 字段识别结果置信度[0.0, 100.0] |
| itemcoord  | x      | int    | item 框左上角 x           |
|            | y      | int    | item 框左上角 y           |
|            | width  | int    | item 框宽度              |
|            | height | int    | item 框高度              |

## 示例

### 使用 url 的请求包

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

### 使用 image 的请求包

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

### 回包

```
{
    "code": 0,
    "message": "OK",
    "data": {
        "session_id": "10000018324840",
        "items": [
            {
                "item": "证号",
                "itemcoord": {
                    "x": 226,
                    "y": 66,
                    "width": 194,
                    "height": 30
                },
                "itemconf": 0.9999638199806212,
                "itemstring": "342221199005033256"
            },
            {
                "item": "姓名",
                "itemcoord": {
                    "x": 84,
                    "y": 98,
                    "width": 93,
                    "height": 26
                },
                "itemconf": 0.999157190322876,
                "itemstring": "张三"
            },
            {
                "item": "性别",
                "itemcoord": {
                    "x": 291,
                    "y": 100,
                    "width": 23,
                    "height": 27
                },
                "itemconf": 0.9999893307685852,
                "itemstring": "男"
            },
            {
                "item": "国籍",
                "itemcoord": {
                    "x": 388,
                    "y": 100,
                    "width": 44,
                    "height": 28
                },
                "itemconf": 0.9999999403953552,
                "itemstring": "中国"
            },
            {
                "item": "住址",
                "itemcoord": {
                    "x": 87,
                    "y": 126,
                    "width": 286,
                    "height": 30
                },
                "itemconf": 0.5020201206207275,
                "itemstring": "深圳市南山区万利达大厦"
            },
            {
                "item": "出生日期",
                "itemcoord": {
                    "x": 224,
                    "y": 195,
                    "width": 106,
                    "height": 25
                },
                "itemconf": 0.999338924884796,
                "itemstring": "1990-05-03"
            },
            {
                "item": "领证日期",
                "itemcoord": {
                    "x": 249,
                    "y": 226,
                    "width": 112,
                    "height": 26
                },
                "itemconf": 0.9999741315841676,
                "itemstring": "2014-12-25"
            },
            {
                "item": "准驾车型",
                "itemcoord": {
                    "x": 262,
                    "y": 261,
                    "width": 58,
                    "height": 27
                },
                "itemconf": 0.9999993443489076,
                "itemstring": "C1"
            },
            {
                "item": "起始日期",
                "itemcoord": {
                    "x": 122,
                    "y": 291,
                    "width": 111,
                    "height": 26
                },
                "itemconf": 0.9859412312507628,
                "itemstring": "2014-12-25"
            },
            {
                "item": "有效日期",
                "itemcoord": {
                    "x": 266,
                    "y": 294,
                    "width": 113,
                    "height": 27
                },
                "itemconf": 0.9921129941940308,
                "itemstring": "2020-12-25"
            },
            {
                "item": "红章",
                "itemcoord": {
                    "x": 52,
                    "y": 186,
                    "width": 110,
                    "height": 100
                },
                "itemconf": 0.9392985105514526,
                "itemstring": "深圳市公安局交通管理局"
            }
        ]
    }
}

```



## 错误码

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
| 107   | 鉴权服务内部错误                 |
| 108   | 鉴权服务不可用                  |
| 213   | 内部错误                     |
| -1102 | 图片解码失败                   |
| -1300 | 图片为空                     |
| -1301 | 参数为空                     |
| -1304 | 参数过长                     |
| -1308 | 图片下载失败                   |
| -9001 | 请求 type 错误，不是 0，1        |
| -9002 | 识别失败                     |
| -9005 | 图片无效                     |
| -9006 | 预处理失败                    |

更多其他 API 错误码请看[**错误码说明**](/document/product/460/8523) 。

 

 