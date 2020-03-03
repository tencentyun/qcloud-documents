## 接口描述
本接口（UpdateCfsRule）用于更新权限规则。
接口请求域名：`cfs.api.qcloud.com`

## 输入参数

|       参数      | 必填 |  类型  |                               描述                           |
|-----------------|------|--------|--------------------------------------------------------------|
| PGroupId    | 是  | string | 权限组 ID |
| RuleId       | 是  | string | 规则 ID|
| ClientIp         | 否   | string |  允许访问的客户端 IP |
| RWPermission   |  否 | string | 读写权限, 可选参数：ro，rw。ro 为只读，rw 为读写 |
| UserPermission | 否 | string | 用户权限，可选参数：all_squash，no_all_squash，root_squash，no_root_squash。其中 all_squash为所有访问用户都会被映射为匿名用户或用户组；no_all_squash 为访问用户会先与本机用户匹配，匹配失败后再映射为匿名用户或用户组；root_squash 为将来访的 root 用户映射为匿名用户或用户组；no_root_squash 为来访的 root 用户保持 root 帐号权限|
| Priority       | 否 | int    | 规则优先级，参数范围1-100。 其中1为最高，100为最低 |

## 输出参数

| 参数名称 | 类型 | 描述 |
|----------|----- | ---- |
| PGroupId    | string | 权限组 ID |
| RuleId       |  string | 规则 ID|
| ClientIp         |   string |  允许访问的客户端 IP |
| RWPermission   |  string | 读写权限|
| UserPermission |  string | 用户权限 |
| Priority       | int    | 优先级 |


## 示例 

#### 输入



<pre>
https://cfs.test.api.qcloud.com/v2/index.php?Action=UpdateCfsRule
&Uin=2770000000
&AppId=1250000000
&RuleId=rule-08fbdvat
&PGroupId=pgroup-fijirhdp
&ClientIp=1.2.4.3
&RWPermission=rw
&UserPermission=no_root_squash
&Priority=7
&<<a href="https://www.cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>

#### 输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "PGroupId": "pgroup-fijirhdp",
        "RuleId": "rule-08fbdvat",
        "ClientIp": "1.2.4.3",
        "RWPermission": "rw",
        "UserPermission": "no_root_squash",
        "Priority": 7
    }
}
```

