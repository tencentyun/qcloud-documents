## 接口概述

### 服务简介
护照 OCR 识别，根据用户上传的图像，返回识别出的护照信息。

### url 说明
支持 HTTP 和 HTTPS 两种协议：

`http://sdkservice.image.myqcloud.com/ocr/passport`

`https://sdkservice.image.myqcloud.com/ocr/passport`

## 请求头 header
所有请求都要求含有以下头部信息：

| 参数名称        | 必选      |值                | 描述                               |
| -------------- | ---------|------------------------------- | ------------------------------|
| host           | 是       |sdkservice.image.myqcloud.com     | 腾讯云智能图像识别服务器域名             |
| content-length | 否       |包体总长度           | 每个请求的包体大小限制为 6 MB；所有接口都为 post 方法； 不支持 .gif 这类的动图。  |
| content-type   | 是       |application/json 或 multipart/form-data | 根据不同接口选择：1. 使用 application/json 格式，参数 url 或 image，其值为图片链接或图片 base64 编码；2. 使用 multipart/form-data 格式，参数为 image，其值为图片的二进制内容。  |
| authorization  | 是       |鉴权签名     | 多次有效签名,用于鉴权，具体生成方式详见[鉴权签名方法](https://cloud.tencent.com/document/product/864/17712) |
>**注意：**如选择 multipart/form-data，请使用 http 框架/库推荐的方式设置请求的 content-type，不推荐直接调用 setheader 等方法设置，否则可能导致 boundary 缺失引起请求失败。

### 请求参数

| 参数名称   | 必选 | 类型            | 描述                                       |
| ------ | ---- | ------------- | ---------------------------------------- |
| app_id | 是   | string        | 接入项目的唯一标识，可在 [账号信息](https://console.cloud.tencent.com/developer) 或 [云 API 密钥](https://console.cloud.tencent.com/cam/capi) 中查看       |
| image  | 否   | binary  | 图片文件                     |
| url    | 否   | string        | 图片 url 或 图片 base64，两者填一个即可。同时赋值时，则以 url 指定的图像作为输入 |

### 返回内容

| 字段         | 类型          | 说明         |
| ---------- | ----------- | ---------- |
| code       | int         | 返回状态值      |
| message    | string      | 返回错误消息     |
| data.items | array(item) | 识别出的所有字段信息 |

item说明

| 字段         | 类型   | 说明   |
| ------------| ------ | ----- |
|class 	  | string | 护照类别 |
|session_id   | string | 相应请求的 session 标识符， 可用于结果查询 |
|words		  |array(word)|字段识别出来的每个字的信息|
|itemcoord    | object |字段在图像中的像素坐标，包括左上角坐标 x,y，以及宽、高 width, height|
|itemstring  | string | 字段字符串 |


## 请求示例
### 使用 url 的请求示例
```
{
"app_id":"123456",
"image":"SALDKHKAFLASD",
"session_id":"1000000111111"
}

```

## 返回示例
```
{
    "code": 0,
    "message": "OK",
    "data": {
        "class": [],
        "session_id": "10000011588781056",
        "items": [
            {
                "item": "类别",
                "itemcoord": {
                    "x": 0,
                    "y": 0,
                    "width": 0,
                    "height": 0
                },
                "itemconf": 0.9990000128746032,
                "itemstring": "P",
                "coords": [],
                "words": [],
                "candword": []
            },
            {
                "item": "签发国",
                "itemcoord": {
                    "x": 229,
                    "y": 377,
                    "width": 24,
                    "height": 11
                },
                "itemconf": 0.9990000128746032,
                "itemstring": "CHN",
                "coords": [],
                "words": [],
                "candword": []
            },
            {
                "item": "护照号码",
                "itemcoord": {
                    "x": 359,
                    "y": 381,
                    "width": 100,
                    "height": 16
                },
                "itemconf": 0.9990000128746032,
                "itemstring": "G38325238",
                "coords": [],
                "words": [],
                "candword": []
            },
            {
                "item": "性别英文",
                "itemcoord": {
                    "x": 163,
                    "y": 492,
                    "width": 31,
                    "height": 15
                },
                "itemconf": 0.9556748270988464,
                "itemstring": "F",
                "coords": [],
                "words": [],
                "candword": []
            },
            {
                "item": "国籍英文",
                "itemcoord": {
                    "x": 0,
                    "y": 0,
                    "width": 0,
                    "height": 0
                },
                "itemconf": 0.9990000128746032,
                "itemstring": "CHN",
                "coords": [],
                "words": [],
                "candword": []
            },
            {
                "item": "出生日期",
                "itemcoord": {
                    "x": 164,
                    "y": 525,
                    "width": 103,
                    "height": 14
                },
                "itemconf": 0.9990000128746032,
                "itemstring": "870704",
                "coords": [],
                "words": [],
                "candword": []
            },
            {
                "item": "出生地英文",
                "itemcoord": {
                    "x": 301,
                    "y": 492,
                    "width": 111,
                    "height": 15
                },
                "itemconf": 0.9976770281791688,
                "itemstring": "XINJIANG",
                "coords": [],
                "words": [],
                "candword": []
            },
            {
                "item": "签发日期",
                "itemcoord": {
                    "x": 165,
                    "y": 557,
                    "width": 101,
                    "height": 14
                },
                "itemconf": 0.9982568621635436,
                "itemstring": "100106",
                "coords": [],
                "words": [],
                "candword": []
            },
            {
                "item": "签发地英文",
                "itemcoord": {
                    "x": 301,
                    "y": 525,
                    "width": 112,
                    "height": 14
                },
                "itemconf": 0.9968590140342712,
                "itemstring": "XINJIANG",
                "coords": [],
                "words": [],
                "candword": []
            },
            {
                "item": "有效期至",
                "itemcoord": {
                    "x": 302,
                    "y": 557,
                    "width": 103,
                    "height": 14
                },
                "itemconf": 0.9902793765068054,
                "itemstring": "200105",
                "coords": [],
                "words": [],
                "candword": []
            },
            {
                "item": "签发机关",
                "itemcoord": {
                    "x": 303,
                    "y": 600,
                    "width": 178,
                    "height": 16
                },
                "itemconf": 0.9489678740501404,
                "itemstring": "MinistryofPublicSecuritys",
                "coords": [],
                "words": [],
                "candword": []
            },
            {
                "item": "机读码1",
                "itemcoord": {
                    "x": 27,
                    "y": 642,
                    "width": 446,
                    "height": 15
                },
                "itemconf": 0.9693686962127686,
                "itemstring": "P0CHNWANG<<Q1<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<",
                "coords": [],
                "words": [],
                "candword": []
            },
            {
                "item": "机读码2",
                "itemcoord": {
                    "x": 28,
                    "y": 667,
                    "width": 445,
                    "height": 17
                },
                "itemconf": 0.9869517683982848,
                "itemstring": "G383252382CHN8707040F200105619206501<<<<<<24",
                "coords": [],
                "words": [],
                "candword": []
            },
            {
                "item": "英文姓",
                "itemcoord": {
                    "x": 163,
                    "y": 425,
                    "width": 65,
                    "height": 13
                },
                "itemconf": 0.9990000128746032,
                "itemstring": "WANG",
                "coords": [],
                "words": [],
                "candword": []
            },
            {
                "item": "英文名",
                "itemcoord": {
                    "x": 162,
                    "y": 458,
                    "width": 47,
                    "height": 15
                },
                "itemconf": 0.9990000128746032,
                "itemstring": "QI",
                "coords": [],
                "words": [],
                "candword": []
            }
        ]
    }
}
```

## HTTP 返回码

| 错误码  | 含义                   |
| ---- | -------------------- |
| 400  | 请求不合法，包体格式错误         |
| 401  | 权限验证失败               |
| 403  | 鉴权信息不合法，禁止访问         |
| 404  | 请求失败                 |
| 411  | 请求没有指定 ContentLength |
| 413  | 请求包体太大               |
| 424  | 请求的方法没有找到            |
| 500  | 服务内部错误               |
| 502  | 网关错误，计算后台服务不可用       |
| 503  | 服务不可用                |
| 504  | 后端服务超时 或者 处理失败       |


## 错误码
| 错误码   | 含义       |
| ----- | -------- |
| -1102 | 图片解码失败   |
| -1300 | 图片为空     |
| -1301 | 参数为空     |
| -1304 | 参数过长     |
| -5208 | 服务器内部初始化错误 |
| -9020 | 护照 OCR 识别失败 |
