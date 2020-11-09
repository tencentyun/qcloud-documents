## 接口描述
协议：HTTPS GET/POST
域名：`csec.api.qcloud.com`
接口名：ActivityAntiRush

## 输入参数
>!以下所有参数在入参时，请正确传参，不能传入空值。

| 参数           | 是否必选 | 参数类型 | 参数描述                                                     |
| ------------------ | --------- | -------- | ------------------------------------------------------------ |
| accountType        | 是      | Uint     | 用户账号类型（默认开通 QQ 开放账号、手机号，手机 MD5 账号类型查询。如需使用微信开放账号，则需要 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=141&level2_id=645&source=0&data_title=%E6%B4%BB%E5%8A%A8%E9%98%B2%E5%88%B7AA&level3_id=654&radio_title=%E5%BC%80%E9%80%9A%E7%94%B3%E8%AF%B7&queue=1&scene_code=16590&step=2) 由腾讯云进行资格审核，审核通过后方可正常使用微信开放账号）：<li>1：QQ 开放帐号。</li><li>2：微信开放账号。</li><li>4：手机号。</li><li>8：设备号（imei/imeiMD5/idfa/idfaMd5）。</li><li>0：其他。</li><li>10004：手机号 MD5。</li>|
| uid                | 是      | String   | 用户 ID 不同的 accountType 对应不同的用户 ID。如果是 QQ，则填入对应的 openid，微信用户则填入对应的 openid/unionid，手机号则填入对应真实用户手机号（如13123456789）。<br>accountType 为8时，支持 imei、idfa、imeiMD5、idfaMD5 入参。<br>注：imeiMd5 加密方式为：imei 明文小写后，进行 MD5 加密，加密后取小写值。IdfaMd5 加密方式为：idfa 明文大写后，进行 MD5 加密，加密后取小写值。     |
| userIp             | 是      | String   | 用户领取奖励时的真实外网 IP。                                   |
| postTime           | 是      | Uint     | 用户操作时间戳，单位秒（格林威治时间精确到秒，如1501590972）。 |
| appId              | 否      | String   | accountType 是 QQ 开放账号时，该参数必填，表示 QQ 开放平台分配给网站或应用的 AppID，用来唯一标识网站或应用。 |
| nickName           | 否      | String   | 昵称，UTF-8 编码。                                             |
| phoneNumber        | 否      | String   | 手机号。若 accountType 选4（手机号）、或10004（手机号 MD5），则无需重复填写。否则填入对应的手机号（如15912345687）。 |
| emailAddress       | 否      | String   | 用户邮箱地址（非系统自动生成）。                               |
| registerTime       | 否      | Uint     | 注册时间戳，单位：秒。                                         |
| registerIp         | 否      | String     | 注册来源的外网 IP。                                             |
| cookieHash         | 否      | String   | 用户 HTTP 请求中的 cookie 进行2次 hash 的值，只要保证相同 cookie 的 hash 值一致即可。 |
| address            | 否      | String   | 地址。                                                         |
| loginSource        | 否      | UInt     | 登录来源：<li>0：其他。</li><li>1：PC 网页。</li><li>2：移动页面。</li><li>3：App。</li><li>4：微信公众号。</li> |
| loginType          | 否      | UInt     | 登录方式：<li>0：其他。</li><li>1：手动账号密码输入。</li><li>2：动态短信密码登录。</li><li>3：二维码扫描登录。 |
| loginSpend         | 否      | Uint     | 登录耗时，单位：秒。                                           |
| rootId             | 否      | String   | 用户操作的目的 ID，如点赞等，该字段就是被点赞的消息 ID，如果是投票，则为被投号码的 ID。 |
| referer            | 否      | String   | 用户 HTTP 请求的 referer 值。                                  |
| jumpUrl            | 否      | String   | 登录成功后跳转页面。                                           |
| userAgent          | 否      | String   | 用户 HTTP 请求的 userAgent。                                   |
| xForwardedFor      | 否      | String   | 用户 HTTP 请求中的 x_forward_for。                             |
| mouseClickCount    | 否      | Uint     | 用户操作过程中鼠标单击次数。                                   |
| keyboardClickCount | 否      | Uint     | 用户操作过程中键盘单击次数。                                   |
| macAddress         | 否      | String   | MAC 地址或设备唯一标识。                                        |
| vendorId           | 否      | String   | 手机制造商 ID，如果手机注册，请带上此信息。                    |
| imei               | 否      | String   | 手机设备号。                                                   |
| appVersion         | 否      | String   | App 客户端版本。                                                |
| businessId         | 否      | Uint     | 业务 ID 网站或应用在多个业务中使用此服务，通过此 ID 区分统计数据。 |
| wxSubType  | 否      | int      |<li>1：微信公众号。</li><li>2：微信小程序。</li>                                |
| randNum        | 否      | String   | Token 签名随机数，微信小程序必填，建议16个字符。                |
| wxToken       | 否      | String   | <li>wxSubType = 2：微信小程序场景，该字段为以 ssesion_key 为 key 去签名随机数 randNum 得到的值（ hmac_sha256 签名算法）。</li><li>wxSubType = 1：微信公众号或第三方登录，则为授权的 access_token（注意：不是普通 access_token，具体看 [微信官方文档](https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1421140842)），而且获取网页版本的 access_token 时，scope 字段必需填写 snsapi_userinfo。</li> |
| checkDevice  | 否      | Int      | 是否识别设备异常：<li>0：不识别。</li><li>1：识别。</li>                             |

## 输出参数

| 参数         | 类型   | 描述                                                         |
| ---------------- | ------ | ------------------------------------------------------------ |
| code             | Int    | 调用接口返回码，0为正常调用。 |
|codeDesc|String|业务侧错误码，成功时返回 Success，错误时返回具体业务错误原因。|
| message          | String |UTF-8 编码，出错消息。                                 |
| Nonce            | UInt   | 随机正整数，与 Timestamp 联合起来，用于防止重放攻击（公共参数）。 |
| associateAccount | String | accountType 是 QQ 或微信开放账号时，用于标识 QQ 或微信用户登录后关联业务自身的账号 ID。 |
| postTime     | String | 操作时间戳，单位：秒。                                         |
| uid              | String | 用户 ID 不同的 accountType 对应不同的用户 ID。如果是 QQ，则填入对应的 openid，微信用户则填入对应的 openid/unionid，手机号则填入对应真实用户手机号（如13123456789）。 |
| rootId       | String | 用户操作的目的 ID，如点赞等，该字段就是被点赞的消息 ID，如果是投票，就是被投号码的 ID。                                            |
| userIp       | String | 用户操作的真实外网 IP（IP 格式支持 IPv4 与 IPv6）。                                            |
| level            | Int    | <li>0：表示无恶意。</li><li>1 - 4：恶意等级由低到高。</li>                     |
| riskType         | Array  | 风险类型，详情请参见下文 **riskType 详细说明**。                                                     |

**riskType 详细说明：**
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
<td rowspan=2>环境风险</td><td>环境异常</td><td>201</td><td>操作 IP/设备/环境存在异常。当前 IP 为非常用 IP 或恶意 IP 段。</td>
</tr>
<tr>
<td>非公网有效 IP</td><td>205</td><td>传进来的 IP 地址为内网 IP 地址或者 IP 保留地址 。</td>
</tr>
<tr><td >设备风险</td><td>设备异常</td><td>206</td><td>该设备存在异常的使用行为。</td></tr>
</table>

## 示例代码

一个完整的请求需要两类请求参数：公共请求参数和接口请求参数。本文只列出了接口请求参数，并未列出公共请求参数，有关公共请求参数的更多说明，请参见 [公共请求参数](https://cloud.tencent.com/document/product/295/7279)。公共参数传参中不需要添加 SignatureMethod 参数，签名计算默认使用 HmacSHA1 的签名算法，示例代码中有具体实现。
- **请求示例** 
```
<https://csec.api.qcloud.com/v2/index.php?Action=ActivityAntiRush
&<公共请求参数>
&secretId=AKID****************************q4Zw
&accountType=10004
&uid = BFD81********AD31C95CA75E21365973
&userIp=127.0.0.1（调用时必须是外网有效 IP 地址）
&postTime=1553484280（uinx 时间戳，仅需要精确到秒）
```
- **响应示例**
```
{
    "Nonce": 516529719,
    "code": 0,
    "level ": 1,
    "message": "NoError",
    "postTime": "1553484280",
    "uid": "BFD81********AD31C95CA75E21365973",
    "userIp": "127.0.0.1",
    "riskType": [1]
}
```
- **代码下载** 
 - [Python 示例](https://mc.qcloudimg.com/static/archive/b449f0f6b49fc1c93c274971e4d300a0/ActivityAntiRush.py.zip)
 -  [PHP 示例](https://mc.qcloudimg.com/static/archive/218a8a04da2a2da7186116a0a820ecdd/ActivityAntiRush.php.zip)
 -  [Java 示例](https://mc.qcloudimg.com/static/archive/2fc1d9734ee03527df2777417b226882/ActivityAntiRush.java.zip)
 -  [.Net 示例](https://mc.qcloudimg.com/static/archive/c3a9c8b4f310117e2caa4c644f15a00f/ActivityAntiRush.cs.zip)
