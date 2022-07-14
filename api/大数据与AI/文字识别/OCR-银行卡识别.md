>!
- 银行卡识别接口全面升级，算法更强、性能更优，支持子账号调用。欢迎立即体验[ 新版银行卡识别](https://cloud.tencent.com/document/product/866/36216)。
- 新老版本的接口计费模式相同，且共享计费阶梯和资源包，您可以在【文字识别控制台】>【[用量统计](https://console.cloud.tencent.com/ocr/stats)】中查看调用情况。
- 老版本接口我们仍继续维护，但不支持新客户开通调用，建议您使用 [新版银行卡识别](https://cloud.tencent.com/document/product/866/36216)，体验更优服务。
## 接口描述
接口请求域名：`https://recognition.image.myqcloud.com/ocr/bankcard`
本接口（bankcard）用于根据用户上传的银行卡图像，返回识别出的银行卡字段信息。开发者使用功能之前，需要先注册腾讯云账号，添加密钥。
>?本接口支持 HTTPS 协议，如果您现在使用的是 HTTP 协议，为了保障您的数据安全，请切换至 HTTPS。

## 请求头 header

| 参数名            |必选| 值                                        | 描述                                       |
| -------------- | -----|----------------------------------- | ---------------------------------------- |
| host           |  是   | recognition.image.myqcloud.com        | 腾讯云文字识别服务器域名。                       |
| content-length |  否   | 包体总长度                          | 每个请求的包体大小限制为6MB，不支持 .gif 类型的动图。 |
| content-type   |  是   |String | 1. 使用 application/json 格式，参数为 url 或 image，其值为图片链接或图片 base64 编码；<br>2. 使用 multipart/form-data 格式，参数为 image，其值为图片的二进制内容。     |
| authorization  |  是   |String | 多次有效签名,用于鉴权， 具体生成方式详见 [鉴权签名方法](https://cloud.tencent.com/document/product/866/17734)。 |
 
## 输入参数

| 参数    | 必选 | 类型     | 说明                                   |
| ----- | ---- | ------ | ------------------------------------ |
| appid | 是   | String |接入项目的唯一标识，可在 [账号信息](https://console.cloud.tencent.com/developer) 或 [云 API 密钥](https://console.cloud.tencent.com/cam/capi) 中查看。                           |
| image | 否   | Binary/String | 图片文件或图片 base64。                                 |
| url   | 否   | String | 图片 url 和 image 同时赋值时，则以 url 指定的图像作为输入。 |

## 输出参数

| 字段         | 类型     | 说明                        |
| ---------- | ------ | ------------------------- |
| code       | Int    | 返回值                       |
| message    | String | 返回消息                      |
| data       | Object | 返回数据                      |
| session_id | String | 相应请求的 session 标识符，可用于结果查询 |
| items      | JSON 数组 | 具体查询数据，内容见下表              |

items 说明：

| 字段         | 类型     | 说明                                       |
| ---------- | ------ | ---------------------------------------- |
| item       | String | 字段名称                                     |
| itemstring | String | 字段结果                                     |
| itemcoord  | Object | 字段在图像中的像素坐标，包括左上角坐标 x、y，以及宽 width、高 height |
| itemconf   | Float  | 识别结果对应的置信度                               |

## 示例
### 输入示例
#### 使用 application/json 
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

#### 使用 multipart/form-dataL
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

### 输出示例
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
| 6     | APPID /存储桶/ URL 不匹配             |
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
| 17    | URL 为空                         |
| 18    | 没有图片或 URL                       |
| 19    | 图片数过多，单次请求最多支持20个 URL 或文件     |
| 20    | 图片过大，单个文件最大支持1MB               |
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
| -9011 | CREDITCARD_OCR_RECOG_FAILED     |
| -9010 | CREDITCARD_OCR_PREPROCESS_ERROR |

更多其他 API 错误码请查看 [错误码说明](https://cloud.tencent.com/document/product/866/17733)。   


