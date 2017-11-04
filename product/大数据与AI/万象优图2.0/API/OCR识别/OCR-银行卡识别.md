## 1. 说明
开发者使用功能之前，需要先注册腾讯云账号，添加密钥
OCR接口采用http协议，支持指定图片URL和上传本地图片文件两种方式。
限制说明
(1) 每个请求的包体大小限制为6MB。
(2) 不支持 .gif这类的多帧动图。

## 2. 接口描述

银行卡 OCR 识别，根据用户上传的银行卡图像，返回识别出的银行卡字段信息。
接口：http://recognition.image.myqcloud.com/ocr/bankcard

方法：POST

## 3. 银行卡 OCR

### 3.1 HTTP 请求格式

#### 头部信息

| 参数名称           | 必选   | 类型     | 描述                                       |
| -------------- | ---- | ------ | ---------------------------------------- |
| Host           | 是    | String | recognition.image.myqcloud.com           |
| Content-Length | 是    | Int    | 整个请求包体内容的总长度，单位：字节（Byte）。                |
| Content-Type   | 是    | String | text/json                                |
| Authorization  | 是    | String | 多次有效签名,用于鉴权， 具体生成方式详见[鉴权签名方法](/document/product/460/6968) |

#### 请求包体

| 参数名称  | 必选   | 类型     | 描述                                   |
| ----- | ---- | ------ | ------------------------------------ |
| appid | 必须   | String | 腾讯云的 AppID                           |
| image | 可选   | binary | 图片内容                                 |
| url   | 可选   | String | 图片的url,image和url只提供一个即可，如果都提供，只使用url |

#### 示例—使用图片URL

```
POST /ocr/creditcardocr HTTP/1.1
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
#### 示例—使用图片文件

```
POST /ocr/creditcardocr HTTP/1.1
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


### 3.2 返回值

#### 返回内容

结果具体内容：

返回字段为一个json数组，其中每一项的内容如下：

| 参数         | 类型     | 说明                        |
| ---------- | ------ | ------------------------- |
| code       | Int    | 返回值                       |
| message    | String | 返回消息                      |
| data       | Object | 返回数据                      |
| session_id | String | 相应请求的 session 标识符，可用于结果查询 |
| items      | json数组 | 具体查询数据，内容见下表              |


items（json数组）中每一项的具体内容：

| 参数         | 类型     | 描述                                       |
| ---------- | ------ | ---------------------------------------- |
| item       | String | 字段名称                                     |
| itemstring | String | 字段结果                                     |
| itemcoord  | Object | 字段在图像中的像素坐标，包括左上角坐标 x,y，以及宽、高 width, height |
| itemconf   | Float  | 识别结果对应的置信度                               |




#### 示例
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

## 4. HTTP 返回码

| 错误码  | 内容                         | 含义                   |
| ---- | -------------------------- | -------------------- |
| 400  | HTTP_BAD_REQUEST           | 请求不合法，包体格式错误         |
| 401  | HTTP_UNAUTHORIZED          | 权限验证失败               |
| 403  | HTTP_FORBIDDEN             | 鉴权信息不合法，禁止访问         |
| 404  | HTTP_NOTFOUND              | 请求失败                 |
| 411  | HTTP_REQ_NOLENGTH          | 请求没有指定 ContentLength |
| 413  | HTTP_REQUEST_LARGE         | 请求包体太大               |
| 424  | HTTP_METHOD_NOTFOUND       | 请求的方法没有找到            |
| 500  | HTTP_INTERNAL_SERVER_ERROR | 服务内部错误               |
| 502  | HTTP_BAD_GATEWAT           | 网关错误，计算后台服务不可用       |
| 503  | HTTP_SERVICE_UNAVAILABLE   | 服务不可用                |
| 504  | HTTP_GATEWAY_TIME_OUT      | 后端服务超时或者处理失败         |

#### 协议错误码

| 错误码   | 内容                              | 含义            |
| ----- | ------------------------------- | ------------- |
| -1102 | SDK_IMAGE_DECODE_FAILED         | 图片解码失败        |
| -1300 | ERROR_IMAGE_EMPTY               | 图片为空          |
| -1301 | ERROR_PARAMETER_EMPTY           | 参数为空          |
| -1304 | ERROR_PARAMETER_TOO_LONG        | 参数过长          |
| -5208 | OCR_SERVER_INTERN_ERROR         | 服务器内部错误       |
| -9010 | CREDITCARD_OCR_PREPROCESS_ERROR | 银行卡 OCR 预处理错误 |
| -9011 | CREDITCARD_OCR_RECOG_FAILED     | 银行卡 OCR 识别失败  |

