## 功能描述
EipAclBmBind 接口用于为某个EIP关联ACL。

接口访问域名: bmeip.api.qcloud.com

## 请求
### 请求示例
```
GET https://bmeip.api.qcloud.com/v2/index.php?
	Action=EipAclBmBind
	&<公共请求参数>
	&eipAcl.0.eipId=<EIP实例ID>
	&eipAcl.0.aclId=<ACL实例ID>
	&eipAcl.1.eipId=<EIP实例ID>
	&eipAcl.1.aclId=<ACL实例ID>
```

### 请求参数
| 参数名称 | 必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| eipAcl | 是 | Array(Object) | 对象数组。数组元素为待关联的EIP与ACL，具体结构描述如eipAcl结构所示。|

eipAcl结构

| 参数名称 | 必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| eipId | 是 | String | EIP实例ID|
| aclId | 是 | String | ACL实例ID|


 > 隧道模式弹性IP不支持ACL。
 > 非自动化专区弹性IP不支持ACL。
 > 已绑定NAT网关的弹性IP不支持ACL。
 > 一个弹性IP只能与一个ACL相关联，但一个ACL可关联多个弹性IP。
 > 如果一个弹性IP已关联了ACL，再次调用该接口关联新的ACL，会先解除与原先的ACL的关联，再关联新的ACL

## 响应
### 响应示例
```
{
	"code": 0,
	"message": "",
	"codeDesc": "Success",
	"data": []
}
```
### 响应参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码, 0: 成功, 其他值: 失败，具体含义可以参考[错误码](/document/product/386/6725)。 |
| message | String | 错误信息 |
| codeDesc | String | 错误码描述 |  


## 错误码
|错误代码|英文提示|错误描述|
|---|---|---|
|9000|InnerError|内部系统错误|
|9003|ParamInvalid|请求参数不正确|
|9006|InternalErr|内部数据操作异常|
|40001|EipAclNotExist|ACL不存在|


## 实际案例
 
### 输入
```
GET https://bmeip.api.qcloud.com/v2/index.php?
	Action=DescribeEipAclBm
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
	&Nonce=57333
	&Timestamp=1507730884
	&Region=bj
	&eipAcl.0.eipId=eip-8mh3442s
	&eipAcl.0.aclId=bmeipacl-2oy40kkm
	&Signature=umZFAAWKzjXEQp4ySgrWAoWOHKI%3D
```

### 输出
```
{
	"code": 0,
	"message": "",
	"codeDesc": "Success",
	"data": []
}
```

