## 开发准备

### 相关资源
对象存储 COS 的 XML Go SDK 资源下载地址：[XML Go SDK](https://github.com/tencentyun/cos-go-sdk-v5)。更多信息请参见 [COS Go SDK API](https://godoc.org/github.com/tencentyun/cos-go-sdk-v5) 文档

### 环境依赖

[Golang](https://golang.org/doc/install/source?spm=a2c4g.11186623.2.11.168ec486fb1eQK) 用于下载和安装 Go 编译运行环境。Go 安装完毕后新建系统变量 GOPATH，并将其指向您的代码目录。
>?关于文章中出现的 SecretId、SecretKey、Bucket 等名称的含义和获取方式请参考：[COS 术语信息](https://cloud.tencent.com/document/product/436/7751)。

### 安装 SDK

执行以下命令安装 COS Go SDK：
```
 go get -u github.com/tencentyun/cos-go-sdk-v5/
```

## 快速入门
本节介绍如何快速使用 COS Go SDK 完成常见操作，如客户端初始化、创建 Bucket、上传文件和下载文件。
各 API 在 [example](https://github.com/tencentyun/cos-go-sdk-v5/tree/master/example) 目录下有对应的使用示例。
### 初始化客户端

使用 COS 域名生成 COS GO 客户端 Client 结构。

#### 方法原型
```Go
func NewClient(uri *BaseURL, httpClient *http.Client) *Client
```
#### 请求示例
```go
//将<bucketname>、<appid>和<region>修改为真实的信息
//例如：http://test-1253846586.cos.ap-guangzhou.myqcloud.com
u, _ := url.Parse("http://<bucketname>-<appid>.cos.<region>.myqcloud.com")
b := &cos.BaseURL{BucketURL: u}
client := cos.NewClient(b, &http.Client{
	Transport: &cos.AuthorizationTransport{
		//填写用户账号密钥信息，也可以设置为环境变量
		SecretID:  os.Getenv("COS_SECRETID"),                         
		SecretKey: os.Getenv("COS_SECRETKEY"),                      
	},                                 
})
```
#### 参数说明
```go
type AuthorizationTransport struct {
	SecretID     string
	SecretKey    string
	SessionToken string
	// 签名多久过期
	Expire time.Duration         
}
```
#### 返回结果说明
返回的 Client 中包含 Service、Bucket 和 Object 结构，这些结构用于调用各自 API 函数。为简化描述，在 SDK 接口文档示例中省略 Client 初始化过程。

### 创建存储桶

```Go
package main
import (
	"context"
	"io/ioutil"
	"net/http"
	"net/url"
	"os"
	"time"
	
	"github.com/tencentyun/cos-go-sdk-v5"
)

func main() {
	//将<bucketname>、<appid>和<region>修改为真实的信息
	//例如：http://test-1253846586.cos.ap-guangzhou.myqcloud.com
	u, _ := url.Parse("http://<bucketname>-<appid>.cos.<region>.myqcloud.com")
	b := &cos.BaseURL{BucketURL: u}
	c := cos.NewClient(b, &http.Client{
		Transport: &cos.AuthorizationTransport{
			//如实填写账号和密钥，也可以设置为环境变量
			SecretID:  os.Getenv("COS_SECRETID"),
			SecretKey: os.Getenv("COS_SECRETKEY"),
		},
	})
	
	_, err := c.Bucket.Put(context.Background(), nil)
	if err != nil {
		panic(err)
	}
}
```

### 上传文件

```Go
package main
import (
	"context"
	"net/url"
	"os"
	"strings"
	"net/http"

	"github.com/tencentyun/cos-go-sdk-v5"
)

func main() {
	//将<bucketname>、<appid>和<region>修改为真实的信息
	//例如：http://test-1253846586.cos.ap-guangzhou.myqcloud.com
	u, _ := url.Parse("http://<bucketname>-<appid>.cos.<region>.myqcloud.com")
	b := &cos.BaseURL{BucketURL: u}
	c := cos.NewClient(b, &http.Client{
		Transport: &cos.AuthorizationTransport{
            //如实填写账号和密钥，也可以设置为环境变量
			SecretID:  os.Getenv("COS_SECRETID"),
			SecretKey: os.Getenv("COS_SECRETKEY"),
		},
	})
    //对象键（Key）是对象在存储桶中的唯一标识。
	//例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/test/objectPut.go ` 中，对象键为 test/objectPut.go
	name := "test/objectPut.go"
	//Local file
	f := strings.NewReader("test")

	_, err := c.Object.Put(context.Background(), name, f, nil)
	if err != nil {
		panic(err)
	}
}
```

### 下载文件

```Go
package main

import (
	"context"
	"fmt"
	"net/url"
	"os"
	"io/ioutil"
	"net/http"

	"github.com/tencentyun/cos-go-sdk-v5"
)

func main() {
	//将<bucketname>、<appid>和<region>修改为真实的信息
	//例如：http://test-1253846586.cos.ap-guangzhou.myqcloud.com
	u, _ := url.Parse("http://<bucketname>-<appid>.cos.<region>.myqcloud.com")
	b := &cos.BaseURL{BucketURL: u}
	c := cos.NewClient(b, &http.Client{
		Transport: &cos.AuthorizationTransport{
			//如实填写账号和密钥，也可以设置为环境变量
			SecretID:  os.Getenv("COS_SECRETID"),
			SecretKey: os.Getenv("COS_SECRETKEY"),
		},
	})
    //Object key
	name := "test/hello.txt"
	resp, err := c.Object.Get(context.Background(), name, nil)
	if err != nil {
		panic(err)
	}
	bs, _ := ioutil.ReadAll(resp.Body)
	resp.Body.Close()
	fmt.Printf("%s\n", string(bs))
}
```
