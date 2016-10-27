## 1. 接口描述
域名:bm.api.qcloud.com
接口名:GetOutBandVPNAuthInfo

获取带外VPN认证信息
用户使用带外SSL VPN客户端登录VPN时，用获取到的信息作为客户端需要输入的信息。


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
<td> 公共错误码，0表示成功，其他值表示失败。详见错误码页面的<a href="https://www.qcloud.com/doc/api/244/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="公共错误码">公共错误码</a>。
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
<td> 带外SSL VPN地址。
<tr>
<td> userName
<td> String
<td> 带外SSL VPN 用户名。
<tr>
<td> userGroup
<td> String
<td> 带外SSL VPN 用户组, 即带外SSL VPN客户端中的域信息。
<tr>
<td> be_first
<td> Bool
<td> 此接口中返回的userName是否为第一次使用, 如为true, 则需要用户调用API SetOutBandVPNAuthPwd并且入参createOrUpdate值为create，创建此appId的vpn帐号; false 为已经调用过SetOutBandVPNAuthPwd创建过VPN帐号。
</tbody></table>


模块错误码

| code | 描述 |
|------|------|
| 9001 | 操作数据库错误 |
| 10100 | 访问鉴权模块错误 |
| 10101 | 鉴权模块返回错误 |
| 10004 | 参数错误 |
| 10105 | 操作错误，系统无此用户的VPN设置信息 |


## 4. 示例
输入
```
https://bm.api.qcloud.com/v2/index.php?Action=GetOutBandVPNAuthInfo&SecretId=AKID52SKw5uMEy3jhpMUBqSylEBJBby6E0KC&Nonce=6392&Timestamp=1476428786&Region=bj&appId=1251001002&Signature=4h2Mv6hGxjQek6EZaXibKbYlOEY%3D
```
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

