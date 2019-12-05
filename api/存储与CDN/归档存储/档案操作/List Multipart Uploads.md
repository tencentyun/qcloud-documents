## 功能描述

List Multipart Uploads请求实现列出正在进行中的分段上传

## 请求

### 请求语法

```HTTP
GET /<UID>/vaults/<VaultName>/multipart-uploads HTTP/1.1
Host: cas.<Region>.myqcloud.com
Date: Date
Authorization: Auth
```

### 请求参数

| 名称     | 描述                         | 类型     | 必选   |
| ------ | -------------------------- | ------ | ---- |
| limit  | 要返回部分的最大数目。最大值和默认值都为 1000。 | 正整数    | 否    |
| marker | 不透明字符串，用来标示一个分段上传，所有的分段上传以时间正序排序，`marker` 指定应从该上传的创建时间点列出其后所有的分段上传  | String | 否    |

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
| Marker             | 如果未展示完所有结果，则返回下一页的Marker，否则返回NULL        | String |
| UploadsList        | 分段上传的列表                                  | Array  |
| ArchiveDescription | 在初始化分段上传请求中指定的档案描述，如无则返回NULL             | String |
| CreationDate       | 分段上传启动的 UTC 时间，ISO 8601 日期格式，举例2013-03-20T17:03:43.221Z | String |
| MultipartUploadId  | 分段上传的 ID                                 | String |
| PartSizeInBytes    | 初始化分段上传请求中指定的段大小                         | Number |
| VaultQCS           | 文件库的资源名称                                 | String |

```JSON
{
	"Marker": "String",
	"UploadsList": [{
			"ArchiveDescription": "String",
			"CreationDate": "String",
			"MultipartUploadId": "String",
			"PartSizeInBytes": "Number",
			"VaultQCS": "String"
		},
		...
	]
}
```
