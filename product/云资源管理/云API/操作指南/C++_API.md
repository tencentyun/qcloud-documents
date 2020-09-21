
腾讯云 API 全新升级3.0，该版本进行了性能优化且全地域部署、支持就近和按地域接入、访问时延下降显著，接口描述更加详细、错误码描述更加全面、SDK 增加接口级注释，让您更加方便快捷的使用腾讯云产品。这里针对 C++ API 调用方式进行简单说明。
现已支持云服务器（CVM）、云硬盘（CBS）、私有网络（VPC）、云数据库（TencentDB）等 [腾讯云产品](https://cloud.tencent.com/product)，后续会支持其他的云产品接入，敬请期待。 


## 了解请求结构

### 1. 服务地址（endpoint）

API 支持就近地域接入（例如：cvm 产品域名为 `cvm.tencentcloudapi.com`），也支持指定地域域名访问（例如：广州地域的域名为 `cvm.ap-guangzhou.tencentcloudapi.com`），各地域参数见下文公共参数中的地域列表，详情请参见各产品的“请求结构”文档说明判断是否支持该地域。

>!对时延敏感的业务，建议指定带地域的域名。

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

>?公共参数是用于标识用户和接口签名的参数，每次请求均需要携带这些参数，才能正常发起请求。 

### 签名方法 V3公共参数

签名方法 v3（有时也称作 TC3-HMAC-SHA256）相比签名方法 v1（部分文档简称为“签名方法”），更安全，支持更大的请求包，支持 POST JSON 格式，性能有一定提升，推荐使用该签名方法计算签名。使用方法见下文“签名方法介绍”。 

| 参数名称       | 类型    | 必选   | 描述                                                         |
| :------------- | :------ | :----- | :----------------------------------------------------------- |
| X-TC-Action    | String  | **是** | 操作的接口名称。取值参考接口文档中输入参数公共参数 Action 的说明。例如云服务器的查询实例列表接口，取值为 DescribeInstances。 |
| X-TC-Region    | String  | -      | 地域参数，用来标识希望操作哪个地域的数据。接口接受的地域取值参考接口文档中输入参数公共参数 Region 的说明。**注意：某些接口不需要传递该参数，接口文档中会对此特别说明，此时即使传递该参数也不会生效。** |
| X-TC-Timestamp | Integer | **是** | 当前 UNIX 时间戳，可记录发起 API 请求的时间。例如1529223702。**注意：如果与服务器时间相差超过5分钟，会引起签名过期错误。** |
| X-TC-Version   | String  | **是** | 操作的 API 的版本。取值参考接口文档中入参公共参数 Version 的说明。例如云服务器的版本2017-03-12。 |
| Authorization  | String  | **是** | HTTP 标准身份认证头部字段，例如： TC3-HMAC-SHA256 Credential=AKIDEXAMPLE/Date/service/tc3_request, SignedHeaders=content-type;host, Signature=72e494ea8******************************************a96525168 <br>其中：<li>TC3-HMAC-SHA256：签名方法，目前固定取该值。</li><li>Credential：签名凭证，AKIDEXAMPLE 是 SecretId。</li><li>Date 是 UTC 标准时间的日期，取值需要和公共参数 X-TC-Timestamp 换算的 UTC 标准时间日期一致。</li><li>service 为产品名，通常为域名前缀，例如域名 cvm.tencentcloudapi.com 意味着产品名是 cvm。本产品取值为 cvm。</li><li>SignedHeaders：参与签名计算的头部信息，content-type 和 host 为必选头部。</li><li>Signature：签名摘要，计算过程详见下文。</li> |
| X-TC-Token     | String  | 否     | 临时证书所用的 Token ，需要结合临时密钥一起使用。临时密钥和 Token 需要到访问管理服务调用接口获取。长期密钥不需要 Token。 |



### 地域列表

由于各个产品支持地域不同，具体详情请参考各产品文档中的地域列表。
例如，您可以参考云服务器的 [地域列表](https://cloud.tencent.com/document/product/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。



## C++ API 调用方式

腾讯云 API 会对每个请求进行身份验证，用户需要使用安全凭证，经过特定的步骤对请求进行签名（Signature），每个请求都需要在公共请求参数中指定该签名结果并以指定的方式和格式发送请求。
>!目前 C++ 暂不支持 API 3.0签名 V1版本。

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

>! **用户必须严格保管安全凭证，避免泄露，否则将危及财产安全。如已泄漏，请立刻禁用该安全凭证。**

前往 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面，即可进行获取。如下图所示：
![](https://main.qcloudimg.com/raw/665e5334b0d5db156ef48a19072ba8bd.png)

### 步骤2：获取 API 3.0 V3 版本签名
签名方法 v3（TC3-HMAC-SHA256）功能上覆盖了以前的签名方法 v1，而且更安全，支持更大的请求，支持 json 格式，性能有一定提升，推荐使用该签名方法计算签名。如下图所示：
>?首次接触，建议使用 [API Explorer](https://console.cloud.tencent.com/api/explorer) 中的“签名串生成”功能，选择签名版本为 “API 3.0 签名 v3”，可以生成签名过程进行验证，也可直接生成 SDK 代码。推荐使用腾讯云 API 配套的7种常见的编程语言 SDK，已经封装了签名和请求过程，均已开源，支持 [Python](https://github.com/TencentCloud/tencentcloud-sdk-python)、[Java](https://github.com/TencentCloud/tencentcloud-sdk-java)、[PHP](https://github.com/TencentCloud/tencentcloud-sdk-php)、[Go](https://github.com/TencentCloud/tencentcloud-sdk-go)、[NodeJS](https://github.com/TencentCloud/tencentcloud-sdk-nodejs)、[.NET](https://github.com/TencentCloud/tencentcloud-sdk-dotnet)、[C++](https://github.com/TencentCloud/tencentcloud-sdk-cpp)。
>
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
| HTTPRequestMethod    | HTTP 请求方法（GET、POST）。此示例取值为 `POST`。           |
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
| RequestTimestamp       | 请求时间戳，即请求头部的公共参数 X-TC-Timestamp 取值，取当前时间 UNIX 时间戳，精确到秒。此示例取值为`1551113065`。 |
| CredentialScope        | 凭证范围，格式为 Date/service/tc3_request，包含日期、所请求的服务和终止字符串（tc3_request）。**Date 为 UTC 标准时间的日期，取值需要和公共参数 X-TC-Timestamp 换算的 UTC 标准时间日期一致**；service 为产品名，必须与调用的产品域名一致。此示例计算结果是2019-02-25/cvm/tc3_request。 |
| HashedCanonicalRequest | 前述步骤拼接所得规范请求串的哈希值，计算伪代码为 Lowercase(HexEncode(Hash.SHA256(CanonicalRequest)))。此示例计算结果是`5ffe6a04c0664d6b969fab9a13bdab201d63ee709638e2749d62a09ca18d7031`。 |

>!
> - Date 必须从时间戳 X-TC-Timestamp 计算得到，且时区为 UTC+0。如果加入系统本地时区信息，例如东八区，将导致白天和晚上调用成功，但是凌晨时调用必定失败。假设时间戳为1551113065，在东八区的时间是2019-02-26 00:44:25，但是计算得到的 Date 取 UTC+0 的日期应为2019-02-25，而不是2019-02-26。
> - Timestamp 必须是当前系统时间，且需确保系统时间和标准时间是同步的，如果相差超过五分钟则必定失败。如果长时间不和标准时间同步，可能导致运行一段时间后，请求必定失败，返回签名过期错误。

 根据以上规则，示例中得到的待签名字符串如下： 

```
TC3-HMAC-SHA256
1551113065
2019-02-25/cvm/tc3_request
5ffe6a04c0664d6b969fab9a13bdab201d63ee709638e2749d62a09ca18d7031
```

#### 3. 计算签名（伪代码）

实际请参考下面示例：
1）计算派生签名密钥，伪代码如下：

```c++
#include <tencentcloud/core/Sign.h>
#include <tencentcloud/core/utils/Utils.h>


using namespace TencentCloud;
using namespace std;

string Sign::Tc3Sign(const string &credDate, const string &serviceName, const string &signStr)
{
    string kKey = "TC3"+this->m_secretKey;
    string kDate = Utils::HmacSha256(kKey, credDate);
    string kService = Utils::HmacSha256(kDate, serviceName);
    string kSigning = Utils::HmacSha256(kService, "tc3_request");
    return Utils::HexEncode(Utils::HmacSha256(kSigning, signStr));
}
```

派生出的密钥 `SecretDate`、`SecretService` 和 `SecretSigning` 是二进制的数据，可能包含不可打印字符，此处不展示中间结果。

>! 不同的编程语言，HMAC 库函数中参数顺序可能不一样，此处的伪代码密钥参数在后，请以实际编程语言为准。通常标准库函数会提供二进制格式的计算值，也即此处使用的，也会提供打印友好的十六进制格式的计算值，将在下面计算签名结果时使用。

| 字段名称    | 解释                                                         |
| :---------- | :----------------------------------------------------------- |
| m_secretKey | 原始的 SecretKey，即 `Gu5t9xGAR***********EXAMPLE`。         |
| credDate    | 即 Credential 中的 Date 字段信息。此示例取值为`2019-02-25`。 |
| serviceName | 即 Credential 中的 Service 字段信息。此示例取值为 `cvm`。    |
| signStr     | 代签名字符串。                                               |

2）计算签名：

此示例计算结果是 `72e494ea8******************************************a96525168`。

#### 4. 拼接 Authorization

按如下格式拼接 Authorization：
```
Authorization =
    Algorithm + ' ' +
    'Credential=' + SecretId + '/' + CredentialScope + ', ' +
    'SignedHeaders=' + SignedHeaders + ', ' +
    'Signature=' + Signature
```

| 字段名称        | 解释                                                         |
| :-------------- | :----------------------------------------------------------- |
| Algorithm       | 签名方法，固定为 `TC3-HMAC-SHA256`。                         |
| SecretId        | 密钥对中的 SecretId，即 `AKIDz8krbsJ5**********mLPx3EXAMPLE`。 |
| CredentialScope | 见上文，凭证范围。此示例计算结果是`2019-02-25/cvm/tc3_request`。 |
| SignedHeaders   | 见上文，参与签名的头部信息。此示例取值为 `content-type;host`。 |
| Signature       | 签名值。此示例计算结果是 `72e494ea8******************************************a96525168`。 |

根据以上规则，示例中得到的值为：

```
TC3-HMAC-SHA256 Credential=AKIDz8krbsJ5**********mLPx3EXAMPLE/2019-02-25/cvm/tc3_request, SignedHeaders=content-type;host, Signature=72e494ea8******************************************a96525168
```

最终完整的调用信息如下：

```
POST https://cvm.tencentcloudapi.com/
Authorization: TC3-HMAC-SHA256 Credential=AKIDz8krbsJ5**********mLPx3EXAMPLE/2019-02-25/cvm/tc3_request, SignedHeaders=content-type;host, Signature=72e494ea8******************************************a96525168
Content-Type: application/json; charset=utf-8
Host: cvm.tencentcloudapi.com
X-TC-Action: DescribeInstances
X-TC-Version: 2017-03-12
X-TC-Timestamp: 1551113065
X-TC-Region: ap-guangzhou

{"Limit": 1, "Filters": [{"Values": ["\u672a\u547d\u540d"], "Name": "instance-name"}]}
```

#### 5. API 3.0签名 V3示例

```c++
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <stdio.h>
#include <time.h>
#include <openssl/sha.h>
#include <openssl/hmac.h>

using namespace std;

string get_data(int64_t &timestamp)
{
    string utcDate;
    char buff[20] = {0};
    // time_t timenow;
    struct tm sttime;
    sttime = *gmtime(&timestamp);
    strftime(buff, sizeof(buff), "%Y-%m-%d", &sttime);
    utcDate = string(buff);
    return utcDate;
}
string int2str(int64_t n)
{
    std::stringstream ss;
    ss << n;
    return ss.str();
}
string sha256Hex(const string &str)
{
    char buf[3];
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256_CTX sha256;
    SHA256_Init(&sha256);
    SHA256_Update(&sha256, str.c_str(), str.size());
    SHA256_Final(hash, &sha256);
    std::string NewString = "";
    for(int i = 0; i < SHA256_DIGEST_LENGTH; i++)
    {
        snprintf(buf, sizeof(buf), "%02x", hash[i]);
        NewString = NewString + buf;
    }
    return NewString;
}
string HmacSha256(const string &key, const string &input)
{
    unsigned char hash[32];

    HMAC_CTX *h;
#if OPENSSL_VERSION_NUMBER < 0x10100000L
    HMAC_CTX hmac;
    HMAC_CTX_init(&hmac);
    h = &hmac;
#else
    h = HMAC_CTX_new();
#endif

    HMAC_Init_ex(h, &key[0], key.length(), EVP_sha256(), NULL);
    HMAC_Update(h, ( unsigned char* )&input[0], input.length());
    unsigned int len = 32;
    HMAC_Final(h, hash, &len);

#if OPENSSL_VERSION_NUMBER < 0x10100000L
    HMAC_CTX_cleanup(h);
#else
    HMAC_CTX_free(h);
#endif

    std::stringstream ss;
    ss << std::setfill('0');
    for (int i = 0; i < len; i++)
    {
        ss  << hash[i];
    }

    return (ss.str());
}
string HexEncode(const string &input)
{
    static const char* const lut = "0123456789abcdef";
    size_t len = input.length();
    
    string output;
    output.reserve(2 * len);
    for (size_t i = 0; i < len; ++i)
    {
        const unsigned char c = input[i];
        output.push_back(lut[c >> 4]);
        output.push_back(lut[c & 15]);
    }
    return output;
}

int main()
{
    // 密钥参数
    string SECRET_ID = "AKIDz8krbsJ5**********mLPx3EXAMPLE";
    string SECRET_KEY = "Gu5t9xGAR***********EXAMPLE";

    string service = "cvm";
    string host = "cvm.tencentcloudapi.com";
    string region = "ap-guangzhou";
    string action = "DescribeInstances";
    string version = "2017-03-12";
    int64_t timestamp = 1551113065;
    string date = get_data(timestamp);

    // ************* 步骤 1：拼接规范请求串 *************
    string httpRequestMethod = "POST";
    string canonicalUri = "/";
    string canonicalQueryString = "";
    string canonicalHeaders = "content-type:application/json; charset=utf-8\nhost:" + host + "\n";
    string signedHeaders = "content-type;host";
    string payload = "{\"Limit\": 1, \"Filters\": [{\"Values\": [\"\\u672a\\u547d\\u540d\"], \"Name\": \"instance-name\"}]}";
    string hashedRequestPayload = sha256Hex(payload);
    string canonicalRequest = httpRequestMethod + "\n" + canonicalUri + "\n" + canonicalQueryString + "\n"
            + canonicalHeaders + "\n" + signedHeaders + "\n" + hashedRequestPayload;
    cout << canonicalRequest << endl;
    cout << "-----------------------" << endl;

    // ************* 步骤 2：拼接待签名字符串 *************
    string algorithm = "TC3-HMAC-SHA256";
    string RequestTimestamp = int2str(timestamp);
    string credentialScope = date + "/" + service + "/" + "tc3_request";
    string hashedCanonicalRequest = sha256Hex(canonicalRequest);
    string stringToSign = algorithm + "\n" + RequestTimestamp + "\n" + credentialScope + "\n" + hashedCanonicalRequest;
    cout << stringToSign << endl;
    cout << "-----------------------" << endl;

    // ************* 步骤 3：计算签名 ***************
    string kKey = "TC3" + SECRET_KEY;
    string kDate = HmacSha256(kKey, date);
    string kService = HmacSha256(kDate, service);
    string kSigning = HmacSha256(kService, "tc3_request");
    string signature = HexEncode(HmacSha256(kSigning, stringToSign));
    cout << signature << endl;
    cout << "-----------------------" << endl;

    // ************* 步骤 4：拼接 Authorization *************
    string authorization = algorithm + " " + "Credential=" + SECRET_ID + "/" + credentialScope + ", "
            + "SignedHeaders=" + signedHeaders + ", " + "Signature=" + signature;
    cout << authorization << endl;
    cout << "------------------------" << endl;
    
    string headers = "curl -X POST https://" + host + "\n"
                   + " -H \"Authorization: " + authorization + "\n"
                   + " -H \"Content-Type: application/json; charset=utf-8\"" + "\n"
                   + " -H \"Host: " + host + "\n"
                   + " -H \"X-TC-Action: " + action + "\n"
                   + " -H \"X-TC-Timestamp: " + RequestTimestamp + "\n"
                   + " -H \"X-TC-Version: " + version + "\n"
                   + " -H \"X-TC-Region: " + region + "\n"
                   + " -d '" + payload;
    cout << headers << endl;
    return 0;
};
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

以云服务器的接口查看实例状态列表（DescribeInstancesStatus）2017-03-12 版本为例，若调用成功，其可能的返回如下为：

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
* 除了固定的字段外，其余均为具体接口定义的字段，不同的接口所返回的字段参见接口文档中的定义。此例中的 `TotalCount` 和 `InstanceStatusSet` 均为 DescribeInstancesStatus 接口定义的字段，由于调用请求的用户暂时还没有云服务器实例，因此 `TotalCount` 在此情况下的返回值为0， `InstanceStatusSet` 列表为空。

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
