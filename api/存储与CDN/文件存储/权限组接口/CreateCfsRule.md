## 1.接口描述
本接口（CreateCfsRule）用于创建规则。
接口请求域名：**cfs.api.qcloud.com**
## 2.输入参数
|       参数      |  必填 |  类型  |                               描述                           |
|-----------------|------|--------|--------------------------------------------------------------|
| PGroupId       |是   | string | 权限组ID                      | 
| RWPermission   |  否 | string | 读写权限, 可选参数：ro, rw。ro为只读，rw为读写 |
| UserPermission | 否 | string | 用户权限，可选参数：all_squash，no_all_squash，root_squash，no_root_squash。其中root_squash为所有访问用户都会被映射为匿名用户或用户组；no_all_squash为访问用户会先与本机用户匹配，匹配失败后再映射为匿名用户或用户组；root_squash为将来访的root用户映射为匿名用户或用户组；no_root_squash为来访的root用户保持root帐号权限。|
| ClientIp            | 是   | string | 允许访问的客户端IP | 
| Priority            |  是   | int    | 规则优先级，参数范围1-100。 其中 1 为最高，100为最低|

## 3.输出参数
| 参数名称 | 类型 | 描述 |
|----------|----- | ---- |
|RuleId            | string |规则ID   |
|PGroupId      | string |权限组ID |
|ClientIp           | string |客户端IP |
|RWPermission       | string |读写权限 |
| UserPermission    | string | 用户权限 |
| Priority          | int    | 优先级   |
## 4.示例 

### 输入


```
<pre>
  https://cfs.test.api.qcloud.com/v2/index.php?Action=CreateCfsRule&SecretId=1
  Uin=27700000
  &AppId=1250000000
  &PGroupId=pgroup-atutdqup
  &RWPermission=rw
  &UserPermission=root_squash
  &ClientIp=10.15.21.101
  &Priority=9
  &<<a href="https://www.cloud.tencent.com/doc/api/229/6976"> 公共请求参数 </a>>
</pre>
```

### 输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "RuleId": "rule-ac898wqn",
        "PGroupId": "pgroup-atutdqup",
        "ClientIp": "10.15.21.101",
        "RWPermission": "rw",
        "UserPermission": "root_squash",
        "Priority": 9
    }
}

```


