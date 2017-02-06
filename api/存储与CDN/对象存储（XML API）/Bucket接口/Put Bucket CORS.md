## 功能描述
Put Bucket CORS实现跨域访问设置，您可以通过传入XML格式的配置文件实现配置，文件大小限制为64 KB。

## 请求

### 请求语法

```HTTP
PUT /?cors HTTP 1.1
Host:<Bucketname>-<UID>.<Region>.myqcloud.com
Date: date
Content-Length: length
Content-Type:application/xml
Content-MD5:MD5
Authorization: Auth

<XML 文件>
```

### 请求参数

无特殊请求参数

### 请求头部

#### 必选头部

| 名称          | 描述                               | 类型     | 必选   |
| ----------- | -------------------------------- | ------ | ---- |
| Content-MD5 | RFC 1864 中定义的 128位 内容 MD5 算法校验值。 | String | 是    |

### 请求内容

| 名称                | 描述                                       | 类型        | 必选   |
| ----------------- | ---------------------------------------- | --------- | ---- |
| CORSConfiguration | 说明跨域配置的所有信息，最多可以包含100条ORSRule            | Contianer | 是    |
| CORSRule          | 单条配置的信息<br/>父节点：CORSRule                 | Contianer | 是    |
| ID                | 规则名称，可选填<br/>父节点：CORSRule                | String    | 否    |
| AllowedMethod     | 允许的HTTP操作，枚举值：Get，Put，Head，Post，Delete<br/>父节点：CORSRule | Enum      | 是    |
| AllowedOrigin     | 允许的访问来源，支持『*』通配符，协议，端口和域名必须一致<br/>父节点：CORSRule | String    | 是    |
| AllowedHeader     | 在发送 OPTIONS 请求时告知服务端，接下来的请求可以使用哪些自定义的 HTTP 请求头部，支持『*』通配符<br/>父节点：CORSRule | String    | 否    |
| MaxAgeSeconds     | 设置 OPTIONS 请求得到结果的有效期<br/>父节点：CORSRule   | Integer   | 否    |
| ExposeHeadr       | 设置浏览器可以接收到的来自服务器端的自定义头部信息<br/>父节点：CORSRule | String    | 否    |

```xml
<CORSConfiguration>
  <CORSRule>
    <ID></ID>
    <AllowedOrigin></AllowedOrigin>
      ...
    <AllowedMethod></AllowedMethod>
      ...
    <AllowedHeader></AllowedHeader>
      ...
    <MaxAgeSeconds></MaxAgeSeconds>
    <ExposeHeader></ExposeHeader>
      ...
  </CORSRule>
  <CORSRule>
    ...
  </CORSRule>
  ...
</CORSConfiguration>
```

## 返回值

### 返回头部

无特殊返回头部，其他头部请参见公共返回头部

### 返回内容

无返回内容