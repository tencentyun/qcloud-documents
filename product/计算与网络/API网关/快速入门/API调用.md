当您已经拥有所要调用 API 的 secret_id 和 secret_key，并且了解相关API 的 URL 及所需参数等，即可进行调用。
当您在调用时，无论使用 http 还是 https，都需要在请求头中包含签名信息，有关签名的计算详见 [密钥对计算](https://cloud.tencent.com/document/product/628/11819)。

具体步骤如下：

## 请求

#### 地址

<pre><code>http://service-kuy3rwbs-1251762227.ap-guangzhou.apigateway.myqcloud.com/release
//请填入您所要调用的API服务URL
</code></pre>

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
Host: service-kuy3rwbs-1251762227.ap-guangzhou.apigateway.myqcloud.com/release
User-Agent: Mozila/4.0(compatible;MSIE5.01;Window NT5.0)
Accept-Encoding: gzip,deflate
Content-Type: application/x-www-form-urlencoded;charset=utf-8
//请求体类型，请根据实际请求体内容设置。
X-Client-Proto: http
X-Client-Proto-Ver: HTTP/1.1
X-Real-IP: 163.177.93.244
X-Forwarded-For: 106.19.71.102, 163.177.93.244
Date: Sun, 21 Sep 2017 06:18:21 GMT
Authorization: hmac id="AKIDCgOPWjQ6BAxvHtyckhWABJVYSBj548pN", algorithm="hmac-sha1", headers="Date Host", signature="630c82836582f78b90f293b2f38bda9c"
//签名，具体签名方法见认证与安全中的密钥计算方法
</code></pre>


## 响应

#### 响应码

<pre><code>200
//响应状态码，大于等于 200 小于 300 表示成功；大于等于 400 小于 500 为客户端错误；大于 500 为服务端错误。
</code></pre>

#### 响应头

<pre><code>Content-Type: text/html; charset=UTF-8
Content-Length: 122
Date: Sun, 21 Sep 2017 06:46:04 GMT
Server: squid/3.5.20
Connection: close
Set-Cookie:1P_JAR=2017-09-18-06; expires=Mon, 25-Sep-2017 06:46:04 GMT; path=/; domain=.qq.com
X-Secret-ID:AKIDCgOPWjQ6BAxvHtyckhWABJVYSBj548pN
//密钥对中的secret_id
X-UsagePlan-ID:Q6BAxvHtyckhWABJVYSBj
//密钥对绑定的使用计划id
X-RateLimit-Limit:500
//使用计划中的限流配置
X-RateLimit-Used:100/125
//使用计划中的限流使用情况
</code></pre>
