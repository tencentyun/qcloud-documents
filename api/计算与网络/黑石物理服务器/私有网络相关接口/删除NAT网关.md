>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
DeleteBmNatGateway 接口用于删除黑石NAT网关

接口请求域名：bmvpc.api.qcloud.com

## 请求

### 请求示例
```
GET https://bmvpc.api.qcloud.com/v2/index.php/?Action=DeleteBmNatGateway
    &<公共请求参数>
    &natId=<NAT网关ID>
    &unVpcId=<vpc网络ID>
```
### 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/document/product/386/6718" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为DeleteBmNatGateway。

| 参数名称 |描述 | 类型 | 必选  | 
|---------|---------|---------|---------|
| unVpcId |私有网络ID值，例如：vpc-kd7d06of，可通过<a href="/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询。| String |  是 |
| natId |  系统分配的黑石NAT网关统一ID，例如：nat-7t9nf3pu | String |  是 |



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

| 参数名称 |描述 | 类型 | 
|---------|---------|---------|
| code |错误码。0: 成功, 其他值: 失败| Int | 
| message | 错误信息| String |
| data |返回操作的任务ID，创建结果可调用<a href="/document/api/386/9356" title="查询NAT网关操作状态">查询NAT网关操作状态</a>查询 | Array | 


## 错误码

| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
| -3047 | InvalidBmVpc.NotFound | 无效的VPC。VPC资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询VPC。 |
| 13014 | BmVpcNat.NotFound | 无效的NAT网关，NAT网关资源不存在。请再次核实您输入的资源信息是否正确，可通过<a href="/document/product/386/9355" title="DescribeBmNatGateway">DescribeBmNatGateway</a>接口查询NAT网关。 |


## 实际案例
### 输入
```
GET https://bmvpc.api.qcloud.com/v2/index.php?
	Action=DeleteBmNatGateway
	&SecretId=AKID1ub7R1JoyBF7nHqjk7IH8nGWaR6Yezwd
	&Nonce=4557
	&Timestamp=1507692902
	&Region=gz
	&natId=nat-dgssere1
	&unVpcId=vpc-kd7d06of
	&Signature=4dq8JXWTyg9n8FuVckaIhg8Pnbw%3D
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
