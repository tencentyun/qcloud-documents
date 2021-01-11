## 功能描述

Get Job Output 请求用来输出缓存池中检索出来的 Archive 或 Archive 列表，缓存池中的内容24小时有效。请求所有数据成功后，返回 200 OK。请求部分数据成功时，返回 206 Partial Content。

支持跨账户操作。当操作本账户时，UID 为"-"。

## 请求

### 请求语法

```HTTP
GET /<UID>/vaults/<VaultName>/jobs/<JobID>/output HTTP 1.1
Host:cas.<Region>.myqcloud.com
Date:date
Authorization: Auth
Range:ByteRangeToRetrieve
```

### 请求参数

无特殊请求参数。

### 请求头部

#### 推荐使用头部

| 名称    | 描述                 | 类型     | 必选   |
| ----- | ------------------ | ------ | ---- |
| Range | 输出取回的字节范围，默认下载所有内容 | String | 否    |

### 请求内容

无请求内容。

## 返回值

### 返回头部

| 名称                     | 描述                                       | 类型     |
| ---------------------- | ---------------------------------------- | ------ |
| Content-Range          | 返回的字节范围       。                          | String |
| Content-Type           | 根据内容类型判断输出是 Archive 还是 Archive 列表，若为 Archive，该值为`application/octet-stream`；若为 JSON 格式 Archive 列表，该值为`application/json`；若为CSV格式Archive列表，该值为  `text/csv` 。 | String |
| x-cas-sha256-tree-hash | Output 中的数据树形哈希，当 Job 为 Archive 的一棵子树，且获取 Job 的 Range 范围也是一棵子树才返回该头部。 | String |

### 返回内容

**检索Archive列表（JSON格式）**

注：CSV 格式有五列：“ArchiveId”、“ArchiveDescription”、“CreationDate”和“Size”，它们的定义与相应 JSON 字段的定义相同。

| 名称                 | 描述                                       | 类型     |
| ------------------ | ---------------------------------------- | ------ |
| VaultQCS           | 从中请求档案取回的资源名称  。                         | String |
| InventoryDate      | 对文件库进行更改后完成文件库上次编制清单的 UTC 日期和时间，ISO 8601 日期格式的字符串表示，例如，`2013-03-20T17:03:43.221Z`。 | String |
| ArchiveList        | 档案元数据数组。数组中的每个数据元均表示文件库中包含的一个档案的元数据 。    | String |
| ArchiveId          | 档案的 ID  。                                | String |
| ArchiveDescription | 档案的描述 。                                  | String |
| CreationDate       | 创建档案的 UTC 日期和时间， ISO 8601 日期格式的字符串表示，例如，`2013-03-20T17:03:43.221Z`。 | String |
| Size               | 档案的大小（以字节为单位）。                           | Number |
| SHA256TreeHash     | 档案的树形哈希 。                                | String |

```JSON
{
	"VaultQCS": "String",
	"InventoryDate": "String",
	"ArchiveList": [{
			"ArchiveId": "String",
			"ArchiveDescription": "String",
			"CreationDate": "String",
			"Size": "Number",
			"SHA256TreeHash": "String"
		},
		...
	]
}
```

**取回 Archive**

下载对应 Archive。

