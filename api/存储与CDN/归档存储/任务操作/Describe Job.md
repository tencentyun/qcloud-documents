## 功能描述

Describle Job 请求实现获取Vault的具体任务信息

支持跨账户操作。当操作本账户时，UID为"-"。

## 请求

### 请求语法

```HTTP
GET /<UID>/vaults/<VaultName>/jobs/<JobID> HTTP 1.1
Host:cas.<Region>.myqcloud.com
Date:date
Authorization: Auth
```

### 请求参数

无特殊请求参数。

### 请求头部

无特殊请求头部，其他头部请参见公共请求头部。

### 请求内容

无请求内容。

## 返回值

### 返回头部

无特殊返回头部，其他头部请参见公共返回头部。

### 返回内容

**检索Archive**

| 名称                    | 描述                                       | 类型       |
| --------------------- | ---------------------------------------- | -------- |
| Action                | Job类型，枚举值：  `ArchiveRetrieval`， `InventoryRetrieval`。 对于档案取回任务，此值为 `ArchiveRetrieval` | String   |
| JobId                 | 任务的ID                                    | String   |
| JobDescription        | 任务的描述                                    | String   |
| CreationDate          | 任务启动时的通用协调时间 (UTC) 日期。ISO 8601 日期格式的字符串表示，例如，`2013-03-20T17:03:43.221Z`。 | ISO 8601 |
| CompletionDate        | 任务完成时的通用协调时间 (UTC) 日期。ISO 8601 日期格式的字符串表示，例如，`2013-03-20T17:03:43.221Z`。 | ISO 8601 |
| Completed             | 如果任务已完成，则为 `true`；否则为 `false`            | Boolen   |
| StatusCode            | 任务状态代码。枚举值： `Succeeded`、`Failed` 或 `InProgress` | String   |
| StatusMessage         | 任务状态消息                                   | String   |
| VaultQCS              | 任务对应Vault的资源名称                           | String   |
| ArchiveId             | 在档案取回操作中请求的档案的 ID                        | String   |
| ArchiveSizeInBytes    | 档案取回任务请求的档案的大小                           | Number   |
| ArchiveSHA256TreeHash | 档案取回操作的整个档案的 SHA256 树形哈希                 | String   |
| RetrievalByteRange    | 档案取回任务所取回的字节范围，格式为“*StartByteValue*-*EndByteValue*”。如果没有在档案取回中指定范围，则取回整个档案，并且 *StartByteValue* 等于 0，*EndByteValue* 等于档案大小减去 1 | String   |
| SHA256TreeHash        | 档案请求范围的 SHA256 树形哈希值。 当指定未以树形哈希对齐的范围的档案取回任务，该值为Null； 当指定不等于整个档案的范围并且任务状态为InProgress的档案任务，该值为Null，任务完成后，SHA256TreeHash字段将具有值。 | String   |
| Tier                 | Archive检索的检索类型。枚举值： `Expedited` ，`Standard` ，`Bulk` | String   |

```JSON
{     
  "Action": String,
  "JobId": String,
  "JobDescription": String,
  "CreationDate": String,
  "CompletionDate": String,
  "Completed": Boolean,
  "StatusCode": String,
  "StatusMessage": String,
  "VaultQCS": String,
  "ArchiveId": String,
  "ArchiveSizeInBytes": Number,
  "ArchiveSHA256TreeHash": String,
  "RetrievalByteRange": String,
  "SHA256TreeHash": String,
  "Tier": String,
}
```

**检索Archive列表**

| 名称                           | 描述                                       | 类型       |
| ---------------------------- | ---------------------------------------- | -------- |
| Action                       | Job类型，枚举值：  `ArchiveRetrieval`， `InventoryRetrieval`。 对于档案取回任务，此值为 `ArchiveRetrieval` | String   |
| JobId                        | 任务的ID                                    | String   |
| JobDescription               | 任务的描述                                    | String   |
| CreationDate                 | 任务启动时的通用协调时间 (UTC) 日期。ISO 8601 日期格式的字符串表示，例如，`2013-03-20T17:03:43.221Z`。 | ISO 8601 |
| CompletionDate               | 任务完成时的通用协调时间 (UTC) 日期。ISO 8601 日期格式的字符串表示，例如，`2013-03-20T17:03:43.221Z`。 | ISO 8601 |
| Completed                    | 如果任务已完成，则为 `true`；否则为 `false`            | Boolen   |
| StatusCode                   | 任务状态代码。枚举值： `Succeeded`、`Failed` 或 `InProgress` | String   |
| StatusMessage                | 任务状态消息                                   | String   |
| VaultQCS                     | 任务对应Vault的资源名称                           | String   |
| InventorySizeInBytes         | 与检索Archive列表任务请求相关联的列表的大小，单位字节           | Number   |
| Format                       | Archive列表输出格式，枚举值： `CSV` ，`JSON`。        | String   |
| StatDate                     | 文件库清单检索的开始日期（采用 UTC 格式）。ISO 8601 日期格式的字符串表示，例如，`2013-03-20T17:03:43.221Z`。 | ISO 8601 |
| EndDate                      | 文件库清单检索的结束日期（采用 UTC 格式）。ISO 8601 日期格式的字符串表示，例如，`2013-03-20T17:03:43.221Z`。 | ISO 8601 |
| Limit                        | 指定每个文件库清单检索请求返回的最大清单项目数。 有效值：正整数         | String   |
| InventorySizeInBytes. Marker | 字典序，从Marker起读取对应Archive列表                | String   |

```JSON
{
  "Action": String,
  "JobId": String,
  "JobDescription": String,
  "CreationDate": String,
  "CompletionDate": String,
  "Completed": Boolean,
  "StatusCode": String,
  "StatusMessage": String,
  "VaultQCS": String,
  "InventorySizeInBytes": String,
  "InventoryRetrievalParameters": { 
    "Format": String,
    "StartDate": String,
    "EndDate": String,
    "Limit": String,
    "Marker": String
}
```