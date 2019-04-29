## 1. 体验与说明

### 1.1 开发准备
开发者使用OCR功能之前，需要先注册腾讯云账号，并创建图片空间，添加密钥，具体操作步骤如下：
1)	前往腾讯云•万象优图控制台注册账号；如果已经注册账号，请跳过此步骤；

![](https://mc.qcloudimg.com/static/img/82462b3d201bee1dd02265a3d477e219/1.png)

2)	在腾讯云•万象优图控制台创建一个图片空间，获取空间名称（bucket）和项目ID；如果已创建过图片空间，请跳过此步骤；

![](https://mc.qcloudimg.com/static/img/69e14001e3f8a6cbcdffd3421021ebf1/2.png)
3)	在腾讯云•万象优图控制台项目设置中添加密钥，获取SecretID和SecretKey；如果已经添加过密钥，请跳过此步骤。

![](https://mc.qcloudimg.com/static/img/e404ca7488e2803674c9fd806621e26d/3.png)

**基本概念：**

| 概念     | 解释               |
| ------ | ---------------- |
| appid  | 项目ID, 用于唯一标识接入项目 |
| bucket | 开发者添加的空间名称       |



## 2. OCR_CGI 

### 2.1 身份证OCR接口
OCR接口采用http协议，支持多URL和多本地图片文件,每个请求最多支持20张图片或url。
接口：`http://service.image.myqcloud.com/ocr/idcard`
方法：POST

#### 2.1.1 身份证OCR-图片URL
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
请求包http header:

| 参数             | 是否必选 | 描述                              |
| -------------- | ---- | ------------------------------- |
| Host           | 是    | 访问域名，service.image.myqcloud.com |
| Authorization  | 是    | 鉴权签名，详见下面鉴权章节                   |
| Content-Type   | 是    | 标准application/json              |
| Content-Length | 是    | http body总长度                    |

请求包http body:

| 参数        | 是否必选 | 类型     | 描述                      |
| --------- | ---- | ------ | ----------------------- |
| appid     | 是    | uint   | 业务id                    |
| bucket    | 是    | string | 图片空间                    |
| card_type | 是    | int    | 0为身份证有照片的一面，1为身份证有国徽的一面 |
| url_list  | 是    | string | 图片url列表                 |



响应http body（json格式）:

| 参数          | 类型     | 类型           |
| ----------- | ------ | ------------ |
| result_list | json数组 | 具体查询数据，内容见下表 |

result_list（json数组）中每一项的具体内容

| 参数      | 类型     | 描述           |
| ------- | ------ | ------------ |
| code    | int    | 服务器错误码，0为成功  |
| message | string | 服务器返回的信息     |
| url     | string | 当前图片的url     |
| data    |        | 具体查询数据，内容见下表 |

data字段具体内容（身份证有照片的一面）

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

data字段具体内容（身份证反面）

| 参数                        | 类型         | 描述       |
| ------------------------- | ---------- | -------- |
| authority                 | string     | 发证机关     |
| valid_date                | string     | 证件有效期    |
| authority_confidence_all  | array(int) | 发证机关置信度  |
| valid_date_confidence_all | array(int) | 证件有效期置信度 |

注：置信度的值为区间在[0,100]的整数

#### 2.1.2 身份证OCR-图片URL示例
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
响应httpbody（application/json格式）：
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

#### 2.1.3 身份证OCR-图片文件 
图片文件OCR使用HTML表单上传一个或多个文件，文件内容通过多重表单格式（multipart/form-data）编码。
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
**请求包http header:**

| 参数             | 是否必选 | 描述                              |
| -------------- | ---- | ------------------------------- |
| Host           | 是    | 访问域名，service.image.myqcloud.com |
| Authorization  | 是    | 鉴权签名，详见下面鉴权章节                   |
| Content-Type   | 是    | 标准的multipart/form-data          |
| Content-Length | 是    | http body总长度                    |

**表单域:**

| 参数        | 是否必选 | 类型          | 描述                                       |
| --------- | ---- | ----------- | ---------------------------------------- |
| appid     | 是    | uint        | 业务id                                     |
| bucket    | 是    | string      | 图片空间                                     |
| card_type | 是    | int         | 0为身份证有照片的一面，1为身份证有国徽的一面                  |
| image     | 是    | image/jpeg等 | 图片文件，支持多个。参数名须为 “image[0]”、“image[1]”等image开头的字符串。响应http body中会按照该字符串的字典序排列。每张图片需指定filename，filename的值为可为空，响应http body中会返回用户设置的filename值。 |

**响应http body（json格式）**

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

data字段具体内容（身份证有照片的一面）

| 参数                     | 类型         | 描述      |
| ---------------------- | ---------- | ------- |
| name                   | string     | 姓名      |
| sex                    | string     | 性别      |
| nation                 | string     | 民族      |
| birthday               | string     | 出生日期    |
| address                | string     | 地址      |
| id                     | string     | 身份证号    |
| name_confidence_all    | array(int) | 证件姓名置信度 |
| sex_confidence_all     | array(int) | 性别置信度   |
| nation_confidence_all  | array(int) | 民族置信度   |
| birth_confidence_all   | array(int) | 出生日期置信度 |
| address_confidence_all | array(int) | 地址置信度   |
| id_confidence_all      | array(int) | 身份证号置信度 |

data字段具体内容（身份证反面）

| 参数                        | 类型         | 描述       |
| ------------------------- | ---------- | -------- |
| authority                 | string     | 发证机关     |
| valid_date                | string     | 证件有效期    |
| authority_confidence_all  | array(int) | 发证机关置信度  |
| valid_date_confidence_all | array(int) | 证件有效期置信度 |

注：置信度的值为区间在[0,100]的整数

#### 2.1.4 身份证OCR-图片文件示例 
http请求：
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
响应httpbody（application/json格式）：
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
### 2.2 名片OCR接口
OCR接口采用http协议，支持多URL和多本地图片文件,每个请求最多支持20张图片或url。
接口：`http://service.image.myqcloud.com/ocr/namecard`
方法：POST

#### 2.2.1 名片OCR-图片URL
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

| 参数             | 是否必选 | 描述                              |
| -------------- | ---- | ------------------------------- |
| Host           | 是    | 访问域名，service.image.myqcloud.com |
| Authorization  | 是    | 鉴权签名，详见下面鉴权章节                   |
| Content-Type   | 是    | 标准application/json              |
| Content-Length | 是    | http body总长度                    |

**请求包http body:**

| 参数        | 是否必选 | 类型     | 描述           |
| --------- | ---- | ------ | ------------ |
| appid     | 是    | uint   | 业务id         |
| bucket    | 是    | string | 图片空间         |
| ret_image | 是    | int    | 0不返回图片，1返回图片 |
| url_list  | 是    | string | 图片url列表      |

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


#### 2.2.2 名片OCR-图片URL示例
http请求：
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
响应httpbody（application/json格式）：
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
#### 2.2.3 名片OCR-图片文件
图片文件OCR使用HTML表单上传一个或多个文件，文件内容通过多重表单格式（multipart/form-data）编码。
##### 请求语法
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

| 参数             | 是否必选 | 描述                              |
| -------------- | ---- | ------------------------------- |
| Host           | 是    | 访问域名，service.image.myqcloud.com |
| Authorization  | 是    | 鉴权签名，详见下面鉴权章节                   |
| Content-Type   | 是    | 标准的multipart/form-data          |
| Content-Length | 是    | http body总长度                    |

**表单域:**

| 参数        | 是否必选 | 类型          | 描述                                       |
| --------- | ---- | ----------- | ---------------------------------------- |
| appid     | 是    | uint        | 业务id                                     |
| bucket    | 是    | string      | 图片空间                                     |
| ret_image | 是    | int         | 0不返回图片，1返回图片                             |
| image     | 是    | image/jpeg等 | 图片文件，支持多个。参数名须为 “image[0]”、“image[1]”等image开头的字符串。响应http body中会按照该字符串的字典序排列。每张图片需指定filename，filename的值为可为空，响应http body中会返回用户设置的filename值。 |

**响应http body（json格式）**

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

| 	参数	| 类型	| 描述
| ---- | ---- | ---- |
| name| 	string	| 姓名| 
| phone| 	string| 	手机号| 
| uin	| string	| QQ号| 
| name_confidence	| double	| 姓名置信度| 
| phone_confidence| 	double	| 手机号置信度| 
| uin_confidence	| double| 	QQ号置信度| 
| image	| string	| 返回图片的base64编码（ret_image=1时返回）| 

注：如未识别出某字段（如name），则该字段对应的置信度（如name_confidence）为-1

#### 2.2.4 名片OCR-图片文件示例

http请求：
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
响应httpbody（application/json格式）：
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

### 2.3 鉴权
腾讯云•万象优图通过签名来验证请求的合法性。
#### 2.3.1 签名算法
1 获取签名所需信息
生成签名所需信息包括项目ID（appid），空间名称（bucket,图片资源的组织管理单元），项目的Secret ID和Secret Key。获取这些信息的方法如下：
a)	登录 万象优图-图片空间, 进入图片空间；
b)	如开发者未创建图片空间，可添加图片空间，获取项目ID（appid），空间名称（bucket）；如果开发者已经创建过空间，则可以直接获取项目ID和空间名称（bucket）；
c)	登录万象优图-项目设置，进入项目设置；
d)	如果开发者未添加密钥，则需添加密钥，获取项目的Secret ID和Secret Key，每个项目最多添加两对密钥；如果已经添加过密钥则直接获取项目的Secret ID和Secret Key。
注：
(1) 添加图片空间可参考添加图片空间；
(2) 添加密钥可参考添加密钥。

2 拼接签名串orignal
`a=[appid]&b=[bucket]&k=[SecretID]&t=[currenTime]&e=[expiredTime]`
注意：如果开发者使用的是V1版本，a字段为appid，b字段的值置空

| 字段名称 | 解释                                   |
| :--- | :----------------------------------- |
| a    | 开发者的项目ID，接入万象优图创建空间时系统生成的唯一标示项目的项目ID |
| b    | 图片空间名称                               |
| k    | 项目的Secret ID                         |
| t    | 当前时间，UNIX时间戳                         |
| e    | 签名过期时间，UNIX时间戳                       |

3 生成签名
a)	万象优图使用 HMAC-SHA1 算法对请求进行签名；
b)	签名串需要使用 Base64 编码。
即生成签名的公式如下：
SignTmp = HMAC-SHA1(SecretKey, orignal)
Sign = Base64(SignTmp.orignal)

其中SecretKey为项目的密钥SecretKey，orignal为1节中拼接好的签名串，首先对orignal使用HMAC-SHA1算法进行签名，然后将orignal附加到签名结果的末尾，再进行Base64编码，得到最终的sign。
注：此处使用的是标准的Base64编码，不是urlsafe的Base64编码，请注意。

#### 2.3.2 签名示例
本节介绍生成签名的算法实例，实例中使用PHP语言，如果开发者使用其他与开发，请使用对应的算法。
1. 获取签名所需信息
   获取得到的签名所需信息如下。
   项目ID：1000027
   空间名称（bucket）：test333
   Secret ID： `AKIDnX91172Bs2NK4SP9Ad9JDVYpm7Lx2Nek`
   Secret Key： `oHL5srXW3Fkn8xtugG0BDhUfOOsC9DAd`
2. 拼接签名串orignal
```
a=1000027&b=test333&k=AKIDnX91172Bs2NK4SP9Ad9JDVYpm7Lx2Nek&t=1443434355&e=1443434365

$appid = "1000027";
$bucket = "test333";
$secret_id = "AKIDnX91172Bs2NK4SP9Ad9JDVYpm7Lx2Nek";
$secret_key = "oHL5srXW3Fkn8xtugG0BDhUfOOsC9DAd";
$expired = time() + 10;
$current = time();

$srcStr = 'a='.$appid.'&b='.$bucket.'&k='.$secret_id.'&t='.$current.'&e='.$expired;
```
1. 生成签名

```
$signStr = base64_encode(hash_hmac('SHA1', $srcStr, $secret_key, true).$srcStr);
echo$signStr."\n";
```

最终得到的签名为：

```
xBx0lpW/tdIr1vfksAt3GpfXo9phPTEwMDAwMjcmYj10ZXN0MzMzJms9QUtJRG5YOTExNzJCczJOSzRTUDlBZDlKRFZZcG03THgyTmVrJnQ9MTQ2NjM5MzQ4OSZlPTE0NjYzOTM0OTk=
```

### 2.4 错误码

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
| -1300 | 图片为空                                |
| -1308 | url图片下载失败                           |
| -1400 | 非法的图片格式                             |
| -1403 | 图片下载失败                              |
| -1404 | 图片无法识别                              |
| -1505 | url格式不对                             |
| -1506 | 图片下载超时                              |
| -1507 | 无法访问url对应的图片服务器                     |
| -5062 | url对应的图片已被标注为不良图片，无法访问（专指存储于腾讯云的图片） |
| -5103 | OCR识别失败                             |


































