>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
DescribeBmNatPartSubnetBindIps 接口用于查询黑石NAT网关部分子网下绑定的IP信息

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
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见 <a href="/document/product/386/6718" title="公共请求参数">公共请求参数</a> 页面。其中，此接口的 Action 字段为 DescribeBmNatPartSubnetBindIps。

| 参数名称 |  描述 | 类型 |必选  |
|---------|---------|---------|---------|
| natId | NAT 网关统一 ID，例如：nat-xx454| String | 是 |
| unSubnetIds | 绑定的部分子网列表 | Aarry | 否 |

## 响应
### 响应示例
```
{
 "code": 0,
 "message": "",
 "codeDesc": "Success",
 "data": [{
  "unSubnetId": "<子网统一ID>",
  "subnetId": "<子网ID>",
  "natIpList": ["<绑定的IP>"]
 }]
}
```

### 响应参数

| 参数名称 | 描述 | 类型 |
|---------|---------|---------|
| code | 错误码，0：成功, 其他值：失败| Int |
| message | 错误信息| String |
| data.n | 查询NAT网关绑定的子网下 IP 信息 | Array |

data 数据结构如下：

| 参数名称 |描述 | 类型 |
|---------|---------|---------|
| data.n.unSubnetId | 子网统一 ID | String |
| data.n.subnetId |  子网 ID |Int |
| data.n.natIpList |  子网下绑定的IP列表 |Int |


## 错误码
 
| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
| -3047 | InvalidBmVpc.NotFound | 无效的 VPC。VPC 资源不存在，请再次核实您输入的资源信息是否正确，可通过 <a href="/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a> 接口查询 VPC。 |
| 13014 | BmVpcNat.NotFound | 无效的 NAT 网关，NAT 网关资源不存在。请再次核实您输入的资源信息是否正确 |

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
