>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述

SetOutBandVPNAuthPwd接口用于设置带外VPN认证用户密码。

创建VPN认证用户: 先调用<a href="/doc/api/386/6679" title="获取带外VPN信息">获取带外VPN信息(GetOutBandVPNAuthInfo)接口</a> 获取VPN信息，如GetOutBandVPNAuthInfo返回的be_first=true, 则必须要调用本API，并设置入参createOrUpdate值为create。

设置认证用户的密码： 已经调用本API创建过VPN认证用户，直接调用本API设置。

接口请求域名：bm.api.qcloud.com

## 请求
### 请求示例
```
GET https://bmeip.api.qcloud.com/v2/index.php?
	&Action=SetOutBandVPNAuthPwd
	&<公共请求参数>
	&password=<vpn用户密码>
	&createOrUpdate=<create or update>
```
### 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见[公共请求参数页面](/document/product/386/6718)。其中，此接口的Action字段为 SetOutBandVPNAuthPwd。

|参数名称|必选|类型|描述|
|-------|----|---|----|
| password | 是 | String | 用户设置的vpn认证密码。密码需要8-16个字符，至少包含英文、数字和符号!#$%&^*()中的2种 |
| createOrUpdate | 是 | String | 取值为create或者update字符串。 create: 创建此appId的VPN帐号，只有在<a href="/doc/api/386/6679" title="获取带外VPN信息">获取带外VPN信息(GetOutBandVPNAuthInfo)接口</a> 返回的be_first=true时需要创建；update:修改此VPN认证帐号的密码，前提条件：已经调用本API创建了VPN认证用户。 |



## 响应
### 响应示例
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": null
}
```
### 响应参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码, 0: 成功, 其他值: 失败，具体含义可以参考[错误码](/document/product/386/6725)。 |
| message |   String | 错误信息 |
| data |   null | 返回申请的eip实例对应的异步任务信息，具体结构描述如下 |



## 错误码

| code |codeDesc| 描述 |
|------|------|------|
| 10004 |OperationDenied| 没有操作权限 |
| 10100 |InternalError.ObAuthAccessError| 访问鉴权模块错误 |
| 10101 |InternalError.ObAuthError|鉴权模块返回错误 |




## 实际案例

### 输入
```
GET https://bm.api.qcloud.com/v2/index.php?
	Action=SetOutBandVPNAuthPwd
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
	&Nonce=52684
	&Timestamp=1508212392
	&Region=gz
	&password=tencentV%89
	&createOrUpdate=update
	&Signature=sU7JPpjAVbwYw%2Fp0m6ysu65VPac%3D
```

### 输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": null
}
```

