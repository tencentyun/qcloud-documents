##### 精准获客API文档

## 更新历史

| 时间           | 说明                                       |
| ------------  | -----------------------------------------  |
| 2020-11-12 | Init         |
|            |      |

## 简介

针对汽车精准获客服务控制台，提供人群特征洞察统计以及购车意向预测统计的控制台展示接口，包括1.总统计数据 2. 根据时间区间获取调用曲线 3.调用明细
## API概览

| 接口名称 | 接口功能         |
|---------|---------|
| QueryGeneralStat |  查询总统计信息    |
| QueryCallsStat      |  查询调用统计    |
| QueryCallDetails      |  查询调用明细    |
## 调用方式
### 请求结构
#### **1.服务地址**

API 支持就近地域接入，本产品就近地域接入域名为 apcas.tencentcloudapi.com ，也支持指定地域域名访问，例如广州地域的域名为 apcas.ap-guangzhou.tencentcloudapi.com 。

推荐使用就近地域接入域名。根据调用接口时客户端所在位置，会自动解析到最近的某个具体地域的服务器。例如在广州发起请求，会自动解析到广州的服务器，效果和指定 apcas.ap-guangzhou.tencentcloudapi.com 是一致的。
**注意：对时延敏感的业务，建议指定带地域的域名。**

**注意：域名是 API 的接入点，并不代表产品或者接口实际提供服务的地域。产品支持的地域列表请在调用方式/公共参数文档中查阅，接口支持的地域请在接口文档输入参数中查阅。**

#### **2.通信协议**

腾讯云 API 的所有接口均通过 HTTPS 进行通信，提供高安全性的通信通道。

#### **3.请求方法**

支持的 HTTP 请求方法:

- POST（推荐）

- GET


POST 请求支持的 Content-Type 类型：

- application/json（推荐），必须使用签名方法 v3（TC3-HMAC-SHA256）。

#### **4.字符编码**

均使用UTF-8编码。
### 公共参数
公共参数是用于标识用户和接口签名的参数，如非必要，在每个接口单独的接口文档中不再对这些参数进行说明，但每次请求均需要携带这些参数，才能正常发起请求。
#### 签名方法 v3
签名方法 v3 （有时也称作 TC3-HMAC-SHA256）相比签名方法 v1 （有些文档可能会简称签名方法），更安全，支持更大的请求包，支持 POST JSON 格式，性能有一定提升，推荐使用该签名方法计算签名。完整介绍详见4.3。

注意：接口文档中的示例由于目的是展示接口参数用法，简化起见，使用的是签名方法 v1 GET 请求，如果依旧想使用签名方法 v1 请参考下文章节。

使用签名方法 v3 时，公共参数需要统一放到 HTTP Header 请求头部中，如下：
| 参数名称 | 类型  | 必选 | 描述 |
|---------|---------|---------|---------|
| X-TC-Action | String | 是 | 操作的接口名称。取值参考接口文档中输入参数公共参数 Action 的说明。例如云服务器的查询实例列表接口，取值为 DescribeInstances。 |
| X-TC-Region | String | - | 地域参数，用来标识希望操作哪个地域的数据。接口接受的地域取值参考接口文档中输入参数公共参数 Region 的说明。**注意：某些接口不需要传递该参数，接口文档中会对此特别说明，此时即使传递该参数也不会生效。** |
| X-TC-Timestamp | Integer | 是 | 当前 UNIX 时间戳，可记录发起 API 请求的时间。例如 1529223702。**注意：如果与服务器时间相差超过5分钟，会引起签名过期错误。** |
| X-TC-Version | String | 是 | 操作的 API 的版本。取值参考接口文档中入参公共参数 Version 的说明。例如云服务器的版本 2017-03-12。 |
| Authorization | String | 是 | HTTP 标准身份认证头部字段，例如： TC3-HMAC-SHA256 Credential=AKIDEXAMPLE/Date/service/tc3_request, SignedHeaders=content-type;host, Signature=fe5f80f77d5fa3beca038a248ff027d0445342fe2855ddc963176630326f1024 其中， - TC3-HMAC-SHA256：签名方法，目前固定取该值； - Credential：签名凭证，AKIDEXAMPLE 是 SecretId；Date 是 UTC 标准时间的日期，取值需要和公共参数 X-TC-Timestamp 换算的 UTC 标准时间日期一致；service 为产品名，通常为域名前缀，例如域名 cvm.tencentcloudapi.com 意味着产品名是 cvm。本产品取值为 soe； - SignedHeaders：参与签名计算的头部信息，content-type 和 host 为必选头部； - Signature：签名摘要，计算过程详见 [文档](https://cloud.tencent.com/document/api/884/30657)。 |
| X-TC-Token | String | 否 | 临时证书所用的 Token ，需要结合临时密钥一起使用。临时密钥和 Token 需要到访问管理服务调用接口获取。长期密钥不需要 Token。 |

假设用户想要查询广州地域的云服务器实例列表，则其请求结构按照请求 URL、请求头部、请求体示例如下:

HTTP GET 请求结构示例:

```json
https://cvm.tencentcloudapi.com/?Limit=10&Offset=0

Authorization: TC3-HMAC-SHA256 Credential=AKID********EXAMPLE/2018-10-09/cvm/tc3_request, SignedHeaders=content-type;host, Signature=5da7a33f6993f0614b047e5df4582db9e9bf4672ba50567dba16c6ccf174c474
Content-Type: application/x-www-form-urlencoded
Host: cvm.tencentcloudapi.com
X-TC-Action: DescribeInstances
X-TC-Version: 2017-03-12
X-TC-Timestamp: 1539084154
X-TC-Region: ap-guangzhou
```

HTTP POST （application/json） 请求结构示例：

```
https://cvm.tencentcloudapi.com/

Authorization: TC3-HMAC-SHA256 Credential=AKID********EXAMPLE/2018-05-30/cvm/tc3_request, SignedHeaders=content-type;host, Signature=582c400e06b5924a6f2b5d7d672d79c15b13162d9279b0855cfba6789a8edb4c
Content-Type: application/json
Host: cvm.tencentcloudapi.com
X-TC-Action: DescribeInstances
X-TC-Version: 2017-03-12
X-TC-Timestamp: 1527672334
X-TC-Region: ap-guangzhou

{"Offset":0,"Limit":10}
```

HTTP POST （multipart/form-data）请求结构示例（仅特定的接口支持）：

```json
https://cvm.tencentcloudapi.com/

Authorization: TC3-HMAC-SHA256 Credential=AKID********EXAMPLE/2018-05-30/cvm/tc3_request, SignedHeaders=content-type;host, Signature=582c400e06b5924a6f2b5d7d672d79c15b13162d9279b0855cfba6789a8edb4c
Content-Type: multipart/form-data; boundary=58731222010402
Host: cvm.tencentcloudapi.com
X-TC-Action: DescribeInstances
X-TC-Version: 2017-03-12
X-TC-Timestamp: 1527672334
X-TC-Region: ap-guangzhou

--58731222010402
Content-Disposition: form-data; name="Offset"

0
--58731222010402
Content-Disposition: form-data; name="Limit"

10
--58731222010402--
```

#### 签名方法 v1

使用签名方法 v1 （有时会称作 HmacSHA256 和 HmacSHA1），公共参数需要统一放到请求串中，完整介绍详见[文档](https://cloud.tencent.com/document/api/884/19314)

| 参数名称        | 类型    | 必选 | 描述                                                         |
| :-------------- | :------ | :--- | :----------------------------------------------------------- |
| Action          | String  | 是   | 操作的接口名称。取值参考接口文档中输入参数公共参数 Action 的说明。例如云服务器的查询实例列表接口，取值为 DescribeInstances。 |
| Region          | String  | -    | 地域参数，用来标识希望操作哪个地域的数据。接口接受的地域取值参考接口文档中输入参数公共参数 Region 的说明。**注意：某些接口不需要传递该参数，接口文档中会对此特别说明，此时即使传递该参数也不会生效。** |
| Timestamp       | Integer | 是   | 当前 UNIX 时间戳，可记录发起 API 请求的时间。例如1529223702，如果与当前时间相差过大，会引起签名过期错误。 |
| Nonce           | Integer | 是   | 随机正整数，与 Timestamp 联合起来，用于防止重放攻击。        |
| SecretId        | String  | 是   | 在 [云API密钥](https://console.cloud.tencent.com/capi) 上申请的标识身份的 SecretId，一个 SecretId 对应唯一的 SecretKey ，而 SecretKey 会用来生成请求签名 Signature。 |
| Signature       | String  | 是   | 请求签名，用来验证此次请求的合法性，需要用户根据实际的输入参数计算得出。具体计算方法参见 [文档](https://cloud.tencent.com/document/api/884/19314)。 |
| Version         | String  | 是   | 操作的 API 的版本。取值参考接口文档中入参公共参数 Version 的说明。例如云服务器的版本 2017-03-12。 |
| SignatureMethod | String  | 否   | 签名方式，目前支持 HmacSHA256 和 HmacSHA1。只有指定此参数为 HmacSHA256 时，才使用 HmacSHA256 算法验证签名，其他情况均使用 HmacSHA1 验证签名。 |
| Token           | String  | 否   | 临时证书所用的 Token ，需要结合临时密钥一起使用。临时密钥和 Token 需要到访问管理服务调用接口获取。长期密钥不需要 Token 。 |

假设用户想要查询广州地域的云服务器实例列表，其请求结构按照请求 URL、请求头部、请求体示例如下:

HTTP GET 请求结构示例:

```json
https://cvm.tencentcloudapi.com/?Action=DescribeInstances&Version=2017-03-12&SignatureMethod=HmacSHA256&Timestamp=1527672334&Signature=37ac2f4fde00b0ac9bd9eadeb459b1bbee224158d66e7ae5fcadb70b2d181d02&Region=ap-guangzhou&Nonce=23823223&SecretId=AKID********EXAMPLE

Host: cvm.tencentcloudapi.com
Content-Type: application/x-www-form-urlencoded
```

HTTP POST 请求结构示例：

```json
https://cvm.tencentcloudapi.com/

Host: cvm.tencentcloudapi.com
Content-Type: application/x-www-form-urlencoded

Action=DescribeInstances&Version=2017-03-12&SignatureMethod=HmacSHA256&Timestamp=1527672334&Signature=37ac2f4fde00b0ac9bd9eadeb459b1bbee224158d66e7ae5fcadb70b2d181d02&Region=ap-guangzhou&Nonce=23823223&SecretId=AKID********EXAMPLE
```

### 签名方法

签名方法 v1 简单易用，但是功能和安全性都不如签名方法 v3，推荐使用签名方法 v3。

首次接触，建议使用 [API Explorer](https://console.cloud.tencent.com/api/explorer) 中的“签名串生成”功能，选择签名版本为“API 3.0 签名 v1”，可以生成签名过程进行验证，并提供了部分编程语言的签名示例，也可直接生成 SDK 代码。推荐使用腾讯云 API 配套的 7 种常见的编程语言 SDK，已经封装了签名和请求过程，均已开源，支持 [Python](https://github.com/TencentCloud/tencentcloud-sdk-python)、[Java](https://github.com/TencentCloud/tencentcloud-sdk-java)、[PHP](https://github.com/TencentCloud/tencentcloud-sdk-php)、[Go](https://github.com/TencentCloud/tencentcloud-sdk-go)、[NodeJS](https://github.com/TencentCloud/tencentcloud-sdk-nodejs)、[.NET](https://github.com/TencentCloud/tencentcloud-sdk-dotnet)。

腾讯云 API 会对每个访问请求进行身份验证，即每个请求都需要在公共请求参数中包含签名信息（Signature）以验证请求者身份。 签名信息由安全凭证生成，安全凭证包括 SecretId 和 SecretKey；若用户还没有安全凭证，请前往 [云API密钥页面](https://console.cloud.tencent.com/capi) 申请，否则无法调用云 API 接口。

#### 1. 申请安全凭证

在第一次使用云 API 之前，请前往 [云 API 密钥页面](https://console.cloud.tencent.com/capi) 申请安全凭证。 安全凭证包括 SecretId 和 SecretKey：

- SecretId 用于标识 API 调用者身份
- SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥。
- **用户必须严格保管安全凭证，避免泄露。**

申请安全凭证的具体步骤如下：

1. 登录 [腾讯云管理中心控制台](https://console.cloud.tencent.com/)。
2. 前往 [云 API 密钥](https://console.cloud.tencent.com/capi) 的控制台页面
3. 在 [云 API 密钥](https://console.cloud.tencent.com/capi) 页面，单击【新建密钥】即可以创建一对 SecretId/SecretKey。

注意：每个账号最多可以拥有两对 SecretId/SecretKey。

#### 2. 生成签名串

有了安全凭证SecretId 和 SecretKey后，就可以生成签名串了。以下是生成签名串的详细过程：

假设用户的 SecretId 和 SecretKey 分别是：

- SecretId: `AKIDz8krbsJ5yKBZQpn74WFkmLPx3*******`
- SecretKey: `Gu5t9xGARNpq86cd98joQYCN3*******`

**注意：这里只是示例，请根据用户实际申请的 SecretId 和 SecretKey 进行后续操作！**

以云服务器查看实例列表(DescribeInstances)请求为例，当用户调用这一接口时，其请求参数可能如下:

| 参数名称      | 中文            | 参数值                                 |
| :------------ | :-------------- | :------------------------------------- |
| Action        | 方法名          | DescribeInstances                      |
| SecretId      | 密钥 ID         | `AKIDz8krbsJ5yKBZQpn74WFkmLPx3*******` |
| Timestamp     | 当前时间戳      | 1465185768                             |
| Nonce         | 随机正整数      | 11886                                  |
| Region        | 实例所在区域    | ap-guangzhou                           |
| InstanceIds.0 | 待查询的实例 ID | ins-09dx96dg                           |
| Offset        | 偏移量          | 0                                      |
| Limit         | 最大允许输出    | 20                                     |
| Version       | 接口版本号      | 2017-03-12                             |

##### 2.1. 对参数排序

首先对所有请求参数按参数名的字典序（ ASCII 码）升序排序。注意：1）只按参数名进行排序，参数值保持对应即可，不参与比大小；2）按 ASCII 码比大小，如 InstanceIds.2 要排在 InstanceIds.12 后面，不是按字母表，也不是按数值。用户可以借助编程语言中的相关排序函数来实现这一功能，如 PHP 中的 ksort 函数。上述示例参数的排序结果如下:

```
{
    'Action' : 'DescribeInstances',
    'InstanceIds.0' : 'ins-09dx96dg',
    'Limit' : 20,
    'Nonce' : 11886,
    'Offset' : 0,
    'Region' : 'ap-guangzhou',
    'SecretId' : 'AKIDz8krbsJ5yKBZQpn74WFkmLPx3*******',
    'Timestamp' : 1465185768,
    'Version': '2017-03-12',
}
```

使用其它程序设计语言开发时，可对上面示例中的参数进行排序，得到的结果一致即可。

##### 2.2. 拼接请求字符串

此步骤生成请求字符串。 将把上一步排序好的请求参数格式化成“参数名称=参数值”的形式，如对 Action 参数，其参数名称为 "Action" ，参数值为 "DescribeInstances" ，因此格式化后就为 Action=DescribeInstances 。 **注意：“参数值”为原始值而非 url 编码后的值。**

然后将格式化后的各个参数用"&"拼接在一起，最终生成的请求字符串为:

```
Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Limit=20&Nonce=11886&Offset=0&Region=ap-guangzhou&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3*******&Timestamp=1465185768&Version=2017-03-12
```

##### 2.3. 拼接签名原文字符串

此步骤生成签名原文字符串。 签名原文字符串由以下几个参数构成:

1. 请求方法: 支持 POST 和 GET 方式，这里使用 GET 请求，注意方法为全大写。
2. 请求主机:查看实例列表(DescribeInstances)的请求域名为：cvm.tencentcloudapi.com。实际的请求域名根据接口所属模块的不同而不同，详见各接口说明。
3. 请求路径: 当前版本云API的请求路径固定为 / 。
4. 请求字符串: 即上一步生成的请求字符串。

签名原文串的拼接规则为：`请求方法 + 请求主机 +请求路径 + ? + 请求字符串`。

示例的拼接结果为：

```
GETcvm.tencentcloudapi.com/?Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Limit=20&Nonce=11886&Offset=0&Region=ap-guangzhou&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3*******&Timestamp=1465185768&Version=2017-03-12
```

##### 2.4. 生成签名串

此步骤生成签名串。 首先使用 HMAC-SHA1 算法对上一步中获得的**签名原文字符串**进行签名，然后将生成的签名串使用 Base64 进行编码，即可获得最终的签名串。

具体代码如下，以 PHP 语言为例：

```
$secretKey = 'Gu5t9xGARNpq86cd98joQYCN3*******';
$srcStr = 'GETcvm.tencentcloudapi.com/?Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Limit=20&Nonce=11886&Offset=0&Region=ap-guangzhou&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3*******&Timestamp=1465185768&Version=2017-03-12';
$signStr = base64_encode(hash_hmac('sha1', $srcStr, $secretKey, true));
echo $signStr;
```

最终得到的签名串为：

```
zmmjn35mikh6pM3V7sUEuX4wyYM=
```

使用其它程序设计语言开发时，可用上面示例中的原文进行签名验证，得到的签名串与例子中的一致即可。

#### 3. 签名串编码

生成的签名串并不能直接作为请求参数，需要对其进行 URL 编码。

如上一步生成的签名串为 zmmjn35mikh6pM3V7sUEuX4wyYM= ，最终得到的签名串请求参数（Signature）为：zmmjn35mikh6pM3V7sUEuX4wyYM%3D，它将用于生成最终的请求 URL。

**注意：如果用户的请求方法是 GET，或者请求方法为 POST 同时 Content-Type 为 application/x-www-form-urlencoded，则发送请求时所有请求参数的值均需要做 URL 编码，参数键和=符号不需要编码。非 ASCII 字符在 URL 编码前需要先以 UTF-8 进行编码。**

**注意：有些编程语言的网络库会自动为所有参数进行 urlencode，在这种情况下，就不需要对签名串进行 URL 编码了，否则两次 URL 编码会导致签名失败。**

**注意：其他参数值也需要进行编码，编码采用 [RFC 3986](http://tools.ietf.org/html/rfc3986)。使用 %XY 对特殊字符例如汉字进行百分比编码，其中“X”和“Y”为十六进制字符（0-9 和大写字母 A-F），使用小写将引发错误。**

#### 4. 签名失败

根据实际情况，存在以下签名失败的错误码，请根据实际情况处理。

| 错误代码                     | 错误描述                        |
| :--------------------------- | :------------------------------ |
| AuthFailure.SignatureExpire  | 签名过期                        |
| AuthFailure.SecretIdNotFound | 密钥不存在                      |
| AuthFailure.SignatureFailure | 签名错误                        |
| AuthFailure.TokenFailure     | token 错误                      |
| AuthFailure.InvalidSecretId  | 密钥非法（不是云 API 密钥类型） |

#### 5. 签名演示

在实际调用 API 3.0 时，推荐使用配套的腾讯云 SDK 3.0 ，SDK 封装了签名的过程，开发时只关注产品提供的具体接口即可。详细信息参见 [SDK 中心](https://cloud.tencent.com/document/sdk)。当前支持的编程语言有：

- [Python](https://github.com/TencentCloud/tencentcloud-sdk-python)
- [Java](https://github.com/TencentCloud/tencentcloud-sdk-java)
- [PHP](https://github.com/TencentCloud/tencentcloud-sdk-php)
- [Go](https://github.com/TencentCloud/tencentcloud-sdk-go)
- [NodeJS](https://github.com/TencentCloud/tencentcloud-sdk-nodejs)
- [.NET](https://github.com/TencentCloud/tencentcloud-sdk-dotnet)

为了更清楚的解释签名过程，下面以实际编程语言为例，将上述的签名过程具体实现。请求的域名、调用的接口和参数的取值都以上述签名过程为准，代码只为解释签名过程，并不具备通用性，实际开发请尽量使用 SDK 。

最终输出的 url 可能为：`https://cvm.tencentcloudapi.com/?Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Limit=20&Nonce=11886&Offset=0&Region=ap-guangzhou&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3*******&Signature=zmmjn35mikh6pM3V7sUEuX4wyYM%3D&Timestamp=1465185768&Version=2017-03-12`。

注意：由于示例中的密钥是虚构的，时间戳也不是系统当前时间，因此如果将此 url 在浏览器中打开或者用 curl 等命令调用时会返回鉴权错误：签名过期。为了得到一个可以正常返回的 url ，需要修改示例中的 SecretId 和 SecretKey 为真实的密钥，并使用系统当前时间戳作为 Timestamp 。

注意：在下面的示例中，不同编程语言，甚至同一语言每次执行得到的 url 可能都有所不同，表现为参数的顺序不同，但这并不影响正确性。只要所有参数都在，且签名计算正确即可。

注意：以下代码仅适用于 API 3.0，不能直接用于其他的签名流程，即使是旧版的 API ，由于存在细节差异也会导致签名计算错误，请以对应的实际文档为准。

##### Java

```java
import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.util.Random;
import java.util.TreeMap;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import javax.xml.bind.DatatypeConverter;

public class TencentCloudAPIDemo {
    private final static String CHARSET = "UTF-8";

    public static String sign(String s, String key, String method) throws Exception {
        Mac mac = Mac.getInstance(method);
        SecretKeySpec secretKeySpec = new SecretKeySpec(key.getBytes(CHARSET), mac.getAlgorithm());
        mac.init(secretKeySpec);
        byte[] hash = mac.doFinal(s.getBytes(CHARSET));
        return DatatypeConverter.printBase64Binary(hash);
    }

    public static String getStringToSign(TreeMap<String, Object> params) {
        StringBuilder s2s = new StringBuilder("GETcvm.tencentcloudapi.com/?");
        // 签名时要求对参数进行字典排序，此处用TreeMap保证顺序
        for (String k : params.keySet()) {
            s2s.append(k).append("=").append(params.get(k).toString()).append("&");
        }
        return s2s.toString().substring(0, s2s.length() - 1);
    }

    public static String getUrl(TreeMap<String, Object> params) throws UnsupportedEncodingException {
        StringBuilder url = new StringBuilder("https://cvm.tencentcloudapi.com/?");
        // 实际请求的url中对参数顺序没有要求
        for (String k : params.keySet()) {
            // 需要对请求串进行urlencode，由于key都是英文字母，故此处仅对其value进行urlencode
            url.append(k).append("=").append(URLEncoder.encode(params.get(k).toString(), CHARSET)).append("&");
        }
        return url.toString().substring(0, url.length() - 1);
    }

    public static void main(String[] args) throws Exception {
        TreeMap<String, Object> params = new TreeMap<String, Object>(); // TreeMap可以自动排序
        // 实际调用时应当使用随机数，例如：params.put("Nonce", new Random().nextInt(java.lang.Integer.MAX_VALUE));
        params.put("Nonce", 11886); // 公共参数
        // 实际调用时应当使用系统当前时间，例如：   params.put("Timestamp", System.currentTimeMillis() / 1000);
        params.put("Timestamp", 1465185768); // 公共参数
        params.put("SecretId", "AKIDz8krbsJ5yKBZQpn74WFkmLPx3*******"); // 公共参数
        params.put("Action", "DescribeInstances"); // 公共参数
        params.put("Version", "2017-03-12"); // 公共参数
        params.put("Region", "ap-guangzhou"); // 公共参数
        params.put("Limit", 20); // 业务参数
        params.put("Offset", 0); // 业务参数
        params.put("InstanceIds.0", "ins-09dx96dg"); // 业务参数
        params.put("Signature", sign(getStringToSign(params), "Gu5t9xGARNpq86cd98joQYCN3*******", "HmacSHA1")); // 公共参数
        System.out.println(getUrl(params));
    }
}
```

##### Python

注意：如果是在 Python 2 环境中运行，需要先安装 requests 依赖包： `pip install requests` 。

```python
# -*- coding: utf8 -*-
import base64
import hashlib
import hmac
import time

import requests

secret_id = "AKIDz8krbsJ5yKBZQpn74WFkmLPx3*******"
secret_key = "Gu5t9xGARNpq86cd98joQYCN3*******"

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

##### Golang

```go
package main

import (
    "bytes"
    "crypto/hmac"
    "crypto/sha1"
    "encoding/base64"
    "fmt"
    "sort"
)

func main() {
    secretId := "AKIDz8krbsJ5yKBZQpn74WFkmLPx3*******"
    secretKey := "Gu5t9xGARNpq86cd98joQYCN3*******"
    params := map[string]string{
        "Nonce":         "11886",
        "Timestamp":     "1465185768",
        "Region":        "ap-guangzhou",
        "SecretId":      secretId,
        "Version":       "2017-03-12",
        "Action":        "DescribeInstances",
        "InstanceIds.0": "ins-09dx96dg",
        "Limit":         "20",
        "Offset":        "0",
    }

    var buf bytes.Buffer
    buf.WriteString("GET")
    buf.WriteString("cvm.tencentcloudapi.com")
    buf.WriteString("/")
    buf.WriteString("?")

    // sort keys by ascii asc order
    keys := make([]string, 0, len(params))
    for k, _ := range params {
        keys = append(keys, k)
    }
    sort.Strings(keys)

    for i := range keys {
        k := keys[i]
        buf.WriteString(k)
        buf.WriteString("=")
        buf.WriteString(params[k])
        buf.WriteString("&")
    }
    buf.Truncate(buf.Len() - 1)

    hashed := hmac.New(sha1.New, []byte(secretKey))
    hashed.Write(buf.Bytes())

    fmt.Println(base64.StdEncoding.EncodeToString(hashed.Sum(nil)))
}
```

##### PHP

```php
<?php
$secretId = "AKIDz8krbsJ5yKBZQpn74WFkmLPx3*******";
$secretKey = "Gu5t9xGARNpq86cd98joQYCN3*******";
$param["Nonce"] = 11886;//rand();
$param["Timestamp"] = 1465185768;//time();
$param["Region"] = "ap-guangzhou";
$param["SecretId"] = $secretId;
$param["Version"] = "2017-03-12";
$param["Action"] = "DescribeInstances";
$param["InstanceIds.0"] = "ins-09dx96dg";
$param["Limit"] = 20;
$param["Offset"] = 0;

ksort($param);

$signStr = "GETcvm.tencentcloudapi.com/?";
foreach ( $param as $key => $value ) {
    $signStr = $signStr . $key . "=" . $value . "&";
}
$signStr = substr($signStr, 0, -1);

$signature = base64_encode(hash_hmac("sha1", $signStr, $secretKey, true));
echo $signature.PHP_EOL;
// need to install and enable curl extension in php.ini
// $param["Signature"] = $signature;
// $url = "https://cvm.tencentcloudapi.com/?".http_build_query($param);
// echo $url.PHP_EOL;
// $ch = curl_init();
// curl_setopt($ch, CURLOPT_URL, $url);
// $output = curl_exec($ch);
// curl_close($ch);
// echo json_decode($output);
```

##### Ruby

```ruby
# -*- coding: UTF-8 -*-
# require ruby>=2.3.0
require 'time'
require 'openssl'
require 'base64'

secret_id = "AKIDz8krbsJ5yKBZQpn74WFkmLPx3*******"
secret_key = "Gu5t9xGARNpq86cd98joQYCN3*******"

method = 'GET'
endpoint = 'cvm.tencentcloudapi.com'
data = {
  'Action' => 'DescribeInstances',
  'InstanceIds.0' => 'ins-09dx96dg',
  'Limit' => 20,
  'Nonce' => 11886,
  'Offset' => 0,
  'Region' => 'ap-guangzhou',
  'SecretId' => secret_id,
  'Timestamp' => 1465185768, # Time.now.to_i
  'Version' => '2017-03-12',
}
sign = method + endpoint + '/?'
params = []
data.sort.each do |item|
  params << "#{item[0]}=#{item[1]}"
end
sign += params.join('&')
digest = OpenSSL::Digest.new('sha1')
data['Signature'] = Base64.encode64(OpenSSL::HMAC.digest(digest, secret_key, sign))
puts data['Signature']

# require 'net/http'
# uri = URI('https://' + endpoint)
# uri.query = URI.encode_www_form(data)
# p uri
# res = Net::HTTP.get_response(uri)
# puts res.body
```

##### DotNet

```c++
using System;
using System.Collections.Generic;
using System.Net;
using System.Security.Cryptography;
using System.Text;

public class Application {
    public static string Sign(string signKey, string secret)
    {
        string signRet = string.Empty;
            using (HMACSHA1 mac = new HMACSHA1(Encoding.UTF8.GetBytes(signKey)))
            {
                byte[] hash = mac.ComputeHash(Encoding.UTF8.GetBytes(secret));
                signRet = Convert.ToBase64String(hash);
            }
        return signRet;
    }
    public static string MakeSignPlainText(SortedDictionary<string, string> requestParams, string requestMethod, string requestHost, string requestPath)
    {
        string retStr = "";
        retStr += requestMethod;
        retStr += requestHost;
        retStr += requestPath;
        retStr += "?";
        string v = "";
        foreach (string key in requestParams.Keys)
        {
            v += string.Format("{0}={1}&", key, requestParams[key]);
        }
        retStr += v.TrimEnd('&');
        return retStr;
    }

    public static void Main(string[] args)
    {
        // 密钥参数
        string SECRET_ID = "AKIDz8krbsJ5yKBZQpn74WFkmLPx3*******";
        string SECRET_KEY = "Gu5t9xGARNpq86cd98joQYCN3*******";

        string endpoint = "cvm.tencentcloudapi.com";
        string region = "ap-guangzhou";
        string action = "DescribeInstances";
        string version = "2017-03-12";
        double RequestTimestamp = 1465185768;  // 时间戳 2019-02-26 00:44:25,此参数作为示例，以实际为准
        // long timestamp = ToTimestamp() / 1000;
        // string requestTimestamp = timestamp.ToString();
        Dictionary<string, string> param = new Dictionary<string, string>();
        param.Add("Limit", "20");
        param.Add("Offset", "0");
        param.Add("InstanceIds.0", "ins-09dx96dg");
        param.Add("Action", action);
        param.Add("Nonce", "11886");
        // param.Add("Nonce", Math.Abs(new Random().Next()).ToString());

        param.Add("Timestamp", RequestTimestamp.ToString());
        param.Add("Version", version);

        param.Add("SecretId", SECRET_ID);
        param.Add("Region", region);
        SortedDictionary<string, string> headers = new SortedDictionary<string, string>(param, StringComparer.Ordinal);
        string sigInParam = MakeSignPlainText(headers, "GET", endpoint, "/");
        string sigOutParam = Sign(SECRET_KEY, sigInParam);
        Console.WriteLine(sigOutParam);
    }
}
```

##### NodeJS

```js
const crypto = require('crypto');

function get_req_url(params, endpoint){
    params['Signature'] = escape(params['Signature']);
    const url_strParam = sort_params(params)
    return "https://" + endpoint + "/?" + url_strParam.slice(1);
}

function formatSignString(reqMethod, endpoint, path, strParam){
    let strSign = reqMethod + endpoint + path + "?" + strParam.slice(1);
    return strSign;
}
function sha1(secretKey, strsign){
    let signMethodMap = {'HmacSHA1': "sha1"};
    let hmac = crypto.createHmac(signMethodMap['HmacSHA1'], secretKey || "");
    return hmac.update(Buffer.from(strsign, 'utf8')).digest('base64')
}

function sort_params(params){
    let strParam = "";
    let keys = Object.keys(params);
    keys.sort();
    for (let k in keys) {
        //k = k.replace(/_/g, '.');
        strParam += ("&" + keys[k] + "=" + params[keys[k]]);
    }
    return strParam
}

function main(){
    // 密钥参数
    const SECRET_ID = "AKIDz8krbsJ5yKBZQpn74WFkmLPx3*******"
    const SECRET_KEY = "Gu5t9xGARNpq86cd98joQYCN3*******"

    const endpoint = "cvm.tencentcloudapi.com"
    const Region = "ap-guangzhou"
    const Version = "2017-03-12"
    const Action = "DescribeInstances"
    const Timestamp = 1465185768  // 时间戳 2016-06-06 12:02:48, 此参数作为示例，以实际为准
    // const Timestamp = Math.round(Date.now() / 1000)
    const Nonce = 11886  // 随机正整数
    //const nonce = Math.round(Math.random() * 65535)

    let params = {};
    params['Action'] = Action;
    params['InstanceIds.0'] = 'ins-09dx96dg';
    params['Limit'] = 20;
    params['Offset'] = 0;
    params['Nonce'] = Nonce;
    params['Region'] = Region;
    params['SecretId'] = SECRET_ID;
    params['Timestamp'] = Timestamp;
    params['Version'] = Version;

    // 1. 对参数排序,并拼接请求字符串
    strParam = sort_params(params)

    // 2. 拼接签名原文字符串
    const reqMethod = "GET";
    const path = "/";
    strSign = formatSignString(reqMethod, endpoint, path, strParam)
    // console.log(strSign)

    // 3. 生成签名串
    params['Signature'] = sha1(SECRET_KEY, strSign)
    console.log(params['Signature'])

    // 4. 进行url编码并拼接请求url
    // const req_url = get_req_url(params, endpoint)
    // console.log(params['Signature'])
    // console.log(req_url)
}
main()
```

### 返回结果

注意：目前只要请求被服务端正常处理了，响应的 HTTP 状态码均为200。例如返回的消息体里的错误码是签名失败，但 HTTP 状态码是200，而不是401。

#### 正确返回结果

以云服务器的接口查看实例状态列表 (DescribeInstancesStatus) 2017-03-12 版本为例，若调用成功，其可能的返回如下为：

```
{
    "Response": {
        "TotalCount": 0,
        "InstanceStatusSet": [],
        "RequestId": "b5b41468-520d-4192-b42f-595cc34b6c1c"
    }
}
```

- Response 及其内部的 RequestId 是固定的字段，无论请求成功与否，只要 API 处理了，则必定会返回。
- RequestId 用于一个 API 请求的唯一标识，如果 API 出现异常，可以联系我们，并提供该 ID 来解决问题。
- 除了固定的字段外，其余均为具体接口定义的字段，不同的接口所返回的字段参见接口文档中的定义。此例中的 TotalCount 和 InstanceStatusSet 均为 DescribeInstancesStatus 接口定义的字段，由于调用请求的用户暂时还没有云服务器实例，因此 TotalCount 在此情况下的返回值为 0， InstanceStatusSet 列表为空。

#### 错误返回结果

若调用失败，其返回值示例如下为：

```
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

- Error 的出现代表着该请求调用失败。Error 字段连同其内部的 Code 和 Message 字段在调用失败时是必定返回的。
- Code 表示具体出错的错误码，当请求出错时可以先根据该错误码在公共错误码和当前接口对应的错误码列表里面查找对应原因和解决方案。
- Message 显示出了这个错误发生的具体原因，随着业务发展或体验优化，此文本可能会经常保持变更或更新，用户不应依赖这个返回值。
- RequestId 用于一个 API 请求的唯一标识，如果 API 出现异常，可以联系我们，并提供该 ID 来解决问题。

#### 公共错误码

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

## 功能接口

### 获取统计信息

#### 1. 接口描述

接口请求域名： apcas.tencentcloudapi.com 。

获取人群特征洞察统计与购车意向预测统计的总体统计信息，包括今日调用量，本周调用量，本月调用量，总调用量。

推荐使用 API Explorer

[点击调试](https://console.cloud.tencent.com/api/explorer?Product=soe&Version=2018-07-24&Action=KeywordEvaluate)

API Explorer 提供了在线调用、签名验证、SDK 代码生成和快速检索接口等能力。您可查看每次调用的请求内容和返回结果以及自动生成 SDK 调用示例。

#### 2. 输入参数

以下请求参数列表仅列出了接口请求参数和部分公共参数，完整公共参数列表见 [公共请求参数](https://cloud.tencent.com/document/api/884/19313)。

| 参数名称 | 必选 | 类型    | 描述                                                         |
| :------- | :--- | :------ | :----------------------------------------------------------- |
| Action   | 是   | String  | 公共参数，本接口取值：QueryGeneralStat。      |
| Type   | 是   | String  | 请求类型:1,人群特征洞察统计 2购车意向预测统计                         |

#### 3. 输出参数

| 参数名称      | 类型                  | 描述                                                         |
| :------------ | :-------------------- | :----------------------------------------------------------- |
| TodayAmount | Long       | 今日调用量 |
| WeekAmount | Long       | 本周调用量 |
| MonthAmount | Long   | 本月调用量 |
| TotalAmount | Long   | 总调用量 |

#### 4. 示例

##### 示例1 关键词评测

评测中文和英文关键词，返回关键词切题分数

##### 输入示例

```json
https://apcas.tencentcloudapi.com/?Action=QueryGeneralStat
&Type=1
&<公共请求参数>
```

##### 输出示例

```json
{
  "Response": {
      "TodayAmount": 122222,
      "WeekAmount": 2222,
      "MonthAmount": 299333,
      "TotalAmount": 10000
}
```
### 获取调用量曲线

#### 1. 接口描述

接口请求域名： apcas.tencentcloudapi.com 。

选定时间区间，返回各时段的调用量。
推荐使用 API Explorer

[点击调试](https://console.cloud.tencent.com/api/explorer?Product=soe&Version=2018-07-24&Action=KeywordEvaluate)

API Explorer 提供了在线调用、签名验证、SDK 代码生成和快速检索接口等能力。您可查看每次调用的请求内容和返回结果以及自动生成 SDK 调用示例。

#### 2. 输入参数

以下请求参数列表仅列出了接口请求参数和部分公共参数，完整公共参数列表见 [公共请求参数](https://cloud.tencent.com/document/api/884/19313)。

| 参数名称 | 必选 | 类型    | 描述                                                         |
| :------- | :--- | :------ | :----------------------------------------------------------- |
| Action   | 是   | String  | 公共参数，本接口取值：QueryCallsStat。      |
| Type   | 是   | String  | 请求类型:1,人群特征洞察统计 2购车意向预测统计                         |
| StartTime   | 是   |  Long    | 开始时间戳（毫秒）         |
| EndTime   | 是   | Long  | 结束时间戳(毫秒）                |
#### 3. 输出参数

| 参数名称      | 类型                  | 描述                                                         |
| :------------ | :-------------------- | :----------------------------------------------------------- |

| CallsSet | Array of DateCalls| 调用量列表 |
| Date | String       | 时间,选择今天、昨天，以小时单位为区间返回;选择天数超过两天，以天为区间返回 |
| Amount | Long       | 各区间内调用量 |

#### 4. 示例

##### 示例1 获取调用量曲线

##### 输入示例

```json
https://apcas.tencentcloudapi.com/?Action=QueryCallsStat
&Type=1
&StartTime=1602470155000
&EndTime=1602470355000
&<公共请求参数>
```

##### 输出示例

```json
{
  "Response": {
      "CallsSet": [
              {
                  "Date": "2020-08-30 00:00:00",
                  "Amount": 2400
              },
               {
                  "Date": "2020-09-01 00:00:00",
                  "Amount": 2400
               }
          ]
}
```

### 获取调用明细

#### 1. 接口描述

接口请求域名： apcas.tencentcloudapi.com 。

选定时间区间，分页获取费用明细。
推荐使用 API Explorer

[点击调试](https://console.cloud.tencent.com/api/explorer?Product=soe&Version=2018-07-24&Action=KeywordEvaluate)

API Explorer 提供了在线调用、签名验证、SDK 代码生成和快速检索接口等能力。您可查看每次调用的请求内容和返回结果以及自动生成 SDK 调用示例。

#### 2. 输入参数

以下请求参数列表仅列出了接口请求参数和部分公共参数，完整公共参数列表见 [公共请求参数](https://cloud.tencent.com/document/api/884/19313)。

| 参数名称 | 必选 | 类型    | 描述                                                         |
| :------- | :--- | :------ | :----------------------------------------------------------- |
| Action   | 是   | String  | 公共参数，本接口取值：QueryCallDetails。      |
| Type   | 是   | String  | 请求类型:1,人群特征洞察统计 2购车意向预测统计                         |
| StartTime   | 是   |  Long    | 开始时间戳（毫秒）         |
| EndTime   | 是   | Long  | 结束时间戳(毫秒）                |
| PageNumber   | 是   |  Long    | 当前页号,从1开始        |
| PageSize   | 是   | Long  |  每页大小               |
#### 3. 输出参数

| 参数名称      | 类型                  | 描述                                                         |
| :------------ | :-------------------- | :----------------------------------------------------------- |
| TotalCount | Long| 符合条件的总条数 |
| CallDetailSet | Array of CallDetails|  |
| DataType | Integer       |  数据类型 0 imei 1 qimei 2 qq 3 phone 7:IDFA 8:MD5(imei)  |
| ValidAmount | Long       | 有效数据量 |
| Date | String       | 调用时间，格式如2020-09-05 17:00:00 |
#### 4. 示例

##### 示例1 获取调用明细

##### 输入示例

```json
https://apcas.tencentcloudapi.com/?Action=QueryCallDetails
&Type=1
&StartTime=1602470155000
&EndTime=1602470355000
&PageNumber=1
&PageSize=100
&<公共请求参数>
```

##### 输出示例

```json
{
  "Response": {
      "CallsSet": [
            "TotalCount": 20,
            "CallDetailSet": [
              {
                  "DataType": 1,
                   "ValidAmount": 3000,
                  "Date": "2020-09-04 18:00:00"
              },
              // ......
              // ......
              {
                  "DataType": 3,
                  "ValidAmount": 6380,
                  "Date": "2020-09-05 17:00:00"
              
          ]
}

```
