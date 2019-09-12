>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
EipBindBmNatGateway 接口用于将EIP绑定到黑石NAT网关，NAT网关使用该EIP作为访问外网的源IP地址，将流量发送到Internet

接口请求域名：bmvpc.api.qcloud.com

## 请求
### 请求示例
```
GET https://bmvpc.api.qcloud.com/v2/index.php?Action=EipBindBmNatGateway
    &<公共请求参数>
    &natId=<NAT网关ID>
    &unVpcId=<vpc网络ID>
    &autoAllocEipNum=<分配IP的个数>
```
### 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/document/product/386/6718" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为EipBindBmNatGateway。

| 参数名称 | 描述 | 类型 | 必选 |
|---------|---------|---------|---------|
| natId | 黑石网关统一ID，例如：nat-df5dfd | String | 是 |
| unVpcId | 私有网络ID值，例如：vpc-kd7d06of，可通过<a href="/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询。 | String | 是 |
| assignedEipSet.n |弹性IP。assignedEipSet 和 autoAllocEipNum 这两个入参需至少传一个，例如：assignedEipSet.0=183.23.0.0.1 | Array | 否 |
| autoAllocEipNum | 需要新申请的弹性IP个数, 取值范围[0, 4]。assignedEipSet 和 autoAllocEipNum 这两个入参需至少传一个| Int | 否 |

## 响应
### 响应示例
```
{
	"code": 0,
	"message": "",
	"data": {
		"taskId": "<NAT异步任务ID>"
	}
}
```
### 响应参数

| 参数名称 | 描述 |  类型 |
|---------|---------|---------|
| code | 错误码。0: 成功, 其他值: 失败| Int |
| message | 错误信息| String |
| data | data中包含操作的任务ID，创建结果可调用<a href="/document/api/386/9356" title="查询NAT网关操作状态">查询NAT网关操作状态</a>查询 | Array |


## 错误码
 
| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
| -3047 | InvalidBmVpc.NotFound | 无效的VPC。VPC资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询VPC。 |
| 13014 | BmVpcNat.NotFound | 无效的NAT网关，NAT网关资源不存在。请再次核实您输入的资源信息是否正确，可通过<a href="/document/product/386/9355" title="DescribeBmNatGateway">DescribeBmNatGateway</a>接口查询NAT网关。 |
| 13010 | BmVpcNat.InvalidEip | 绑定NAT网关的弹性IP不存在。 |
| 13011 | BmVpcNat.InvalidEipVpcId | 弹性IP所属VPC与NAT网关不一致。 |
| 13013 | BmVpcNat.EipUsed | 绑定NAT网关的弹性IP已被使用。 |
| 13015 | BmVpcNat.EipLimitExceeded | 绑定NAT网关的弹性IP达到上限。 |


## 实际案例
### 输入
```
GET https://bmvpc.api.qcloud.com/v2/index.php?
	Action=EipBindBmNatGateway
	&SecretId=AKID1ub7R1JoyBF7nHqjk7IH8nGWaR6Yezwd
	&Nonce=4557
	&Timestamp=1507692902
	&Region=gz
	&unVpcId=300006
	&natId=nat-et8e970y
	&autoAllocEipNum=1
	&Signature=xhpWkOBXHyEdddxK2KIH%2F14bMrc%3D
```

### 输出
```
{
	"code": 0,
	"message": "",
	"data": {
		"taskId": 9641
	}
}
```
