## 输入参数
<table>
   <tr>
      <th>参数名称</th>
      <th nowrap="nowrap">是否必选</th>
      <th>类型</th>
      <th>描述</th>
   </tr>
   <tr>
      <td>accountType</td>
      <td>是</td>
      <td>Uint</td>
      <td>用户账号类型<br>1：QQ开放帐号<br> 2：微信开放账号<br> 4：手机号 （暂仅支持国内手机号）<br> 10004： 手机号MD5 </td>
   </tr>
   <tr>
      <td>uid</td>
      <td>是</td>
      <td>String</td>
      <td>用户 ID 值，如微信/QQ openid，或手机号等（如15912345687）</td>
   </tr>
   <tr>
      <td>userIP</td>
      <td>是</td>
      <td>String</td>
      <td>用户领取奖励时的真实外网 IP</td>
   </tr>
   <tr>
      <td>postTime</td>
      <td>是</td>
      <td>Uint</td>
      <td>用户操作时间戳，单位秒（格林威治时间精确到秒，如1501590972）</td>
   </tr>
   <tr>
      <td>appId</td>
      <td>可选</td>
      <td>String</td>
      <td>accountType 是 QQ 或微信开放账号时，该参数必填，表示 QQ 或微信分配给给网站或应用的 appId，用来唯一标识网站或应用</td>
   </tr>
   <tr>
      <td>goodInfo</td>
      <td>是</td>
      <td>String</td>
      <td>所买物品信息</td>
   </tr>
   <tr>
      <td>encryptedCode</td>
      <td nowrap="nowrap">可选（建议填写）</td>
      <td>String</td>
      <td>领奖码的唯一加密码（请注意信息安全，使用加密码，确保唯一ID即可）</td>
   </tr>
   <tr>
      <td>share</td>
      <td>可选（建议填写）</td>
      <td>Uint</td>
      <td>单个红包允许领取的用户数量（分享红包）<br> 举例：<br> 1：单个红包仅支持1个用户领取（非分享红包） <br>2：单个红包可允许2个用户领取 </td>
   </tr>
   <tr>
      <td>dayTimes</td>
      <td>可选（建议填写）</td>
      <td>Uint</td>
      <td>单日内，单个账号每日领取奖励的最大次数</td>
   </tr>
   <tr>
      <td>totaltimes</td>
      <td>可选（建议填写）</td>
      <td>Uint</td>
      <td>整个活动周期内，单个账号能领取奖励的最大次数</td>
   </tr>
   <tr>
      <td>phoneNumber</td>
      <td>可选（建议填写）</td>
      <td>String</td>
      <td>若 accountType 非手机号码， 且能获取到手机号。则填入对应的手机号（如：15912345687）</td>
   </tr>
   <tr>
      <td>address</td>
      <td>可选（建议填写）</td>
      <td>String</td>
      <td>用户参加活动的地址位置信息。如可填入 用经纬度信息转化为的具体地址信息</td>
   </tr>
   <tr>
      <td>latitude</td>
      <td>可选（建议填写）</td>
      <td>Float</td>
      <td>维度。浮点数，范围为 90 ~ -90</td>
   </tr>
   <tr>
      <td>longitude</td>
      <td>可选（建议填写）</td>
      <td>Float</td>
      <td>经度。浮点数，范围为 180 ~ -180</td>
   </tr>
   <tr>
      <td>imei</td>
      <td>可选</td>
      <td>String</td>
      <td>手机设备号</td>
   </tr>
   <tr>
      <td>referer</td>
      <td>可选</td>
      <td>String</td>
      <td>用户 HTTP 请求的 referer 值</td>
   </tr>
   <tr>
      <td>loginType</td>
      <td>可选</td>
      <td>UInt</td>
      <td>登录方式：<br>0：其他 <br>1：手动帐号密码输入 <br>2：动态短信密码登录<br> 3：二维码扫描登录</td>
   </tr>
   <tr>
      <td>loginSource</td>
      <td>可选</td>
      <td>UInt</td>
      <td>登录来源 ：<br>0：其他 <br>1：PC网页 <br>2：移动页面 <br>3：APP <br>4：微信公众号</td>
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
      <td>返回码</td>
   </tr>
   <tr>
      <td>codeDesc</td>
      <td>String</td>
      <td>业务侧错误码。成功时返回 Success，错误时返回具体业务错误原因。</td>
   </tr>
   <tr>
      <td>message</td>
      <td>String</td>
      <td>UTF-8 编码，出错消息</td>
   </tr>
   <tr>
      <td>nonce</td>
      <td>UInt</td>
      <td>随机正整数，与 Timestamp 联合起来, 用于防止重放攻击（公共参数）</td>
   </tr>
   <tr>
      <td>postTime（*对应输入参数）</td>
      <td>String</td>
      <td>操作时间戳，单位秒</td>
   </tr>
   <tr>
      <td>uid（*对应输入参数）</td>
      <td>String</td>
      <td>用户 ID  accountType 不同对应不同的用户 ID。如果是 QQ 或微信用户则填入对应的 openId</td>
   </tr>
   <tr>
      <td>userIp（*对应输入参数）</td>
      <td>String</td>
      <td>操作来源的外网IP</td>
   </tr>
   <tr>
      <td>level（*重要：风险值）</td>
      <td>Int</td>
      <td>0：表示无恶意<br>1～4：恶意等级由低到高</td>
   </tr>
   <tr>
      <td nowrap="nowrap">riskType（*重要：风险标签）</td>
      <td>Array</td>
      <td>风险类型</td>
   </tr>
   <tr>
      <td>associateAccount</td>
      <td>String</td>
      <td>accountType 是 QQ 或微信开放账号时，用于标识 QQ 或微信用户登录后关联业务自身的账号 ID</td>
   </tr>
</table>


## risktype 详细说明
<table>
   <tr>
      <th>风险类型</th>
      <th>风险详情</th>
      <th>风险码</th>
      <th>解释说明</th>
   </tr>
   <tr>
      <td rowspan="3">账号风险</td>
      <td>账号信用低</td>
      <td>1</td>
      <td>账号近期存在 因恶意被处罚历史、低活跃、被举报等因素</td>
   </tr>
   <tr>
      <td>垃圾账号</td>
      <td>2</td>
      <td>疑似批量注册小号、近期存在严重违规或大量举报</td>
   </tr>
   <tr>
      <td>无效账号</td>
      <td>3</td>
      <td>送检账号参数无法成功解析，若为微信/QQ openid 请检查是否送检数据错误</td>
   </tr>
   <tr>
      <td rowspan="3">行为风险</td>
      <td>批量操作</td>
      <td>101</td>
      <td>存在 IP/设备/环境等因素的聚集性异常</td>
   </tr>
   <tr>
      <td>自动机</td>
      <td>102</td>
      <td>疑似自动机批量请求</td>
   </tr>
   <tr>
      <td>异常扫码</td>
      <td>103</td>
      <td>频繁扫码、大量扫废码等异常扫码行为</td>
   </tr>
   <tr>
      <td rowspan="2">环境风险</td>
      <td >环境异常</td>
      <td>201</td>
      <td>操作IP/设备/环境存在异常。如当前 IP 非常用 IP 或恶意IP段</td>
   </tr>
   <tr>
      <td>Js上报异常</td>
      <td>202</td>
      <td>需用户在前端部署 js 方有效</td>
   </tr>
</table>
