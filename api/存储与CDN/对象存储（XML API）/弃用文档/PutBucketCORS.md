## 功能描述
PUT Bucket cors 接口用来请求设置 Bucket 的跨域资源共享权限，您可以通过传入 XML 格式的配置文件来实现配置，文件大小限制为 64 KB。默认情况下，Bucket 的持有者直接有权限使用该 API 接口，Bucket 持有者也可以将权限授予其他用户。

>**注意：**
>使用 PUT Bucket cors 接口创建的规则权限是覆盖当前的所有规则而不是新增一条权限规则。

## 请求

语法示例：
```
PUT /?cors HTTP/1.1
Host: <Bucketname-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-Length: length
Content-Type: application/xml
Content-MD5: MD5
Authorization: Auth String

<XML 文件>
```
> Authorization: Auth String (详细参见 [访问控制](https://cloud.tencent.com/document/product/436/7778) 章节)

### 请求行
~~~
PUT /?cors HTTP/1.1
~~~ 
该 API 接口接受 PUT 请求。
### 请求头

**公共头部**
该请求操作的实现使用公共请求头，了解公共请求头详细请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 章节。

**非公共头部**
该请求操作的实现需要用帯 Content-MD5 的请求头来验证消息的完整性，具体内容如下：

|名称|描述|类型|必选 |
|:---|:-- |:--|:--|
| Content-MD5 | RFC 1864 中定义的 128位 内容 MD5 算法校验值，用以验证请求体在传输过程中是否有损坏。 | String| 是 |

### 请求体
该请求操作的实现需要有请求体。帯所有节点的请求体内容示例如下：
```
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

具体的数据描述如下：<style  rel="stylesheet"> table th:nth-of-type(1) { width: 200px; }</style>

|节点名称（关键字）|父节点|描述|类型|必选 |
|:---|:-- |:--|:--|:--|
| CORSConfiguration |无| 说明跨域资源共享配置的所有信息，最多可以包含100条 CORSRule | Container | 是 |

Container 节点 CORSConfiguration 的内容：

|节点名称（关键字）|父节点|描述|类型|必选 |
|:---|:-- |:--|:--|:--|
| CORSRule | CORSConfiguration | 说明单条配置的信息 |  Container | 是 |

Container 节点 CORSRule 的内容：

|节点名称（关键字）|父节点|描述|类型| 必选 |
|:---|:-- |:--|:--|:--|
| ID | CORSConfiguration.CORSRule | 配置规则的 ID，可选填|  String |否 |
| AllowedOrigin | CORSConfiguration.CORSRule | 允许的访问来源，支持通配符 *  <br/>格式为：协议://域名[:端口]如：`http://www.qq.com`|  String |是 |
| AllowedMethod | CORSConfiguration.CORSRule | 允许的 HTTP 操作，枚举值：GET，PUT，HEAD，POST，DELETE | Enum |是 |
| AllowedHeader | CORSConfiguration.CORSRule | 在发送 OPTIONS 请求时告知服务端，接下来的请求可以使用哪些自定义的 HTTP 请求头部，支持通配符 * |String |否 |
| MaxAgeSeconds | CORSConfiguration.CORSRule | 设置 OPTIONS 请求得到结果的有效期 | Integer |否 |
| ExposeHeader | CORSConfiguration.CORSRule | 设置浏览器可以接收到的来自服务器端的自定义头部信息 | String |否 |


## 响应

### 响应头
#### 公共响应头
该响应使用公共响应头,了解公共响应头详细请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 章节。
#### 特有响应头
该响应无特殊的响应头。
### 响应体
该响应体返回为空。

## 实际案例

### 请求
```
PUT /?cors HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Mar 2017 09:45:46 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484814927;32557710927&q-key-time=1484814927;32557710927&q-header-list=host&q-url-param-list=cors&q-signature=8b9f05dabce2578f3a79d732386e7cbade9033e3
Content-Type: application/xml
Content-Length: 280

<CORSConfiguration>
  <CORSRule>
    <ID>1234</ID>
    <AllowedOrigin>http://www.qq.com</AllowedOrigin>
    <AllowedMethod>PUT</AllowedMethod>
    <AllowedHeader>x-cos-meta-test</AllowedHeader>
    <MaxAgeSeconds>500</MaxAgeSeconds>
    <ExposeHeader>x-cos-meta-test1</ExposeHeader>
  </CORSRule>
</CORSConfiguration>
```

### 响应
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Fri, 10 Mar 2017 09:45:46 GMT
Server: tencent-cos
x-cos-request-id: NTg4MDdiZWRfOWExZjRlXzQ2OWVfZGY0

```

