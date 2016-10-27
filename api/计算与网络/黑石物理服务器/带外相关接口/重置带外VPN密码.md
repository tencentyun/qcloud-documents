## 1. 接口描述
域名:bm.api.qcloud.com
接口名:SetOutBandVPNAuthPwd

设置带外VPN认证用户密码
此API分为两个逻辑，创建VPN认证用户及设置认证用户的密码。

创建VPN认证用户: 先调用 GetOutBandVPNAuthInfo 获取VPN信息，如GetOutBandVPNAuthInfo返回的be_first=true, 则必须要调用本API，并设置入参createOrUpdate值为create。

设置认证用户的密码： 已经调用本API创建过VPN认证用户，直接调用本API设置。


## 2. 输入参数
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> appId
<td> 是
<td> Int
<td> 开发商自己的appId
<tr>
<td> password
<td> 是
<td> String
<td> 用户设置的vpn认证密码。密码需要8-16个字符，至少包含英文、数字和符号!#$%&^*()中的2种


<tr>
<td> createOrUpdate
<td> 是
<td> String
<td> 取值为create或者update字符串。 create: 创建此appId的VPN帐号，只有在GetOutBandVPNAuthInfo返回的be_first=true时需要创建；
update:修改此PN帐号的密码，前提条件已经调用本API创建了VPN认证用户。
</tbody></table>


## 3. 输出参数

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> code
<td> Int
<td> 公共错误码，0表示成功，其他值表示失败。详见错误码页面的<a href="https://www.qcloud.com/doc/api/244/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="公共错误码">公共错误码</a>。
<tr>
<td> message
<td> String
<td> 模块错误信息描述，与接口相关。
<tr>
<td> data
<td> null
<td> 
</tbody></table>


模块错误码

| code | 描述 |
|------|------|
| 10100 | 访问鉴权模块错误 |
| 10101 | 鉴权模块返回错误 |
| 10004 | 参数错误 |




## 4. 示例
输入
```
https://bm.api.qcloud.com/v2/index.php?Action=SetOutBandVPNAuthPwd&SecretId=AKID52SKw5uMEy3jhpMUBqSylEBJBby6E0KC&Nonce=57726&Timestamp=1476431939&Region=bj&appId=1251001002&password=tencent89&createOrUpdate=update&Signature=42ZqsjKT%2F%2Fdv7X0JKpoDmR1PjlE%3D
```
输出
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": null
}
```

