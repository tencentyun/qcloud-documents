## 1. 接口描述
活动防刷接口提供抢券、红包分发、游戏道具、刷榜等活动中用户恶意行为判断能力，可根据当前用户的账号、信用、行为判断用户当前操作的恶意等级。
协议：HTTPS
域名：csec.api.qcloud.com
接口名：ActivityAntiRush

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见 [公共请求参数](https://cloud.tencent.com/document/product/295/7279 ) 页面。其中，此接口的 Action 字段为 ActivityAntiRush。
<table>
<tbody><tr>
<th> <b>参数名称</b>
</th><th> <b>是否必选</b>
</th><th> <b>类型</b>
</th><th> <b>描述</b>
</th></tr>
<tr>
<td> accountType
</td><td>是
</td><td> UInt
</td><td> 用户账号类型（QQ 开放帐号、微信开放账号需要提交 <a href='https://console.cloud.tencent.com/workorder/category'>工单</a> 由腾讯云进行资格审核） 
<br> 1：QQ 开放帐号
<br> 2：微信开放账号
<br> 4：手机号
<br> 0：其他
<br> 10004： 手机号 MD5
</td></tr>
<tr>
<td> uid
</td><td>是
</td><td> String
</td><td> 用户 ID
<br>不同 accountType 对应不同的用户 ID。如果是 QQ 或微信用户，则填入对应的 openid；若是手机号，则填入对应的手机号（如 15912345687）
</td></tr>
<tr>
<td> userIp
</td><td>是
</td><td> String
</td><td> 用户的外网 IP
</td></tr>
<tr>
<td> postTime
</td><td>是
</td><td> UInt
</td><td> 用户操作时间戳，单位：秒（格林威治时间精确到秒，如1501590972）
</td></tr>
<tr>
<td> appId
</td><td> 否
</td><td> String
</td><td> accountType 是 QQ 或微信开放账号时，该参数必填，表示 QQ 或微信分配给给网站或应用的 appId，用来唯一标识网站或应用
</td></tr>
<tr>
<td> associateAccount
</td><td> 否
</td><td> String
</td><td> accountType 是 QQ 或微信开放账号时，用于标识 QQ 或微信用户登录后关联业务自身的账号 ID
</td></tr>
<tr>
<tr>
<td> nickName
</td><td> 否
</td><td> String
</td><td> 昵称，UTF-8 编码
</td></tr>
<td> phoneNumber
</td><td> 否
</td><td> String
</td><td> 手机号。若 accountType 选 4（手机号）、或10004（手机号 MD5），则无需重复填写。否则填入对应的手机号（如 15912345687）
</td></tr>
<tr>
<td> emailAddress
</td><td> 否
</td><td> String
</td><td> 用户邮箱地址（非系统自动生成）
</td></tr>
<tr>
<td> registerTime
</td><td> 否
</td><td> UInt
</td><td> 注册时间戳，单位：秒
</td></tr>
<tr>
<td> registerIp
</td><td> 否
</td><td> String
</td><td> 注册来源的外网 IP
</td></tr>
<tr>
<td> cookieHash
</td><td> 否
</td><td> String
</td><td> 用户 Http 请求中的 cookie 进行 2 次 hash 的值，只要保证相同 cookie 的 hash 值一致即可
</td></tr>
<td> passwordHash
</td><td> 否
</td><td> String
</td><td> 用户密码进行 2 次 hash 的值，只要保证相同密码 hash 值一致即可
</td></tr>
<tr>
<td> loginSource
</td><td> 否
</td><td> UInt
</td><td> 登录来源
<br> 0：其他
<br> 1：PC 网页
<br> 2：移动页面
<br> 3：App
<br> 4：微信公众号
</td></tr>
<tr>
<td> loginType
</td><td> 否
</td><td> UInt
</td><td> 登录方式
<br> 0：其他
<br> 1：手动帐号密码输入
<br> 2：动态短信密码登录
<br> 3：二维码扫描登录
</td></tr>
<tr>
<td> loginSpend
</td><td> 否
</td><td> UInt
</td><td> 登录耗时，单位：秒
</td></tr>
<td> rootId
</td><td> 否
</td><td> String
</td><td> 用户操作的目的 ID
<br> 比如：点赞，该字段就是被点赞的消息 ID，如果是投票，就是被投号码的 ID
</td></tr>
<td> referer
</td><td> 否
</td><td> String
</td><td> 用户 Http 请求的 referer 值
</td></tr>
<td> jumpUrl
</td><td> 否
</td><td> String
</td><td> 登录成功后跳转页面
</td></tr>
<td> userAgent
</td><td> 否
</td><td> String
</td><td> 用户 Http 请求的 userAgent
</td></tr>
<td> xForwardedFor
</td><td> 否
</td><td> String
</td><td> 用户 Http 请求中的 x_forward_for
</td></tr>
<td> mouseClickCount
</td><td> 否
</td><td> UInt
</td><td> 用户操作过程中鼠标单击次数
</td></tr>
<td> keyboardClickCount
</td><td> 否
</td><td> UInt
</td><td> 用户操作过程中键盘单击次数
</td></tr>
<tr>
<td> macAddress
</td><td> 否
</td><td> String
</td><td> mac地址或设备唯一标识
</td></tr>
<tr>
<td> vendorId
</td><td> 否
</td><td> String
</td><td> 手机制造商 ID，如果手机注册，请带上此信息
</td></tr>
<td> imei
</td><td> 否
</td><td> String
</td><td> 手机设备号
</td></tr>
<tr>
<td> appVersion
</td><td> 否
</td><td> String
</td><td> APP客户端版本
</td></tr>
<tr>
<td> businessId
</td><td> 否
</td><td> UInt
</td><td> 业务 ID
<br> 网站或应用在多个业务中使用此服务，通过此 ID 区分统计数据
</td></tr>
</td></tr></tbody></table>

## 3. 输出参数
<table>
<tbody><tr>
<th> <b>参数名称</b>
</th><th> <b>类型</b>
</th><th> <b>描述</b>
</th></tr>
<tr>
<td> code
</td><td> Int
</td><td> 返回码
</td></tr>
<tr><td> codeDesc
</td><td> String
</td><td> 业务侧错误码。成功时返回 Success，错误时返回具体业务错误原因
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> UTF-8 编码，出错消息
</td></tr>
<tr>
<td> Nonce
</td><td> UInt
</td><td> 随机正整数，与 Timestamp 联合起来, 用于防止重放攻击（公共参数）
</td></tr>
<tr>
<td> associateAccount
</td><td> String
</td><td> accountType 是 QQ 或微信开放账号时，用于标识 QQ 或微信用户登录后关联业务自身的账号 ID
</td></tr>
<tr>
<td> postTime
</td><td> String
</td><td> 操作时间戳，单位：秒
</td></tr>
<td> uid
</td><td> String
</td><td> 用户 ID
<br> accountType 不同对应不同的用户 ID。如果是 QQ 或微信用户则填入对应的 openId
</td></tr>
<td> rootId
</td><td> String
</td><td> 用户操作的目的 ID
<br> 比如：点赞，该字段就是被点 赞的消息 ID，如果是投票，就是被投号码的 ID
</td></tr>
<tr>
<td> userIp
</td><td> String
</td><td> 操作来源的外网 IP
</td></tr>
<tr>
<td> level
</td><td> Int
</td><td> 0：表示无恶意<br>1 - 4：恶意等级由低到高
<tr>
<td> riskType
</td><td> Array
</td><td> 风险类型
</td></tr></tbody></table>

riskType 详细说明
<table >
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
<td>js 上报异常<br></td><td>202</td></tr><tr>
<td>撞库<br></td><td>203</td></tr><tr>
</tr>
</td></tr></tbody></table>

## 4. 示例代码
代码下载：  [Python 示例](https://mc.qcloudimg.com/static/archive/b449f0f6b49fc1c93c274971e4d300a0/ActivityAntiRush.py.zip)、 [PHP 示例](https://mc.qcloudimg.com/static/archive/218a8a04da2a2da7186116a0a820ecdd/ActivityAntiRush.php.zip)、 [Java 示例](https://mc.qcloudimg.com/static/archive/2fc1d9734ee03527df2777417b226882/ActivityAntiRush.java.zip)、 [.Net 示例](https://mc.qcloudimg.com/static/archive/c3a9c8b4f310117e2caa4c644f15a00f/ActivityAntiRush.cs.zip)。
一个完整的请求需要两类请求参数：公共请求参数和接口请求参数。本文只列出了接口请求参数，并未列出公共请求参数，有关公共请求参数的更多说明，请参见 [公共请求参数](https://cloud.tencent.com/document/product/295/7279)。
```
请求示例 ：
<https://csec.api.qcloud.com/v2/index.php?Action=ActivityAntiRush
&<公共请求参数>
&secretId=AKIDmQtAxYTAB2iBS8s2DCzazCD2g7OUq4Zw
&accountType=1
&uid=D692D87319F2098C3877C3904B304706
&userIp=127.0.0.1
&postTime=11254
```

## 5. 响应示例
```
{
"Nonce":516529719,
"associateAccount":"373909726",
"code":0,"
level":1,
"message":"NoError",
"postTime":"11254",
"rootId":"sdsds234sd",
"uid":"D692D87319F2098C3877C3904B304706",
"userIp":"10.23.23.20"
"riskType":[1]
}
```
## 6. 错误码说明
参考返回的 message 字段描述。
