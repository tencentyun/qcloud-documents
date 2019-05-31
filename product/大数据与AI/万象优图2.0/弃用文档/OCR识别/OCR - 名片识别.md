## 简介
本接口用于识别名片上的姓名、手机号、地址等信息。

## 计费说明
请查看[计费说明](/document/product/460/6970)。


## 说明
| 概念     | 解释               |
| ------ | ---------------- |
| appid  | 项目ID, 接入项目的唯一标识 |
><font color="#0000cc">**注意：** </font>
 如果开发者使用的是 V1 版本，则 appid 为其当时生成的 appid。

## 调用URL
`http://service.image.myqcloud.com/ocr/namecard`

## 请求包header
接口采用 http 协议，支持多 url 和多本地图片文件，每个请求最多支持 20 张图片或 url 。
所有请求都要求含有下表列出的头部信息：

| 参数名            | 值                                        | 描述                                       |
| -------------- | ---------------------------------------- | ---------------------------------------- |
| Host           | service.image.myqcloud.com               | 万象优图服务器域名                                |
| Content-Length | 包体总长度                                    | 整个请求包体内容的总长度，单位：字节（Byte）                 |
| Content-Type   | application/json  或者  multipart/form-data | 根据不同接口选择                                 |
| Authorization  | 鉴权签名                                     | 用于[**鉴权**](https://cloud.tencent.com/doc/product/275/3805)的签名 |

## 使用图片 URL
### 请求参数
使用 application/json 格式。

| 参数        | 是否必选 | 类型     | 说明           |
| --------- | ---- | ------ | ------------ |
| appid     | 必选    | string | 项目ID         |
| bucket    | 必选    | string | 图片空间         |
| ret_image | 必选    | int    | 0 不返回图片，1 返回图片 |
| url_list  | 必选    | string 数组 | 图片 url 列表      |

### 返回内容
| 字段          | 类型     | 说明           |
| ----------- | ------ | ------------ |
| result_list | json 数组 | 具体查询数据，内容见下表 |

result_list（json 数组）中每一项的具体内容

| 字段      | 类型     | 说明           |
| ------- | ------ | ------------ |
| code    | int    | 服务器错误码，0 为成功  |
| message | string | 服务器返回的信息     |
| url     | string | 当前图片的 url     |
| data    | object       | 具体查询数据，内容见下表 |

data字段具体内容

| 字段               | 类型     | 说明     |
| ---------------- | ------ | ------ |
| name             | string | 姓名     |
| phone            | string | 手机号    |
| uin              | string | QQ号    |
| name_confidence  | double | 姓名置信度，取值范围[0.0,100.0]  |
| phone_confidence | double | 手机号置信度，取值范围[0.0,100.0] |
| uin_confidence   | double | QQ号置信度，取值范围[0.0,100.0]                        |

><font color="#0000cc">**注意：** </font>
>如未识别出某字段（如 name ），则该字段对应的置信度（如 name_confidence ）为-1。


### 示例
#### 请求包

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

#### 回包

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



## 使用图片文件

### 请求参数

图片文件 OCR 使用 HTML 表单上传一个或多个文件，文件内容通过多重表单格式（multipart/form-data）编码。

| 参数        | 是否必选 | 类型          | 说明                                       |
| --------- | ---- | ----------- | ---------------------------------------- |
| appid     | 必选    | uint        | 项目ID                                     |
| bucket    | 必选    | string      | 图片空间                                     |
| ret_image | 必选    | int         | 0 不返回图片，1 返回图片                             |
| image     | 必选    | image/jpeg等 | 图片文件，支持多个。参数名须为 “image[0]”、“image[1]”等 image 开头的字符串。响应 http body 中会按照该字符串的字典序排列。每张图片需指定 filename，filename 的值为可为空，响应 http body 中会返回用户设置的 filename 值。 |

### 返回内容

| 字段               | 类型     | 说明                            |
| ---------------- | ------ | ----------------------------- |
| name             | string | 姓名                            |
| phone            | string | 手机号                           |
| uin              | string | QQ号                           |
| name_confidence  | double | 姓名置信度，取值范围[0.0,100.0]                          |
| phone_confidence | double | 手机号置信度，取值范围[0.0,100.0]                        |
| uin_confidence   | double | QQ号置信度，取值范围[0.0,100.0]                        |
| image            | string | 返回图片的base64编码（ret_image=1时返回） |

><font color="#0000cc">**注意：** </font>
如未识别出某字段（如 name ），则该字段对应的置信度（如 name_confidence ）为-1


### 示例
#### 请求包
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

#### 回包
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

## 错误码
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

更多其他 API 错误码请看[**错误码说明**](/document/product/460/8523) 。









