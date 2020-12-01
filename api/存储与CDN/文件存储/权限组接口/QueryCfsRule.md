## 接口描述
本接口（QueryCfsRule）用于查询权限组规则列表。
接口请求域名：`cfs.api.qcloud.com`

## 输入参数
|       参数      |  必填 |  类型  |                               描述                           |
|-----------------|------|--------|--------------------------------------------------------------|
|PGroupId    |   是  | string | 权限组 ID |

## 输出参数

| 参数名称 | 子参数 | 类型 | 描述 |
|----------|------  |----- | ---- |
|RuleList |     -    |  array  |权限组规则列表 |
|       -   | RuleId |   string |规则 ID |
|    -      | ClientIp |  string |允许访问的客户端 IP |
|    -      | RWPermission|  string |读写权限，ro 为只读，rw 为读写 |
|      -    | UserPermission   | string |用户权限。其中 all_squash 为所有访问用户都会被映射为匿名用户或用户组；no_all_squash 为访问用户会先与本机用户匹配，匹配失败后再映射为匿名用户或用户组；root_squash 为将来访的 root 用户映射为匿名用户或用户组；no_root_squash 为来访的 root 用户保持 root 帐号权限。 |
|    -      | Priority|  int    |规则优先级，1 - 100，其中1为最高，100为最低|


## 示例 

#### 输入



<pre>
https://cfs.test.api.qcloud.com/v2/index.php?Action=QueryCfsRule
&Uin=2779000000
&AppId=12500000000
&PGroupId=pgroup-atutdqup
&<<a href="https://www.cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>


#### 输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "RuleList": [
            {
                "RuleId": "rule-9c93j63j",
                "ClientIp": "10.15.21.100",
                "RWPermission": "rw",
                "UserPermission": "root_squash",
                "Priority": 7
            }
        ]
    }
}

```


