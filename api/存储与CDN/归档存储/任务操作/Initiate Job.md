## 功能描述

Initiate Job 请求实现将档案或者档案列表取出到缓存池，该过程可能需要 3-5 小时。完成以后，用户可以通过Get Job Output 读取对应 Archive。

同时还实现了同账户之内**从对象存储导入对象到归档存储**，**将档案导入对象存储**两个特性，后者支持三种检索模式，实施过程需要花费3-5小时。以上两个特性需在CAS控制台-权限管理中预配置内部系统权限，赋予COS所有行为的权限

支持跨账户操作。当操作本账户时，UID为"-"。

目前提供三种检索数据的模式:

| -      | Expedited | Standard | Bulk    |
| ------ | --------- | -------- | ------- |
| 数据访问时间 | 1-5 分钟    | 3-5 小时   | 5-12 小时 |

 Expedited 类型请求，最大支持256 MB文件。

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
| EndDate                      | Archive列表检索的结束日期（采用 UTC 格式），包含当日或之前创建的档案。ISO 8601 日期格式 `YYYY-MM-DDThh:mm:ssTZD`（以秒为单位）的字符串表示 | String | 否    |
| Limit                        | Archive列表检索请求返回的最大条目数。默认值：10000，有效值：1-10000之间的正整数 | String | 否    |
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

将档案导入COS

| 名称                 | 描述                                       | 类型     | 必选   |
| ------------------ | ---------------------------------------- | ------ | ---- |
| Type               | 任务类型，将档案导入COS时，此处填写` push-to-cos`        | String | 是    |
| ArchiveId          | 检索的档案的 ID                                | String | 是    |
| Description        | 任务的描述                                    | String | 否    |
| RetrievalByteRange | 档案检索操作要检索的字节范围。其格式为“*StartByteValue*-*EndByteValue*”。如果未指定，则检索整个档案。如果指定了字节范围，则字节范围必须以兆字节 (1 024\*1 024) 对齐，这意味着，*StartByteValue* 必须可被 1MB 整除，并且 *EndByteValue* 加 1 必须可被 1MB 整除，或者等于指定为档案字节大小值减 1 的结束值。如果 RetrievalByteRange 没有以兆字节对齐，则此操作会返回 `400` 响应。 | String | 否    |
| Tier               | Archive检索的检索类型。枚举值： `Expedited` ，`Standard` ，`Bulk`。默认值：`Standard` | String | 否    |
| Bucket             | COS中目标Bucket的域名                          | String | 是    |
| Object             | COS中目标Bucket的Object地址                    | String | 是    |

```json
{
  "Type": "push-to-cos",
  "Description": String,
  "ArchiveId": String,
  "RetrievalByteRange":String,
  "Tier":String,
  "Bucket":String,
  "Object":String
}
```

从COS中拉取对象文件

| 名称                 | 描述                                    | 类型     | 必选   |
| ------------------ | ------------------------------------- | ------ | ---- |
| Type               | 任务类型，从COS中拉取对象文件，此处填写` pull-from-cos` | String | 是    |
| Description        | 任务的描述                                 | String | 否    |
| Bucket             | COS中源Bucket的域名                        | String | 是    |
| Object             | COS中源Bucket的Object地址                  | String | 是    |
| Range              | COS中源Object的Range范围， 以字节（bytes）为单位    | String | 是    |
| Condition          | 从COS获取数据的前置条件                         | Array  | 否    |
| If-Modified-Since  | 如果文件修改时间晚于指定时间，返回文件内容。否则返回 304        | String | 否    |
| If-Umodified-Since | 如果文件修改时间早于指定时间，返回文件内容。否则返回 412        | String | 否    |
| If-Match           | 如果文件ETag与指定的一致，返回文件内容。否则返回 412        | String | 否    |
| If-None-Match      | 如果文件ETag与指定的不一致，返回文件内容。否则返回 412       | String | 否    |
| ArchiveDescription | 档案文件描述                                | String | 否    |

```json
{
  "Type": "pull-from-cos",
  "Description":String,
  "Bucket":String,
  "Object":String,
  "Range":String,
  "Condition":{
    "If-Modified-Since":String,
    "If-Umodified-Since":String,
    "If-Match":String,
    "If-None-Match":String
  },
  "ArchiveDescription":String
}
```

## 返回值

### 返回头部

| 名称           | 描述                                       | 类型     |
| ------------ | ---------------------------------------- | ------ |
| Location     | 任务的相对 URI 路径，格式 /< UID >/vaults/< VaultName >/jobs/< JobID > | String |
| x-cas-job-id | 任务的 ID，即 JobID                           | String |

### 返回内容

无返回内容
