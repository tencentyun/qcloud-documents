## 功能描述

Initiate Job 请求实现将档案或者档案列表取出到缓存池。操作完成后，用户可以通过 Get Job Output 请求读取对应档案或者档案列表。

### 细节分析

检索任务所对应的三种模式下的时间如下表：

|  任务类型   | Expedited | Standard | Bulk    |
| --------- | --------- | -------- | ------- |
| 检索档案的任务时间 | 1-5分钟，<br>最大支持256MB 文件    | 3-5小时   | 5-12小时 |
| 检索档案列表的任务时间 | -|3-5小时   |-|

Initiate Job 请求还实现了同账户之内**从归档存储导入档案到对象存储**和**从对象存储导入对象到归档存储**两个特性。这两个特性需在 [CAS 控制台](https://console.cloud.tencent.com/cas/vault) 的【权限管理】中**预配置内部系统权限**，赋予 COS 所有操作行为的权限。

从归档存储导入档案到对象存储三种模式对应的时间：

|任务描述     | Expedited | Standard | Bulk    |
| -------------- | --------- | -------- | ------- |
| 导入档案到对象存储的任务时间 | 1-5分钟    | 3-5小时   | 5-12小时 |

>!该请求支持跨账户操作。当操作本账户时，UID 为"-"。

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
	"CallBackUrl": "String",
	"Description": "String",
	"RetrievalByteRange": "String",
	"Tier": "String"
}
```

参数说明如下：

| 名称                 | 描述                                       | 类型     | 必选   |
| ------------------ | ---------------------------------------- | ------ | ---- |
| Type               | 任务类型，当检索 Archive 时，此处填写`archive-retrieval` | String | 是    |
| ArchiveId          | 检索的档案的 ID                                | String | 是    |
| CallBackUrl        | 回调的 HTTP 地址，地址必须以 `http://` 或者 `https://` 开头   | String | 否    |
| Description        | 任务的描述                                    | String | 否    |
| RetrievalByteRange | 档案检索操作要检索的字节范围。其格式为“StartByteValue-EndByteValue”。如果未指定，则检索整个档案。如果指定了字节范围，则字节范围必须以兆字节 (1024\*1024) 对齐，这意味着，StartByteValue 必须可被1MB 整除，并且 EndByteValue 加1必须可被1MB整除，或者等于指定为档案字节大小值减1的结束值。如果 RetrievalByteRange 没有以兆字节对齐，则此操作会返回`400`响应。 | String | 否    |
| Tier               | Archive 检索的检索类型。枚举值： `Expedited`、`Standard` 和 `Bulk`。默认值：`Standard`。| String | 否    |

#### 检索档案列表
示例如下：
```json
{
	"Type": "inventory-retrieval",
	"CallBackUrl": "String",
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

| 名称                           | 描述                                       | 类型     | 必选   |
| ---------------------------- | ---------------------------------------- | ------ | ---- |
| Type                         | 任务类型，`inventory-retrieval`，当检索 Archive 列表时，此处填写 `inventory-retrieval` | String | 是    |
| CallBackUrl                  | 回调的 HTTP 地址，地址必须以 `http://` 或者 `https://` 开头   | String | 否    |
| Description                  | 任务的描述                                    | String | 否    |
| Format                       | Archive 列表输出格式，枚举值： `CSV` ，`JSON`。默认值：`JSON` | String | 否    |
| InventoryRetrievalParameters | Archive 列表检索的相关配置                         | String | 否    |
| StartDate                    | Archive 列表检索的开始日期（采用 UTC 格式），包含当日或之后创建的档案。ISO 8601 日期格式 `YYYY-MM-DDThh:mm:ssZ`（以秒为单位）的字符串表示。例如， 2017-02-28T17:03:43Z | String | 否    |
| EndDate                      | Archive 列表检索的结束日期（采用 UTC 格式），包含当日或之前创建的档案。ISO 8601 日期格式 `YYYY-MM-DDThh:mm:ssZ`（以秒为单位）的字符串表示。例如， 2017-02-28T17:03:43Z | String | 否    |
| Limit                        | Archive 列表检索请求返回的最大条目数。默认值：10000，有效值：1-10000之间的正整数 | String | 否    |
| Marker                       | 字典序，从 Marker 起读取对应 Archive 列表                | String | 否    |


#### 将档案导入 COS

示例如下：
```json
{
	"Type": "push-to-cos",
	"Description": "String",
	"ArchiveId": "String",
	"CallBackUrl": "String",
	"RetrievalByteRange": "String",
	"Tier": "String",
	"Bucket": "String",
	"Object": "String"
}
```

参数说明如下：

| 名称                 | 描述                                       | 类型     | 必选   |
| ------------------ | ---------------------------------------- | ------ | ---- |
| Type               | 任务类型，将档案导入COS时，此处填写`push-to-cos`        | String | 是    |
| ArchiveId          | 检索的档案的 ID                                | String | 是    |
| CallBackUrl        | 回调的HTTP地址，地址必须以 http:// 或者 https:// 开头   | String | 否    |
| Description        | 任务的描述                                    | String | 否    |
| RetrievalByteRange | 档案检索操作要检索的字节范围。其格式为“StartByteValue-EndByteValue”。如果未指定，则检索整个档案。如果指定了字节范围，则字节范围必须以兆字节 (1 024\*1 024) 对齐，这意味着，StartByteValue 必须可被1MB 整除，并且 EndByteValue 加 1 必须可被 1MB 整除，或者等于指定为档案字节大小值减 1 的结束值。如果 RetrievalByteRange 没有以兆字节对齐，则此操作会返回 `400` 响应。 | String | 否    |
| Tier               | Archive检索的检索类型。枚举值： `Expedited` ，`Standard` ，`Bulk`。默认值：`Standard` | String | 否    |
| Bucket             | COS 中目标 Bucket 的域名                          | String | 是    |
| Object             | COS 中目标 Bucket 的 Object 地址                    | String | 是    |


#### 从 COS 中拉取对象文件

示例如下：
```json
{
	"Type": "pull-from-cos",
	"CallBackUrl": "String",
	"Description": "String",
	"Bucket": "String",
	"Object": "String",
	"Range": "String",
	"Condition": {
		"If-Modified-Since": "String",
		"If-Umodified-Since": "String",
		"If-Match": "String",
		"If-None-Match": "String"
	},
	"ArchiveDescription": "String"
}
```

参数说明如下：

| 名称                 | 描述                                     | 类型     | 必选   |
| ------------------ | -------------------------------------- | ------ | ---- |
| Type               | 任务类型，从 COS 中拉取对象文件，此处填写 `pull-from-cos`  | String | 是    |
| CallBackUrl        | 回调的 HTTP 地址，地址必须以 http:// 或者 https:// 开头 | String | 否    |
| Description        | 任务的描述                                  | String | 否    |
| Bucket             | COS 中源 Bucket 的域名                         | String | 是    |
| Object             | COS 中源 Bucket 的 Object 地址                   | String | 是    |
| Range              | COS 中源 Object 的 Range 范围， 以字节（bytes）为单位     | String | 是    |
| Condition          | 从 COS 获取数据的前置条件                          | Array  | 否    |
| If-Modified-Since  | 如果文件修改时间晚于指定时间，返回文件内容。                 | String | 否    |
| If-Umodified-Since | 如果文件修改时间早于指定时间，返回文件内容。                 | String | 否    |
| If-Match           | 如果文件 ETag 与指定的一致，返回文件内容。                 | String | 否    |
| If-None-Match      | 如果文件 ETag 与指定的不一致，返回文件内容。                | String | 否    |
| ArchiveDescription | 档案文件描述                                 | String | 否    |


## 返回值

### 返回头部

| 名称           | 描述                                       | 类型     |
| ------------ | ---------------------------------------- | ------ |
| Location     | 任务的相对 URI 路径，格式 /< UID >/vaults/< VaultName >/jobs/< JobID > | String |
| x-cas-job-id | 任务的 ID，即 JobID               | String |

### 返回内容
无返回内容。

