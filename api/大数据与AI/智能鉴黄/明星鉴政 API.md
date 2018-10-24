## 接口概述

### 服务简介
本接口用于明星、名人的识别。支持用户上传人脸图像，返回识别出的明星名人等信息。

### url 说明
支持 http 和 https 两种协议：

`http://recognition.image.myqcloud.com/celebrity/identify`

`https://recognition.image.myqcloud.com/celebrity/identify`

## 请求头 header
所有请求都要求含有以下头部信息：

| 参数名            | 必选| 值              | 描述                            |
| -------------- | -------|---------------- | ---------------------------------------- |
| host           | 是     | recognition.image.myqcloud.com          | 腾讯云智能图像识别服务器域名       |
| content-length | 否      |包体总长度             | 每个请求的包体大小限制为 6 MB；所有接口都为 post 方法； 不支持 .gif 这类的动图。               |
| content-type   | 是      |application/json 或 multipart/form-data | 根据不同接口选择，每个请求最多支持 20 张 url 或图片：<br/>1. 使用图片 url，选择 application/json；<br/>2. 使用图片文件，选择 multipart/form-data。               |
| authorization  | 是      |鉴权签名             | 多次有效签名，用于鉴权，详见[鉴权签名方法](/document/product/641/12409) |
>**注意：**如选择 multipart/form-data，请使用 http 框架/库推荐的方式设置请求的 content-type，不推荐直接调用 setheader 等方法设置，否则可能导致 boundary 缺失引起请求失败。


### 请求参数

| 参数名称  | 必选 | 类型          | 说明                                  |
| ----- | ---- | ----------- | ----------------------------------- |
| appid | 是   | string      | 腾讯云申请的 appid                        |
| image | 否   | binary | 图片文件 |
| url   | 否   | string      | 图片 url                              |
| topk  | 否   | int         | 每个人脸返回的最相似的人物数量，默认为top 5            |
| seq   | 否   | string      | 标示识别请求的序列号                          |

> 注意： 
> 入参优先级，urls > images > url > image。

## 请求示例
### 使用 url 的请求示例

```
POST /celebrity/identify HTTP/1.1
Authorization: FCHXdPTEwMDAwMzc5Jms9QUtJRGVRZDBrRU1yM2J4ZjhRckJi==
Host: recognition.image.myqcloud.com
Content-Length: 187
Content-Type: application/json

{
  "appid":"123456",
  "url":"http://cossh.myqcloud.com/star.jpg",
  "seq":"xxx"
}
```

### 使用图片 Base64 编码的请求示例

```
POST /celebrity/identify HTTP/1.1
Authorization: FCHXdPTEwMDAwMzc5Jms9QUtJRGVRZDBrRU1yM2J4ZjhRckJi==
Host: recognition.image.myqcloud.com
Content-Length: 187
Content-Type: application/json

{
  "appid":"123456",
  "image":"==base64=code==",
  "seq":"xxx"
}
```

### 使用图片文件的请求示例

```
POST /celebrity/identify HTTP/1.1
Authorization: FCHXdPTEwMDAwMzc5Jms9QUtJRGVRZDBrRU1yM2J4ZjhRckJi==
Host: recognition.image.myqcloud.com
Content-Length: 735
Content-Type: multipart/form-data;boundary=--------------acebdf13572468

----------------acebdf13572468
Content-Disposition: form-data; name="appid";

test
----------------acebdf13572468
Content-Disposition: form-data; name="seq";

xxx
----------------acebdf13572468
Content-Disposition: form-data; name="image"; filename="star.jpg"
Content-Type: image/jpeg

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
----------------acebdf13572468--
```


## 返回示例

| 字段      | 类型     | 说明           |
| ------- | ------ | ------------ |
| code    | int    | 服务器错误码，0 为成功 |
| message | string | 服务器返回的信息     |
| seq     | string | string       |
| data    | result | 识别结果列表，内容见下表 |

Result字段具体内容：

| 字段    | 类型          | 说明   |
| ----- | ----------- | ---- |
| faces | array(face) | 人脸列表 |

Face说明

| 字段         | 类型              | 说明                                       |
| ---------- | --------------- | ---------------------------------------- |
| face_infos | array(faceInfo) | 人物信息列表，按置信度逆序排序，可以通过入参topk控制返回的个数，默认top5 |
| face_coord | coord           | 人脸在图像中的像素坐标                              |

FaceInfo说明

| 字段         | 类型     | 说明                           |
| ---------- | ------ | ---------------------------- |
| face_id    | string | 人物 ID                         |
| face_name  | string | 人物姓名                         |
| confidence | double | 结果置信度，取值范围[0，1] ，目前建议阈值0.6以上 |

Coord说明

| 字段     | 类型   | 说明      |
| ------ | ---- | ------- |
| x      | Int  | 商品框左上角x |
| y      | Int  | 商品框左上角y |
| width  | Int  | 商品框宽度   |
| height | Int  | 商品框高度   |

### 示例

```
{
    "code": 0,
    "message": "ok",
    "data": {
        "faces": [{
            "face_infos": [{
                "face_id": "n010239",
                "face_name": "全度妍",
                "confidence": 0.4776408672332764
            }, {
                "face_id": "n009934",
                "face_name": "潘晓婷",
                "confidence": 0.38438236713409426
            }],
            "face_coord": {
                "x": 173,
                "y": 91,
                "width": 142,
                "height": 142
            }
        }, {
            "face_infos": [{
                "face_id": "n009489",
                "face_name": "苏有朋",
                "confidence": 0.7746740579605103
            }, {
                "face_id": "n003468",
                "face_name": "韩青",
                "confidence": 0.4874064922332764
            }],
            "face_coord": {
                "x": 6,
                "y": 77,
                "width": 170,
                "height": 170
            }
        }, {
            "face_infos": [{
                "face_id": "n010502",
                "face_name": "赵薇",
                "confidence": 0.7209092378616333
            }, {
                "face_id": "n009805",
                "face_name": "申敏儿",
                "confidence": 0.3396953344345093
            }],
            "face_coord": {
                "x": 286,
                "y": 107,
                "width": 134,
                "height": 134
            }
        }]
    }
}
```


## 错误码
| 错误码  | 含义                         |
| ---- | -------------------------- |
| 3    | 错误的请求                      |
| 4    | 签名为空                       |
| 5    | 签名串错误                      |
| 6    | 签名中的 appid/bucket 与操作目标不匹配 |
| 9    | 签名过期                       |
| 10   | appid 不存在                  |
| 11   | secretid 不存在               |
| 12   | appid 和 secretid 不匹配       |
| 13   | 重放攻击                       |
| 14   | 签名校验失败                     |
| 15   | 操作太频繁，触发频控                 |
| 16   | Bucket不存在                  |
| 21   | 无效参数                       |
| 23   | 请求包体过大                     |
| 24   | 没有权限                       |
| 25   | 您购买的资源已用完                  |
| 107  | 鉴权服务内部错误                   |
| 108  | 鉴权服务不可用                    |
| 213  | 内部错误                       |