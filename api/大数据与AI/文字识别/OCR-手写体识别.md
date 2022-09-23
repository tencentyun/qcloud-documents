
>!
- 通用手写体识别接口全面升级，算法更强、性能更优，支持子账号调用。欢迎立即体验 [新版通用手写体识别](https://cloud.tencent.com/document/product/866/36212)。
- 新老版本的接口计费模式相同，且共享计费阶梯和资源包，您可以在【文字识别控制台】>【[用量统计](https://console.cloud.tencent.com/ocr/stats)】中查看调用情况。
- 老版本接口我们仍继续维护，但不支持新客户开通调用，建议您使用 [新版通用手写体识别](https://cloud.tencent.com/document/product/866/36212)，体验更优服务。
## 接口描述
接口请求域名：`https://recognition.image.myqcloud.com/ocr/handwriting`
本接口（handwriting）用于手写体识别。根据用户上传的图像，返回识别出的字段信息。
>?本接口支持 HTTPS 协议，如果您现在使用的是 HTTP 协议，为了保障您的数据安全，请切换至 HTTPS。

## 请求头 header

| 参数名            |必选| 值                                        | 描述                                       |
| -------------- | -----|----------------------------------- | ---------------------------------------- |
| host           |  是   | recognition.image.myqcloud.com        | 腾讯云文字识别服务器域名。                       |
| content-length |  否   | 包体总长度                          | 每个请求的包体大小限制为6MB，不支持 .gif 类型的动图。 |
| content-type   | 是|application/json 或 multipart/form-data | 根据不同接口选择：<br/>1. 使用 application/json 格式，参数为 url 或  image，其值为图片链接或图片 base64 编码；<br>2. 使用 multipart/form-data 格式，参数为 image，其值为图片的二进制内容。|
| authorization  |是| 鉴权签名                                    | 多次有效签名，用于鉴权，生成方式见 [鉴权签名方法](https://cloud.tencent.com/document/product/866/17734)。|

>!如选择 multipart/form-data，请使用 HTTP 框架/库推荐的方式设置请求的 content-type，不推荐直接调用 setheader 等方法设置，否则可能导致 boundary 缺失引起请求失败。

## 输入参数

| 参数名称   | 必选 | 类型            | 说明                                       |
| ------ | ---- | ------------- | ---------------------------------------- |
| appid | 是   | String        | 接入项目的唯一标识，可在 [账号信息](https://console.cloud.tencent.com/developer) 或 [云 API 密钥](https://console.cloud.tencent.com/cam/capi) 中查看。                                 |
| image  | 否   |  Binary/String | 图片文件 或 图片 base64。                |
| url    | 否   | String        | 图片 url 和 image 同时赋值时，则以 url 指定的图像作为输入。 |

## 输出参数

| 字段         | 类型          | 说明         |
| ---------- | ----------- | ---------- |
| code       | Int         | 返回状态值      |
| message    | String      | 返回错误消息     |
| data.items | Array(item) | 识别出的所有字段信息 |

item 说明：

| 字段         | 类型          | 说明                                       |
| ---------- | ----------- | ---------------------------------------- |
| itemstring | String      | 字段字符串                                    |
| itemcoord  | Object      | 字段在图像中的像素坐标，包括左上角坐标 x、y，以及宽、高 width,height |
| words      | Array(word) | 字段识别出来的每个字的信息                            |

words 说明：

| 字段         | 类型     | 说明                             |
| ---------- | ------ | ------------------------------ |
| character  | String | 识别出的单字字符                       |
| confidence | Float  | 识别出的单字字符对应的置信度，取值范围[0,100] |

## 示例
### 输入示例
#### 使用 url 
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

#### 使用 image 
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


### 输出示例
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
| 3     | 错误的请求；其中 message:account abnormal,errorno is:2为账号欠费停服                       |
| 4     | 签名为空                       |
| 5     | 签名串错误                      |
| 6     | 签名中的 APPID/Bucket 与操作目标不匹配 |
| 9     | 签名过期                       |
| 10    | APPID 不存在                  |
| 11    | SecretId 不存在               |
| 12    | APPID和 SecretId 不匹配       |
| 13    | 重放攻击                       |
| 14    | 签名校验失败                     |
| 15    | 操作太频繁，触发频控                 |
| 16    | Bucket 不存在                  |
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
| -9011 | 识别失败                       |
| -1308 | 图片下载失败                     |


更多其他 API 错误码请查看 [错误码说明](https://cloud.tencent.com/document/product/866/17733)。  
