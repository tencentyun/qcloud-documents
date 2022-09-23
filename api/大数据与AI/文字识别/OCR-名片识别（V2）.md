>!
- 名片识别接口全面升级，算法更强、性能更优，支持子账号调用。欢迎立即体验 [新版名片识别](https://cloud.tencent.com/document/product/866/36214)。
- 新老版本的接口计费模式相同，且共享计费阶梯和资源包，您可以在【文字识别控制台】>【[用量统计](https://console.cloud.tencent.com/ocr/stats)】中查看调用情况。
- 老版本接口我们仍继续维护，但不支持新客户开通调用，建议您使用 [新版名片识别](https://cloud.tencent.com/document/product/866/36214)，体验更优服务。
## 接口描述
接口请求域名：`https://recognition.image.myqcloud.com/ocr/businesscard`
本接口（businesscard）用于根据用户上传的名片图片，返回识别出的20多个字段信息，详细字段包括：姓名、英文姓名、职位、英文职位、部门、英文部门、公司、英文公司、地址、英文地址、邮编、邮箱、网址、手机、电话、传真、MSN、QQ、微信、微博、公司账号、logo、其他。

>?
- 本接口支持 HTTPS 协议，如果您现在使用的是 HTTP 协议，为了保障您的数据安全，请切换至 HTTPS。
- 如果开发者使用的是 V1 版本，为获得更优体验，请及时切换到 [新版名片识别](https://cloud.tencent.com/document/product/866/36214)。

## 请求头 header

| 参数名            |必选| 值                                        | 描述                                       |
| -------------- | -----|----------------------------------- | ---------------------------------------- |
| host           |  是   | recognition.image.myqcloud.com        | 腾讯云文字识别服务器域名。                       |
| content-length |  否   | 包体总长度                          | 每个请求的包体大小限制为6MB，不支持 .gif 类型的动图。 | 
| content-type   | 是| application/json 或者 multipart/form-data | 根据不同接口选择：<br/>1. 使用 application/json 格式，参数为 url ，其值为图片链接。<br>2. 使用 multipart/form-data 格式，参数为 image，其值为图片的二进制内容。 |
| authorization  | 是| 鉴权签名                                    | 多次有效签名，用于鉴权， 具体生成方式详见 [鉴权签名方法](https://cloud.tencent.com/document/product/866/17734)。 |


>!如选择 multipart/form-data，请使用 HTTP 框架/库推荐的方式设置请求的 content-type，不推荐直接调用 setheader 等方法设置，否则可能导致 boundary 缺失引起请求失败。


## 输入参数

| 参数名       | 必选     | 类型           | 说明                               |
| ------------- | ----------- | ------------- | ---------------------------------  |
| appid         | 是         | String        | 接入项目的唯一标识，可在 [账号信息](https://console.cloud.tencent.com/developer) 或 [云 API 密钥](https://console.cloud.tencent.com/cam/capi) 中查看.                 |
| image         | 否   | Binary | 图片文件，支持多个。参数名须为 “image[0]”、“image[1]”等 image 开头的字符串。响应 HTTP body 中会按照该字符串的字典序排列。每张图片需指定 filename，filename 的值为可为空，响应 HTTP Body 中会返回用户设置的 filename 值。 |
| url_list	    | 否  |	String 数组	    | 图片 url 列表，和 image 同时赋值时，则以 url 指定的图像作为输入。|

## 输出参数

| 字段          | 类型      | 说明           |
| ----------- | ------- | ------------ |
| result_list | JSON 数组 | 具体查询数据，内容见下表。 |

result_list（JSON 数组）中每一项的具体内容：

| 字段      | 类型     | 说明           |
| ------- | ------ | ------------ |
| code    | Int    | 服务器错误码，0为成功。 |
| message | string | 服务器返回的信息。     |
| url     | String | 请求参数选择 url，则返回当前图片的 url。    |
| filename     | String | 请求参数选择 image，当前图片的 filname。    |
| data    | Array(item) | 具体查询数据，内容见下表。 |

data 字段具体内容：

| 字段               | 类型     | 说明                     |
| ---------------- | ------ | ---------------------- |
| item             | String | 字段字符串                     |
| value            | String | 字段识别出来的信息                    |
| confidence  | Double | 字段识别出来的信息的置信度，取值范围[0,1]  |

## 示例
### 输入示例
#### 使用 application/json 
```
POST /ocr/businesscard HTTP/1.1
Authorization: FCHXdPTEwMDAwMzc5Jms9QUtJRGVRZDBrRU1yM2J4ZjhRckJi==
Host: recognition.image.myqcloud.com
Content-Length: 187
Content-Type: application/json

{
  "appid":"123456",
  "bucket":"test",
  "url_list":["http://yoututest-1251966477.cossh.myqcloud.com/mingpian.jpg"]
}
```

#### 使用 multipart/form-data  
```
POST /ocr/businesscard HTTP/1.1
Authorization: FCHXdPTEwMDAwMzc5Jms9QUtJRGVRZDBrRU1yM2J4ZjhRckJi==
Host: recognition.image.myqcloud.com
Content-Length: 735
Content-Type: multipart/form-data;boundary=--------------acebdf13572468

----------------acebdf13572468
Content-Disposition: form-data; name="appid";

123456
----------------acebdf13572468
Content-Disposition: form-data; name="bucket";

test
----------------acebdf13572468
Content-Disposition: form-data; name="image"; filename="mingpian.jpg"
Content-Type: image/jpeg

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
----------------acebdf13572468--
```

### 输出示例
```
{
    "result_list": [
        {
            "code": 0,
            "message": "OK",
            "filename": "名片2.jpg",
            "data": [
                {
                    "item": "姓名",
                    "value": "温星涛",
                    "confidence": 0.9994000196456908
                },
                {
                    "item": "职位",
                    "value": "解决方案高级架构师",
                    "confidence": 0.9758999943733216
                },
                {
                    "item": "部门",
                    "value": "云产品部",
                    "confidence": 0.9998999834060668
                },
                {
                    "item": "公司",
                    "value": "Tencent腾讯",
                    "confidence": 0.8555999994277954
                },
                {
                    "item": "地址",
                    "value": "成都市高新区天府三街198号腾讯成都大厦A座1层610041",
                    "confidence": 0.5228000283241272
                },
                {
                    "item": "邮箱",
                    "value": "timwen@tencent.com",
                    "confidence": 0.9995999932289124
                },
                {
                    "item": "手机",
                    "value": "+86-18109023170",
                    "confidence": 0.9914000034332277
                },
                {
                    "item": "电话",
                    "value": "9761758",
                    "confidence": 0.9998999834060668
                },
                {
                    "item": "电话",
                    "value": "+86-28-85225111转51468",
                    "confidence": 0.9078999757766724
                },
                {
                    "item": "传真",
                    "value": "+86-28-85980512",
                    "confidence": 0.9944000244140624
                }
            ]
        }
    ]
}
```


## 错误码
| 错误码   | 含义                         |
| ----- | -------------------------- |
| 3     | 错误的请求；当 "message" 字段等于 “account abnormal,errorno is：2”时，表示账号欠费停服               |
| 4     | 签名为空                       |
| 5     | 签名串错误                      |
| 6     | 签名中的 appid/bucket 与操作目标不匹配 |
| 9     | 签名过期                       |
| 10    | appid 不存在                  |
| 11    | secretid 不存在               |
| 12    | appid 和 secretid 不匹配       |
| 13    | 重放攻击                       |
| 14    | 签名校验失败                     |
| 15    | 操作太频繁，触发频控                 |
| 16    | Bucket不存在                  |
| 21    | 无效参数                       |
| 23    | 请求包体过大                     |
| 24    | 没有权限                       |
| 25    | 您购买的资源已用完                  |
| 107   | 鉴权服务内部错误                   |
| 108   | 鉴权服务不可用                    |
| 213   | 内部错误                       |
| -1102 | 图片解码失败                     |
|-1300 |图片为空|
|-1301| 参数为空|
|-1304  | 参数过长|
| -1308 | 图片下载失败                     |
|-5201 | 名片无足够的文本|
|-5202 |名片文本行倾斜角度太大|
|-5203 | 名片模糊|
|-5204 |名片姓名识别失败|
|-5205 | 名片电话识别失败|
|-5206 | 上传图像不是名片|
|-5207| 检测或者识别失败|
|-5208 | 名片 OCR 服务内部出错|


更多其他 API 错误码请查看 [错误码说明](https://cloud.tencent.com/document/product/866/17733)。   
