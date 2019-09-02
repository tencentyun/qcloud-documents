## 1. 接口描述

本接口(DescribeVpcPeeringConnections)用于查询私有网络对等连接
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font>

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为DescribeVpcPeeringConnections。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 否 | String | 发起方私有网络ID值，可使用vpcId或unVpcId，建议使用unVpcId。可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>接口查询。|
| peeringConnectionId | 否 | string | 私有网络对等连接 ID，例如：pcx-dt8c7fa0。|
| peeringConnectionName | 否 | String | 对等连接名称。|
| state | 否 | Int | 连接状态<br>0：申请中；1：连接成功；2：已过期；3：对端已拒绝；4：对端已删除。|
| offset | 否 | Int | 初始行的偏移量，默认为0。|
| limit | 否 | Int | 每页行数，默认为20，最多支持50。|
| orderField | 否 | String | 按某个字段排序，默认不排序。<br>支持字段：peeringConnectionname,createTime。|
| orderDirection | 否 | String | 升序（asc）或降序（desc），默认：desc。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码。0：成功，其他值：失败|
| message | String | 错误信息|
| totalCount | Int | 返回的对等连接数 |
| data.n | Array | 对等连接信息数组 |
| data.n.vpcId | String | 发起方私有网络ID，例如：gz_vpc_245 | 
| data.n.unVpcId | String | 发起方私有网络统一ID，例如：vpc-8e0ypm3z| 
| data.n.peerVpcId | String | 接收方私有网络ID，例如：gz_vpc_24| 
| data.n.unPeerVpcId | String | 接收方统一私有网络ID，例如：vpc-8e0ypm35| 
| data.n.appId | String | 发起方appId | 
| data.n.peeringConnectionId | String | 对等连接ID，，例如：pcx-dt8c7fa0 | 
| data.n.peeringConnectionName | String | 对等连接名称 | 
| data.n.state | Int | 连接状态<br>0：申请中；1：连接成功；2：已过期；3：对端已拒绝；4：对端已删除| 
| data.n.createTime | String | 对等连接创建时间 | 
| data.n.uin | String | 您在腾讯云唯一账号标识，您可以用户中心的个人信息中查看，<a href="https://cloud.tencent.com/doc/product/215/5000#.E6.9F.A5.E7.9C.8B.E5.AF.B9.E7.AB.AF.E8.B4.A6.E5.8F.B7id">点击查看操作指南</a>。| 
| data.n.peerUin | String | 接收方腾讯云唯一账号标识，您可以联系接收方去用户中心的个人信息中查看，<a href="https://cloud.tencent.com/doc/product/215/5000#.E6.9F.A5.E7.9C.8B.E5.AF.B9.E7.AB.AF.E8.B4.A6.E5.8F.B7id">点击查看操作指南</a>。| 

 ## 4. 错误码表
以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。

| 错误码 | 描述 |
|---------|---------|
| InvalidVpc.NotFound | 无效的vpc，vpc资源不存在。请再次核实您输入的资源信息是否正确。 |
| InvalidPeeringConnection.NotFound | 无效的对等连接，对等连接资源不存在。请再次核实您输入的资源信息是否正确。 |

## 5. 示例
输入
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DescribeVpcPeeringConnections
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&peeringConnectionId=pcx-dt8c7fa0
</pre>
输出
```
{
    "code":"0",
    "message":"",
    "totalCount":"8",
    "data":[
        {
            "vpcId":"gz_vpc_245",
            "unVpcId":"vpc-8e0ypm3z",
            "peerVpcId":"gz_vpc_20",
            "unPeerVpcId":"vpc-kx49lmyv",
            "appId":"1351000042",
            "peeringConnectionId":"pcx-dt8c7fa0",
            "peeringConnectionName":"示例1",
            "state":1,
            "createTime":"2016-01-06 20:56:07",
            "uin":"909619400",
            "peerUin":"909619400"
        }
    ]
}
```

