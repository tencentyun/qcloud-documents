
## 简介

本文档提供关于存储桶的基本操作和访问控制列表（ACL）的相关 API 概览以及 SDK 示例代码。

**基本操作**

| API                                                          | 操作名             | 操作描述                           |
| ------------------------------------------------------------ | ------------------ | ---------------------------------- |
| [GET Service](https://cloud.tencent.com/document/product/436/8291) | 查询存储桶列表     | 查询指定账号下所有的存储桶列表    |
| [PUT Bucket](https://cloud.tencent.com/document/product/436/7738) | 创建存储桶         | 在指定账号下创建一个存储桶   |
| [HEAD Bucket](https://cloud.tencent.com/document/product/436/7735) | 检索存储桶及其权限 | 检索存储桶是否存在且是否有权限访问 |
| [DELETE Bucket](https://cloud.tencent.com/document/product/436/7732) | 删除存储桶         | 删除指定账号下的空存储桶           |

**访问控制列表**

| API                                                          | 操作名         | 操作描述              |
| ------------------------------------------------------------ | -------------- | --------------------- |
| [PUT Bucket acl](https://cloud.tencent.com/document/product/436/7737) | 设置存储桶 ACL | 设置存储桶的 ACL 配置 |
| [GET Bucket acl](https://cloud.tencent.com/document/product/436/7733) | 查询存储桶 ACL | 查询存储桶的 ACL 配置 |

## 基本操作

### 查询存储桶列表

#### 功能说明

查询指定账号下所有的存储桶列表。

#### 方法原型

```go
func (s *ServiceService) Get(ctx context.Context) (*ServiceGetResult, *Response, error)
```

#### 请求示例

```go
s, resp, err := c.Service.Get(context.Background()) 
```

#### 返回结果说明
通过 GetServiceResult 返回请求结果。
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

### 创建存储桶

#### 功能说明

在指定账号下创建一个存储桶。

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
| XCosGrantFullControl | 赋予指定账户对 Bucket 的读写权限。格式为`id=" ",id=" "`。当需要给子账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`，当需要给主账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`。例如`id="qcs::cam::uin/100000000001:uin/100000000011",id="qcs::cam::uin/100000000001:uin/100000000001"` | string | 否   |
| XCosGrantRead        | 赋予指定账户对 Bucket 的读权限。格式为`id=" ",id=" "`。当需要给子账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`，当需要给主账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`。例如`id="qcs::cam::uin/100000000001:uin/100000000011",id="qcs::cam::uin/100000000001:uin/100000000001"` | string | 否   |
| XCosGrantWrite       | 赋予指定账户对 Bucket 的写权限。格式为`id=" ",id=" "`。当需要给子账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`，当需要给主账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`。例如`id="qcs::cam::uin/100000000001:uin/100000000011",id="qcs::cam::uin/100000000001:uin/100000000001"` | string | 否   |

### 检索存储桶及其权限

#### 功能说明

检索存储桶是否存在且是否有权限访问。

#### 方法原型

```go
func (s *BucketService) Head(ctx context.Context) (*Response, error)
```

#### 请求示例

```go
resp, err := client.Bucket.Head(context.Background())
```


### 删除存储桶

#### 功能说明

删除指定账号下的空存储桶。

#### 方法原型

```go
func (s *BucketService) Delete(ctx context.Context) (*Response, error)
```

#### 请求示例

```go
resp, err := client.Bucket.Delete(context.Background())
```

## 访问控制列表

### 设置存储桶 ACL

#### 功能说明

设置指定存储桶访问权限控制列表（PUT Bucket acl）。

#### 方法原型

```go
func (s *BucketService) PutACL(ctx context.Context, opt *BucketPutACLOptions) (*Response, error)
```

#### 请求示例

```go
// 1. Set Bucket ACL by header.
opt := &cos.BucketPutACLOptions{
	Header: &cos.ACLHeaderOptions{
		//private，public-read，public-read-write
		XCosACL: "private",
	},
}
resp, err := client.Bucket.PutACL(context.Background(), opt)

// 2. Set Bucket ACL by body.
opt := &cos.BucketPutACLOptions{
    Body: &cos.ACLXml{
        Owner: &cos.Owner{
            ID: "qcs::cam::uin/100000760461:uin/100000760461",
        },
        AccessControlList: []cos.ACLGrant{
            {
                Grantee: &cos.ACLGrantee{
		    // Type can also chose the "Group", "CanonicalUser"
                    Type: "RootAccount",
                    ID:"qcs::cam::uin/100000760461:uin/100000760461",
                },
		// Permission can also chose the "WRITE"，"FULL_CONTROL" 
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
| XCosGrantFullControl | 赋予指定账户对 Bucket 的读写权限。格式为`id=" ",id=" "`。当需要给子账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`，当需要给主账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`。例如`id="qcs::cam::uin/100000000001:uin/100000000011",id="qcs::cam::uin/100000000001:uin/100000000001"` | string | 否   |
| XCosGrantRead        | 赋予指定账户对 Bucket 的读权限。格式为`id=" ",id=" "`。当需要给子账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`，当需要给主账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`。例如`id="qcs::cam::uin/100000000001:uin/100000000011",id="qcs::cam::uin/100000000001:uin/100000000001"` | string | 否   |
| XCosGrantWrite       | 赋予指定账户对 Bucket 的写权限。格式为`id=" ",id=" "`。当需要给子账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{SubUin}"`，当需要给主账户授权时，格式为`id="qcs::cam::uin/{OwnerUin}:uin/{OwnerUin}"`。例如`id="qcs::cam::uin/100000000001:uin/100000000011",id="qcs::cam::uin/100000000001:uin/100000000001"` | string | 否   |
| ACLXML               | 赋予指定账户对 Bucket 的访问权限，具体格式见 GET Bucket acl 返回结果说明 | struct | 否   |

### 查询存储桶 ACL

#### 功能说明

查询指定存储桶的访问权限控制列表（GET Bucket acl）。

#### 方法原型

```go
func (s *BucketService) GetACL(ctx context.Context) (*BucketGetACLResult, *Response, error)
```

#### 请求示例

```go
v, resp, err := client.Bucket.GetACL(context.Background())
```

#### 返回结果说明

通过 GetBucketACLResult 返回请求结果。

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
