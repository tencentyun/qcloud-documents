>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
RegisterBatchIp 用于指定子网IP进行IP注册。

接口请求域名：bmvpc.api.qcloud.com


## 请求

### 请求示例
```
GET https://bmvpc.api.qcloud.com/v2/index.php?Action=RegisterBatchIp
    &<公共请求参数>
    &unVpcId=<VPC网络唯一ID>
	&unSubnetId=<子网唯一ID>
    &ipList=<注册IP数组>
```
### 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为RegisterBatchIp。

| 参数名称 |  描述 | 类型 |必选  |
|---------|---------|---------|---------|
| unVpcId | 系统分配的私有网络ID，例如：vpc-kd7d06of。可通过DescribeBmVpcEx接口查询返回的unVpcId值。 |String | 是 | 
| unSubnetId | 系统分配的私有网络子网ID，例如：subnet-k20jbhp0。可通过DescribeBmSubnetEx接口查询返回的unSubnetId值。 |String | 是 | 
| ipList | 注册IP数组，数组个数范围为1-20。 |Array | 是 |


## 响应
### 响应示例
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": [
        "10.1.1.10",
		"10.1.1.2",
		"10.1.1.130"
    ],
    "extramsg":""
    "count": 1
}

{
    "code": 4000,
    "message": "(-3031)没有可用的IP地址 10.1.1.4 ip冲突，10.1.1.200 ip不在子网范围内，剩余ip注册成功",
    "codeDesc": "AvailableIpUseUp"
}
```
### 响应参数

| 参数名称 | 描述 | 类型 |
|---------|---------|---------|
| code | 公共错误码, 0表示成功，其他值表示失败。详见错误码页面的<a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="公共错误码">公共错误码</a>。| Int |
| message | 模块错误信息描述，与接口相关。| String |
| count | 注册成功的IP个数。| Int |
| extramsg |  接口返回的提示信息。| String |
| data.n | 注册成功的IP数组。|Array | 

## 错误码

| 错误代码 |英文提示| 描述 |
|---------|---------|---------|
| -3047 |InvalidBmVpc.NotFound| 无效的VPC,VPC资源不存在，请再次核实您输入的资源信息是否正确。 |
| -3030  |InvalidBmSubnet.NotFound| 无效的子网,子网资源不存在，请再次核实您输入的资源信息是否正确。 |
| -3031 |AvailableIpUseUp| IP已被注册或者IP不在子网所属范围内。请仔细查看详细错误信息 |
| -3001| InvalidInputParams|参数不合法


## 实际案例
### 输入
```
GET https://bmvpc.api.qcloud.com/v2/index.php?
	Action=RegisterBatchIp
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
    &Nonce=6791
    &Timestamp=1507777243
    &Region=bj
    &Signature=RLfmJ0mnkm2Fla4zbTGABkRA%2Ft4%3D
	&unVpcId=vpc-2ari9m7h
	&unSubnetId=subnet-keqt3oty
	&ipList.0=10.1.1.2&ipList.1=10.1.1.130&10.1.1.10
```

### 输出
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": [
        "10.1.1.10",
		"10.1.1.2",
		"10.1.1.130"
    ],
    "extramsg":""
    "count": 1
}
```

### 输入
```
GET https://bmvpc.api.qcloud.com/v2/index.php?
	Action=RegisterBatchIp
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
    &Nonce=6791
    &Timestamp=1507777243
    &Region=bj
    &Signature=RLfmJ0mnkm2Fla4zbTGABkRA%2Ft4%3D
	&unVpcId=vpc-2ari9m7h
	&unSubnetId=subnet-keqt3oty
	&ipList.0=10.1.1.4&ipList.1=10.1.1.200&10.1.1.6
```

### 输出
```
{
    "code": 4000,
    "message": "(-3031)没有可用的IP地址 10.1.1.4 ip冲突，10.1.1.200 ip不在子网范围内，剩余ip注册成功",
    "codeDesc": "AvailableIpUseUp"
}
```
