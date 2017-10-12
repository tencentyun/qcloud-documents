## 1. 接口描述

本接口 (GetOutBandVPNAuthInfo) 获取带外VPN认证信息。
接口请求域名：<font style="color:red">bm.api.qcloud.com</font>


用户使用带外SSL VPN客户端登录VPN时，用获取到的信息作为VPN客户端输入的信息。


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
<td> Object
<td> 返回的authInfo实例，具体数据结构如下表说明。
</tbody></table>

</b></th>authInfo结构</b></th>
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> vpnGwAddr
<td> String
<td> 带外SSL VPN网关地址。
<tr>
<td> userName
<td> String
<td> 带外SSL VPN 认证用户名。
<tr>
<td> userGroup
<td> String
<td> 带外SSL VPN 认证用户所在的用户组, 对应带外SSL VPN客户端中需要输入的域信息。
<tr>
<td> be_first
<td> Bool
<td> 此接口中返回的userName是否为第一次使用。 
 如为true, 则是第一次, 需要用户调用API SetOutBandVPNAuthPwd并且入参createOrUpdate值为create，创建此appId的vpn认证帐号; 
 false 为已经调用过SetOutBandVPNAuthPwd创建过VPN认证帐号。
</tbody></table>


## 4. 模块错误码

| code |codeDesc| 描述 |
|------|------|------|
| 9001 |InternalError.DbError| 操作数据库错误 |
| 10004 |OperationDenied| 没有操作权限 |
| 10100 |InternalError.ObAuthAccessError| 访问鉴权模块错误 |
| 10101 |InternalError.ObAuthError|鉴权模块返回错误 |
| 10105 |InvalidResource.ObAuthNoConfig|操作错误，系统无此用户的VPN设置信息 |


## 5. 示例
输入
<pre>
https://bm.api.qcloud.com/v2/index.php?
Action=GetOutBandVPNAuthInfo
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>
输出
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "authInfo": {
            "vpnGwAddr": "115.159.242.100:443",
            "userName": "1251001002",
            "userGroup": "bm1251001002",
            "be_first": false
        }
    }
}
```

