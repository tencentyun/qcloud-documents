## 功能描述

要实现锁定文件库，需进行以下步骤：

1. 初始化文件库锁定策略。成功后返回锁定 ID，同时文件库进入InProgress状态。此时文件库表现形如文件库已锁定，可用以测试效果
2. 进入 InProgress 状态之后24 小时内，利用锁定ID调用Complete Vault Lock以完成锁定。文件库在锁定之后无法进行解锁使用，也无法发起中止锁定

说明：

- 进入InProgress状态之后，若测试不及预期，用户可调用Abort Vault Lock以中止锁定，并重新发起初始化。
- 如果进入InProgress状态之后24 小时内，未完成锁定，则文件库会退出 InProgress 状态，并删除文件库锁定策略。

Initiate Vault Lock实现初始化文件库锁定策略

## 请求

### 请求语法

```http
POST /<UID>/vaults/<VaultName>/lock-policy HTTP 1.1
Host:cas.<Region>.myqcloud.com
Date:date
Authorization: Auth
Content-Length: Length

{
  "Policy"："String"      
}
```

### 请求参数

无特殊请求参数

### 请求头部

无特殊请求头部，其他头部请参见公共请求头部

### 请求内容

```json
{
  "Policy":"String"
}
```

为了便于阅读，以下显示了**不带转义符" \ "**的Policy变量值（即上文String部分），实际调用时需要**将引号转义**，同时**消除换行**。

**对于创建时间不满指定天数的文件，拒绝所有删除请求**

```json
{
    "version": "2.0",
    "statement": [
        {
            "effect": "Deny",
            "principal": {
              "qcs": [
                "qcs::cam::uin/<RootAccout>:uin/<SubAccount>",
                "qcs::cam::uin/<RootAccout>:uin/<SubAccount>"
              ]
            },
            "action": [
                "name/cas:DeleteArchive"
            ],
            "resource": [
                "qcs::cas:<Region>:uid/<Accout>:vaults/<VaultName>"
            ],
            "condition": {
                "NumericLessThan": {
                    "cas:ArchiveAgeInDays":"<Days>"
                }
            }
        }
    ]
}
```

**对于指定标签的文件文件库，拒绝所有删除请求**

```json
{
    "version": "2.0",
    "statement": [
        {
            "effect": "Deny",
            "principal": {
              "qcs": [
                "qcs::cam::uin/<RootAccout>:uin/<SubAccount>",
                "qcs::cam::uin/<RootAccout>:uin/<SubAccount>"
              ]
            },
            "action": [
                "name/cas:DeleteArchive"
            ],
            "resource": [
                "qcs::cas:<Region>:uid/<Accout>:vaults/<VaultName>"
            ],
            "condition": {
                "StringLike": {
                    "cas:ResourceTag/<Key>":"<Value>"
                }
            }
        }
    ]
}
```

## 返回值

### 返回头部

| 名称            | 描述                | 类型     |
| ------------- | ----------------- | ------ |
| x-cas-lock-id | 用于完成文件库锁定过程的锁定 ID | String |

### 返回内容

无返回内容

