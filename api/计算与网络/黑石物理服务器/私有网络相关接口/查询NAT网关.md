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
    &unVpcId=<vpc网络ID>
    &offset=<初始行的偏移量>
    &limit=<每页行数>
    &orderField=<排序字段>
	&orderDirection=<排序类型>
```
### 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/document/product/386/6718" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为DescribeBmNatGateway

| 参数名称 |  描述 | 类型 |必选  |
|---------|---------|---------|---------|
| natId | NAT网关统一ID，例如：nat-xx454| String | 否 |
| natName | NAT网关名称 (支持模糊查找) | String | 否 |
| unVpcId | 私有网络ID值，例如：vpc-kd7d06of，可通过<a href="/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询。| Int | 否 |
| offset |  初始行的偏移量，默认为0| Int | 否 |
| limit |  每页行数，默认为20，最大支持50。| Int | 否 |
| orderField |按某个字段排序，默认不排序。<br>支持字段：natId。| String | 否 |
| orderDirection | 升序（asc）或降序（desc），默认：desc。| String | 否 |


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
            "vpcId": <vpc网络ID>,
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
            "exclusive": <NAT网关共享型和独占型标识>,
            "createTime": <创建时间>
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
| data.n | 查询的NAT网关信息数组 | Array |

data数据结构如下：

| 参数名称 |描述 | 类型 |
|---------|---------|---------|
| data.n.natId |  NAT网关统一ID，例如：nat-xx454 |String |
| data.n.natName | NAT网关名称 | String |
| data.n.unVpcId |私有网络统一ID，例如：vpc-xgfd55d | String | 
| data.n.vpcId | 私有网络ID | Int |
| data.n.vpcName |  vpc网络名称 |String |
| data.n.state | NAT网关状态，1:运行中, 0:不可用 | Int |
| data.n.productionStatus |  NAT网关的生产状态, 0: 创建中, 1: 创建成功, 2: 创建失败 |Int |
| data.n.maxConcurrent |  NAT网关并发连接上限, 100w:小型, 300w:中型, 1000w:大型，详见NAT网关产品说明 |Int |
| data.n.ntype |  对应NAT网关并发连接上限, 取值为small, middle, big, 分别对应小型、中型、大型|String |
| data.n.exclusive |  NAT网关共享型和独占型标识，0表示共享型NAT网关，1表示独占型NAT网关 |Int 
| data.n.eipCount |  NAT网关绑定eip的个数 |String |
| data.n.eipSet |  NAT网关绑定的弹性IP列表，例如：[183.60.249.11] |Array |
| data.n.createTime | NAT网关网关创建时间，例如：2016-06-21 12:01:23 |String | 


## 错误码
 
| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
| -3047 | InvalidBmVpc.NotFound | 无效的VPC。VPC资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询VPC。 |
| 13014 | BmVpcNat.NotFound | 无效的NAT网关，NAT网关资源不存在。请再次核实您输入的资源信息是否正确 |

## 实际案例

### 输入
```
GET https://bmvpc.api.qcloud.com/v2/index.php?
	Action=DescribeBmNatGateway
	&SecretId=AKID1ub7R1JoyBF7nHqjk7IH8nGWaR6Yezwd
	&Nonce=4557
	&Timestamp=1507692902
	&Region=gz
	&unVpcId=300006
	&Signature=4dq8JXWTyg9n8FuVckaIhg8Pnbw%3D
```

### 输出
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
            "exclusive": 0,
            "createTime": "2017-05-12 11:35:57"
        }
    ]
}
```