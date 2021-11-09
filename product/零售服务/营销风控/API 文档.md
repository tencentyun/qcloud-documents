

## 接口描述
协议：HTTPS GET/POST
域名：`csec.api.qcloud.com`
接口名：IntelligentQRCode


## 输入参数
>!以下所有参数在入参时，请正确传参，不能传入空值。
<table>
   <tr>
      <th>参数名称</th>
      <th>是否必须</th>
      <th>类型</th>
      <th>描述</th>
   </tr>
   <tr>
      <td>accountType</td>
      <td>必须</td>
      <td>Uint</td>
      <td>用户账号类型（默认开通 QQ 开放账号、手机号，手机 MD5 账号类型查询。如需使用微信开放账号，需要 <a href =https://console.cloud.tencent.com/workorder/category >提交工单</a> 由腾讯云进行资格审核，审核通过后方可正常使用微信开放账号）：<li>1：QQ 开放帐号。</li><li>2：微信开放账号。</li><li>4：手机号。</li><li>8：设备号（imei/imeiMD5/idfa/idfaMd5）。</li><li>0：其他。</li><li>10004：手机号 MD5。</li></td>
   </tr>
   <tr>
      <td>uid</td>
      <td>必须</td>
      <td>String</td>
      <td>用户 ID 不同的 accountType 对应不同的用户 ID。如果是 QQ，则填入对应的 openid，微信用户则填入对应的 openid/unionid，手机号则填入对应真实用户手机号（如13123456789）。<br>accountType 为8时，支持 imei、idfa、imeiMD5、idfaMD5 入参。<br>注：imeiMd5 加密方式为：imei 明文小写后，进行 MD5 加密，加密后取小写值。IdfaMd5 加密方式为：idfa 明文大写后，进行 MD5 加密，加密后取小写值。</td>
   </tr>
   <tr>
      <td>userIp</td>
      <td>必须</td>
      <td>String</td>
      <td>用户领取奖励时的真实外网 IP。</td>
   </tr>
   <tr>
      <td>postTime</td>
      <td>必须</td>
      <td>Uint</td>
      <td>用户操作时间戳，单位秒（格林威治时间精确到秒，如1501590972）。</td>
   </tr>
   <tr>
      <td>appId</td>
      <td>可选</td>
      <td>String</td>
      <td>accountType 是 QQ 开放账号时，该参数必填，表示 QQ 开放平台分配给网站或应用的 AppID，用来唯一标识网站或应用。</td>
   </tr>
   <tr>
      <td>goodInfo</td>
      <td>必须</td>
      <td>String</td>
      <td>所买物品信息。</td>
   </tr>
   <tr>
      <td>encryptedCode</td>
      <td nowrap="nowrap">可选（建议填写）</td>
      <td>String</td>
      <td>领奖码的唯一加密码（请注意信息安全，使用加密码，确保唯一 ID 即可）。</td>
   </tr>
   <tr>
      <td>cookie</td>
      <td>可选</td>
      <td>string</td>
      <td>用户 HTTP 请求中的 cookie 进行2次 hash 的值，只要保证相同 cookie 的 hash 值一致即可。</td>
   </tr>
   <tr>
      <td>share</td>
      <td>可选（建议填写）</td>
      <td>Uint</td>
      <td>单个红包允许领取的用户数量（分享红包）。<br> 例如：<li>1：单个红包仅支持1个用户领取（非分享红包）。</li><li>2：单个红包可允许2个用户领取。</li></td>
   </tr>
   <tr>
      <td>dayTimes</td>
      <td>可选（建议填写）</td>
      <td>Uint</td>
      <td>单日内，单个账号每日领取奖励的最大次数。</td>
   </tr>
   <tr>
      <td>totaltimes</td>
      <td>可选（建议填写）</td>
      <td>Uint</td>
      <td>整个活动周期内，单个账号能领取奖励的最大次数。</td>
   </tr>
   <tr>
      <td>phoneNumber</td>
      <td>可选（建议填写）</td>
      <td>String</td>
      <td>若 accountType 非手机号码， 且能获取到手机号，则填入对应的手机号（如：15912345687）。</td>
   </tr>
   <tr>
      <td>address</td>
      <td>可选（建议填写）</td>
      <td>String</td>
      <td>用户参加活动的地址位置信息，如可填入用经纬度信息转化为的具体地址信息。</td>
   </tr>
   <tr>
      <td>latitude</td>
      <td>可选（建议填写）</td>
      <td>Float</td>
      <td>纬度。浮点数，范围为-90 - 90。</td>
   </tr>
   <tr>
      <td>longitude</td>
      <td>可选（建议填写）</td>
      <td>Float</td>
      <td>经度。浮点数，范围为-180 - 180。</td>
   </tr>
   <tr>
      <td>imei</td>
      <td>可选</td>
      <td>String</td>
      <td>手机设备号。</td>
   </tr>
   <tr>
      <td>referer</td>
      <td>可选</td>
      <td>String</td>
      <td>用户 HTTP 请求的 referer 值。</td>
   </tr>
   <tr>
      <td>loginType</td>
      <td>可选</td>
      <td>UInt</td>
      <td>登录方式：<li> 0：其他。</li><li>1：手动帐号密码输入。</li><li>2：动态短信密码登录。</li><li>3：二维码扫描登录。</li></td>
   </tr>
   <tr>
      <td>loginSource</td>
      <td>可选</td>
      <td>UInt</td>
      <td>登录来源：<li>0：其他 。</li><li>1：PC 网页。</li><li>2：移动页面。</li><li>3：App。</li><li>4：微信公众号。</li></td>
   </tr>
   <tr>
      <td>wxSubType</td>
      <td>可选</td>
      <td>int</td>
      <td><li>1：微信公众号。</li><li>2：微信小程序。</li></td>
   </tr>
   <tr>
      <td>randNum</td>
      <td>可选</td>
      <td>String</td>
      <td>Token 签名随机数，微信小程序必填，建议16个字符。</td>
   </tr>
   <tr>
      <td>wxToken</td>
      <td>可选</td>
      <td>String</td>
      <td><li>如果是微信小程序，该字段为以 ssesion_key 为 key 去签名随机数 randNum 得到的值（hmac_sha256签名算法）。</li><li>如果是微信公众号或第三方登录，则为授权的 access_token（注意：不是普通 access_token，详细请参阅官方 <a href="https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1421140842">说明文档</a>。</li></td>
   </tr>
</table>



## 输出参数
<table>
   <tr>
      <th>参数名称</th>
      <th>类型</th>
      <th>描述</th>
   </tr>
   <tr>
      <td>code</td>
      <td>Int</td>
      <td>返回码。</td>
   </tr>
   <tr>
      <td>codeDesc</td>
      <td>String</td>
      <td>业务侧错误码。成功时返回 Success，错误时返回具体业务错误原因。</td>
   </tr>
   <tr>
      <td>message</td>
      <td>String</td>
      <td>UTF-8 编码，出错消息。</td>
   </tr>
   <tr>
      <td>Nonce</td>
      <td>UInt</td>
      <td>随机正整数，与 Timestamp 联合起来, 用于防止重放攻击（公共参数）。</td>
   </tr>
   <tr>
      <td>postTime</td>
      <td>String</td>
      <td>操作时间戳，单位秒（对应输入参数）。</td>
   </tr>
   <tr>
      <td>uid</td>
      <td>String</td>
      <td>用户 ID 不同的 accountType 对应不同的用户 ID。如果是 QQ，则填入对应的 openid，微信用户则填入对应的 openid/unionid，手机号则填入对应真实用户手机号（如13123456789）。</td>
   </tr>
   <tr>
      <td>userIp</td>
      <td>String</td>
      <td>操作来源的外网 IP（对应输入参数）。</td>
   </tr>
   <tr>
      <td>level</td>
      <td>Int</td>
      <td>风险值：<li>0：表示无恶意。</li><li>1 - 4：恶意等级由低到高。</li></td>
   </tr>
   <tr>
      <td nowrap="nowrap">riskType</td>
      <td>Array</td>
      <td>风险类型，详情请参见下文 riskType 详细说明。</td>
   </tr>
   <tr>
      <td>associateAccount</td>
      <td>String</td>
      <td>accountType 是 QQ 或微信开放账号时，用于标识 QQ 或微信用户登录后关联业务自身的账号 ID。</td>
   </tr>
</table>

## risktype 详细说明
<table>
   <tr>
      <th>风险类型</th>
      <th>风险详情</th>
      <th>风险码</th>
      <th>描述</th>
   </tr>
   <tr>
      <td rowspan="5">账号风险</td>
      <td>账号信用低</td>
      <td>1</td>
      <td>账号近期存在因恶意被处罚历史、低活跃、被举报等因素。</td>
   </tr>
   <tr>
      <td>垃圾账号</td>
      <td>2</td>
      <td>疑似批量注册小号、近期存在严重违规或大量举报。</td>
   </tr>
   <tr>
      <td>无效账号</td>
      <td>3</td>
      <td>送检账号参数无法成功解析，若为微信或 QQ openid，请检查是否送检数据错误。</td>
   </tr>
   <tr>
      <td>黑名单</td>
      <td>4</td>
      <td>业务自行加黑的记录。</td>
   </tr>
   <tr>
      <td>白名单</td>
      <td>5</td>
      <td>业务自行加白的记录。</td>
   </tr>
   <tr>
      <td rowspan="4">行为风险</td>
      <td>批量操作</td>
      <td>101</td>
      <td>存在 IP、设备、环境等因素的聚集性异常。</td>
   </tr>
   <tr>
      <td>自动机</td>
      <td>102</td>
      <td>疑似自动机批量请求。</td>
   </tr>
   <tr>
	  <td>异常扫码</td>
      <td>103</td>
      <td>频繁扫码、大量扫废码等异常扫码行为。</td>
   </tr>
   <tr>
      <td>登录态无效</td>
      <td>104</td>
      <td>检查 wxtoken 参数，是否已经失效。</td>
   </tr>
   <tr>
      <td rowspan="2">环境风险</td>
      <td>环境异常</td>
      <td>201</td>
      <td>操作 IP、设备、环境存在异常。如当前 IP 为非常用 IP 或恶意 IP 段。</td>
   </tr>
   <tr>
      <td>非公网有效 IP</td>
      <td>205</td>
      <td>传进来的 IP 地址为内网 IP 地址，或者为 IP 保留地址。 </td>
   </tr>
 <tr> <td >设备风险</td><td>设备异常</td><td>206</td><td>该设备存在异常的使用行为。</td></tr>
</table>


## 示例代码
代码示例下载： [Python示例](https://main.qcloudimg.com/raw/9db908ac917f1d9202c34089607d63d8/IntelligentQRCode-python.rar) 、[Java示例](https://main.qcloudimg.com/raw/41c42df463a8e2995461e3cf451badf1/IntelligentQRCode-java.rar) 。
一个完整的请求需要两类请求参数：公共请求参数和接口请求参数。本文列出了接口请求参数，未列出公共请求参数，有关公共请求参数的更多说明，请参阅 [公共请求参数](https://cloud.tencent.com/document/product/295/7279) 文档。

### 请求示例
```
https://csec.api.qcloud.com/v2/index.php?
Action=IntelligentQRCode
&<公共请求参数>
&secretId=AKI*****************************q4Zw
&accountType=10004
&cookie = "asdasldkjaslkjdsfjlsad" //用户 HTTP 请求中的 cookie 进行2次 hash 的值
&goodInfo="good"  //业务侧自定义内容
&uid=BF**********AD31C95CA75E21365973
&userIP=127.0.0.1 //调用时必须是外网有效 IP 地址
&postTime=11254 //uinx 时间戳，仅需要精确到秒
&associateAccount="SpFsjpyvaJ27329"
```

### 响应示例
```json
{
	"code": 0,
	"message": "No Error",
	"level": 0,
	"userIP": "127.0.0.1",
	"postTime": 1436673889,
	"uid": "BF**********AD31C95CA75E21365973",
	"associateAccount": "SpFsjpyvaJ27329"
}
```
