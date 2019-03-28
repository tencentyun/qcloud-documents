## 接口描述
协议：HTTPS POST
域名：`csec.api.qcloud.com`
接口名：IntelligentQRCode


## 输入参数
|   参数名称    | 是否必须         |  类型  | 描述                                                         |
| :-----------: | :----------------: | :----: | ------------------------------------------------------------ |
|  accountType  | 必须             |  Uint  | 用户账号类型：<br>1：QQ开放帐号<br> 2：微信开放账号 <br>4：手机号 （暂仅支持国内手机号）<br>    10004：   手机号MD5 |
|      uid      | 必须             | String | 用户 ID 值，如微信/QQ openid，或手机号等（如15912345687）     |
|    userIP     | 必须             | String | 用户领取奖励时的真实外网 IP                                   |
|   postTime    | 必须             |  Uint  | 用户操作时间戳，单位秒（格林威治时间精确到秒，如1501590972） |
|     appId     | 可选             | String | accountType 是 QQ 或微信开放账号时，该参数必填，表示 QQ 或微信分配给网站或应用的 appId，用来唯一标识网站或应用 |
|   goodInfo    | 必须             | String | 所买物品信息                                                 |
| encryptedCode | 可选（建议填写） | String | 领奖码的唯一加密码（请注意信息安全，使用加密码，确保唯一ID即可） |
|    cookie     | 必选             | string | 码MD5                                                        |
|     share     | 可选（建议填写） |  Uint  | 单个红包允许领取的用户数量（分享红包） <br>举例：<br>   1：单个红包仅支持1个用户领取（非分享红包） <br>  2：单个红包可允许2个用户领取 |
|   dayTimes    | 可选（建议填写） |  Uint  | 单日内，单个账号每日领取奖励的最大次数                       |
|  totaltimes   | 可选（建议填写） |  Uint  | 整个活动周期内，单个账号能领取奖励的最大次数                 |
|  phoneNumber  | 可选（建议填写） | String | 若 accountType 非手机号码， 且能获取到手机号。则填入对应的手机号（如：15912345687） |
|    address    | 可选（建议填写） | String | 用户参加活动的地址位置信息。如可填入   用经纬度信息转化为的具体地址信息 |
|   latitude    | 可选（建议填写） | Float  | 维度。浮点数，范围为90 ~ -90                                   |
|   longitude   | 可选（建议填写） | Float  | 经度。浮点数，范围为180 ~ -180                                 |
|     imei      | 可选             | String | 手机设备号                                                   |
|    referer    | 可选             | String | 用户 HTTP 请求的 referer 值                                      |
|   loginType   | 可选             |  UInt  | 登录方式： <br>   0：其他<br>     1：手动帐号密码输入  <br>   2：动态短信密码登录 <br>    3：二维码扫描登录 |
|  loginSource  | 可选             |  UInt  | 登录来源：<br>  0：其他  <br>   1：PC网页 <br>    2：移动页面  <br>   3：APP  <br>   4：微信公众号 |
|   wxSubType   | 可选             |  int   | 1：微信公众号 <br>  2：微信小程序                                |
|    randNum    | 可选             | String | Token 签名随机数，微信小程序必填，建议16个字符                |
|    wxToken    | 可选             | String | 如果是微信小程序，该字段为以 ssesion_key 为 key 去签名随机数 radnNum 得到的值（hmac_sha256签名算法）。<br>如果是微信公众号或第三方登录，则为授权的 access_token（注意：不是普通 access_token，详细请参阅官方 [说明文档](https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1421140842) |
