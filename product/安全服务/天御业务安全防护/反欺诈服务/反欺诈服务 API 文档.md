## 1.接口描述
<br> 协议：HTTPS
<br> 域名：csec.api.qcloud.com
<br> 接口名：AntiFraud

## 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见[公共请求参数](https://www.qcloud.com/document/product/295/7279)页面。其中，此接口的Action字段为AntiFraud。
<br>注意：以下每一个参数对于识别恶意都非常重要，任何参数的缺少都有可能影响识别效果 。
<table class="t">
<th><b>参数名称</b>
</th><th> <b>类型</b>
</th><th> <b>描述</b>
</th></tr>
<tr> <td colspan="3">基本字段：共有五项，要求至少选择两项</td>
</tr>
<tr>
<td> idNumber
</td><td> String
</td><td> 身份证号
</td></tr>
<tr>
<td> phoneNumber
</td><td> String
</td><td> 手机号码：国家代码
<br> 手机号，如0086-15912345678
<br> 注意0086前不需要+号
</td></tr>
<tr>
<td> bankCardNumber
</td><td> String
</td><td> 银行卡号
</td></tr>
<tr>
<td> userIp
</td><td> String
</td><td> 用户请求来源IP
</td></tr>
<tr>
<td rowspan="2"> imei <br> idfa
</td><td> String
</td><td> imei 国际移动用户识别码 
</td></tr>
<tr><td> String
</td><td> idfa ios系统广告标示符
</td></tr>
<tr> <td colspan="3">其他可选字段</td>
</th></tr>
</td></tr>
<tr>
<td> scene
</td><td> Uint
</td><td> 业务场景ID， 0：借贷（默认值） 1：支付
</td></tr>
<tr>
<td> name
</td><td> String
</td><td> 姓名(注意：使用中文参与鉴权签名)
</td></tr>
<tr>
<td> emailAddress
</td><td> String
</td><td> 用户邮箱地址
</td></tr>
<tr>
<td> address
</td><td> String
</td><td> 用户住址
</td></tr>
<tr>
<td> mac
</td><td> String
</td><td> MAC地址
</td></tr>
<tr>
<td> imsi
</td><td> String
</td><td> 国际移动用户识别码
</td></tr>
<tr>
<td> accountType
</td><td> UInt
</td><td> 关联的腾讯帐号1：QQ开放帐号 2：微信开放帐号
</td></tr>
<tr>
<td> uid
</td><td> String
</td><td> 可选的QQ或微信openid
</td></tr>
<tr>
<td> appId
</td><td> String
</td><td> qq或微信分配网站或应用的appid，用来唯一标识网站或应用
</td></tr>
<tr>
<td> wifiMac
</td><td> String
</td><td> wifimac
</td></tr>
<tr>
<td> wifiSSID
</td><td> String
</td><td> WIFI服务集标识
</td></tr>
<tr>
<td> wifiBSSID
</td><td> String
</td><td> WIFI-BSSID
</td></tr>
<tr>
<td> businessId
</td><td> String
</td><td> 业务ID，在多个业务中使用此服务，通过此ID区分统计数据
</td></tr>
</tbody></table>

## 3.输出参数
<table class="t">
<tbody><tr>
<th> <b>参数名称</b>
</th><th> <b>类型</b>
</th><th> <b>描述</b>
</th></tr>
<td> code
</td><td> Int
</td><td> 公共错误码，0表示成功，其他值表示失败。详见错误码页面的<a href="https://www.qcloud.com/document/product/295/7285"target="black">公共错误码</a>
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
<td> riskScore
</td><td> UInt
</td><td> 0-100:欺诈分值。值越高欺诈可能性越大；-1:查询不到数据
</td></tr>
<tr>
<td> riskInfo
</td><td> RiskDetail
</td><td> 扩展字段，对风险类型的说明
<br> riskScore为0时无此字段
</td></tr>
</tbody></table>

RiskDetail类型说明
<table class="t">
<tbody><tr>
<th height="23"> <b>风险类型</b>
</th><th> <b>风险详情</b>
</th><th> <b>风险码</b>
</th><th> <b>说明</b>
</th></tr>
<tr>
<td rowspan="7"> 帐号风险
</td>
<td> 信贷中介
</td>
<td>1</td>
<td>涉嫌从事包装客户资料，伪造客户资料，冒用客户资料，套取机构风险政策等职业的用户或者机构成员</td></tr>
<tr>
  <td>不法分子 </td>
  <td>2</td>
  <td>互联网行为涉嫌色情、赌博、毒品等违法行为</td>
</tr>

<tr>
  <td>虚假资料 </td>
  <td>3</td>
  <td>输入信息和虚假身份信息提交强相关，或者有恶意申请/操作记录，或者个人信息疑似泄漏、冒用、伪造等</td>
</tr>
<tr>
  <td>羊毛党 </td>
  <td>4</td>
  <td>在网贷、电商、O2O等平台有薅羊毛行为的用户</td>
</tr>
<tr>
  <td>身份认证失败 </td>
  <td>5</td>
  <td>身份信息对（身份证、手机号、姓名）涉嫌伪造</td>
</tr>
<tr>
  <td>疑似恶意欺诈 </td>
  <td>6</td>
  <td>存在骗贷行为</td>
</tr>
<tr>
  <td>失信名单 </td>
  <td>7</td>
  <td>失信名单</td>
</tr>
<tr>
<td rowspan="4"> 区域风险
</td><td> 手机号归属地高风险聚集
<br></td><td> 100
</td>
<td>手机号归属地命中信贷高风险地区灰名单</td>
</tr>
<tr>
  <td>身份证归属地高风险聚集 <br></td>
  <td>101</td>
  <td>身份证归属地命中信贷高风险地区灰名单</td>
</tr>
<tr>
  <td>常用地址高风险聚集 <br></td>
  <td>102</td>
  <td>常用地址命中信贷高风险地区灰名单</td>
</tr>
<tr>
  <td>操作IP为高风险聚集 </td>
  <td>103</td>
  <td>操作IP所在地命中信贷高风险地区灰名单</td>
</tr>
<tr>
<td rowspan="7"> 异常设备
</td><td> 设备使用过多的身份证或手机号进行申请
<br></td><td> 201
</td>
<td>疑似中介代办</td>
</tr>
<tr>
  <td>身份证使用过多设备进行申请 <br></td>
  <td>202</td>
  <td>疑似中介代办</td>
</tr>
<tr>
  <td>用户疑似使用代理设备<br></td>
  <td>203</td>
  <td>疑似中介代办</td>
</tr>
<tr>
  <td>用户使用过多设备进行申请 <br></td>
  <td>204</td>
  <td>疑似中介代办</td>
</tr>
<tr>
  <td>异地使用设备 <br></td>
  <td>205</td>
  <td>疑似设备被盗或中介代办</td>
</tr>
<tr>
  <td>非本人常用设备 <br></td>
  <td>206</td>
  <td>疑似设备被盗或中介代办</td>
</tr>
<tr>
  <td>涉黑设备 </td>
  <td>207</td>
  <td>命中设备黑名单</td>
</tr>
<tr>
<td rowspan="3"> 异常环境
</td><td> 恶意环境
<br></td><td> 301
</td>
<td>设备和IP命中黑数据库，包括使用虚拟机、代理设备、代理IP、猫池等。</td>
</tr>
<tr>
  <td>手机环境异常 <br></td>
  <td>302</td>
  <td>账号有被盗风险</td>
</tr>
<tr>
  <td>PC环境异常 </td>
  <td>303</td>
  <td>账号有被盗风险</td>
</tr>
<tr>
<td rowspan="7"> 多头借贷
</td><td> 身份证在一定时间内多次申请借贷
<br></td><td> 401
</td>
<td>疑似多头借贷</td>
</tr>
<tr>
  <td>手机号在一定时间内多次申请借贷 <br></td>
  <td>402</td>
  <td>疑似多头借贷</td>
</tr>
<tr>
  <td>银行卡在一定时间内多次申请借贷 <br></td>
  <td><p>403</p></td>
  <td>疑似多头借贷</td>
</tr>
<tr>
  <td>IMEI信息在一定时间内多次申请借贷中出现 <br></td>
  <td>404</td>
  <td>疑似多头借贷或黑中介代办</td>
</tr>
<tr>
  <td>IMSI在一定时间内多次借贷信息中出现 <br></td>
  <td>405</td>
  <td>疑似多头借贷或黑中介代办</td>
</tr>
<tr>
  <td>MAC信息在一定时间内多次借贷信息中出现 <br></td>
  <td>406</td>
  <td>疑似多头借贷或黑中介代办</td>
</tr>
<tr>
  <td>申请人在一定时间内在多个平台申请借款</td>
  <td>407</td>
  <td>疑似多头借贷</td>
</tr>
<tr>
<td rowspan="3"> 异常行为
</td><td> 组团骗贷
<br></td><td> 501
</td>
<td>输入信息与团伙骗贷行为关联度较高</td>
</tr>
<tr>
  <td>所在地跳变 </td>
  <td>502</td>
  <td>可能有跑路、催债困难等风险</td>
</tr>
<tr>
  <td>其他异常行为</td>
  <td>503</td>
  <td>输入信息和以下高风险可能性关联度较高：被盗风险较高、社交圈子不固定、地理圈子变化较大</td>
</tr>
</td></tr></tbody></table>

## 4.示例代码
代码下载：  [Python示例](https://mc.qcloudimg.com/static/archive/a8b291becf06c9fefab003f6afc16509/AntiFraud.py.zip) [PHP示例](https://mc.qcloudimg.com/static/archive/06397c265ae2dc364f2f47559125ce5b/AntiFraud.php.zip) [Java示例](https://mc.qcloudimg.com/static/archive/04d6cf531a5487399c4f824238df1a25/AntiFraud.java.zip) [.Net示例](https://mc.qcloudimg.com/static/archive/de77f53a2d809c5bbdb569c5ca5c77aa/AntiFraud.cs.zip)

一个完整的请求需要两类请求参数：公共请求参数和接口请求参数。这里只列出了接口请求参数，并未列出公共请求参数，有关公共请求参数的说明可见[公共请求参数](https://www.qcloud.com/document/product/295/7279)小节。
```
请求示例 ：
https://csec.api.qcloud.com/v2/index.php?Action=AntiFraud
&<公共请求参数>
&idNumber=1234567890
&name=%E6%9D%A8%E7%BA%A2
&phoneNumber=008613246208548
```

## 5.响应示例
```
{
"code": 0,
"codeDesc":"success" ,
"message": "OK",
"riskScore": 90,
"riskInfo": [
　　{
　　　"riskCode": 1
　　},
　　{
　　　"riskCode": 203
　　}
　]
}
```
