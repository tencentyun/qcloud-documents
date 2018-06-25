## 接口概述

### 服务简介
本接口用于识别身份证上的姓名、证件号、地址等信息。

### 计费说明
本接口按实际使用量计费，具体定价请查看 [计费说明](/document/product/641/12399)。

### url 说明
支持 http 和 https 两种协议：

`http://recognition.image.myqcloud.com/ocr/idcard`

`https://recognition.image.myqcloud.com/ocr/idcard`

## 请求方式

### 请求头 header

| 参数名            |必选| 值                                        | 描述                                       |
| -------------- | -----|----------------------------------- | ---------------------------------------- |
| host           |  是   | recognition.image.myqcloud.com        | 腾讯云文字识别服务器域名                       |
| content-length |  否   | 包体总长度                          | 每个请求的包体大小限制为 6MB，不支持 .gif 类型的动图 | 
| content-type   | 是| application/json  或者  multipart/form-data | 根据不同接口选择：<br/>1. 使用图片 url，选择 application/json；<br/>2. 使用图片 image，选择 multipart/form-data。      |
| authorization  |是| 鉴权签名                              |多次有效签名，用于鉴权，生成方式见 [鉴权签名方法](/document/product/641/12409) |
>**注意：**
>如选择 multipart/form-data，请使用 http 框架/库推荐的方式设置请求的 content-type，不推荐直接调用 setheader 等方法设置，否则可能导致 boundary 缺失引起请求失败。

## 使用图片 URL
### 请求参数

使用 application/json 格式：

| 参数        | 必选 | 类型        | 说明             |
| --------- | ---- | --------- | -------------- |
| appid     | 是   | string    | 接入项目的唯一标识，可在 [账号信息](https://console.cloud.tencent.com/developer) 或 [云 API 密钥](https://console.cloud.tencent.com/cam/capi) 中查看。           |
| url_list  | 是   | string 数组 | 图片 url 列表      |


### 返回内容

| 参数          | 类型      | 类型           |
| ----------- | ------- | ------------ |
| result_list | json 数组 | 具体查询数据，内容见下表 |

result_list（ json 数组）中每一项的具体内容：

| 参数      | 类型     | 描述           |
| ------- | ------ | ------------ |
| code    | int    | 错误码，0 为成功    |
| message | string | 错误描述         |
| url     | string | 当前图片的 url    |
| data    | object | 具体查询数据，内容见下表 |

data 字段具体内容（身份证有照片的一面）：

| 参数                        | 类型            | 描述                              |
| ------------------------- | ------------- | ------------------------------- |
| name                      | string        | 姓名                              |
| sex                       | string        | 性别                              |
| nation                    | string        | 民族                              |
| birth                     | string        | 出生日期                            |
| address                   | string        | 地址                              |
| id                        | string        | 身份证号                            |
| name_confidence_all       | array(int)    | 证件姓名置信度，取值范围[0,100]             |
| sex_confidence_all        | array(int)    | 性别置信度，取值范围[0,100]               |
| nation_confidence_all     | array(int)    | 民族置信度，取值范围[0,100]               |
| birth_confidence_all      | array(int)    | 出生日期置信度，取值范围[0,100]             |
| address_confidence_all    | array(int)    | 地址置信度，取值范围[0,100]               |
| id_confidence_all         | array(int)    | 身份证号置信度,，取值范围[0,100]            |


data 字段具体内容（身份证反面）：

| 参数                        | 类型         | 描述                   |
| ------------------------- | ---------- | -------------------- |
| authority                 | string     | 发证机关                 |
| valid_date                | string     | 证件有效期                |
| authority_confidence_all  | array(int) | 发证机关置信度，取值范围[0,100]  |
| valid_date_confidence_all | array(int) | 证件有效期置信度，取值范围[0,100] |


>**注意：** 
>如未识别出某字段（如 name ），则该字段对应的置信度（如 name_confidence ）为-1。

### 请求示例
```
POST /ocr/idcardHTTP/1.1
Authorization: FL26MsO1nhrZGuXdin10DE5tnDdhPTEwMDAwMDEmYj1xaW5pdXRlc3QyJms9QUtJRG1PNWNQVzNMREdKc2FyREVEY1ExRnByWlZDMW9wZ3FYJnQ9MTQ2OTE3NTIzMCZlPTE0NjkxNzYyMzA=
Host: recognition.image.myqcloud.com
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

### 返回示例

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

## 使用图片文件

### 请求参数
使用 multipart/form-data 格式：

| 参数        | 是否必选 | 类型           | 描述                                       |
| --------- | ---- | ------------ | ---------------------------------------- |
| appid     | 是    | uint         | 项目ID                                     |
| card_type | 否    | int          | 0 为身份证有照片的一面，1 为身份证有国徽的一面；如果未指定，默认为0。     |
| image     | 是    | image/jpeg 等 | 图片文件，支持多个：<br>1. 参数名须为 “image[0]”、“image[1]”等 image 开头的字符串。响应 http body 中会按照该字符串的字典序排列。<br>2. 每张图片需指定 filename，filename 的值为可为空，响应 http body 中会返回用户设置的 filename 值。 |

### 返回内容

| 字段          | 类型      | 说明           |
| ----------- | ------- | ------------ |
| result_list | json 数组 | 具体查询数据，内容见下表 |

result_list（json 数组）中每一项的具体内容：

| 字段       | 类型     | 说明                               |
| -------- | ------ | -------------------------------- |
| code     | int    | 服务器错误码，0 为成功                     |
| message  | string | 服务器返回的信息                         |
| filename | string | 当前图片的 filename，与请求包中 filename 一致 |
| data     | object | 具体查询数据，内容见下表                     |

data 字段具体内容（身份证有照片的一面）：

| 字段                     | 类型         | 说明                  |
| ---------------------- | ---------- | ------------------- |
| name                   | string     | 姓名                  |
| sex                    | string     | 性别                  |
| nation                 | string     | 民族                  |
| birth                  | string     | 出生日期                |
| address                | string     | 地址                  |
| id                     | string     | 身份证号                |
| name_confidence_all    | array(int) | 证件姓名置信度，取值范围[0,100] |
| sex_confidence_all     | array(int) | 性别置信度，取值范围[0,100]]  |
| nation_confidence_all  | array(int) | 民族置信度，取值范围[0,100]   |
| birth_confidence_all   | array(int) | 出生日期置信度，取值范围[0,100] |
| address_confidence_all | array(int) | 地址置信度，取值范围[0,100]   |
| id_confidence_all      | array(int) | 身份证号置信度，取值范围[0,100] |

>**注意：** 
>如未识别出某字段（如 name），则该字段对应的置信度（如 name_confidence）为-1。

data 字段具体内容（身份证反面）：

| 字段                        | 类型         | 描述                   |
| ------------------------- | ---------- | -------------------- |
| authority                 | string     | 发证机关                 |
| valid_date                | string     | 证件有效期                |
| authority_confidence_all  | array(int) | 发证机关置信度，取值范围[0,100]  |
| valid_date_confidence_all | array(int) | 证件有效期置信度，取值范围[0,100] |

>**注意：** 
>如未识别出某字段（如 name ），则该字段对应的置信度（如 name_confidence ）为-1。

### 请求示例
```
POST /ocr/idcard HTTP/1.1
Content-Type:multipart/form-data;boundary=-------------------------acebdf13572468
Authorization: FCHXddYbhZEBfTeZ0j8mn9Og16JhPTEwMDAwMzc5Jms9QUtJRGVRZDBrRU1yM2J4ZjhRckJiUkp3Sk5zbTN3V1lEeHN1JnQ9MTQ2ODQ3NDY2MiZyPTU3MiZ1PTAmYj10ZXN0YnVja2V0JmU9MTQ3MTA2NjY2Mg==
Host: recognition.image.myqcloud.com
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

### 返回示例

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

## 错误码
| **错误码** | **含义**                            |
| ------- | --------------------------------- |
| 3       | 错误的请求；其中 message:account abnormal,errorno is:2 为账号欠费停服                              |
| 4       | 签名为空                              |
| 5       | 签名串错误                             |
| 6       | APPID /存储桶/ url 不匹配               |
| 7       | 签名编码失败（内部错误）                      |
| 8       | 签名解码失败（内部错误）                      |
| 9       | 签名过期                              |
| 10      | APPID 不存在                         |
| 11      | SecretId 不存在                      |
| 12      | APPID 不匹配                         |
| 13      | 重放攻击                              |
| 14      | 签名失败                              |
| 15      | 操作太频繁，触发频控                        |
| 16      | 存储桶不存在                            |
| 17      | url  为空                           |
| 18      | 没有图片或 url                         |
| 19      | 图片数过多，单次请求最多支持 20 个 url 或文件       |
| 20      | 图片过大，单个文件最大支持 1MB                 |
| 21      | 无效的参数                             |
| 200     | 内部打包失败                            |
| 201     | 内部解包失败                            |
| 202     | 内部链接失败                            |
| 203     | 内部处理超时                            |
| -1102   | 图片解码失败                            |
| -1300   | 图片为空                              |
| -1301   | 参数为空                              |
| -1304   | 参数过长                              |
| -1308   | url	图片下载失败                        |
| -5101   | OCR	照片为空                          |
| -5103   | OCR	识别失败                          |
| -5106   | 身份证边框不完整                          |
| -5107   | 输入图片不是身份证                         |
| -5108   | 身份证信息不合规范                         |
| -5109   | 照片模糊                              |
| -7001   | 未检测到身份证，请对准边框(请避免拍摄时倾角和旋转角过大、摄像头) |
| -7002   | 请使用第二代身份证件进行扫描                    |
| -7003   | 不是身份证正面照片(请使用带证件照的一面进行扫描)         |
| -7004   | 不是身份证反面照片(请使用身份证反面进行扫描)           |
| -7005   | 确保扫描证件图像清晰                        |
| -7006   | 请避开灯光直射在证件表面                      |
| -9100   | 身份证日期不合法                          |
| -9101   | 身份证边框不完整                          |

更多其他 API 错误码请看[**错误码说明**](/document/product/641/12410)  。
