## 接口描述
接口请求域名：`https://recognition.image.myqcloud.com/v1/detection/imagetag_detect`
本接口（imagetag_detect）用于识别图片内容信息，并以标签的形式显示。
>!本接口支持 HTTPS 协议，如果您现在使用的是 HTTP 协议，为了保障您的数据安全，请切换至 HTTPS。

## 请求头 header
>!如果选择 multipart/form-data，请使用 HTTP 框架/库推荐的方式，设置请求的 contenttype，不推荐直接调用 setheader 等方法进行设置，否则可能导致由于 boundary 缺失引起的请求失败。

所有请求都要求含有以下头部信息：

| 参数名            | 必选|值                          | 描述                       |
| -------------- | -----|--------------------- | ------------------------ |
| host           | 是|recognition.image.myqcloud.com | 腾讯云图片分析服务器域名。           |
| content-length | 否|包体总长度                  | 整个请求包体内容的总长度，单位：字节（Byte）。 |
| content-type   | 是|application/json 或  multipart/form-data   | 根据不同接口选择：<br/>1. 使用图片 url，选择 application/json。<br/>2. 使用图片文件，选择 multipart/form-data。  |
| authorization  | 是|鉴权签名                    | 多次有效签名，用于鉴权，生成方式见 [鉴权签名方法](/document/product/865/17723)。     |

## 输入参数

| 参数名 | 必选 | 类型   | 说明                                    |
| ----- | ---- | ------| ---------------------------------------- |
| appid | 是   | String |接入项目的唯一标识，可在 [账号信息](https://console.cloud.tencent.com/developer) 或 [云 API 密钥](https://console.cloud.tencent.com/cam/capi) 中查看。                                     |
| image | 否   | String | 图像 Base64 编码，图像格式为 JPG/PNG/BMP 其中之一。 |
| url   | 否  | String | 可下载的图片 url。如果 url 和 image 都提供，仅使用 url。  |



## 输出参数
| 字段      | 类型    | 说明                     |
| ------- | -------- | -------------------     |
| code    | Int      | 错误码，0为成功。          |
| message | String   | 服务器返回的信息。           |
| tags    | ImageTag | 图像的分类标签列表，具体内容如下表。 |

其中 ImageTag 具体内容为：      

| 字段             | 类型     | 说明                            |
| -------------- | ------ | ----------------------------- |
| tag_name       | String | 返回的图像分析名字。                     |
| tag_confidence | Int    | 图像分析的置信度，取值范围[0， 100]，数值越大置信度越高。 |


## 示例
### 输入示例
```
POST /v1/detection/imagetag_detect HTTP/1.1
Host: recognition.image.myqcloud.com
Content-Type: application/json
authorization: WrE/BkJAorkCm0gg3/GKdVttlqVhPTEyNTcyMzc1MTEmaz1BS0lEZVE0WnN5b2I3MHl3b0Y4aWpaRGo1SUo4YnpCSGZ1UWsmZT0xNTUwOTEzMTkwJnQ9MTU0ODMyMTE5MCZyPTE4MDQyODkzODM=
cache-control: no-cache

{
    "appid": "1234567890",
    "image": "图片的base64"
}
```

### 输出示例
```
{
    "code": 0,
    "message": "success",
    "tags": [
        {
            "tag_name": "大头照",
            "tag_confidence": 18
        },
        {
            "tag_name": "女孩",
            "tag_confidence": 65
        },
        {
            "tag_name": "海报",
            "tag_confidence": 12
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
| 6       | APPID/存储桶/url 不匹配                  |
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


更多其他 API 错误码请查看 [**错误码说明**](https://cloud.tencent.com/document/product/865/17722) 。
