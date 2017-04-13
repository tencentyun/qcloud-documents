## 功能描述

Initiate Job 请求实现将 Archive 或者 Archive 列表取出到缓存池，该过程可能需要 3-5 小时。完成以后，用户可以通过Get Job Output 读取对应 Archive。

支持跨账户操作。当操作本账户时，UID为"-"。

目前提供三种检索数据的模式:

| -      | Expedited | Standard | Bulk    |
| ------ | --------- | -------- | ------- |
| 数据访问时间 | 1-5 分钟    | 3-5 小时   | 5-12 小时 |


如果没有足够的容量处理 Expedited 类型请求时，则返回503 InsufficientCapacityException。

## 请求

### 请求语法

```HTTP
POST /<UID>/vaults/<VaultName>/jobs HTTP 1.1
Host:cas.<Region>.myqcloud.com
Date:date
Authorization: Auth
```

### 请求参数

无特殊请求参数。

### 请求头部

无特殊请求头部，其他头部请参见公共请求头部。

### 请求内容

检索Archive

| 名称                 | 描述                                       | 类型     | 必选   |
| ------------------ | ---------------------------------------- | ------ | ---- |
| Type               | 任务类型，当检索Archive时，此处填写`archive-retrieval` | String | 是    |
| ArchiveId          | 检索的档案的 ID                                | String | 是    |
| Description        | 任务的描述                                    | String | 否    |
| RetrievalByteRange | 档案检索操作要检索的字节范围。其格式为“*StartByteValue*-*EndByteValue*”。如果未指定，则检索整个档案。如果指定了字节范围，则字节范围必须以兆字节 (1 024\*1 024) 对齐，这意味着，*StartByteValue* 必须可被 1MB 整除，并且 *EndByteValue* 加 1 必须可被 1MB 整除，或者等于指定为档案字节大小值减 1 的结束值。如果 RetrievalByteRange 没有以兆字节对齐，则此操作会返回 `400` 响应。 | String | 否    |
| Tier               | Archive检索的检索类型。枚举值： `Expedited` ，`Standard` ，`Bulk`。默认值：`Standard` | String | 否    |

```json
{
  "Type": "archive-retrieval",
  "ArchiveId": String,
  "Description": String,
  "RetrievalByteRange": String,
  "Tier": String 
}
```

检索Archive列表

| 名称                           | 描述                                       | 类型     | 必选   |
| ---------------------------- | ---------------------------------------- | ------ | ---- |
| Type                         | 任务类型，`inventory-retrieval`，当检索Archive列表时，此处填写`inventory-retrieval` | String | 是    |
| Description                  | 任务的描述                                    | String | 否    |
| Format                       | Archive列表输出格式，枚举值： `CSV` ，`JSON`。默认值：`JSON` | String | 否    |
| InventoryRetrievalParameters | Archive列表检索的相关配置                         | String | 否    |
| StartDate                    | Archive列表检索的开始日期（采用 UTC 格式），包含当日或之后创建的档案。ISO 8601 日期格式 `YYYY-MM-DDThh:mm:ssTZD`（以秒为单位）的字符串表示 | String | 否    |
| EndDate                      | Archive列表检索的结束日期（采用 UTC 格式），包含当日或之后创建的档案。ISO 8601 日期格式 `YYYY-MM-DDThh:mm:ssTZD`（以秒为单位）的字符串表示 | String | 否    |
| Limit                        | Archive列表检索请求返回的最大条目数。默认值：10000，有效值：正整数  | String | 否    |
| Marker                       | 字典序，从Marker起读取对应Archive列表                | String | 否    |

```json
{
  "Type":"inventory-retrieval",
  "Description": String,
  "Format": String,  
  "InventoryRetrievalParameters": { 
      "StartDate": String,
      "EndDate": String,
      "Limit": String,
      "Marker": String
   }   
}
```

## 返回值

### 返回头部

| 名称           | 描述                                       | 类型     |
| ------------ | ---------------------------------------- | ------ |
| Location     | 任务的相对 URI 路径，格式 / <UID> / vaults / <VaultName> / jobs / <JobID> | String |
| x-cas-job-id | 任务的 ID，即 JobID                           | String |

### 返回内容

无返回内容
