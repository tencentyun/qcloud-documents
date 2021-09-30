
>!
- 行驶证驾驶证识别接口全面升级，算法更强、性能更优，支持子账号调用。欢迎立即体验 [新版行驶证识别](https://cloud.tencent.com/document/product/866/36209) 和 [新版驾驶证识别](https://cloud.tencent.com/document/product/866/36213)。
- 新老版本的接口计费模式相同，且共享计费阶梯和资源包，您可以在【文字识别控制台】>【[用量统计](https://console.cloud.tencent.com/ocr/stats)】中查看调用情况。
- 老版本接口我们仍继续维护，但不支持新客户开通调用，建议您使用 [新版行驶证识别](https://cloud.tencent.com/document/product/866/36209) 和 [新版驾驶证识别](https://cloud.tencent.com/document/product/866/36213)，体验更优服务。

## 接口描述
接口请求域名：`https://recognition.image.myqcloud.com/ocr/drivinglicence`
本接口（drivinglicence）用于根据用户上传的图像，识别出行驶证或驾驶证的各字段信息。开发者使用功能之前，需要先注册腾讯云账号，添加密钥。
>?本接口支持 HTTPS 协议，如果您现在使用的是 HTTP 协议，为了保障您的数据安全，请切换至 HTTPS。

## 请求头 header

| 参数名            |必选| 值                                        | 描述                                       |
| -------------- | -----|----------------------------------- | ---------------------------------------- |
| host           |  是   | recognition.image.myqcloud.com        | 腾讯云文字识别服务器域名。                       |
| content-length |  否   | 包体总长度                          | 1. 每个请求的包体大小限制为6MB；<br/>2. 图片格式支持：JPG、JPEG、PNG、BMP 等；<br/>3. 不支持 .gif 类型的动图。 | 
| content-type   | 是| application/json  或者  multipart/form-data | 根据不同接口选择：<br/>1. 使用 application/json 格式，参数 url 或 image，其值为图片链接或图片 base64编码；<br/>2. 使用 multipart/form-data 格式，参数为 image，其值为图片的二进制内容。 |
| authorization  | 是 | 鉴权签名                             | 多次有效签名，用于鉴权，生成方式见 [鉴权签名方法](https://cloud.tencent.com/document/product/866/17734)。|

>?如选择 multipart/form-data，请使用 HTTP 框架/库推荐的方式设置请求的 content-type，不推荐直接调用 setheader 等方法设置，否则可能导致 boundary 缺失引起请求失败。

## 输入参数
使用 multipart/form-data 格式，参数选择 image ；使用 application/json 格式，参数选择 url 或 base64。

| 参数名    | 必选 | 类型     | 说明                                       |
| ------ | ---- | ------ | ---------------------------------------- |
| appid  | 是   | String | 接入项目的唯一标识，可在 [账号信息](https://console.cloud.tencent.com/developer) 或 [云 API 密钥](https://console.cloud.tencent.com/cam/capi) 中查看。                                      |
| type   | 是   | Int    | 识别类型，0 表示行驶证，1 表示驾驶证，2 表示行驶证副页。        |
| image  | 否   | Binary/String | 图片文件 或 图片 base64                                |
| url    | 否   | String | 图片 url。url 和 image 同时赋值时，则以 url 指定的图像作为输入。 |



## 输出参数

| 字段              | 类型          | 说明                |
| --------------- | ----------- | ----------------- |
| data.session_id | String      | 相应请求的 session 标识符 |
| data.items      | Array(Item) | 识别出的所有字段信息        |
| code            | Int         | 返回码               |
| message         | String      | 返回错误消息            |

Item 说明：
<table>
<th colspan="2">字段</th>
<th>类型</th>
<th>说明</th><tr>
<td colspan="2">item</td>
<td>String</td>
<td>字段名称</td><tr>
<td colspan="2">itemstring</td>
<td>String</td>
<td>字段内容</td><tr>
<td colspan="2">itemconf</td>
<td>Float</td>
<td>字段识别结果置信度[0.0, 100.0]</td><tr>
<td rowspan="4">itemcoord</td>
<td >x</td>
<td >Int</td>
<td>item 框左上角 x</td><tr>
<td>y</td>
<td >Int</td>
<td>item 框左上角 y</td><tr>
<td>width</td>
<td >Int</td>
<td>item 框宽度</td><tr>
<td>height</td>
<td >Int</td>
<td>item 框高度</td>
</table>

目前支持的字段为：

| 行驶证    | 驾驶证  |
| ------ | ---- |
| 车牌号码   | 证号   |
| 车辆类型   | 姓名   |
| 所有人    | 性别   |
| 住址     | 国籍   |
| 使用性质   | 住址   |
| 品牌型号   | 出生日期 |
| 识别代码   | 领证日期 |
| 发动机号   | 准驾车型 |
| 注册日期   | 起始日期 |
| 发证日期   | 有效日期 |
|  -  | 红章   |

## 示例
### 输入示例
#### 使用 application/json 
```
POST /ocr/drivinglicence HTTP/1.1
Authorization: FCHXdPTEwMDAwMzc5Jms9QUtJRGVRZDBrRU1yM2J4ZjhRckJi==
Host: recognition.image.myqcloud.com
Content-Length: 187
Content-Type: application/json

{
  "appid":"123456",
  "bucket":"test",
  "type":1,
  "url":"http://test-123456.image.myqcloud.com/test.jpg"
}
```

#### 使用 multipart/form-data 
```
POST /ocr/drivinglicence HTTP/1.1
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
Content-Disposition: form-data; name="type";

1
----------------acebdf13572468
Content-Disposition: form-data; name="image"; filename="test.jpg"
Content-Type: image/jpeg

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
----------------acebdf13572468--
```

### 输出示例
```
{
    "code": 0,
    "message": "OK",
    "data": {
        "session_id": "10000018324840",
        "items": [
            {
                "item": "证号",
                "itemcoord": {
                    "x": 226,
                    "y": 66,
                    "width": 194,
                    "height": 30
                },
                "itemconf": 0.9999638199806212,
                "itemstring": "342221199005033256"
            },
            {
                "item": "姓名",
                "itemcoord": {
                    "x": 84,
                    "y": 98,
                    "width": 93,
                    "height": 26
                },
                "itemconf": 0.999157190322876,
                "itemstring": "张三"
            },
            {
                "item": "性别",
                "itemcoord": {
                    "x": 291,
                    "y": 100,
                    "width": 23,
                    "height": 27
                },
                "itemconf": 0.9999893307685852,
                "itemstring": "男"
            },
            {
                "item": "国籍",
                "itemcoord": {
                    "x": 388,
                    "y": 100,
                    "width": 44,
                    "height": 28
                },
                "itemconf": 0.9999999403953552,
                "itemstring": "中国"
            },
            {
                "item": "住址",
                "itemcoord": {
                    "x": 87,
                    "y": 126,
                    "width": 286,
                    "height": 30
                },
                "itemconf": 0.5020201206207275,
                "itemstring": "深圳市南山区万利达大厦"
            },
            {
                "item": "出生日期",
                "itemcoord": {
                    "x": 224,
                    "y": 195,
                    "width": 106,
                    "height": 25
                },
                "itemconf": 0.999338924884796,
                "itemstring": "1990-05-03"
            },
            {
                "item": "领证日期",
                "itemcoord": {
                    "x": 249,
                    "y": 226,
                    "width": 112,
                    "height": 26
                },
                "itemconf": 0.9999741315841676,
                "itemstring": "2014-12-25"
            },
            {
                "item": "准驾车型",
                "itemcoord": {
                    "x": 262,
                    "y": 261,
                    "width": 58,
                    "height": 27
                },
                "itemconf": 0.9999993443489076,
                "itemstring": "C1"
            },
            {
                "item": "起始日期",
                "itemcoord": {
                    "x": 122,
                    "y": 291,
                    "width": 111,
                    "height": 26
                },
                "itemconf": 0.9859412312507628,
                "itemstring": "2014-12-25"
            },
            {
                "item": "有效日期",
                "itemcoord": {
                    "x": 266,
                    "y": 294,
                    "width": 113,
                    "height": 27
                },
                "itemconf": 0.9921129941940308,
                "itemstring": "2020-12-25"
            },
            {
                "item": "红章",
                "itemcoord": {
                    "x": 52,
                    "y": 186,
                    "width": 110,
                    "height": 100
                },
                "itemconf": 0.9392985105514526,
                "itemstring": "深圳市公安局交通管理局"
            }
        ]
    }
}

```



## 错误码

| 错误码   | 含义                       |
| ----- | ------------------------ |
| 3     | 错误的请求；其中 message:account abnormal,errorno is:2为账号欠费停服                    |
| 4     | 签名为空                     |
| 5     | 签名串错误                    |
| 6     | 签名中的 APPID/Bucket 与操作目标不匹配 |
| 9     | 签名过期                     |
| 10    | APPID 不存在                 |
| 11    | SecretId 不存在              |
| 12    | APPID 和 SecretId 不匹配        |
| 13    | 重放攻击                     |
| 14    | 签名校验失败                   |
| 15    | 操作太频繁，触发频控               |
| 16    | Bucket 不存在                |
| 21    | 无效参数                     |
| 23    | 请求包体过大                   |
| 24    | 没有权限                     |
| 25    | 您购买的资源已用完                |
| 107   | 鉴权服务内部错误                 |
| 108   | 鉴权服务不可用                  |
| 213   | 内部错误                     |
| -1102 | 图片解码失败                   |
| -1300 | 图片为空                     |
| -1301 | 参数为空                     |
| -1304 | 参数过长                     |
| -1308 | 图片下载失败                   |
| -9001 | 请求 type 错误，不是0或1        |
| -9002 | 识别失败                     |
| -9006 | 预处理失败                    |
| -9005 | 图片无效                     |

更多其他 API 错误码请查看 [错误码说明](https://cloud.tencent.com/document/product/866/17733) 。 

 

 
