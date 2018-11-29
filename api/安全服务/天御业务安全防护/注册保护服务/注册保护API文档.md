## 1.接口描述
注册保护接口提供恶意注册识别等能力，根据用户账号、信用和注册的行为和来源判断当次注册的恶意等级。

协议：HTTPS

域名：csec.api.qcloud.com

接口名：RegisterProtection

## 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见[公共请求参数](https://cloud.tencent.com/document/product/295/7279)页面。其中，此接口的Action字段为RegisterProtection。
<table class="t">
<tbody><tr>
<th> <b>参数名称</b>
</th><th> <b>是否必须</b>
</th><th> <b>类型</b>
</th><th> <b>描述</b>
</th></tr>
<tr>
<td> registerIp
</td><td><font color="red"> 必选</font color="red">
</td><td> String
</td><td>注册来源的外网IP
</td></tr>
<tr>
<td> uid
</td><td><font color="red"> 必选</font color="red">
</td><td> String
</td><td> 用户ID
<br> accountType不同对应不同的用户ID。如果是QQ或微信用户则填入对应的openId
</td></tr>
<tr>
<td> registerTime
</td><td><font color="red"> 必选</font color="red">
</td><td> UInt
</td><td> 注册时间戳，单位秒
</td></tr>
<tr>
<td> accountType
</td><td><font color="red"> 必选</font color="red">
</td><td> UInt
</td><td> 用户账号类型
<br> 0：其他账号
<br> 1：QQ开放帐号
<br> 2：微信开放帐号
<br> 4：手机号
<br> 6：手机动态码
<br> 7：邮箱
</td></tr>
<tr>
<td> appId
</td><td> 可选
</td><td> String
</td><td> accountType是QQ或微信开放账号时，该参数必填，表示QQ或微信分配给给网站或应用的appId，用来唯一标识网站或应用
</td></tr>
<tr>
<td> associateAccount
</td><td> 可选
</td><td> String
</td><td> accountType是QQ或微信开放账号时，用于标识QQ或微信用户登录后关联业务自身的账号ID
</td></tr>
<tr>
<td> nickName
</td><td> 可选
</td><td> String
</td><td> 昵称，utf8编码
</td></tr>
<tr>
<td> phoneNumber
</td><td> 可选
</td><td> String
</td><td> 手机号；国家代码-手机号， 如0086-15912345687. 注意0086前不需要+号
</td></tr>
<tr>
<td> emailAddress
</td><td> 可选
</td><td> String
</td><td> 用户邮箱地址（非系统自动生成）
</td></tr>
<tr>
<td> passwordHash
</td><td> 可选
</td><td> String
</td><td> 用户密码进行2次hash的值，只要保证相同密码hash值一致即可
</td></tr>
<tr>
<td> cookieHash
</td><td> 可选
</td><td> String
</td><td> 用户Http请求中的cookie进行2次hash的值，只要保证相同cookie的Hash值一致即可
</td></tr>
<tr>
<td> registerSource
</td><td> 可选
</td><td> String
</td><td> 注册来源<br>0：其他<br>1：PC网页<br>2：移动页面<br>3：APP<br>4：微信公众号
</td></tr>
<tr>
<td> referer
</td><td> 可选
</td><td> String
</td><td> 用户Http请求的referer值
</td></tr>
<tr>
<td> jumpUrl
</td><td> 可选
</td><td> String
</td><td> 注册成功后跳转页面
</td></tr>
<tr>
<td> userAgent
</td><td> 可选
</td><td> String
</td><td> 用户Http请求的userAgent
</td></tr>
<tr>
<td> xForwardedFor
</td><td> 可选
</td><td> String
</td><td> 用户Http请求中的x_forward_for
</td></tr>
<tr>
<td> mouseClickCount
</td><td> 可选
</td><td> UInt
</td><td> 用户操作过程中鼠标单击次数
</td></tr>
<tr>
<td> keyboardClickCount
</td><td> 可选
</td><td> UInt
</td><td> 用户操作过程中键盘单击次数
</td></tr>
<tr>
<td> result
</td><td> 可选
</td><td> UInt
</td><td> 注册结果<br>0：失败<br>1：成功
</td></tr>
<tr>
<td> reason
</td><td> 可选
</td><td> UInt
</td><td> 失败原因
<br>0：其他
<br>1：参数错误
<br>2：帐号冲突
<br>3：验证错误
</td></tr>
<tr>
<td> registerSpend
</td><td> 可选
</td><td> UInt
</td><td> 登录耗时，单位秒
</td></tr>
<td> macAddress
</td><td> 可选
</td><td> String
</td><td> mac地址或设备唯一标识
</td></tr>
<tr>
<td> vendorId
</td><td> 可选
</td><td> String
</td><td> 手机制造商ID，如果手机注册，请带上此信息
</td></tr>
<tr>
<td> appVersion
</td><td> 可选
</td><td> String
</td><td> APP客户端版本
</td></tr>
<tr>
<td> imei
</td><td> 可选
</td><td> String
</td><td> 手机设备号
</td></tr>
<td> businessId
</td><td> 可选
</td><td> UInt
</td><td> 业务ID
<br> 网站或应用在多个业务中使用此服务，通过此ID区分统计数据
</td>
<tr>
<td> sceneId
</td><td> 可选
</td><td> UInt
</td><td> 场景ID
<br> 网站或应用的业务下有多个场景使用此服务，通过此ID区分统计数据
</td></tr></tbody></table>

## 3.输出参数
<table class="t">
<tbody><tr>
<th><b>参数名称</b>
</th><th> <b>类型</b>
</th><th> <b>描述</b>
</th></tr>
<td> code
</td><td> Int
</td><td> 公共错误码，0表示成功，其他值表示失败。详见错误码页面的<a href="https://cloud.tencent.com/document/product/295/7285"target="black">公共错误码</a>
</td></tr>
<tr><td> codeDesc
</td><td> String
</td><td> 业务侧错误码。成功时返回Success，错误时返回具体业务错误原因。
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> 模块错误信息描述，与接口相关
</td></tr>
<tr>
<td> Nonce
</td><td> UInt
</td><td> 随机正整数，与 Timestamp 联合起来, 用于防止重放攻击（公共参数）
</td></tr>
<tr>
<td> registerIp
</td><td> String
</td><td> 注册来源的外网IP
</td></tr>
<tr>
<td> registerTime
</td><td> String
</td><td> 注册时间戳，单位秒
</td></tr>
<tr>
<td> uid
</td><td> String
</td><td> 用户ID，accountType不同对应不同的用户ID。如果是QQ或微信用户则填入对应的openId
</td></tr>
<tr>
<td> associateAccount
</td><td> String
</td><td> accountType是QQ或微信开放账号时，用于标识QQ或微信用户登录后关联业务自身的账号ID
</td></tr>
<tr>
<td> level
</td><td> Int
</td><td> 0：表示无恶意<br>1～4：恶意等级由低到高
</td></tr>
<tr>
<td> riskType
</td><td> Array
</td><td> 风险类型
</td></tr>
</tbody></table>

riskType详细说明
<table class="t">
<tbody><tr>
<th height="23"> <b>风险类型</b>
</th><th> <b>风险详情</b>
</th><th> <b>风险码</b>
</th></tr>
<tr>
<td rowspan="4">账号风险 </td>
<td>帐号信用低<br></td><td>1</td></tr><tr>
<td>垃圾帐号<br></td><td>2</td></tr><tr>
<td>无效帐号<br></td><td>3</td></tr><tr>
<td>黑名单<br></td><td>4</td></tr><tr>
</tr>
<td rowspan="2">行为风险</td>
<td>批量操作<br></td><td>101</td></tr><tr>
<td>自动机<br></td><td>102</td></tr><tr>
</tr>
<td rowspan="3">环境风险</td>
<td>环境异常<br></td><td>201</td></tr><tr>
<td>js上报异常<br></td><td>202</td></tr><tr>
<td>撞库<br></td><td>203</td></tr><tr>
</tr>
</td></tr></tbody></table>

## 4.示例代码
代码下载： [Python示例](https://mc.qcloudimg.com/static/archive/96f7d86723aebd2cd824a93bc405f5aa/RegisterProtection.py.zip) [PHP示例](https://mc.qcloudimg.com/static/archive/316eacff388775f02eabf769cced222a/RegisterProtection.php.zip) [Java示例](https://mc.qcloudimg.com/static/archive/1d4853fb7b41fc405adf20a9aed47f24/RegisterProtection.java.zip) [.Net示例](https://mc.qcloudimg.com/static/archive/c699e43c486a75fadb12dd146a3820c4/RegisterProtection.cs.zip)
<br> 一个完整的请求需要两类请求参数：公共请求参数和接口请求参数。这里只列出了接口请求参数，并未列出公共请求参数，有关公共请求参数的说明可见[公共请求参数](https://cloud.tencent.com/document/product/295/7279)小节。
```
请求示例 ：
https://csec.api.qcloud.com/v2/index.php?
Action=RegisterProtection
&<公共请求参数>
&secretId=AKIDmQtAxYTAB2iBS8s2DCzazCD2g7OUq4Zw
&accountType=1
&uid=D692D87319F2098C3877C3904B304706
&registerIp=127.0.0.1
&registerTime=11254
&associateAccount="SpFsjpyvaJ27329"
```

## 5.响应示例
```
{
"code": 0,
"message": "No Error",
"level": 0,
"registerIp": "121.14.96.121",
"registerTime": 1436673889,
"uid": "00000000000000000000000033121475",
"associateAccount": "SpFsjpyvaJ27329"
}
```
