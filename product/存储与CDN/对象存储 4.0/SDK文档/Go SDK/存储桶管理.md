## 简介
本文档提供关于跨域访问、生命周期、版本控制和跨地域复制相关的 API 概览以及 SDK 示例代码。

**跨域访问**

| API                                                          | 操作名       | 操作描述                       |
| ------------------------------------------------------------ | ------------ | ------------------------------ |
| [PUT Bucket cors](https://cloud.tencent.com/document/product/436/8279) | 设置跨域配置 | 设置存储桶的跨域访问权限     |
| [GET Bucket cors](https://cloud.tencent.com/document/product/436/8274) | 查询跨域配置 | 查询存储桶的跨域访问配置信息 |
| [DELETE Bucket cors](https://cloud.tencent.com/document/product/436/8283) | 删除跨域配置 | 删除存储桶的跨域访问配置信息 |

**生命周期**

| API                                                          | 操作名       | 操作描述                         |
| ------------------------------------------------------------ | ------------ | -------------------------------- |
| [PUT Bucket lifecycle](https://cloud.tencent.com/document/product/436/8280) | 设置生命周期 | 设置存储桶的生命周期管理的配置 |
| [GET Bucket lifecycle](https://cloud.tencent.com/document/product/436/8278) | 查询生命周期 | 查询存储桶生命周期管理的配置   |
| [DELETE Bucket lifecycle](https://cloud.tencent.com/document/product/436/8284) | 删除生命周期 | 删除存储桶生命周期管理的配置   |

**版本控制**

| API | 操作名 | 操作描述 |
| ------------------- | ------------ | ------------------ |
| [PUT Bucket versioning](https://cloud.tencent.com/document/product/436/19889) | 设置版本控制   | 设置存储桶的版本控制功能 |
| [GET Bucket versioning](https://cloud.tencent.com/document/product/436/19888) | 查询版本控制 | 查询存储桶的版本控制信息 |

**跨地域复制**

| API | 操作名 | 操作描述 |
| ------------------- | ------------ | ------------------ |
| [PUT Bucket replication](https://cloud.tencent.com/document/product/436/19223) | 设置跨地域复制   | 设置存储桶的跨地域复制规则 |
| [GET Bucket replication](https://cloud.tencent.com/document/product/436/19222) | 查询跨地域复制 | 查询存储桶的跨地域复制规则 |
| [DELETE Bucket replication](https://cloud.tencent.com/document/product/436/19221) | 删除跨地域复制 | 删除存储桶的跨地域复制规则 |


## 跨域访问
### 设置跨域配置

#### 功能说明

设置指定存储桶的跨域访问配置信息（PUT Bucket cors）。

#### 方法原型
```go
func (s *BucketService) PutCORS(ctx context.Context, opt *BucketPutCORSOptions) (*Response, error)
```

#### 请求示例
```go
opt := &cos.BucketPutCORSOptions{
    Rules: []cos.BucketCORSRule{
        {
            AllowedOrigins: []string{"http://www.qq.com"},
            AllowedMethods: []string{"PUT", "GET"},
            AllowedHeaders: []string{"x-cos-meta-test", "x-cos-xx"},
            MaxAgeSeconds:  500,
            ExposeHeaders:  []string{"x-cos-meta-test1"},
        },
        {
            ID:             "1234",
            AllowedOrigins: []string{"http://www.baidu.com", "twitter.com"},
            AllowedMethods: []string{"PUT", "GET"},
            MaxAgeSeconds:  500,
        },
    },
}
resp, err := client.Bucket.PutCORS(context.Background(), opt)
```

#### 参数说明

```go
type BucketCORSRule struct {
	ID             string   
	AllowedMethods []string 
	AllowedOrigins []string 
	AllowedHeaders []string 
	MaxAgeSeconds  int      
	ExposeHeaders  []string 
}
```

| 参数名称       | 参数描述                                                     | 类型     | 必填 |
| -------------- | ------------------------------------------------------------ | -------- | ---- |
| BucketCORSRule | 设置对应的跨域规则，包括 ID，MaxAgeSeconds，AllowedOrigin，AllowedMethod，AllowedHeader，ExposeHeader | struct   | 是   |
| ID             | 设置规则的 ID                                                | string   | 否   |
| AllowedMethods | 设置允许的方法，如 GET，PUT，HEAD，POST，DELETE              | []string | 是   |
| AllowedOrigins | 设置允许的访问来源，如 `"http://cloud.tencent.com"`，支持通配符 * | []string | 是   |
| AllowedHeaders | 设置请求可以使用哪些自定义的 HTTP 请求头部，支持通配符 *     | []string | 否   |
| MaxAgeSeconds  | 设置 OPTIONS 请求得到结果的有效期                            | int      | 否   |
| ExposeHeaders  | 设置浏览器可以接收到的来自服务器端的自定义头部信息           | []string | 否   |


### 查询跨域配置

#### 功能说明

查询存储桶的跨域访问配置信息（GET Bucket cors）。

#### 方法原型
```go
func (s *BucketService) GetCORS(ctx context.Context) (*BucketGetCORSResult, *Response, error)
```

#### 请求示例
```go
v, resp, err := client.Bucket.GetCORS(context.Background())
```

#### 返回结果说明
通过 GetBucketCORSResult 返回请求结果。

```go
type BucketCORSRule struct {
	ID             string   
	AllowedMethods []string 
	AllowedOrigins []string 
	AllowedHeaders []string 
	MaxAgeSeconds  int      
	ExposeHeaders  []string 
}
```

| 参数名称       | 参数描述                                                     | 类型     | 必填 |
| -------------- | ------------------------------------------------------------ | -------- | ---- |
| BucketCORSRule | 设置对应的跨域规则，包括 ID，MaxAgeSeconds，AllowedOrigin，AllowedMethod，AllowedHeader，ExposeHeader | struct   | 是   |
| ID             | 设置规则的 ID                                                | string   | 否   |
| AllowedMethods | 设置允许的方法，如 GET，PUT，HEAD，POST，DELETE              | []string | 是   |
| AllowedOrigins | 设置允许的访问来源，如 `"http://cloud.tencent.com"`，支持通配符 * | []string | 是   |
| AllowedHeaders | 设置请求可以使用哪些自定义的 HTTP 请求头部，支持通配符 *     | []string | 否   |
| MaxAgeSeconds  | 设置 OPTIONS 请求得到结果的有效期                            | int      | 否   |
| ExposeHeaders  | 设置浏览器可以接收到的来自服务器端的自定义头部信息           | []string | 否   |                 |

### 删除跨域配置

#### 功能说明

删除指定存储桶的跨域访问配置（DELETE Bucket cors）。

#### 方法原型

```go
func (s *BucketService) DeleteCORS(ctx context.Context) (*Response, error)
```

#### 请求示例
```go
resp, err := client.Bucket.DeleteCORS(context.Background())
```

## 生命周期
### 设置生命周期

#### 功能说明

设置指定存储桶的生命周期配置信息（PUT Bucket lifecycle）。

#### 方法原型
```go
func (s *BucketService) PutLifecycle(ctx context.Context, opt *BucketPutLifecycleOptions) (*Response, error)
```

#### 请求示例
```go
lc := &cos.BucketPutLifecycleOptions{
    Rules: []cos.BucketLifecycleRule{
        {
            ID:     "1234",
            Filter: &cos.BucketLifecycleFilter{Prefix: "test"},
            Status: "Enabled",
            Transition: &cos.BucketLifecycleTransition{
                Days:         10,
                StorageClass: "Standard",
            },
        },
        {
            ID:     "123422",
            Filter: &cos.BucketLifecycleFilter{Prefix: "gg"},
            Status: "Disabled",
            Expiration: &cos.BucketLifecycleExpiration{
                Days: 10,
            },
        },
    },
}
resp, err := client.Bucket.PutLifecycle(context.Background(), lc)
```

#### 参数说明
```go
type BucketLifecycleRule struct {
	ID                             string
	Status                         string
	Filter                         *BucketLifecycleFilter
	Transition                     *BucketLifecycleTransition
	Expiration                     *BucketLifecycleExpiration
	AbortIncompleteMultipartUpload  *BucketLifecycleAbortIncompleteMultipartUpload 
}
type BucketLifecycleFilter struct {
	Prefix       string 
}
type BucketLifecycleTransition struct {
	Date         string 
	Days         int    
	StorageClass string
}
type BucketLifecycleExpiration struct {
	Date string 
	Days int    
}
type BucketLifecycleAbortIncompleteMultipartUpload struct {
	DaysAfterInitiation string 
}
```

| 参数名称                       | 参数描述                                                     | 类型   | 必填 |
| ------------------------------ | ------------------------------------------------------------ | ------ | ---- |
| BucketLifecycleRule            | 设置对应的规则，包括 ID，Filter，Status，Expiration，Transition，AbortIncompleteMultipartUpload | List   | 是   |
| ID                             | 设置规则的 ID                                                | string | 否   |
| Status                         | 设置 Rule 是否启用，可选值为 Enabled 或者 Disabled           | string | 是   |
| Filter                         | 用于描述规则影响的 Object 集合，如需设置 Bucket 中的所有 objects，请设置 Prefix 为空 | struct | 是   |
| Transition                     | 设置 Object 转换存储类型规则，可以指定天数 Days 或者指定日期 Date，Date 的格式必须是 GMT ISO 8601。StorageClass 可选 Standard_IA，Archive，可以同时设置多条此类规则 | struct | 否   |
| Expiration                     | 设置 Object 过期规则，可以指定天数 Days 或者指定日期 Date，Date 的格式必须是 GMT ISO 8601 | struct | 否   |
| AbortIncompleteMultipartUpload | 指明分块上传开始后多少天内必须完成上传                       | struct | 否   |

### 查询生命周期

#### 功能说明

查询存储桶生命周期管理的配置（GET Bucket lifecycle）。

#### 方法原型
```go
func (s *BucketService) GetLifecycle(ctx context.Context) (*BucketGetLifecycleResult, *Response, error)
```

#### 请求示例

```go
v, resp, err := client.Bucket.GetLifecycle(context.Background()) 
```

#### 返回结果说明

通过 GetBucketLifecycleResult 返回请求结果。

```go
type BucketLifecycleRule struct {
	ID                             string
	Status                         string
	Filter                         *BucketLifecycleFilter
	Transition                     *BucketLifecycleTransition
	Expiration                     *BucketLifecycleExpiration
	AbortIncompleteMultipartUpload  *BucketLifecycleAbortIncompleteMultipartUpload 
}
type BucketLifecycleFilter struct {
	Prefix       string 
}
type BucketLifecycleTransition struct {
	Date         string 
	Days         int    
	StorageClass string
}
type BucketLifecycleExpiration struct {
	Date string 
	Days int    
}
type BucketLifecycleAbortIncompleteMultipartUpload struct {
	DaysAfterInitiation string 
}
```

| 参数名称                       | 参数描述                                                     | 类型   | 必填 |
| ------------------------------ | ------------------------------------------------------------ | ------ | ---- |
| BucketLifecycleRule            | 设置对应的规则，包括 ID，Filter，Status，Expiration，Transition，AbortIncompleteMultipartUpload | List   | 是   |
| ID                             | 设置规则的 ID                                                | string | 否   |
| Status                         | 设置 Rule 是否启用，可选值为 Enabled 或者 Disabled           | string | 是   |
| Filter                         | 用于描述规则影响的 Object 集合，如需设置 Bucket 中的所有 objects，请设置 Prefix 为空 | struct | 是   |
| Transition                     | 设置 Object 转换存储类型规则，可以指定天数 Days 或者指定日期 Date，Date 的格式必须是 GMT ISO 8601。StorageClass 可选 Standard_IA，Archive，可以同时设置多条此类规则 | struct | 否   |
| Expiration                     | 设置 Object 过期规则，可以指定天数 Days 或者指定日期 Date，Date 的格式必须是 GMT ISO 8601 | struct | 否   |
| AbortIncompleteMultipartUpload | 指明分块上传开始后多少天内必须完成上传                       | struct | 否   |


### 删除生命周期

#### 功能说明

删除存储桶生命周期管理的配置（DELETE Bucket lifecycle）。

#### 方法原型

```go
func (s *BucketService) DeleteLifecycle(ctx context.Context) (*Response, error)
```

#### 请求示例

```go
resp, err := client.Bucket.DeleteLifecycle(context.Background())
```

## 版本控制
### 设置版本控制

#### 功能说明

设置指定存储桶的版本控制功能（PUT Bucket versioning）。

#### 方法原型
```go
func (s *BucketService) PutVersioning(ctx context.Context, opt *BucketPutVersionOptions) (*Response, error)
```

#### 请求示例
```go
opt := &cos.BucketPutVersionOptions{
	// Enabled or Suspended, the versioning once opened can not close.
	Status: "Enabled",
}
resp, err := c.Bucket.PutVersioning(context.Background(), opt)
```

#### 参数说明
```go
type BucketPutVersionOptions struct {
	Status  string
}
```
| 参数名称| 描述  | 类型  |
| ----| ---- | ---- |
| BucketPutVersionOptions | 版本控制策略  | struct |
| Status | 说明版本是否开启，枚举值：Suspended（暂停版本控制）、Enabled（开启版本控制）  | string |

### 查询版本控制

#### 功能说明

查询指定存储桶的版本控制信息（GET Bucket versioning）。

#### 方法原型
```go
func (s *BucketService) GetVersioning(ctx context.Context) (*BucketGetVersionResult, *Response, error)
```

#### 请求示例
```go
v, resp, err := c.Bucket.GetVersioning(context.Background())
```

#### 返回结果说明
```go
type BucketGetVersionResult struct {
	Status  string
}
```
| 参数名称| 描述  | 类型  |
| ----| ---- | ---- |
| BucketGetVersionResult | 版本控制策略  | struct |
| Status | 说明版本是否开启，枚举值：Suspended（暂停版本控制）、Enabled（开启版本控制）  | string |

## 跨地域复制
### 设置跨地域复制

#### 功能说明

设置指定存储桶的跨地域复制规则（PUT Bucket replication）。

#### 方法原型
```go
func (s *BucketService) PutBucketReplication(ctx context.Context, opt *PutBucketReplicationOptions) (*Response, error)
```

#### 请求示例
```go
opt := &cos.PutBucketReplicationOptions{
	// qcs::cam::uin/[UIN]:uin/[Subaccount]
	Role: "qcs::cam::uin/100000000001:uin/100000000001",
	Rule: []cos.BucketReplicationRule{
		{
			ID: "1",
			// Enabled or Disabled
			Status: "Enabled",
			Destination: &cos.ReplicationDestination{
				// qcs::cos:[Region]::[Bucketname-Appid]
				Bucket: "qcs::cos:ap-guangzhou::examplebucket-1250000000",
			},
		},
	},
}
resp, err := c.Bucket.PutBucketReplication(context.Background(), opt)
```

#### 参数说明
```go
type PutBucketReplicationOptions struct {
	Role    string
	Rule    []BucketReplicationRule
}
type BucketReplicationRule struct {
	ID          string
	Status      string
	Prefix      string
	Destination *ReplicationDestination
}
type ReplicationDestination struct {
	Bucket       string
	StorageClass string
}
```
| 参数名称| 描述  | 类型  |
| ----| ---- | ---- |
| PutBucketReplicationOptions  | 跨地域复制规则 | struct                         |
| Role | 发起者身份标示：`qcs::cam::uin/<OwnerUin>:uin/<SubUin>`  | string |
| Rule | 具体配置信息，最多支持1000个，所有策略只能指向一个目标存储桶  | struct |
| ID | 	用来标注具体 Rule 的名称  | string |
| Status | 标识 Rule 是否生效，枚举值：Enabled, Disabled  | string |
| Prefix | 	前缀匹配策略，不可重叠，重叠返回错误。前缀匹配根目录为空  | string |
| Destination | 目标存储桶信息  | struct |
| Bucket | 资源标识符：`qcs::cos:[region]::[bucketname-AppId]`  | string | 
| StorageClass |  存储级别，枚举值：STANDARD，TANDARD_IA。默认值：原存储桶级别  | string |

### 查询跨地域复制

#### 功能说明

查询指定存储桶的跨地域复制规则（GET Bucket replication）。

#### 方法原型
```go
func (s *BucketService) GetBucketReplication(ctx context.Context) (*GetBucketReplicationResult, *Response, error)
```

#### 请求示例
```go
v, resp, err := c.Bucket.GetBucketReplication(context.Background())
```

#### 返回结果说明
```go
type GetBucketReplicationResult struct {
	Role    string
	Rule    []BucketReplicationRule
}
type BucketReplicationRule struct {
	ID          string
	Status      string
	Prefix      string
	Destination *ReplicationDestination
}
type ReplicationDestination struct {
	Bucket       string
	StorageClass string
}
```
| 参数名称| 描述  | 类型  |
| ----| ---- | ---- |
| GetBucketReplicationResult  | 跨地域复制规则 | struct                         |
| Role | 发起者身份标示：`qcs::cam::uin/<OwnerUin>:uin/<SubUin>`  | string |
| Rule | 具体配置信息，最多支持1000个，所有策略只能指向一个目标存储桶  | struct |
| ID | 	用来标注具体 Rule 的名称  | string |
| Status | 标识 Rule 是否生效，枚举值：Enabled，isabled  | string |
| Prefix | 	前缀匹配策略，不可重叠，重叠返回错误。前缀匹配根目录为空  | string |
| Destination | 目标存储桶信息  | struct |
| Bucket | 资源标识符：`qcs::cos:[region]::[bucketname-AppId]`  | string | 
| StorageClass |  存储级别，枚举值：STANDARD，ANDARD_IA。默认值：原存储桶级别  | string |


### 删除跨地域复制

#### 功能说明

删除指定存储桶的跨地域复制规则（DELETE Bucket replication）。

#### 方法原型
```go
func (s *BucketService) DeleteBucketReplication(ctx context.Context) (*Response, error)
```

#### 请求示例
```go
resp, err := c.Bucket.DeleteBucketReplication(context.Background())
```

