## 1.接口描述
本接口（QueryCfsRule）用于查询权限组规则列表。
接口请求域名：**cfs.api.qcloud.com**
## 2.输入参数
|       参数      | 子参数 | 必填 |  类型  |                               描述                           |
|-----------------|--------|------|--------|--------------------------------------------------------------|
|PGroupOrderId    |        |  是  | string | 权限组ID |

## 3.输出参数
| 参数名称 | 子参数 |  子参数 | 类型 | 描述 |
|----------|------  |-------- |----- | ---- |
|RuleList |         |           |array  |权限组规则列表 |
|          | OrderId |           |string |规则ID |
|          | ClientIp |          |string |IP列表 |
|          | RWPermission|       |string |读写权限 |
|          | UserPermission   |  |string |用户权限 |
|          | Priority|           |int    |优先级|


## 4.示例 

### 输入


```
<pre>
  https://cfs.test.api.qcloud.com/v2/index.php?Action=QueryCfsRule
  &Uin=2779643970
  &AppId=1251668577
  &PGroupOrderId=pgroup-atutdqup
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
        "RuleList": [
            {
                "OrderId": "rule-9c93j63j",
                "ClientIp": "10.15.21.100",
                "RWPermission": "rw",
                "UserPermission": "root_squash",
                "Priority": 7
            }
        ]
    }
}

```


