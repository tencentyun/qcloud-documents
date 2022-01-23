## 操作场景

该任务指导您使用 Go 语言，通过应用认证来对您的 API 进行认证管理。

## 操作步骤

1. 在 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1)，创建一个 API，选择鉴权类型为“应用认证”（参考 [创建 API 概述](https://cloud.tencent.com/document/product/628/11795)）。
2. 将 API 所在服务发布至发布环境（参考 [服务发布与下线](https://cloud.tencent.com/document/product/628/11809)）。
3. 在控制台 [应用管理](https://console.cloud.tencent.com/apigateway/app) 界面创建应用。
4. 在应用列表中选中已经创建好的应用，单击**绑定 API**，选择服务和 API 后单击**提交**，即可将应用与 API 建立绑定关系。
5. 参考 [示例代码](#示例代码)，使用 Go 语言生成签名内容。

## 环境依赖

API 网关提供 JSON 请求方式和 form 请求方式的示例代码，请您根据自己业务的实际情况合理选择。

## 注意事项

- 应用生命周期管理，以及 API 向应用授权、应用绑定 API 等操作请您参考 [应用管理](https://cloud.tencent.com/document/product/628/55087)。
- 应用生成签名过程请您参考 [应用认证方式](https://cloud.tencent.com/document/product/628/55088)。

## 示例代码[](id:示例代码)

### JSON 请求方式示例代码

```go
package main

import (
    "crypto/hmac"
    "crypto/md5"
    "crypto/sha1"
    "encoding/base64"
    "encoding/hex"
    "fmt"
    "io/ioutil"
    "log"
    "net/http"
	"net/url"
	"sort"
    "strings"
    "time"
)

func main() {
    // 应用 ApiAppKey
    const ApiAppKey = "Your ApiAppKey"
    //应用 ApiAppSecret
	const ApiAppSecret = "Your ApiAppSecret"
	
    const Url = "http://service-xxx-xxx.gz.apigw.tencentcs.com/"

    const GmtFormat = "Mon, 02 Jan 2006 15:04:05 GMT"
    const HTTPMethod = "GET"
    const Accept = "application/json"
    const ContentType = "application/json"

    // 根据 Url 解析 Host 和 Path
    u, err := url.Parse(Url)
    if err != nil {
        log.Fatal(err)
    }
    Host := u.Hostname()
	Path := u.Path
	Query := u.RawQuery
	
	// 签名path不带环境信息
	if strings.HasPrefix(Path, "/release") {
		Path = strings.TrimPrefix(Path, "/release")
	}else if strings.HasPrefix(Path, "/test") {
		Path = strings.TrimPrefix(Path, "/test")
	}else if strings.HasPrefix(Path, "/prepub") {
		Path = strings.TrimPrefix(Path, "/prepub")
	}
	
	if Path == "" {
		Path = "/"
	}

	// 拼接query参数，query参数需要按字典序排序
	if len(Query) > 0 {
		args, _ := url.ParseQuery(Query)

		var keys []string
		for k := range args {
			keys = append(keys, k)
		}
		sort.Strings(keys)

		sortQuery := ""
		for _, k := range keys {
			if args[k][0] != "" {
				sortQuery = sortQuery + "&" + k + "=" + args[k][0]
			} else {
				sortQuery = sortQuery + "&" + k 
			}
		}
		sortQuery = strings.TrimPrefix(sortQuery, "&")
		
    	Path = Path + "?" + sortQuery
	}

    // 获取当前 UTC
    xDate := time.Now().UTC().Format(GmtFormat)
	ContentMD5 := ""
	bodyStr := `{"arg1":"a","arg2":"b"}`
	if HTTPMethod == "POST" {
		h := md5.New()
		h.Write([]byte(bodyStr))
		md5Str := hex.EncodeToString(h.Sum(nil))
		ContentMD5 = base64.StdEncoding.EncodeToString([]byte(md5Str))
	}

    // 构造签名
    signingStr := fmt.Sprintf("x-date: %s\n%s\n%s\n%s\n%s\n%s", xDate, HTTPMethod, Accept, ContentType,
        ContentMD5, Path)
    mac := hmac.New(sha1.New, []byte(ApiAppSecret))

    _, err = mac.Write([]byte(signingStr))
    if err != nil {
        log.Fatal(err)
    }
    signature := base64.StdEncoding.EncodeToString(mac.Sum(nil))
    sign := fmt.Sprintf("hmac id=\"%s\", algorithm=\"hmac-sha1\", headers=\"x-date\", signature=\"%s\"",
        ApiAppKey, signature)

    // 构造请求
    headers := map[string]string{
        "Host":          Host,
        "Accept":        Accept,
        "Content-Type":  ContentType,
        "x-date":        xDate,
        "Authorization": sign,
    }

    // 发送请求
    req, err := http.NewRequest(HTTPMethod, Url, strings.NewReader(bodyStr))
    if err != nil {
        log.Fatal(err)
    }

    for k, v := range headers {
        req.Header.Add(k, v)
    }

    res, err := http.DefaultClient.Do(req)
    if err != nil {
        log.Fatal(err)
    }
    defer res.Body.Close()

    resBody, _ := ioutil.ReadAll(res.Body)

    fmt.Println(string(resBody))
}
```

### form 请求方式示例代码

```go
package main

import (
    "crypto/hmac"
    "crypto/sha1"
    "encoding/base64"
    "fmt"
    "io/ioutil"
    "log"
    "net/http"
    "net/url"
    "sort"
    "strings"
    "time"
)

func main() {
    // 应用 ApiAppKey
    const ApiAppKey = "Your ApiAppKey"
    //应用 ApiAppSecret
	const ApiAppSecret = "Your ApiAppSecret"
	
    const Url = "http://service-xxx-xxx.gz.apigw.tencentcs.com/"

    const GmtFormat = "Mon, 02 Jan 2006 15:04:05 GMT"
    const HTTPMethod = "POST"
    const Accept = "application/json"
    const ContentType = "application/x-www-form-urlencoded"

    // 根据 Url 解析 Host 和 Path
    u, err := url.Parse(Url)
    if err != nil {
        log.Fatal(err)
    }
    Host := u.Hostname()
	Path := u.Path
    Query := u.RawQuery
	
	// 签名path不带环境信息
	if strings.HasPrefix(Path, "/release") {
		Path = strings.TrimPrefix(Path, "/release")
	}else if strings.HasPrefix(Path, "/test") {
		Path = strings.TrimPrefix(Path, "/test")
	}else if strings.HasPrefix(Path, "/prepub") {
		Path = strings.TrimPrefix(Path, "/prepub")
	}
	
	if Path == "" {
		Path = "/"
	}

	// 拼接query参数，query参数需要按字典序排序，demo假设已经排序，请自行实现排序
	if len(Query) > 0 {
    	Path = Path + "?" + Query
	}

    // 获取当前 UTC
    xDate := time.Now().UTC().Format(GmtFormat)
    ContentMD5 := ""
    
    // 请求 Body form数据
	body := map[string]string{
        "arg1": "a",
        "arg2": "b",
    }
    var bodyKeys []string
    for k := range body {
        bodyKeys = append(bodyKeys, k)
    }
    
    var bodyBuilder strings.Builder
    sort.Strings(bodyKeys)
    for _, k := range bodyKeys {
        bodyBuilder.WriteString(fmt.Sprintf("%s=%s&", k, body[k]))
    }
    bodyStr := bodyBuilder.String()
    // 去掉最后一个&
    bodyStr = bodyStr[:len(bodyStr) - 1]

    // 构造签名
    signingStr := fmt.Sprintf("x-date: %s\n%s\n%s\n%s\n%s\n%s?%s", xDate, HTTPMethod, Accept, ContentType,
        ContentMD5, Path, bodyStr)
    mac := hmac.New(sha1.New, []byte(ApiAppSecret))

    _, err = mac.Write([]byte(signingStr))
    if err != nil {
        log.Fatal(err)
    }
    signature := base64.StdEncoding.EncodeToString(mac.Sum(nil))
    sign := fmt.Sprintf("hmac id=\"%s\", algorithm=\"hmac-sha1\", headers=\"x-date\", signature=\"%s\"",
        ApiAppKey, signature)

    // 构造请求
    headers := map[string]string{
        "Host":          Host,
        "Accept":        Accept,
        "Content-Type":  ContentType,
        "x-date":        xDate,
        "Authorization": sign,
    }

    // 发送请求
    req, err := http.NewRequest(HTTPMethod, Url, strings.NewReader(bodyStr))
    if err != nil {
        log.Fatal(err)
    }

    for k, v := range headers {
        req.Header.Add(k, v)
    }

    res, err := http.DefaultClient.Do(req)
    if err != nil {
        log.Fatal(err)
    }
    defer res.Body.Close()

    resBody, _ := ioutil.ReadAll(res.Body)

    fmt.Println(string(resBody))
}
```



### 国密 hmac_sm3 算法代码示例

[点击下载>>](https://bruceppeng-1300555551.cos.ap-nanjing.myqcloud.com/%E5%9B%BD%E5%AF%86hmac_sm3%E7%AE%97%E6%B3%95.zip) 完整项目示例

```go
package main

import (
    "crypto/md5"
    "encoding/base64"
    "encoding/hex"
    "fmt"
    "io/ioutil"
    "log"
    "net/http"
	"net/url"
	"sort"
    "strings"
    "time"
    "unsafe"
)

/*
#cgo CFLAGS: -I./
#cgo LDFLAGS: -L./ -lTencentSM
#include "sm.h" //非标准c头文件，所以用引号
*/
import "C"


func mySM3_HMAC(data []byte, dataLen int, key []byte, keyLen int, mac []byte, macLen int) int {
    if data == nil || key == nil || mac == nil || len(mac) != macLen {
		panic("invalid parameter")
	}
	return int(C.SM3_HMAC((*C.uchar)(unsafe.Pointer(&data[0])), (C.size_t)(dataLen),
		(*C.uchar)(unsafe.Pointer(&key[0])), (C.size_t)(keyLen), (*C.uchar)(unsafe.Pointer(&mac[0]))))
}

func main() {
    // 应用 ApiAppKey
    const ApiAppKey = "Your ApiAppKey"
    //应用 ApiAppSecret
	const ApiAppSecret = "Your ApiAppSecret"
	
    const Url = "http://service-xxx-xxx.gz.apigw.tencentcs.com/a?c=1&b=3"

    const GmtFormat = "Mon, 02 Jan 2006 15:04:05 GMT"
    const HTTPMethod = "GET"
    const Accept = "application/json"
    const ContentType = "application/json"

    // 根据 Url 解析 Host 和 Path
    u, err := url.Parse(Url)
    if err != nil {
        log.Fatal(err)
    }
    Host := u.Hostname()
	Path := u.Path
	Query := u.RawQuery
	
	// 签名path不带环境信息
	if strings.HasPrefix(Path, "/release") {
		Path = strings.TrimPrefix(Path, "/release")
	}else if strings.HasPrefix(Path, "/test") {
		Path = strings.TrimPrefix(Path, "/test")
	}else if strings.HasPrefix(Path, "/prepub") {
		Path = strings.TrimPrefix(Path, "/prepub")
	}
	
	if Path == "" {
		Path = "/"
	}

	// 拼接query参数，query参数需要按字典序排序
	if len(Query) > 0 {
		args, _ := url.ParseQuery(Query)

		var keys []string
		for k := range args {
			keys = append(keys, k)
		}
		sort.Strings(keys)

		sortQuery := ""
		for _, k := range keys {
			if args[k][0] != "" {
				sortQuery = sortQuery + "&" + k + "=" + args[k][0]
			} else {
				sortQuery = sortQuery + "&" + k 
			}
		}
		sortQuery = strings.TrimPrefix(sortQuery, "&")
		
    	Path = Path + "?" + sortQuery
	}

    // 获取当前 UTC
    xDate := time.Now().UTC().Format(GmtFormat)
	ContentMD5 := ""
	bodyStr := `{"arg1":"a","arg2":"b"}`
	if HTTPMethod == "POST" {
		h := md5.New()
		h.Write([]byte(bodyStr))
		md5Str := hex.EncodeToString(h.Sum(nil))
		ContentMD5 = base64.StdEncoding.EncodeToString([]byte(md5Str))
	}

    // 构造签名
    signingStr := fmt.Sprintf("x-date: %s\n%s\n%s\n%s\n%s\n%s", xDate, HTTPMethod, Accept, ContentType,
        ContentMD5, Path)

    data := []byte(signingStr)
    key := []byte(ApiAppSecret)
    var out [32]byte

    mySM3_HMAC(data[:], len(data), key[:], len(key), out[:], len(out))
    signature := base64.StdEncoding.EncodeToString(out[:])
    
    sign := fmt.Sprintf("hmac id=\"%s\", algorithm=\"hmac-sm3\", headers=\"x-date\", signature=\"%s\"",
        ApiAppKey, signature)

    // 构造请求
    headers := map[string]string{
        "Host":          Host,
        "Accept":        Accept,
        "Content-Type":  ContentType,
        "x-date":        xDate,
        "Authorization": sign,
    }

    // 发送请求
    req, err := http.NewRequest(HTTPMethod, Url, strings.NewReader(bodyStr))
    if err != nil {
        log.Fatal(err)
    }

    for k, v := range headers {
        req.Header.Add(k, v)
    }

    res, err := http.DefaultClient.Do(req)
    if err != nil {
        log.Fatal(err)
    }
    defer res.Body.Close()

    resBody, _ := ioutil.ReadAll(res.Body)

    fmt.Println(string(resBody))
}
```



