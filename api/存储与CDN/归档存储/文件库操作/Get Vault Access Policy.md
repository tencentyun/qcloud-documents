## 功能描述

Get Vault Access Policy 请求读取一个 Vault 的权限。

只支持所有者操作，对应 UID 值为"-"。成功后返回200 OK。

## 请求

#### 请求语法

```HTTP
GET /<UID>/vaults/<VaultName>/access-policy HTTP 1.1
Host:cas.<Region>.myqcloud.com
Date:date
Authorization: Auth
```

#### 请求参数

无特殊请求参数。

#### 请求头部

无特殊请求头部，其他头部请参见公共请求头部。

#### 请求内容

无请求内容。

## 返回值

#### 返回头部

无特殊返回头部，其他头部请参见公共返回头部。

#### 返回内容

```json
{
  "policy":"String"
}
```

String 值解析

```JSON
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

