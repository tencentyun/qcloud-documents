说明：该接口的费用可查看[文档](/document/product/460/6970)。按使用量进行月结。

## 1. 描述

OCR接口采用http协议，支持多URL和多本地图片文件,每个请求最多支持20张图片或url。
接口：http://service.image.myqcloud.com/ocr/namecard
方法：POST

## 2. 使用图片URL
### 2.1 请求内容

**请求语法:**

```
POST /ocr/namecard HTTP/1.1
Authorization: Signature
Host: service.image.myqcloud.com
Content-Length: ContentLength
Content-Type: "application/json"

{
    "appid": appid,
"bucket": "bucket",
"ret_image": ret,
    "url_list": [
        "url",
        "url"
    ]
}
```

**请求包http header:**

| 参数             | 是否必选 | 描述                                   |
| -------------- | ---- | ------------------------------------ |
| Host           | 是    | 访问域名，service.image.myqcloud.com      |
| Authorization  | 是    | 鉴权签名，详见[鉴权文档](/doc/product/460/6968) |
| Content-Type   | 是    | 标准application/json                   |
| Content-Length | 是    | http body总长度                         |

**请求包http body:**

| 参数        | 是否必选 | 类型     | 描述           |
| --------- | ---- | ------ | ------------ |
| appid     | 是    | string | 业务id         |
| bucket    | 是    | string | 图片空间         |
| ret_image | 是    | int    | 0不返回图片，1返回图片 |
| url_list  | 是    | string | 图片url列表      |

### 2.2  返回内容

**响应http body（json格式）:**

| 参数          | 类型     | 描述           |
| ----------- | ------ | ------------ |
| result_list | json数组 | 具体查询数据，内容见下表 |

result_list（json数组）中每一项的具体内容

| 参数      | 类型     | 描述           |
| ------- | ------ | ------------ |
| code    | int    | 服务器错误码，0为成功  |
| message | string | 服务器返回的信息     |
| url     | string | 当前图片的url     |
| data    |        | 具体查询数据，内容见下表 |

data字段具体内容

| 参数               | 类型     | 描述     |
| ---------------- | ------ | ------ |
| name             | string | 姓名     |
| phone            | string | 手机号    |
| uin              | string | QQ号    |
| name_confidence  | double | 姓名置信度  |
| phone_confidence | double | 手机号置信度 |

注：如未识别出某字段（如name），则该字段对应的置信度（如name_confidence）为-1

### 2.3  示例

#### 2.3.1  请求包

```
POST /ocr/namecard HTTP/1.1
Authorization: FL26MsO1nhrZGuXdin10DE5tnDdhPTEwMDAwMDEmYj1xaW5pdXRlc3QyJms9QUtJRG1PNWNQVzNMREdKc2FyREVEY1ExRnByWlZDMW9wZ3FYJnQ9MTQ2OTE3NTIzMCZlPTE0NjkxNzYyMzA=
Host: service.image.myqcloud.com
Content-Length: 302
Content-Type: "application/json"

{
"appid":11111,
"bucket":"test",
"ret_image":0,
"url_list":[
"http://www.test.com/aaa.jpg",
"http://www.test.com/bbb.jpg"
]
}
```

#### 2.3.2  响应httpbody（application/json格式）：

```
{
    "result_list": [
        {
            "code": 0,
            "message": "OK",
            "url": " http://www.test.com/aaa.jpg",
            "data": {
                "name": "某某",
                "phone": "12345678998”,
                "uin": "10000",
                "name_confidence": 0.9,
                "phone_confidence": 0.9,
                "uin_confidence": 0.9
            }
        },
        {
            "code": 0,
            "message": "OK",
            "url": " http://www.test.com/bbb.jpg",
            "data": {
                "name": "某某某",
                "phone": "12345678999”,
                "uin": "10001",
                "name_confidence": 0.99,
                "phone_confidence": 0.99,
                "uin_confidence": 0.99
            }
        }
    ]
}
```

## 3 使用图片文件
### 3.1 请求包

图片文件OCR使用HTML表单上传一个或多个文件，文件内容通过多重表单格式（multipart/form-data）编码。

**请求语法**

```
POST /ocr/namecard HTTP/1.1
Content-Type:multipart/form-data;boundary=-------------------------acebdf13572468
Authorization: Signature
Host: service.image.myqcloud.com
Content-Length: ContentLength

---------------------------acebdf13572468
Content-Disposition: form-data; name="appid";

appid
---------------------------acebdf13572468
Content-Disposition: form-data; name="bucket";

bucket
---------------------------acebdf13572468
Content-Disposition: form-data; name="ret_image";

0
---------------------------acebdf13572468
Content-Disposition: form-data; name="image[0]"; filename="image _1.jpg"
Content-Type: image/jpeg

image_content
---------------------------acebdf13572468
Content-Disposition: form-data; name="image[1]"; filename="image _2.jpg "
Content-Type: image/jpeg

image_content
---------------------------acebdf13572468--
```

**请求包http header:**

| 参数             | 是否必选 | 描述                                   |
| -------------- | ---- | ------------------------------------ |
| Host           | 是    | 访问域名，service.image.myqcloud.com      |
| Authorization  | 是    | 鉴权签名，详见[鉴权文档](/doc/product/460/6968) |
| Content-Type   | 是    | 标准的multipart/form-data               |
| Content-Length | 是    | http body总长度                         |

**表单域:**

| 参数        | 是否必选 | 类型          | 描述                                       |
| --------- | ---- | ----------- | ---------------------------------------- |
| appid     | 是    | uint        | 业务id                                     |
| bucket    | 是    | string      | 图片空间                                     |
| ret_image | 是    | int         | 0不返回图片，1返回图片                             |
| image     | 是    | image/jpeg等 | 图片文件，支持多个。参数名须为 “image[0]”、“image[1]”等image开头的字符串。响应http body中会按照该字符串的字典序排列。每张图片需指定filename，filename的值为可为空，响应http body中会返回用户设置的filename值。 |

### 3.2   使用图片文件的回包

响应http body（json格式）**

| 参数          | 类型     | 描述           |
| ----------- | ------ | ------------ |
| result_list | json数组 | 具体查询数据，内容见下表 |

result_list（json数组）中每一项的具体内容

| 参数       | 类型     | 描述                            |
| -------- | ------ | ----------------------------- |
| code     | int    | 服务器错误码，0为成功                   |
| message  | string | 服务器返回的信息                      |
| filename | string | 当前图片的filename，与请求包中filename一致 |
| data     |        | 具体查询数据，内容见下表                  |

data字段具体内容

| 参数               | 类型     | 描述                            |
| ---------------- | ------ | ----------------------------- |
| name             | string | 姓名                            |
| phone            | string | 手机号                           |
| uin              | string | QQ号                           |
| name_confidence  | double | 姓名置信度                         |
| phone_confidence | double | 手机号置信度                        |
| uin_confidence   | double | QQ号置信度                        |
| image            | string | 返回图片的base64编码（ret_image=1时返回） |

注：如未识别出某字段（如name），则该字段对应的置信度（如name_confidence）为-1

### 3.3 示例

#### 3.3.1  http请求：

```
POST /ocr/namecard HTTP/1.1
Content-Type:multipart/form-data;boundary=-------------------------acebdf13572468
Authorization: FCHXddYbhZEBfTeZ0j8mn9Og16JhPTEwMDAwMzc5Jms9QUtJRGVRZDBrRU1yM2J4ZjhRckJiUkp3Sk5zbTN3V1lEeHN1JnQ9MTQ2ODQ3NDY2MiZyPTU3MiZ1PTAmYj10ZXN0YnVja2V0JmU9MTQ3MTA2NjY2Mg==
Host: service.image.myqcloud.com
Content-Length: 61478

---------------------------acebdf13572468
Content-Disposition: form-data; name="appid";

11111
---------------------------acebdf13572468
Content-Disposition: form-data; name="bucket";

testbucket
---------------------------acebdf13572468
Content-Disposition: form-data; name="ret_image";

0
---------------------------acebdf13572468
Content-Disposition: form-data; name="image[0]"; filename="1.jpg"
Content-Type: image/jpeg

<@INCLUDE *D:\185839ggh0oedgnog04g0b.jpg.thumb.jpg*@>
---------------------------acebdf13572468
Content-Disposition: form-data; name="image[1]"; filename="2.jpg"
Content-Type: image/jpeg

<@INCLUDE *D:\200132svnmybmhbmmgbmga.jpg.thumb.jpg*@>
---------------------------acebdf13572468
```

#### 3.3.2  响应httpbody（application/json格式）：

```
{
    "result_list": [
        {
            "code": 0,
            "message": "success",
            "filename": "1.jpg",
            "data": {
                "name": "某某",
                "phone": "12345678998”,
                "uin": "10000",
                "name_confidence": 0.9,
                "phone_confidence": 0.9,
                "uin_confidence": 0.9
            }
        },
        {
            "code": 0,
            "message": "success",
            "filename": "2.jpg",
            "data": {
                "name": "某某某",
                "phone": "12345678999”,
                "uin": "10001",
                "name_confidence": 0.99,
                "phone_confidence": 0.99,
                "uin_confidence": 0.99
            }
        }
    ]
}
```

## 4 错误码
| 错误码   | 含义                                  |
| :---- | :---------------------------------- |
| 3     | 错误的请求                               |
| 4     | 签名为空                                |
| 5     | 签名串错误                               |
| 6     | appid/bucket/url不匹配                 |
| 7     | 签名编码失败（内部错误）                        |
| 8     | 签名解码失败（内部错误）                        |
| 9     | 签名过期                                |
| 10    | appid不存在                            |
| 11    | secretid不存在                         |
| 12    | appid不匹配                            |
| 13    | 重放攻击                                |
| 14    | 签名失败                                |
| 15    | 操作太频繁，触发频控                          |
| 16    | Bucket不存在                           |
| 17    | url为空                               |
| 18    | 没有图片或url                            |
| 19    | 图片数过多，单次请求最多支持20个url或文件             |
| 20    | 图片过大，单个文件最大支持1MB                    |
| 21    | 无效的参数                               |
| 200   | 内部打包失败                              |
| 201   | 内部解包失败                              |
| 202   | 内部链接失败                              |
| 203   | 内部处理超时                              |
| -1102 | 图片解码失败                              |
| -1300 | 图片为空                                |
| -1301 | 请求的参数为空                             |
| -1308 | url图片下载失败                           |
| -1400 | 非法的图片格式                             |
| -1403 | 图片下载失败                              |
| -1404 | 图片无法识别                              |
| -1505 | url格式不对                             |
| -1506 | 图片下载超时                              |
| -1507 | 无法访问url对应的图片服务器                     |
| -5062 | url对应的图片已被标注为不良图片，无法访问（专指存储于腾讯云的图片） |
| -5103 | OCR识别失败                             |
