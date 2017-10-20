## 功能描述
DescribeBmNatGateway 接口用于查询租户创建的NAT网关列表信息，包括网关统一ID、网关名称、网关并发连接上限、绑定eip列表等

接口请求域名：bmvpc.api.qcloud.com


## 请求

### 请求示例
```
GET https://bmvpc.api.qcloud.com/v2/index.php/?Action=DescribeBmNatGateway
    &<公共请求参数>
    &natId=<NAT网关ID>
    &natName=<NAT网关名称>
    &vpcId=<vpc网络ID>
    &offset=<初始行的偏移量>
    &limit=<每页行数>
    &orderField=<排序字段>
	&orderDirection=<排序类型>
```
### 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为DescribeNatGateway

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| natId | 否 | String | NAT网关统一ID，例如：nat-xx454|
| natName | 否 | String | NAT网关名称 (支持模糊查找) |
| vpcId | 否 | Int | 私有网络ID值，可使用vpcId或unVpcId，建议使用unVpcId，例如：vpc-kd7d06of，可通过<a href="https://www.qcloud.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询。|
| offset | 否 | Int | 初始行的偏移量，默认为0|
| limit | 否 | Int | 每页行数，默认为20，最大支持50。|
| orderField | 否 | String | 按某个字段排序，默认不排序。<br>支持字段：natId。|
| orderDirection | 否 | String | 升序（asc）或降序（desc），默认：desc。|


## 响应
### 响应示例
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "totalCount": <NAT网关数目>,
    "data": [
        {
            "natId": <NAT网关ID>,
            "natName": <NAT网关名称>,
            "unVpcId": <VPC统一ID>,
            "vpcId": <VPCID>,
            "vpcName": <VPC名称>,
            "state": <NAT网关状态>,
            "productionStatus": <NAT网关生产状态>,
            "eipCount": <绑定至NAT网关的eip个数>,
            "eipSet": [
                <绑定的eip>
            ],
            "maxConcurrent":  <NAT网关并发连接上限>,
            "ntype": <NAT网关并发连接上限类型>,
            "subnetAll": <是否绑定全部子网>,
            "createTime": <创建时间>,
            "subnets": [
                {
                    "name": <子网名称>,
                    "unSubnetId": <子网统一ID>,
                    "subnetId": <子网ID>,
                    "subnetNatType": <绑定的子网类型>,
                    "cidrBlock": <子网网段>
                }
            ]
        }
    ]
}
```

### 响应参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码, 0: 成功, 其他值: 失败|
| message | String | 错误信息|
| totalCount | Int | 查询的NAT网关总数 |
| data.n | Array | 查询的NAT网关信息数组 |

data数据结构如下：

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| data.n.natId | String | NAT网关统一ID，例如：nat-xx454 |
| data.n.natName | String | NAT网关名称 |
| data.n.unVpcId | String | 私有网络统一ID，例如：vpc-xgfd55d |
| data.n.vpcId | Int | 私有网络ID |
| data.n.vpcName | String | vpc网络名称 |
| data.n.state | Int | NAT网关状态，1:运行中, 0:不可用 |
| data.n.productionStatus | Int | NAT网关的生产状态, 0: 创建中, 1: 创建成功, 2: 创建失败 |
| data.n.maxConcurrent | Int | NAT网关并发连接上限, 100w:小型, 300w:中型, 1000w:大型，详见<a href="">NAT网关产品说明</a> |
| data.n.ntype | String | 对应NAT网关并发连接上限, 取值为small, middle, big, 分别对应小型、中型、大型|
| data.n.eipCount | String | NAT网关绑定eip的个数 |
| data.n.eipSet | Array | NAT网关绑定的弹性IP列表，例如：[183.60.249.11] |
| data.n.createTime | String | NAT网关网关创建时间，例如：2016-06-21 12:01:23 |
| data.n.subnets | Array | NAT网关绑定的子网列表信息 |

subnets包含的数据结构如下：

|参数名称|类型|描述|
|-------|---|---------------|
|name|String|子网名称|
|unSubnetId|String|子网统一ID|
|subnetId|Int|子网ID|
|subnetNatType|Int|绑定的子网类型，0表示子网部分IP，1表示子网全部IP|
|cidrBlock|String|子网网段|

## 错误码
 
| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
| -3047 | InvalidBmVpc.NotFound | 无效的VPC。VPC资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="https://cloud.tencent.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询VPC。 |
| 13014 | BmVpcNat.NotFound | 无效的NAT网关，NAT网关资源不存在。请再次核实您输入的资源信息是否正确，可通过DescribeBmNatGateway接口查询NAT网关。 |

## 实际案例

### 请求
```
GET https://bmvpc.api.qcloud.com/v2/index.php?
	Action=DescribeBmNatGateway
	&SecretId=AKID1ub7R1JoyBF7nHqjk7IH8nGWaR6Yezwd
	&Nonce=4557
	&Timestamp=1507692902
	&Region=gz
	&vpcId=300006
	&Signature=4dq8JXWTyg9n8FuVckaIhg8Pnbw%3D
```

### 响应
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "totalCount": 1,
    "data": [
        {
            "natId": "nat-3247x9jj",
            "natName": "test3",
            "unVpcId": "vpc-ab3y4x6m",
            "vpcId": 300006,
            "vpcName": "mgt_two",
            "state": 0,
            "productionStatus": 1,
            "eipCount": 2,
            "eipSet": [
                "211.129.128.123",
                "211.129.138.229"
            ],
            "maxConcurrent": 10000000,
            "ntype": "big",
            "createTime": "2017-05-12 11:35:57",
            "subnets": [
                {
                    "name": "wefwefwe",
                    "unSubnetId": "subnet-00al7z8l",
                    "subnetId": 224,
                    "subnetNatType": 1,
                    "cidrBlock": "10.11.5.0/24"
                },
                {
                    "name": "test0717",
                    "unSubnetId": "subnet-4qh1a0bt",
                    "subnetId": 263,
                    "subnetNatType": 1,
                    "cidrBlock": "10.11.8.0/24"
                }
            ]
        }
    ]
}
```