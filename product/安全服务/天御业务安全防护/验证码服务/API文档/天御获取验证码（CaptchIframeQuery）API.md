## 1.接口描述
协议：HTTPS 
<br> 域名：csec.api.qcloud.com 
<br> 接口名: CaptchaIframeQuery  
获取验证码的JavaScript连接，通过将验证码的JavaScript嵌入页面实现验证码的刷新和验证操作。

## 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见[公共请求参数页面](https://www.qcloud.com/doc/api/254/1778)。<br> 其中，此接口的Action字段为CaptchaIframeQuery。
<table class="t">
<tbody><tr>
<th> <b>参数名称</b>
</th><th> <b>是否必须</b>
</th><th> <b>类型</b>
</th><th> <b>描述</b>
</th></tr>
<tr>
<td> captchaType
</td><td> <font color=red>  必选 </font>
</td><td> UInt
</td><td>
<a href="https://www.qcloud.com/doc/product/295/6622#2.-.E5.A4.A9.E5.BE.A1.E9.AA.8C.E8.AF.81.E7.A0.81.E7.B1.BB.E5.9E.8B" target="blank">验证码类型</a>
</td></tr>
<tr>
<td> disturbLevel
</td><td> <font color=red>  必选 </font>
</td><td> UInt
</td><td><a href="https://www.qcloud.com/doc/api/254/%E9%AA%8C%E8%AF%81%E7%A0%81%E7%B1%BB%E5%9E%8B%E8%AF%B4%E6%98%8E" target="blank">验证码干扰程度</a>
</td></tr>
<tr>
<td> isHttps
</td><td> <font color=red>  必选 </font>
</td><td> UInt
</td><td> 返回的JavaScript中是否使用HTTPS
<br> 0：HTTP
<br> 1：HTTPS
</td></tr>
<tr>
<td> clientType
</td><td> <font color=red>  必选 </font>
</td><td> UInt
</td><td> 客户端类型
<br> 1：手机Web页面
<br> 2：PCWeb页面
<br> 3：APP
</td></tr>
<tr>
<td> accountType
</td><td> <font color=red>  必选 </font>
</td><td> UInt
</td><td> 用户账号类型
<br> 0：其他账号
<br> 1：QQ开放帐号
<br> 2：微信开放帐号
<br> 4：手机账号
<br> 6：手机动态码
<br> 7：邮箱账号
</td></tr>
<td> appId
</td><td> 建议
</td><td> String
</td><td> accountType是QQ或微信开放账号时，该参数必填，表示QQ或微信分配给给网站或应用的appId，用来唯一标识网站或应用
</td></tr>
<tr>
<tr>
<td> uid
</td><td> 建议
</td><td> String
</td><td> 用户IDaccountType不同对应不同的用户ID。如果是QQ或微信用户则填入对应的openId
</td></tr>
<tr>
<td> businessId
</td><td> 建议
</td><td> UInt
</td><td> 业务ID
<br> 网站或应用在多个业务中使用此服务，通过此ID区分统计数据
</td></tr>
<tr>
<td> registerTime
</td><td> 可选
</td><td> UInt
</td><td> 注册时间戳，单位秒
</td></tr>
<tr>
<tr>
<td> userIp
</td><td> 可选
</td><td> String
</td><td> 用户操作来源的外网IP
</td></tr>
<tr>
<td> xForwardedFor
</td><td> 可选
</td><td> String
</td><td> 用户Http请求中的x_forward_for
</td></tr>
<tr>
<td> macAddress
</td><td> 可选
</td><td> String
</td><td> mac地址或设备唯一标识
</td></tr>
<tr>
<td> imei
</td><td> 可选
</td><td> String
</td><td> 手机设备号
</td></tr>
<td> associateAccount
</td><td> 可选
</td><td> String
</td><td> accountType是QQ或微信开放账号时，用于标识QQ或微信用户登录后关联业务自身的账号ID
</td></tr>
<td> sceneId
</td><td> 可选
</td><td> UInt
</td><td> 场景ID
<br> 网站或应用的业务下有多个场景使用此服务，通过此ID区分统计数据
</td></tr>
</td></tr></tbody></table>

## 3. 输出参数
<table class="t">
<tbody><tr>
<th> <b>参数名称</b>
</th><th> <b>类型</b>
</th><th> <b>描述</b>
</th></tr>
<tr>
<td> url
</td><td> String
</td><td> 验证码JavaScript地址，该链接单次有效
</td></tr></tbody></table>

## 4.示例代码
代码下载： [java](https://tianyu.qcloud.com/sdk/download/Captcha/java/iframe)  　 [Python](https://tianyu.qcloud.com/sdk/download/Captcha/python/iframe) 　[ php ](https://tianyu.qcloud.com/sdk/download/Captcha/php/iframe) 
<p> 一个完整的请求需要两类请求参数：公共请求参数和接口请求参数。这里只列出了接口请求参数，并未列出公共请求参数，有关公共请求参数的说明可见[公共请求参数](https://www.qcloud.com/doc/api/254/1778)小节。
<br> 请求示例 ：
<br> https://csec.api.qcloud.com/v2/index.php?Action=CaptchaIframeQuery
<br> &<公共请求参数>
<br> &secretId=AKIDmQtAxYTAB2iBS8s2DCzazCD2g7OUq4Zw
<br> &captchaType=1
<br> &disturbLevel=1
<br> &isHttps=1
<br> &clientType=1

## 5.响应示例
{
<br> "code":0,
<br> "message":"No Error",
<br>"url":"https://captcha.guard.qcloud.com/template/TCapIframeApi.js?appid=1251001047&clientype=1&lang=2052&asig=-DhJtUkDwLzJpmIfAmasXFn1Y6zCkRQUn8WERrs4lVNmUDcuoDiYYLmoKqd-Ev77Eogpq97Dpb69_MrwGjWXKmTGg9y9iW7wjdriTu_y6WBN4qGsHn6VRk0W1hLB6ZWvqHqw2E5IFCRUcGrHBzMF7A**"
<br> }

## 6.错误代码说明
参考返回的message字段描述