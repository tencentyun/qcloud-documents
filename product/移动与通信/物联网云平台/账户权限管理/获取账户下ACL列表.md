

## 1.接口描述
本接口（GetUserAclList）用于获取账户下ACL列表。


## 2.输入参数
参数名称 | 是否必选 | 类型 | 描述
---|---|---|---
userName | 是 | String | 设备账户的名称



## 3.输出参数
参数名称 | 类型 | 描述
---|---|---
code | Int | 公共错误码。0表示成功，其他值表示失败
message | String | 模块错误信息描述 
totalCount | Int | 实际返回的数量
acls | Array | 账户acl列表（topic，access）

## 4.示例
### 4.1  GET请求
GET 请求需要将所有参数都加在 URL 后：
```
https://iot.api.qcloud.com/v2/index.php?
Action=GetUserAclList
&SecretId=XXXXXXXX
&Nonce=63035
&Timestamp=1487910930
&Region=gz
&Uin=XXXXXXXX
&AppId=XXXXXXXX
&userName=XXXXXXXX_XXXXXXXX
&Signature=XXXXXXXX
```

### 4.2 POST请求
POST请求时，参数填充在HTTP Request-body 中，请求地址：https://iot.api.qcloud.com/v2/index.php

参数支持 form-data、x-www-form-urlencoded 等格式，参数数组如下：
```
array (
'Action'=>'GetUserAclList'
'SecretId'=>'XXXXXXXX'
'Nonce'=>63035
'Timestamp'=>1487910930
'Region'=>'gz'
'Uin'=>XXXXXXXX
'AppId'=>XXXXXXXX
'userName'=>'XXXXXXXX_XXXXXXXX'
'Signature'=>'XXXXXXXX'
)
```

### 4.3 返回结果示例
**获取成功**
```
{
	"code": 0,
	"message": "",
	"codeDesc": "Success",
	"totalCount": 1,
	"acls": [{
		"access": 3,
		"topic": "hello/tencent"
	}]
}

```
**修改失败**
```
{
    "code": 4000,
    "message": "(10022)userName不存在",
    "codeDesc": "InvalidResource"
}

```

