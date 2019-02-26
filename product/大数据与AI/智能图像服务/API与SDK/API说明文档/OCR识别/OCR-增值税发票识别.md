## 接口概述

### 服务简介

增值税发票 OCR 识别，用于根据用户上传的图像，返回识别出的发票信息。

### url 说明
支持 http 和 https 两种协议：

`http://recognition.image.myqcloud.com/ocr/invoice`

`https://recognition.image.myqcloud.com/ocr/invoice`

## 请求方式
### 请求头 header

| 参数名            |必选| 值                                        | 描述                                       |
| -------------- | -----|----------------------------------- | ---------------------------------------- |
| host           |  是   | recognition.image.myqcloud.com        | 腾讯云文字识别服务器域名                       |
| content-length |  否   | 包体总长度                          | 每个请求的包体大小限制为 6MB，不支持 .gif 类型的动图 |
| content-type   | 是   |application/json 或 multipart/form-data | 据不同接口选择：<br/>1. 使用 application/json 格式，参数为    url，其值为图片的 url ；<br/>2. 使用 multipart/form-data 格式，参数为 image，其值为图片的 base64 。 |
| authorization  | 是   |鉴权签名                                   | 多次有效签名,用于鉴权，具体生成方式详见 [鉴权签名方法](https://cloud.tencent.com/document/product/641/12409) |

>**注意：**
> 选择 multipart/form-data，请使用 http 框架/库推荐的方式设置请求的 content-type，不推荐直接调用 setHeader 等方法设置，否则可能导致 boundary 缺失引起请求失败。

### 请求参数

| 参数名称  | 必选   | 类型            | 描述                                       |
| ----- | ---- | ------------- | ---------------------------------------- |
| appid | 是    | string        | 接入项目的唯一标识，可在 [账号信息](https://console.cloud.tencent.com/developer) 或 [云 API 密钥](https://console.cloud.tencent.com/cam/capi) 中查看 |
| image | 否    | string(bytes) | 使用 base64 编码的二进制图片数据                     |
| url   | 否    | string        | 图片 url 地址，url 与 image 两者填一个即可。同时赋值时，则以 url 指定的图像作为输入 |


## 返回内容

| 字段         | 类型          | 说明         |
| ---------- | ----------- | ---------- |
| code       | int         | 返回状态值      |
| message    | string      | 返回错误消息     |
| data.items | array(item) | 识别出的所有字段信息 |

item说明

| 字段         | 类型          | 说明                              |
| ---------- | ----------- | ------------------------------- |
| itemstring | string      | 字段字符串                           |
| itemcoord  | object      | 字段在图像中的像素坐标，包括左上角坐标 （x,y），以及宽、高 |
| words      | array(word) | 字段识别出来的每个字的信息                   |

words说明

| 字段         | 类型     | 说明                          |
| ---------- | ------ | --------------------------- |
| character  | string | 识别出的单字字符                    |
| confidence | float  | 识别出的单字字符对应的置信度，取值范围 [0,100] |


## 实际示例
### 参数示例

```
{
"app_id":"123456",
"image":"SALDKHKAFLASD",
"session_id":"1000000111111"
}

```
### 返回示例

```
{
"code":0,
"message":"OK",
"items":
 [
 {
"itemstring":"发票代码"，
"itemcoord":{"x" : 0, "y" : 1, "width" : 2, "height" : 3},
 "words": [{"character": " 手 ", "confidence": 98.99}, {"character": " 机 ",
"confidence": 87.99}]
 },
 {
"itemstring":"开票日期"，
"itemcoord":{"x" : 0, "y" : 1, "width" : 2, "height": 3},
 "words": [{"character": " 姓 ", "confidence": 98.99}, {"character": " 名 ",
"confidence": 87.99}]
 }
 ],
"session_id":"xxxxxx"
}
```

## HTTP 返回码

| 错误码  | 含义                    |
| ---- | --------------------- |
| 400  | 请求不合法，包体格式错误          |
| 401  | 权限验证失败                |
| 403  | 鉴权信息不合法，禁止访问          |
| 404  | 请求失败                  |
| 411  | 请求没有指定 content length |
| 413  | 请求包体太大                |
| 424  | 请求的方法没有找到             |
| 500  | 服务内部错误                |
| 502  | 网关错误，计算后台服务不可用        |
| 503  | 服务不可用                 |
| 504  | 后端服务超时 或者 处理失败        |


## 错误码

| 错误码   | 含义       |
| ----- | -------- |
| -1102 | 图片解码失败   |
| -1300 | 图片为空     |
| -1301 | 参数为空     |
| -1304 | 参数过长     |
| -9018 | OCR 识别失败 |
