
## 1.接口描述
本接口（AddUserAcl）用于添加账户ACL。


## 2.输入参数
参数名称 | 是否必选 | 类型 | 描述
---|---|---|---
userName | 是 | String | 设备账户的名称
topic | 是 | String | 主题名称
access | 是 | Int | 方式：1 sub 2 pub 3 subpub


## 3.输出参数
参数名称 | 类型 | 描述
---|---|---
code | Int | 公共错误码。0表示成功，其他值表示失败
message | String | 模块错误信息描述 
ret | String | 模块处理结果（OK）

## 4.示例
### 4.1  GET请求
GET 请求需要将所有参数都加在 URL 后：

```
https://iot.api.qcloud.com/v2/index.php?
Action=AddUserAcl
&SecretId=XXXXXXXX
&Nonce=60363
&Timestamp=1487910497
&Region=gz
&Uin=XXXXXXXX
&AppId=XXXXXXXX
&userName=XXXXXXXX_XXXXXXXX
&topic=XXXXXXXX
&access=3
&Signature=XXXXXXXX
```

### 4.2 POST请求
POST请求时，参数填充在HTTP Request-body 中，请求地址：https://iot.api.qcloud.com/v2/index.php

参数支持 form-data、x-www-form-urlencoded 等格式，参数数组如下：
```
array (
'Action'=>'AddUserAcl'
'SecretId'=>'XXXXXXXX'
'Nonce'=>60363
'Timestamp'=>1487910497
'Region'=>'gz'
'Uin'=>XXXXXXXX
'AppId'=>XXXXXXXX
'userName'=>'XXXXXXXX_XXXXXXXX'
'topic'=>'XXXXXXXX'
'access'=>3
'Signature'=>'XXXXXXXX'
)
```

### 4.3 返回结果示例
**修改成功**
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "ret": "Ok"
}
```
**修改失败**
```
{
    "code": 4000,
    "message": "请求失败，参数[access]不能为空。",
    "codeDesc": "InvalidParameter"
}
```

