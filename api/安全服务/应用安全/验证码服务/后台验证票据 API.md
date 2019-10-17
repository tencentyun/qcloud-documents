## 接口描述
协议：HTTPS
域名：`csec.api.qcloud.com`
接口名：CaptchaCheck
用户输入验证码之后会获取 API 返回的票据，必须将此票据通过本接口进行校验，以确认票据是从安全 API 返回的，否则将可能导致验证码功能被绕过。

## 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见 [公共请求参数](https://cloud.tencent.com/document/product/295/7279) 页面。其中，此接口的 Action 字段为 CaptchaCheck。
<table class="t">
<tbody><tr>
<th> <b>参数名称</b>
</th><th> <b>是否必须</b>
</th><th> <b>类型</b>
</th><th> <b>描述</b>
</th></tr>
<tr>
<td> ticket
</td><td>是
</td><td> String
</td><td>API 返回给用户的票据
</td></tr>
<tr>
<td> captchaType
</td><td>是
</td><td> Int
</td><td> <a href="https://cloud.tencent.com/doc/product/295/6622#2.-.E5.A4.A9.E5.BE.A1.E9.AA.8C.E8.AF.81.E7.A0.81.E7.B1.BB.E5.9E.8B" target="blank">验证码类型</a>
</td></tr>
<td> userIp
</td><td>是
</td><td> String
</td><td> 用户操作来源的外网 IP
</td></tr>
<tr>
<td> accountType
</td><td> 是
</td><td> UInt
</td><td> 用户账号类型
<br> 0：其他账号
<br> 1：QQ 开放帐号
<br> 2：微信开放帐号
<br> 4：手机账号
<br> 6：手机动态码
<br> 7：邮箱账号
</td></tr>
<tr>
<td> appId
</td><td>否，但建议选择
</td><td> String
</td><td> accountType 是 QQ 或微信开放账号时，该参数必填，表示 QQ 或微信分配给给网站或应用的 AppID，用来唯一标识网站或应用
</td></tr>
<tr>
<td> businessId
</td><td> 否
</td><td> UInt
</td><td> 业务 ID，网站或应用在多个业务中使用此服务，通过此 ID 区分统计数据
</td></tr>
<tr>
<td> sceneId
</td><td> 否
</td><td> UInt
</td><td> 场景 ID，网站或应用的业务下有多个场景使用此服务，通过此 ID 区分统计数据
</td></tr>
<tr>
<tr>
<td> uid
</td><td> 否
</td><td> String
</td><td> 用户 ID，accountType 不同对应不同的用户 ID。如果是 QQ 或微信用户则填入对应的 openId
</td></tr>
<td> associateAccount
</td><td> 否
</td><td> String
</td><td> accountType 是 QQ 或微信开放账号时，用于标识 QQ 或微信用户登录后关联业务自身的账号 ID
</td></tr>
<tr>
<td> registerTime
</td><td> 否
</td><td> UInt
</td><td> 注册时间戳，单位秒
</td></tr>
<tr>
<td> xForwardedFor
</td><td> 否
</td><td> String
</td><td> 用户 HTTP 请求中的 x_forward_for
</td></tr>
<tr>
<td> macAddress
</td><td> 否
</td><td> String
</td><td> mac 地址或设备唯一标识
</td></tr>
<tr>
<td> imei
</td><td> 否
</td><td> String
</td><td> 手机设备号
</td></tr>
</td></tr></tbody></table>

## 输出参数
<table class="t">
<tbody><tr>
<th> <b>参数名称</b>
</th><th> <b>类型</b>
</th><th> <b>描述</b>
</th></tr>
<tr>
<td> code
</td><td> Int
</td><td> 公共错误码，0表示成功，其他值表示失败。详见错误码页面的 <a href='https://cloud.tencent.com/document/product/295/7285'>公共错误码</a>
</td></tr>
<tr><td> codeDesc
</td><td> String
</td><td> 业务侧错误码。成功时返回 Success，错误时返回具体业务错误原因。
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> 模块错误信息描述，与接口相关
</td></tr>
</td></tr></tbody></table>

## 示例代码
代码下载： [Java](https://mc.qcloudimg.com/static/archive/91612588f14dd8632dbb044d4a62061c/captcha_iframe_java%281%29.zip)、[PHP](https://mc.qcloudimg.com/static/archive/81a341051425904e44540a986f1a44a6/captcha_iframe_php.zip)、[Python](https://mc.qcloudimg.com/static/archive/caec2d56c3e4560eda138426bfd36492/captcha_iframe_python.zip)
<br> 一个完整的请求需要两类请求参数：公共请求参数和接口请求参数。这里只列出了接口请求参数，并未列出公共请求参数，有关公共请求参数的说明可见 [公共请求参数](https://cloud.tencent.com/document/product/295/7279)。
- **请求示例：**
```
https://csec.api.qcloud.com/v2/index.php?Action=CaptchaCheck
&<公共请求参数>
&ticket=1111
&captchaType=1
&disturbLevel=1
&userIp=127.0.0.1
```
- **响应示例**
```
{
"code":0,
"message":"No Error",
"is_right":0
}
```

