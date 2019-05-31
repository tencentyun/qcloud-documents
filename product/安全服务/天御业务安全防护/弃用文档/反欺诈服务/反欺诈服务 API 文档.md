## 接口描述

协议： `HTTPS`

域名： `csec.api.qcloud.com`

接口名： `AntiFraud`

## 输入参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见 [公共请求参数](https://cloud.tencent.com/document/product/295/7279) 页面。其中，此接口的 Action 字段为 AntiFraud。

注意：以下每一个参数对于识别恶意用户和行为都非常重要，缺少任何参数都有可能影响识别效果 。

<table>
<tr>
<th>参数名称</th>
<th>类型</th>
<th>描述</th></tr>
<tr>
<td colspan="3">基本字段：共有五项，要求至少选择两项</td>
</tr>
<tr>
<td>idNumber</td>
<td>String</td>
<td>身份证号</td>
</tr>
<tr>
<td>phoneNumber</td>
<td>String</td>
<td>手机号码：国家代码</br>
手机号，如 0086-15912345678</br> 
注意 0086 前不需要 + 号</td>
</tr>
<tr>
<td>bankCardNumber</td>
<td>String</td>
<td>银行卡号</td>
</tr>
<tr>
<td>userIp</td>
<td>String</td>
<td>用户请求来源 IP</td>
</tr>
<tr>
<td rowspan="2">imei</br>
idfa</td>
<td>String</td>
<td>imei 国际移动用户识别码</td>
</tr>
<tr>
<td>String</td>
<td>idfa iOS系统广告标示符</td>
</tr>
<tr>
<td colspan="3">其他可选字段</td>
</tr>
<tr>
<td>scene</td>
<td>Uint</td>
<td>业务场景 ID， 0：借贷（默认值） 1：支付</td>
</tr>
<tr>
<td>name</td>
<td>String</td>
<td>姓名(注意：使用中文参与鉴权签名)</td>
</tr>
<tr>
<td>emailAddress</td>
<td>String</td>
<td>用户邮箱地址</td>
</tr>
<tr>
<td>address</td>
<td>String</td>
<td>用户住址</td>
</tr>
<tr>
<td>mac</td>
<td>String</td>
<td>MAC 地址</td>
</tr>
<tr>
<td>imsi</td>
<td>String</td>
<td>国际移动用户识别码</td>
</tr>
<tr>
<td>accountType</td>
<td>UInt</td>
<td>关联的腾讯帐号 1：QQ 开放帐号 2：微信开放帐号</td>
</tr>
<tr>
<td>uid</td>
<td>String</td>
<td>可选的 QQ 或微信 openid</td>
</tr>
<tr>
<td>appId</td>
<td>String</td>
<td>QQ 或微信分配网站或应用的 appid，用来唯一标识网站或应用</td>
</tr>
<tr>
<td>wifiMac</td>
<td>String</td>
<td>wifimac</td>
</tr>
<tr>
<td>wifiSSID</td>
<td>String</td>
<td>WiFi 服务集标识</td>
</tr>
<tr>
<td>wifiBSSID</td>
<td>String</td>
<td>WIFI-BSSID</td>
</tr>
<tr>
<td>businessId</td>
<td>String</td>
<td>业务 ID，在多个业务中使用此服务，通过此 ID 区分统计数据</td>
</tr>
<tr>
<td>idCryptoType
</td><td> uint
</td><td>身份证加密类型， 0：不加密（默认值） 1：md5
</td></tr>
<tr>
<td> phoneCryptoType
</td><td> uint
</td><td> 手机号加密类型，0：不加密（默认值） 1：md5
</td></tr>
<tr>
<td> nameCryptoType
</td><td> uint
</td><td> 姓名加密类型，0：不加密（默认值） 1：md5
</td></tr>
</table>

## 输出参数

| 参数名称 | 类型 | 描述 |
| ----- | ----- | ----- |
| code | Int | 公共错误码；</br>0 表示成功，其他值表示失败；</br>详见 [错误码](https://cloud.tencent.com/document/product/295/7285) 页面中的“公共错误码”相关内容。 |
| codeDesc | String | 业务侧错误码；</br>成功时返回 Success；</br>错误时返回具体业务错误原因。 |
| message | String | 模块错误信息描述，与接口相关。 |
| idfound | Int | 表示该条记录中的身份证能否查到；</br>1 :能查到；</br>-1 :查不到。 |
| found | Int | 表示该条记录能否查到；</br>1 :能查到；</br>-1 :查不到。 |
| riskScore | UInt | 0-100：欺诈分值；</br>值越高欺诈可能性越大；</br>-1：查询不到数据。 |
| riskInfo | RiskDetail | 扩展字段，对风险类型的说明；</br>riskScore 0 :无此字段。 |

RiskDetail 类型说明

| 名称 | 类型 | 描述 |
| ----- | ----- | ----- |
| riskCode | UInt | 风险码 |
| riskCodeValue | UInt | 风险详情值 |

风险码

<table>
<tr>
<th>风险类型</th>
<th>风险详情</th>
<th>风险码</th>
<th>命中时输出
风险码等级</th>
<th>说明</th>
</tr>
<tr>
<td rowspan="8">账号风险</td>
<td>信贷中介</td>
<td>1</td>
<td>1：低风险</br>2：中风险</br>3：高风险</td>
<td>涉嫌从事包装客户资料、伪造客户资料、冒用客户资料、套取机构风险政策等职业的用户或者机构成员。</td>
</tr>
<tr>
<td>不法分子</td>
<td>2</td>
<td>1：低风险</br>2：中风险</br>3：高风险</td>
<td>互联网行为涉嫌色情、赌博、毒品等违法行为。</td>
</tr>
<tr>
<td>虚假资料</td>
<td>3</td>
<td>1：低风险</br>2：中风险</br>3：高风险</td>
<td>输入信息和虚假身份信息提交强相关，或者有恶意申请/操作记录，或者个人信息疑似泄漏、冒用、伪造等。</td>
</tr>
<tr>
<td>羊毛党</td>
<td>4</td>
<td>1：低风险</br>2：中风险</br>3：高风险</td>
<td>在网贷、电商、O2O 等平台有薅羊毛行为的用户。</td>
</tr>
<tr>
<td>身份认证失败</td>
<td>5</td>
<td>2：中风险</td>
<td>身份信息对（身份证、手机号、姓名）涉嫌伪造。</td>
</tr>
<tr>
<td>疑似恶意欺诈</td>
<td>6</td>
<td>1：低风险</br>2：中风险</br>3：高风险</td>
<td>存在骗贷行为。</td>
</tr>
<tr>
<td>失信名单</td>
<td>7</td>
<td>3：高风险</td>
<td>失信名单。</td>
</tr>
<tr>
<td>异常支付行为</td>
<td>8</td>
<td>1：低风险</br>2：中风险</br>3：高风险</td>
<td>支付行为异常包括支付频次、额度、场景等方面有过异常的。</td>
</tr>
<tr>
<td rowspan="2">异常环境</td>
<td>恶意环境</td>
<td>301</td>
<td>1：低风险</br>2：中风险</br>3：高风险</td>
<td>设备和 IP 命中黑数据库，包括使用虚拟机、代理设备、代理 IP、猫池等。</td>
</tr>
<tr>
<td>其他异常行为</td>
<td>503</td>
<td>1：低风险</br>2：中风险</br>3：高风险</td>
<td>输入信息和以下高风险可能性关联度较高：被盗风险较高、社交圈子不固定、地理圈子变化较大。</td>
</tr>
</table>

## 示例代码

代码下载：[Python 示例](https://mc.qcloudimg.com/static/archive/a8b291becf06c9fefab003f6afc16509/AntiFraud.py.zip)、 [PHP 代码示例](https://mc.qcloudimg.com/static/archive/06397c265ae2dc364f2f47559125ce5b/AntiFraud.php.zip)、 [Java 示例](https://mc.qcloudimg.com/static/archive/70b700e34e982822af2a020454185a8d/AntiFraud.zip)、 [.Net 示例](https://mc.qcloudimg.com/static/archive/05c3d0f6edbcd297502ab7407e91275b/AntiFraud.zip)

一个完整的请求需要两类请求参数：公共请求参数和接口请求参数。这里只列出了接口请求参数，并未列出公共请求参数，有关公共请求参数的说明可见 [公共请求参数](https://cloud.tencent.com/document/product/295/7279) 页面。

```
请求示例 ：
https://csec.api.qcloud.com/v2/index.php?Action=AntiFraud
&<公共请求参数>
&idNumber=1234567890
&name=%E6%9D%A8%E7%BA%A2
&phoneNumber=008613246208548
```

## 响应示例


```
{"code":0,
"codeDesc":"Success",
"found":1,  //表示该条记录能被查到
"idFound":1, //表示该条记录中的身份证能被查到
"message":"No Error",
"riskInfo":
[
  {
     "riskCode":5,  
     "riskCodeValue":2 //命中风险码 5：身份认证失败，风险等级为中风险
  },     
  {
    "riskCode":6,
    "riskCodeValue":3 //命中风险码 6：疑似恶意欺诈，风险等级为高风险
  }
], 
"riskScore":88
}
```
