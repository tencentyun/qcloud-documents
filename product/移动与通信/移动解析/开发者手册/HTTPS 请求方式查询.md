移动解析 HTTPDNS 的 HTTPS 请求方式查询可以通过 `https://119.29.29.99/d? + {请求参数}` 接口使用移动解析 HTTPDNS 服务。

>? 
>- [开通移动解析 HTTPDNS 服务](https://cloud.tencent.com/document/product/379/54577) 后，您需在移动解析 HTTPDNS 控制台添加解析域名后才可正常使用。具体操作请参见 [添加域名](https://cloud.tencent.com/document/product/379/54588)。
>- HTTP 协议服务地址为 `119.29.29.98`，HTTPS 协议服务地址为 `119.29.29.99`。
>- 新版本 API 更新为使用 `119.29.29.99/98` 接入，同时原移动解析 HTTPDNS 服务地址 `119.29.29.29` 仅供开发调试使用，无 SLA 保障，不建议用于正式业务，请您尽快将正式业务迁移至 `119.29.29.99/98`。


## 前期准备
使用请求接口 `https://119.29.29.99/d? + {请求参数}` 时，需使用以下配置信息。请先前往移动解析 HTTPDNS 管理控制台 [开发配置页](https://console.cloud.tencent.com/httpdns/configure) 获取相关配置信息：
![](https://main.qcloudimg.com/raw/588d4d57fd15c3e801bc0ca036862f2f.png)
**HTTPS 加密 Token**：调⽤移动解析 HTTPDNS 的 HTTPS 解析接口 `https://119.29.29.99` ，对 DNS 请求数据进⾏鉴权的 Token 信息。

## 接口描述
- 接口请求地址：  `https://119.29.29.99/d? + {请求参数}`。
- 请求方式：POST 或 GET。

## 请求参数
<table>
<thead>
  <tr>
    <th>参数名</th>
    <th>参数含义</th>
    <th>是否必选</th>
    <th>取值</th>
    <th>加密</th>
    <th>说明</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>dn</td>
    <td>被查询的域名</td>
    <td>是</td>
    <td>字符串</td>
    <td>否</td>
    <td>需在移动解析 HTTPDNS 控制台已添加域名。具体请参见 <a href="https://cloud.tencent.com/document/product/379/54588">添加域名</a>。</td>
  </tr>
  <tr>
    <td>token</td>
    <td>使用 HTTPS 方式的标识</td>
    <td>是</td>
    <td>整型数据</td>
    <td>否</td>
    <td>token 获取请参见 <a href="https://cloud.tencent.com/document/product/379/61203">配置信息说明</a>。</td>
  </tr>
  <tr>
    <td>ip</td>
    <td>DNS 请求的 ECS（EDNS-Client-Subnet）值</td>
    <td>否</td>
    <td>IPv4/IPv6 地址值</td>
    <td>否</td>
    <td>默认情况下 HTTPDNS 服务器会查询客户端出口 IP 为 DNS 线路查询 IP，使用 “ip=xxx” 参数，可以指定线路 IP 地址。支持 IPv4/IPv6 地址传入，接口会自动识别。</td>
  </tr>
  <tr>
    <td>query</td>
    <td>结果中返回被查询域名</td>
    <td>否</td>
    <td>1</td>
    <td>否</td>
    <td>单域名查询情况下，此参数要求返回结果中携带被查询域名。</td>
  </tr>
  <tr>
    <td>timeout</td>
    <td>超时返回时间</td>
    <td>否</td>
    <td>1000 - 5000，单位为毫秒</td>
    <td>否</td>
    <td>可用值[1000, 5000]，单位为ms，查询超时时间，默认值为5秒。</td>
  </tr>
  <tr>
    <td>ttl</td>
    <td>查询结果是否返回 TTL 值</td>
    <td>否</td>
    <td>1</td>
    <td>否</td>
    <td>可用值 [1]，不携带此参数，默认为不传递TTL值。</td>
  </tr>
  <tr>
    <td>type</td>
    <td>查询类型</td>
    <td>否</td>
    <td>[aaaa/AAAA/addrs/ADDRS]</td>
    <td>否</td>
    <td>可用值[aaaa,AAAA,addrs,ADDRS]。默认查询 A 记录，设置 AAAA/aaaa 查询 AAAA 记录，设置 addrs/ADDRS 同时查询 A 和 AAAA 记录。</td>
  </tr>
  <tr>
    <td>clientip</td>
    <td>查询结果中返回的客户端 IP 地址</td>
    <td>否</td>
    <td>1</td>
    <td>否</td>
    <td>可用值 [1]，不携带此参数，默认为不传递 clientip 值。若此参数取值，则返回结果中地址值在 | 符号后，若携带有 ip 参数，返回的是 ip 参数的值，否则返回客户端地址 IP。</td>
  </tr>
</tbody>
</table>

>?
>- ECS（EDNS-Client-Subnet）协议在 DNS 请求包中附加请求域名解析的用户 IP 地址，DNS 服务器可以根据该地址返回用户更快速访问的服务器 IP 地址。
>- 使用 HTTPS 方式，传输的数据会因为 TLS 通道而被加密保护，因此不需要主动对传入的数据额外加密。
>- 出于安全和身份认证的考虑，需要传入 HTTPS Token 实现身份鉴权。

## 请求说明
以请求域名为 `cloud.tencent.com`，token 为 `yyyy` 为例。

>!
>- 若 HTTPDNS 未查询到解析结果，将返回为空值。
>- HTTP 已接入 BGP Anycast，并实现多地机房容灾，但为了服务质量更高的保障，建议您采用 [Failed over 策略](https://cloud.tencent.com/document/product/379/3523) 进行接入。 

### 请求 A 记录
- **输入示例：**
```
curl "https://119.29.29.99/d?dn=cloud.tencent.com&token=yyyy"
```
- **返回格式：**
```
2.3.3.4;2.3.3.5;2.3.3.6
```
- **格式说明**：返回查询结果，多个结果以 ';' 分隔。


### 返回结果中携带 ttl 信息
- **输入示例：**
```
curl "https://119.29.29.99/d?dn=cloud.tencent.com&token=yyyy&ttl=1"
```
- **返回格式：**
```
2.3.3.4;2.3.3.5;2.3.3.6,120
```
- **格式说明**：返回查询结果，多个结果以 ';' 分隔。记录值与 ttl 值以 ',' 分隔。


### 返回结果携带查询线路 IP 地址
- **输入示例：**
```
curl "https://119.29.29.99/d?dn=cloud.tencent.com&token=yyyy&clientip=1&ip=1.2.3.4&ttl=1"
```
- **返回格式：**
```
12.3.3.4;2.3.3.5;2.3.3.6,120|1.2.3.4
```
- **格式说明**：返回结果中携带线路 ip 地址，以'|'分隔。如果没有传入 “ip=xxx” 参数，则返回出口 IP 地址；否则返回 ip 参数中的地址。

### 同时请求 A 和 AAAA 记录
- **输入示例：**
```
curl "https://119.29.29.99/d?dn=cloud.tencent.com&token=yyyy&clientip=1&ip=1.2.3.4&type=addrs&ttl=1"
```
- **返回格式：**
```
2.3.3.4;2.3.3.5;2.3.3.6,120-2402:4e00:0123:4567:0::2345;2403:4e00:0123:4567:0::2346,120|1.2.3.4
```
- **格式说明**：A 记录和 AAAA 记录之间以 '-' 分隔，A 记录在前，AAAA 记录在后。


### 返回结果中携带被查询域名
- **输入示例：**
```
curl "https://119.29.29.99/d?dn=cloud.tencent.com&token=yyyy&clientip=1&ip=1.2.3.4&query=1&ttl=1"
```
- **返回格式：**
```
cloud.tencent.com.:2.3.3.4;2.3.3.5;2.3.3.6,120|1.2.3.4
```
- **格式说明**：返回格式为 “域名.:结果” 的格式。

### 批量域名请求
- **输入示例：**
```
curl "https://119.29.29.99/d?dn=cloud.tencent.com,www.qq.com,www.dnspod.cn&token=yyyy&clientip=1&ip=1.2.3.4&ttl=1"
```
- **返回格式：**
```
cloud.tencent.com.:2.3.3.4;2.3.3.5;2.3.3.6,120
www.qq.com.:3.3.3.4;3.3.3.5;3.3.3.6,180
www.dnspod.cn.:4.3.3.4;4.3.3.5;4.3.3.6,60|1.2.3.4
```
- **格式说明：**多个域名返回内容之间以 “换行符” 分隔，ip 地址附加在所有记录值的最后。

## 请求异常或无记录说明

### 查询 A 记录
- **输入示例：**
```
curl "https://119.29.29.99/d?dn=cloud.tencent.com&token=yyyy&id=xxx"
```
- **返回格式：** 空。
- **格式说明：** 没有记录，则返回空字符串。

### 返回结果中包含域名
- **输入示例：**
```
curl "https://119.29.29.99/d?dn=cloud.tencent.com&token=yyyy&type=addrs&query=1&ip=1.2.3.4"
```
- **返回格式：**
```
cloud.tencent.com|1.2.3.4
```
- **格式说明：**0表示没有记录。



### 返回 A 与 AAAA 的记录
- **输入示例：**
```
curl "https://119.29.29.99/d?dn=cloud.tencent.com&token=yyyy&type=addrs&query=1&ip=1.2.3.4"
```
- **返回格式：**
```
cloud.tencent.com.:0-0|1.2.3.4
```
- **格式说明：**0表示没有记录。如果某个记录存在，则该记录正常返回在结果中，例如 `cloud.tencent.com.:2.3.4.5;3.3.3.3-0|1.2.3.4`，表示 AAAA 记录无法查询到。


### 批量域名请求
- **输入示例：**
```
curl "https://119.29.29.99/d?dn=cloud.tencent.com,www.qq.com,www.dnspod.cn&token=yyyy&clientip=1&ip=1.2.3.4&ttl=1"
```
- **返回格式**：
```
cloud.tencent.com.:0
www.qq.com.:3.3.3.4;3.3.3.5;3.3.3.6,180
www.dnspod.cn.:4.3.3.4;4.3.3.5;4.3.3.6,60|1.2.3.4
```
- **格式说明：**未查询到数据的域名则返回0。如果某个记录存在，则该记录正常返回在结果中。

## HTTP 状态码
以下为接口业务逻辑相关的 HTTP 状态码。

| 状态码 | 描述|
|---------|---------|
| 200 OK | 如果接口调用正确，无论是否查询成功，均返回状态码200。|
| 404 Not Found | 接口不存在或 URL 实际上访问了某不存在的资源。|
| 429 Too Many Request | 访问过于频繁，超过了服务器限制。|
| 501 Not Implemented | 使用了非 “GET” 或 “POST” 请求方式。|

