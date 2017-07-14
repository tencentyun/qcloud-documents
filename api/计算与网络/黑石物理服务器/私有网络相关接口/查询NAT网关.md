## 1. 接口描述

本接口(DescribeBmNatGateway)用于查询黑石NAT网关
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font>


## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为DescribeNatGateway

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| natId | 否 | String | NAT网关统一ID，例如：nat-xx454|
| natName | 否 | String | NAT网关名称 (支持模糊查找) |
| vpcId | 否 | String | 私有网络ID值，可使用vpcId或unVpcId，建议使用unVpcId，例如：vpc-kd7d06of，可通过<a href="https://www.qcloud.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询。|
| offset | 否 | Int | 初始行的偏移量，默认为0|
| limit | 否 | Int | 每页行数，默认为20，最大支持50。|
| orderField | 否 | String | 按某个字段排序，默认不排序。<br>支持字段：natId。|
| orderDirection | 否 | String | 升序（asc）或降序（desc），默认：desc。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | int | 错误码, 0: 成功, 其他值: 失败|
| message | string | 错误信息|
| totalCount | int | 查询的NAT网关总数 |
| data.n | array | 查询的NAT网关信息数组 |

**data数据结构如下：**

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| data.n.natId | string | NAT网关统一ID，例如：nat-xx454 |
| data.n.vpcId | Int | 私有网络ID |
| data.n.unVpcId | string | 私有网络统一ID，例如：vpc-xgfd55d |
| data.n.natName | string | NAT网关名称 |
| data.n.state | int | NAT网关状态，1:运行中, 0:不可用 |
| data.n.maxConcurrent | int | NAT网关并发连接上限, 100w:小型, 300w:中型, 1000w:大型，详见<a href="">NAT网关产品说明</a> |
| data.n.eipCount | string | NAT网关统一ID，例如：nat-xx454 |
| data.n.eipSet | array | 网关所有弹性IP信息，例如：[183.60.249.11] |
| data.n.createTime | string | NAT网关网关创建时间，例如：2016-06-21 12:01:23 |
| data.n.productionStatus | int | NAT网关的生产状态, 0: 创建中, 1: 创建成功, 2: 创建失败 |
| data.n.subnetAll | int | 是否选择了新建子网包括后续子网选项 |
| data.n.subnets | array | NAT网关绑定的子网列表 |

 ## 4. 错误码表
 以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://www.qcloud.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。
 
| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
| -3047 | InvalidBmVpc.NotFound | 无效的VPC。VPC资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="https://www.qcloud.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询VPC。 |
| 13014 | BmVpcNat.NotFound | 无效的NAT网关，NAT网关资源不存在。请再次核实您输入的资源信息是否正确，可通过DescribeBmNatGateway接口查询NAT网关。 |

## 5. 示例
输入
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DescribeBmNatGateway
&<<a href="https://www.qcloud.com/doc/api/229/6976">公共请求参数</a>>
&vpcId=vpc-8e0ypm3z
</pre>
输出
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "totalCount": 1,
    "data": [
        {
            "natId": "nat-787jwhek",
            "natName": "testnat",
            "unVpcId": "vpc-34cxlz7z",
            "vpcId": 4097,
            "vpcName": "test",
            "state": 0,
            "productionStatus": 1,
            "eipCount": 4,
            "eipSet": [
                "115.159.240.68",
                "115.159.240.83",
                "115.159.240.86",
                "115.159.240.96"
            ],
            "maxConcurrent": 1000000,
            "ntype": "small",
            "subnetAll": "0",
            "createTime": "2017-05-10 20:13:00",
            "subnets": [
                {
                    "name": "vm",
                    "unSubnetId": "subnet-jv24ivq0",
                    "subnetId": 8946
                }
            ]
        }
    ]
}
```

