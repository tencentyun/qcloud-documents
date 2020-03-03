## 1. 接口描述

本接口（DescribeNatGateway）用于查询 NAT 网关。
接口请求域名：`vpc.api.qcloud.com`


## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见 <a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a> 页面。其中，此接口的 Action 字段为 DescribeNatGateway。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| natId | 否 | String | NAT网关统一 ID，例如：nat-xx454|
| natName | 否 | String | NAT网关名称 (支持模糊查找) |
| vpcId | 否 | String | 私有网络 ID 或统一 ID，建议使用统一 ID，例如：vpc-dfdg42d|
| offset | 否 | Int | 初始行的偏移量，默认为0|
| limit | 否 | Int | 每页行数，默认为20，最大支持50|
| orderField | 否 | String | 按某个字段排序，默认不排序。<br>支持字段：natId|
| orderDirection | 否 | String | 升序（asc）或降序（desc），默认：desc|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | int | 错误码，0：成功，其他值：失败|
| message | string | 错误信息|
| totalCount | int | 查询的 NAT 网关总数 |
| data.n | array | 查询的 NAT 网关信息数组 |

**data数据结构如下：**

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| data.n.natId | string | NAT网关统一ID，例如：nat-xx454 |
| data.n.vpcId | string | 私有网络统一ID，例如：vpc-xgfd55d |
| data.n.natName | string | NAT网关名称 |
| data.n.state | int | NAT网关状态，0:运行中, 1:不可用, 2:欠费停服 |
| data.n.maxConcurrent | int | NAT网关并发连接上限, 100w:小型, 300w:中型, 1000w:大型，详见<a href="">NAT网关产品说明</a> |
| data.n.bandwidth | int | 网关最大外网出带宽(单位:Mbps)，详见<a href="">NAT网关产品说明</a> |
| data.n.eipCount | string | 弹性 IP 的个数，例如：nat-xx454 |
| data.n.eipSet | array | 网关所有弹性IP信息，例如：[183.60.249.11] |
| data.n.createTime | string | NAT网关网关创建时间，例如：2016-06-21 12:01:23 |
| data.n.productionStatus | int | NAT网关的生产状态, 0: 创建中, 1: 创建成功, 2: 创建失败, 3: 变更中, 4: 变更失败, 5: 删除中, 6: 删除失败 |

 ## 4. 错误码表
 以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见 <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码"> VPC错误码</a>。
 
| 错误码 | 描述 |
|---------|---------|
| InvalidVpc.NotFound | 无效的VPC，VPC资源不存在。请再次核实您输入的资源信息是否正确，可通过 <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a> 接口查询 VPC |
| InvalidNatGatewayId.NotFound | 无效的NAT网关，NAT网关资源不存在。请再次核实您输入的资源信息是否正确，可通过 <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2NAT%e7%bd%91%e5%85%b3?viewType=preview" title="DescribeNatGateway">DescribeNatGateway</a> 接口查询NAT网关 |

## 5. 示例
输入
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DescribeNatGateway
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&vpcId=vpc-8e0ypm3z
</pre>
输出
```
{
    "code":"0",
    "message":"",
    "totalCount":1,
    "data": [
        {
            "appId": "1351000042",
            "vpcId": "vpc-8e0ypm3z",
            "vpcName": "alblack.bbb1",
            "natId": "nat-dhfpwhtm",
            "natName": "apollan",
            "maxConcurrent": 0,
            "eipCount": 1,
            "createTime": "2016-06-21 12:01:23",
            "state": 1,
            "bandwidth": 90000,
            "productionStatus": 1,
            "eipSet": [
                "183.60.249.11"
            ]
        }
     ]
}
```

