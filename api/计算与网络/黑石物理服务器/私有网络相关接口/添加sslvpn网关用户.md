>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
AddBmSslVpnGwUser 用于添加黑石sslvpn网关用户密码。一个网关下最大限制为10个用户。

接口请求域名：bmvpc.api.qcloud.com


## 请求

语法示例：
```
GET https://bmvpc.api.qcloud.com/v2/index.php/?Action=AddBmSslVpnGwUser
    &<公共请求参数>
	&vpnGwId=<sslvpn网关唯一ID>
    &userName=<sslvpn网关用户名>
    &pin=<用户密码>
```

### 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为 AddBmSslVpnGwUser。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpnGwId | 是 | string | 网关唯一ID |
| userName | 是 | string | sslvpn网关用户名， 仅支持英文、数字，4-20个字符。 |
| pin | 是 | string | 用户密码，密码需要8-16个字符，至少包含英文、数字和符号!#$%&^*()中的2种。|



## 响应
响应示例：
```
{
    "code": 0,
    "message": "",
}

```
### 响应参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | int | 错误码。0：成功, 其他值：失败|
| message | string | 错误信息|


## 错误码
以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。
 
| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
| 10001 | BmVpc.InvalidParameterValue | 参数设置错误，具体错误信息可查看返回的message信息 |
| -3264 | BmVpc.SslVpnNotExist | 私有网络下sslvpn网关不存在。 |
| -3263 | BmVpc.SslVpnUserPerVpnGwLimit | sslvpn网关下用户数超过最大限制，限制最大10个。 |


## 实际案例
### 请求
```
GET https://bmvpc.api.qcloud.com/v2/index.php?
	Action=AddBmSslVpnGwUser
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
	&Nonce=11362
	&Timestamp=1515570588
	&Region=sh
	&vpnGwId=sshvpngw-hm6uj2yu
	&vpnGwName=testma111
	&userName=ssdfffffA
	&pin=a123dsasd
	&Signature=tvpK%2BxnptHI1O0WgnMG6C9pVBxc%3D
```

### 响应
```
{
    "code": 0,
    "message": "",
}
```