## 准备工作

1. 获取 SecretId 和 SecretKey。
    在控制台 [云API密钥](https://console.cloud.tencent.com/capi) 页面可获取。
2. 确定开发语言：
     支持但不限于 Java、PHP、C Sharp、C++、Node.js、Python，根据不同的开发语言，确定对应的 HMAC-SHA1函数。

## 签名内容
通过 API 对 CLS 发起的 HTTP 签名请求，使用标准的 HTTP Authorization 头部来传递，如下例所示：
```
GET /logset?logset_name=testset HTTP/1.1
Host: ap-shanghai.cls.myqcloud.com
Authorization: q-sign-algorithm=sha1&q-ak=AKIDc9YlmrBcFk4C8sbmXQ8i65XXXXXXXXXX&q-sign-time=1510109254;1510109314&q-key-time=1510109254;1510109314&q-header-list=content-type;host&q-url-param-list=logset_name&q-signature=e8b23b818caf4e33f196f895218bdabdbd1f1423
```

请求中的Host 字段为 ${region}.cls.myqcloud.com 其中 region 字段为日志服务区域，服务区域编码如下：

```
ap-beijing - 北京
ap-shanghai - 上海
ap-guangzhou - 广州
ap-chengdu - 成都
```

请求中的签名内容由多个 key=value 对，通过 “&” 连接而成，格式如下：

```
q-sign-algorithm=[Algorithm]&q-ak=[SecretId]&q-sign-time=[SignTime]&q-key-time=[KeyTime]&q-header-list=[SignedHeaderList]&q-url-param-list=[SignedParamList]&q-signature=[Signature]
```

### 键值描述

上述组成签名内容的键值(Key=Value)描述如下：

| 键（Key）        | 值（Value）            | 含义                                                         |
| ---------------- | ---------------------- | ------------------------------------------------------------ |
| q-sign-algorithm | sha1                   | 必填，签名算法，目前仅支持 sha1                              |
| q-ak             | 参数[SecretId]         | 必填，账户的SecretId，上述准备工作中从控制台获取的Id         |
| q-sign-time      | 参数[SignTime]         | 必填，签名有效起止时间，Unix时间戳，以秒为单位，用`;`分隔    |
| q-key-time       | 参数[KeyTime]          | 必填，与 q-sign-time 值相同                                  |
| q-header-list    | 参数[SignedHeaderList] | 必填，需要加入签名的Http请求头部的key，且 key 需转化为小写，并将多个 key 之间以字典顺序排序，如有多组 key，用`;`分隔。 |
| q-url-param-list | 参数[SignedParamList]  | 必填，需要加入签名的Http请求Uri部分参数，且 key 需转化为小写，并将多个 key 之间以字典顺序排序，如有多组 key，用```;```分隔。 |
| q-signature      | 参数[Signature]        | 必填，计算出的签名内容，小写字母                             |

> **注：** 关于q-sign-time 和 q-key-time， 结束时间要大于起始时间，否则会导致签名马上过期。

### 计算方法

Signature 的计算分为四个步骤：

1. 按照一定格式拼接Http请求的相关信息为字符串 HttpRequestInfo。

2. 对 HttpRequestInfo 使用 sha1 算法计算哈希值，与其他指定参数按照一定格式组成签名原串 StringToSign。

3. 使用 SecretKey 对 q-key-time 进行加密，得到 SignKey。

4. 使用 SignKey 对 StringToSign 进行加密，生成 Signature。

具体步骤如下：


#### 1. 拼接 HttpRequestInfo

HttpRequestInfo 由 HTTP 请求中的 Method, Uri，Headers, Parameters 组成，具体方式如下：
```
HttpRequestInfo = Method + "\n"
                + Uri + "\n"
                + FormatedParameters + "\n"
                + FormatedHeaders + "\n"
```

上述中的 ```\n``` 表示换行转义字符， ```+``` 表示字符串连接操作，其他各个参数定义如下：

| 字段名                | 含义                                       |
| ------------------ | ---------------------------------------- |
| Method             | Http请求使用的方法，小写字母，如 ```get、post```等       |
| Uri                | Http请求的资源名称，不包含query string部分，如 ```/logset``` |
| FormatedParameters | Http请求query string部分参数序列化的字符串，即 q-url-param-list中指定的参数，若无指定，则使用空字符串。key 和 value 以```=```连接，不同键值对以```&``` 连接， 需要以字典序排列，key为小写字母，value需要做urlencode |
| FormatedHeaders    | Http请求的header，即q-header-list中指定的Http头部，如无指定，则使用空字符串，key 和 value 以```=```连接，不同键值对以```&``` 连接， 需要以字典序排列，key为小写字母，value需要做urlencode |

#### 2. 拼接 StringToSign

StringToSign 由 q-sign-algorithm, q-sign-time，HttpRequestInfo的sha1哈希值 组成，具体方式如下：
```
StringToSign = q-sign-algorithm + "\n"
             + q-sign-time + "\n"
             + sha1(HttpRequestInfo) + "\n"
```

上述中的 ```\n``` 表示换行转义字符， ```+``` 表示字符串连接操作，其他参数上面已经描述过，其中 HttpRequestInfo的 sha1 哈希值为 16进制的小写字符串。

#### 3. 生成 SignKey
目前，API 只支持一种数字签名算法，即默认签名算法 hmac-sha1。 其伪代码如下：
```
SignKey = Hexdigest(HMAC-SHA1(q-key-time, SecretKey))
```
其中```HMAC-SHA1```为加密算法，```Hexdigest```为转换为16进制字符串的方法。有些语言的 加密算法输出结果直接为16进制字符串，则无需转换。

#### 4. 生成 Signature
目前，API 只支持一种数字签名算法，即默认签名算法 hmac-sha1。 其伪代码如下：
```
Signature = Hexdigest(HMAC-SHA1(StringToSign, SignKey))
```
其中```HMAC-SHA1```为加密算法，```Hexdigest```为转换为16进制字符串的方法。有些语言的 加密算法输出结果直接为16进制字符串，则无需转换。


## 示例

使用如下 SecretId 和 SecretKey 进行签名说明：
```
SecretId = "AKIDc9YlmrBcFk4C8sbmXQ8i65XXXXXXXXXX"
SecretKey = "LUSE4nPK1d4tX5SHyXv6tZXXXXXXXXXX"

StartTime = 1510109254
EndTime = 1510109314
```

### 示例一

获取logset信息，HTTP请求如下：

```
GET /logset?logset_name=testset HTTP/1.1
Host: ap-shanghai.cls.myqcloud.com

```

对如上请求，请求头Host如果加入签名则生成的字符串 HttpRequestInfo 为：
```
get\n/logset\nlogset_name=testset\nhost=ap-shanghai.cls.myqcloud.com\n
```

根据 HttpRequestInfo 组成签名原串 StringToSign 为：
```
sha1\n1510109254;1510109314\n74713a7e01250b81424dac21dced038ee5b8054d\n
```

使用 SecretKey 对 q-key-time 进行加密，得到 SignKey 为：
```
a4501294d3a835f8dab6caf5c19837dd19eef357
```

使用 SignKey 对 StringToSign 进行加密，生成 Signature：
```
42a7a1d1b44f14ae39a5e7fc3172feec6a08b197
```

拼接最后的签名 Authorization 为：
```
q-sign-algorithm=sha1&q-ak=AKIDc9YlmrBcFk4C8sbmXQ8i65XXXXXXXXXX&q-sign-time=1510109254;1510109314&q-key-time=1510109254;1510109314&q-header-list=host&q-url-param-list=logset_name&q-signature=42a7a1d1b44f14ae39a5e7fc3172feec6a08b197
```

最终的请求内容为：
```
GET /logset?logset_name=testset HTTP/1.1
Host: ap-shanghai.cls.myqcloud.com
Authorization: q-sign-algorithm=sha1&q-ak=AKIDc9YlmrBcFk4C8sbmXQ8i65XXXXXXXXXX&q-sign-time=1510109254;1510109314&q-key-time=1510109254;1510109314&q-header-list=host&q-url-param-list=logset_name&q-signature=42a7a1d1b44f14ae39a5e7fc3172feec6a08b197

```

### 示例二

修改logset信息，HTTP请求如下：

```
PUT /logset HTTP/1.1
Host: ap-shanghai.cls.myqcloud.com
Content-Type: application/json
Content-Length: 50

{"logset_id":"xxxx-xx-xx-xx-xxxxxxxx","period":30}
```

其中对body的内容计算md5值为：
```
f9c7fc33c7eab68dfa8a52508d1f4659
```

对如上请求，请求头Host如果加入签名则生成的字符串 HttpRequestInfo 为：
```
put\n/logset\n\ncontent-md5=f9c7fc33c7eab68dfa8a52508d1f4659&content-type=application%2Fjson&host=ap-shanghai.cls.myqcloud.com\n
```

根据 HttpRequestInfo 组成签名原串 StringToSign 为：
```
sha1\n1510109254;1510109314\n0ca0242c3d50441fda6aa234d31bea7a7a12a1ea\n
```

使用 SecretKey 对 q-key-time 进行加密，得到 SignKey 为：
```
a4501294d3a835f8dab6caf5c19837dd19eef357
```

使用 SignKey 对 StringToSign 进行加密，生成 Signature：
```
85a55e61de42483ba03bffd07a6c01b8d651af51
```

拼接最后的签名 Authorization 为：
```
q-sign-algorithm=sha1&q-ak=AKIDc9YlmrBcFk4C8sbmXQ8i65XXXXXXXXXX&q-sign-time=1510109254;1510109314&q-key-time=1510109254;1510109314&q-header-list=content-md5;content-type;host&q-url-param-list=&q-signature=85a55e61de42483ba03bffd07a6c01b8d651af51
```

最终的请求内容为：
```
PUT /logset HTTP/1.1
Host: ap-shanghai.cls.myqcloud.com
Content-Type: application/json
Content-MD5: f9c7fc33c7eab68dfa8a52508d1f4659
Content-Length: 50
Authorization: q-sign-algorithm=sha1&q-ak=AKIDc9YlmrBcFk4C8sbmXQ8i65XXXXXXXXXX&q-sign-time=1510109254;1510109314&q-key-time=1510109254;1510109314&q-header-list=content-md5;content-type;host&q-url-param-list=&q-signature=85a55e61de42483ba03bffd07a6c01b8d651af51

{"logset_id":"xxxx-xx-xx-xx-xxxxxxxx","period":30}
```
