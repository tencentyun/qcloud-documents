## 接口描述
协议：HTTPS
域名：`csec.api.qcloud.com`
接口名：RegisterProtection
## 输入参数
>!以下所有参数在入参时，请正确传参，不能传入空值。

| 参数           | 是否必选 | 参数类型 | 参数描述                                                     |
| ------------------ | --------- | -------- | ----------------------------------------------- |
| registerIp         | 是      | String   | 注册来源的外网 IP。                                            |
| uid                | 是      | String   | 用户 ID 不同的 accountType 对应不同的用户 ID。如果是 QQ，则填入对应的 openid，微信用户则填入对应的 openid/unionid，手机号则填入对应真实用户手机号（如13123456789）。 |
| registerTime       | 是      | UInt     | 注册时间戳，单位：秒。                                         |
| accountType        | 是      | UInt     | 用户账号类型（QQ 开放帐号、微信开放账号需要 [提交工单](https://console.cloud.tencent.com/workorder/category) 由腾讯云进行资格审核）：<li>1：QQ 开放帐号。</li><li>2：微信开放账号。</li><li>4：手机号。</li><li>0：其他。</li><li>10004：手机号 MD5。</li> |
| appId              | 否      | String     | accountType   是 QQ 或微信开放账号时，该参数必填，表示 QQ 或微信分配给网站或应用的 AppID，用来唯一标识网站或应用。 |
| associateAccount   | 否      | String   | accountType   是 QQ 或微信开放账号时，用于标识 QQ 或微信用户登录后关联业务自身的账号 ID。 |
| nickName           | 否      | String   | 昵称，UTF-8 编码。                                             |
| phoneNumber        | 否      | String   | 手机号：国家代码-手机号， 如0086-15912345687（0086前不需要+号）。 |
| emailAddress       | 否      | String   | 用户邮箱地址（非系统自动生成）。                               |
| address            | 否      | String   | 地址。                                                         |
| cookieHash         | 否      | String   | 用户 HTTP 请求中的 cookie 进行2次 hash 的值，只要保证相同 cookie 的 hash 值一致即可。 |
| registerSource     | 否      | String   | 注册来源：<li>0：其他。</li><li>1：PC 网页。</li><li>2：移动页面。</li><li>3：App。</li><li>4：微信公众号。</li> |
| referer            | 否      | String   | 用户 HTTP 请求的 referer 值。                                  |
| jumpUrl            | 否      | String   | 注册成功后跳转页面。                                           |
| userAgent          | 否      | String   | 用户 HTTP 请求的 userAgent。                                   |
| xForwardedFor      | 否      | String   | 用户 HTTP 请求中的 x_forward_for。                             |
| mouseClickCount    | 否      | Uint     | 用户操作过程中鼠标单击次数。                                   |
| keyboardClickCount | 否      | Uint     | 用户操作过程中键盘单击次数。                                   |
| result             | 否      | Uint     | 注册结果：<li>0：失败。</li><li>1：成功。</li>                                 |
| reason             | 否      | Uint     | 失败原因：<li>0：其他。</li><li>1：参数错误。   </li><li>2：帐号冲突。</li><li>3：验证错误。</li>|
| registerSpend      | 否      | Uint     | 登录耗时，单位：秒。                                           |
| macAddress         | 否      | String   | MAC 地址或设备唯一标识。                                        |
| vendorId           | 否      | String   | 手机制造商 ID，如果手机注册，请带上此信息。                    |
| appVersion         | 否      | String   | App 客户端版本。                                               |
| imei               | 否      | String   | 手机设备号。                                                   |
| businessId         | 否      | Uint     | 业务 ID 网站或应用在多个业务中使用此服务，通过此 ID 区分统计数据。 |
| wxSubType          | 否      | Int      | <li>1：微信公众号。</li><li>2：微信小程序。</li>                                |
| randNum            | 否      | String   | Token 签名随机数，微信小程序必填，建议16个字符。                |
| wxToken            | 否      | String   | <li>如果是微信小程序，该字段为以 ssesion_key 为 key 去签名随机数 radnNum 得到的值（hmac_sha256签名算法）。</li><li>如果是微信公众号或第三方登录，则为授权的 access_token（注意：不是普通 access_token，具体看 [微信官方文档](https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1421140842)）。</li> |

## 输出参数

| 参数         | 类型   | 描述                                                         |
| ---------------- | ------ | ------------------------------------------------------------ |
| code             | Int    | 公共错误码：<li>0：成功。</li><li>其他值：失败。</li>详情请参见错误码页面的 [公共错误码](https://cloud.tencent.com/document/product/295/7285)。 |
| codeDesc         | String | 业务侧错误码，成功时返回 Success，错误时返回具体业务错误原因。 |
| message          | String | 模块错误信息描述，与接口相关。                                 |
| Nonce            | UInt   | 随机正整数，与 Timestamp 联合起来, 用于防止重放攻击（公共参数）。 |
| associateAccount | String | accountType 是 QQ 或微信开放账号时，用于标识 QQ 或微信用户登录后关联业务自身的账号 ID。 |
| registerTime     | String | 注册时间戳，单位：秒。                                         |
| uid              | String | 用户 ID 不同的 accountType 对应不同的用户 ID。如果是 QQ，则填入对应的 openid，微信用户则填入对应的 openid/unionid，手机号则填入对应真实用户手机号（如13123456789）。 |
| registerIp       | String | 注册来源的外网 IP。                                            |
| level            | Int    | <li>0：表示无恶意。</li><li>1 - 4：恶意等级由低到高。</li>                     |
| riskType         | Array  | 风险类型，详情请参见下文 **riskType 详细说明**。                                                     |

**riskType 详细说明**
<table>
<tr><th>风险类型</th><th>风险详情</th><th>风险码</th><th>说明</th</tr>
<tr>
<td rowspan=5>账号风险</td>
<td>账号信用低</td><td>1</td><td>账号近期存在因恶意被处罚历史，网络低活跃，被举报等因素。</td>
</tr>
<tr>
<td>垃圾账号</td><td>2</td><td>疑似批量注册小号，近期存在严重违规或大量举报。</td>
</tr>
<tr>
<td>无效账号</td><td>3</td><td>送检账号参数无法成功解析，请检查微信 OpenID 是否有误 。</td>
</tr>
<tr>
<td>黑名单</td><td>4</td><td>该账号在业务侧有过拉黑记录。</td>
</tr>
<tr>
<td>白名单</td><td>5</td><td>业务自行有添加过白名单记录。</td>
</tr>
<tr>
<td rowspan=3>行为风险</td><td>批量操作</td><td>101</td><td>存在 IP/设备/环境等因素的聚集性异常。</td>
</tr>
<tr>
<td>自动机</td><td>102</td><td>疑似自动机批量请求。</td>
</tr>
<tr>
<td>微信登录态无效</td><td>104</td><td>检查 wxtoken 参数，是否已经失效。</td>
</tr>
<tr>
<td rowspan=4>环境风险</td><td>环境异常</td><td>201</td><td>操作 IP/设备/环境存在异常。当前 IP 为非常用 IP 或恶意 IP 段。</td>
</tr>
<tr>
<td>JS 上报异常</td><td>202</td><td>需要用户在前端部署 JS 方有效。</td>
</tr>
<tr>
<td>撞库</td><td>203</td><td>该账号有过“撞库”的历史行为。</td>
</tr>
<tr>
<td>非公网有效 IP</td><td>205</td><td>传进来的 IP 地址为内网 IP 地址或者 IP 保留地址 。</td>
</tr>
</table>

## 示例代码
一个完整的请求需要两类请求参数：公共请求参数和接口请求参数。本文只列出了接口请求参数，并未列出公共请求参数，有关公共请求参数的更多说明，请参见 [公共请求参数](https://cloud.tencent.com/document/product/295/7279)。公共参数传参中不需要添加 SignatureMethod 参数，签名计算默认使用 HmacSHA1 的签名算法，示例代码中有具体实现。
- **请求示例** 
```
<https://csec.api.qcloud.com/v2/index.php?Action=RegisterProtection
&<公共请求参数>
&secretId=AKIDmQtAxYTAB2iBS8s2DCzazCD2g7OUq4Zw
&accountType=1
&uid=D692D87319F2098C3877C3904B304706
&registerIp=127.0.0.1（调用时必须是外网有效ip地址）
&registerTime=1553484280（uinx时间戳，仅需要精确到秒）
&associateAccount="SpFsjpyvaJ27329"
```
- **响应示例**
```
{
    "Nonce": 516529719,
    "associateAccount": "SpFsjpyvaJ27329",
    "code": 0,
    "level ": 1,
    "message": "NoError",
    "registerTime": "1553484280",
    "rootId": "sdsds234sd",
    "uid": "D692D87319F2098C3877C3904B304706",
    "registerIp": "127.0.0.1",
    "riskType": [1]
}
```
- **代码下载** 
 - [Python 示例](https://mc.qcloudimg.com/static/archive/96f7d86723aebd2cd824a93bc405f5aa/RegisterProtection.py.zip)
 -  [PHP 示例](https://mc.qcloudimg.com/static/archive/316eacff388775f02eabf769cced222a/RegisterProtection.php.zip)
 -  [Java 示例](https://mc.qcloudimg.com/static/archive/1d4853fb7b41fc405adf20a9aed47f24/RegisterProtection.java.zip)
 -  [.Net 示例](https://mc.qcloudimg.com/static/archive/c699e43c486a75fadb12dd146a3820c4/RegisterProtection.cs.zip)
