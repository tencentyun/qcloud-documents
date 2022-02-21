## 功能描述

List Jobs 请求实现列出 Vault 的任务，包括正在进行的任务以及最近完成的任务。

## 请求

### 请求语法

```HTTP
GET /<UID>/vaults/<VaultName>/jobs HTTP 1.1
Host:cas.<Region>.myqcloud.com
Date:date
Authorization: Auth
```

### 请求参数

| 名称         | 描述                                       | 类型     | 必选   |
| ---------- | ---------------------------------------- | ------ | ---- |
| completed  | 要返回的任务的状态。枚举值： `true` ， `false`。         | Boolen | 否    |
| limit      | 要返回任务的最大数目，默认限制为 1000                    | String | 否    |
| marker     | 字典序，从Marker起读取对应条目                       | String | 否    |
| statuscode | 要返回的任务状态的类型。枚举值： `InProgress`，`Succeeded` ， `Failed` | String | 否    |

### 请求头部

无特殊请求头部，其他头部请参见公共请求头部

### 请求内容

无请求内容

## 返回值

### 返回头部

无特殊返回头部，其他头部请参见公共返回头部

### 返回内容

**检索Archive**

| 名称                  | 描述                                                         | 类型     |
| --------------------- | ------------------------------------------------------------ | -------- |
| Action                | Job类型， 对于档案取回任务，此值为 `ArchiveRetrieval`        | String   |
| JobId                 | 任务的ID                                                     | String   |
| JobDescription        | 任务的描述                                                   | String   |
| CreationDate          | 任务启动时的通用协调时间 (UTC) 日期。ISO 8601 日期格式的字符串表示，例如，`2013-03-20T17:03:43.221Z` | ISO 8601 |
| CompletionDate        | 任务完成时的通用协调时间 (UTC) 日期。ISO 8601 日期格式的字符串表示，例如，`2013-03-20T17:03:43.221Z` | ISO 8601 |
| Completed             | 如果任务已完成，则为 `true`；否则为 `false`                  | Boolen   |
| StatusCode            | 任务状态代码。枚举值： `Succeeded`、`Failed` 或 `InProgress` | String   |
| StatusMessage         | 任务状态消息                                                 | String   |
| VaultQCS              | 任务对应Vault的资源名称                                      | String   |
| Marker                | 字典序，Joblist被截断，下一个Job从该marker开始读取           | String   |
| ArchiveId             | 在档案取回操作中请求的档案的 ID                              | String   |
| ArchiveSizeInBytes    | 档案取回任务请求的档案的大小                                 | Number   |
| ArchiveSHA256TreeHash | 档案取回操作的整个档案的 SHA256 树形哈希                     | String   |
| RetrievalByteRange    | 档案取回任务所取回的字节范围，格式为“StartByteValue-EndByteValue”。 StartByteValue 等于 0，EndByteValue 等于档案大小减去 1 | String   |
| Tier                  | Archive检索的检索类型。枚举值： `Expedited` ，`Standard` ，`Bulk` | String   |

```JSON
{
	"JobList": [{
			"Action": "String",
			"JobId": "String",
			"JobDescription": "String",
			"CreationDate": "String",
			"CompletionDate": "String",
			"Completed": "Boolean",
			"StatusCode": "String",
			"StatusMessage": "String",
			"VaultQCS": "String",
			"ArchiveId": "String",
			"ArchiveSizeInBytes": "Number",
			"ArchiveSHA256TreeHash": "String",
			"RetrievalByteRange": "String",
			"Tier": "String"
		},
		...
	],
	"Marker": "String"
}
```

**检索Archive列表**

| 名称                                   | 描述                                                         | 类型     |
| -------------------------------------- | ------------------------------------------------------------ | -------- |
| Action                                 | Job类型， 对于档案取回任务，此值为 `ArchiveRetrieval`        | String   |
| JobId                                  | 任务的ID                                                     | String   |
| JobDescription                         | 任务的描述                                                   | String   |
| CreationDate                           | 任务启动时的通用协调时间 (UTC) 日期。ISO 8601 日期格式的字符串表示，例如，`2013-03-20T17:03:43.221Z` | ISO 8601 |
| CompletionDate                         | 任务完成时的通用协调时间 (UTC) 日期。ISO 8601 日期格式的字符串表示，例如，`2013-03-20T17:03:43.221Z` | ISO 8601 |
| Completed                              | 如果任务已完成，则为 `true`；否则为 `false`                  | Boolen   |
| StatusCode                             | 任务状态代码。枚举值： `Succeeded`、`Failed` 或 `InProgress` | String   |
| StatusMessage                          | 任务状态消息                                                 | String   |
| VaultQCS                               | 任务对应Vault的资源名称                                      | String   |
| Marker                                 | 字典序，Joblist被截断，下一个Job从该marker开始读取           | String   |
| InventorySizeInBytes                   | 与检索Archive列表任务请求相关联的列表的大小，单位字节        | Number   |
| InventoryRetrievalParameters.Format    | Archive列表输出格式，枚举值： `CSV` ，`JSON`。               | String   |
| InventoryRetrievalParameters.StartDate | 文件库清单检索的开始日期（采用 UTC 格式）。ISO 8601 日期格式的字符串表示，例如，`2013-03-20T17:03:43.221Z` | ISO 8601 |
| InventoryRetrievalParameters.EndDate   | 文件库清单检索的结束日期（采用 UTC 格式）。ISO 8601 日期格式的字符串表示，例如，`2013-03-20T17:03:43.221Z` | ISO 8601 |
| InventoryRetrievalParameters.Limit     | 指定每个文件库清单检索请求返回的最大清单项目数。 有效值：正整数 | String   |
| InventoryRetrievalParameters.Marker    | 字典序，从Marker起读取对应Archive列表                        | String   |

```JSON
{
	"JobList": [{
			"Action": "String",
			"JobId": "String",
			"JobDescription": "String",
			"CreationDate": "String",
			"CompletionDate": "String",
			"Completed": "Boolean",
			"StatusCode": "String",
			"StatusMessage": "String",
			"VaultQCS": "String",
			"InventorySizeInBytes": "String",
			"InventoryRetrievalParameters": {
				"Format": "String",
				"StartDate": "String",
				"EndDate": "String",
				"Limit": "String",
				"Marker": "String"
			}
		},
		...
	],
	"Marker": "String"
}
```


