## 功能描述

List Vaults 接口实现列出该账户下所有的文件库。档案数与档案总大小，每日盘点更新，非实时数据。

支持跨账户操作。当操作本账户时，UID为"-"。

## 请求

### 请求语法

```HTTP
GET /<UID>/vaults HTTP/1.1
Host:cas.<Region>.myqcloud.com
Date:date
Authorization: Auth
```

### 请求参数

| 名称     | 描述                                       | 类型     | 必选   |
| ------ | ---------------------------------------- | ------ | ---- |
| limit  | 指定要返回的文件库最大数目。该值为正整数，取值`1`-`1000`，默认为 `1000` | String | 否    |
| marker | 按字典序，从该 Marker 开始列出 Vault 的 QCS，如果为空则从头列出 。 | String | 否    |

### 请求头部

无特殊请求头部，其他头部请参见公共请求头部。

### 请求内容

无请求内容。

## 返回值

### 返回头部

无特殊返回头部，其他头部请参见公共返回头部。

### 返回内容

| 名称                | 描述                                       | 类型     |
| ----------------- | ---------------------------------------- | ------ |
| Marker            | 如果返回的列表未能显示完全，该值为下一次请求的 Marker 值。 如果返回的列表已经显示完全，则此值为 `null` | String |
| VaultList         | 文件库描述                                    | Array  |
| CreationDate      | 文件库创建时间， ISO 8601 日期格式的字符串表示，例如，`2017-03-20T17:03:43.221Z` | String |
| LastInventoryDate | 文件库最新读取档案列表时间， ISO 8601 日期格式的字符串表示，例如，`2017-03-20T17:03:43.221Z` | String |
| NumberOfArchives  | 截止到上次读取档案列表时间，文件库中的档案数                   | Number |
| SizeInBytes       | 截止到上次读取档案列表时间，文件库中的总档案大小                 | Number |
| VaultQCS          | 文件库的资源名称 （QCS）                           | String |
| VaultName         | 文件库名称                                    | String |

```JSON
{
	"Marker": "String",
	"VaultList": [{
			"CreationDate": "String",
			"LastInventoryDate": "String",
			"NumberOfArchives": "Number",
			"SizeInBytes": "Number",
			"VaultQCS": "String",
			"VaultName": "String"
		}
		...
	]
}
```
