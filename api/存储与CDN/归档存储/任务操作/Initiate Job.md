## 功能描述

Initiate Job 请求实现将档案或者档案列表取出到缓存池。操作完成后，用户可以通过 Get Job Output 请求读取对应档案或者档案列表。

### 细节分析

检索任务所对应的三种模式下的时间如下表：

|  任务类型   | Expedited | Standard | Bulk    |
| --------- | --------- | -------- | ------- |
| 检索档案的任务时间 | 1-5分钟，<br>最大支持256MB 文件    | 3-5小时   | 5-12小时 |
| 检索档案列表的任务时间 | -|3-5小时   |-|

## 请求

### 请求示例

```HTTP
POST /<UID>/vaults/<VaultName>/jobs HTTP 1.1
Host:cas.<Region>.myqcloud.com
Date:date
Authorization: Auth
```

### 请求头部
无特殊请求头部，其他头部请参见 [公共请求头部](https://cloud.tencent.com/document/product/572/8743) 文档。

### 请求参数
无特殊请求参数。

### 请求内容
#### 检索档案

示例如下：
```json
{
	"Type": "archive-retrieval",
	"ArchiveId": "String",
	"Description": "String",
	"Tier": "String"
}
```

参数说明如下：

| 名称        | 描述                                                         | 类型   | 必选 |
| ----------- | ------------------------------------------------------------ | ------ | ---- |
| Type        | 任务类型，当检索 Archive 时，此处填写`archive-retrieval`     | String | 是   |
| ArchiveId   | 检索的档案的 ID                                              | String | 是   |
| Description | 任务的描述                                                   | String | 否   |
| Tier        | Archive 检索的检索类型。枚举值： `Expedited`、`Standard` 和 `Bulk`。默认值：`Standard`。 | String | 否   |

#### 检索档案列表
示例如下：
```json
{
	"Type": "inventory-retrieval",
	"Description": "String",
	"Format": "String",
	"InventoryRetrievalParameters": {
		"StartDate": "String",
		"EndDate": "String",
		"Limit": "String",
		"Marker": "String"
	}
}
```

参数说明如下：

| 名称                         | 描述                                                         | 类型   | 必选 |
| ---------------------------- | ------------------------------------------------------------ | ------ | ---- |
| Type                         | 任务类型，`inventory-retrieval`，当检索 Archive 列表时，此处填写 `inventory-retrieval` | String | 是   |
| Description                  | 任务的描述                                                   | String | 否   |
| Format                       | Archive 列表输出格式，枚举值： `CSV` ，`JSON`。默认值：`JSON` | String | 否   |
| InventoryRetrievalParameters | Archive 列表检索的相关配置                                   | String | 否   |
| StartDate                    | Archive 列表检索的开始日期（采用 UTC 格式），包含当日或之后创建的档案。ISO 8601 日期格式 `YYYY-MM-DDThh:mm:ssZ`（以秒为单位）的字符串表示。例如， 2017-02-28T17:03:43Z | String | 否   |
| EndDate                      | Archive 列表检索的结束日期（采用 UTC 格式），包含当日或之前创建的档案。ISO 8601 日期格式 `YYYY-MM-DDThh:mm:ssZ`（以秒为单位）的字符串表示。例如， 2017-02-28T17:03:43Z | String | 否   |
| Limit                        | Archive 列表检索请求返回的最大条目数。默认值：10000，有效值：1-10000之间的正整数 | String | 否   |
| Marker                       | 字典序，从 Marker 起读取对应 Archive 列表                    | String | 否   |


## 返回值

### 返回头部

| 名称           | 描述                                       | 类型     |
| ------------ | ---------------------------------------- | ------ |
| Location     | 任务的相对 URI 路径，格式 /< UID >/vaults/< VaultName >/jobs/< JobID > | String |
| x-cas-job-id | 任务的 ID，即 JobID               | String |

### 返回内容
无返回内容。

