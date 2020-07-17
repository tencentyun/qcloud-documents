>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
DescribeBmNatGateway 接口用于查询租户创建的NAT网关列表信息，包括网关统一 ID、网关名称、网关并发连接上限、绑定 eip 列表等。
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
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/document/product/386/6718" title="公共请求参数">公共请求参数</a>页面。其中，此接口的 Action 字段为 DescribeBmNatGateway。

| 参数名称 |  描述 | 类型 |必选  |
|---------|---------|---------|---------|
| natId | NAT 网关统一 ID，例如：nat-xx454| String | 否 |
| natName | NAT 网关名称 (支持模糊查找) | String | 否 |
| unVpcId | 私有网络 ID 值，例如：vpc-kd7d06of，可通过<a href="/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询。| Int | 否 |
| offset |  初始行的偏移量，默认为 0| Int | 否 |
| limit |  每页行数，默认为 20，最大支持 50。| Int | 否 |
| orderField |按某个字段排序，默认不排序。<br>支持字段：natId。| String | 否 |
| orderDirection | 升序（asc）或降序（desc），默认：desc。| String | 否 |


## 响应
### 响应示例
```
{
 "code": 0,
 "message": "",
 "codeDesc": "Success",
 "totalCount": "< NAT网关数目 > ",
 "data": [{
  "natId": "< NAT网关ID >",
  "natName": "< NAT网关名称 >",
  "unVpcId": "< VPC统一ID >",
  "vpcId": "< vpc网络ID >",
  "vpcName": "< VPC名称 >",
  "state": "< NAT网关状态 >",
  "forwardMode": "< 转发方式 >",
  "productionStatus": "< NAT网关生产状态 >",
  "eipCount": "< 绑定至NAT网关的eip个数 >",
  "eipSet": ["<绑定的eip >"],
  "maxConcurrent": "< NAT网关并发连接上限 >",
  "ntype": "< NAT网关并发连接上限类型 >",
  "exclusive": "< NAT网关共享型和独占型标识 >",
  "createTime": "< 创建时间 >"
 }]
}

```

### 响应参数

| 参数名称 | 描述 | 类型 |
|---------|---------|---------|
| code | 错误码，0：成功，其他值：失败| Int |
| message | 错误信息| String |
| totalCount |  查询的 NAT 网关总数 | Int |
| data.n | 查询的 NAT 网关信息数组 | Array |

data 数据结构如下：

| 参数名称 |描述 | 类型 |
|---------|---------|---------|
| data.n.natId |  NAT 网关统一 ID，例如：nat-xx454 |String |
| data.n.natName | NAT 网关名称 | String |
| data.n.unVpcId |私有网络统一 ID，例如：vpc-xgfd55d | String | 
| data.n.vpcId | 私有网络 ID | Int |
| data.n.vpcName |  vpc 网络名称 |String |
| data.n.state | NAT 网关状态，1：运行中，0：不可用 | Int |
| data.n.productionStatus |  NAT 网关的生产状态，0：创建中，1：创建成功，2：创建失败 |Int |
| data.n.maxConcurrent |  NAT 网关并发连接上限，100w：小型, 300w：中型, 1000w：大型，详见 NAT 网关产品说明 |Int |
| data.n.ntype |  对应 NAT 网关并发连接上限, 取值为 small，middle，big，分别对应小型、中型、大型|String |
| data.n.forwardMode | NAT 网关的转发方式。当值为 0 时表示 IP 方式，值为 1 时表示 cidr 方式| Int |
| data.n.exclusive |  NAT 网关共享型和独占型标识，0 表示共享型 NAT 网关，1 表示独占型 NAT 网关 |Int 
| data.n.eipCount |  NAT 网关绑定 eip 的个数 |String |
| data.n.eipSet |  NAT 网关绑定的弹性 IP 列表，例如：`[183.60.249.11]` |Array |
| data.n.createTime | NAT 网关网关创建时间，例如：2016-06-21 12:01:23 |String | 


## 错误码
 
| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
| -3047 | InvalidBmVpc.NotFound | 无效的 VPC。VPC 资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询 VPC。 |
| 13014 | BmVpcNat.NotFound | 无效的 NAT 网关，NAT 网关资源不存在。请再次核实您输入的资源信息是否正确 |

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
			"forwardMode": 1,
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
