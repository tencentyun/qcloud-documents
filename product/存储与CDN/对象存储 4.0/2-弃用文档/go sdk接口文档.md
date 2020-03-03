COS Go SDK（XML API）操作返回相应 API 的 Result 结构和 Golang HTTP 标准库的 [Response](https://golang.org/pkg/net/http/#Response) 结构。

> ?关于文章中出现的 SecretId、SecretKey、Bucket 等名称的含义和获取方式请参考：[COS 术语信息](https://cloud.tencent.com/document/product/436/7751)。

## Service API 描述

### 获取存储桶列表

#### 功能说明

用来获取请求者名下的所有存储空间列表（Bucket list）。

#### 方法原型

```go
func (s *ServiceService) Get(ctx context.Context) (*ServiceGetResult, *Response, error)
```

#### 请求示例

```go
s, resp, err := c.Service.Get(context.Background()) 
```

#### 返回结果说明

```go
type ServiceGetResult struct {
    Owner   *Owner  
    Buckets []Bucket 
}
type Owner struct {
    ID          string 
    DisplayName string                                              
}
type Bucket struct {
	Name       string
    Region     string
    CreationDate string                                               
} 
```

| 参数名称     | 参数描述                                                     | 类型   |
| ------------ | ------------------------------------------------------------ | ------ |
| ID           | Bucket 所有者的 ID                                           | string |
| DisplayName  | Bucket 所有者的名字信息                                      | string |
| Name         | Bucket 的名称                                                | string |
| Region       | Bucket 所在地域                                              | string |
| CreationDate | Bucket 创建时间。ISO8601 格式，例如 2016-11-09T08:46:32.000Z | string |

## Bucket API 描述

### 创建存储桶

#### 功能说明

在指定账号下创建一个新的 Bucket，当 Bucket 已存在时会返回错误。

#### 方法原型

```go
func (s *BucketService) Put(ctx context.Context, opt *BucketPutOptions) (*Response, error)
```

#### 请求示例

```go
opt := &cos.BucketPutOptions{
	XCosACL: "public-read",
}
resp, err := client.Bucket.Put(context.Background(), opt)
```

#### 参数说明

```go
type BucketPutOptions struct {
	XCosACL              string 
	XCosGrantRead        string  
	XCosGrantWrite       string  
	XCosGrantFullControl string 
}
```

| 参数名称             | 参数描述                                                     | 类型   | 必填 |
| -------------------- | ------------------------------------------------------------ | ------ | ---- |
| XCosACL              | 设置 Bucket 的 ACL，如 private，public-read，public-read-write | string | 否   |
| XCosGrantFullControl | 赋予指定账户对 Bucket 的读写权限。格式为`id=" ",id=" "`当需要给子账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`当需要给根账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`例如`id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"` | string | 否   |
| XCosGrantRead        | 赋予指定账户对 Bucket 的读权限。格式为`id=" ",id=" "`当需要给子账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`当需要给根账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`例如`id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"` | string | 否   |
| XCosGrantWrite       | 赋予指定账户对 Bucket 的写权限。格式为`id=" ",id=" "`当需要给子账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`当需要给根账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`例如`id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"` | string | 否   |

### 删除存储桶

#### 功能说明

在指定账号下删除一个已经存在的 Bucket，删除时 Bucket 必须为空。

#### 方法原型

```go
func (s *BucketService) Delete(ctx context.Context) (*Response, error)
```

#### 请求示例

```go
resp, err := client.Bucket.Delete(context.Background())
```

### 检索存储桶及其权限

#### 功能说明

查询一个 Bucket 是否存在或者拥有访问权限。

#### 方法原型

```go
func (s *BucketService) Head(ctx context.Context) (*Response, error)
```

#### 请求示例

```go
resp, err := client.Bucket.Head(context.Background())
```

### 获取地域信息

#### 功能说明

查询一个 Bucket 所在 region 的信息。

#### 方法原型

```go
func (s *BucketService) GetLocation(ctx context.Context) (*BucketGetLocationResult, *Response, error)
```

#### 请求示例

```go
v, resp, err := client.Bucket.GetLocation(context.Background())
```

#### 返回结果说明

```go
type BucketGetLocationResult struct {
	Location string                                      
}
```

```go
{
    'Location': 'ap-beijing-1'|'ap-beijing'|'ap-shanghai'|'ap-guangzhou'|'ap-chengdu'|'ap-chongqing'|'ap-singapore'|'ap-hongkong'|'na-toronto'|'eu-frankfurt'|'ap-mumbai'|'ap-seoul'|'na-siliconvalley'|'na-ashburn'
}
```

| 参数名称 | 参数描述              | 类型   |
| -------- | --------------------- | ------ |
| Location | Bucket 所在地域的信息 | string |

### 获取对象列表

#### 功能说明

获取指定 Bucket 下的所有 Objects。

#### 方法原型

```go
func (s *BucketService) Get(ctx context.Context, opt *BucketGetOptions) (*BucketGetResult, *Response, error)
```

#### 请求示例

```go
opt := &cos.BucketGetOptions{
	Prefix:  "test",
	MaxKeys: 100,                                
}
v, resp, err := client.Bucket.Get(context.Background(), opt)
```

#### 参数说明

```go
type BucketGetOptions struct {
	Prefix       string 
	Delimiter    string 
	EncodingType string 
	Marker       string 
	MaxKeys      int    
}
```

| 参数名称     | 参数描述                                                     | 类型   | 必填 |
| ------------ | ------------------------------------------------------------ | ------ | ---- |
| Prefix       | 默认为空，对 object 的 key 进行筛选，匹配 prefix 为前缀的 objects | string | 否   |
| Delimiter    | 默认为空，设置分隔符，比如设置/来模拟文件夹                  | string | 否   |
| EncodingType | 默认不编码，规定返回值的编码方式，可选值：url                | string | 否   |
| Marker       | 默认以 UTF-8 二进制顺序列出条目，标记返回 objects 的 list 的起点位置 | string | 否   |
| MaxKeys      | 最多返回的 objects 数量，默认为最大的1000                    | int    | 否   |

#### 返回结果说明

```go
type BucketGetResult struct {
	Name           string
	Prefix         string 
	Marker         string 
	NextMarker     string 
	Delimiter      string 
	MaxKeys        int
	IsTruncated    bool
	Contents       []Object 
	CommonPrefixes []string 
	EncodingType   string   
}
```

| 参数名称       | 参数描述                                                     | 类型     |
| -------------- | ------------------------------------------------------------ | -------- |
| Name           | Bucket 名称，由 bucketname-appid 构成                        | string   |
| Prefix         | 默认为空，对 object 的 key 进行筛选，匹配 prefix 为前缀的 objects | string   |
| Marker         | 默认以 UTF-8 二进制顺序列出条目，标记返回 objects 的 list 的起点位置 | string   |
| NextMarker     | 当 IsTruncated 为 true 时，标记下一次返回 objects 的 list 的起点位置 | string   |
| Delimiter      | 默认为空，设置分隔符，比如设置/来模拟文件夹                  | string   |
| MaxKeys        | 最多返回的 objects 数量，默认为最大的1000                    | int      |
| IsTruncated    | 表示返回的 objects 否被截断                                  | bool     |
| Contents       | 包含所有 object 元信息的list，每个Object类型包括 ETag，StorageClass，Key，Owner，LastModified，Size等信息 | []Object |
| CommonPrefixes | 所有以 Prefix 开头，以 Delimiter 结尾的 Key 被归到同一类      | []string |
| EncodingType   | 默认不编码，规定返回值的编码方式，可选值：url                | string   |

### 查询分块上传

#### 功能说明

查询指定 Bucket 下的所有正在进行中的分块上传。

#### 方法原型

```go
func (s *BucketService) ListMultipartUploads(ctx context.Context, opt *ListMultipartUploadsOptions) (*ListMultipartUploadsResult, *Response, error)
```

#### 请求示例

```go
opt := &cos.ListMultipartUploadsOptions{
	Prefix: "test",
}
v, resp, err := client.Bucket.ListMultipartUploads(context.Background(), opt)
```

#### 参数说明

```go
type ListMultipartUploadsOptions struct {
	Delimiter      string 
	EncodingType   string 
	Prefix         string 
	MaxUploads     int    
	KeyMarker      string 
	UploadIDMarker string 
}
```

| 参数名称       | 参数描述                                                     | 类型   | 必填 |
| -------------- | ------------------------------------------------------------ | ------ | ---- |
| Delimiter      | 默认为空，设置分隔符                                         | string | 否   |
| EncodingType   | 默认不编码，规定返回值的编码方式，可选值：url                | string | 否   |
| Prefix         | 默认为空，对分块上传的 key 进行筛选，匹配 prefix 为前缀的分块上传 | string | 否   |
| MaxUploads     | 最多返回的分块上传的数量，默认为最大的1000                   | int    | 否   |
| KeyMarker      | 和 UploadIdMarker 一起使用，指明列出分块上传的起始位置       | string | 否   |
| UploadIdMarker | 和 KeyMarker 一起使用，指明列出分块上传的起始位置。如果没有指定 KeyMarker，UploadIdMarker 会被忽略 | string | 否   |

#### 返回结果说明

```go
type ListMultipartUploadsResult struct {
	Bucket             string   
	EncodingType       string   
	KeyMarker          string
	UploadIDMarker     string 
	NextKeyMarker      string
	NextUploadIDMarker string 
	MaxUploads         int
	IsTruncated        bool
	Uploads            []struct {
        Key          string
        UploadID     string 
        StorageClass string
        Initiator    *Initiator
        Owner        *Owner
        Initiated    string
	} 
	Prefix         string
	Delimiter      string   
	CommonPrefixes []string 
}
```

| 参数名称           | 参数描述                                                     | 类型     |
| ------------------ | ------------------------------------------------------------ | -------- |
| Bucket             | Bucket 名称，由 bucketname-appid 构成                        | string   |
| EncodingType       | 默认不编码，规定返回值的编码方式，可选值：url                | string   |
| KeyMarker          | 和 UploadIdMarker 一起使用，指明列出分块上传的 key 起始位置  | string   |
| UploadIdMarker     | 和 KeyMarker 一起使用，指明列出分块上传的 uploadid 起始位置。如果没有指定 KeyMarker，UploadIdMarker 会被忽略 | string   |
| NextKeyMarker      | 当 IsTruncated 为 true 时，指明下一次列出分块上传的 key 的起始位置 | string   |
| NextUploadIDMarker | 当 IsTruncated 为 true 时，指明下一次列出分块上传的 uploadid 的起始位置 | string   |
| MaxUploads         | 最多返回的分块上传的数量，默认为最大的1000                   | int      |
| IsTruncated        | 表示返回的分块上传否被截断                                   | bool     |
| Uploads             | 包含所有分块上传的 list，包括 UploadId，storageClass，Key，Owner，Initiator，Initiated 等信息 | []struct |
| Prefix             | 默认为空，对分块上传的 key 进行筛选，匹配 prefix 为前缀的分块上传 | string   |
| Delimiter          | 默认为空，设置分隔符                                         | string   |
| CommonPrefixes     | 所有以 Prefix 开头，以 Delimiter 结尾的 Key 被归到同一类      | []string |

### 设置存储桶 ACL

#### 功能说明

设置 Bucket 的 ACL 信息， 通过 XCosACL，XCosGrantFullControl，XCosGrantRead，XCosGrantWrite传入 header 的方式来设置 ACL，或者通过 ACLXML 传入 body 来设置 ACL，两种方式只能选择一种，否则会返回冲突。

#### 方法原型

```go
func (s *BucketService) PutACL(ctx context.Context, opt *BucketPutACLOptions) (*Response, error)
```

#### 请求示例

通过 header 设置 Bucket ACL。

```go
opt := &cos.BucketPutACLOptions{
	Header: &cos.ACLHeaderOptions{
		//private，public-read，public-read-write
		XCosACL: "private",
	},
}
resp, err := client.Bucket.PutACL(context.Background(), opt)
```

通过 body 设置 Bucket ACL。

```go
opt = &cos.BucketPutACLOptions{
    Body: &cos.ACLXml{
        Owner: &cos.Owner{
            ID: "qcs::cam::uin/100000760461:uin/100000760461",
        },
        AccessControlList: []cos.ACLGrant{
            {
                Grantee: &cos.ACLGrantee{
                    Type: "RootAccount",
                    ID:"qcs::cam::uin/100000760461:uin/100000760461",
                },
                Permission: "FULL_CONTROL",
            },
        },
    },
}
resp, err := client.Bucket.PutACL(context.Background(), opt)
```

#### 参数说明

```go
type ACLHeaderOptions struct {
	XCosACL              string 
	XCosGrantRead        string 
	XCosGrantWrite       string 
	XCosGrantFullControl string 
}
```

| 参数名称             | 参数描述                                                     | 类型   | 必填 |
| -------------------- | ------------------------------------------------------------ | ------ | ---- |
| XCosACL              | 设置 Bucket 的 ACL，如 private，public-read，public-read-write | string | 否   |
| XCosGrantFullControl | 赋予指定账户对 Bucket 的读写权限。格式为`id=" ",id=" "`当需要给子账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`当需要给根账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`例如`id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"` | string | 否   |
| XCosGrantRead        | 赋予指定账户对 Bucket 的读权限。格式为`id=" ",id=" "`当需要给子账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`当需要给根账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`例如`id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"` | string | 否   |
| XCosGrantWrite       | 赋予指定账户对 Bucket 的写权限。格式为`id=" ",id=" "`当需要给子账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`当需要给根账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`例如`id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"` | string | 否   |
| ACLXML               | 赋予指定账户对 Bucket 的访问权限，具体格式见 get bucket acl 返回结果说明 | struct | 否   |



### 获取存储桶 ACL

#### 功能说明

获取指定 Bucket 的 ACL 信息。

#### 方法原型

```go
func (s *BucketService) GetACL(ctx context.Context) (*BucketGetACLResult, *Response, error)
```

#### 请求示例

```go
v, resp, err := client.Bucket.GetACL(context.Background())
```

#### 返回结果说明

```go
type ACLXml struct {
	Owner             *Owner
	AccessControlList []ACLGrant 
}
type Owner struct { 
	ID          string 
	DisplayName string
}
type ACLGrant struct {
	Grantee    *ACLGrantee
	Permission string
}
type ACLGrantee struct {
	Type        string 
	ID          string 
	DisplayName string
    UIN         string 
}
```

| 参数名称          | 参数描述                                                     | 类型   |
| ----------------- | ------------------------------------------------------------ | ------ |
| Owner             | Bucket 拥有者的信息，包括 DisplayName 和 ID                  | struct |
| AccessControlList | Bucket 权限授予者的信息，包括 Grantee和 Permission           | struct |
| Grantee           | 权限授予者的信息，包括 DisplayName，Type，ID 和 UIN          | struct |
| Type              | 权限授予者的类型，类型为 CanonicalUser 或者 Group            | string |
| ID                | Type 为 CanonicalUser 时，对应权限授予者的 ID                | string |
| DisplayName       | 权限授予者的名字                                             | string |
| UIN               | Type 为 Group 时，对应权限授予者的 UIN                       | string |
| Permission        | 授予者所拥有的 Bucket 的权限，可选值有 FULL_CONTROL，WRITE，READ，分别对应读写权限、写权限、读权限 | string |

### 设置跨域配置

#### 功能说明

设置指定 Bucket 的跨域资源配置。

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

### 获取跨域配置

#### 功能说明

获取指定 Bucket 的跨域配置。

#### 方法原型

```go
func (s *BucketService) GetCORS(ctx context.Context) (*BucketGetCORSResult, *Response, error)
```

#### 请求示例

```go
v, resp, err := client.Bucket.GetCORS(context.Background())
```

#### 返回结果说明

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

### 删除跨域配置

#### 功能说明

删除指定 Bucket 的跨域配置。

#### 方法原型

```go
func (s *BucketService) DeleteCORS(ctx context.Context) (*Response, error)
```

#### 请求示例

```go
resp, err := client.Bucket.DeleteCORS(context.Background())
```

### 设置生命周期

#### 功能说明

设置指定 Bucket 的生命周期配置。

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
| Filter                         | 用于描述规则影响的 Object 集合,如需设置 bucket 中的所有 objects，请设置 Prefix 为空 | struct | 是   |
| Transition                     | 设置 Object 转换存储类型规则，可以指定天数 Days 或者指定日期 Date，Date 的格式必须是 GMT ISO 8601。StorageClass 可选 Standard_IA，Archive，可以同时设置多条此类规则 | struct | 否   |
| Expiration                     | 设置 Object 过期规则，可以指定天数 Days 或者指定日期 Date，Date 的格式必须是 GMT ISO 8601 | struct | 否   |
| AbortIncompleteMultipartUpload | 指明分块上传开始后多少天内必须完成上传                       | struct | 否   |

### 查询生命周期

#### 功能说明

查询指定 Bucket 的生命周期配置。

#### 方法原型

```go
func (s *BucketService) GetLifecycle(ctx context.Context) (*BucketGetLifecycleResult, *Response, error)
```

#### 请求示例

```go
v, resp, err := client.Bucket.GetLifecycle(context.Background()) 
```

#### 返回结果说明

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
| Filter                         | 用于描述规则影响的 Object 集合,如需设置 bucket 中的所有 objects，请设置 Prefix 为空 | struct | 是   |
| Transition                     | 设置 Object 转换存储类型规则，可以指定天数 Days 或者指定日期 Date，Date 的格式必须是 GMT ISO 8601。StorageClass 可选 Standard_IA，Archive，可以同时设置多条此类规则 | struct | 否   |
| Expiration                     | 设置 Object 过期规则，可以指定天数 Days 或者指定日期 Date，Date 的格式必须是 GMT ISO 8601 | struct | 否   |
| AbortIncompleteMultipartUpload | 指明分块上传开始后多少天内必须完成上传                       | struct | 否   |

### 删除生命周期

#### 功能说明

删除指定 Bucket 的生命周期配置。

#### 方法原型

```go
func (s *BucketService) DeleteLifecycle(ctx context.Context) (*Response, error)
```

#### 请求示例

```go
resp, err := client.Bucket.DeleteLifecycle(context.Background())
```

## Object API 描述

### 上传对象

#### 功能说明

支持上传本地文件或输入流到指定的 Bucket 中。推荐上传不大于20 MB 的小文件，单次上传大小限制为5GB，大文件上传请使用分块上传。

> !当前访问策略条目限制为1000条，如果您不需要进行对象 ACL 控制，请在上传时不要设置，默认继承 Bucket 权限。

#### 方法原型

```go
func (s *ObjectService) Put(ctx context.Context, key string, r io.Reader, opt *ObjectPutOptions) (*Response, error)
```

#### 请求示例

```go	
key := "put_option.go"
f, err := os.Open("./test")
opt := &cos.ObjectPutOptions{
	ObjectPutHeaderOptions: &cos.ObjectPutHeaderOptions{
		ContentType: "text/html",
	},
	ACLHeaderOptions: &cos.ACLHeaderOptions{
		XCosACL: "private",
	},
}
resp, err = client.Object.Put(context.Background(), key, f, opt)
```

#### 参数说明

```go
type ObjectPutOptions struct {
	*ACLHeaderOptions       
	*ObjectPutHeaderOptions 
}
type ACLHeaderOptions struct {
	XCosACL              string                           
    XCosGrantRead        string
    XCosGrantWrite       string 
    XCosGrantFullControl string                                           
} 
type ObjectPutHeaderOptions struct {
	CacheControl       string 
	ContentDisposition string 
	ContentEncoding    string 
	ContentType        string 
	ContentLength      int   
	Expires            string 
	// 自定义的 x-cos-meta-* header
	XCosMetaXXX        *http.Header 
	XCosStorageClass   string      
}
```

| 参数名称             | 参数描述                                                     | 类型        | 必填 |
| -------------------- | ------------------------------------------------------------ | ----------- | ---- |
| r                    | 上传文件的内容，可以为文件流或字节流，当 r 不是 bytes.Buffer/bytes.Reader/strings.Reader 时，必须指定 opt.ObjectPutHeaderOptions.ContentLength | io.Reader   | 是   |
| key                  | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | string      | 是   |
| XCosACL              | 设置文件的ACL，如 private，public-read，public-read-write    | string      | 否   |
| XCosGrantFullControl | 赋予指定账户对文件的读写权限。格式为`id=" ",id=" "`当需要给子账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`当需要给根账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`例如`id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"` | string      | 否   |
| XCosGrantRead        | 赋予指定账户对文件的读权限。格式为`id=" ",id=" "`当需要给子账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`当需要给根账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`例如`id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"` | string      | 否   |
| XCosGrantWrite       | 赋予指定账户对文件的写权限。格式为`id=" ",id=" "`当需要给子账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`当需要给根账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`例如`id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"` | string      | 否   |
| XCosStorageClass     | 设置文件的存储类型，STANDARD、STANDARD_IA、ARCHIVE，默认值：STANDARD   | string      | 否   |
| Expires              | 设置 Content-Expires                                         | string      | 否   |
| CacheControl         | 缓存策略，设置 Cache-Control                                 | string      | 否   |
| ContentType          | 内容类型，设置 Content-Type                                  | string      | 否   |
| ContentDisposition   | 文件名称，设置 Content-Disposition                           | string      | 否   |
| ContentEncoding      | 编码格式，设置 Content-Encoding                              | string      | 否   |
| ContentLength        | 设置传输长度                                                 | string      | 否   |
| XCosMetaXXX          | 用户自定义的文件元信息， 必须以 x-cos-meta 开头，否则会被忽略 | http.Header | 否   |

#### 返回结果说明

```go
{
    'ETag': 'string',
    'x-cos-expiration': 'string'
}
```

| 参数名称         | 参数描述                         | 类型   |
| ---------------- | -------------------------------- | ------ |
| ETag             | 上传文件的 MD5 值                | string |
| x-cos-expiration | 设置生命周期后，返回文件过期规则 | string |

### 获取对象

#### 功能说明

获取指定 Bucket 中的文件内容或下载文件到本地。

#### 方法原型

```go
func (s *ObjectService) Get(ctx context.Context, key string, opt *ObjectGetOptions) (*Response, error)

func (s *ObjectService) GetToFile(ctx context.Context, key, localfile string, opt *ObjectGetOptions) (*Response, error)
```

#### 请求示例

```go
key := "test/hello.txt"
opt := &cos.ObjectGetOptions{
	ResponseContentType: "text/html",
	Range:               "bytes=0-3",
}
//opt可选，无特殊设置可设为nil
resp, err := client.Object.Get(context.Background(), key, opt)
bs, _ = ioutil.ReadAll(resp.Body)
resp.Body.Close()
fmt.Printf("%s\n", string(bs))

// Download object to local file
_, err = c.Object.GetToFile(context.Background(), name, "hello_1.txt", nil)
if err != nil {
	panic(err)
}
```

#### 参数说明

```go
type ObjectGetOptions struct {
	ResponseContentType        string 
	ResponseContentLanguage    string 
	ResponseExpires            string 
	ResponseCacheControl       string 
	ResponseContentDisposition string 
	ResponseContentEncoding    string 
	Range                      string 
	IfModifiedSince            string 
}
```

| 参数名称                   | 参数描述                                                     | 类型   | 必填 |
| -------------------------- | ------------------------------------------------------------ | ------ | ---- |
| key                        | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | string | 是   |
| localfile        | 设置响应头部 Content-Type                                    | string | 是   |
| ResponseContentType        | 设置响应头部 Content-Type                                    | string | 否   |
| ResponseContentLanguage    | 设置响应头部 Content-Language                                | string | 否   |
| ResponseExpires            | 设置响应头部 Content-Expires                                 | string | 否   |
| ResponseCacheControl       | 设置响应头部 Cache-Control                                   | string | 否   |
| ResponseContentDisposition | 设置响应头部 Content-Disposition                             | string | 否   |
| ResponseContentEncoding    | 设置响应头部 Content-Encoding                                | string | 否   |
| Range                      | 设置下载文件的范围，格式为 bytes=first-last                  | string | 否   |
| IfModifiedSince            | 在指定时间后被修改才返回                                     | string | 否   |

#### 返回结果说明

```go
{
    'Body': '',
    'Accept-Ranges': 'bytes',
    'Content-Type': 'application/octet-stream',
    'Content-Length': '16807',
    'Content-Disposition': 'attachment; filename="filename.jpg"',
    'Content-Range': 'bytes 0-16086/16087',
    'ETag': '"9a4802d5c99dafe1c04da0a8e7e166bf"',
    'Last-Modified': 'Wed, 28 Oct 2014 20:30:00 GMT',
    'X-Cos-Request-Id': 'NTg3NzQ3ZmVfYmRjMzVfMzE5N182NzczMQ=='
}
```

| 参数名称   | 参数描述                                                     | 类型       |
| ---------- | ------------------------------------------------------------ | ---------- |
| Body       | 下载文件的内容                                               | StreamBody |
| 文件元信息 | 下载文件的元信息，包括 Etag 和 X-Cos-Request-Id 等信息，也会返回设置的文件元信息 | string     |

### 删除单个对象

#### 功能说明

删除 Bucket 中对应文件。

#### 方法原型

```go
func (s *ObjectService) Delete(ctx context.Context, key string) (*Response, error)
```

#### 请求示例

```go
key := "test/objectPut.go"
resp, err := client.Object.Delete(context.Background(), name)
```

#### 参数说明

| 参数名称 | 参数描述                                                     | 类型   | 必填 |
| -------- | ------------------------------------------------------------ | ------ | ---- |
| key      | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | string | 是   |

### 删除多个对象

#### 功能说明

将指定 Bucket 中的文件批量删除。

#### 方法原型

```go
func (s *ObjectService) DeleteMulti(ctx context.Context, opt *ObjectDeleteMultiOptions) (*ObjectDeleteMultiResult, *Response, error)
```

#### 请求示例

```go
var keys = []string{"a","b","c"}
obs := []cos.Object{}
for _, v := range keys {
    obs = append(obs, cos.Object{Key: v})
}
opt := &cos.ObjectDeleteMultiOptions{
    Objects: obs,
    Quiet: true,
}
v, resp, err := client.Object.DeleteMulti(ctx, opt)
```

#### 参数说明

```go
type ObjectDeleteMultiOptions struct {
	Quiet   bool     
	Objects []Object 
}
type Object struct {
	Key		string 
}
```

| 参数名称 | 参数描述                                                     | 类型   | 必填 |
| -------- | ------------------------------------------------------------ | ------ | ---- |
| Objects  | 说明每个将要删除的目标 Object 信息                           | List   | 是   |
| Key      | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | string | 否   |
| Quiet    | 指明删除的返回结果方式，可选值为 true，false，默认为 false。设置为 true 只返回失败的错误信息，设置为false时返回成功和失败的所有信息 | bool   | 否   |

#### 返回结果说明

```go
type ObjectDeleteMultiResult struct {
	DeletedObjects []Object
	Errors         []struct {
		Key     string
		Code    string
		Message string
	}
}
type Object struct {
	Key		string 
}
```

| 参数名称       | 参数描述                         | 类型     |
| -------------- | -------------------------------- | -------- |
| DeletedObjects | 删除成功的 Object 信息           | []struct |
| Errors         | 删除失败的 Object 信息           | string   |
| Key            | 删除失败的 Object 的路径         | string   |
| Code           | 删除失败的 Object 对应的错误码   | string   |
| Message        | 删除失败的 Object 对应的错误信息 | string   |

### 获取对象元数据

#### 功能说明

获取指定文件的元信息。

#### 方法原型

```go
func (s *ObjectService) Head(ctx context.Context, key string, opt *ObjectHeadOptions) (*Response, error)
```

#### 请求示例

```go
key := "test/hello.txt"
resp, err := client.Object.Head(context.Background(), key, nil)
```

#### 参数说明

```go
type ObjectHeadOptions struct {
	IfModifiedSince string 
}
```

| 参数名称        | 参数描述                                                     | 类型   | 必填 |
| --------------- | ------------------------------------------------------------ | ------ | ---- |
| key             | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | string | 是   |
| IfModifiedSince | 在指定时间后被修改才返回                                     | string | 否   |

#### 返回结果说明

```go
{
    'Content-Type': 'application/octet-stream',
    'Content-Length': '16807',
    'ETag': '"9a4802d5c99dafe1c04da0a8e7e166bf"',
    'Last-Modified': 'Wed, 28 Oct 2014 20:30:00 GMT',
    'X-Cos-Request-Id': 'NTg3NzQ3ZmVfYmRjMzVfMzE5N182NzczMQ=='
}
```

| 参数名称   | 参数描述                                                     | 类型   |
| ---------- | ------------------------------------------------------------ | ------ |
| 文件元信息 | 获取文件的元信息，包括 Etag 和 X-Cos-Request-Id 等信息，也会包含设置的文件元信息 | string |

### 初始化分块上传

#### 功能说明

创建一个新的分块上传任务，返回 UploadId。

#### 方法原型

```go
func (s *ObjectService) InitiateMultipartUpload(ctx context.Context, name string, opt *InitiateMultipartUploadOptions) (*InitiateMultipartUploadResult, *Response, error)
```

#### 请求示例

```go
name := "test_multipart"
//可选opt
v, resp, err := client.Object.InitiateMultipartUpload(context.Background(), name, nil）
```

#### 参数说明

```go
type InitiateMultipartUploadOptions struct {
	*ACLHeaderOptions       
	*ObjectPutHeaderOptions 
}
type ACLHeaderOptions struct {
	XCosACL              string                           
	XCosGrantRead        string
	XCosGrantWrite       string 
	XCosGrantFullControl string                                           
} 
type ObjectPutHeaderOptions struct {
	CacheControl       string 
	ContentDisposition string 
	ContentEncoding    string 
	ContentType        string 
	ContentLength      int   
	Expires            string 
	// 自定义的 x-cos-meta-* header
	XCosMetaXXX        *http.Header 
	XCosStorageClass   string      
}
```

| 参数名称             | 参数描述                                                     | 类型        | 必填 |
| -------------------- | ------------------------------------------------------------ | ----------- | ---- |
| r                    | 上传文件的内容，可以为文件流或字节流，当 r 不是 bytes.Buffer/bytes.Reader/strings.Reader 时，必须指定 opt.ObjectPutHeaderOptions.ContentLength | io.Reader   | 是   |
| key                  | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | string      | 是   |
| XCosACL              | 设置文件的ACL，如 private，public-read，public-read-write    | string      | 否   |
| XCosGrantFullControl | 赋予指定账户对文件的读写权限。格式为`id=" ",id=" "`当需要给子账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`当需要给根账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`例如`id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"` | string      | 否   |
| XCosGrantRead        | 赋予指定账户对文件的读权限。格式为`id=" ",id=" "`当需要给子账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`当需要给根账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`例如`id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"` | string      | 否   |
| XCosGrantWrite       | 赋予指定账户对文件的写权限。格式为`id=" ",id=" "`当需要给子账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`当需要给根账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`例如`id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"` | string      | 否   |
| XCosStorageClass     | 设置文件的存储类型，STANDARD、STANDARD_IA、ARCHIVE，默认值：STANDARD   | string      | 否   |
| Expires              | 设置 Content-Expires                                         | string      | 否   |
| CacheControl         | 缓存策略，设置 Cache-Control                                 | string      | 否   |
| ContentType          | 内容类型，设置 Content-Type                                  | string      | 否   |
| ContentDisposition   | 文件名称，设置 Content-Disposition                           | string      | 否   |
| ContentEncoding      | 编码格式，设置 Content-Encoding                              | string      | 否   |
| ContentLength        | 设置传输长度                                                 | string      | 否   |
| XCosMetaXXX          | 用户自定义的文件元信息， 必须以 x-cos-meta 开头，否则会被忽略 | http.Header | 否   |

#### 返回结果说明

```go
type InitiateMultipartUploadResult struct {
	Bucket   string
	Key      string
	UploadID string                   
} 
```

| 参数名称 | 参数描述                                                     | 类型   |
| -------- | ------------------------------------------------------------ | ------ |
| UploadId | 标识分块上传的 ID                                            | string |
| Bucket   | Bucket 名称，由 bucket-appid 组成                            | string |
| Key      | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | string |

### 终止分块上传

#### 功能说明

放弃一个分块上传任务，删除所有已上传的分块。

#### 方法原型

```go
func (s *ObjectService) AbortMultipartUpload(ctx context.Context, key, uploadID string) (*Response, error)
```

#### 请求示例

```go
key := "test_multipart.txt"
v, _, err := client.Object.InitiateMultipartUpload(context.Background(), key, nil)
// Abort
resp, err := client.Object.AbortMultipartUpload(context.Background(), key, v.UploadID)
```

#### 参数说明

| 参数名称 | 参数描述                                                     | 类型   | 必填 |
| -------- | ------------------------------------------------------------ | ------ | ---- |
| key      | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | string | 是   |
| UploadId | 标识分块上传的 ID                                            | string | 是   |

### 上传分块

#### 功能说明

上传一个分块到指定的 UploadId 中，单个大小不得超过5GB。

#### 方法原型

```go
func (s *ObjectService) UploadPart(ctx context.Context, key, uploadID string, partNumber int, r io.Reader, opt *ObjectUploadPartOptions) (*Response, error)
```

#### 请求示例

```go
// 注意，上传分块的块数最多10000块
key := "test/test_multi_upload.go"
f := strings.NewReader("test heoo")
// opt可选
_, err := client.Object.UploadPart(
    context.Background(), key, uploadID, 1, f, nil,
)
```

#### 参数说明

```go
type ObjectUploadPartOptions struct {
    ContentLength   int                                      
}
```

| 参数名称      | 参数描述                                                     | 类型      | 必填 |
| ------------- | ------------------------------------------------------------ | --------- | ---- |
| key           | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | string    | 是   |
| UploadId      | 标识分块上传的 ID，由 InitiateMultipartUpload 生成             | string    | 是   |
| PartNumber    | 标识上传分块的序号                                           | int       | 是   |
| r             | 上传分块的内容，可以为本地文件流或输入流。当 r 不是 bytes.Buffer/bytes.Reader/strings.Reader 时，必须指定 opt.ContentLength | io.Reader | 是   |
| ContentLength | 设置传输长度                                                 | int       | 否   |

#### 返回结果说明

```go
{
    'ETag': 'string'
}
```

| 参数名称 | 参数描述            | 类型   |
| -------- | ------------------- | ------ |
| ETag     | 上传分块的 MD5 值 | string |

### 列出分块 

#### 功能说明

列出指定 UploadId 中已经上传的分块的信息。

#### 方法原型

```go
func (s *ObjectService) ListParts(ctx context.Context, name, uploadID string) (*ObjectListPartsResult, *Response, error)
```

#### 请求示例

```go
key := "test/test_list_parts.go"
v, resp, err := client.Object.ListParts(context.Background(), key, uploadID) 
```

#### 参数说明

| 参数名称 | 参数描述                                                     | 类型   | 必填 |
| -------- | ------------------------------------------------------------ | ------ | ---- |
| key      | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | string | 是   |
| UploadId | 标识分块上传的 ID，由 InitiateMultipartUpload 生成             | string | 是   |

#### 返回结果说明

```go
type ObjectListPartsResult struct {
	Bucket               string
	EncodingType         string 
	Key                  string
	UploadID             string     
	Initiator            *Initiator 
	Owner                *Owner     
	StorageClass         string
	PartNumberMarker     int
	NextPartNumberMarker int 
	MaxParts             int
	IsTruncated          bool
	Parts                []Object 
}
type Initiator struct {
	UIN         string
	ID          string 
	DisplayName string                                
}
type Owner struct {
	UIN         string
	ID          string 
	DisplayName string                                
}
type Object struct {
	Key          string 
	ETag         string 
	Size         int    
	PartNumber   int    
	LastModified string 
	StorageClass string 
	Owner        *Owner
}
```

| 参数名称             | 参数描述                                                     | 类型   |
| -------------------- | ------------------------------------------------------------ | ------ |
| Bucket               | Bucket 名称，由 bucketname-appid 构成                        | string |
| EncodingType         | 默认不编码，规定返回值的编码方式，可选值：url                | string |
| Key                  | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | string |
| UploadId             | 标识分块上传的 ID，由 InitiateMultipartUpload 生成             | string |
| Initiator            | 分块上传的创建者，包括 DisplayName，UIN 和 ID                | struct |
| Owner                | 文件拥有者的信息，包括 DisplayName ，UIN和 ID                | struct |
| StorageClass         | 文件的存储类型，STANDARD、STANDARD_IA、ARCHIVE，默认值：STANDARD       | string |
| PartNumberMarker     | 默认为0，从第一块列出分块，从 PartNumberMarker 下一个分块开始列出 | int    |
| NextPartNumberMarker | 指明下一次列出分块的起始位置                                 | int    |
| MaxParts             | 最多返回的分块的数量，默认为最大的1000                       | int    |
| IsTruncated          | 表示返回的分块是否被截断                                     | bool   |
| Part                 | 上传分块的相关信息，包括 ETag，PartNumber，Size，LastModified | struct |

### 完成分块上传

#### 功能说明

组装指定 UploadId 中所有的分块为一个完整的文件，文件最终大小必须大于1MB，否则会返回错误。

#### 方法原型

```go
func (s *ObjectService) CompleteMultipartUpload(ctx context.Context, key, uploadID string, opt *CompleteMultipartUploadOptions) (*CompleteMultipartUploadResult, *Response, error)
```

#### 请求示例

```go
// 封装 UploadPart 接口返回 etag 信息
func uploadPart(c *cos.Client, name string, uploadID string, blockSize, n int) string {
	b := make([]byte, blockSize)
	if _, err := rand.Read(b); err != nil {
		panic(err)
	}
	s := fmt.Sprintf("%X", b)
	f := strings.NewReader(s)

	// 当传入参数f不是 bytes.Buffer/bytes.Reader/strings.Reader 时，必须指定 opt.ContentLength
	//opt := &cos.ObjectUploadPartOptions{
	//	ContentLength: size,
	//}

	resp, err := c.Object.UploadPart(
		context.Background(), name, uploadID, n, f, nil,
	)
	if err != nil {
		panic(err)
	}
	return resp.Header.Get("Etag")
}

// Init, UploadPart and Complete process
key := "test/test_complete_upload.go"
v, resp, err := client.Object.InitiateMultipartUpload(context.Background(), key, nil)
uploadID := v.UploadID
blockSize := 1024 * 1024 * 3

opt := &cos.CompleteMultipartUploadOptions{}
for i := 1; i < 5; i++ {
	// 调用上面封装的接口获取 etag 信息
	etag := uploadPart(c, key, uploadID, blockSize, i)
	opt.Parts = append(opt.Parts, cos.Object{
		PartNumber: i, ETag: etag},
	)
}

v, resp, err = client.Object.CompleteMultipartUpload(
	context.Background(), key, uploadID, opt,
)
```

#### 参数说明

```go
type CompleteMultipartUploadOptions struct {
	Parts   []Object 
}
type Object struct { 
	ETag         string 
	PartNumber   int     
}
```


| 参数名称                       | 参数描述                                                     | 类型   | 必填 |
| ------------------------------ | ------------------------------------------------------------ | ------ | ---- |
| key                            | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | string | 是   |
| UploadId                       | 标识分块上传的 ID，由 InitiateMultipartUpload 生成             | string | 是   |
| CompleteMultipartUploadOptions | 所有分块的 ETag 和 PartNumber 信息                           | struct | 是   |

#### 返回结果说明

```go
type CompleteMultipartUploadResult struct {
	Location string
	Bucket   string
	Key      string
	ETag     string
}
```

| 参数名称 | 参数描述                                                     | 类型   |
| -------- | ------------------------------------------------------------ | ------ |
| Location | URL 地址                                                     | string |
| Bucket   | Bucket 名称，由 bucketname-appid 构成                        | string |
| Key      | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | string |
| ETag     | 合并后对象的唯一标签值，该值不是对象内容的 MD5 校验值，仅能用于检查对象唯一性。如需校验文件内容，可以在上传过程中校验单个分块的 ETag 值 | string |

### 设置对象 ACL

#### 功能说明

设置文件的 ACL 信息，通过 XCosACL，XCosGrantFullControl，XCosGrantRead，XCosGrantWrite传入 header 的方式来设置 ACL，或者通过 ACLXML 传入 body 来设置 ACL，两种方式只能选择一种，否则会返回冲突。

> !当前访问策略条目限制为1000条，如果您不需要进行对象 ACL 控制，请不要设置，默认继承 Bucket 权限。

#### 方法原型

```go
func (s *ObjectService) PutACL(ctx context.Context, key string, opt *ObjectPutACLOptions) (*Response, error)
```

#### 请求示例

通过 Header 设置 Object ACL

```go
opt := &cos.ObjectPutACLOptions{
    Header: &cos.ACLHeaderOptions{
        XCosACL: "private",
    },
}
key := "test/hello.txt"
resp, err := client.Object.PutACL(context.Background(), key, opt)
```

通过 Body 设置 Object ACL

```go
opt = &cos.ObjectPutACLOptions{
    Body: &cos.ACLXml{
        Owner: &cos.Owner{
            ID: "qcs::cam::uin/100000760461:uin/100000760461",
        },
        AccessControlList: []cos.ACLGrant{
            {
                Grantee: &cos.ACLGrantee{
                    Type: "RootAccount",
                    ID:   "qcs::cam::uin/100000760461:uin/100000760461",
                },

                Permission: "FULL_CONTROL",
            },
        },
    },
}

resp, err = client.Object.PutACL(context.Background(), key, opt)
```

#### 参数说明

```go
type ACLHeaderOptions struct {
	XCosACL              string 
	XCosGrantRead        string 
	XCosGrantWrite       string 
	XCosGrantFullControl string 
}
```

| 参数名称             | 参数描述                                                     | 类型   | 必填 |
| -------------------- | ------------------------------------------------------------ | ------ | ---- |
| key                  | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | string | 是   |
| XCosACL              | 设置 Bucket 的 ACL，如 private，public-read，public-read-write | string | 否   |
| XCosGrantFullControl | 赋予指定账户对 Bucket 的读写权限。格式为`id=" ",id=" "`当需要给子账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`当需要给根账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`例如`id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"` | string | 否   |
| XCosGrantRead        | 赋予指定账户对 Bucket 的读权限。格式为`id=" ",id=" "`当需要给子账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`当需要给根账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`例如`id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"` | string | 否   |
| XCosGrantWrite       | 赋予指定账户对 Bucket 的写权限。格式为`id=" ",id=" "`当需要给子账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`当需要给根账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`例如`id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"` | string | 否   |
| ACLXML               | 赋予指定账户对 Bucket 的访问权限，具体格式见 get object acl 返回结果说明 | struct | 否   |

### 恢复归档文件

#### 功能说明

对一个通过 COS 归档为 archive 类型的对象进行恢复。

#### 方法原型

```go
func (s *ObjectService) PutRestore(ctx context.Context, key string, opt *ObjectRestoreOptions) (*Response, error) 
```

#### 请求示例

```go
opt := &cos.ObjectRestoreOptions{
	Days: 2,
	Tier: &cos.CASJobParameters{
    		// Standard, Exepdited and Bulk
    		Tier: "Expedited",
	},
}
key := "archivetest"
resp, err := c.Object.PutRestore(context.Background(), key, opt)
```

#### 参数说明

```go
type ObjectRestoreOptions struct {        
    Days    int               
    Tier    *CASJobParameters 
}
type CASJobParameters struct {
    Tier    string 
}
```

| 参数名称             | 参数描述                                                     | 类型   | 必填 |
| -------------------- | ------------------------------------------------------------ | ------ | ---- |
| key                  | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | string | 是   |
| ObjectRestoreOptions               | 描述取回的临时文件的规则 | struct | 是   |
| Days               | 描述临时文件的过期时间	 | int | 是   |
| CASJobParameters               | 描述恢复类型的配置信息 | struct | 否   |
| Tier               | 描述取回临时文件的模式，可选值为'Expedited'，Standard'，'Bulk'，分别对应快速、标准以及慢这三种模式 | string | 否   |


### 获取对象 ACL

#### 功能说明

获取指定文件的 ACL 信息。

#### 方法原型

```go
func (s *ObjectService) GetACL(ctx context.Context, key string) (*ObjectGetACLResult, *Response, error)
```

#### 请求示例

```go
key := "test/hello.txt"
v, resp, err := client.Object.GetACL(context.Background(), key)
```

#### 参数说明

| 参数名称 | 参数描述                                                     | 类型   | 必填 |
| -------- | ------------------------------------------------------------ | ------ | ---- |
| key      | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | string | 是   |

#### 返回结果说明

```go
type ACLXml struct {
	Owner             *Owner
	AccessControlList []ACLGrant 
}
type Owner struct { 
	ID          string 
	DisplayName string
}
type ACLGrant struct {
	Grantee    *ACLGrantee
	Permission string
}
type ACLGrantee struct {
	Type        string 
	ID          string 
	DisplayName string
    UIN         string 
}
```

| 参数名称          | 参数描述                                                     | 类型   |
| ----------------- | ------------------------------------------------------------ | ------ |
| Owner             | Bucket 拥有者的信息，包括 DisplayName 和 ID                  | struct |
| AccessControlList | Bucket 权限授予者的信息，包括 Grantee和 Permission           | struct |
| Grantee           | 权限授予者的信息，包括 DisplayName，Type，ID 和 UIN          | struct |
| Type              | 权限授予者的类型，类型为 CanonicalUser 或者 Group            | string |
| ID                | Type 为 CanonicalUser 时，对应权限授予者的 ID                | string |
| DisplayName       | 权限授予者的名字                                             | string |
| UIN               | Type 为 Group 时，对应权限授予者的 UIN                       | string |
| Permission        | 授予者所拥有的 Bucket 的权限，可选值有 FULL_CONTROL，WRITE，READ，分别对应读写权限、写权限、读权限 | string |

### 设置对象复制

#### 功能说明

将一个文件从源路径复制到目标路径。建议文件大小1M 到5G，超过5G 的文件请使用分块上传 Upload - Copy。在拷贝的过程中，文件元属性和 ACL 可以被修改。用户可以通过该接口实现文件移动，文件重命名，修改文件属性和创建副本。
>!在跨帐号复制的时候，需要先设置被复制文件的权限为公有读，或者对目标帐号赋权，同帐号则不需要。

#### 方法原型

```go
func (s *ObjectService) Copy(ctx context.Context, key, sourceURL string, opt *ObjectCopyOptions) (*ObjectCopyResult, *Response, error)
```

#### 请求示例

```go
u, _ := url.Parse("http://test-1253846586.cos.ap-guangzhou.myqcloud.com")
source := "test/objectMove_src"
soruceURL := fmt.Sprintf("%s/%s", u.Host, source)
dest := "test/objectMove_dest"
//opt := &cos.ObjectCopyOptions{}
r, resp, err := client.Object.Copy(context.Background(), dest, soruceURL, nil)
```

#### 参数说明

```go
type ObjectCopyOptions struct {
	*ObjectCopyHeaderOptions 
	*ACLHeaderOptions        
}
type ACLHeaderOptions struct {
	XCosACL              string 
	XCosGrantRead        string 
	XCosGrantWrite       string 
	XCosGrantFullControl string 
}
type ObjectCopyHeaderOptions struct {
	XCosMetadataDirective           string 
	XCosCopySourceIfModifiedSince   string 
	XCosCopySourceIfUnmodifiedSince string 
	XCosCopySourceIfMatch           string 
	XCosCopySourceIfNoneMatch       string 
	XCosStorageClass                string 
	// 自定义的 x-cos-meta-* header
	XCosMetaXXX    				    *http.Header 
	XCosCopySource 					string      
}
```

| 参数名称                        | 参数描述                                                     | 类型        | 必填 |
| ------------------------------- | ------------------------------------------------------------ | ----------- | ---- |
| key                             | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | string      | 是   |
| sourceURL                       | 描述拷贝源文件的 URL                                          | string      | 是   |
| XCosACL                         | 设置文件的 ACL，如 private，public-read，public-read-write    | string      | 否   |
| XCosGrantFullControl            | 赋予指定账户对文件的读写权限。格式为：id=" ",id=" "。当需要给子账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`当需要给根账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`例如`id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"` | string      | 否   |
| XCosGrantRead                   | 赋予指定账户对文件的读权限。格式为`id=" ",id=" "`当需要给子账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`当需要给根账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`例如`id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"` | string      | 否   |
| XCosGrantWrite                  | 赋予指定账户对文件的写权限。格式为`id=" ",id=" "`当需要给子账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`当需要给根账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`例如`id="qcs::cam::uin/123:uin/456",id="qcs::cam::uin/123:uin/123"` | string      | 否   |
| XCosMetadataDirective           | 可选值为 Copy,Replaced，设置为 Copy 时，忽略设置的用户元数据信息直接复制，设置为 Replaced 时，按设置的元信息修改元数据，当目标路径和源路径一样时，必须设置为Replaced | string      | 是   |
| XCosCopySourceIfModifiedSince   | 当 Object 在指定时间后被修改，则执行操作，否则返回412。可与 XCosCopySourceIfNoneMatch 一起使用，与其他条件联合使用返回冲突 | string      | 否   |
| XCosCopySourceIfUnmodifiedSince | 当 Object 在指定时间后未被修改，则执行操作，否则返回412。可与 XCosCopySourceIfMatch 一起使用，与其他条件联合使用返回冲突 | string      | 否   |
| XCosCopySourceIfMatch           | 当 Object 的 Etag 和给定一致时，则执行操作，否则返回412。可与 XCosCopySourceIfUnmodifiedSince 一起使用，与其他条件联合使用返回冲突 | string      | 否   |
| XCosCopySourceIfNoneMatch       | 当 Object 的 Etag 和给定不一致时，则执行操作，否则返回412。可与 XCosCopySourceIfModifiedSince 一起使用，与其他条件联合使用返回冲突 | string      | 否   |
| XCosStorageClass                | 设置文件的存储类型，STANDARD、STANDARD_IA，默认值：STANDARD   | string      | 否   |
| XCosMetaXXX                     | 用户自定义的文件元信息                                       | http.Header | 否   |
| XCosCopySource                  | 源文件 URL 路径，可以通过 versionid 子资源指定历史版本       | string      | 否   |

#### 返回结果说明

上传文件的属性：

```go
type ObjectCopyResult struct {
    ETag         string 
    LastModified string
}
```

| 参数名称     | 参数描述                   | 类型   |
| ------------ | -------------------------- | ------ |
| ETag         | 拷贝文件的 MD5 值          | string |
| LastModified | 拷贝文件的最后一次修改时间 | string |

## 异常说明

API 返回的 Response 为 Golang http 标准库 [Response](https://golang.org/pkg/net/http/#Response)  类型。
可通过 err.Error() 获取错误提示，服务端返回的具体信息，获取错误码的更多信息请参考：[COS 错误码](https://cloud.tencent.com/document/product/436/7730)。
