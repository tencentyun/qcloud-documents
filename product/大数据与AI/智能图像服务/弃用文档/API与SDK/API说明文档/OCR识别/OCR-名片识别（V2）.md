## 接口概述

### 服务简介
名片 OCR 识别，根据用户上传的名片图像，返回识别出的名片字段信息，目前已支持20 多个字段识别，详细字段如下：

姓名、英文姓名、职位、英文职位、部门、英文部门、公司、英文公司、地址、英文地址、邮编、邮箱、网址、手机、电话、传真、QQ、MSN、微信、微博、公司账号、logo、其他。

>注意：
>如果开发者使用的是 V1 版本，请查看 [名片识别（V1）](/document/product/641/12423)。

### 计费说明
本接口按实际使用量计费，具体定价请查看 [计费说明](/document/product/641/12399)。

### url 说明
支持 http 和 https 两种协议：

`http://recognition.image.myqcloud.com/ocr/businesscard`

`https://recognition.image.myqcloud.com/ocr/businesscard`

## 请求方式

### 请求头 header

| 参数名            |必选| 值                                        | 描述                                       |
| -------------- | -----|----------------------------------- | ---------------------------------------- |
| host           |  是   | recognition.image.myqcloud.com        | 腾讯云文字识别服务器域名                       |
| content-length |  否   | 包体总长度                          | 每个请求的包体大小限制为 6MB，不支持 .gif 类型的动图 | 
| content-type   | 是| application/json 或者 multipart/form-data | 根据不同接口选择：<br/>1. 使用图片 url，选择 application/json；<br/>2. 使用图片 image，选择 multipart/form-data。 |
| authorization  | 是| 鉴权签名                                    | 多次有效签名，用于鉴权， 具体生成方式详见[鉴权签名方法](/document/product/641/12409) |

>**注意：**
如选择 multipart/form-data，请使用 http 框架/库推荐的方式设置请求的 content-type，不推荐直接调用 setheader 等方法设置，否则可能导致 boundary 缺失引起请求失败。


### 请求参数

| 参数名       | 必选     | 类型           | 说明                               |
| ------------- | ----------- | ------------- | ---------------------------------  |
| appid         | 是         | string        | 接入项目的唯一标识，可在 [账号信息](https://console.cloud.tencent.com/developer) 或 [云 API 密钥](https://console.cloud.tencent.com/cam/capi) 中查看                 |
| image         | 是   | image/jpeg等 | 图片文件，支持多个。参数名须为 “image[0]”、“image[1]”等 image 开头的字符串。响应 http body 中会按照该字符串的字典序排列。每张图片需指定 filename，filename 的值为可为空，响应 http body 中会返回用户设置的 filename 值。 |
| url_list   | 是   | string 数组 | 图片 url 列表。image 和 url 只提供一个即可；如果都提供，只使用 url   |

## 返回内容

| 字段          | 类型      | 说明           |
| ----------- | ------- | ------------ |
| result_list | json 数组 | 具体查询数据，内容见下表 |

result_list（json 数组）中每一项的具体内容：

| 字段      | 类型     | 说明           |
| ------- | ------ | ------------ |
| code    | int    | 服务器错误码，0 为成功 |
| message | string | 服务器返回的信息     |
| url     | string | 请求参数选择url，则返回当前图片的 url    |
| filename     | string | 请求参数选择image，当前图片的 filname    |
| data    | array(item) | 具体查询数据，内容见下表 |

data字段具体内容：

| 字段               | 类型     | 说明                     |
| ---------------- | ------ | ---------------------- |
| item             | string | 字段字符串                     |
| value            | string | 字段识别出来的信息                    |
| confidence  | double | 字段识别出来的信息的置信度，取值范围[0,1]  |

## 请求示例

### 使用 url 的请求示例

```
POST /ocr/businesscard HTTP/1.1
Authorization: FCHXdPTEwMDAwMzc5Jms9QUtJRGVRZDBrRU1yM2J4ZjhRckJi==
Host: recognition.image.myqcloud.com
Content-Length: 187
Content-Type: application/json

{
  "appid":"123456",
  "bucket":"test",
  "url_list":["http://yoututest-1251966477.cossh.myqcloud.com/mingpian.jpg"]
}
```

### 使用 image 的请求示例 

```
POST /ocr/businesscard HTTP/1.1
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
Content-Disposition: form-data; name="image"; filename="mingpian.jpg"
Content-Type: image/jpeg

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
----------------acebdf13572468--
```

### 返回示例

```
{
    "result_list": [
        {
            "code": 0,
            "message": "OK",
            "filename": "名片2.jpg",
            "data": [
                {
                    "item": "姓名",
                    "value": "温星涛",
                    "confidence": 0.9994000196456908
                },
                {
                    "item": "职位",
                    "value": "解决方案高级架构师",
                    "confidence": 0.9758999943733216
                },
                {
                    "item": "部门",
                    "value": "云产品部",
                    "confidence": 0.9998999834060668
                },
                {
                    "item": "公司",
                    "value": "Tencent腾讯",
                    "confidence": 0.8555999994277954
                },
                {
                    "item": "地址",
                    "value": "成都市高新区天府三街198号腾讯成都大厦A座1层610041",
                    "confidence": 0.5228000283241272
                },
                {
                    "item": "邮箱",
                    "value": "timwen@tencent.com",
                    "confidence": 0.9995999932289124
                },
                {
                    "item": "手机",
                    "value": "+86-18109023170",
                    "confidence": 0.9914000034332277
                },
                {
                    "item": "电话",
                    "value": "9761758",
                    "confidence": 0.9998999834060668
                },
                {
                    "item": "电话",
                    "value": "+86-28-85225111转51468",
                    "confidence": 0.9078999757766724
                },
                {
                    "item": "传真",
                    "value": "+86-28-85980512",
                    "confidence": 0.9944000244140624
                }
            ]
        }
    ]
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
|-1300 |图片为空|
|-1301| 参数为空|
|-1304  | 参数过长|
| -1308 | 图片下载失败                     |
|-5201 | 名片无足够的文本|
|-5202 |名片文本行倾斜角度太大|
|-5203 | 名片模糊|
|-5204 |名片姓名识别失败|
|-5205 | 名片电话识别失败|
|-5206 | 上传图像不是名片|
|-5207| 检测或者识别失败|
|-5208 | 名片 OCR 服务内部出错|


更多其他 API 错误码请看[**错误码说明**](/document/product/641/12410)  。
