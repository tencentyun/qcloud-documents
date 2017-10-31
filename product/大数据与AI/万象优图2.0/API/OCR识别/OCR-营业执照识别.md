## 1. 接口描述

营业执照OCR识别，根据用户上传的营业执照图像，返回识别出的注册号、公司名称、地址字段信息

接口：http://recognition.image.myqcloud.com/ocr/bizlicense

方法：POST

## 2. 营业执照OCR

### 2.1  HTTP请求格式

#### 头部信息

| 参数名称           | 必选   | 类型     | 描述                                       |
| -------------- | ---- | ------ | ---------------------------------------- |
| Host           | 是    | String | recognition.image.myqcloud.com           |
| Content-Length | 是    | Int    | 整个请求包体内容的总长度，单位：字节（Byte）。                |
| Content-Type   | 是    | String | text/json                                |
| Authorization  | 是    | String | 多次有效签名,用于鉴权， 具体生成方式详见[鉴权签名方法](https://www.qcloud.com/document/product/460/6968) |

#### 请求包体

| 必须   | appid | String       | 腾讯云appid                                 |
| ---- | ----- | ------------ | ---------------------------------------- |
| 可选   | url   | String       | 图片url地址，url与image两者填一个即可，同时赋值时，则以url指定的图像作为输入 |
| 可选   | image | image/jpeg 等 | 图片文件。图片需指定  filename，filename 的值为可为空，响应 http body 中会返回用户设置的 filename 值。 |

#### 示例—使用图片 url

```
POST /ocr/bizlicense HTTP/1.1

Authorization:FL26MsO1nhrZGuXdin10DE5tnDdhPTEwMDAwMDEmYj1xaW5pdXRlc3QyJms9QUtJRG1PNWNQVzNMREdKc2FyREVEY1ExRnByWlZDMW9wZ3FYJnQ9MTQ2OTE3NTIzMCZlPTE0NjkxNzYyMzA=

Host: recognition.image.myqcloud.com

Content-Length: 302

Content-Type: "application/json"

{

"appid":"appid",

"url":"http://www.test.com/aaa.jpg"

} 
```

#### 示例—使用图片文件

```
POST /ocr/bizlicenseHTTP/1.1

Content-Type:multipart/form-data;boundary=-------------------------acebdf13572468

Authorization:Signature

Host: recognition.image.myqcloud.com

Content-Length:ContentLength

 

---------------------------acebdf13572468

Content-Disposition:form-data; name="appid";

 

appid

---------------------------acebdf13572468

Content-Disposition:form-data; name="image"; filename="image _2.jpg "

Content-Type:image/jpeg

 

image_content

---------------------------acebdf13572468
```

### 2.2 返回值

#### 返回内容

响应http body（ json 格式）： 

| 参数    | 类型     | 描述           |
| ----- | ------ | ------------ |
| items | json数组 | 具体查询数据，内容见下表 |

items（json数组）中每一项的具体内容：

| 参数         | 类型     | 描述                                       |
| ---------- | ------ | ---------------------------------------- |
| item       | String | 字段名称（取值为注册号、公司名称、地址）                     |
| itemstring | String | 字段结果                                     |
| itemcoord  | Object | 字段在图像中的像素坐标，包括左上角坐标x,y，以及宽、高width, height |
| itemconf   | Float  | 识别结果对应的置信度                               |

结果具体内容：

返回字段为一个json数组，其中每一项的内容如下：

| 参数      | 类型     | 描述   |
| ------- | ------ | ---- |
| code    | int    | 返回码  |
| message | string | 返回信息 |
| data    | Object | 返回数据 |

#### 示例

```
{

   "code": 0,

   "message": "OK",

   "data": {

       "session_id": "12531712471066566515",

       "items": [

           {

                "item": "注册号",

                "itemcoord": {

                    "x": 703,

                    "y": 689,

                    "width": 272,

                    "height": 34

                },

                "itemconf":0.9979159235954284,

                "itemstring":"310114002784042",

                "coords": [],

                "words": [],

                "candword": []

           },

           {

                "item": "公司名称",

                "itemcoord": {

                    "x": 446,

                    "y": 805,

                    "width": 380,

                    "height": 37

                },

                "itemconf":0.9843763709068298,

                "itemstring": "上海横策营销策划有限公司",

                "coords": [],

                "words": [],

                "candword": []

           },

           {

                "item": "地址",

                "itemcoord": {

                    "x": 445,

                    "y": 902,

                    "width": 567,

                    "height": 38

               },

                "itemconf":0.9998522996902466,

                "itemstring": "上海市徐汇区虹梅路1905号西部203室",

                "coords": [],

                "words": [],

                "candword": []

           }

       ]

    }

}
```

## 3. HTTP返回码

|错误码 | 内容 | 含义|
|----------|--------|
|400 |HTTP_BAD_REQUEST    |    请求不合法，包体格式错误|
|401 | HTTP_UNAUTHORIZED  | 权限验证失败|
|403 |HTTP_FORBIDDEN |    鉴权信息不合法，禁止访问|
|404 | HTTP_NOTFOUND| 请求失败|
|411 |HTTP_REQ_NOLENGTH  | 请求没有指定ContentLength|
|413  |HTTP_REQUEST_LARGE |  请求包体太大|
|424 |HTTP_METHOD_NOTFOUND| 请求的方法没有找到|
|500 |HTTP_INTERNAL_SERVER_ERROR| 服务内部错误|
|502|HTTP_BAD_GATEWAT |   网关错误，计算后台服务不可用|
|503|HTTP_SERVICE_UNAVAILABLE| 服务不可用|
|504 | HTTP_GATEWAY_TIME_OUT   |   后端服务超时或者 处理失败|

###协议错误码

|错误码 | 内容 | 含义|
|----------|--------|
|-1102| SDK_IMAGE_DECODE_FAILED |图片解码失败|
|-1300| ERROR_IMAGE_EMPTY | 图片为空|
|-1301|ERROR_PARAMETER_EMPTY | 参数为空|
|-1304 | ERROR_PARAMETER_TOO_LONG|参数过长|
|-5208 |OCR_SERVER_INTERN_ERROR|服务器内部错误|
|-9501 | BIZLICENSE_OCR_PREPROCESS_FAILED|营业执照OCR预处理失败|
|-9502 |BIZLICENSE_OCR_RECOG_FAILED| 营业执照OCR识别失败|

 