## 功能描述
本接口（CreateBmVpc）用于创建黑石私有网络。

接口访问域名: bmvpc.api.qcloud.com

## 请求

### 请求示例

```
GET https://bmvpc.api.qcloud.com/v2/index.php?
  &Action=CreateBmVpc
  &<公共请求参数>
  &vpcName=<VPC名称>
  &cidrBlock=<私有网络CIDR>
  &zoneId=<可用区的ID>

```

### 请求参数
 以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/229/6976" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为CreateBmVpc。

| 参数名称 | 描述 | 类型 | 必选 |
|---------|---------|---------|---------|
| vpcName | VPC名称。规则：1-60个中文、英文大小写的字母、数字和下划线分隔符 | String | 是 |
| cidrBlock | 私有网络网段CIDR（VPC网段）,格式如：10.1.1.0/24 | String | 是 |
| zoneId | 黑石可用区ID | Int | 是 |
| subnetSet.n | 子网信息数组，创建VPC时可以同时创建子网，可选项。 | Array | 否 |
| subnetSet.n.subnetName | 子网名称，可任意命名，但不得超过60个字符。 | String | 否 |
| subnetSet.n.cidrBlock | 私有网络子网网段CIDR,格式如：10.1.1.0/24 | String | 否 |


## 响应

### 响应示例

```
{
    "code": 0,
    "message": "",
	"codeDesc":"Success",
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
| -3001  | InvalidInputParams | 输入参数不符合指定格式，例如名字只支持最多60个字符。 |
| 16001  | BmVpcLimitExceeded| vpc创建个数超过限制。 |

## 实际案例

### 输入
```

GET https://bmvpc.api.qcloud.com/v2/index.php?Action=CreateBmVpc
    &SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
    &Nonce=6791
    &Timestamp=1507777243
    &Region=bj
    &Signature=RLfmJ0mnkm2Fla4zbTGABkRA%2Ft4%3D
    &vpcName=myvpc
    &cidrBlock=10.0.200.0/24
    &zoneId=1000800001
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

