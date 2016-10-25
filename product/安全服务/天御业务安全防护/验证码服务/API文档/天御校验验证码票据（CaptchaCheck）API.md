## 1.接口描述
协议：HTTPS
<p> 域名：csec.api.qcloud.com
<p> 接口名: CaptchaCheck
<p> 用户输入验证码之后会获取API返回的票据，必须将此票据通过本接口进行校验，以确认票据是从安全API返回的，否则将可能导致验证码功能被绕过

## 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见公共请求参数页面。其中，此接口的Action字段为CaptchaCheck。
<table class="t">
<tbody><tr>
<th> <b>参数名称</b>
</th><th> <b>是否必须</b>
</th><th> <b>类型</b>
</th><th> <b>描述</b>
</th></tr>
<tr>
<td> ticket
</td><td><font color=red> 是 </font>
</td><td> String
</td><td>API返回给用户的票据
</td></tr>
<tr>
<td> captchaType
</td><td> <font color=red> 是 </font>
</td><td> Int
</td><td> 验证码图片的类型
</td></tr>
<tr>
<td> disturbLevel
</td><td> <font color=red> 是 </font>
</td><td> Int
</td><td> 验证码干扰程度
</td></tr>
<tr>
<td> userIp
</td><td> <font color=red> 是 </font>
</td><td> String
</td><td> 用户操作来源的外网IP
</td></tr>
<tr>
<td> businessId
</td><td> 可选
</td><td> UInt
</td><td> 业务ID，网站或应用在多个业务中使用此服务，通过此ID区分统计数据
</td></tr>
<tr>
<td> sceneId
</td><td> 可选
</td><td> UInt
</td><td> 场景ID，网站或应用的业务下有多个场景使用此服务，通过此ID区分统计数据
</td></tr>
<tr>
<td> accountType
</td><td> 可选
</td><td> UInt
</td><td> 用户账号类型
<br> 0：其他账号
<br> 1：QQ开放帐号
<br> 2：微信开放帐号
<br> 4：手机账号
<br> 6：手机动态码
<br> 7：邮箱账号
</td></tr>
<tr>
<td> appId
</td><td> 可选
</td><td> String
</td><td> accountType是QQ或微信开放账号时，该参数必填，表示QQ或微信分配给给网站或应用的appId，用来唯一标识网站或应用
</td></tr>
<tr>
<tr>
<td> uid
</td><td> 可选
</td><td> String
</td><td> 用户ID，accountType不同对应不同的用户ID。如果是QQ或微信用户则填入对应的openId
</td></tr>
<td> associateAccount
</td><td> 可选
</td><td> String
</td><td> accountType是QQ或微信开放账号时，用于标识QQ或微信用户登录后关联业务自身的账号ID
</td></tr>
<tr>
<td> registerTime
</td><td> 可选
</td><td> UInt
</td><td> 注册时间戳，单位秒
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
</td></tr></tbody></table>

## 3. 输出参数
<table class="t">
<tbody><tr>
<th> <b>参数名称</b>
</th><th> <b>类型</b>
</th><th> <b>描述</b>
</th></tr>
<tr>
<td> code
</td><td> Int
</td><td> 错误码 0: 成功 5100: 验证失败 其他值表示请求失败
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> 错误信息
</td></tr>
</td></tr></tbody></table>

## 4.示例代码
代码下载： java  Python  php 
一个完整的请求需要两类请求参数：公共请求参数和接口请求参数。这里只列出了接口请求参数，并未列出公共请求参数，有关公共请求参数的说明可见公共请求参数小节。
<p> 请求示例 ：
<p> https://csec.api.qcloud.com/v2/index.php?Action=CaptchaCheck
<p> &<公共请求参数>
<p> &ticket=1111
<p> &captchaType=1
<p> &disturbLevel=1
<p> &userIp=127.0.0.1
## 5.响应示例
{
<p> 　　"code":0,
<p>　　 "message":"No Error",
<p> 　　　"is_right":0
<p> }
## 6.错误码说明
参考返回的message字段描述

