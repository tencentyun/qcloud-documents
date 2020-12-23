> !
> 1. 此文档仅适用于 RTMP 协议的推流请求。
> 2. 此文档不适用于 COS 其他 HTTP 请求。

## 推流请求

使用 RTMP 协议推流的请求组成规则为：

```plaintext
rtmp://[BucketName-APPID].[host]/live/[channel]?[params]
```

一个包含签名信息完整的请求如下：

```plaintext
rtmp://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/live/test-channel?q-sign-algorithm=sha1&q-ak=ak&q-sign-time=1606445586;1606545646&q-key-time=1606445586;1606545646&q-signature=signature
```

- **rtmp**：RTMP 协议名称，固定值。
- **examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com**：带有存储桶与 APPID 的域名，与 COS 其他 HTTP 请求类似。
- **live**：RTMP 协议中 app 名称，COS 使用固定值 live。
- **test-channel**：通道名，可以在创建通道时定义。
- **params**：推流参数，在“?”之后以“q-sign-algorithm=sha1&q-ak=ak... ...”形式排列，当前主要用于传递签名信息，下面会详细介绍签名参数的生成方法。

## 推流请求中的签名参数

推流请求的签名参数包括：

| 签名参数         | 具体描述                                                     |
| ---------------- | :----------------------------------------------------------- |
| q-sign-algorithm | 签名算法，当前固定为“sha1”                                   |
| q-ak             | SecretId，可登录 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面获取 |
| q-sign-time      | 签名有效时间对应的 Uninx 起始、结束时间戳，例如1557902800;1557910000 |
| q-key-time       | 同 q-sign-time                                                |
| 其他参数         | 其他参数待后续扩展，当前建议保持为空                         |
| q-signature      | 根据各签名要素计算出的签名值                                 |



## 推流请求签名的计算步骤

推流请求中 q-signature 签名值的计算规则如下：

```plaintext
Signaure=hmac-sha1(SecretKey , "sha1\n" + KeyTime + "\n" + sha1Hex(RtmpString) + "\n")
```

下面分步骤进行介绍。

### 步骤1：生成 KeyTime
1. 获取当前时间对应的 Unix 时间戳 StartTimestamp，Unix 时间戳是从 UTC（协调世界时，或 GMT 格林威治时间）1970年1月1日0时0分0秒（北京时间 1970年1月1日8时0分0秒）起至现在的总秒数。
2. 根据上述时间戳和期望的签名有效时长算出签名过期时间对应的 Unix 时间戳 EndTimestamp。
3. 拼接签名有效时间，格式为`StartTimestamp;EndTimestamp`，即为 KeyTime。例如：`1557902800;1557910000`。

### 步骤2：生成 RtmpString
根据请求里的资源信息、参数（当前保持为空）生成 RtmpString，格式为`CanonicalizedResource\nCanonicalizedParams\n`。

其中：
- CanonicalizedResource 为请求资源信息，在 RTMP 推流请求中，取`/[BucketName-APPID]/[channel]`。
- CanonicalizedParams 为请求参数信息，当前保持为空即可。
- `\n`为换行符。如果其中有字符串为空，前后的换行符需要保留，例如`/examplebucket-1250000000/test-channel\n\n`。


### 步骤3：生成 StringToSign

根据 KeyTime 与 RtmpString 生成 StringToSign，格式为`sha1\nKeyTime\nsha1Hex(RtmpString)\n`。
其中：

- sha1 为固定字符串。
- `\n`为换行符。
- SHA1(RtmpString) 为使用 sha1Hex 对 Rtmp 计算的消息摘要，16进制小写形式，例如：`54ecfe22f59d3514fdc764b87a32d8133ea611e6`。

### 步骤4：生成 Signature

使用 [HMAC-SHA1](#.E5.87.86.E5.A4.87.E5.B7.A5.E4.BD.9C) 以 SecretKey 密钥，以 [StringToSign](#stringtosign) 为消息，计算消息摘要，即为 Signature，例如：`01681b8c9d798a678e43b685a9f1bba0f6c0e012`。

### 步骤5：生成完整的签名参数

计算出 SecretId、KeyTime、Signature 后生成完整签名信息，格式为：

```plaintext
q-sign-algorithm=sha1
&q-ak=SecretId
&q-sign-time=KeyTime
&q-key-time=KeyTime
&q-signature=Signature
```

>!上述格式中的换行仅用于更好的阅读，实际格式并不包含换行。

将上述信息填入 RTMP 协议的请求参数中即可。有别于 HTTP，RTMP 没有头域的概念，因此只能通过请求参数传递签名信息。

## 代码示例

### 伪代码

```plaintext
KeyTime = [Now];[Expires]
RtmpString = [CanonicalizedResource]\n\n
StringToSign = sha1\nKeyTime\nSHA1(RtmpString)\n
Signature = HMAC-SHA1(SignKey, StringToSign)
```

### 消息摘要算法示例

不同语言如何调用 HMAC-SHA1 可以参考 [请求签名](https://cloud.tencent.com/document/product/436/7778) 中的代码示例章节。

## 实际案例

### 准备工作

1. 登录访问管理控制台的 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面获取其 APPID、SecretId 和 SecretKey，举例如下：

| APPID      | SecretId                             | SecretKey                        |
| ---------- | ------------------------------------ | -------------------------------- |
| 1250000000 | AKIDQjz3ltompVjBni5LitkWHFlFpwkn9U5q | BQYIM75p8x0iWVFSIgqEKwFprpRSVHlz |

2. 在对象存储控制台上创建存储桶，获取以下信息：

| 地域（Region）       | 存储桶名称        | channel 名称     |
| ------------ | --------------------- | ------------ |
| ap-guangzhou | examplebucket-1250000000 | test-channel |



### 签名过程中间变量

- **KeyTime** = `1606550430;1606554030`
- **CanonicalizedResource**=`/examplebucket-1250000000/test-channel`
- **RtmpString** = `/examplebucket-1250000000/test-channel\n\n`
- **StringToSign** = `sha1\n1606550430;1606554030\n44bb35a2713324b40406f7b4b457e33df378a346\n`<span id="stringtosign"></span>
- **Signature** = `d3b294bdf047228fca13291dea70a28e563ce4e2`

  

使用 ffmpeg 推送本地视频文件至 COS，请求如下：

```plaintext
ffmpeg -re -i /data/example.mp4 -vcodec h264 -acodec aac -f flv -y  "rtmp://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/live/test-channel?q-sign-algorithm=sha1&q-ak=AKIDQjz3ltompVjBni5LitkWHFlFpwkn9U5q&q-sign-time=1606550430;1606554030&q-key-time=1606550430;1606554030&q-signature=d3b294bdf047228fca13291dea70a28e563ce4e2"
```

> !因推流请求的签名信息中包含"&"与";"符号，请使用双引号（" "）将整个请求包括起来，避免没有转义而请求失败。
