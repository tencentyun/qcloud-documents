## 接口概述

### 服务简介
图片标签 V2 版接口，用于根据用户上传的图像，识别并返回图片内包含的各种元素，以及属于这些元素的可能性。  

### URL 说明
支持 HTTP 和 HTTPS 两种协议：

`http://recognition.image.myqcloud.com/imagetag/picture_classify`

`https://recognition.image.myqcloud.com/imagetag/picture_classify`

>?如果开发者使用的是 V1 版本，您也可以切换本版本以获得更优体验。

## 请求方式

### 请求头 header

| 参数名称        | 值                                       | 描述                                       |
| -------------- | ---------------------------------------- | ------------------------------|
| Host           | recognition.image.myqcloud.com           | 腾讯云智能图像识别服务器域名。                           |
| Content-Length | 包体总长度                                   | 整个请求包体内容的总长度，每个请求的包体大小限制为 6MB。                |
| Content-Type   | application/json |  根据不同接口选择：<br/>1. 使用 application/json 格式，参数为 url ，其值为图片链接；<br>2. 使用 multipart/form-data 格式，参数为 image，其值为图片的二进制内容。                                    |
| Authorization  | 鉴权签名                                    | 多次有效签名,用于鉴权，具体生成方式详见 [鉴权签名方法](https://cloud.tencent.com/document/product/865/17723)。 |

>**注意**：如选择 multipart/form-data，请使用 HTTP 框架/库推荐的方式设置请求的 contenttype，不推荐直接调用 setheader 等方法设置，否则可能导致 boundary 缺失引起请求失败。


### 请求参数

| 参数名称   | 必选 | 类型            | 描述                                       |
| ------ | ---- | ------------- | ---------------------------------------- |
| App_ID | 是   | String        | 接入项目的唯一标识，可在 [账号信息](https://console.cloud.tencent.com/developer) 或 [云 API 密钥](https://console.cloud.tencent.com/cam/capi) 中查看。                          |
| image  | 否   | String(Bytes) | 使用 base64 编码的二进制图片数据。                     |
| url    | 否   | String        | 图片 url 地址，url 与 image 两者填一个即可。同时赋值时，则以 url 指定的图像作为输入。 |


### 返回内容

| 字段         | 类型          | 说明         |
| ---------- | ----------- | ---------- |
| code       | Int         | 返回状态值      |
| message    | String      | 返回错误消息     |
| data.items | Array(item) | 识别出的所有类别信息 |

item 说明：

| 字段         | 类型   | 说明   |
| ------------| ------ | ----- |
| items 	  | String | 5种类别 |
|level_name   | String | 对应的类别名称 |
|probability  | Float   | 对应类别的可能性 |

## 实际示例

### 请求示例

```
{
"app_id":"1000001",
"image":"SALDKHKAFLASD",
}
```

### 返回示例

```
{
    "code": 0,
    "message": "ok",
    "data": [
        {
            "items": [
                {
                    "label_name": "Person",
                    "probability": 0.9545053839683533
                },
                {
                    "label_name": "Sportsequipment",
                    "probability": 0.7610472440719603
                },
                {
                    "label_name": "Clothing",
                    "probability": 0.7246530652046204
                },
                {
                    "label_name": "Footwear",
                    "probability": 0.6895578503608704
                },
                {
                    "label_name": "Man",
                    "probability": 0.38944029808044436
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
| 504  | 后端服务超时或者处理失败       |


## 错误码
| 错误码   | 含义       |
| ----- | -------- |
| -1102 | 图片解码失败   |
| -1300 | 图片为空     |
| -1301 | 参数为空     |
| -1304 | 参数过长     |
