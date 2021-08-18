## 操作场景

该任务指导您使用 JavaScript 语言，通过密钥对鉴权来对您的 API 进行认证管理。

## 操作步骤
1. 在 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1)，创建一个 API，选择鉴权类型为“密钥对鉴权”（参考 [创建 API 概述](https://cloud.tencent.com/document/product/628/11795)）。
2. 将 API 所在服务发布至发布环境（参考 [服务发布与下线](https://cloud.tencent.com/document/product/628/11809)）。
3. 在控制台密钥管理界面创建密钥对。
4. 在控制台使用计划界面创建使用计划，并将使用计划与已创建的密钥对绑定（参考 [使用计划示例](https://cloud.tencent.com/document/product/628/11816)）。
5. 将使用计划与 API 或 API 所在服务进行绑定。
6. 参考 [示例代码](#example)，使用 JavaScript 语言生成签名内容。

## 注意事项
- 最终发送的 HTTP 请求内至少包含两个 Header：Date 和 X-Date 二选一以及 Authorization，可以包含更多 header。如果使用 Date Header，服务端将不会校验时间；如果使用 X-Date Header，服务端将校验时间。
- Date Header 的值为格林威治时间（GMT）格式的 HTTP 请求构造时间，例如 Fri, 09 Oct 2015 00:00:00 GMT。
- X-Date Header 的值为格林威治时间（GMT）格式的 HTTP 请求构造时间，例如 Mon, 19 Mar 2018 12:08:40 GMT。X-Date Header 里的时间和当前时间的差值不能超过15分钟。
- 如果是微服务 API，Header 中需要添加 “X-NameSpace-Code” 和 “X-MicroService-Name” 两个字段，通用 API 不需要添加，Demo 中默认添加了这两个字段。

<span id="example"></span>
## 示例代码
```
/*
used...
<script src="js/vue.js"></script>
<script src="js/axios.js"></script>
<script src="js/qs.js"></script>
<script src="js/crypto-js/crypto-js.js"></script>
*/
var nowDate = new Date(); 

var dateTime = nowDate.toUTCString();
//dateTime = "Mon, 19 Mar 2018 12:00:44 GMT"
var SecretId = 'your SecretId'; // 密钥对的 SecretId
var SecretKey = 'your SecretKey'; // 密钥对的 SecretKey
var source = 'xxxxxx'; // 签名水印值，可填写任意值
var auth = "hmac id=\"" + SecretId + "\", algorithm=\"hmac-sha1\", headers=\"x-date source\", signature=\"";
var signStr = "x-date: " + dateTime + "\n" + "source: " + source;
console.log(signStr)
var sign = CryptoJS.HmacSHA1(signStr, SecretKey)
console.log(sign.toString())
sign = CryptoJS.enc.Base64.stringify(sign)
sign = auth + sign + "\""
console.log(sign)
console.log(dateTime)

var instance = axios.create({
    baseURL: 'http://service-xxxxxxxx-1234567890.ap-guangzhou.apigateway.myqcloud.com/release/api/shoplist', // 用户 API 的访问路径
    timeout: 5000,
    headers: {
                "Source":source,
                "X-Date":dateTime,
                "Authorization":sign
                
                // 如果是微服务 API，Header 中需要添加'X-NameSpace-Code'、'X-MicroService-Name'两个字段，通用 API 不需要添加。
				"X-NameSpace-Code": "testmic",
				"X-MicroService-Name": "provider-demo",
    },
    withCredentials: true
});

instance.get()
.then(function (response) {
        console.log(response);
    })
    .catch(function (error) {
        console.log(error);
    });;
```
