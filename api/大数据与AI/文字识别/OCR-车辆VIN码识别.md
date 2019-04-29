## 接口描述

### 服务简介

本接口用来识别车辆 vin 码，根据用户上传的图像，返回识别出的车辆识别代码。

### 计费说明

本接口目前是免费体验阶段，预计 9 月起开始收费。

### url说明

支持 HTTP 和 HTTPS 两种协议：

`http://recognition.image.myqcloud.com/ocr/vin_detection`

`https://recognition.image.myqcloud.com/ocr/vin_detection`

## 请求方式

### 请求头header

| 参数名            | 值                              | 描述                                       |
| -------------- | ------------------------------ | ---------------------------------------- |
| host           | recognition.image.myqcloud.com | 腾讯云文字识别服务器域名                             |
| content-length | 包体总长度                          | 每个请求的包体大小限制为 6MB，不支持 .gif 类型的动图          |
| content-type   | application/json               | 标准 json 格式                               |
| authorization  | 鉴权签名                           | 用于鉴权的签名，使用多次有效签名。详请参见 [鉴权签名](https://cloud.tencent.com/document/product/641/12409)。 |

#### 请求参数

| 参数名   | 必选   | 类型            | 参数说明                                     |
| ----- | ---- | ------------- | ---------------------------------------- |
| appid | 是    | String        | 接入项目的唯一标识，可在 [账号信息](https://console.cloud.tencent.com/developer) 或 [云 API 密钥](https://console.cloud.tencent.com/cam/capi) 中查看。 |
| image | 否    | String(Bytes) | 使用 base64 编码的二进制图片数据                       |
| url   | 否    | String        | 图片的 url、image 和 url 只提供一个即可，如果都提供，只使用 url    |


### 返回内容

| 字段         | 类型           | 说明                     |
| ---------- | ------------ | ---------------------- |
| code       |Int          | 返回码                    |
| message    | String       | 返回错误消息                 |
| data.items | Arrays(Item) | 识别出的所有字段信息，详见下文 items 说明 |

items说明

| 字段         | 类型     | 说明                                       |
| ---------- | ------ | ---------------------------------------- |
| item       | String | 字段名称                                     |
| itemcoord  | Object | 字段在图像中的像素坐标，包括左上角坐标 x、y，以及宽 width、高  height |
| itemstring | String | 字段内容                                     |
| words      | Array  | 字段识别出来的每个字的信息，详见下文 words 说明                |

words说明

| 字段         | 类型     | 说明             |
| ---------- | ------ | -------------- |
| character  | String | 识别出的单字字符       |
| confidence | Float  | 识别出的单字字符对应的置信度 |

## 请求示例

### 请求示例

```
{

"app_id":"123456",

"image":"SALDKHKAFLASD",

}

```

### 返回示例

```
{

"errorcode":0,

"errormsg":"OK",

"items":

    [

        {

  "itemstring":"手机"，

"itemcoord":{"x": 0, "y" : 1, "width" : 2, "height" : 3}, 

            "words": [{"character":"手","confidence": 98.99}, {"character": "机", "confidence": 87.99}]

        },

        {

               "itemstring":"姓名"，

 "itemcoord":{"x": 0, "y" : 1, "width" : 2, "height": 3},

           "words": [{"character":"姓","confidence": 98.99}, {"character": "名", "confidence": 87.99}]

        }

    ],

"session_id":"xxxxxx"

}



```

 

## 错误码

| 错误码   | 协议                  |
| ----- | ------------------- |
| 400   | 请求不合法，包体格式错误        |
| 401   | 权限验证失败              |
| 403   | 鉴权信息不合法，禁止访问        |
| 404   | 请求失败                |
| 411   | 请求没有指定 contentLength |
| 413   | 请求包体太大              |
| 424   | 请求的方法没有找到           |
| 500   | 服务内部错误              |
| 502   | 网关错误，计算后台服务不可用      |
| 503   | 服务不可用               |
| 504   | 后端服务超时或者 处理失败       |
| -1102 | 图片解码失败              |
| -1300 | 图片为空                |
| -1301 | 参数为空                |
| -1304 | 参数过长                |
| -9003 | OCR 识别失败             |
