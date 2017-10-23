## 1. 接口描述
 
本接口（DescribeVpcEx）用于查询私有网络列表。
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font>

本接口不传参数时，返回默认排序下的前20条VPC信息。

 

## 2. 输入参数
 以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为DescribeVpcEx。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 否 | String | 系统分配的私有网络ID，支持升级前的vpcId，也支持升级后的unVpcId。 |
| vpcName | 否 | String | 私有网络名称，支持模糊搜索。 |
| offset | 否 | Int | 初始行的偏移量，默认为0。 |
| limit | 否 | Int | 每页行数，默认为20。 |
| orderField | 否 | String | 按某个字段排序，目前仅支持createTime,vpcName排序，默认按createTime排序。 |
| orderDirection | 否 | String | 升序（asc）还是降序（desc），默认：desc。 |

 

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码, 0表示成功，其他值表示失败。详见错误码页面的<a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="公共错误码">公共错误码</a>。|
| message | String | 模块错误信息描述，与接口相关。|
| totalCount | Int | 开发商VPC总数。|
| data.n | Array | VPC信息组。|
| data.n.vpcId | String | 系统分配的vpcId，例如：gz_vpc_266。|
| data.n.unVpcId | String | 系统分配的新vpcID，由子网ID升级而来，推荐使用新vpcId，示例:vpc-5gu2jxf4。|
| data.n.vpcName | String | 私有网络名称。|
| data.n.cidrBlock | String | 私有网络网段，例如：192.168.0.1/24。|
| data.n.subnetNum | Int | VPC下子网个数。|
| data.n.routeTableNum | Int | VPC下路由表个数。|
| data.n.vpnGwNum | Int | VPC下VPN网关个数。|
| data.n.vpcPeerNum | Int | VPC下对等连接个数。|
| data.n.vpcDeviceNum | Int | VPC下云主机个数。|
| data.n.classicLinkNum | Int | VPC下与VPC互通的基础网络设备个数。|
| data.n.vpgNum | Int | VPC下专线网关个数。|
| data.n.natNum | Int | VPC下NAT网关个数。|
| data.n.createTime | String | VPC创建时间。|
| data.n.isDefault | Bool | 是否是默认vpc。 |

  ## 4. 错误码表
 以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。
 
 | 错误码 | 描述 |
|---------|---------|
| InvalidVpc.NotFound | 无效的VPC,VPC资源不存在，请再次核实您输入的资源信息是否正确。 |

## 5. 示例
 
输入
<pre>

  https://vpc.api.qcloud.com/v2/index.php?Action=DescribeVpcEx
	&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
	&vpcId=vpc-2ari9m7h
	&offset=0
	&limit=1
	&orderDirection=desc
</pre>

输出
```

{
    "code": 0,
    "message": "",
		"totalCount":10,
		"data":[
        {
            "vpcId":"gz_vpc_245",
            "unVpcId":"vpc-8e0ypm3z",
            "vpcName":"alblack.bbb",
            "cidrBlock":"10.0.0.0/24",
            "subnetNum":0,
            "routeTableNum":5,
            "vpnGwNum":3,
            "vpcPeerNum":5,
            "vpcDeviceNum":0,
            "classicLinkNum":1,
            "vpgNum":0,
            "natNum":0,
            "createTime":"2015-08-24 15:05:16"
        }
   ]
}

```

