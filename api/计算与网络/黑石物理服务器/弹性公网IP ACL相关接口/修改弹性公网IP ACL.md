>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
EipAclBmSet 接口用于修改 ACL 名称、状态、入站规则、出战规则。

接口访问域名: bmeip.api.qcloud.com

## 请求
### 请求示例
```
GET https://bmeip.api.qcloud.com/v2/index.php?
	Action=EipAclBmSet
	&<公共请求参数>
	&aclId=<ACL实例ID>
	&aclName=<ACL名称>
	&status=<ACL状态>
	&type=<规则类型 入站/出战>
	&rule.0.ip=<IP地址>
	&rule.0.port=<端口>
	&rule.0.protocol=<协议>
	&rule.0.action=<策略>
	&rule.0.description=<备注>
	&rule.1.ip=<IP地址>
	&rule.1.port=<端口>
	&rule.1.protocol=<协议>
	&rule.1.action=<策略>
	&rule.1.description=<备注>
```

### 请求参数
| 参数名称 | 必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| aclId | 是 | String | ACL 实例 ID|
| aclName | 否 | String | ACL 名称|
| status | 否 | Int | ACL 状态。0：无状态 1：有状态|
| type | 否 | String | 规则类型（in/out）。in：入站规则 out：出站规则|
| rule | 否 | Array(Object) | 对象数组。数组的每一个元素是一条规则。规则的结构描述如 rule 结构所示  |

rule结构

| 参数名称          | 类型     | 描述                                       |
| ------------- | ------ | ---------------------------------------- |
| ip    | String | IP 地址,支持 IP 与 cidr 两种方式                                  |
| port         | String    | 目标端口，支持单个端口与端口区间                                |
| protocol         | String    | 协议(TCP/UDP/ICMP/ANY)                                |
| action         | String    | 策略（accept/drop）                                |
| description         | String    | 备注                                |

 > 清空入站规则，参数 type 填写 in,rule 参数不用填写
 > 清空出站规则，参数 type 填写 out,rule 参数不用填写





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
| code |  Int | 错误码, 0: 成功, 其他值: 失败，具体含义可以参考 [错误码](/document/product/386/6725)。 |
| message | String | 错误信息 |
| codeDesc | String | 错误码描述 |  


## 错误码
|错误代码|英文提示|错误描述|
|---|---|---|
|9000|InnerError|内部系统错误|
|9003|ParamInvalid|请求参数不正确|
|9006|InternalErr|内部数据操作异常|
|40001|EipAclNotExist|ACL 不存在|


## 实际案例
 
### 输入
```
GET https://bmeip.api.qcloud.com/v2/index.php?
	Action=EipAclBmSet
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
	&Nonce=57333
	&Timestamp=1507730884
	&Region=bj
	&aclId=bmeipacl-2oy40kkm
	&type=in
	&rule.0.ip=8.8.8.8
	&rule.0.port=80-8080
	&rule.0.protocol=tcp
	&rule.0.action=accept
	&rule.0.description=testtest
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

