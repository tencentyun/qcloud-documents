## 接口概述

### 服务简介
本接口用于根据用户上传的银行卡图像，返回识别出的银行卡字段信息。

开发者使用功能之前，需要先注册腾讯云账号，添加密钥。

### 计费说明
本接口按实际使用量计费，具体定价请查看 [计费说明](/document/product/641/12399)。

### url 说明
支持 http 和 https 两种协议：

`http://recognition.image.myqcloud.com/ocr/bankcard`

`https://recognition.image.myqcloud.com/ocr/bankcard`

## 请求方式

### 请求头 header

| 参数名            |必选| 值                                        | 描述                                       |
| -------------- | -----|----------------------------------- | ---------------------------------------- |
| host           |  是   | recognition.image.myqcloud.com        | 腾讯云文字识别服务器域名                       |
| content-length |  否   | 包体总长度                          | 每个请求的包体大小限制为 6MB，不支持 .gif 类型的动图 |
| content-type   |  是   |string | text/json                                |
| authorization  |  是   |string | 多次有效签名,用于鉴权， 具体生成方式详见 [鉴权签名方法](/document/product/641/12409) |

### 请求参数

| 参数    | 必选 | 类型     | 说明                                   |
| ----- | ---- | ------ | ------------------------------------ |
| appid | 是   | string |接入项目的唯一标识，可在 [账号信息](https://console.cloud.tencent.com/developer) 或 [云 API 密钥](https://console.cloud.tencent.com/cam/capi) 中查看                           |
| image | 否   | binary | 图片内容                                 |
| url   | 否   | string | image和url只提供一个即可；如果都提供，只使用url |

## 返回内容

| 字段         | 类型     | 说明                        |
| ---------- | ------ | ------------------------- |
| code       | int    | 返回值                       |
| message    | string | 返回消息                      |
| data       | object | 返回数据                      |
| session_id | string | 相应请求的 session 标识符，可用于结果查询 |
| items      | json数组 | 具体查询数据，内容见下表              |

items 说明：

| 字段         | 类型     | 说明                                       |
| ---------- | ------ | ---------------------------------------- |
| item       | string | 字段名称                                     |
| itemstring | string | 字段结果                                     |
| itemcoord  | object | 字段在图像中的像素坐标，包括左上角坐标 x,y，以及宽、高 width, height |
| itemconf   | float  | 识别结果对应的置信度                               |

## 请求示例
### 使用 url 的请求示例

```
POST /ocr/bankcard HTTP/1.1
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
POST /ocr/bankcard HTTP/1.1
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
Content-Length: 932
Content-Type: application/json

{
    "code": 0,
    "message": "OK",
    "data": {
        "session_id": "10000011579925413",
        "items": [
            {
                "item": "卡号",
                "itemcoord": {
                    "x": 28,
                    "y": 101,
                    "width": 244,
                    "height": 22
                },
                "itemconf": 0.9542132019996644,
                "itemstring": "514958888888888",
                "coords": [],
                "words": [],
                "candword": []
            },
            {
                "item": "卡类型",
                "itemcoord": {
                    "x": 10,
                    "y": 10,
                    "width": 10,
                    "height": 10
                },
                "itemconf": 0.9542132019996644,
                "itemstring": "贷记卡",
                "coords": [],
                "words": [],
                "candword": []
            },
            {
                "item": "卡名字",
                "itemcoord": {
                    "x": 10,
                    "y": 30,
                    "width": 10,
                    "height": 10
                },
                "itemconf": 0.9542132019996644,
                "itemstring": "中银万事达信用卡",
                "coords": [],
                "words": [],
                "candword": []
            },
            {
                "item": "银行信息",
                "itemcoord": {
                    "x": 10,
                    "y": 50,
                    "width": 10,
                    "height": 10
                },
                "itemconf": 0.9542132019996644,
                "itemstring": "中国银行(01040000)",
                "coords": [],
                "words": [],
                "candword": []
            },
            {
                "item": "有效期",
                "itemcoord": {
                    "x": 117,
                    "y": 137,
                    "width": 55,
                    "height": 14
                },
                "itemconf": 0.928840160369873,
                "itemstring": "08/2008",
                "coords": [],
                "words": [],
                "candword": []
            }
        ]
    }
}
```


## 错误码

| 错误码   | 含义                              |
| ----- | ------------------------------- |
| 3     | 错误的请求；其中 message:account abnormal,errorno is:2 为账号欠费停服   |
| 4     | 签名为空                            |
| 5     | 签名串错误                           |
| 6     | APPID /存储桶/ url 不匹配             |
| 7     | 签名编码失败（内部错误）                    |
| 8     | 签名解码失败（内部错误）                    |
| 9     | 签名过期                            |
| 10    | APPID 不存在                       |
| 11    | SecretId 不存在                    |
| 12    | APPID 不匹配                       |
| 13    | 重放攻击                            |
| 14    | 签名失败                            |
| 15    | 操作太频繁，触发频控                      |
| 16    | 存储桶不存在                          |
| 17    | url  为空                         |
| 18    | 没有图片或 url                       |
| 19    | 图片数过多，单次请求最多支持 20 个 url 或文件     |
| 20    | 图片过大，单个文件最大支持 1MB               |
| 21    | 无效的参数                           |
| 200   | 内部打包失败                          |
| 201   | 内部解包失败                          |
| 202   | 内部链接失败                          |
| 203   | 内部处理超时                          |
| -1102 | SDK_IMAGE_DECODE_FAILED         |
| -1300 | ERROR_IMAGE_EMPTY               |
| -1301 | ERROR_PARAMETER_EMPTY           |
| -1304 | ERROR_PARAMETER_TOO_LONG        |
| -5208 | OCR_SERVER_INTERN_ERROR         |
| -9010 | CREDITCARD_OCR_PREPROCESS_ERROR |
| -9011 | CREDITCARD_OCR_RECOG_FAILED     |

更多其他 API 错误码请看[错误码说明](/document/product/641/12410) 


