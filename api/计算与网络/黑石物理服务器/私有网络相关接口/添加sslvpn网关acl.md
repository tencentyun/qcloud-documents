>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
AddBmSslVpnGwAcl 用于添加黑石sslvpn网关下的acl列表。 acl的position为每条acl的唯一标识，acl的匹配规则为从position最小到最大，匹配到后终止不再执行后面的匹配。此接口成功后返回的sslvpn网关所有的acl列表。

接口请求域名：bmvpc.api.qcloud.com


## 请求

语法示例：
```
GET https://bmvpc.api.qcloud.com/v2/index.php/?Action=AddBmSslVpnGwAcl
    &<公共请求参数>
    &unVpcId=<私有网络唯一ID>
	&vpnGwId=<sslvpn网关唯一ID>
	&aclRuleList.0.dstCidr=<目标网段Cidr>
	&aclRuleList.0.direction=ingress
	&aclRuleList.0.protocol=<协议>
	&aclRuleList.0.ipVersion=4
	&aclRuleList.0.srcCidr=<源网段Cidr>
	&aclRuleList.0.action=<动作>
	&aclRuleList.0.position=<标识ID>
	&Signature=PQZ%2FE%2Bs8FbSfZXoCVqg52khNfdg%3D
 

```

### 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为 AddBmSslVpnGwAcl。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| unVpcId | 是 | string | 私有网络ID。 例如：vpc-kd7d06of，可通过<a href="https://cloud.tencent.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询。|
| vpnGwId | 是 | string | sslvpn网关唯一ID。 |
| aclRuleList | 是 || array | aclRule数组 |
| aclRuleList.n.position | 是 | int | 每条acl的唯一标识，从1开始，最大50（包括）。|
| aclRuleList.n.ipVersion | 是 | int | 目前只支持ip V4, 值为4。|
| aclRuleList.n.protocol | 是 | String | 支持tcp udp icmp any。|
| aclRuleList.n.srcCidr | 是 | String | 源ip网段，cidr形式, 默认169.254.0.0/16, 为vpn客户端网段, 必须与已有网络独立不重叠。|
| aclRuleList.n.dstCidr | 是 | String | 目标ip网段，cidr形式,如 192.168.10.0/24。 必须在用户私有网络unVpcId内或为私有网络自身。|
| aclRuleList.n.direction | 是 | string | 规则生效方向，目前只有ingress。|
| aclRuleList.n.action | 是 | string | 规则生效动作，allow 或 deny。|
| aclRuleList.n.portRange | 是 | string | 如果protocol为tcp或者udp生效，否则填null。 两种：1.单个port,  (0, 65535) 范围: p1:p2 (p1,p2的范围为0:65535)。|



## 响应
响应示例：
```
 {
    "code": 0,
    "message": "",
    "totalCount": 2,
    "data": [
        {
            "dstCidr": "10.88.0.0/16",
            "direction": "ingress",
            "protocol": "tcp",
            "portRange": "0:65535",
            "ipVersion": 4,
            "srcCidr": "10.254.0.0/16",
            "action": "allow",
            "position": 50
        },
        {
            "dstCidr": "10.88.0.0/24",
            "direction": "ingress",
            "protocol": "icmp",
            "portRange": null,
            "ipVersion": 4,
            "srcCidr": "10.254.0.0/16",
            "action": "allow",
            "position": 3
        }
    ]
}
```
### 响应参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | int | 错误码。0：成功, 其他值：失败|
| message | string | 错误信息|
| totalCount | int | 返回的sslvpn网关个数|
| data | array | 返回的sslvpn网关所有的acl列表 |
| data.n.position | int | 每条acl的唯一标识。|
| data.n.ipVersion | int | 目前只支持ip V4, 值为4。|
| data.n.srcCidr | String | 源ip网段，cidr形式,如 192.168.10.0/24, 为创建时返回的ipPool段内的ip段。|
| data.n.dstCidr | String | 目标ip网段，cidr形式,如 192.168.10.0/24。为用户私有网络unVpcId内的子网|
| data.n.direction | string | 规则生效方向，目前只有ingress。|
| data.n.action | string | 规则生效动作，allow 或 deny。|
| data.n.portRange | string | 如果protocol为tcp或者udp，必须指定port或范围：1).单个port,  2).范围: p1:p2 (p1,p2的范围为0:65535); 如非tcp或udp, portRange填null。|


## 错误码
以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。
 
| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
| 10001 | BmVpc.InvalidParameterValue | 参数设置错误，具体错误信息可查看返回的message信息 |
| -3264 | BmVpc.SslVpnNotExist | sslvpn不存在 |




## 实际案例
### 请求
```
GET https://bmvpc.api.qcloud.com/v2/index.php?
	Action=AddBmSslVpnGwAcl
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
	&Nonce=11362
	&Timestamp=1515570588
	&Region=sh
	&unVpcId=vpc-0lapori0
	&vpnGwId=sshvpngw-0lrdvko4
	&aclRuleList.0.dstCidr=10.88.0.0%252f24
	&aclRuleList.0.direction=ingress
	&aclRuleList.0.protocol=icmp
	&aclRuleList.0.ipVersion=4
	&aclRuleList.0.srcCidr=10.254.0.0%252f16
	&aclRuleList.0.action=allow
	&aclRuleList.0.position=3
	&Signature=Ni3ZCuIFjylUZya7CBp5Sixl0NY%3D
```

### 响应
```
 {
    "code": 0,
    "message": "",
    "totalCount": 2,
    "data": [
        {
            "dstCidr": "10.88.0.0/16",
            "direction": "ingress",
            "protocol": "tcp",
            "portRange": "0:65535",
            "ipVersion": 4,
            "srcCidr": "10.254.0.0/16",
            "action": "allow",
            "position": 50
        },
        {
            "dstCidr": "10.88.0.0/24",
            "direction": "ingress",
            "protocol": "icmp",
            "portRange": null,
            "ipVersion": 4,
            "srcCidr": "10.254.0.0/16",
            "action": "allow",
            "position": 3
        }
    ]
}
```