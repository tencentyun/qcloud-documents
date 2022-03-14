

## 简介

本文档提供关于自定义域名的 API 概览以及 SDK 示例代码。

| API               | 操作名         | 操作描述                   |
| ----------------- | -------------- | -------------------------- |
| PUT Bucket domain | 设置自定义域名 | 设置存储桶的自定义域名信息 |
| GET Bucket domain | 查询自定义域名 | 查询存储桶的自定义域名信息 |
| DELETE Bucket domain | 删除自定义域名 |删除存储桶的自定义域名信息|

## 设置自定义域名

#### 功能说明

PUT Bucket domain 用于为存储桶配置自定义域名。

#### 方法原型

```go
func (s *BucketService) PutDomain(ctx context.Context, opt *BucketPutDomainOptions) (*Response, error)
```

#### 请求示例

[//]: # (.cssg-snippet-put-bucket-domain)
```go
package main

import (
    "context"
    "fmt"
    "github.com/tencentyun/cos-go-sdk-v5"
    "net/http"
    "net/url"
    "os"
)

func main() {
    // 存储桶名称，由bucketname-appid 组成，appid必须填入，可以在COS控制台查看存储桶名称。 https://console.cloud.tencent.com/cos5/bucket
    // 替换为用户的 region，存储桶region可以在COS控制台“存储桶概览”查看 https://console.cloud.tencent.com/ ，关于地域的详情见 https://cloud.tencent.com/document/product/436/6224 。
    u, _ := url.Parse("https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com")
    b := &cos.BaseURL{BucketURL: u}
    client := cos.NewClient(b, &http.Client{
        Transport: &cos.AuthorizationTransport{
            // 通过环境变量获取密钥
            // 环境变量 SECRETID 表示用户的 SecretId，登录访问管理控制台查看密钥，https://console.cloud.tencent.com/cam/capi
            SecretID: os.Getenv("SECRETID"),
            // 环境变量 SECRETKEY 表示用户的 SecretKey，登录访问管理控制台查看密钥，https://console.cloud.tencent.com/cam/capi
            SecretKey: os.Getenv("SECRETKEY"),
        },
    })
    opt := &cos.BucketPutDomainOptions{
        Rules: []cos.BucketDomainRule{
            {
                Status:            "ENABLED",
                Name:              "www.example.com",
                Type:              "REST",
                ForcedReplacement: "CNAME",
            },
        },
    }
    _, err := client.Bucket.PutDomain(context.Background(), opt)
    if err != nil {
        fmt.Println(err)
    }
}
```

#### 参数说明

```go
type BucketDomainRule struct {
    Status            string
    Name              string
    Type              string
    ForcedReplacement string
}

type BucketPutDomainOptions struct {
    XMLName xml.Name
    Rules   []BucketDomainRule
}
```

| 参数名称               | 描述                                                         | 类型   |
| ---------------------- | ------------------------------------------------------------ | ------ |
| BucketPutDomainOptions | 自定义域名配置                                               | Struct |
| Rules                  | 域名配置规则                                                 | Array  |
| Status                 | 域名上线/下线状态，有效值 ENABLED/DISABLED                   | String |
| Name                   | 用户的自定义域名，有效值：字母、数字、点                     | String |
| Type                   | 绑定的源站类型，有效值 REST/WEBSITE                          | String |
| ForcedReplacement      | 替换已存在的配置，有效值 CNAME/TXT。填写则强制校验域名所有权后，再下发配置 | String |

#### 返回错误码说明

该请求可能会发生的一些常见的特殊错误如下：

| 状态码                                 | 说明                                                         |
| -------------------------------------- | ------------------------------------------------------------ |
| HTTP 409 Conflict                      | 该域名记录已存在，且请求中没有设置强制覆盖。或者该域名记录不存在，且请求中设置了强制覆盖 |
| HTTP 451 Unavailable For Legal Reasons | 该域名是中国境内域名，并且没有备案                           |

## 查询自定义域名

#### 功能说明

GET Bucket domain 用于查询存储桶的自定义域名信息。

#### 方法原型

```go
func (s *BucketService) GetDomain(ctx context.Context) (*BucketGetDomainResult, *Response, error)
```

#### 请求示例

[//]: # (.cssg-snippet-get-bucket-domain)
```go
package main

import (
    "context"
    "fmt"
    "github.com/tencentyun/cos-go-sdk-v5"
    "net/http"
    "net/url"
    "os"
)

func main() {
    // 存储桶名称，由bucketname-appid 组成，appid必须填入，可以在COS控制台查看存储桶名称。 https://console.cloud.tencent.com/cos5/bucket
    // 替换为用户的 region，存储桶region可以在COS控制台“存储桶概览”查看 https://console.cloud.tencent.com/ ，关于地域的详情见 https://cloud.tencent.com/document/product/436/6224 。
    u, _ := url.Parse("https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com")
    b := &cos.BaseURL{BucketURL: u}
    client := cos.NewClient(b, &http.Client{
        Transport: &cos.AuthorizationTransport{
            // 通过环境变量获取密钥
            // 环境变量 SECRETID 表示用户的 SecretId，登录访问管理控制台查看密钥，https://console.cloud.tencent.com/cam/capi
            SecretID: os.Getenv("SECRETID"),
            // 环境变量 SECRETKEY 表示用户的 SecretKey，登录访问管理控制台查看密钥，https://console.cloud.tencent.com/cam/capi
            SecretKey: os.Getenv("SECRETKEY"),
        },
    })
    v, _, err := client.Bucket.GetDomain(context.Background())
    if err != nil {
        fmt.Println(err)
    }
    fmt.Println(v)
}
```

#### 返回结果说明

```go
type BucketGetDomainResult BucketPutDomainOptions
```

| 参数名称              | 描述                                                         | 类型   |
| --------------------- | ------------------------------------------------------------ | ------ |
| BucketGetDomainResult | 自定义域名配置                                               | Struct |
| Rules                 | 域名配置规则                                                 | Array  |
| Status                | 域名上线/下线状态，有效值 ENABLED/DISABLED                   | String |
| Name                  | 用户的自定义域名，有效值：字母、数字、点                     | String |
| Type                  | 绑定的源站类型，有效值 REST/WEBSITE                          | String |
| ForcedReplacement     | 替换已存在的配置，有效值 CNAME/TXT。填写则强制校验域名所有权后，再下发配置 | String |

## 删除自定义域名

DELETE  Bucket domain 用于删除存储桶所有的自定义域名信息。

#### 方法原型

```go
func (s *BucketService) DeleteDomain(ctx context.Context) (*Response, error)
```

#### 请求示例

[//]: # (.cssg-snippet-delete-bucket-domain)
```go
package main

import (
    "context"
    "fmt"
    "github.com/tencentyun/cos-go-sdk-v5"
    "net/http"
    "net/url"
    "os"
)

func main() {
    // 存储桶名称，由bucketname-appid 组成，appid必须填入，可以在COS控制台查看存储桶名称。 https://console.cloud.tencent.com/cos5/bucket
    // 替换为用户的 region，存储桶region可以在COS控制台“存储桶概览”查看 https://console.cloud.tencent.com/ ，关于地域的详情见 https://cloud.tencent.com/document/product/436/6224 。
    u, _ := url.Parse("https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com")
    b := &cos.BaseURL{BucketURL: u}
    client := cos.NewClient(b, &http.Client{
        Transport: &cos.AuthorizationTransport{
            // 通过环境变量获取密钥
            // 环境变量 SECRETID 表示用户的 SecretId，登录访问管理控制台查看密钥，https://console.cloud.tencent.com/cam/capi
            SecretID: os.Getenv("SECRETID"),
            // 环境变量 SECRETKEY 表示用户的 SecretKey，登录访问管理控制台查看密钥，https://console.cloud.tencent.com/cam/capi
            SecretKey: os.Getenv("SECRETKEY"),
        },
    })
    _, err := client.Bucket.DeleteDomain(context.Background())
    if err != nil {
        fmt.Println(err)
    }
}
```
