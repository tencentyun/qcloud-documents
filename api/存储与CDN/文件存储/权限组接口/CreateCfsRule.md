## 1.接口描述
本接口（CreateCfsRule）用于创建规则。
接口请求域名：**cfs.api.qcloud.com**
## 2.输入参数
|       参数      | 子参数 | 必填 |  类型  |                               描述                           |
|-----------------|--------|------|--------|--------------------------------------------------------------|
| PGroupOrderId            |        | 是   | string | 权限组ID                      | 
| RWPermission        |        | 是   | string | 读写权限 |
| UserPermission      |        | 是   | string | 用户权限 |
| ClientIp            |        | 是   | string | 客户端IP | 
| Priority            |        | 是   | int    | 优先级   |

## 3.输出参数
| 参数名称 | 子参数 |  子参数 | 类型 | 描述 |
|----------|------  |-------- |----- | ---- |
|OrderId            |  |           |string |规则ID   |
|PGroupOrderId      |  |           |string |权限组ID |
|ClientIp           |  |           |string |客户端IP |
|RWPermission       |  |           |string |读写权限 |
| UserPermission    |  |           | string | 用户权限 |
| Priority          |  |           | int    | 优先级   |
## 4.示例 

### 输入


```
<pre>
  https://cfs.test.api.qcloud.com/v2/index.php?Action=CreateCfsRule&SecretId=1
  Uin=2779643970
  &AppId=1251668577
  &PGroupOrderId=pgroup-atutdqup
  &RWPermission=rw
  &UserPermission=root_squash
  &ClientIp=10.15.21.101
  &Priority=9
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
        "OrderId": "rule-ac898wqn",
        "PGroupOrderId": "pgroup-atutdqup",
        "ClientIp": "10.15.21.101",
        "RWPermission": "rw",
        "UserPermission": "root_squash",
        "Priority": 9
    }
}

```
