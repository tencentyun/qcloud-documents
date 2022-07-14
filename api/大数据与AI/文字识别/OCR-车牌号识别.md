
>!
- 车牌识别接口全面升级，算法更强、性能更优，支持子账号调用。欢迎立即体验 [新版车牌识别](https://cloud.tencent.com/document/product/866/36211)。
- 新老版本的接口计费模式相同，且共享计费阶梯和资源包，您可以在【文字识别控制台】>【[用量统计](https://console.cloud.tencent.com/ocr/stats)】中查看调用情况。
- 老版本接口我们仍继续维护，但不支持新客户开通调用，建议您使用 [新版车牌识别](https://cloud.tencent.com/document/product/866/36211)，体验更优服务。
## 接口描述
接口请求域名：`https://recognition.image.myqcloud.com/ocr/plate`
本接口（plate）用于识别用户上传照片的车牌号码。
>?本接口支持 HTTPS 协议，如果您现在使用的是 HTTP 协议，为了保障您的数据安全，请切换至 HTTPS。

## 请求头 header

| 参数名            |必选| 值                                        | 描述                                       |
| -------------- | -----|----------------------------------- | ---------------------------------------- |
| host           |  是   | recognition.image.myqcloud.com        | 腾讯云文字识别服务器域名。                       |
| content-length |  否   | 包体总长度                          | 每个请求的包体大小限制为6MB，不支持 .gif 类型的动图 | 
| content-type   | 是 |application/json 或者 multipart/form-data    | 1. 使用 application/json 格式，参数 url 或 image，其值为图片链接或图片 base64 编码；<br>2. 使用 multipart/form-data 格式，参数为 image，其值为图片的二进制内容。                               |
| authorization  | 是 |鉴权签名             | 用于鉴权的签名，使用 [多次有效签名](https://cloud.tencent.com/document/product/866/17734)。 |

## 输入参数

| 参数名   | 必选 | 类型     | 参数说明                                  |
| ----- | ---- | ------ | ------------------------------------- |
| appid | 是   | String | 接入项目的唯一标识，可在 [账号信息](https://console.cloud.tencent.com/developer) 或 [云 API 密钥](https://console.cloud.tencent.com/cam/capi) 中查看。                                  |
| image | 否   | Binary/String | 图片文件 或 图片 base64                    |
| url   | 否   | String | 图片 url 和 image 同时赋值时，则以 url 指定的图像作为输入 |

## 输出参数

| 字段         | 类型          | 说明                     |
| ---------- | ----------- | ---------------------- |
| code       | Int         | 返回码                    |
| message    | String      | 返回错误消息                 |
| data.items | Array(Item) | 识别出的所有字段信息，详见下文 Items 说明 |

Items 说明：
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
<td>字段识别结果置信度</td><tr>
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

## 示例
### 输入示例
#### 使用 application/json 
```
POST /ocr/plate HTTP/1.1
Authorization: FCHXdPTEwMDAwMzc5Jms9QUtJRGVRZDBrRU1yM2J4ZjhRckJi==
Host: recognition.image.myqcloud.com
Content-Length: 80
Content-Type: application/json

{
  "appid":"123456",
  "url":"http://test-123456.image.myqcloud.com/test.jpg"
}
```

#### 使用 multipart/form-data 
```
POST /ocr/plate HTTP/1.1
Authorization: FCHXdPTEwMDAwMzc5Jms9QUtJRGVRZDBrRU1yM2J4ZjhRckJi==
Host: recognition.image.myqcloud.com
Content-Length: 49
Content-Type: application/json

{
  "appid":"123456",
  "image":"SALDKHKAFLASD"
}
```

### 输出示例
```
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 242
Content-Type: text/json

{
"code":0,
"message":"OK",
"items":
    [
        {"item": "车牌", 
          "itemstring": "京NC32A1",
         "itemcoord":{"x" : 0, "y" : 1, "width" : 2, "height" : 3}, 
         "itemconf": 0.99
        },
    ]
} 
```

## 错误码

| 错误码   | 含义                         |
| ----- | -------------------------- |
| 3     | 错误的请求；其中 message:account abnormal,errorno is:2为账号欠费停服                      |
| 4     | 签名为空                       |
| 5     | 签名串错误                      |
| 6     | 签名中的 APPID/Bucket 与操作目标不匹配 |
| 9     | 签名过期                       |
| 10    |  APPID 不存在                  |
| 11    | SecretId 不存在               |
| 12    | APPID 和 SecretId 不匹配       |
| 13    | 重放攻击                       |
| 14    | 签名校验失败                     |
| 15    | 操作太频繁，触发频控                 |
| 21    | 无效参数                       |
| 23    | 请求包体过大                     |
| 24    | 没有权限                       |
| 25    | 您购买的资源已用完                  |
| 107   | 鉴权服务不可用                    |
| 108   | 鉴权服务不可用                    |
| 213   | 内部错误                       |
| -1102 | 图片解码失败                     |
| -1300 | 图片为空                       |
| -1301 | 参数为空                       |
| -1304 | 参数过长                       |
| -1308 | url 图片下载失败                 |
| -9702 | 车牌识别失败                   |
| -5208 | 服务器内部错误                 |


更多其他 API 错误码请查看 [错误码说明](https://cloud.tencent.com/document/product/866/17733) 。   


