## 1.接口描述
<br> 协议：HTTPS
<br> 域名：csec.api.qcloud.com
<br> 接口名：AntiFraud

## 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见[公共请求参数](https://www.qcloud.com/doc/api/254/1778)页面。其中，此接口的Action字段为AntiFraud。
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
<td> bankCardNum
</td><td> String
</td><td> 银行卡号
</td></tr>
<tr>
<td> userIp
</td><td> String
</td><td> 用户请求来源IP
</td></tr>
<tr>
<td> imei
</td><td> String
</td><td> 国际移动用户识别码
<tr> <td colspan="3">其他可选字段</td>
</th></tr>
</td></tr>
<tr>
<td> name
</td><td> String
</td><td> 姓名
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
<tr>
<td> message
</td><td> String
</td><td> 模块错误信息描述，与接口相关
</td></tr>
<td> code
</td><td> Int
</td><td> 公共错误码，0表示成功，其他值表示失败。详见错误码页面的<a href="https://www.qcloud.com/doc/api/254/1781"target="black">公共错误码</a>
</td></tr>
</tbody></table>

RiskDetail类型说明
<table class="t">
<tbody><tr>
<th height="23"> <b>风险类型</b>
</th><th> <b>风险详情</b>
</th><th> <b>风险码</b>
</th></tr>
<tr>
<td rowspan="5"> 帐号风险
</td><td> 信贷中介
<br></td>
<td>1</td></tr>
<tr>
  <td>不法分子 </td>
  <td>2</td>
</tr>
<tr>
  <td>虚假资料 </td>
  <td>3</td>
</tr>
<tr>
  <td>羊毛党 </td>
  <td>4</td>
</tr>
<tr>
  <td>身份认证失败 </td>
  <td>5</td>
</tr>
<tr>
<td rowspan="4"> 区域风险
</td><td> 手机号归属地高风险聚集
<br></td><td> 100
</td></tr>
<tr>
  <td>身份证归属地高风险聚集 <br></td>
  <td>101</td>
</tr>
<tr>
  <td>常用地址高风险聚集 <br></td>
  <td>102</td>
</tr>
<tr>
  <td>操作IP为高风险聚集 </td>
  <td>103</td>
</tr>
<tr>
<td rowspan="7"> 异常设备
</td><td> 设备使用过多的身份证或手机号进行申请
<br></td><td> 201
</td></tr>
<tr>
  <td>身份证使用过多设备进行申请 <br></td>
  <td>202</td>
</tr>
<tr>
  <td>用户疑似使用代理设备<br></td>
  <td>203</td>
</tr>
<tr>
  <td>用户使用过多设备进行申请 <br></td>
  <td>204</td>
</tr>
<tr>
  <td>异地使用设备 <br></td>
  <td>205</td>
</tr>
<tr>
  <td>非本人常用设备 <br></td>
  <td>206</td>
</tr>
<tr>
  <td>涉黑设备 </td>
  <td>207</td>
</tr>
<tr>
<td rowspan="3"> 异常环境
</td><td> 恶意环境
<br></td><td> 301
</td></tr>
<tr>
  <td>手机环境异常 <br></td>
  <td>302</td>
</tr>
<tr>
  <td>PC环境异常 </td>
  <td>303</td>
</tr>
<tr>
<td rowspan="7"> 多头借贷
</td><td> 身份证在一定时间内多次申请借贷
<br></td><td> 401
</td></tr>
<tr>
  <td>手机号在一定时间内多次申请借贷 <br></td>
  <td>402</td>
</tr>
<tr>
  <td>银行卡在一定时间内多次申请借贷 <br></td>
  <td><p>403</p></td>
</tr>
<tr>
  <td>IMEI信息在一定时间内多次申请借贷中出现 <br></td>
  <td>404</td>
</tr>
<tr>
  <td>IMSI在一定时间内多次借贷信息中出现 <br></td>
  <td>405</td>
</tr>
<tr>
  <td>MAC信息在一定时间内多次借贷信息中出现 <br></td>
  <td>406</td>
</tr>
<tr>
  <td>申请人在一定时间内在多个平台申请借款</td>
  <td>407</td>
</tr>
<tr>
<td rowspan="3"> 异常行为
</td><td> 组团骗贷
<br></td><td> 501
</td></tr>
<tr>
  <td>所在地跳变 </td>
  <td>502</td>
</tr>
<tr>
  <td>其他异常行为</td>
  <td>503</td>
</tr>
</td></tr></tbody></table>

## 4.示例代码
一个完整的请求需要两类请求参数：公共请求参数和接口请求参数。这里只列出了接口请求参数，并未列出公共请求参数，有关公共请求参数的说明可见[公共请求参数](https://www.qcloud.com/doc/api/254/1778)小节。
<pre>
请求示例 ：
https://csec.api.qcloud.com/v2/index.php?Action=AntiFraud
&<a href="https://www.qcloud.com/doc/api/229/6976">公共请求参数</a>
&idNumber=1234567890
&name=%E6%9D%A8%E7%BA%A2
&phoneNumber=008613246208548
</pre>

## 5.响应示例
```
{
"code": 0,
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
