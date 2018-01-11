## 功能描述
DescribeBmNatPartSubnetBindIps 接口用于查询黑石NAT网关部分子网下绑定的IP

接口请求域名：bmvpc.api.qcloud.com


## 请求

### 请求示例
```
GET https://bmvpc.api.qcloud.com/v2/index.php/?Action=DescribeBmNatPartSubnetBindIps
    &<公共请求参数>
    &natId=<NAT网关ID>
    &unSubnetIds.n=<子网统一ID>

```
### 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/document/product/386/6718" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为DescribeBmNatPartSubnetBindIps

| 参数名称 |  描述 | 类型 |必选  |
|---------|---------|---------|---------|
| natId | NAT网关统一ID，例如：nat-xx454| String | 是 |
| unSubnetIds | 绑定的部分子网 | Aarry | 否 |

## 响应
### 响应示例
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": [
        {
			"unSubnetId": <子网统一ID>,
            "subnetId": <子网ID>,
            "subnetNatType": <子网NAT绑定的类型>,
            "natIpList": [
                <绑定的IP>
            ],
        }
    ]
}
```

### 响应参数

| 参数名称 | 描述 | 类型 |
|---------|---------|---------|
| code | 错误码, 0: 成功, 其他值: 失败| Int |
| message | 错误信息| String |
| totalCount |  查询的NAT网关总数 | Int |
| data.n | 查询NAT网关绑定的子网下IP信息 | Array |

data数据结构如下：

| 参数名称 |描述 | 类型 |
|---------|---------|---------|
| data.n.subnets.n.unSubnetId | 子网统一ID | String |
| data.n.subnetId |  子网ID |Int |
| data.n.natIpList |  该子网下绑定的IP |Int |


## 错误码
 
| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
| -3047 | InvalidBmVpc.NotFound | 无效的VPC。VPC资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询VPC。 |
| 13014 | BmVpcNat.NotFound | 无效的NAT网关，NAT网关资源不存在。请再次核实您输入的资源信息是否正确 |

## 实际案例

### 输入
```
GET https://bmvpc.api.qcloud.com/v2/index.php?
	Action=DescribeBmNatPartSubnetBindIps
	&SecretId=AKID1ub7R1JoyBF7nHqjk7IH8nGWaR6Yezwd
	&Nonce=4557
	&Timestamp=1507692902
	&Region=gz
	&natId=nat-axd6t16w
	&unSubnetIds.1=subnet-5n0j08b2
	&Signature=4dq8JXWTyg9n8FuVckaIhg8Pnbw%3D
```

### 输出
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": [
        {
            "subnetId": 858,
            "natIpList": [
                "172.16.128.12",
                "172.16.128.13",
                "172.16.128.14",
                "172.16.128.15",
                "172.16.128.16",
                "172.16.128.17",
                "172.16.128.18",
                "172.16.128.19"
            ],
            "unSubnetId": "subnet-5n0j08b2"
        }
    ]
}
```