## 1.接口描述
本接口（DeleteCfsRule）用于删除规则。
接口请求域名：**cfs.api.qcloud.com**
## 2.输入参数
|       参数      |  必填 |  类型  |                               描述                           |
|-----------------|------|--------|--------------------------------------------------------------|
| PGroupOrderId      | 是   | string | 权限组ID                      | 
| OrderId        | 是   | string | 规则ID |


## 3.输出参数
| 参数名称 |  类型 | 描述 |
|----------|------ | ---- |
|OrderId            |  string |规则ID   |
|PGroupOrderId      |  string |权限组ID |


## 4.示例 

### 输入


```
<pre>
  https://cfs.test.api.qcloud.com/v2/index.php?Action=DeleteCfsRule
  &Uin=2779643970
  &AppId=1251668577
  &PGroupOrderId=pgroup-atutdqup
  &OrderId=rule-ac898wqn
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
        "OrderId": "rule-ac898wqn",
        "PGroupOrderId": "pgroup-atutdqup"
    }
}

```



