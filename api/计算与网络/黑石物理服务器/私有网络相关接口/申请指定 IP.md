>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
RegisterBatchIp 用于指定子网 IP 进行 IP 申请。

为了避免出现 IP 冲突导致网络异常的情况，当您需要使用某些子网下的特定的 IP 资源时（物理机 IP 除外），需要调用此接口进行指定 IP 申请。
- 指定的 IP 资源（事先知道了具体要使用哪些 IP）在可用 IP 资源列表中：则会对该 IP 资源进行申请，否则，对已经调用 ApplyIps 接口申请或者调用RegisterBatchIp 接口注册的 IP 资源进行申请，
- 指定的 IP 资源不在 IP 资源列表中：会返回 IP 资源冲突错误，除非您把 IP 资源退还了。
- 已经申请的 IP 资源，可用IP资源列表中将不再返回此 IP。

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
| unVpcId | 系统分配的私有网络 ID，例如：vpc-kd7d06of。可通过 DescribeBmVpcEx 接口查询返回的 unVpcId 值。 |String | 是 | 
| unSubnetId | 系统分配的私有网络子网 ID，例如：subnet-k20jbhp0。可通过 DescribeBmSubnetEx 接口查询返回的 unSubnetId 值。 |String | 是 | 
| ipList | 注册 IP 数组，数组个数范围为 1-20。 |Array | 是 |


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
| code | 公共错误码, 0 表示成功，其他值表示失败。| Int |
| message | 模块错误信息描述，与接口相关。| String |
| count | 注册成功的 IP 个数。| Int |
| extramsg |  接口返回的提示信息。| String |
| data.n | 注册成功的 IP 数组。|Array | 

## 错误码

| 错误代码 |英文提示| 描述 |
|---------|---------|---------|
| -3047 |InvalidBmVpc.NotFound| 无效的 VPC,VPC 资源不存在，请再次核实您输入的资源信息是否正确。 |
| -3030  |InvalidBmSubnet.NotFound| 无效的子网,子网资源不存在，请再次核实您输入的资源信息是否正确。 |
| -3031 |AvailableIpUseUp| IP 已被注册或者 IP 不在子网所属范围内。请仔细查看详细错误信息 |
| -3001| InvalidInputParams|参数不合法|


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
