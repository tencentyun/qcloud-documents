## 简介
Go SDK 提供获取请求预签名 URL 接口，详细操作请查看本文示例。

关于使用预签名 URL 上传的说明请参见 [预签名授权上传](https://cloud.tencent.com/document/product/436/14114)， 使用预签名 URL 下载的说明请参见 [预签名授权下载](https://cloud.tencent.com/document/product/436/14116)。

>?
> - 建议用户使用临时密钥生成预签名，通过临时授权的方式进一步提高预签名上传、下载等请求的安全性。申请临时密钥时，请遵循 [最小权限指引原则](https://cloud.tencent.com/document/product/436/38618)，防止泄漏目标存储桶或对象之外的资源。
> - 如果您一定要使用永久密钥来生成预签名，建议永久密钥的权限范围仅限于上传或下载操作，以规避风险。
> 

## 获取请求预签名 URL 

```go
func (s *ObjectService) GetPresignedURL(ctx context.Context, httpMethod, key, ak, sk string, expired time.Duration, opt interface{}, signHost ...bool) (*url.URL, error)
```

#### 参数说明

```go
type PresignedURLOptions struct {
    Query      *url.Values
    Header     *http.Header
}
```

| 参数名称           | 类型                         | 描述                            |
| ------------------ | ---------------------------- | ------------------------------- |
| httpMethod            | string                   | HTTP 请求方法                        |
| key    | string       |  对象键（Key）是对象在存储桶中的唯一标识，详情请参见 [对象键](https://cloud.tencent.com/document/product/436/13324#.E5.AF.B9.E8.B1.A1.E9.94.AE)（**注意：用户无需对 key 进行编码操作**）|
| ak             | string                       | SecretId                    |
| sk               | string                       | SecretKey         |
| expired            | time.Duration | 签名有效时长             |
| opt    | interface{} | 扩展项，建议填写 \*PresignedURLOptions 类型的参数。可填nil |
| PresignedURLOptions | struct | 指定签入的请求参数和请求头部。 |
| Query | struct | 签名中要签入的请求参数。 |
| Header | struct | 签名中要签入的请求头部。 |
| signHost | bool | 可选参数，默认为true，获取签名时是否签入Header Host；您也可以选择不签入 Header Host，但可能导致请求失败或安全漏洞。 |

## 永久密钥预签名请求示例

#### 上传请求示例

[//]: # (.cssg-snippet-get-presign-upload-url)
```go
package main

import (
        "context"
        "github.com/tencentyun/cos-go-sdk-v5"
        "net/http"
        "net/url"
        "os"
        "strings"
        "time"
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

        ak := "SECRETID"
        sk := "SECRETKEY"

        name := "exampleobject"
        ctx := context.Background()
        f := strings.NewReader("test")

        // 1. 通过普通方式上传对象
        _, err := client.Object.Put(ctx, name, f, nil)
        if err != nil {
                panic(err)
        }
        // 获取预签名 URL
        presignedURL, err := client.Object.GetPresignedURL(ctx, http.MethodPut, name, ak, sk, time.Hour, nil)
        if err != nil {
                panic(err)
        }
        // 2. 通过预签名方式上传对象
        data := "test upload with presignedURL"
        f = strings.NewReader(data)
        req, err := http.NewRequest(http.MethodPut, presignedURL.String(), f)
        if err != nil {
                panic(err)
        }
        // 用户可自行设置请求头部
        req.Header.Set("Content-Type", "text/html")
        _, err = http.DefaultClient.Do(req)
        if err != nil {
                panic(err)
        }
}
```

#### 下载请求示例

[//]: # (.cssg-snippet-get-presign-download-url)
```go
package main

import (
        "bytes"
        "context"
        "errors"
        "github.com/tencentyun/cos-go-sdk-v5"
        "io/ioutil"
        "net/http"
        "net/url"
        "os"
        "time"
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

        ak := "SECRETID"
        sk := "SECRETKEY"
        name := "exampleobject"
        ctx := context.Background()
        // 1. 通过普通方式下载对象
        resp, err := client.Object.Get(ctx, name, nil)
        if err != nil {
                panic(err)
        }
        bs, _ := ioutil.ReadAll(resp.Body)
        resp.Body.Close()
        // 获取预签名 URL
        presignedURL, err := client.Object.GetPresignedURL(ctx, http.MethodGet, name, ak, sk, time.Hour, nil)
        if err != nil {
                panic(err)
        }
        // 2. 通过预签名 URL下载对象
        resp2, err := http.Get(presignedURL.String())
        if err != nil {
                panic(err)
        }
        bs2, _ := ioutil.ReadAll(resp2.Body)
        resp2.Body.Close()
        if bytes.Compare(bs2, bs) != 0 {
                panic(errors.New("content is not consistent"))
        }
}
```

## 临时密钥预签名请求示例

#### 上传请求示例
```go
package main

import (
    "context"
    "fmt"
    "github.com/tencentyun/cos-go-sdk-v5"
    "net/http"
    "net/url"
    "os"
    "time"
    "strings"
)
// 通过 tag 的方式，用户可以将请求参数或者请求头部放进签名中。
type URLToken struct {
	SessionToken string `url:"x-cos-security-token,omitempty" header:"-"`
}

func main() {
	// 替换成您的临时密钥
	tak := os.Getenv("SECRETID")	// 用户的 SecretId，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140
	tsk := os.Getenv("SECRETKEY")	// 用户的 SecretKey，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140
	token := &URLToken{
		SessionToken: "<token>",
	}
	u, _ := url.Parse("https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com")
	b := &cos.BaseURL{BucketURL: u}
	c := cos.NewClient(b, &http.Client{})

	name := "exampleobject"
	ctx := context.Background()

	// 方法1 通过 PresignedURLOptions 设置 x-cos-security-token
	// PresignedURLOptions 提供用户添加请求参数和请求头部
	opt := &cos.PresignedURLOptions{
		Query:  &url.Values{},
		Header: &http.Header{},
	}
	opt.Query.Add("x-cos-security-token", "<token>")
	// 获取预签名
	presignedURL, err := c.Object.GetPresignedURL(ctx, http.MethodPut, name, tak, tsk, time.Hour, opt)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}
	// 通过预签名方式上传对象
	data := "test upload with presignedURL"
	f := strings.NewReader(data)
	req, err := http.NewRequest(http.MethodPut, presignedURL.String(), f)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
	}
	_, err = http.DefaultClient.Do(req)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
	}	

	// 方法2 通过 tag 设置 x-cos-security-token
	// 获取预签名
	presignedURL, err = c.Object.GetPresignedURL(ctx, http.MethodPut, name, tak, tsk, time.Hour, token)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}
	f = strings.NewReader(data)
	req, err = http.NewRequest(http.MethodPut, presignedURL.String(), f)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
	}
	_, err = http.DefaultClient.Do(req)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
	}	
}
```

#### 下载请求示例

```go
package main

import (
    "context"
    "fmt"
    "github.com/tencentyun/cos-go-sdk-v5"
    "net/http"
    "net/url"
    "os"
    "time"
)
// 通过 tag 的方式，用户可以将请求参数或者请求头部放进签名中。
type URLToken struct {
	SessionToken string `url:"x-cos-security-token,omitempty" header:"-"`
}

func main() {
	// 替换成您的临时密钥
	tak := os.Getenv("SECRETID")  // 用户的 SecretId，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140
	tsk := os.Getenv("SECRETKEY") // 用户的 SecretKey，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140
	token := &URLToken{
		SessionToken: "<token>",
	}
	u, _ := url.Parse("https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com")
	b := &cos.BaseURL{BucketURL: u}
	c := cos.NewClient(b, &http.Client{})

	name := "exampleobject"
	ctx := context.Background()

    // 方法1 通过 PresignedURLOptions 设置 x-cos-security-token
    // PresignedURLOptions 提供用户添加请求参数和请求头部
	opt := &cos.PresignedURLOptions{
		Query:  &url.Values{},
		Header: &http.Header{},
	}
	opt.Query.Add("x-cos-security-token", "<token>")
	// 获取预签名
	presignedURL, err := c.Object.GetPresignedURL(ctx, http.MethodGet, name, tak, tsk, time.Hour, opt)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}
	// 通过预签名访问对象
	resp, err := http.Get(presignedURL.String())
	if err != nil {
		fmt.Printf("Error: %v\n", err)
	}
	defer resp.Body.Close()
	fmt.Println(presignedURL.String())
	fmt.Printf("resp:%v\n", resp)

	// 方法2 通过 tag 设置 x-cos-security-token
	// 获取预签名
	presignedURL, err = c.Object.GetPresignedURL(ctx, http.MethodGet, name, tak, tsk, time.Hour, token)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}
	// 通过预签名访问对象
	resp, err = http.Get(presignedURL.String())
	if err != nil {
		fmt.Printf("Error: %v\n", err)
	}
	defer resp.Body.Close()
	fmt.Println(presignedURL.String())
	fmt.Printf("resp:%v\n", resp)
}
```

## 自定义域名生成预签名示例
```go
package main

import (
    "context"
    "fmt"
    "github.com/tencentyun/cos-go-sdk-v5"
    "net/http"
    "net/url"
    "os"
    "time"
)
func main() {
    // 替换成您的密钥
    tak := os.Getenv("SECRETID")  // 用户的 SecretId，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140
    tsk := os.Getenv("SECRETKEY") // 用户的 SecretKey，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140
    // 修改成用户的自定义域名
    u, _ := url.Parse("https://<自定义域名>")
    b := &cos.BaseURL{BucketURL: u}
    c := cos.NewClient(b, &http.Client{})

    name := "exampleobject"
    ctx := context.Background()

    // 获取预签名
    presignedURL, err := c.Object.GetPresignedURL(ctx, http.MethodGet, name, tak, tsk, time.Hour, nil)
    if err != nil {
        fmt.Printf("Error: %v\n", err)
        return
    }
    // 通过预签名访问对象
    resp, err := http.Get(presignedURL.String())
    if err != nil {
        fmt.Printf("Error: %v\n", err)
    }
    defer resp.Body.Close()
    fmt.Println(presignedURL.String())
    fmt.Printf("resp:%v\n", resp)
}
```

## 添加请求参数或请求头部
```go
package main

import (
    "context"
    "fmt"
    "github.com/tencentyun/cos-go-sdk-v5"
    "net/http"
    "net/url"
    "os"
    "time"
)
func main() {
	// 替换成您的临时密钥
	tak := os.Getenv("SECRETID")   // 用户的 SecretId，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140
	tsk := os.Getenv("SECRETKEY")  // 用户的 SecretKey，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140
	u, _ := url.Parse("https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com")
	b := &cos.BaseURL{BucketURL: u}
	c := cos.NewClient(b, &http.Client{})

	name := "exampleobject"
	ctx := context.Background()

	// PresignedURLOptions 提供用户添加请求参数和请求头部
	opt := &cos.PresignedURLOptions{
	    // http 请求参数，传入的请求参数需与实际请求相同，能够防止用户篡改此 HTTP 请求的参数
		Query:  &url.Values{},
		// http 请求头部，传入的请求头部需包含在实际请求中，能够防止用户篡改签入此处的 HTTP 请求头部
		Header: &http.Header{},
	}
	// 添加请求参数, 返回的预签名 url 将包含该参数
	opt.Query.Add("x-cos-security-token", "<token>")
	// 添加请求头部，返回的预签名 url 只是将请求头部设置到签名里，请求时还需要自行设置对应的 header。
	opt.Header.Add("Content-Type", "text/html")

	// SDK 默认签入 Header Host，不传递 signHost 参数或者 SignHost = true 时，表示签入 Header Host。
	// signHost = false 时，表示不签入 Header Host，不签入 Header Host 可能导致请求失败或安全漏洞。
	var signHost bool = true
	// 获取预签名, 签名中携带host。
	presignedURL, err := c.Object.GetPresignedURL(ctx, http.MethodPut, name, tak, tsk, time.Hour, opt, signHost)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}
	// 通过预签名访问对象
	req, _ := http.NewRequest(http.MethodPut, presignedURL.String(), strings.NewReader("test"))
	// 请求时需要设置对应 header
	req.Header.Set("Content-Type", "text/html")
	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
	}
	defer resp.Body.Close()
	fmt.Println(presignedURL.String())
	fmt.Printf("resp:%v\n", resp)
}
```

