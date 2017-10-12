## 1. 接口描述

本接口 (SetOutBandVPNAuthPwd) 设置带外VPN认证用户密码。
接口请求域名：<font style="color:red">bm.api.qcloud.com</font>


此API分为两个逻辑，创建VPN认证用户及设置认证用户的密码，需两次不同参数值调用。

创建VPN认证用户: 先调用<a href="/doc/api/386/6679" title="获取带外VPN信息">获取带外VPN信息(GetOutBandVPNAuthInfo)接口</a> 获取VPN信息，如GetOutBandVPNAuthInfo返回的be_first=true, 则必须要调用本API，并设置入参createOrUpdate值为create。

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
<td> 取值为create或者update字符串。 create: 创建此appId的VPN帐号，只有在<a href="/doc/api/386/6679" title="获取带外VPN信息">获取带外VPN信息(GetOutBandVPNAuthInfo)接口</a> 返回的be_first=true时需要创建；
update:修改此VPN认证帐号的密码，前提条件：已经调用本API创建了VPN认证用户。
</tbody></table>


## 3. 输出参数

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> code
<td> Int
<td> 公共错误码，0表示成功，其他值表示失败。详见错误码页面的<a href="/doc/api/456/6725" title="公共错误码">公共错误码</a>。
<tr>
<td> message
<td> String
<td> 模块错误信息描述，与接口相关。
<tr>
<td> data
<td> null
<td> 
</tbody></table>


## 4. 模块错误码

| code |codeDesc| 描述 |
|------|------|------|
| 10004 |OperationDenied| 没有操作权限 |
| 10100 |InternalError.ObAuthAccessError| 访问鉴权模块错误 |
| 10101 |InternalError.ObAuthError|鉴权模块返回错误 |




## 5. 示例
输入
<pre>
https://bm.api.qcloud.com/v2/index.php?
Action=SetOutBandVPNAuthPwd
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&password=tencent89
&createOrUpdate=update
</pre>
输出
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": null
}
```

