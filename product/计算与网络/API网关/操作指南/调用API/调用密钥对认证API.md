## 操作场景
该任务指导您对密钥对认证的 API 发起调用。


## 前提条件
#### 创建密钥对鉴权的API
1. 在 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1)，创建一个 API，选择鉴权类型为“密钥对鉴权”（参考 [创建 API 概述](https://cloud.tencent.com/document/product/628/11795)）。
2. 将 API 所在服务发布至发布环境（参考 [服务发布与下线](https://cloud.tencent.com/document/product/628/11809)）。
3. 在控制台密钥管理界面创建密钥对。
4. 在控制台使用计划界面创建使用计划，并将使用计划与已创建的密钥对绑定（参考 [使用计划示例](https://cloud.tencent.com/document/product/628/11816)）。
5. 将使用计划与 API 或 API 所在服务进行绑定。

#### 确认信息
在发起调用前，您必须拥有所要调用的 API 的 SecretId 和 SecretKey，了解所调用 API 的请求路径、请求方法、请求参数等信息。

#### 工具准备
您可以通过浏览器、浏览器插件、Postman 工具、客户端等来源发起请求，如果是简单验证，建议使用 Postman 工具来发起请求。


## 调用样例
#### 地址
<pre><code>http://service-xxxxxxxx-1234567890.ap-guangzhou.apigateway.myqcloud.com/release
//请填入您所要调用的 API 服务 URL
</code></pre>
URL 拼接规则为：服务路径 + 环境参数 + API path

#### 方法
<pre><code>POST
</code></pre>

#### 请求体
<pre><code>QueryParam_a=value1&QueryParam_b=value2
</code></pre>

#### 请求头
<pre><code>Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: zh-cn
Connection: Keep-Alive
Host: service-xxxxxxxx-1234567890.ap-guangzhou.apigateway.myqcloud.com/release
User-Agent: Mozila/4.0(compatible;MSIE5.01;Window NT5.0)
Accept-Encoding: gzip,deflate
Content-Type: application/x-www-form-urlencoded;charset=utf-8
//请求体类型，请根据实际请求体内容设置。
X-Client-Proto: http
X-Client-Proto-Ver: HTTP/1.1
X-Real-IP: 163.177.93.244
X-Forwarded-For: 106.19.71.102, 163.177.93.244
Date: Sun, 21 Sep 2017 06:18:21 GMT
Authorization: hmac id="AKIDCgXXXXXXXX48pN", algorithm="hmac-sha1", headers="Date Host", signature="630123456789da9c"
//签名，具体签名方法见认证与安全中的密钥计算方法
</code></pre>
- 最终发送的 HTTP 请求内至少包含两个 Header：Date 和 X-Date 二选一以及 Authorization，可以包含更多 header。如果使用 Date Header，服务端将不会校验时间；如果使用 X-Date Header，服务端将校验时间。
- Date Header 的值为格林威治时间（GMT）格式的 HTTP 请求构造时间，例如 Fri, 09 Oct 2015 00:00:00 GMT。
- X-Date Header 的值为格林威治时间（GMT）格式的 HTTP 请求构造时间，例如 Mon, 19 Mar 2018 12:08:40 GMT。X-Date Header 里的时间和当前时间的差值不能超过15分钟。
- Authorization Header的组成可参考 [密钥对认证](https://cloud.tencent.com/document/product/628/11819)，多种语言生成签名的样例可参考 [多种语言生成签名](https://cloud.tencent.com/document/product/628/42189)。


## 响应处理
#### 响应码
| 响应码（code） | 含义 |
|---------|---------|
| 200 ≤ code ＜ 300 | 成功 |
| 300 ≤ code ＜ 400 | 重定向，需要进一步的操作以完成请求 |
| 400 ≤ code ＜ 500 | 客户端错误 |
| code > 500 | 服务端错误 |

#### 响应头
<pre><code>Content-Type: text/html; charset=UTF-8
Content-Length: 122
Date: Sun, 21 Sep 2017 06:46:04 GMT
Server: squid/3.5.20
Connection: close
Set-Cookie:1P_JAR=2017-09-18-06; expires=Mon, 25-Sep-2017 06:46:04 GMT; path=/; domain=.qq.com
X-Secret-ID:AKIDXXXXXXXX48pN
//密钥对中的 secret_id
X-UsagePlan-ID:XXXXXXXX
//密钥对绑定的使用计划 ID
X-RateLimit-Limit:500
//使用计划中的限流配置
X-RateLimit-Used:100/125
//使用计划中的限流使用情况
</code></pre>
