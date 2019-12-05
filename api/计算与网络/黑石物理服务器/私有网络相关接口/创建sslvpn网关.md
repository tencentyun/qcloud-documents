>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
CreateBmSslVpnGw 用于创建黑石sslvpn网关，每VPC只限一个sslvpn网关。

接口请求域名：bmvpc.api.qcloud.com


## 请求

语法示例：
```
GET https://bmvpc.api.qcloud.com/v2/index.php/?Action=CreateBmSslVpnGw
    &<公共请求参数>
    &unVpcId=<私有网络唯一ID>
    &vpnGwName=<sslvpn网关名称>
    &txPeakLimit=<最大出带宽>
    &rxPeakLimit=<最大入带宽>
```

### 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为 CreateBmSslVpnGw。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| unVpcId | 是 | string | 要创建网关所在的私有网络ID。 例如：vpc-kd7d06of，可通过<a href="https://cloud.tencent.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询。|
| vpnGwName | 是 | string | 网关名称，英文字母或数字组成 |
| publicPort | 否 | int | 网关的公网端口 (0-65535)， 默认443。 |
| clientIPPool | 否 | string | vpn客户端所在的网段CIDR，用户填写时必须要确保此网段与用户客户端机器所在现有网段不冲突, 默认为169.254.0.0/16。|
| txPeakLimit | 是 | int | 网关最大出带宽，最大100Mbps。|
| rxPeakLimit | 是 | int | 网关最大入带宽，最大100Mbps。|



## 响应
响应示例：
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "sslVpnGw": {
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
            "zoneId": 1000100002
        }
    }
}
```
### 响应参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | int | 错误码。0：成功, 其他值：失败|
| message | string | 错误信息|
| data | array | 返回操作的任务ID，创建结果可调用<a href="https://cloud.tencent.com/document/api/386/9356" title="查询NAT网关操作状态">查询NAT网关操作状态</a>查询 |

## 错误码
以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。
 
| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
| 10001 | BmVpc.InvalidParameterValue | 参数设置错误，具体错误信息可查看返回的message信息 |
| -3047 | InvalidBmVpc.NotFound | 无效的VPC。VPC资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="https://cloud.tencent.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询VPC。 |
| -3261 | BmVpc.SslVpnPerVpcLimit | 私有网络下sslvpn网关数超过最大限制，每VPC只限一个。 |


## 实际案例
### 请求
```
GET https://bmvpc.api.qcloud.com/v2/index.php?
	Action=CreateBmSslVpnGw
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
	&Nonce=11362
	&Timestamp=1515570588
	&Region=sh
	&unVpcId=vpc-0lapori0
	&vpnGwName=testma
	&txPeakLimit=10
	&rxPeakLimit=10
	&Signature=tvpK%2BxnptHI1O0WgnMG6C9pVBxc%3D
```

### 响应
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "sslVpnGw": {
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
            "zoneId": 1000100002
        }
    }
}
```