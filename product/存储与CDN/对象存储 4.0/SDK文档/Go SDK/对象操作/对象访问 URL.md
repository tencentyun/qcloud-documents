## 简介

本文档提供获取对象访问 URL 的代码示例。

## 获取对象访问 URL

#### 功能说明

获取对象访问 URL 用于匿名下载或分发。

>! COS Go SDK 版本需要大于等于 v0.7.26。

#### 方法原型

```
func (s *ObjectService) GetObjectURL(key string) *url.URL
```

#### 请求示例


[//]: # (.cssg-snippet-get-object-url-alias)
```go
package main

import (
    "fmt"
    "github.com/tencentyun/cos-go-sdk-v5"
    "net/http"
    "net/url"
    "os"
)

func main() {
    // 存储桶名称，由 bucketname-appid 组成，appid 必须填入，可以在 COS 控制台查看存储桶名称。 https://console.cloud.tencent.com/cos5/bucket
    // 替换为用户的 region，存储桶 region 可以在 COS 控制台“存储桶概览”查看 https://console.cloud.tencent.com/ ，关于地域的详情见 https://cloud.tencent.com/document/product/436/6224 。
    u, _ := url.Parse("https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com")
    b := &cos.BaseURL{BucketURL: u}
    client := cos.NewClient(b, &http.Client{
        Transport: &cos.AuthorizationTransport{
            // 通过环境变量获取密钥
            // 环境变量 SECRETID 表示用户的 SecretId，登录访问管理控制台查看密钥，https://console.cloud.tencent.com/cam/capi
            SecretID: os.Getenv("SECRETID"),  // 用户的 SecretId，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140
            // 环境变量 SECRETKEY 表示用户的 SecretKey，登录访问管理控制台查看密钥，https://console.cloud.tencent.com/cam/capi
            SecretKey: os.Getenv("SECRETKEY"),  // 用户的 SecretKey，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140
        },
    })
    key := "exampleobject"
    ourl := client.Object.GetObjectURL(key)
    fmt.Println(ourl)
}
```

#### 参数说明

| 参数名称   | 参数描述   |类型 | 是否必填 |
| -------------- | -------------- |---------- | ----------- |
| Key  | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 `examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/doc/pic.jpg` 中，对象键为 doc/pic.jpg | String | 是 |

#### 返回结果说明

该方法返回值为对象访问的 URL。
