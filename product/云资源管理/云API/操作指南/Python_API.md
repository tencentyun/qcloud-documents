
腾讯云 API 全新升级3.0 ，该版本进行了性能优化且全地域部署、支持就近和按地域接入、访问时延下降显著，接口描述更加详细、错误码描述更加全面、SDK 增加接口级注释，让您更加方便快捷的使用腾讯云产品。这里针对 Python API 调用方式进行简单说明。
现已支持云服务器（CVM）、云硬盘（CBS） 、私有网络（VPC）、云数据库（TencentDB）等 [腾讯云产品](https://cloud.tencent.com/product)，后续会支持其他的云产品接入，敬请期待。 


## 了解请求结构

### 1. 服务地址（endpoint）

API 支持就近地域接入（例如：cvm 产品域名为 `cvm.tencentcloudapi.com`），也支持指定地域域名访问（例如：广州地域的域名为 `cvm.ap-guangzhou.tencentcloudapi.com`），各地域参数见下文公共参数中的地域列表，详情请参见各产品的“请求结构”文档说明判断是否支持该地域。



<dx-alert infotype="notice" title="">
对时延敏感的业务，建议指定带地域的域名。
</dx-alert>



### 2. 通信协议

 腾讯云 API 的所有接口均通过 HTTPS 进行通信，提供高安全性的通信通道。 

### 3. 请求方法

支持的 HTTP 请求方法：

- POST（推荐）
- GET

POST 请求支持的 Content-Type 类型：
- application/json（推荐），必须使用签名方法 v3（TC3-HMAC-SHA256）。
- application/x-www-form-urlencoded，必须使用签名方法 v1（HmacSHA1 或 HmacSHA256）。
- multipart/form-data（仅部分接口支持），必须使用签名方法 v3（TC3-HMAC-SHA256）。

GET 请求的请求包大小不得超过32KB。POST 请求使用签名方法 v1（HmacSHA1、HmacSHA256）时不得超过1MB。POST 请求使用签名方法 v3（TC3-HMAC-SHA256）时支持10MB。

### 4. 字符编码

均使用 <kbd>UTF-8</kbd> 编码。




## 公共参数

<dx-alert infotype="explain" title="">
公共参数是用于标识用户和接口签名的参数，每次请求均需要携带这些参数，才能正常发起请求。 
</dx-alert>



### 签名方法 V3 公共参数

签名方法 v3 （有时也称作 TC3-HMAC-SHA256）相比签名方法 v1 （有些文档可能会简称“签名方法”），更安全，支持更大的请求包，支持 POST JSON 格式，性能有一定提升，推荐使用该签名方法计算签名。使用方法见下文 “签名方法介绍”。 

| 参数名称       | 类型    | 必选 | 描述                                                         |
| :------------- | :------ | :--- | :----------------------------------------------------------- |
| X-TC-Action    | String  | 是   | 操作的接口名称。取值参考接口文档中输入参数公共参数 Action 的说明。例如云服务器的查询实例列表接口，取值为 DescribeInstances。 |
| X-TC-Region    | String  | -    | 地域参数，用来标识希望操作哪个地域的数据。接口接受的地域取值参考接口文档中输入参数公共参数 Region 的说明。**注意：某些接口不需要传递该参数，接口文档中会对此特别说明，此时即使传递该参数也不会生效。** |
| X-TC-Timestamp | Integer | 是   | 当前 UNIX 时间戳，可记录发起 API 请求的时间。例如 1529223702。**注意：如果与服务器时间相差超过5分钟，会引起签名过期错误。** |
| X-TC-Version   | String  | 是   | 操作的 API 的版本。取值参考接口文档中入参公共参数 Version 的说明。例如云服务器的版本 2017-03-12。 |
| Authorization  | String  | 是   | HTTP 标准身份认证头部字段，例如： TC3-HMAC-SHA256 Credential=AKIDEXAMPLE/Date/service/tc3_request, SignedHeaders=content-type;host, Signature=72e494ea8******************************************a96525168 <br>其中：<li>TC3-HMAC-SHA256：签名方法，目前固定取该值。</li><li> Credential：签名凭证，AKIDEXAMPLE 是 SecretId。</li><li>Date 是 UTC 标准时间的日期，取值需要和公共参数 X-TC-Timestamp 换算的 UTC 标准时间日期一致。</li><li>service 为产品名，通常为域名前缀，例如域名 cvm.tencentcloudapi.com 意味着产品名是 cvm。本产品取值为 cvm。</li><li>SignedHeaders：参与签名计算的头部信息，content-type 和 host 为必选头部。</li><li>Signature：签名摘要，计算过程详见下文。</li> |
| X-TC-Token     | String  | 否   | 临时证书所用的 Token ，需要结合临时密钥一起使用。临时密钥和 Token 需要到访问管理服务调用接口获取。长期密钥不需要 Token。 |

### 签名方法 V1 公共参数

使用签名方法 v1 （有时会称作 HmacSHA256 和 HmacSHA1），公共参数需要统一放到请求串中。

| 参数名称        | 类型    | 必选 | 描述                                                         |
| :-------------- | :------ | :--- | :----------------------------------------------------------- |
| Action          | String  | 是   | 操作的接口名称。取值参考接口文档中输入参数公共参数 Action 的说明。例如云服务器的查询实例列表接口，取值为 DescribeInstances。 |
| Region          | String  | -    | 地域参数，用来标识希望操作哪个地域的数据。接口接受的地域取值参考接口文档中输入参数公共参数 Region 的说明。**注意：某些接口不需要传递该参数，接口文档中会对此特别说明，此时即使传递该参数也不会生效。** |
| Timestamp       | Integer | 是   | 当前 UNIX 时间戳，可记录发起 API 请求的时间。例如1529223702，如果与当前时间相差过大，会引起签名过期错误。 |
| Nonce           | Integer | 是   | 随机正整数，与 Timestamp 联合起来，用于防止重放攻击。        |
| SecretId        | String  | 是   | 在 [云API密钥](https://console.cloud.tencent.com/capi) 上申请的标识身份的 SecretId，一个 SecretId 对应唯一的 SecretKey，而 SecretKey 会用来生成请求签名 Signature。 |
| Signature       | String  | 是   | 请求签名，用来验证此次请求的合法性，需要用户根据实际的输入参数计算得出。具体计算方法参见下文“签名方法介绍”。 |
| Version         | String  | 是   | 操作的 API 的版本。取值参考接口文档中入参公共参数 Version 的说明。例如云服务器的版本 2017-03-12。 |
| SignatureMethod | String  | 否   | 签名方式，目前支持 HmacSHA256 和 HmacSHA1。只有指定此参数为 HmacSHA256 时，才使用 HmacSHA256 算法验证签名，其他情况均使用 HmacSHA1 验证签名。 |
| Token           | String  | 否   | 临时证书所用的 Token ，需要结合临时密钥一起使用。临时密钥和 Token 需要到访问管理服务调用接口获取。长期密钥不需要 Token 。 |

### 地域列表

由于各个产品支持地域不同，具体详情请参考各产品文档中的地域列表。
例如，您可以参考云服务器的 [地域列表](https://cloud.tencent.com/document/product/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。



## Python API 调用方式

 腾讯云 API 会对每个请求进行身份验证，用户需要使用安全凭证，经过特定的步骤对请求进行签名（Signature），每个请求都需要在公共请求参数中指定该签名结果并以指定的方式和格式发送请求。


假设用户的 SecretId 和 SecretKey 分别是：`AKIDz8krbsJ5**********mLPx3EXAMPLE` 和 `Gu5t9xGAR***********EXAMPLE`。用户想查看广州区云服务器名为 “未命名” 的主机状态，只返回一条数据。则请求可能为： 
```
curl -X POST https://cvm.tencentcloudapi.com \
-H "Authorization: TC3-HMAC-SHA256 Credential=AKIDz8krbsJ5**********mLPx3EXAMPLE/2019-02-25/cvm/tc3_request, SignedHeaders=content-type;host, Signature=72e494ea809ad7a8c8f7a4507b9bddcbaa8e581f516e8da2f66e2c5a96525168" \
-H "Content-Type: application/json; charset=utf-8" \
-H "Host: cvm.tencentcloudapi.com" \
-H "X-TC-Action: DescribeInstances" \
-H "X-TC-Timestamp: 1551113065" \
-H "X-TC-Version: 2017-03-12" \
-H "X-TC-Region: ap-guangzhou" \
-d '{"Limit": 1, "Filters": [{"Values": ["\u672a\u547d\u540d"], "Name": "instance-name"}]}'
```

### 步骤1：申请安全凭证

本文使用的安全凭证为密钥，密钥包括 SecretId 和 SecretKey。每个用户最多可以拥有两对密钥。

- SecretId：用于标识 API 调用者身份，可以简单类比为用户名。
- SecretKey：用于验证 API 调用者的身份，可以简单类比为密码。



<dx-alert infotype="notice" title="">
**用户必须严格保管安全凭证，避免泄露，否则将危及财产安全。如已泄漏，请立刻禁用该安全凭证。**
</dx-alert>



前往 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面，即可进行获取。如下图所示：
![](https://main.qcloudimg.com/raw/665e5334b0d5db156ef48a19072ba8bd.png)

### 步骤2
### 1. 获取 API 3.0 V3 版本签名
签名方法 v3 （TC3-HMAC-SHA256）功能上覆盖了以前的签名方法 v1，而且更安全，支持更大的请求，支持 json 格式，性能有一定提升，推荐使用该签名方法计算签名。如下图所示：


<dx-alert infotype="explain" title="">
首次接触，建议使用 [API Explorer](https://console.cloud.tencent.com/api/explorer) 中的“签名串生成”功能，选择签名版本为 “API 3.0 签名 v3”，可以生成签名过程进行验证，也可直接生成 SDK 代码。推荐使用腾讯云 API 配套的7种常见的编程语言 SDK，已经封装了签名和请求过程，均已开源，支持 [Python](https://github.com/TencentCloud/tencentcloud-sdk-python)、[Java](https://github.com/TencentCloud/tencentcloud-sdk-java)、[PHP](https://github.com/TencentCloud/tencentcloud-sdk-php)、[Go](https://github.com/TencentCloud/tencentcloud-sdk-go)、[NodeJS](https://github.com/TencentCloud/tencentcloud-sdk-nodejs)、[.NET](https://github.com/TencentCloud/tencentcloud-sdk-dotnet)、[C++](https://github.com/TencentCloud/tencentcloud-sdk-cpp)。
</dx-alert>

![](https://main.qcloudimg.com/raw/f35b61c6b76765f4aae33e9b99673984.png)


云 API 支持 GET 和 POST 请求。对于 GET 方法，只支持 Content-Type: application/x-www-form-urlencoded 协议格式。对于 POST 方法，目前支持 Content-Type: application/json 以及 Content-Type: multipart/form-data 两种协议格式，json 格式绝大多数接口均支持，multipart 格式只有特定接口支持，此时该接口不能使用 json 格式调用，参考具体业务接口文档说明。推荐使用 POST 请求，因为两者的结果并无差异，但 GET 请求只支持32KB以内的请求包。

下面以 [查看实例列表](https://cloud.tencent.com/document/product/213/15728) 接口为例，分步骤介绍签名的计算过程。我们选择该接口原因是：
1. 云服务器默认已开通，该接口很常用。
2. 该接口是只读的，不会改变现有资源的状态。
3. 接口覆盖的参数种类较全，可以演示包含数据结构的数组如何使用。

#### 1. 拼接规范请求串

```
CanonicalRequest =
    HTTPRequestMethod + '\n' +
    CanonicalURI + '\n' +
    CanonicalQueryString + '\n' +
    CanonicalHeaders + '\n' +
    SignedHeaders + '\n' +
    HashedRequestPayload
```

| 字段名称             | 解释                                                         |
| :------------------- | :----------------------------------------------------------- |
| HTTPRequestMethod    | HTTP 请求方法（GET、POST ）。此示例取值为 `POST`。           |
| CanonicalURI         | URI 参数，API 3.0 固定为正斜杠（/）。                        |
| CanonicalQueryString | 发起 HTTP 请求 URL 中的查询字符串，对于 POST 请求，固定为空字符串""，对于 GET 请求，则为 URL 中问号（?）后面的字符串内容，例如：Limit=10&Offset=0。 注意：CanonicalQueryString 需要参考 [RFC3986](https://tools.ietf.org/html/rfc3986) 进行 URLEncode，字符集 UTF8，推荐使用编程语言标准库，所有特殊字符均需编码，大写形式。 |
| CanonicalHeaders     | 参与签名的头部信息，至少包含 host 和 content-type 两个头部，也可加入自定义的头部参与签名以提高自身请求的唯一性和安全性。 拼接规则：头部 key 和 value 统一转成小写，并去掉首尾空格，按照 key:value\n 格式拼接；多个头部，按照头部 key（小写）的 ASCII 升序进行拼接。此示例计算结果是 `content-type:application/json; charset=utf-8\nhost:cvm.tencentcloudapi.com\n`。 注意：content-type 必须和实际发送的相符合，有些编程语言网络库即使未指定也会自动添加 charset 值，如果签名时和发送时不一致，服务器会返回签名校验失败。 |
| SignedHeaders        | 参与签名的头部信息，说明此次请求有哪些头部参与了签名，和 CanonicalHeaders 包含的头部内容是一一对应的。content-type 和 host 为必选头部。 拼接规则：头部 key 统一转成小写；多个头部 key（小写）按照 ASCII 升序进行拼接，并且以分号（;）分隔。此示例为 content-type;host |
| HashedRequestPayload | 请求正文（Requestpayload，即 body，此示例为 `{"Limit": 1, "Filters": [{"Values": ["\u672a\u547d\u540d"], "Name": "instance-name"}]}`）的哈希值，计算伪代码为 Lowercase(HexEncode(Hash.SHA256(RequestPayload)))，即对 HTTP 请求正文做 SHA256 哈希，然后十六进制编码，最后编码串转换成小写字母。对于 GET 请求，RequestPayload 固定为空字符串。此示例计算结果是 `35e9c5b0e3ae67532d3c9f17ead6c90222632e5b1ff7f6e89887f1398934f064`。 |

根据以上规则，示例中得到的规范请求串如下： 
```
POST
/

content-type:application/json; charset=utf-8
host:cvm.tencentcloudapi.com

content-type;host
35e9c5b0e3ae67532d3c9f17ead6c90222632e5b1ff7f6e89887f1398934f064
```

#### 2. 拼接待签名字符串

按如下格式拼接待签名字符串：
```
StringToSign =
    Algorithm + \n +
    RequestTimestamp + \n +
    CredentialScope + \n +
    HashedCanonicalRequest
```

| 字段名称               | 解释                                                         |
| :--------------------- | :----------------------------------------------------------- |
| Algorithm              | 签名算法，目前固定为 `TC3-HMAC-SHA256`。                     |
| RequestTimestamp       | 请求时间戳，即请求头部的公共参数 X-TC-Timestamp 取值，取当前时间 UNIX 时间戳，精确到秒。此示例取值为 `1551113065`。 |
| CredentialScope        | 凭证范围，格式为 Date/service/tc3_request，包含日期、所请求的服务和终止字符串（tc3_request）。**Date 为 UTC 标准时间的日期，取值需要和公共参数 X-TC-Timestamp 换算的 UTC 标准时间日期一致**；service 为产品名，必须与调用的产品域名一致。此示例计算结果是 2019-02-25/cvm/tc3_request。 |
| HashedCanonicalRequest | 前述步骤拼接所得规范请求串的哈希值，计算伪代码为 Lowercase(HexEncode(Hash.SHA256(CanonicalRequest)))。此示例计算结果是 `5ffe6a04c0664d6b969fab9a13bdab201d63ee709638e2749d62a09ca18d7031`。 |



<dx-alert infotype="notice" title="">
- Date 必须从时间戳 X-TC-Timestamp 计算得到，且时区为 UTC+0。如果加入系统本地时区信息，例如东八区，将导致白天和晚上调用成功，但是凌晨时调用必定失败。假设时间戳为 1551113065，在东八区的时间是 2019-02-26 00:44:25，但是计算得到的 Date 取 UTC+0 的日期应为 2019-02-25，而不是 2019-02-26。
- Timestamp 必须是当前系统时间，且需确保系统时间和标准时间是同步的，如果相差超过五分钟则必定失败。如果长时间不和标准时间同步，可能导致运行一段时间后，请求必定失败，返回签名过期错误。
</dx-alert>
 

 根据以上规则，示例中得到的待签名字符串如下： 

```
TC3-HMAC-SHA256
1551113065
2019-02-25/cvm/tc3_request
5ffe6a04c0664d6b969fab9a13bdab201d63ee709638e2749d62a09ca18d7031
```

#### 3. 计算签名(伪代码)

```
SecretKey = "Gu5t9xGARN**********QYCN3EXAMPLE"
SecretDate = HMAC_SHA256("TC3" + SecretKey, Date)
SecretService = HMAC_SHA256(SecretDate, Service)
SecretSigning = HMAC_SHA256(SecretService, "tc3_request")
```

| 字段名称  | 解释                                                         |
| :-------- | :----------------------------------------------------------- |
| SecretKey | 原始的 SecretKey，即 `Gu5t9xGARN**********QYCN3EXAMPLE`。    |
| Date      | 即 Credential 中的 Date 字段信息。此示例取值为 `2019-02-25`。 |
| Service   | 即 Credential 中的 Service 字段信息。此示例取值为 `cvm`。    |

签名结果如下：

```
Signature = HexEncode(HMAC_SHA256(SecretSigning, StringToSign))
```

 此示例计算结果是 `72e494ea8*******************************c5a96525168`。 

#### 4. 获取调用信息

 按如下格式拼接 Authorization： 

```python
Authorization =
    Algorithm + ' ' +
    'Credential=' + SecretId + '/' + CredentialScope + ', ' +
    'SignedHeaders=' + SignedHeaders + ', ' +
    'Signature=' + Signature
```

| 字段名称        | 解释                                                         |
| :-------------- | :----------------------------------------------------------- |
| Algorithm       | 签名方法，固定为 `TC3-HMAC-SHA256`。                         |
| SecretId        | 密钥对中的 SecretId，即 `AKIDz8krbsJ5yK**********mLPx3EXAMPLE`。 |
| CredentialScope | 见上文，凭证范围。此示例计算结果是 `2019-02-25/cvm/tc3_request`。 |
| SignedHeaders   | 见上文，参与签名的头部信息。此示例取值为 `content-type;host`。 |
| Signature       | 签名值。此示例计算结果是 `72e494ea809ad7a8c8f7a450***************f516e8da2f66e2c5a96525168`。 |

 根据以上规则，示例中得到的值为： 

```
TC3-HMAC-SHA256 Credential=AKIDz8krbsJ5yK**********mLPx3EXAMPLE/2019-02-25/cvm/tc3_request, SignedHeaders=content-type;host, Signature=72e494ea809ad7a8c8f7a450***************f516e8da2f66e2c5a96525168
```

 最终完整的调用信息如下： 

```
POST https://cvm.tencentcloudapi.com/
Authorization: TC3-HMAC-SHA256 Credential=AKIDz8krbsJ5yK**********mLPx3EXAMPLE/2019-02-25/cvm/tc3_request, SignedHeaders=content-type;host, Signature=72e494ea809ad7a8c8f7a450***************f516e8da2f66e2c5a96525168
Content-Type: application/json; charset=utf-8
Host: cvm.tencentcloudapi.com
X-TC-Action: DescribeInstances
X-TC-Version: 2017-03-12
X-TC-Timestamp: 1551113065
X-TC-Region: ap-guangzhou

{"Limit": 1, "Filters": [{"Values": ["\u672a\u547d\u540d"], "Name": "instance-name"}]}
```

#### 5. API 3.0 签名 V3 示例

```python
# -*- coding: utf-8 -*-
import hashlib, hmac, json, os, sys, time
from datetime import datetime

# 密钥参数
secret_id = "`AKIDz8krbsJ5yK**********mLPx3EXAMPLE`"
secret_key = "`Gu5t9xGARN**********QYCN3EXAMPLE`"

service = "cvm"
host = "cvm.tencentcloudapi.com"
endpoint = "https://" + host
region = "ap-guangzhou"
action = "DescribeInstances"
version = "2017-03-12"
algorithm = "TC3-HMAC-SHA256"
#timestamp = int(time.time())
timestamp = 1551113065
date = datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d")
params = {"Limit": 1, "Filters": [{"Name": "instance-name", "Values": [u"未命名"]}]}

# ************* 步骤 1：拼接规范请求串 *************
http_request_method = "POST"
canonical_uri = "/"
canonical_querystring = ""
ct = "application/json; charset=utf-8"
payload = json.dumps(params)
canonical_headers = "content-type:%s\nhost:%s\n" % (ct, host)
signed_headers = "content-type;host"
hashed_request_payload = hashlib.sha256(payload.encode("utf-8")).hexdigest()
canonical_request = (http_request_method + "\n" +
                     canonical_uri + "\n" +
                     canonical_querystring + "\n" +
                     canonical_headers + "\n" +
                     signed_headers + "\n" +
                     hashed_request_payload)
print(canonical_request)

# ************* 步骤 2：拼接待签名字符串 *************
credential_scope = date + "/" + service + "/" + "tc3_request"
hashed_canonical_request = hashlib.sha256(canonical_request.encode("utf-8")).hexdigest()
string_to_sign = (algorithm + "\n" +
                  str(timestamp) + "\n" +
                  credential_scope + "\n" +
                  hashed_canonical_request)
print(string_to_sign)

# ************* 步骤 3：计算签名 *************
# 计算签名摘要函数
def sign(key, msg):
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()
secret_date = sign(("TC3" + secret_key).encode("utf-8"), date)
secret_service = sign(secret_date, service)
secret_signing = sign(secret_service, "tc3_request")
signature = hmac.new(secret_signing, string_to_sign.encode("utf-8"), hashlib.sha256).hexdigest()
print(signature)

# ************* 步骤 4：拼接 Authorization *************
authorization = (algorithm + " " +
                 "Credential=" + secret_id + "/" + credential_scope + ", " +
                 "SignedHeaders=" + signed_headers + ", " +
                 "Signature=" + signature)
print(authorization)

print('curl -X POST ' + endpoint
      + ' -H "Authorization: ' + authorization + '"'
      + ' -H "Content-Type: application/json; charset=utf-8"'
      + ' -H "Host: ' + host + '"'
      + ' -H "X-TC-Action: ' + action + '"'
      + ' -H "X-TC-Timestamp: ' + str(timestamp) + '"'
      + ' -H "X-TC-Version: ' + version + '"'
      + ' -H "X-TC-Region: ' + region + '"'
      + " -d '" + payload + "'")
```



### 2. 获取 API 3.0  V1 版本签名


签名方法 v1（HmacSHA1、HmacSHA256）简单易用，但是功能和安全性都不如签名方法 v3，推荐使用签名方法 v3。

首次接触，建议使用 [API Explorer](https://console.cloud.tencent.com/api/explorer) 中的“签名串生成”功能，选择签名版本为“API 3.0 签名 v1”，可以生成签名过程进行验证，并提供了部分编程语言的签名示例，也可直接生成 SDK 代码。推荐使用腾讯云 API 配套的 7 种常见的编程语言 SDK，已经封装了签名和请求过程，均已开源，支持 [Python](https://github.com/TencentCloud/tencentcloud-sdk-python)、[Java](https://github.com/TencentCloud/tencentcloud-sdk-java)、[PHP](https://github.com/TencentCloud/tencentcloud-sdk-php)、[Go](https://github.com/TencentCloud/tencentcloud-sdk-go)、[NodeJS](https://github.com/TencentCloud/tencentcloud-sdk-nodejs)、[.NET](https://github.com/TencentCloud/tencentcloud-sdk-dotnet)、[C++](https://github.com/TencentCloud/tencentcloud-sdk-cpp)。

以云服务器查看实例列表(DescribeInstances)请求为例，当用户调用这一接口时，其请求参数可能如下:

| 参数名称      | 中文            | 参数值                               |
| :------------ | :-------------- | :----------------------------------- |
| Action        | 方法名          | DescribeInstances                    |
| SecretId      | 密钥 ID         | `AKIDz8krbsJ5**********mLPx3EXAMPLE` |
| Timestamp     | 当前时间戳      | 1465185768                           |
| Nonce         | 随机正整数      | 11886                                |
| Region        | 实例所在区域    | ap-guangzhou                         |
| InstanceIds.0 | 待查询的实例 ID | ins-09dx96dg                         |
| Offset        | 偏移量          | 0                                    |
| Limit         | 最大允许输出    | 20                                   |
| Version       | 接口版本号      | 2017-03-12                           |

#### 1. 对参数排序

首先对所有请求参数按参数名的字典序（ ASCII 码）升序排序。

<dx-alert infotype="notice" title="">
- 只按参数名进行排序，参数值保持对应即可，不参与比大小。 
- 按 ASCII 码比大小，如 InstanceIds.2 要排在 InstanceIds.12 后面，不是按字母表，也不是按数值。用户可以借助编程语言中的相关排序函数来实现这一功能，如 PHP 中的 ksort 函数。
</dx-alert>


上述示例参数的排序结果如下：

```
{
    'Action' : 'DescribeInstances',
    'InstanceIds.0' : 'ins-09dx96dg',
    'Limit' : 20,
    'Nonce' : 11886,  
    'Offset' : 0,
    'Region' : 'ap-guangzhou',
    'SecretId' : 'AKIDz8krbsJ5**********mLPx3EXAMPLE',
    'Timestamp' : 1465185768,
    'Version': '2017-03-12',
}
```

 使用程序设计语言开发时，可对上面示例中的参数进行排序，得到的结果一致即可。 

#### 2. 拼接规范请求串

此步骤生成请求字符串。 将把上一步排序好的请求参数格式化成“参数名称=参数值”的形式，如对 Action 参数，其参数名称为 "Action" ，参数值为 "DescribeInstances" ，因此格式化后就为 Action=DescribeInstances。


<dx-alert infotype="notice" title="">
“参数值”为原始值而非 url 编码后的值。
</dx-alert>


然后将格式化后的各个参数用"&"拼接在一起，最终生成的请求字符串为:

```
Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Limit=20&Nonce=11886&Offset=0&Region=ap-guangzhou&SecretId=AKIDz8krbsJ5**********mLPx3EXAMPLE&Timestamp=1465185768&Version=2017-03-12
```

#### 3. 拼接待签名字符串

此步骤生成签名原文字符串。 签名原文字符串由以下几个参数构成：

1. 请求方法: 支持 POST 和 GET 方式，这里使用 GET 请求，注意方法为全大写。
2. 请求主机:查看实例列表(DescribeInstances)的请求域名为：cvm.tencentcloudapi.com。实际的请求域名根据接口所属模块的不同而不同，详见各接口说明。
3. 请求路径: 当前版本云API的请求路径固定为 / 。
4. 请求字符串: 即上一步生成的请求字符串。

签名原文串的拼接规则为：`请求方法 + 请求主机 +请求路径 + ? + 请求字符串` 。

示例的拼接结果为：

```
GETcvm.tencentcloudapi.com/?Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Limit=20&Nonce=11886&Offset=0&Region=ap-guangzhou&SecretId=AKIDz8krbsJ5**********mLPx3EXAMPLE&Timestamp=1465185768&Version=2017-03-12
```

#### 4. 计算签名（伪代码）

 此步骤生成签名串。 首先使用 HMAC-SHA1 算法对上一步中获得的**签名原文字符串**进行签名，然后将生成的签名串使用 Base64 进行编码，即可获得最终的签名串。 
 
```python
secret_key = "Gu5t9xGAR********QYCN3EXAMPLE"
s = "GETcvm.tencentcloudapi.com/?Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Limit=20&Nonce=11886&Offset=0&Region=ap-guangzhou&SecretId=AKIDz8krbsJ5yK**********mLPx3EXAMPLE&Timestamp=1465185768&Version=2017-03-12"
hmac_str = hmac.new(secret_key.encode("utf8"), s.encode("utf8"),hashlib.sha1).digest()
# 最终签名串
Signature = base64.b64encode(hmac_str)
```

 #### 5. 获取调用信息并发送请求

```python
data["Signature"] = base64.b64encode(hmac_str)
print(data["Signature"])  # 最终签名串
# 此处会实际调用，成功后可能产生计费
resp = requests.get("https://" + endpoint, params=data)
print(resp.url)
```


| 字段名称 | 解释                                                         |
| :------- | ------------------------------------------------------------ |
| endpoint | 服务地址， 例如：`cvm.tencentcloudapi.com`                   |
| data     | API 3.0 签名 V1 所举示例接口参数，**注意** 这里需要将计算的签名已键值对的形式加入 data 中 |

<dx-alert infotype="notice" title="">
由于示例中的密钥是虚构的，时间戳也不是系统当前时间，因此如果将此 url 在浏览器中打开或者用 curl 等命令调用时会返回鉴权错误：签名过期。为了得到一个可以正常返回的 url ，需要修改示例中的 SecretId 和 SecretKey 为真实的密钥，并使用系统当前时间戳作为 Timestamp 。 
</dx-alert>


为了更清楚的解释签名过程，下面以 Python 语言为例，将上述的签名过程具体实现。请求的域名、调用的接口和参数的取值都以上述签名过程为准，代码只为解释签名过程，并不具备通用性，实际开发请尽量使用 SDK 。

#### 6. 签名串编码

生成的签名串并不能直接作为请求参数，需要对其进行 URL 编码。

如上一步生成的签名串为 `Eli*****************cGeI=`，最终得到的签名串请求参数（Signature）为：`EliP***********************eI%3D`，它将用于生成最终的请求 URL。


<dx-alert infotype="notice" title="">
 - 如果用户的请求方法是 GET，或者请求方法为 POST 同时 Content-Type 为 application/x-www-form-urlencoded，则发送请求时所有请求参数的值均需要做 URL 编码，参数键和=符号不需要编码。非 ASCII 字符在 URL 编码前需要先以 UTF-8 进行编码。
 - 有些编程语言的网络库会自动为所有参数进行 urlencode，在这种情况下，就不需要对签名串进行 URL 编码了，否则两次 URL 编码会导致签名失败。
 - 其他参数值也需要进行编码，编码采用 [RFC 3986](http://tools.ietf.org/html/rfc3986)。使用 %XY 对特殊字符例如汉字进行百分比编码，其中“X”和“Y”为十六进制字符（0-9 和大写字母 A-F），使用小写将引发错误。
</dx-alert>





#### 7. API 3.0 签名 V1示例

<dx-alert infotype="notice" title="">
如果是在 Python 2环境中运行，需要先安装 requests 依赖包：`pip install requests`。 
</dx-alert>


```python
# -*- coding: utf8 -*-
import base64
import hashlib
import hmac
import time

import requests

secret_id = "AKIDz8k*********LPx3EXAMPLE"
secret_key = "Gu5t9xGA*********YCN3EXAMPLE"

def get_string_to_sign(method, endpoint, params):
    s = method + endpoint + "/?"
    query_str = "&".join("%s=%s" % (k, params[k]) for k in sorted(params))
    return s + query_str

def sign_str(key, s, method):
    hmac_str = hmac.new(key.encode("utf8"), s.encode("utf8"), method).digest()
    return base64.b64encode(hmac_str)

if __name__ == '__main__':
    endpoint = "cvm.tencentcloudapi.com"
    data = {
        'Action' : 'DescribeInstances',
        'InstanceIds.0' : 'ins-09dx96dg',
        'Limit' : 20,
        'Nonce' : 11886,
        'Offset' : 0,
        'Region' : 'ap-guangzhou',
        'SecretId' : secret_id,
        'Timestamp' : 1465185768, # int(time.time())
        'Version': '2017-03-12'
    }
    s = get_string_to_sign("GET", endpoint, data)
    data["Signature"] = sign_str(secret_key, s, hashlib.sha1)
    print(data["Signature"])
    # 此处会实际调用，成功后可能产生计费
    # resp = requests.get("https://" + endpoint, params=data)
    # print(resp.url)
```



## API 2.0 签名

此签名现已不在维护，建议使用性能更优的 **API 3.0 签名**，如需使用，请直接在 [API Explorer](https://console.cloud.tencent.com/api/explorer) 的**签名串生成>选择 API 2.0 签名版本**进行操作。


## 签名失败

存在以下签名失败的错误码，请根据实际情况处理。

| 错误码                       | 错误描述                                                     |
| :--------------------------- | :----------------------------------------------------------- |
| AuthFailure.SignatureExpire  | 签名过期。Timestamp 与服务器接收到请求的时间相差不得超过五分钟。 |
| AuthFailure.SecretIdNotFound | 密钥不存在。请到控制台查看密钥是否被禁用，是否少复制了字符或者多了字符。 |
| AuthFailure.SignatureFailure | 签名错误。可能是签名计算错误，或者签名与实际发送的内容不相符合，也有可能是密钥 SecretKey 错误导致的。 |
| AuthFailure.TokenFailure     | 临时证书 Token 错误。                                        |
| AuthFailure.InvalidSecretId  | 密钥非法（不是云 API 密钥类型）。                            |

## 返回结果

### 正确返回结果

以云服务器的接口查看实例状态列表 (DescribeInstancesStatus) 2017-03-12 版本为例，若调用成功，其可能的返回如下为：

```json
{
    "Response": {``
        "TotalCount": 0,
        "InstanceStatusSet": [],
        "RequestId": "b5b41468-520d-4192-b42f-595cc34b6c1c"
    }
}
```

* `Response` 及其内部的 `RequestId` 是固定的字段，无论请求成功与否，只要 API 处理了，则必定会返回。
* `RequestId` 用于一个 API 请求的唯一标识，如果 API 出现异常，可以联系我们，并提供该 ID 来解决问题。
* 除了固定的字段外，其余均为具体接口定义的字段，不同的接口所返回的字段参见接口文档中的定义。此例中的 `TotalCount` 和 `InstanceStatusSet` 均为 DescribeInstancesStatus 接口定义的字段，由于调用请求的用户暂时还没有云服务器实例，因此 `TotalCount` 在此情况下的返回值为 0， `InstanceStatusSet` 列表为空。

### 错误返回结果

 若调用失败，其返回值示例如下为： 

```json
{
    "Response": {
        "Error": {
            "Code": "AuthFailure.SignatureFailure",
            "Message": "The provided credentials could not be validated. Please check your signature is correct."
        },
        "RequestId": "ed93f3cb-f35e-473f-b9f3-0d451b8b79c6"
    }
}
```

* `Error` 的出现代表着该请求调用失败。`Error` 字段连同其内部的 `Code` 和 `Message` 字段在调用失败时是必定返回的。
* `Code` 表示具体出错的错误码，当请求出错时可以先根据该错误码在公共错误码和当前接口对应的错误码列表里面查找对应原因和解决方案。
* `Message` 显示出了这个错误发生的具体原因，随着业务发展或体验优化，此文本可能会经常保持变更或更新，用户不应依赖这个返回值。
* `RequestId` 用于一个 API 请求的唯一标识，如果 API 出现异常，可以联系我们，并提供该 ID 来解决问题。

### 公共错误码

 返回结果中如果存在 Error 字段，则表示调用 API 接口失败。 Error 中的 Code 字段表示错误码，所有业务都可能出现的错误码为公共错误码，下表列出了公共错误码。 

| 错误码                            | 错误描述                                                    |
| :-------------------------------- | :---------------------------------------------------------- |
| AuthFailure.InvalidSecretId       | 密钥非法（不是云 API 密钥类型）。                           |
| AuthFailure.MFAFailure            | MFA 错误。                                                  |
| AuthFailure.SecretIdNotFound      | 密钥不存在。                                                |
| AuthFailure.SignatureExpire       | 签名过期。                                                  |
| AuthFailure.SignatureFailure      | 签名错误。                                                  |
| AuthFailure.TokenFailure          | token 错误。                                                |
| AuthFailure.UnauthorizedOperation | 请求未 CAM 授权。                                           |
| DryRunOperation                   | DryRun 操作，代表请求将会是成功的，只是多传了 DryRun 参数。 |
| FailedOperation                   | 操作失败。                                                  |
| InternalError                     | 内部错误。                                                  |
| InvalidAction                     | 接口不存在。                                                |
| InvalidParameter                  | 参数错误。                                                  |
| InvalidParameterValue             | 参数取值错误。                                              |
| LimitExceeded                     | 超过配额限制。                                              |
| MissingParameter                  | 缺少参数错误。                                              |
| NoSuchVersion                     | 接口版本不存在。                                            |
| RequestLimitExceeded              | 请求的次数超过了频率限制。                                  |
| ResourceInUse                     | 资源被占用。                                                |
| ResourceInsufficient              | 资源不足。                                                  |
| ResourceNotFound                  | 资源不存在。                                                |
| ResourceUnavailable               | 资源不可用。                                                |
| UnauthorizedOperation             | 未授权操作。                                                |
| UnknownParameter                  | 未知参数错误。                                              |
| UnsupportedOperation              | 操作不支持。                                                |
| UnsupportedProtocol               | HTTPS 请求方法错误，只支持 GET 和 POST 请求。               |
| UnsupportedRegion                 | 接口不支持所传地域。                                        |
