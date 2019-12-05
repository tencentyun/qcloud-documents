>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
DescribeBmSslVpnGw 用于获取黑石sslvpn网关。

接口请求域名：bmvpc.api.qcloud.com


## 请求

语法示例：
```
GET https://bmvpc.api.qcloud.com/v2/index.php/?Action=DescribeBmSslVpnGw
    &<公共请求参数>
    &unVpcId=<私有网络唯一ID>
```

### 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为 DescribeBmSslVpnGwEx。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| unVpcId | 否 | string | 私有网络ID。 例如：vpc-kd7d06of，可通过<a href="https://cloud.tencent.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询。|
| vpnGwId | 否 | string | 查询指定的sslvpn网关唯一ID， 如不存在返回空。 |
| orderField | 否 | string | 按某个字段排序，目前仅支持createTime。 |
| orderDirection | 否 | string | 排序顺序，升序（asc）或降序（desc），默认：asc。|
| zoneId | 是 | Int | 可用区ID，用于非指定查询时过滤。 需调用<a href="/doc/api/386/6634" title="查询地域以及可用区">查询地域以及可用区(DescribeRegions)接口</a> 获取zoneId |



## 响应
响应示例：
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": [
        {
            "vpnGwId": "sshvpngw-0lrdvko4",
            "unVpcId": "vpc-0lapori0",
            "vpnGwName": "testma",
            "domain": "206001",
            "publicIp": "139.199.40.244",
            "publicPort": 443,
            "clientIPPool": "10.254.0.0/16",
            "txPeakLimit": 10,
            "rxPeakLimit": 10,
            "sessionLimit": 10,
            "createTime": "2018-01-10 16:23:25",
            "zoneId": 1000100002
        }
    ],
    "totalCount": 1
}
```
### 响应参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | int | 错误码。0：成功, 其他值：失败|
| message | string | 错误信息|
| totalCount | int | 返回的sslvpn网关个数|
| data | array | 返回的sslvpn网关数组 |
| data.n.vpnGwId | String | sslvpn网关ID。|
| data.n.unVpcId | String | 用户私有网络ID。|
| data.n.vpnGwName | int | 网关名称。|
| data.n.domain | string | 系统分配的域，对应登录vpn时inode client的域。|
| data.n.publicIp | string | 网关ip。|
| data.n.publicPort | int | 网关port。|
| data.n.zoneId | int | 子网所在可用区ID,示例:200001。|
| data.n.clientIPPool | string | 子网的vlanid。|
| data.n.txPeakLimit | int | 网关最大出带宽。|
| data.n.rxPeakLimit | int | 网关最大入带宽。|
| data.n.createTime | string | 网关的创建时间，如 2018-01-02 00:00:23。|
## 错误码
以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。
 
| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
| 10001 | BmVpc.InvalidParameterValue | 参数设置错误，具体错误信息可查看返回的message信息 |




## 实际案例
### 请求
```
GET https://bmvpc.api.qcloud.com/v2/index.php?
	Action=DescribeBmSslVpnGw
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
	&Nonce=11362
	&Timestamp=1515570588
	&Region=sh
	&unVpcId=vpc-0lapori0
	&Signature=Ni3ZCuIFjylUZya7CBp5Sixl0NY%3D
```

### 响应
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": [
        {
            "vpnGwId": "sshvpngw-0lrdvko4",
            "unVpcId": "vpc-0lapori0",
            "vpnGwName": "testma",
            "domain": "206001",
            "publicIp": "139.199.40.244",
            "publicPort": 443,
            "clientIPPool": "10.254.0.0/16",
            "txPeakLimit": 10,
            "rxPeakLimit": 10,
            "sessionLimit": 10,
            "createTime": "2018-01-10 16:23:25",
            "zoneId": 1000100002
        }
    ],
    "totalCount": 1
}
```