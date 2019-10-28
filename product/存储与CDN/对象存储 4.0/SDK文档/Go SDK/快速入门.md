## 下载与安装

#### 相关资源
- 对象存储 COS 的 XML Go SDK 源码下载地址：[ XML Go SDK ](https://github.com/tencentyun/cos-go-sdk-v5)。
- 示例 Demo 下载地址：[ COS XML Go SDK 示例](https://github.com/tencentyun/cos-go-sdk-v5/tree/master/example)。
- 更多信息请参见 [COS Go SDK API](https://godoc.org/github.com/tencentyun/cos-go-sdk-v5) 文档。

#### 环境依赖
- Golang：用于下载和安装 Go 编译运行环境，请前往 Golang 官网进行下载。

#### 安装 SDK
执行以下命令安装 COS Go SDK：
```
go get -u github.com/tencentyun/cos-go-sdk-v5/
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
```go
// 将<BucketName-APPID>和<region>修改为真实的信息
// 例如：http://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com
u, _ := url.Parse("http://<BucketName-APPID>.cos.<region>.myqcloud.com")
b := &cos.BaseURL{BucketURL: u}
// 1.永久密钥
client := cos.NewClient(b, &http.Client{
	Transport: &cos.AuthorizationTransport{
		SecretID: "COS_SECRETID",
        SecretKey: "COS_SECRETKEY",                      
	},                                 
})
// 2.临时密钥
client := cos.NewClient(b, &http.Client{
	Transport: &cos.AuthorizationTransport{
		SecretID: "COS_SECRETID",
        SecretKey: "COS_SECRETKEY",    
        SessionToken："COS_SECRETTOKEN",
	},                                 
})
```

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
	// 将<BucketName-APPID>和<region>修改为真实的信息
	// 例如：http://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com
	u, _ := url.Parse("http://<BucketName-APPID>.cos.<region>.myqcloud.com")
	b := &cos.BaseURL{BucketURL: u}
	c := cos.NewClient(b, &http.Client{
		Transport: &cos.AuthorizationTransport{
			SecretID: "COS_SECRETID",
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
	"os"
	"net/http"

	"github.com/tencentyun/cos-go-sdk-v5"
)

func main() {
	c := cos.NewClient(nil, &http.Client{
		Transport: &cos.AuthorizationTransport{
			SecretID: "COS_SECRETID",
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
	"net/url"
	"os"
	"strings"
	"net/http"

	"github.com/tencentyun/cos-go-sdk-v5"
)

func main() {
	// 将<BucketName-APPID>和<region>修改为真实的信息
	// 例如：http://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com
	u, _ := url.Parse("http://<BucketName-APPID>.cos.<region>.myqcloud.com")
	b := &cos.BaseURL{BucketURL: u}
	c := cos.NewClient(b, &http.Client{
		Transport: &cos.AuthorizationTransport{
			SecretID: "COS_SECRETID",
        	SecretKey: "COS_SECRETKEY",  
		},
	})
    	// 对象键（Key）是对象在存储桶中的唯一标识。
	// 例如，在对象的访问域名 `examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/test/objectPut.go` 中，对象键为 test/objectPut.go
	name := "test/objectPut.go"
	// 1.Normal put string content
	f := strings.NewReader("test")

	_, err := c.Object.Put(context.Background(), name, f, nil)
	if err != nil {
		panic(err)
	}
	// 2.Put object by local file path
	_, err = c.Object.PutFromFile(context.Background(), name, "./test", nil)
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
	"os"
	"net/url"
	"net/http"

	"github.com/tencentyun/cos-go-sdk-v5"
)

func main() {
// 将<BucketName-APPID>和<region>修改为真实的信息
	// 例如：http://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com
	u, _ := url.Parse("http://<BucketName-APPID>.cos.<region>.myqcloud.com")
	b := &cos.BaseURL{BucketURL: u}
	c := cos.NewClient(b, &http.Client{
		Transport: &cos.AuthorizationTransport{
			SecretID: "COS_SECRETID",
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
	"net/url"
	"os"
	"io/ioutil"
	"net/http"

	"github.com/tencentyun/cos-go-sdk-v5"
)

func main() {
	// 将<BucketName-APPID>和<region>修改为真实的信息
	// 例如：http://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com
	u, _ := url.Parse("http://<BucketName-APPID>.cos.<region>.myqcloud.com")
	b := &cos.BaseURL{BucketURL: u}
	c := cos.NewClient(b, &http.Client{
		Transport: &cos.AuthorizationTransport{
			SecretID: "COS_SECRETID",
        	SecretKey: "COS_SECRETKEY",  
		},
	})
    // 1.Get object content by resp body.
	name := "test/hello.txt"
	resp, err := c.Object.Get(context.Background(), name, nil)
	if err != nil {
		panic(err)
	}
	bs, _ := ioutil.ReadAll(resp.Body)
	resp.Body.Close()
	fmt.Printf("%s\n", string(bs))
	// 2.Get object to local file path.
	_, err = c.Object.GetToFile(context.Background(), name, "example", nil)
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
	"fmt"
	"net/url"
	"os"
	"io/ioutil"
	"net/http"

	"github.com/tencentyun/cos-go-sdk-v5"
)

func main() {
	// 将<BucketName-APPID>和<region>修改为真实的信息
	// 例如：http://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com
	u, _ := url.Parse("http://<BucketName-APPID>.cos.<region>.myqcloud.com")
	b := &cos.BaseURL{BucketURL: u}
	c := cos.NewClient(b, &http.Client{
		Transport: &cos.AuthorizationTransport{
			SecretID: "COS_SECRETID",
        	SecretKey: "COS_SECRETKEY",  
		},
	})
	name := "test_object"
	_, err := c.Object.Delete(context.Background(), name)
	if err != nil {
    	panic(err)
    }
}
```
