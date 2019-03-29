## 1. 接口描述
登录保护接口提供恶意登录识别、撞库行为识别等能力，根据用户的账号、信用和登录行为来源判断当次登录的恶意等级。
协议：HTTPS
域名：csec.api.qcloud.com
接口名：LoginProtection

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见 [公共请求参数](https://cloud.tencent.com/document/product/295/7279) 页面。其中，此接口的 Action 字段为 LoginProtection。

| 参数名称           | 是否必选 | 类型 | 描述                                  |
| ------------------ | -------- | ------ | ---------------------------------------- |
| loginIp            | 是        | String | 登录来源的外网 IP                               |
| loginTime          | 是        | UInt   | 登录时间戳，单位：秒                               |
| accountType        | 是        | UInt   | 用户账号类型（QQ 开放帐号、微信开放账号需要提交 [工单](https://console.cloud.tencent.com/workorder/category)由腾讯云进行资格审核）<br>1：QQ 开放帐号<br>2：微信开放账号<br>4：手机号<br>0：其他<br>10004：手机号 MD5 |
| uid                | 是        | String | 用户 ID 不同 accountType 对应不同的用户 ID。如果是 QQ 或微信用户则填入对应的 openId |
| appId              | 否        | String | accountType 是 QQ 或微信开放账号时，该参数必填，表示 QQ 或微信分配给给网站或应用的 appId，用来唯一标识网站或应用 |
| associateAccount   | 否        | String | accountType 是 QQ 或微信开放账号时，用于标识 QQ 或微信用户登录后关联业务自身的账号 ID |
| nickName           | 否        | String | 昵称，UTF-8 编码                              |
| phoneNumber        | 否        | String | 手机号；国家代码-手机号，如 0086-15912345687（0086前不需要+号） |
| emailAddress       | 否        | String | 用户邮箱地址（非系统自动生成）                          |
| registerTime       | 否        | UInt   | 注册时间戳，单位：秒                               |
| registerIp         | 否        | String | 注册来源的外网 IP                               |
| address       | 否        | String | 地址   |
| cookieHash         | 否        | String | 用户 HTTP 请求中的 cookie 进行2次 hash 的值，只要保证相同 cookie 的 hash 值一致即可 |
| loginSource        | 否        | UInt   | 登录来源<br>0：其他<br>1：PC 网页<br>2：移动页面<br>3：App<br>4：微信公众号   |
| loginType          | 否        | UInt   | 登录方式<br>0：其他<br>1：手动帐号密码输入<br>2：动态短信密码登录<br>3：二维码扫描登录 |
| referer            | 否        | String | 用户 HTTP 请求的 referer 值                    |
| jumpUrl            | 否        | String | 登录成功后跳转页面                                |
| userAgent          | 否        | String | 用户 HTTP 请求的 userAgent                    |
| xForwardedFor      | 否        | String | 用户 HTTP 请求中的 x_forward_for               |
| mouseClickCount    | 否        | UInt   | 用户操作过程中鼠标单击次数                            |
| keyboardClickCount | 否        | UInt   | 用户操作过程中键盘单击次数                            |
| result             | 否        | UInt   | 登录结果<br>0：失败<br>1：成功                           |
| reason             | 否        | UInt   | 失败原因<br>0：其他<br>1：帐号不存在<br>2：密码错误<br>3：参数错误 未按要求填写数据<br>4：验证错误 |
| loginSpend         | 否        | UInt   | 登录耗时，单位：秒                                |
| macAddress         | 否        | String | mac 地址或设备唯一标识                             |
| vendorId           | 否        | String | 手机制造商 ID，如果手机注册，请带上此信息                   |
| appVersion         | 否        | String | App 客户端版本                                |
| imei               | 否        | String | 手机设备号                                    |
| businessId         | 否        | UInt   | 业务 ID 网站或应用在多个业务中使用此服务，通过此 ID 区分统计数据     |

## 3. 输出参数

| 参数名称         | 类型 | 描述                                   |
| ---------------- | ------ | ---------------------------------------- |
| code             | Int    | 公共错误码，0表示成功，其他值表示失败。详情请参见错误码页面的 [公共错误码](https://cloud.tencent.com/document/product/295/7285) |
| codeDesc         | String | 业务侧错误码。成功时返回 Success，错误时返回具体业务错误原因       |
| message          | String | 模块错误信息描述，与接口相关                           |
| Nonce            | UInt   | 随机正整数，与 Timestamp 联合起来, 用于防止重放攻击（公共参数）   |
| loginIp          | String | 登录 IP                                    |
| loginTime        | String | 登录时间                                     |
| uid              | String | 用户 ID，accountType 不同对应不同的用户 ID。如果是 QQ 或微信用户则填入对应的 openId |
| associateAccount | String | accountType 是 QQ 或微信开放账号时，用于标识 QQ 或微信用户登录后关联业务自身的账号 ID |
| level            | Int    | 0：表示无恶意<br>1 - 4：恶意等级由低到高                    |
| riskType         | Array  | 风险类型                                     |

riskType 详细说明
<table >
<tbody><tr>
<th height="23"> <b>风险类型</b>
</th><th> <b>风险详情</b>
</th><th> <b>风险码</b>
</th></tr>
<tr>
<td rowspan="5">账号风险 </td>
<td>帐号信用低<br></td><td>1</td></tr><tr>
<td>垃圾帐号<br></td><td>2</td></tr><tr>
<td>无效帐号<br></td><td>3</td></tr><tr>
<td>黑名单<br></td><td>4</td></tr><tr>
<td>业务白名单<br></td><td>5</td></tr><tr>
</tr>
<td rowspan="2">行为风险</td>
<td>批量操作<br></td><td>101</td></tr><tr>
<td>自动机<br></td><td>102</td></tr><tr>
</tr>
<td rowspan="4">环境风险</td>
<td>环境异常<br></td><td>201</td></tr><tr>
<td>js 上报异常<br></td><td>202</td></tr><tr>
<td>撞库<br></td><td>203</td></tr><tr>
<td>非公网有效 IP<br></td><td>205</td></tr><tr>
</tr>
</td></tr></tbody></table>

## 4. 示例代码
代码下载：  [Python 示例](https://mc.qcloudimg.com/static/archive/de08cb326ab99b568664b2bb7c269f4e/LoginProtection.py.zip)、 [PHP 示例](https://mc.qcloudimg.com/static/archive/2a728e6e88889ae9082d596288505cfd/LoginProtection.php.zip)、 [Java 示例](https://mc.qcloudimg.com/static/archive/db5e010d2ab0070fe8b4f08e3a71238b/LoginProtection.java.zip) 、[.Net 示例](https://mc.qcloudimg.com/static/archive/8773908b78df5570f45d3b2a7d25cbfc/LoginProtection.cs.zip)。
一个完整的请求需要两类请求参数：公共请求参数和接口请求参数。本文只列出了接口请求参数，并未列出公共请求参数，有关公共请求参数的更多说明，请参见 [公共请求参数](https://cloud.tencent.com/document/product/295/7279)。

**请求示例:**
```
https://csec.api.qcloud.com/v2/index.php?
Action=LoginProtection
&<公共请求参数>
&secretId=AKIDmQtAxYTAB2iBS8s2DCzazCD2g7OUq4Zw
&accountType=1
&uid=D692D87319F2098C3877C3904B304706
&loginIp=127.0.0.1
&loginTime=11254
&associateAccount="SpFsjpyvaJ27329"
```

**响应示例:**
```
{
"code": 0,
"message": "No Error",
"level": 0,
"loginIp": "121.14.96.121",
"loginTime": 1436673889,
"uid": "00000000000000000000000033121475",
"associateAccount": "SpFsjpyvaJ27329"
}　
```
