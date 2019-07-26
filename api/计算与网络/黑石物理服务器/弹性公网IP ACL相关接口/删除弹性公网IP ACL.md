>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
EipAclBmDelete 接口用于删除当前账号下的弹性公网 ACL。

接口访问域名: bmeip.api.qcloud.com

## 请求
### 请求示例
```
GET https://bmeip.api.qcloud.com/v2/index.php?
	Action=EipAclBmDelete
	&<公共请求参数>
	&aclId=<EIPACL实例ID>
```

### 请求参数
| 参数名称 | 必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| aclId | 是 | String | 待删除的 ACL 实例 ID |

 > 已关联了EIP 的 ACL 不可删除，只可以删除未关联 EIP 的 ACL。

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
|40001|EipAclNotExist|EIPACL不存在|


## 实际案例
 
### 输入
```
GET https://bmeip.api.qcloud.com/v2/index.php?
	Action=EipAclBmDelete
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
	&Nonce=57333
	&Timestamp=1507730884
	&Region=bj
	&aclId=bmeipacl-7mc70i3o
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

