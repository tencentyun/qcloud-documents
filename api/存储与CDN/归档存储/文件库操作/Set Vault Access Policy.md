## 功能描述

Set Vault Access Policy 请求实现为一个 Vault 设置权限。

只支持所有者设置权限，对应 UID 值为 "-"。成功后返回 204 No Content。

## 请求

### 请求语法

```HTTP
PUT /<UID>/vaults/<VaultName>/access-policy HTTP 1.1
Host:cas.<Region>.myqcloud.com
Date:date
Authorization: Auth
```

### 请求参数

无特殊请求参数

### 请求头部

无特殊请求头部，其他头部请参见公共请求头部

### 请求内容

```json
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "principal": {
              "qcs": [
                "qcs::cam::uin/<RootAccout>:uin/<SubAccount>",
                "qcs::cam::uin/<RootAccout>:uin/<SubAccount>"
              ]
            },
            "action": [
                "name/cas:<ActionName>"
            ],
            "resource": [
                "qcs::cas:<Region>:uid/<Accout>:vault/<VaultName>",
                "qcs::cas:<Region>:uid/<Accout>:vault/<VaultName>"
            ],
            "condition": {
                "<ConditionOperator>": {
                    "<ConditionName>": [
                        "<ConditionValue>",
                        "<ConditionValue>"
                    ]
                }
            }
        }
    ]
}
```


已支持条件操作

| ConditionOperator       | 含义     | 条件名                    | 举例                                       |
| ----------------------- | ------ | ---------------------- | ---------------------------------------- |
| ip_equal                | ip等于   | ip,ip要符合CIDR规范         | {" ip_equal  ":{"qcs:ip":"10.121.2.10/24"}} |
| ip_not_equal            | ip不等于  | ip，ip要符合CIDR规范         | {" ip_not_equal  ":{"qcs:ip":["10.121.2.10/24",  "10.121.2.20/24"]}} |
| date_not_equal          | 时间不等于  | qcs:current_time(当前时间) | {"date_not_equal":{"qcs:current_time":"2016-01-01T12:00:11Z"}} |
| date_greater_than       | 时间大于   | qcs:current_time(当前时间) | {" date_greater_than  ":{"qcs:current_time":"2016-01-01T12:00:11Z"}} |
| date_greater_than_equal | 时间大于等于 | qcs:current_time(当前时间) | {"  date_greater_than_equal ":{"qcs:current_time":2016-01-01T12:00:11Z"}} |
| date_less_than          | 时间小于   | qcs:current_time(当前时间) | {" date_less_than  ":{"qcs:current_time":"2016-01-01T12:00:11Z"}} |
| date_less_than_equal    | 时间小于等于 | qcs:current_time(当前时间) | {"  date_less_than_equal ":{"qcs:current_time":"2016-01-01T12:00:11Z"}} |


## 返回值

### 返回头部

无特殊返回头部，其他头部请参见公共返回头部。

### 返回内容

无返回内容。
