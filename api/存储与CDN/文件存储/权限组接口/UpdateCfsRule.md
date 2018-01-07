## 1.接口描述
本接口（UpdateCfsRule）用于更新权限规则。
接口请求域名：**cfs.api.qcloud.com**
## 2.输入参数
|       参数      | 子参数 | 必填 |  类型  |                               描述                           |
|-----------------|--------|------|--------|--------------------------------------------------------------|
| PGroupOrderId    |        |  是  | string | 权限组ID |
| OrderId       |        |  是  | string | 规则ID|
| ClientIp         |       | 否   | string | 规则适用IP地址 |
| RWPermission   |    |  否 | string | 读写权限|
| UserPermission |    | 否 | string | 用户权限 |
| Priority       |    | 否 | int    | 优先级 |

## 3.输出参数
| 参数名称 | 子参数 |  子参数 | 类型 | 描述 |
|----------|------  |-------- |----- | ---- |
| PGroupOrderId    |        |    | string | 权限组ID |
| OrderId       |        |    | string | 规则ID|
| ClientIp         |       |    | string | 规则适用IP地址 |
| RWPermission   |    |   | string | 读写权限|
| UserPermission |    |  | string | 用户权限 |
| Priority       |    |  | int    | 优先级 |


## 4.示例 

### 输入


```
<pre>
  https://cfs.test.api.qcloud.com/v2/index.php?Action=UpdateCfsRule
  &Uin=2779643970
  &AppId=1251668577
  &OrderId=rule-08fbdvat
  &PGroupOrderId=pgroup-fijirhdp
  &ClientIp=1.2.4.3
  &RWPermission=rw
  &UserPermission=no_root_squash
  &Priority=7
  &<<a href="https://www.qcloud.com/doc/api/229/6976"> 公共请求参数 </a>>
</pre>
```

### 输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "PGroupOrderId": "pgroup-fijirhdp",
        "OrderId": "rule-08fbdvat",
        "ClientIp": "1.2.4.3",
        "RWPermission": "rw",
        "UserPermission": "no_root_squash",
        "Priority": 7
    }
}

```