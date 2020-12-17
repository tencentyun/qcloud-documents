## 下载与安装

#### 相关资源
- 对象存储 COS 的 XML Go SDK 源码下载地址：[ XML Go SDK](https://github.com/tencentyun/cos-go-sdk-v5)。
- 示例 Demo 下载地址：[ COS XML Go SDK 示例](https://github.com/tencentyun/cos-go-sdk-v5/tree/master/example)。
- 更多信息请参见 [COS Go SDK API](https://godoc.org/github.com/tencentyun/cos-go-sdk-v5) 文档。
- SDK 文档中的所有示例代码请参见 [SDK 代码示例](https://github.com/tencentyun/cos-snippets/tree/master/Go)。
- SDK 更新日志请参见 [ChangeLog](https://github.com/tencentyun/cos-go-sdk-v5/blob/master/CHANGELOG.md)。

#### 环境依赖
- Golang：用于下载和安装 Go 编译运行环境，请前往 Golang 官网进行下载。

#### 安装 SDK
执行以下命令安装 COS Go SDK：
```sh
go get -u github.com/tencentyun/cos-go-sdk-v5
```

## 开始使用
下面为您介绍如何使用 COS Go SDK 完成一个基础操作，如初始化客户端、创建存储桶、查询存储桶列表、上传对象、查询对象列表、下载对象和删除对象。

### 初始化
使用 COS 域名生成 COS GO 客户端 Client 结构。

#### 方法原型
```Go
func NewClient(uri *BaseURL, httpClient *http.Client) *Client
```

#### 请求示例
使用永久密钥：

[//]: # (.cssg-snippet-global-init)
```go
// 将 examplebucket-1250000000 和 COS_REGION修改为真实的信息
u, _ := url.Parse("https://examplebucket-1250000000.cos.COS_REGION.myqcloud.com")
b := &cos.BaseURL{BucketURL: u}
// 1.永久密钥
client := cos.NewClient(b, &http.Client{
    Transport: &cos.AuthorizationTransport{
        SecretID:  "COS_SECRETID",
        SecretKey: "COS_SECRETKEY",
    },
})
```

使用临时密钥：

[//]: # (.cssg-snippet-global-init-sts)
```go
// 将 examplebucket-1250000000 和 COS_REGION 修改为真实的信息
u, _ := url.Parse("https://examplebucket-1250000000.cos.COS_REGION.myqcloud.com")
b := &cos.BaseURL{BucketURL: u}
// 2.临时密钥
client := cos.NewClient(b, &http.Client{
    Transport: &cos.AuthorizationTransport{
        SecretID:     "COS_SECRETID",
        SecretKey:    "COS_SECRETKEY",
        SessionToken: "COS_SECRETTOKEN",
    },
})
if client != nil {
    // 调用 COS 请求
}
```

>?临时密钥生成和使用可参见 [临时密钥生成及使用指引](https://cloud.tencent.com/document/product/436/14048)。

### 创建存储桶

```Go
package main

import (
    "context"
    "net/http"
    "net/url"
    "os"

    "github.com/tencentyun/cos-go-sdk-v5"
)

func main() {
    // 将 examplebucket-1250000000 和 COS_REGION 修改为真实的信息
    u, _ := url.Parse("https://examplebucket-1250000000.cos.COS_REGION.myqcloud.com")
    b := &cos.BaseURL{BucketURL: u}
    c := cos.NewClient(b, &http.Client{
        Transport: &cos.AuthorizationTransport{
            SecretID:  "COS_SECRETID",
            SecretKey: "COS_SECRETKEY",
        },
    })

    _, err := c.Bucket.Put(context.Background(), nil)
    if err != nil {
        panic(err)
    }
}
```


### 查询存储桶列表
```go
package main

import (
    "context"
    "fmt"
    "net/http"
    "os"

    "github.com/tencentyun/cos-go-sdk-v5"
)

func main() {
    c := cos.NewClient(nil, &http.Client{
        Transport: &cos.AuthorizationTransport{
            SecretID:  "COS_SECRETID",
            SecretKey: "COS_SECRETKEY",
        },
    })

    s, _, err := c.Service.Get(context.Background())
    if err != nil {
        panic(err)
    }

    for _, b := range s.Buckets {
        fmt.Printf("%#v\n", b)
    }
}
```

### 上传对象
```Go
package main

import (
    "context"
    "net/http"
    "net/url"
    "os"
    "strings"

    "github.com/tencentyun/cos-go-sdk-v5"
)

func main() {
    // 将 examplebucket-1250000000 和 COS_REGION 修改为真实的信息
    u, _ := url.Parse("https://examplebucket-1250000000.cos.COS_REGION.myqcloud.com")
    b := &cos.BaseURL{BucketURL: u}
    c := cos.NewClient(b, &http.Client{
        Transport: &cos.AuthorizationTransport{
            SecretID:  "COS_SECRETID",
            SecretKey: "COS_SECRETKEY",
        },
    })
    // 对象键（Key）是对象在存储桶中的唯一标识。
    // 例如，在对象的访问域名 `examplebucket-1250000000.cos.COS_REGION.myqcloud.com/test/objectPut.go` 中，对象键为 test/objectPut.go
    name := "test/objectPut.go"
    // 1.通过字符串上传对象
    f := strings.NewReader("test")

    _, err := c.Object.Put(context.Background(), name, f, nil)
    if err != nil {
        panic(err)
    }
    // 2.通过本地文件上传对象
    _, err = c.Object.PutFromFile(context.Background(), name, "../test", nil)
    if err != nil {
        panic(err)
    }
}
```

### 查询对象列表
```go
package main

import (
    "context"
    "fmt"
    "net/http"
    "net/url"
    "os"

    "github.com/tencentyun/cos-go-sdk-v5"
)

func main() {
    // 将 examplebucket-1250000000 和 COS_REGION 修改为真实的信息
    u, _ := url.Parse("https://examplebucket-1250000000.cos.COS_REGION.myqcloud.com")
    b := &cos.BaseURL{BucketURL: u}
    c := cos.NewClient(b, &http.Client{
        Transport: &cos.AuthorizationTransport{
            SecretID:  "COS_SECRETID",
            SecretKey: "COS_SECRETKEY",
        },
    })

    opt := &cos.BucketGetOptions{
        Prefix:  "test",
        MaxKeys: 3,
    }
    v, _, err := c.Bucket.Get(context.Background(), opt)
    if err != nil {
        panic(err)
    }

    for _, c := range v.Contents {
        fmt.Printf("%s, %d\n", c.Key, c.Size)
    }
}
```

### 下载对象
```Go
package main

import (
    "context"
    "fmt"
    "io/ioutil"
    "net/http"
    "net/url"
    "os"

    "github.com/tencentyun/cos-go-sdk-v5"
)

func main() {
    // 将 examplebucket-1250000000 和 COS_REGION 修改为真实的信息
    u, _ := url.Parse("https://examplebucket-1250000000.cos.COS_REGION.myqcloud.com")
    b := &cos.BaseURL{BucketURL: u}
    c := cos.NewClient(b, &http.Client{
        Transport: &cos.AuthorizationTransport{
            SecretID:  "COS_SECRETID",
            SecretKey: "COS_SECRETKEY",
        },
    })
    // 1.通过响应体获取对象
    name := "test/objectPut.go"
    resp, err := c.Object.Get(context.Background(), name, nil)
    if err != nil {
        panic(err)
    }
    bs, _ := ioutil.ReadAll(resp.Body)
    resp.Body.Close()
    fmt.Printf("%s\n", string(bs))
    // 2.获取对象到本地文件
    _, err = c.Object.GetToFile(context.Background(), name, "exampleobject", nil)
    if err != nil {
        panic(err)
    }
}
```

### 删除对象
```go
package main

import (
    "context"
    "net/http"
    "net/url"
    "os"

    "github.com/tencentyun/cos-go-sdk-v5"
)

func main() {
    // 将 examplebucket-1250000000 和 COS_REGION 修改为真实的信息
    u, _ := url.Parse("https://examplebucket-1250000000.cos.COS_REGION.myqcloud.com")
    b := &cos.BaseURL{BucketURL: u}
    c := cos.NewClient(b, &http.Client{
        Transport: &cos.AuthorizationTransport{
            SecretID:  "COS_SECRETID",
            SecretKey: "COS_SECRETKEY",
        },
    })
    name := "test/objectPut.go"
    _, err := c.Object.Delete(context.Background(), name)
    if err != nil {
        panic(err)
    }
}
```
