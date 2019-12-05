## 接口概述

### 服务简介
本接口用于识别用户上传照片的车牌号码。

### 计费说明
本接口按实际使用量计费，具体定价请查看 [计费说明](/document/product/641/12399)。

### url 说明
支持 http 和 https 两种协议：

`http://recognition.image.myqcloud.com/ocr/plate`

`https://recognition.image.myqcloud.com/ocr/plate`

## 请求方式
### 请求头 header

| 参数名            |必选| 值                                        | 描述                                       |
| -------------- | -----|----------------------------------- | ---------------------------------------- |
| host           |  是   | recognition.image.myqcloud.com        | 腾讯云文字识别服务器域名                       |
| content-length |  否   | 包体总长度                          | 每个请求的包体大小限制为 6MB，不支持 .gif 类型的动图 | 
| content-type   | 是 |application/json 或者 multipart/form-data    | 标准 json 格式                               |
| authorization  | 是 |鉴权签名             | 用于鉴权的签名，使用 [多次有效签名](/document/product/641/12409) |

#### 请求参数

| 参数名   | 必选 | 类型     | 参数说明                                  |
| ----- | ---- | ------ | ------------------------------------- |
| appid | 是   | string | 接入项目的唯一标识，可在 [账号信息](https://console.cloud.tencent.com/developer) 或 [云 API 密钥](https://console.cloud.tencent.com/cam/capi) 中查看。                                  |
| image | 否   | string | 使用 base64 编码的二进制图片数据。                    |
| url   | 否   | string | 图片的 url, image 和 url 只提供一个即可,如果都提供,只使用 url。 |

#### 返回内容

| 字段         | 类型          | 说明                     |
| ---------- | ----------- | ---------------------- |
| code       | int         | 返回码                    |
| message    | string      | 返回错误消息                 |
| data.items | array(Item) | 识别出的所有字段信息，详见下文 items 说明 |

items 说明

| 字段         | 子字段    | 类型     | 说明        |
| ---------- | ------ | ------ | --------- |
| item       | &nbsp; | string | 字段名称      |
| itemstring | &nbsp; | string | 字段内容      |
| itemcoord  | x      | int    | item框左上角x |
| &nbsp;     | y      | int    | item框左上角y |
| &nbsp;     | width  | int    | item框宽度   |
| &nbsp;     | height | int    | item框高度   |
| itemconf   | &nbsp; | float  | 字段识别结果置信度 |

## 请求示例

#### 使用 url 的请求示例

```
POST /ocr/plate HTTP/1.1
Authorization: FCHXdPTEwMDAwMzc5Jms9QUtJRGVRZDBrRU1yM2J4ZjhRckJi==
Host: recognition.image.myqcloud.com
Content-Length: 80
Content-Type: application/json

{
  "appid":"123456",
  "url":"http://test-123456.image.myqcloud.com/test.jpg"
}
```

#### 使用 image 的请求示例

```
POST /ocr/plate HTTP/1.1
Authorization: FCHXdPTEwMDAwMzc5Jms9QUtJRGVRZDBrRU1yM2J4ZjhRckJi==
Host: recognition.image.myqcloud.com
Content-Length: 49
Content-Type: application/json

{
  "appid":"123456",
  "image":"SALDKHKAFLASD"
}
```

#### 返回示例

```
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 242
Content-Type: text/json

{
"code":0,
"message":"OK",
"items":
    [
        {"item": "车牌", 
          "itemstring": "京NC32A1",
         "itemcoord":{"x" : 0, "y" : 1, "width" : 2, "height" : 3}, 
         "itemconf": 0.99
        },
    ]
} 
```

## 错误码

| 错误码   | 含义                         |
| ----- | -------------------------- |
| 3     | 错误的请求；其中 message:account abnormal,errorno is:2 为账号欠费停服                      |
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
| 21    | 无效参数                       |
| 23    | 请求包体过大                     |
| 24    | 没有权限                       |
| 25    | 您购买的资源已用完                  |
| 107   | 鉴权服务不可用                    |
| 108   | 鉴权服务不可用                    |
| 213   | 内部错误                       |
| -1102 | 图片解码失败                     |
| -1300 | 图片为空                       |
| -1301 | 参数为空                       |
| -1304 | 参数过长                       |
| -1308 | url 图片下载失败                 |
| -5208 | 服务器内部错误                 |
| -9702 | 车牌识别失败                   |


更多其他 API 错误码请看[**错误码说明**](/document/product/641/12410) 。


