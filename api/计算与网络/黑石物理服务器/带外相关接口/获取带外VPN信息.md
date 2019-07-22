>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述

GetOutBandVPNAuthInfo接口用来获取带外VPN认证信息。用户使用带外SSL VPN客户端登录VPN时，用获取到的信息作为VPN客户端输入的信息。

接口请求域名：<font style="color:red">bm.api.qcloud.com</font>

## 请求
### 请求示例
```
GET https://bmeip.api.qcloud.com/v2/index.php?
	&Action=GetOutBandVPNAuthInfo
	&<公共请求参数>
	&zoneId=<可用区zoneId>
```
### 请求参数
|参数名称|必选|类型|描述|
|-------|----|---|----|
| zoneId | 是 | Int | 可用区ID，需调用<a href="/doc/api/386/6634" title="查询地域以及可用区">查询地域以及可用区(DescribeRegions)接口</a> 获取zoneId |



## 响应
### 响应示例
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "authInfo": {
            "vpnGwAddr": "<带外vpn地址>",
            "userName": "<带外vpn用户名>",
            "userGroup": "<带外vpn用户域信息>",
            "be_first": "<true or false>"
        }
    }
}
```
### 响应参数
响应参数部分包含两层结构，外层展示接口的响应结果，内层展示具体的接口内容，包括带外登录信息。

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码, 0: 成功, 其他值: 失败，具体含义可以参考[错误码](/document/product/386/6725)。 |
| message |   String | 错误信息 |
| data |   Object | 返回的authInfo实例，具体数据结构如下表说明。 |

data.authInfo实例结构

|参数名称|类型|描述|
|---|---|---|
| authInfo.vpnGwAddr | String | 带外SSL VPN网关地址。|
| authInfo.userName | String | 带外SSL VPN 认证用户名。|
| authInfo.userGroup | String | 带外SSL VPN 认证用户所在的用户组, 对应带外SSL VPN客户端中需要输入的域信息。|
| authInfo.be_first | String | 此接口中返回的userName是否为第一次使用。 如为true, 则是第一次, 需要用户调用API SetOutBandVPNAuthPwd并且入参createOrUpdate值为create，创建此appId的vpn认证帐号;  false 为已经调用过SetOutBandVPNAuthPwd创建过VPN认证帐号。|


## 错误码

| code |codeDesc| 描述 |
|------|------|------|
| 9001 |InternalError.DbError| 操作数据库错误 |
| 10004 |OperationDenied| 没有操作权限 |
| 10100 |InternalError.ObAuthAccessError| 访问鉴权模块错误 |
| 10101 |InternalError.ObAuthError|鉴权模块返回错误 |
| 10105 |InvalidResource.ObAuthNoConfig|操作错误，系统无此用户的VPN设置信息 |


## 实际案例

### 输入
```
GET https://bm.api.qcloud.com/v2/index.php?
	Action=GetOutBandVPNAuthInfo
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
	&Nonce=35342
	&Timestamp=1508213215
	&Region=gz
	&zoneId=1000100003
	&Signature=o%2Fx5UUFhEO%2F5V2oADueinidHS9A%3D
```

### 输出
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

