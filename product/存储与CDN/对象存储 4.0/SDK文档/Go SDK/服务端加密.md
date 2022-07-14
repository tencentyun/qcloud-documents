
如果需要对上传的对象进行加密，我们支持以下加密方式。

#### 使用 COS 托管加密密钥的服务端加密（SSE-COS）保护数据

由腾讯云 COS 托管主密钥和管理数据。COS 会帮助您在数据写入数据中心时自动加密，并在您取用该数据时自动解密。目前支持使用 COS 主密钥对数据进行 AES-256 加密。

GO SDK 通过设置`ObjectPutHeaderOptions`的`XCosServerSideEncryption`成员来完成。

[//]: # (.cssg-snippet-put-object-sse)
```go
	// 下载对象，下载对象需要用户提供密钥	// 下载对象，下载对象需要用户提供密钥package main

import (
	"context"
    "errors"
    "io/ioutil"
    "net/http"
    "net/url"
    "os"
    "strings"

    "github.com/tencentyun/cos-go-sdk-v5"
    "github.com/tencentyun/cos-go-sdk-v5/debug"
)

func main() {
    // 替换成您的<Bucketname-APPID>
    u, _ := url.Parse("https://<Bucketname-APPID>.cos.ap-guangzhou.myqcloud.com")
    b := &cos.BaseURL{BucketURL: u}
    c := cos.NewClient(b, &http.Client{
            Transport: &cos.AuthorizationTransport{
                    SecretID:  os.Getenv("SECRETID"),
                    SecretKey: os.Getenv("SECRETKEY"),
                    Transport: &debug.DebugRequestTransport{
                            RequestHeader: true,
                            // Notice when put a large file and set need the request body, might happend out of memory error.
                            RequestBody:    false,
                            ResponseHeader: true,
                            ResponseBody:   true,
                    },
            },
    })
    opt := &cos.ObjectPutOptions{
            ObjectPutHeaderOptions: &cos.ObjectPutHeaderOptions{
                    ContentType:           "text/html",
    		        XCosServerSideEncryption: "AES256",
            },
            ACLHeaderOptions: &cos.ACLHeaderOptions{},
    }
    name := "PutFromGoWithSSE-COS"
    content := "Put Object From Go With SSE-COS"
    f := strings.NewReader(content)
    _, err := c.Object.Put(context.Background(), name, f, opt)
    if err != nil {
    	panic(err)
    }
	// 下载对象
    getopt := &cos.ObjectGetOptions{}
    var resp *cos.Response
    resp, err = c.Object.Get(context.Background(), name, getopt)
    if err != nil {
    	panic(err)
    }
	// 验证
    bodyBytes, _ := ioutil.ReadAll(resp.Body)
    bodyContent := string(bodyBytes)
    if bodyContent != content {
    	panic(errors.New("Content inconsistency"))
    }
}
```

#### 使用客户提供的加密密钥的服务端加密 （SSE-C）保护数据

加密密钥由用户自己提供，用户在上传对象时，COS 将使用用户提供的加密密钥对用户的数据进行 AES-256 加密。GO SDK 通过设置 `ObjectPutHeaderOptions`的`XCosSSECustomer*`成员来完成。

> !
>- 该加密所运行的服务需要使用 HTTPS 请求。
>- customerKey：用户提供的密钥，传入一个32字节的字符串，支持数字、字母、字符的组合，不支持中文。
>- 如果上传的源文件调用了该方法，那么在使用 GET（下载）、HEAD（查询）时对源对象操作的时候也要调用该方法。

[//]: # (.cssg-snippet-put-object-sse-c)
```go
package main

import (
	"context"
    "net/url"
    "os"
    "strings"
    "errors"
    "io/ioutil"
    "net/http"

    "github.com/tencentyun/cos-go-sdk-v5"
    "github.com/tencentyun/cos-go-sdk-v5/debug"
)

func main() {
    // 替换成您的<Bucketname-APPID>
    u, _ := url.Parse("https://<Bucketname-APPID>.cos.ap-guangzhou.myqcloud.com")
    b := &cos.BaseURL{BucketURL: u}
    c := cos.NewClient(b, &http.Client{
            Transport: &cos.AuthorizationTransport{
                    SecretID:  os.Getenv("SECRETID"),
                    SecretKey: os.Getenv("SECRETKEY"),
                    Transport: &debug.DebugRequestTransport{
                            RequestHeader: true,
                            // Notice when put a large file and set need the request body, might happend out of memory error.
                            RequestBody:    false,
                            ResponseHeader: true,
                            ResponseBody:   true,
                    },
            },
    })
    opt := &cos.ObjectPutOptions{
            ObjectPutHeaderOptions: &cos.ObjectPutHeaderOptions{
                    ContentType: "text/html",
            		XCosSSECustomerAglo: "AES256",
                    XCosSSECustomerKey: "MDEyMzQ1Njc4OUFCQ0RFRjAxMjM0NTY3ODlBQkNERUY=",
                    XCosSSECustomerKeyMD5: "U5L61r7jcwdNvT7frmUG8g==",
                },
            ACLHeaderOptions: &cos.ACLHeaderOptions{},
    }
    name := "PutFromGoWithSSE-C"
    content := "Put Object From Go With SSE-C"
    f := strings.NewReader(content)
    _, err := c.Object.Put(context.Background(), name, f, opt)
    if err != nil {
    	panic(err)
    }
	// 下载对象，下载对象需要用户提供密钥
    getopt := &cos.ObjectGetOptions{
        XCosSSECustomerAglo: "AES256",
        XCosSSECustomerKey: "MDEyMzQ1Njc4OUFCQ0RFRjAxMjM0NTY3ODlBQkNERUY=",
        XCosSSECustomerKeyMD5: "U5L61r7jcwdNvT7frmUG8g==",
    }
    var resp *cos.Response
    resp, err = c.Object.Get(context.Background(), name, getopt)
    if err != nil {
        panic(err)
    }
	// 验证
    bodyBytes, _ := ioutil.ReadAll(resp.Body)
    bodyContent := string(bodyBytes)
    if bodyContent != content {
        panic(errors.New("Content inconsistency"))
    }
}
```
