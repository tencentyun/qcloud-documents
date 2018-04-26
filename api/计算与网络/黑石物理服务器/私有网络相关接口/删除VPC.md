## 功能描述
 
本接口（DeleteBmVpc）用于删除黑石私有网络。
接口访问域名: bmvpc.api.qcloud.com

删除私有网络前，请清理该私有网络下所有资源，包括子网、负载均衡、弹性IP、对等连接、NAT网关、专线通道、SSLVPN等资源

## 请求

### 请求示例

```
GET https://bmvpc.api.qcloud.com/v2/index.php?
  &Action=DeleteBmVpc
  &<公共请求参数>
  &unVpcId=<VPC实例ID>

```

### 请求参数

 以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/229/6976" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为DeleteBmVpc。

| 参数名称 | 描述 | 类型 | 必选 |
|---------|---------|---------|---------|
| unVpcId | 私有网络ID值，例如：vpc-kd7d06of。可通过DescribeBmVpcEx接口查询。 | String | 是 |
 

## 响应

### 响应示例

```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
	"data": {
        "taskId": <异步任务ID>
    }
}

```
### 响应参数

| 参数名称 | 描述 | 类型 |
|---------|---------|---------|
| code | 公共错误码, 0表示成功，其他值表示失败。详见错误码页面的<a href="/document/product/386/6725" title="公共错误码">公共错误码</a>。| Int |
| message | 模块错误信息描述，与接口相关。| String |
| data | 返回操作的异步任务ID。| Array |

## 错误码
 
| 错误代码 |英文提示| 描述 |
|--------|---------|---------|
| -3047  | InvalidBmVpc.NotFound | 无效的VPC。VPC资源不存在，请再次核实您输入的资源信息是否正确，可通过DescribeBmVpcEx接口查询VPC。 |
| -3001  | InvalidInputParams | 输入参数不符合指定格式。 |
| 16003  | BmInvalidVpc.CannotDelete | VPC下有子网资源，不能删除。|
| 16004  | BmInvalidVpc.CannotDelete | VPC下有对等连接资源，不能删除。|
| 16005  | BmInvalidVpc.CannotDelete | VPC下有弹性IP资源，不能删除。|
| 16006  | BmInvalidVpc.CannotDelete | VPC下有LB资源，不能删除。|
| 16007  | BmInvalidVpc.CannotDelete | VPC下有子网资源，不能删除。|
| 16008  | BmInvalidVpc.CannotDelete | VPC下有专线资源，不能删除。|
| 16009  | BmInvalidVpc.CannotDelete | VPC下有运维SSLVPN资源，不能删除。|
| 16010  | BmInvalidVpc.CannotDelete | VPC下有IPSecVpn资源，不能删除。|
| 16011 | BmInvalidVpc.CannotDelete | VPC下有NAT资源，不能删除。|
| 16012 | BmInvalidVpc.CannotDelete | VPC已在流程中，不能删除。|
| 16013 | BmInvalidVpc.CannotDelete | 老专区VPC，不可删除。|

## 实际案例

### 输入
```

GET https://bmvpc.api.qcloud.com/v2/index.php?Action=DeleteBmVpc
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
    &Nonce=6791
    &Timestamp=1507777243
    &Region=bj
    &Signature=RLfmJ0mnkm2Fla4zbTGABkRA%2Ft4%3D
	&unVpcId=vpc-kd7d06of
```

### 输出
```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
	"data": {
        "taskId": 9641
    }
}

```

