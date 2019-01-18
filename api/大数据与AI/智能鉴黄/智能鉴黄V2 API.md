## 接口概述

### 服务简介
本接口用于根据用户上传的图像，返回判别图片为"色情（porn）","低俗（vulgar）","擦边（somewhat）","性感（sexy）","正常（normal）"这五种情况的可能性。

### url 说明
支持 HTTP 和 HTTPS 两种协议：

`http://recognition.image.myqcloud.com/porn/picture_detect`

`https://recognition.image.myqcloud.com/porn/picture_detect`


## 请求头 header
所有请求都要求含有以下头部信息：

| 参数名称        | 值                             | 描述                                       |
| -------------- | ---------------------------------------- | ------------------------------|
| host           | https://recognition.image.myqcloud.com/porn/picture_detect           | 腾讯云智能图像识别服务器域名                           |
| content-length | 包体总长度                   | 每个请求的包体大小限制为 6MB；所有接口都为 POST 方法； 不支持 .gif 这类的动图。          |
| content-type   | application/json 或  multipart/form-data| 根据不同接口选择，每个请求最多支持 20 张 url 或图片：<br/>1. 使用图片 url，选择 application/json；<br/>2. 使用图片文件，选择 multipart/form-data。                               |
| authorization  | 鉴权签名        | 多次有效签名,用于鉴权，具体生成方式详见 [鉴权签名方法](/document/product/864/17712)。 |

### 请求参数

| 参数名称   | 必选 | 类型            | 描述                                       |
| ------ | ---- | ------------- | ---------------------------------------- |
| app_id | 是   | string        | 接入项目的唯一标识，可在 [账号信息](https://console.cloud.tencent.com/developer) 或 [云 API 密钥](https://console.cloud.tencent.com/cam/capi) 中查看。                       |
| image  | 否   | binary | 图片内容                     |
| url    | 否   | string       | 图片 url 地址，url 与 image 两者填一个即可。同时赋值时，则以 url 指定的图像作为输入 |


### 返回内容

| 字段         | 类型          | 说明         |
| ---------- | ----------- | ---------- |
| code       | int         | 返回状态值      |
| message    | string      | 返回错误消息     |
| data.items | array(item) | 识别出的所有类别信息 |

item说明：

| 字段         | 类型   | 说明   |
| ------------| ------ | ----- |
| items 	  | string | 5种类别 |
|level_name   | string | 对应的类别名称 |
|probability  | float   | 对应类别的可能性 |



## 请求示例

```
{
"app_id":"1000001",
"image":"SALDKHKAFLASD",
}
```


## 返回示例

```
{
    "code": 0,
    "message": "ok",
    "data": [
        {
            "items": [
                {
                    "level_name": "porn",
                    "probability": 0.000008085176887107082
                },
                {
                    "level_name": "vulgar",
                    "probability": 0.01226817350834608
                },
                {
                    "level_name": "somewhat",
                    "probability": 0.16955731809139253
                },
                {
                    "level_name": "sexy",
                    "probability": 0.8175094127655029
                },
                {
                    "level_name": "normal",
                    "probability": 0.000656917633023113
                }
            ]
        }
    ]
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