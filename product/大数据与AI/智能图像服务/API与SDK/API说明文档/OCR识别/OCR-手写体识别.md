## 接口概述

### 服务简介
手写体 OCR 识别，根据用户上传的图像，返回识别出的字段信息。

### 计费说明
本接口按实际使用量计费，具体定价请查看 [计费说明](/document/product/641/12399)。

### url 说明
支持 http 和 https 两种协议：

`http://recognition.image.myqcloud.com/ocr/handwriting`

`https://recognition.image.myqcloud.com/ocr/handwriting`

## 请求方式

### 请求头 header

| 参数名            |必选| 值                                        | 描述                                       |
| -------------- | -----|----------------------------------- | ---------------------------------------- |
| host           |  是   | recognition.image.myqcloud.com        | 腾讯云文字识别服务器域名                       |
| content-length |  否   | 包体总长度                          | 每个请求的包体大小限制为 6MB，不支持 .gif 类型的动图 |
| content-type   | 是|application/json 或 multipart/form-data | 根据不同接口选择：<br/>1. 使用图片 url，选择 application/json；<br/>2. 使用图片 image，选择 multipart/form-data。         |
| authorization  |是| 鉴权签名                                    | 多次有效签名，用于鉴权，生成方式见 [鉴权签名方法](/document/product/641/12409)|

>**注意：**
如选择 multipart/form-data，请使用 http 框架/库推荐的方式设置请求的 content-type，不推荐直接调用 setheader 等方法设置，否则可能导致 boundary 缺失引起请求失败。

### 请求参数

| 参数名称   | 必选 | 类型            | 说明                                       |
| ------ | ---- | ------------- | ---------------------------------------- |
| appid | 是   | string        | 接入项目的唯一标识，可在 [账号信息](https://console.cloud.tencent.com/developer) 或 [云 API 密钥](https://console.cloud.tencent.com/cam/capi) 中查看                                 |
| image  | 否   | binary | 图片文件，支持多个                  |
| url    | 否   | String        | image 和 url 只提供一个即可；如果都提供，只使用 url |

## 返回内容

| 字段         | 类型          | 说明         |
| ---------- | ----------- | ---------- |
| code       | Int         | 返回状态值      |
| message    | String      | 返回错误消息     |
| data.items | array(item) | 识别出的所有字段信息 |

item 说明：

| 字段         | 类型          | 说明                                       |
| ---------- | ----------- | ---------------------------------------- |
| itemstring | string      | 字段字符串                                    |
| itemcoord  | object      | 字段在图像中的像素坐标，包括左上角坐标 x,y，以及宽、高 width,height |
| words      | array(word) | 字段识别出来的每个字的信息                            |

words 说明：

| 字段         | 类型     | 说明                             |
| ---------- | ------ | ------------------------------ |
| character  | string | 识别出的单字字符                       |
| confidence | float  | 识别出的单字字符对应的置信度，取值范围[0,100] |

## 请求示例

### 使用 url 的请求示例

```
POST /ocr/handwriting HTTP/1.1
Authorization: FCHXdPTEwMDAwMzc5Jms9QUtJRGVRZDBrRU1yM2J4ZjhRckJi==
Host: recognition.image.myqcloud.com
Content-Length: 187
Content-Type: application/json

{
  "appid":"123456",
  "bucket":"test",
  "url":"http://test-1254540501.cosgz.myqcloud.com/%E6%89%8B%E5%86%99%E4%BD%93.jpg"
}
```

### 使用 image 的请求示例 

```
POST /ocr/handwriting HTTP/1.1
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
{
    "code": 0,
    "message": "OK",
    "data": {
        "session_id": "10000011386698236",
        "items": [
            {
                "itemcoord": {
                    "x": 37,
                    "y": 22,
                    "width": 221,
                    "height": 40
                },
                "itemstring": "只要有百分之一的希些",
                "coords": [],
                "words": [
                    {
                        "character": "只",
                        "confidence": 0.9995492100715636
                    },
                    {
                        "character": "要",
                        "confidence": 0.9999183416366576
                    },
                    {
                        "character": "有",
                        "confidence": 0.9975007176399232
                    },
                    {
                        "character": "百",
                        "confidence": 0.9886131286621094
                    },
                    {
                        "character": "分",
                        "confidence": 0.8933222889900208
                    },
                    {
                        "character": "之",
                        "confidence": 0.9992995262145996
                    },
                    {
                        "character": "一",
                        "confidence": 0.8288528323173523
                    },
                    {
                        "character": "的",
                        "confidence": 0.999326467514038
                    },
                    {
                        "character": "希",
                        "confidence": 0.959851086139679
                    },
                    {
                        "character": "些",
                        "confidence": 0.3065926730632782
                    }
                ],
                "candword": []
            },
            {
                "itemcoord": {
                    "x": 37,
                    "y": 59,
                    "width": 254,
                    "height": 37
                },
                "itemstring": "涿会付头百分动+九的多力t",
                "coords": [],
                "words": [
                    {
                        "character": "涿",
                        "confidence": 0.330208957195282
                    },
                    {
                        "character": "会",
                        "confidence": 0.9987956285476684
                    },
                    {
                        "character": "付",
                        "confidence": 0.9981868863105774
                    },
                    {
                        "character": "头",
                        "confidence": 0.5886265635490418
                    },
                    {
                        "character": "百",
                        "confidence": 0.9990888833999634
                    },
                    {
                        "character": "分",
                        "confidence": 0.9986497759819032
                    },
                    {
                        "character": "动",
                        "confidence": 0.6296136379241943
                    },
                    {
                        "character": "+",
                        "confidence": 0.865349292755127
                    },
                    {
                        "character": "九",
                        "confidence": 0.9954916834831238
                    },
                    {
                        "character": "的",
                        "confidence": 0.9976463913917542
                    },
                    {
                        "character": "多",
                        "confidence": 0.505245566368103
                    },
                    {
                        "character": "力",
                        "confidence": 0.6335962414741516
                    },
                    {
                        "character": "t",
                        "confidence": 0.3001934289932251
                    }
                ],
                "candword": []
            },
            {
                "itemcoord": {
                    "x": 32,
                    "y": 88,
                    "width": 227,
                    "height": 38
                },
                "itemstring": "让它变或百分百的现实",
                "coords": [],
                "words": [
                    {
                        "character": "让",
                        "confidence": 0.97903972864151
                    },
                    {
                        "character": "它",
                        "confidence": 0.9997988343238832
                    },
                    {
                        "character": "变",
                        "confidence": 0.9956278800964356
                    },
                    {
                        "character": "或",
                        "confidence": 0.5307473540306091
                    },
                    {
                        "character": "百",
                        "confidence": 0.9948757290840148
                    },
                    {
                        "character": "分",
                        "confidence": 0.9949339032173156
                    },
                    {
                        "character": "百",
                        "confidence": 0.9808925986289978
                    },
                    {
                        "character": "的",
                        "confidence": 0.8506680130958557
                    },
                    {
                        "character": "现",
                        "confidence": 0.9439561367034912
                    },
                    {
                        "character": "实",
                        "confidence": 0.997634768486023
                    }
                ],
                "candword": []
            },
            {
                "itemcoord": {
                    "x": 57,
                    "y": 130,
                    "width": 33,
                    "height": 18
                },
                "itemstring": "an",
                "coords": [],
                "words": [
                    {
                        "character": "a",
                        "confidence": 0.3443509638309479
                    },
                    {
                        "character": "n",
                        "confidence": 0.6972714066505432
                    }
                ],
                "candword": []
            }
        ]
    }
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
| -9011 | 识别失败                       |


更多其他 API 错误码请看 [**错误码说明**](/document/product/641/12410)  。
