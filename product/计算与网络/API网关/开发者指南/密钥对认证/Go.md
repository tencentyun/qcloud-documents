## 操作场景

该任务指导您使用 Go 语言，通过密钥对鉴权来对您的 API 进行认证管理。

## 操作步骤
1. 在 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1)，创建一个 API，选择鉴权类型为“密钥对鉴权”（参考 [创建 API 概述](https://cloud.tencent.com/document/product/628/11795)）。
2. 将 API 所在服务发布至发布环境（参考 [服务发布与下线](https://cloud.tencent.com/document/product/628/11809)）。
3. 在控制台密钥管理界面创建密钥对。
4. 在控制台使用计划界面创建使用计划，并将使用计划与已创建的密钥对绑定（参考 [使用计划示例](https://cloud.tencent.com/document/product/628/11816)）。
5. 将使用计划与 API 或 API 所在服务进行绑定。
6. 参考 [示例代码](#example)，使用 Go 语言生成签名内容。

## 注意事项
- 最终发送的 HTTP 请求内至少包含两个 Header：Date 和 X-Date 二选一以及 Authorization，可以包含更多 header。如果使用 Date Header，服务端将不会校验时间；如果使用 X-Date Header，服务端将校验时间。
- Date Header 的值为格林威治时间（GMT）格式的 HTTP 请求构造时间，例如 Fri, 09 Oct 2015 00:00:00 GMT。
- X-Date Header 的值为格林威治时间（GMT）格式的 HTTP 请求构造时间，例如 Mon, 19 Mar 2018 12:08:40 GMT。X-Date Header 里的时间和当前时间的差值不能超过15分钟。
- 如果是微服务 API，Header 中需要添加 “X-NameSpace-Code” 和 “X-MicroService-Name” 两个字段，通用 API 不需要添加，Demo 中默认添加了这两个字段。

<span id="example"></span>
## 示例代码
```
package main

import (
	"time"
	"fmt"
	"crypto/hmac"
	"crypto/sha1"
	"io"
	"io/ioutil"
	"encoding/base64"
	"net/http"
)


func calcAuthorization(source string, secretId string, secretKey string) (sign string, dateTime string, err error) {
	timeLocation, _ := time.LoadLocation("Etc/GMT")
	dateTime = time.Now().In(timeLocation).Format("Mon, 02 Jan 2006 15:04:05 GMT")
	sign = fmt.Sprintf("x-date: %s\nsource: %s", dateTime, source)
	fmt.Println(sign)

	//hmac-sha1
	h := hmac.New(sha1.New, []byte(secretKey))
	io.WriteString(h, sign)
	sign = fmt.Sprintf("%x", h.Sum(nil))
	sign = string(h.Sum(nil))
	fmt.Println("sign:", fmt.Sprintf("%s", h.Sum(nil)))

	//base64
	sign = base64.StdEncoding.EncodeToString([]byte(sign))
	fmt.Println("sign:", sign)

	auth := fmt.Sprintf("hmac id=\"%s\", algorithm=\"hmac-sha1\", headers=\"x-date source\", signature=\"%s\"", 
		secretId, sign)
	fmt.Println("auth:", auth)
		
	return auth, dateTime, nil
}

func main () {
	SecretId := "your SecretId" // 密钥对的 SecretId
	SecretKey := "your SecretKey" // 密钥对的 SecretKey
	source := "xxxxxx" // 签名水印值，可填写任意值

	sign, dateTime, err := calcAuthorization(source, SecretId, SecretKey)
	if err != nil {
		fmt.Println(err)
		return
	}

	defaultDomain := "service-xxxxxxxx-1234567890.ap-guangzhou.apigateway.myqcloud.com" // 用户 API 所在服务的域名

	reqUrl := "https://service-xxxxxxxx-1234567890.ap-guangzhou.apigateway.myqcloud.com/release/yousa" // 用户 API 的访问路径
	client := &http.Client{
		Timeout: 7 * time.Second,//set timeout
	}

	req, err := http.NewRequest("GET", reqUrl, nil) //set body
	if err != nil {
		fmt.Println(err)		
		return 
	}

	req.Header.Set("Accept", "*/*")
	req.Header.Set("Accept-Charset", "utf-8;")
	req.Header.Set("Host", defaultDomain)
	req.Header.Set("Source", source)
	req.Header.Set("X-Date", dateTime)
	req.Header.Set("Authorization", sign)
	
	// 如果是微服务 API，Header 中需要添加'X-NameSpace-Code'、'X-MicroService-Name'两个字段，通用 API 不需要添加。
	req.Header.Set("x-NameSpace-Code", "testmic")
	req.Header.Set("x-MicroService-Name", "provider-demo")

	resp, err := client.Do(req)
	if err != nil {
		fmt.Println(err)		
		return 
	}
	defer resp.Body.Close()

	fmt.Println("status code:", resp.StatusCode)
	
	//get resp header
	var headerMsg string
	for key, _ := range resp.Header {
		headerMsg += fmt.Sprintf("\n%s:%s", key, resp.Header.Get(key))
	}
	fmt.Println(headerMsg)

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println(err)		
		return 
	}

	fmt.Println(string(body))
	
}
```

