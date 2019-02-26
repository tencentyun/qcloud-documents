## 接口描述
接口请求域名：`https://recognition.image.myqcloud.com/detection/porn_detect`
本接口（porn_detect）用于对用户上传的图片进行鉴黄处理。

>?
- 本接口支持 HTTPS 协议，如果您现在使用的是 HTTP 协议，为了保障您的数据安全，请切换至 HTTPS。
- 开发者无需注册账号，即可在 [用户体验平台](http://cloud.tencent.com/event/pd) 体验智能鉴黄效果。

## 请求头 header
所有请求都要求含有以下头部信息：

| 参数          | 必选|值                         | 描述                                     |
| -------------- | ----|---------------------- | ---------------------------------------- |
| host           | 是|recognition.image.myqcloud.com | 腾讯云图片鉴黄服务器域名                    |
| content-length | 否|包体总长度                  | 整个请求包体内容的总长度，单位：字节（byte）  |
| content-type   | 是|application/json 或  multipart/form-data  | 根据不同接口选择，每个请求最多支持 20 张 url 或图片：<br/>1. 使用图片 url，选择 application/json；<br/>2. 使用图片文件，选择 multipart/form-data。 |
| authorization  | 是|鉴权签名                    | 用于 [**鉴权**](/document/product/864/17712) 的签名 |

>!如选择 multipart/form-data，请使用 HTTP 框架/库推荐的方式设置请求的 contenttype，不推荐直接调用 setheader 等方法设置，否则可能导致 boundary 缺失引起请求失败。

## 使用图片 url
### 输入参数
使用 application/json 格式：

| 参数       | 必选 | 类型        | 说明        |
| -------- | ---- | --------- | --------- |
| appid    | 是   | String    | 接入项目的唯一标识，可在 [账号信息](https://console.cloud.tencent.com/developer) 或 [云 API 密钥](https://console.cloud.tencent.com/cam/capi) 中查看。     |
| url_list | 是   | String 数组 | 图片 url 列表 |

### 输出参数
接口返回的 result_list 为 JSON 数组，数组的每个元素如下：

| 字段      | 类型     | 说明           |
| ------- | ------ | ------------ |
| code    | Int    | 错误码，0为成功。    |
| message | String | 服务器返回的信息。    |
| url     | String | 当前图片的 url。    |
| data    | Object | 具体查询数据，具体见下表。 |

data 字段具体内容：

| 字段            | 类型     | 说明                                       |
| ------------- | ------ | ---------------------------------------- |
| result        | Int    | 供参考的识别结果：0为正常，1为黄图，2为疑似图片。                |
| confidence    | Double | 识别为黄图的置信度，分值 0-100；是 normal_score、hot_score、porn_score 的综合评分。 |
| normal_score  | Double | 图片为正常图片的评分。                               |
| hot_score     | Double | 图片为性感图片的评分。                               |
| porn_score    | Double | 图片为色情图片的评分。                               |
| forbid_status | Int    | 封禁状态，0表示正常，1表示图片已被封禁（只有存储在腾讯云的图片才会被封禁）。 |

>?
- 当 result=0时，表明图片为正常图片。
- 当 result=1时，表明该图片是系统判定为违禁涉黄的图片，如果存储在腾讯云则会直接被封禁掉。
- 当 result=2 时，表明该图片是疑似图片(83 ≤ confidence < 91)，即为黄图的可能性很大。

### 示例
输入示例：
```
POST /detection/porn_detect HTTP/1.1
Authorization: FCHXddYbhZEBfTeZ0j8mn9Og16JhPTEwMDAwMzc5Jms9QUtJRGVRZDBrRU1yM2J4ZjhRckJiUkp3Sk5zbTN3V1lEeHN1JnQ9MTQ2ODQ3NDY2MiZyPTU3MiZ1PTAmYj10ZXN0YnVja2V0JmU9MTQ3MTA2NjY2Mg==
Host: recognition.image.myqcloud.com
Content-Length: 238
Content-Type: "application/json"

{
    "appid": 10000379,
    "url_list": [
        "http://www.bz55.com/uploads/allimg/140805/1-140P5162300-50.jpg",
        "http://img.taopic.com/uploads/allimg/130716/318769-130G60P30462.jpg"
    ]
}
```

输出示例：
```
{
    "result_list": [
        {
            "code": 0,
            "message": "success",
            "url": "http://www.bz55.com/uploads/allimg/140805/1-140P5162300-50.jpg",
            "data": {
                "result": 0,
                "forbid_status": 0,
                "confidence": 12.509,
                "hot_score": 87.293,
                "normal_score": 12.707,
                "porn_score": 0.0
            }
        },
        {
            "code": 0,
            "message": "success",
            "url": "http://img.taopic.com/uploads/allimg/130716/318769-130G60P30462.jpg",
            "data": {
                "result": 0,
                "forbid_status": 0,
                "confidence": 14.913,
                "hot_score": 99.997,
                "normal_score": 0.003,
                "porn_score": 0.0
            }
        }
    ]
}
```
## 使用图片文件

### 输入参数
使用 multipart/form-data 格式：

| 参数    | 必选 | 类型         | 说明                                       |
| ----- | ---- | ---------- | ---------------------------------------- |
| appid | 是   | uint       | 业务 ID。                                    |
| image | 是   | image/jpeg | 图片文件，每个请求最多支持20个。参数名须为 “image[0]”、“image[1]”等，每张图片需指定 filename。 |

### 输出参数
接口返回的 result_list 为 json 数组，数组的每个元素如下：

| 字段       | 类型     | 说明                               |
| -------- | ------ | -------------------------------- |
| code     | Int    | 服务器错误码，0为成功。                     |
| message  | String | 服务器返回的信息。                         |
| filename | String | 当前图片的 filename，与请求包中 filename 一致。 |
| data     | Object | 具体查询数据，内容见下表。                     |

data 字段具体内容：

| 字段            | 类型     | 说明                                       |
| ------------- | ------ | ---------------------------------------- |
| result        | Int    | 供参考的识别结果：0为正常，1为黄图，2为疑似图片。                |
| confidence    | Double | 识别为黄图的置信度，分值 0-100 ；是 normal_score、hot_score、porn_score 的综合评分。 |
| normal_score  | Double | 图片为正常图片的评分。                               |
| hot_score     | Double | 图片为性感图片的评分。                               |
| porn_score    | Double | 图片为色情图片的评分。                               |
| forbid_status | Int    | 封禁状态，0表示正常，1表示图片已被封禁（只有存储在腾讯云的图片才会被封禁）。 |
>?
- 当 result=0时，表示该图片为正常图片。</br>
- 当 result=1时，表示该图片是系统判定的涉黄违禁的图片，如果存储在腾讯云则会直接被封禁掉。</br>
- 当 result=2时，表示该图片是疑似图片(83 ≤ confidence < 91)，即为黄图的可能性很大。

### 示例
输入示例：
```
POST /detection/porn_detect HTTP/1.1
Content-Type:multipart/form-data;boundary=-------------------------acebdf13572468
Authorization:FCHXddYbhZEBfTeZ0j8mn9Og16JhPTEwMDAwMzc5Jms9QUtJRGVRZDBrRU1yM2J4ZjhRckJiUkp3Sk5zbTN3V1lEeHN1JnQ9MTQ2ODQ3NDY2MiZyPTU3MiZ1PTAmYj10ZXN0YnVja2V0JmU9MTQ3MTA2NjY2Mg==
Host: recognition.image.myqcloud.com
Content-Length: 61478

---------------------------acebdf13572468
Content-Disposition: form-data; name="appid";

10000379
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

输出示例：
```
{
    "result_list": [
        {
            "code": 0,
            "message": "success",
            "filename": "1.jpg",
            "data": {
                "result": 1,
                "forbid_status": 0,
                "confidence": 96.853,
                "hot_score": 0.0,
                "normal_score": 0.0,
                "porn_score": 100.0
            }
        },
        {
            "code": 0,
            "message": "success",
            "filename": "2.jpg",
            "data": {
                "result": 0,
                "forbid_status": 0,
                "confidence": 41.815,
                "hot_score": 19.417,
                "normal_score": 0.077,
                "porn_score": 80.506
            }
        }
    ]
}
```

## 错误码
| **错误码** | **含义**                               |
| ------- | ------------------------------------ |
| 3       | 错误的请求；其中 message:account abnormal,errorno is:2 为账号欠费停服                                |
| 4       | 签名为空                                 |
| 5       | 签名串错误                                |
| 6       | APPID/存储桶/ url 不匹配                  |
| 7       | 签名编码失败（内部错误）                         |
| 8       | 签名解码失败（内部错误）                         |
| 9       | 签名过期                                 |
| 10      | APPID 不存在                            |
| 11      | SecretId 不存在                         |
| 12      | APPID 不匹配                            |
| 13      | 重放攻击                                 |
| 14      | 签名失败                                 |
| 15      | 操作太频繁，触发频控                           |
| 16      | 内部错误                                 |
| 17      | 未知错误                                 |
| 200     | 内部打包失败                               |
| 201     | 内部解包失败                               |
| 202     | 内部链接失败                               |
| 203     | 内部处理超时                               |
| -1300   | 图片为空                                 |
| -1308   | url 图片下载失败                           |
| -1400   | 非法的图片格式                              |
| -1403   | 图片下载失败                               |
| -1404   | 图片无法识别                               |
| -1505   | url 格式不对                             |
| -1506   | 图片下载超时                               |
| -1507   | 无法访问 url 对应的图片服务器                    |
| -5062   | url 对应的图片已被标注为不良图片，无法访问（专指存储于腾讯云的图片） |

更多其他 API 错误码请查看 [**错误码说明**](/document/product/864/17713) 。









