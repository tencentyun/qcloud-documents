## 服务端API分类：
腾讯云点播的服务端API分为两类：
1. 一般服务端API：请求参数均为UTF-8字符，符合腾讯云通用的接口规范，可以使用腾讯云标准的服务端SDK；
2. 数据上传类API：请求内容包含二进制数据，无法使用腾讯云标准的服务端SDK，点播提供了专门服务端SDK来简化调用。

## 请求结构（一般服务端API）

### 服务域名
vod.api.qcloud.com。

### 通信协议
HTTPS。

### 请求方法
同时支持POST和GET请求，需要注意不能混合使用。即：
1. 如果使用GET方式，则参数均从QueryString传输；
2. 如果使用POST方式，则参数均从RequestBody中取得，QueryString中的参数将忽略；
3. 两种方式参数格式规则相同；
4. 一般情况下建议使用GET，当参数字符串过长时建议使用POST。

### 字符编码
均使用UTF-8编码。

### 服务端SDK
为简化调用方式，避免复杂的鉴权参数生成，建议开发者使用服务端SDK来发起调用。

## 请求结构（数据上传类API）

### 服务域名
vod2.qcloud.com

### 通信方法
HTTP/HTTPS。

### 请求方法
POST

### 服务端SDK
面向一般服务端API的SDK无法用于上传二进制数据。为此我们提供了专门的本地视频上传SDK。详见本地视频上传。

## 公共参数
公共参数是用于标识用户和接口鉴权目的的参数, 如非必要, 在每个接口单独的接口文档中不再对这些参数进行说明, 但每次请求均需要携带这些参数, 才能正常发起请求。

不论是一般服务端API还是数据上传类API，其公共参数均相同。

| 名称 | 类型 | 描述 | 必选 |
|---------|---------|---------|---------|
| Action | String | 接口指令的名称，例如: DescribeClass | 是 |
| Region | String | 区域参数，用来标识希望操作哪个区域的实例，备选值见下文，对于云点播，可以直接填gz | 是 |
| Timestamp | UInt | 当前UNIX时间戳 | 是 |
| Nonce | UInt | 随机正整数，与 Timestamp 联合起来, 用于防止重放攻击 | 是 |
| SecretId | String | 由腾讯云平台上申请的标识身份的 SecretId 和 SecretKey, 其中 SecretKey 会用来生成 Signature，具体参考[接口鉴权](/doc/api/257/接口鉴权 "接口鉴权")页面 | 是 |
| Signature | String | 请求签名，用来验证此次请求的合法性,具体参考[接口鉴权](/doc/api/257/接口鉴权 "接口鉴权")页面 | 是 |

腾讯云Region的可选值如下：

| Region | 区域 |
|---------|---------|
| bj | 北京 |
| gz | 广州 |
| sh | 上海 |
| hk | 中国香港 |
| ca | 北美 |

一个典型的接口请求如下, Action=DescribeVodPlayUrls，表示获取视频详细信息。

```
https://vod.api.qcloud.com/v2/interface.php?Action=DescribeVodPlayUrls
&SecretId=xxxxxxx
&Region=gz
&Timestamp=1402992826
&Nonce=345122
&Signature=mysignature
&fileId=1234567
```
其中fileId为API本身的指令参数，其余为公共参数。

## 接口应答
如无特别说明, 每次请求的返回值中, 都会包含下面的字段：

| 名称 | 类型 | 描述 |
|---------|---------|---------|---------|
| code | Int | 返回结果的错误码，0表示成功，其它值表示失败。具体错误码的含义可以参考错误码页面 |
| message | String | 请求结果 |

例如：对于如上所示的接口调用可能的返回结果如下：

```
{
    "code": 0,
    "message": "",
    "playSet": [
        {
            "url": "http://vcloud1200.tc.qq.com/1200_5b9688d481d8b811095d30a78cf44c4285026a4c.f0.mp4",
            "definition": 0,
            "vbitrate": 2332000,
            "vheight": 576,
            "vwidth": 1024
        }
    ]
}
```
