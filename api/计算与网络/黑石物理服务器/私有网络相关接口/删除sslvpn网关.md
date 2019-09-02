>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
DeleteBmSslVpnGw 用于删除黑石sslvpn网关。

接口请求域名：bmvpc.api.qcloud.com


## 请求

语法示例：
```
GET https://bmvpc.api.qcloud.com/v2/index.php/?Action=DeleteBmSslVpnGw
    &<公共请求参数>
    &unVpcId=<私有网络唯一ID>
    &vpnGwId=<sslvpn网关唯一ID>
```

### 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为 DescribeBmSslVpnGwEx。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| unVpcId | 否 | string | 私有网络ID。 例如：vpc-kd7d06of，可通过<a href="https://cloud.tencent.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询。|
| vpnGwId | 否 | string | 查询指定的sslvpn网关唯一ID。 |




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
| -3262 | BmVpc.SslVpnUserExist | 存在sslvpn用户,需先删除此网关下的所有用户 |



## 实际案例
### 请求
```
GET https://bmvpc.api.qcloud.com/v2/index.php?
	Action=DeleteBmSslVpnGw
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
	&Nonce=11362
	&Timestamp=1515570588
	&Region=sh
	&unVpcId=vpc-0lapori0
	&vpnGwId=sshvpngw-fw0qxf9o
	&Signature=WALOeUYVxPeNL0ihou%2Bn59QxGuA%3D
```

### 响应
```
{
    "code": 0,
    "message": "",
}
```