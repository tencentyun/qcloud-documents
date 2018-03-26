## 接口概述

### 服务简介
本接口用于根据用户上传的营业执照图像，返回识别出的注册号、公司名称、地址字段信息。

### 计费说明
本接口按实际使用量计费，具体定价请查看 [计费说明](/document/product/641/12399)。

### url 说明
支持 http 和 https 两种协议：

`http://recognition.image.myqcloud.com/ocr/bizlicense`

`https://recognition.image.myqcloud.com/ocr/bizlicense`

## 请求方式

### 请求头 header
所有请求都要求含有以下头部信息：

| 参数名            | 值                                        | 描述                                       |
| -------------- | ---------------------------------------- | ---------------------------------------- |
| host           | service.image.myqcloud.com               | 腾讯云文字识别服务器域名                       |
| content-length | 包体总长度                                    | 整个请求包体内容的总长度，单位：字节（Byte）                 |
| content-type   | application/json  或者  multipart/form-data | 根据不同接口选择：<br/>1. 使用图片 url，选择 application/json；<br/>2. 使用图片 image，选择 multipart/form-data。                     |
| authorization  | 鉴权签名                                     | 多次有效签名,用于鉴权， 具体生成方式详见 [鉴权签名方法](/document/product/641/12409) |

>**注意：**
如选择 multipart/form-data，请使用 http 框架/库推荐的方式设置请求的 content-type，不推荐直接调用 setheader 等方法设置，否则可能导致 boundary 缺失引起请求失败。

### 请求参数

| 参数名   | 必选 | 类型           | 参数说明                                     |
| ----- | ---- | ------------ | ---------------------------------------- |
| appid | 是   | string       | 接入项目的唯一标识，可在 [账号信息](https://console.cloud.tencent.com/developer) 或 [云 API 密钥](https://console.cloud.tencent.com/cam/capi) 中查看                    |
| image | 否   | image/jpeg 等 | 图片文件。图片需指定 filename，filename 的值为可为空，响应 http body 中会返回用户设置的 filename 值。 |
| url   | 否   | string       | image 和 url 只提供一个即可；如果都提供，只使用 url |


## 返回内容

| 参数    | 类型      | 描述           |
| ----- | ------- | ------------ |
| items | json 数组 | 具体查询数据，内容见下表 |

items（ json 数组）：

| 参数         | 类型     | 描述                                       |
| ---------- | ------ | ---------------------------------------- |
| item       | string | 字段名称（取值为注册号、公司名称、地址）                     |
| itemstring | string | 字段结果                                     |
| itemcoord  | object | 字段在图像中的像素坐标，包括左上角坐标 x, y，以及宽、高 width, height |
| itemconf   | float  | 识别结果对应的置信度                               |

返回字段为一个 json 数组，其中每一项的内容如下：

| 参数      | 类型     | 描述   |
| ------- | ------ | ---- |
| code    | int    | 错误码  |
| message | string | 错误描述 |
| data    | object | 返回数据 |

## 请求示例

### 使用 url 的请求示例

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

### 使用 image 的请求示例

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


### 返回示例
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


### 错误码

| 错误码   | 含义                       |
| ----- | ------------------------ |
| 3     | 错误的请求                    |
| 4     | 签名为空                     |
| 5     | 签名串错误                    |
| 6     | 签名中的appid/bucket与操作目标不匹配 |
| 9     | 签名过期                     |
| 10    | appid不存在                 |
| 11    | secretid不存在              |
| 12    | appid和secretid不匹配        |
| 13    | 重放攻击                     |
| 14    | 签名校验失败                   |
| 15    | 操作太频繁，触发频控               |
| 16    | Bucket不存在                |
| 21    | 无效参数                     |
| 23    | 请求包体过大                   |
| 24    | 没有权限                     |
| 25    | 您购买的资源已用完                |
| 107   | 鉴权服务内部错误                 |
| 108   | 鉴权服务不可用                  |
| 213   | 内部错误                     |
| -1102 | 图片解码失败                   |
| -1300 | 图片为空                     |
| -1301 | 参数为空                     |
| -1304 | 参数过长                     |
| -1308 | 图片下载失败                   |
| -5208 | 服务器内部错误                  |
| -9001 | 请求 type 错误，不是 0，1        |
| -9002 | 识别失败                     |
| -9005 | 图片无效                     |
| -9006 | 预处理失败                    |
| -9501 | 营业执照OCR预处理失败             |
| -9502 | 营业执照OCR识别失败              |


更多其他 API 错误码请看[**错误码说明**](/document/product/641/12410) 。

 