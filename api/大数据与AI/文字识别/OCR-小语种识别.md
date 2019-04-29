## 接口概述

### 服务简介
本接口用于根据用户上传的护照图像，返回识别出的护照信息。

### url 说明
支持 HTTP 和 HTTPS 两种协议：

`http://sdkservice.image.myqcloud.com/ocr/minorlanguage`

`https://sdkservice.image.myqcloud.com/ocr/minorlanguage`

## 请求头 header
所有请求都要求含有以下头部信息：

| 参数名            | 必选| 值              | 描述                            |
| -------------- | -------|---------------- | ---------------------------------------- |
| host           | 是     | sdkservice.image.myqcloud.com        | 腾讯云智能图像文字识别服务器域名       |
| content-length | 否      |包体总长度             | 每个请求的包体大小限制为 6 MB；所有接口都为 post 方法； 不支持 .gif 这类的动图。               |
| content-type   | 是      |application/json 或 multipart/form-data | 根据不同接口选择，每个请求最多支持 20 张 url 或图片：<br/>1. 1. 使用 application/json 格式，参数为 url 或 image，其值为图片链接或图片 base64 编码；2. 使用 multipart/form-data 格式，参数为 image，其值为图片的二进制内容。             |
| authorization  | 是      |鉴权签名             | 多次有效签名，用于鉴权，详见[鉴权签名方法](/document/product/641/12409) |
>**注意：**如选择 multipart/form-data，请使用 http 框架/库推荐的方式设置请求的 content-type，不推荐直接调用 setheader 等方法设置，否则可能导致 boundary 缺失引起请求失败。


### 请求参数

| 参数名称   | 必选 | 类型            | 描述                                       |
| ------ | ---- | ------------- | ---------------------------------------- |
| app_id | 是   | string        | 腾讯云申请的 appid                        |
| image  | 否   | binary       | 图片文件                   |
| url    | 否   | string        | 图片 url 或 图片 base64，两者填一个即可。同时赋值时，则以 url 指定的图像作为输入 |
| options  | 否  | object        | 表示可支持的小语种，目前包括：zh(中英文混合)、por(葡萄牙语)、fre(法语)、ger（德语）、spa（西班牙语）、jap（日语）、kor（韩语）、lat（拉丁语系） |

### 返回内容

| 字段         | 类型          | 说明         |
| ---------- | ----------- | ---------- |
| code       | int         | 返回状态值      |
| message    | string      | 返回错误消息     |
| data.items | array(item) | 识别出的所有字段信息 |
item说明

| 字段         | 类型   | 说明   |
| ------------| ------ | ----- |
|class 	  | string | 小语种类别 |
|session_id   | string | 相应请求的 session 标识符， 可用于结果查询 |
|words		  |array(word)|字段识别出来的每个字的信息|
|itemcoord    | object |字段在图像中的像素坐标，包括左上角坐标 x,y，以及宽、高 width, height|
|itemstring  | string | 字段字符串 |


## 请求示例
```
{
"app_id":"1000001",
"image":"SALDKHKAFLASD",
"options": {
  	"language":"jap"
  }
}
```

## 返回示例
```
{
    "code": 0,
    "message": "OK",
    "data": {
        "class": [],
        "angle": -1.65625,
        "items": [
            {
                "itemcoord": {
                    "x": 103,
                    "y": 19,
                    "width": 135,
                    "height": 29
                },
                "words": [
                    {
                        "character": "か",
                        "confidence": 0.9999997615814208
                    },
                    {
                        "character": "っ",
                        "confidence": 0.9999659061431884
                    },
                    {
                        "character": "こ",
                        "confidence": 0.9999947547912598
                    },
                    {
                        "character": "い",
                        "confidence": 0.9999805688858032
                    },
                    {
                        "character": "い",
                        "confidence": 0.9990127086639404
                    }
                ],
                "itemstring": "かっこいい"
            },
            {
                "itemcoord": {
                    "x": 102,
                    "y": 51,
                    "width": 136,
                    "height": 27
                },
                "words": [
                    {
                        "character": "社",
                        "confidence": 0.9999765157699584
                    },
                    {
                        "character": "名",
                        "confidence": 0.9999951124191284
                    },
                    {
                        "character": "の",
                        "confidence": 0.9999998807907105
                    },
                    {
                        "character": "由",
                        "confidence": 0.9999953508377076
                    },
                    {
                        "character": "来",
                        "confidence": 0.9999982118606569
                    }
                ],
                "itemstring": "社名の由来"
            }
        ],
        "session_id": "1000001162717723"
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
| -9003 | OCR 识别失败 |
