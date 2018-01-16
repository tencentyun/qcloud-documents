## 1.接口描述
本接口（DeleteCfsRule）用于删除规则。
接口请求域名：**cfs.api.qcloud.com**
## 2.输入参数
|       参数      |  必填 |  类型  |                               描述                           |
|-----------------|------|--------|--------------------------------------------------------------|
| PGroupId      | 是   | string | 权限组ID                      | 
| RuleId        | 是   | string | 规则ID |


## 3.输出参数
| 参数名称 |  类型 | 描述 |
|----------|------ | ---- |
|RuleId            |  string |规则ID   |
|PGroupId      |  string |权限组ID |


## 4.示例 

### 输入


```
<pre>
  https://cfs.test.api.qcloud.com/v2/index.php?Action=DeleteCfsRule
  &Uin=277000000
  &AppId=1250000000
  &PGroupId=pgroup-atutdqup
  &RuleId=rule-ac898wqn
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
        "PGroupId": "pgroup-atutdqup"
    }
}

```



