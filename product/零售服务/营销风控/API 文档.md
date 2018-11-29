## 请求参数

| 参数               | 是否必选     | 类型     | 描述                                       |
| ------------------- | -------- | ------ | ---------------------------------------- |
| accountType         | 是       | Uint   | 用户账号类型<br/>1：QQ 开放帐号<br/>2：微信开放账号<br/>4：手机号 （暂仅支持国内手机号）<br/>10004： 手机号 MD5 |
| uid                 | 是       | String | 用户 ID 值，如微信 / QQ openid，或手机号等（如15912345687） |
| userIP              | 是       | String | 用户领取奖励时的真实外网 IP                           |
| postTime            | 是       | Uint   | 用户操作时间戳，单位：秒（格林威治时间精确到秒，如1501590972）      |
|                     | 是       | String | 所买物品信息                                   |
| EncryptedCode       | 否（建议填写） | String | 领奖码的唯一加密码（请注意信息安全，使用加密码，确保唯一 ID 即可）        |
| Share               | 否（建议填写） | Uint   | 单个红包允许领取的用户数量（分享红包）<br/>例如：<br/>1：单个红包仅支持 1 个用户领取（非分享红包）<br/>2：单个红包可允许 2 个用户领取 |
| Daytimes            | 否（建议填写） | Uint   | 单日内，单个账号每日领取奖励的最大次数                      |
| Totaltimes          | 否（建议填写） | Uint   | 整个活动周期内，单个账号能领取奖励的最大次数                   |
| phoneNumber         | 否（建议填写） | String | 若 accountType 非手机号码， 且能获取到手机号。则填入对应的手机号（如：15912345687） |
| Address             | 否（建议填写） | String | 用户参加活动的地址位置信息。如：可填入用经纬度信息转化为的具体地址信息      |
| Latitude            | 否（建议填写） | Float  | 维度。浮点数，范围为 90~-90                         |
| Longitude           | 否（建议填写） | Float  | 经度。浮点数，范围为 180~-180                       |
| Imei                | 否       | String | 手机设备号                                    |
| referer             | 否       | String | 用户 HTTP 请求的 referer 值                        |
| typeID（内部使用，区分电商 / 快消） | -       | Uint   | 0：传统防刷接口<br/>1：快消、新零售接口                       |
| loginType           | 否       | UInt   | 登录方式<br/> 0：其他<br/> 1：手动帐号密码输入<br/> 2：动态短信密码登录<br/> 3：二维码扫描登录 |
| loginSource         | 否       | UInt   | 登录来源<br/> 0：其他 <br/>1：PC 网页<br/> 2：移动页面 3：App<br/> 4：微信公众号    |

## 响应参数

| 参数              | 类型     | 描述                                       |
| ------------------ | ------ | ---------------------------------------- |
| code               | Int    | 返回码                                      |
| codeDesc           | String | 业务侧错误码<br/>成功：返回 Success<br/>错误：返回具体业务错误原因       |
| message            | String | UTF-8 编码，出错消息                             |
| Nonce              | UInt   | 随机正整数，与 Timestamp 联合起来，用于防止重放攻击（公共参数）   |
| postTime（对应输入参数）  | String | 操作时间戳，单位秒                                |
| uid（对应输入参数）       | String | 不同用户 ID accountType 对应不同的用户 ID<br/>若是 QQ 或微信用户则填入对应的 openId |
| userIp（对应输入参数）    | String | 操作来源的外网IP                                |
| Level（重要：风险值）     | Int    | 0：表示无恶意<br/>1～4：恶意等级由低到高                      |
| riskType（重要：风险标签） | Array  | 风险类型，详情请参见下文 **risktype 详细说明**                               |
| associateAccount   | String | accountType 是 QQ 或微信开放账号时，用于标识 QQ 或微信用户登录后关联业务自身的账号 ID |

## risktype 详细说明

<table>
<tbody>
<tr><th>风险类型</th><th>风险详情</th><th >风险码</th><th >解释说明</th></tr>
<tr>
<td rowspan= '3'>账号风险</td>
<td >账号信用低</td>
<td >1</td>
<td >账号近期存在 因恶意被处罚历史、低活跃、被举报等因素</td>
</tr>
<tr>
<td >垃圾账号</td>
<td >2</td>
<td >疑似批量注册小号、近期存在严重违规或大量举报</td>
</tr>
<tr>
<td >无效账号</td>
<td >3</td>
<td >送检账号参数无法成功解析，若为微信 / QQ openid 请检查是否送检数据错误</td>
</tr>
<tr>
<td rowspan= '3' >行为风险</td>
<td >批量操作</td>
<td >101</td>
<td >存在 IP / 设备 / 环境等因素的聚集性异常</td>
</tr>
<tr>
<td >自动机</td>
<td >102</td>
<td >疑似自动机批量请求</td>
</tr>
<tr>
<td >异常扫码</td>
<td >103</td>
<td >频繁扫码、大量扫废码等异常扫码行为</td>
</tr>
<tr>
<td rowspan= '2' >环境风险</td>
<td >环境异常</td>
<td >201</td>
<td >操作 IP / 设备 / 环境存在异常。如当前 IP 非常用 IP 或恶意 IP 段</td>
</tr>
<tr>
<td >JS 上报异常</td>
<td >202</td>
<td >需用户在前端部署 JS 方有效</td>
</tr>
</tbody>
</table>
