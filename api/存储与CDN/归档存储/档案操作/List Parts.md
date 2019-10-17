## 功能描述

List Parts请求实现列出已上传的数据段。

## 请求

### 请求语法

```HTTP
GET /<UID>/vaults/<VaultName>/multipart-uploads/<uploadID> HTTP/1.1
Host: cas.<Region>.myqcloud.com
Date: Date
Authorization: Auth
```

### 请求参数

| 名称     | 描述                            | 类型     | 必选   |
| ------ | ----------------------------- | ------ | ---- |
| limit  | 要返回部分的最大数目。最大值和默认值都为 1000。    | 正整数    | 否    |
| marker | 所有的块以OffSet排序，`marker` 指定应从该Offset值开始列出段 | String | 否   |

### 请求头部

无特殊请求头部，其他头部请参见公共请求头部。

### 请求内容

无请求内容

## 返回值

### 返回头部

无特殊返回头部，其他头部请参见公共返回头部。

### 返回内容

| 名称                 | 描述                                       | 类型     |
| ------------------ | ---------------------------------------- | ------ |
| ArchiveDescription | 在启动分段上传请求中指定的档案描述，若无，则返回NULL             | String |
| CreationDate       | 分段上传启动的 UTC 时间，ISO 8601 日期格式，例如， 2013-03-20T17:03:43.221Z | String |
| Marker             | 如果未展示完所有结果，则返回下一页的Marker，否则返回NULL        | String |
| MultipartUploadId  | 用以标示上传的UploadID                          | String |
| PartSizeInBytes    | 固定的每段大小（以字节为单位）                           | Number |
| Parts              | 分段上传的数据段的列表                              | Array  |
| RangeInBytes       | 数据段的字节范围                                 | String |
| SHA256TreeHash     | 数据段的SHA256 树形哈希值                         | String |
| VaultQCS           | 文件库的资源名称                                 | String |

```JSON
{
	"ArchiveDescription": "String",
	"CreationDate": "String",
	"Marker": "String",
	"MultipartUploadId": "String",
	"PartSizeInBytes": "Number",
	"Parts": [{
			"RangeInBytes": "String",
			"SHA256TreeHash": "String"
		},
		...
	],
	"VaultQCS": "String"
}
```
