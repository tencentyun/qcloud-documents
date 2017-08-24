## 简介
OCR - 身份证识别可识别身份证上的姓名、证件号、地址等信息。OCR 接口采用 http 协议，支持多 url 和多本地图片文件,每个请求最多支持 20 张图片或 url 。
## 接口形式
OCR 接口采用 http 协议，支持多 url 和多本地图片文件,每个请求最多支持 20 张图片或 url 。
接口：`http://service.image.myqcloud.com/ocr/idcard`
请求方式：POST

说明：该接口的费用可查看 [计费说明](/doc/product/460/6970?!preview=true&lang=zh)，按使用量进行月结。

## 身份证 OCR - 图片 url
### 请求
请求语法:
```
POST /ocr/idcard HTTP/1.1
Authorization: Signature
Host: service.image.myqcloud.com
Content-Length: ContentLength
Content-Type: "application/json"

{
    "appid": appid,
"bucket": "bucket",
"card_type":type,
    "url_list": [
        "url",
        "url"
    ]
}
```
请求包 http header:

| 参数             | 是否必选 | 描述                                   |
| -------------- | ---- | ------------------------------------ |
| Host           | 是    | 访问域名，service.image.myqcloud.com      |
| Authorization  | 是    | 鉴权签名，详见 [签名与鉴权](/doc/product/460/6968) |
| Content-Type   | 是    | 标准 application/json                   |
| Content-Length | 是    | http body 总长度                         |

请求包 http body:

| 参数        | 是否必选 | 类型     | 描述                      |
| --------- | ---- | ------ | ----------------------- |
| appid     | 是    | string | 业务 id                    |
| bucket    | 是    | string | 图片空间                    |
| card_type | 是    | int    | 0 为身份证有照片的一面，1为身份证有国徽的一面 |
| url_list  | 是    | string | 图片 url 列表                 |

### 返回内容

响应 http body（ json 格式）:

| 参数          | 类型     | 类型           |
| ----------- | ------ | ------------ |
| result_list | json 数组 | 具体查询数据，内容见下表 |

result_list（ json 数组）中每一项的具体内容

| 参数      | 类型     | 描述           |
| ------- | ------ | ------------ |
| code    | int    | 服务器错误码，0 为成功  |
| message | string | 服务器返回的信息     |
| url     | string | 当前图片的 url     |
| data    |        | 具体查询数据，内容见下表 |

data 字段具体内容（身份证有照片的一面）

| 参数                     | 类型         | 描述      |
| ---------------------- | ---------- | ------- |
| name                   | string     | 姓名      |
| sex                    | string     | 性别      |
| nation                 | string     | 民族      |
| birth                  | string     | 出生日期    |
| address                | string     | 地址      |
| id                     | string     | 身份证号    |
| name_confidence_all    | array(int) | 证件姓名置信度 |
| sex_confidence_all     | array(int) | 性别置信度   |
| nation_confidence_all  | array(int) | 民族置信度   |
| birth_confidence_all   | array(int) | 出生日期置信度 |
| address_confidence_all | array(int) | 地址置信度   |
| id_confidence_all      | array(int) | 身份证号置信度 |

data 字段具体内容（身份证反面）

| 参数                        | 类型         | 描述       |
| ------------------------- | ---------- | -------- |
| authority                 | string     | 发证机关     |
| valid_date                | string     | 证件有效期    |
| authority_confidence_all  | array(int) | 发证机关置信度  |
| valid_date_confidence_all | array(int) | 证件有效期置信度 |

><font color="#0000cc">**注意：** </font>
置信度的值为区间在 [0,100] 的整数。

### 示例

http请求：
```
POST /ocr/idcardHTTP/1.1
Authorization: FL26MsO1nhrZGuXdin10DE5tnDdhPTEwMDAwMDEmYj1xaW5pdXRlc3QyJms9QUtJRG1PNWNQVzNMREdKc2FyREVEY1ExRnByWlZDMW9wZ3FYJnQ9MTQ2OTE3NTIzMCZlPTE0NjkxNzYyMzA=
Host: service.image.myqcloud.com
Content-Length: 302
Content-Type: "application/json"

{
"appid":11111,
"bucket":"test",
"card_type":0,
"url_list":[
"http://www.test.com/aaa.jpg",
"http://www.test.com/bbb.jpg"
]
}
```

响应 httpbody（ application/json 格式）：

```
{
    "result_list": [
        {
            "code": 0,
            "message": "OK",
            "url": " http://www.test.com/aaa.jpg",
            "data": {
                "name": "某某",
                "sex": "男",
                "nation": "汉",
                "birth": "2000/1/1",
                "address": "某地",
                "id": "123456200001011234",
                "name_confidence_all": [
                    38,28
                ],
                "sex_confidence_all": [
                    28
                ],
                "nation_confidence_all": [
                    34
                ],
                "birth_confidence_all": [
                    38, 38, 20, 46, 50, 49
                ],
                "address_confidence_all": [
                    13, 30,
                ],
                "id_confidence_all": [
49, 50, 58, 63, 51, 52, 55, 48, 48, 47, 58, 47, 48, 56,
                    45, 55, 54, 47
                ]
            }
        },
        {
            "code": 0,
            "message": "OK",
            "url": " http://www.test.com/bbb.jpg",
            "data": {
                "name": "某某某",
                "sex": "女",
                "nation": "汉",
                "birth": "2001/1/1",
                "address": "某地",
                "id": "123456200101011234",
                "name_confidence_all": [
                    38,28,55
                ],
                "sex_confidence_all": [
                    28
                ],
                "nation_confidence_all": [
                    34
                ],
                "birth_confidence_all": [
                    38, 38, 20, 46, 50, 49
                ],
                "address_confidence_all": [
                    13, 30,
                ],
                "id_confidence_all": [
49, 50, 58, 63, 51, 52, 55, 48, 48, 47, 58, 47, 48, 56,
                    45, 55, 54, 47
                ]
            }
        }
    ]
}
```

## 身份证 OCR - 图片文件

图片文件 OCR 使用 HTML 表单上传一个或多个文件，文件内容通过多重表单格式（ multipart/form-data ）编码。
### 请求
请求语法:
```
POST /ocr/idcard HTTP/1.1
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
Content-Disposition: form-data; name="card_type";

1
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
请求包 http header：

| 参数             | 是否必选 | 描述                                   |
| -------------- | ---- | ------------------------------------ |
| Host           | 是    | 访问域名， service.image.myqcloud.com      |
| Authorization  | 是    | 鉴权签名，详见 [签名与鉴权 ](/doc/product/460/6968) |
| Content-Type   | 是    | 标准的 multipart/form-data               |
| Content-Length | 是    | http body 总长度                         |

表单域：

| 参数        | 是否必选 | 类型          | 描述                                       |
| --------- | ---- | ----------- | ---------------------------------------- |
| appid     | 是    | uint        | 业务id                                     |
| bucket    | 是    | string      | 图片空间                                     |
| card_type | 是    | int         | 0 为身份证有照片的一面，1 为身份证有国徽的一面                  |
| image     | 是    |  image/jpeg 等 | 图片文件，支持多个。参数名须为 “image[0]”、“image[1]”等 image 开头的字符串。响应 http body 中会按照该字符串的字典序排列。每张图片需指定 filename，filename 的值为可为空，响应 http body 中会返回用户设置的 filename 值。 |

### 返回内容

**响应 http body（ json 格式）**

| 参数          | 类型     | 描述           |
| ----------- | ------ | ------------ |
| result_list | json 数组 | 具体查询数据，内容见下表 |

result_list（json 数组）中每一项的具体内容

| 参数       | 类型     | 描述                            |
| -------- | ------ | ----------------------------- |
| code     | int    | 服务器错误码，0 为成功                   |
| message  | string | 服务器返回的信息                      |
| filename | string | 当前图片的 filename，与请求包中 filename 一致 |
| data     |        | 具体查询数据，内容见下表                  |

data 字段具体内容（身份证有照片的一面）：

| 参数                     | 类型         | 描述      |
| ---------------------- | ---------- | ------- |
| name                   | string     | 姓名      |
| sex                    | string     | 性别      |
| nation                 | string     | 民族      |
| birth                  | string     | 出生日期    |
| address                | string     | 地址      |
| id                     | string     | 身份证号    |
| name_confidence_all    | array(int) | 证件姓名置信度 |
| sex_confidence_all     | array(int) | 性别置信度   |
| nation_confidence_all  | array(int) | 民族置信度   |
| birth_confidence_all   | array(int) | 出生日期置信度 |
| address_confidence_all | array(int) | 地址置信度   |
| id_confidence_all      | array(int) | 身份证号置信度 |

data 字段具体内容（身份证反面）：

| 参数                        | 类型         | 描述       |
| ------------------------- | ---------- | -------- |
| authority                 | string     | 发证机关     |
| valid_date                | string     | 证件有效期    |
| authority_confidence_all  | array(int) | 发证机关置信度  |
| valid_date_confidence_all | array(int) | 证件有效期置信度 |

><font color="#0000cc">**注意：** </font>
置信度的值为区间在 [0,100] 的整数。

### 示例

http 请求：
```
POST /ocr/idcard HTTP/1.1
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
Content-Disposition: form-data; name="card_type";

1
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

响应 httpbody（application/json 格式）：

```
{
    "result_list": [
        {
            "code": 0,
            "message": "success",
            "filename": "1.jpg",
            "data": {
                "authority": "某市派出所",
                "valid_date": "2012.01.01-2022.01.01",
                "authority_confidence_all": [
                    42, 36, 40, 49, 41
                ],
                "valid_date_confidence_all": [
                    44, 50, 63, 44, 47, 42, 43, 53, 48, 52, 44, 47, 48, 45, 50, 58
                ]
}
        },
        {
            "code": 0,
            "message": "success",
            "filename": "2.jpg",
            "data": {
                "authority": "某市派出所",
                "valid_date": "2012.01.01-2022.01.01",
                "authority_confidence_all": [
                    42, 36, 40, 49, 41
                ],
                "valid_date_confidence_all": [
                    44, 50, 63, 44, 47, 42, 43, 53, 48, 52, 44, 47, 48, 45, 50, 58
                ]
             }
        }
    ]
}
```

## 错误码说明
| **错误码** | **含义**                              |
| ------- | ----------------------------------- |
| 3       | 错误的请求                               |
| 4       | 签名为空                                |
| 5       | 签名串错误                               |
| 6       |  APPID /存储桶/ url 不匹配                 |
| 7       | 签名编码失败（内部错误）                        |
| 8       | 签名解码失败（内部错误）                        |
| 9       | 签名过期                                |
| 10      |  APPID 不存在                            |
| 11      | SecretId 不存在                         |
| 12      |  APPID 不匹配                            |
| 13      | 重放攻击                                |
| 14      | 签名失败                                |
| 15      | 操作太频繁，触发频控                          |
| 16      | 存储桶不存在                           |
| 17      |  url  为空                               |
| 18      | 没有图片或 url                            |
| 19      | 图片数过多，单次请求最多支持 20 个 url 或文件             |
| 20      | 图片过大，单个文件最大支持 1MB                    |
| 21      | 无效的参数                               |
| 200     | 内部打包失败                              |
| 201     | 内部解包失败                              |
| 202     | 内部链接失败                              |
| 203     | 内部处理超时                              |
| -1102   | 图片解码失败                              |
| -1300   | 图片为空                                |
| -1301   | 请求的参数为空                             |
| -1308   | url 图片下载失败                           |
| -1400   | 非法的图片格式                             |
| -1403   | 图片下载失败                              |
| -1404   | 图片无法识别                              |
| -1505   |  url 格式不对                             |
| -1506   | 图片下载超时                              |
| -1507   | 无法访问 url 对应的图片服务器                     |
| -5062   |  url 对应的图片已被标注为不良图片，无法访问（专指存储于腾讯云的图片） |
| -5103   |  OCR 识别失败                             |
| -5107   | 提供的图片不是身份证                          |
