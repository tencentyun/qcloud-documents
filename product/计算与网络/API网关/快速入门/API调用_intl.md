You can call an API after obtaining its secret_id and secret_key and knowing the URL and required parameters.
Whether you use HTTP or HTTPS for API calling, the signature information must be included in the request header. For more information on signature calculation, see [secret_id + secret_key Verification](https://cloud.tencent.com/document/product/628/11819).

The steps are as follows:

## Request

#### Address

<pre><code>http://service-kuy3rwbs-1251762227.ap-guangzhou.apigateway.myqcloud.com/release
//Enter the URL of the API service to be called
</code></pre>

#### Method

<pre><code>POST
</code></pre>

#### Request body
<pre><code>QueryParam_a=value1&QueryParam_b=value2
</code></pre>

#### Request header
<pre><code>Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: zh-cn
Connection: Keep-Alive
Host: service-kuy3rwbs-1251762227.ap-guangzhou.apigateway.myqcloud.com/release
User-Agent: Mozila/4.0(compatible;MSIE5.01;Window NT5.0)
Accept-Encoding: gzip,deflate
Content-Type: application/x-www-form-urlencoded;charset=utf-8
//Request body type, which is set based on the actual request body content.
X-Client-Proto: http
X-Client-Proto-Ver: HTTP/1.1
X-Real-IP: 163.177.93.244
X-Forwarded-For: 106.19.71.102, 163.177.93.244
Date: Sun, 21 Sep 2017 06:18:21 GMT
Authorization: hmac id="AKIDCgOPWjQ6BAxvHtyckhWABJVYSBj548pN", algorithm="hmac-sha1", headers="Date Host", signature="630c82836582f78b90f293b2f38bda9c"
//Signature. For the specific signature method, see the key calculation method in Verification and Security.
</code></pre>


## Response

#### Response code

<pre><code>200
//Response status code. A value greater than or equal to 200 and less than 300 indicates success; a value greater than or equal to 400 and less than 500 indicates a client error; a value greater than 500 indicates a server error.
</code></pre>

#### Response header

<pre><code>Content-Type: text/html; charset=UTF-8
Content-Length: 122
Date: Sun, 21 Sep 2017 06:46:04 GMT
Server: squid/3.5.20
Connection: close
Set-Cookie:1P_JAR=2017-09-18-06; expires=Mon, 25-Sep-2017 06:46:04 GMT; path=/; domain=.qq.com
X-Secret-ID:AKIDCgOPWjQ6BAxvHtyckhWABJVYSBj548pN
//secret_id in the key pair
X-UsagePlan-ID:Q6BAxvHtyckhWABJVYSBj
//ID of the usage plan bound to the key pair
X-RateLimit-Limit:500
//The traffic limit configuration in the usage plan
X-RateLimit-Used:100/125
//The traffic usage in the usage plan
</code></pre>

