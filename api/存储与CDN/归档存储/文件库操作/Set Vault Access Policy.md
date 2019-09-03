## 功能描述

Set Vault Access Policy 请求实现为一个 Vault 设置权限。具体策略语法参见 [权限管理](https://cloud.tencent.com/document/product/572/8741)。

只支持所有者设置权限，对应 UID 值为 "-"。成功后返回204 No Content。

## 请求

#### 请求语法

```HTTP
PUT /<UID>/vaults/<VaultName>/access-policy HTTP 1.1
Host:cas.<Region>.myqcloud.com
Date:date
Authorization: Auth
```

#### 请求参数

无特殊请求参数。

#### 请求头部

无特殊请求头部，其他头部请参见公共请求头部。

#### 请求内容

```JSON
{
  "policy":"String"
}
```

为了便于阅读，以下显示了**不带转义符" \ "**的Policy变量值（即上文 String 部分），实际调用时需要**将引号转义**，同时**消除换行**。

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
                "qcs::cas:<Region>:uid/<Accout>:vaults/<VaultName>",
                "qcs::cas:<Region>:uid/<Accout>:vaults/<VaultName>"
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
| ip_equal                | IP 等于   | IP，IP 要符合 CIDR 规范         | {" ip_equal  ":{"qcs:ip":"10.121.2.10/24"}} |
| ip_not_equal            | IP不等于  | IP，IP 要符合 CIDR 规范         | {" ip_not_equal  ":{"qcs:ip":["10.121.2.10/24",  "10.121.2.20/24"]}} |
| date_not_equal          | 时间不等于  | qcs:current_time(当前时间) | {"date_not_equal":{"qcs:current_time":"2016-01-01T12:00:11Z"}} |
| date_greater_than       | 时间大于   | qcs:current_time(当前时间) | {" date_greater_than  ":{"qcs:current_time":"2016-01-01T12:00:11Z"}} |
| date_greater_than_equal | 时间大于等于 | qcs:current_time(当前时间) | {"  date_greater_than_equal ":{"qcs:current_time":2016-01-01T12:00:11Z"}} |
| date_less_than          | 时间小于   | qcs:current_time(当前时间) | {" date_less_than  ":{"qcs:current_time":"2016-01-01T12:00:11Z"}} |
| date_less_than_equal    | 时间小于等于 | qcs:current_time(当前时间) | {"  date_less_than_equal ":{"qcs:current_time":"2016-01-01T12:00:11Z"}} |


## 返回值

#### 返回头部

无特殊返回头部，其他头部请参见公共返回头部。

#### 返回内容

无返回内容。
