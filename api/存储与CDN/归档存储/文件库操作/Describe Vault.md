## 功能描述

Describe Vault 请求实现读取一个 Vault 的属性。档案数与档案总大小，每日盘点更新，非实时数据。请求成功后返回 200 OK。

支持跨账户操作。当操作本账户下 valut 时，UID值为"-"。

## 请求

### 请求语法

```HTTP
GET /<UID>/vaults/<VaultName> HTTP 1.1
Host:cas.<Region>.myqcloud.com
Date:date
Authorization: Auth
```

### 请求参数

无特殊请求参数

### 请求头部

无特殊请求头部，其他头部请参见公共请求头部

### 请求内容

无请求内容

## 返回值

### 返回头部

无特殊返回头部，其他头部请参见公共返回头部。

### 返回内容

| 名称                | 描述                                       | 类型     |
| ----------------- | ---------------------------------------- | ------ |
| CreationDate      | 创建文件库的 UTC 日期， ISO 8601 日期格式， 例如，`2017-03-20T17:03:43.221Z` 。 | String |
| LastInventoryDate | 完成上次文件库清单盘点的 UTC 日期，ISO 8601 日期格式， 例如，`2017-03-20T17:03:43.221Z` 。 | String |
| NumberOfArchives  | 上次文件库清单盘点时，文件库中的档案数。尚未运行，返回Null          | Number |
| SizeInBytes       | 截止到上次编制清单日期，文件库中的档案总大小，单位：B。尚未运行，返回Null  | Number |
| VaultQCS          | 文件库的资源名称 (QCS)                           | String |
| VaultName         | 在创建时间指定的文件库名称                            | String |

```JSON
{
	"CreationDate": "String",
	"LastInventoryDate": "String",
	"NumberOfArchives": "Number",
	"SizeInBytes": "Number",
	"VaultQCS": "String",
	"VaultName": "String"
}
```
