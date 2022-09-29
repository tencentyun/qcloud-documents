## 概述
腾讯云智聆口语评测（Smart Oral Evaluation，SOE）是腾讯云推出的语音评测产品，是基于口语类教育培训场景和腾讯云的语音处理技术，应用特征提取、声学模型和语音识别算法，为儿童和成人提供高准确度的口语发音评测。支持单词、句子和段落模式的评测，多维度反馈口语表现，可广泛应用于中文及英语口语类教学中。
Tencent Cound API 3.0 SDK，封装了腾讯云的 SDK，通过集成SDK，可以快速接入相关产品功能，如智聆口语评测，数学作业批改，英文作文批改。本文档介绍 [智聆口语评测](https://cloud.tencent.com/document/product/884/19309) 相关说明。

## 流程图
流程图请参见 [服务模式](https://cloud.tencent.com/document/product/884/33697)。

## SDK 集成准备
1. 获取密钥
SecretId 和 SecretKey 是使用 SDK 的安全凭证，您可以在访问管理 > 访问密钥 > [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取该凭证。
>! 密钥属于敏感信息，正式密钥仅可在调试使用，线上环境情况下，为了防止他人盗取，推荐使用 [临时签名](https://cloud.tencent.com/document/product/884/31888#SecretKey)，具体请参考 [签名](https://cloud.tencent.com/document/product/884/31888#SecretKey) 相关内容。
>
![](https://qcloudimg.tencent-cloud.cn/raw/3049463174ada47857762086690e7c26.png)
2. 设备准备
准备一台电脑。


## SDK DEMO 使用流程
1. 安装依赖环境
Go 1.9 版本及以上（如使用 go mod 需要 Go 1.14）。

2. 下载 SDK
从 github 下载 [tencentcloud-sdk-go](https://github.com/TencentCloud/tencentcloud-sdk-go)。或者在终端输入 git 命令：
```
git clone https://github.com/TencentCloud/tencentcloud-sdk-go.git
```
如果无法使用 git 或不清楚如何使用，可以单击 [这里](https://github.com/TencentCloud/tencentcloud-sdk-go/archive/refs/heads/master.zip) 下载。

3. 获取安装
	- 通过 go get 安装（推荐）
推荐使用腾讯云镜像加速下载：
		1. Linux 或 MacOS：
```
export GOPROXY=https://mirrors.tencent.com/go/
```
		2. Windows：
```
set GOPROXY=https://mirrors.tencent.com/go/
```
	- 按需安装（推荐）
>! 此安装方式仅支持使用 Go Modules 模式进行依赖管理，即环境变量 GO111MODULE=auto 或者 GO111MODULE=on, 并且在您的项目中执行了 go mod init xxx。
>
如果您使用 GOPATH，请参考下节： 全部安装。
v1.0.170后可以按照产品下载，您只需下载基础包和对应的产品包(如 cvm)即可，不需要下载全部的产品，从而加快您构建镜像或者编译的速度：
		1. 安装公共基础包：
```
go get -v -u github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common
```
		2. 安装对应的产品包(如 soe)：
```
go get -v -u github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/soe
```
	- 全部安装
此模式支持 GOPATH 和 Go Modules。此方式会一次性下载腾讯云所有产品的包：
```
go get -v -u github.com/tencentcloud/tencentcloud-sdk-go
```
>! 为了支持 go mod，SDK 版本号从 v3.x 降到了 v1.x。并于2021.05.10移除了所有v3.0.*和3.0.*的 tag，如需追溯以前的 tag，请参考项目根目录下的 commit2tag文件。
	- 通过源码安装
前往代码托管地址 [Github](https://github.com/tencentcloud/tencentcloud-sdk-go) 或者 [Gitee](https://gitee.com/tencentcloud/tencentcloud-sdk-go) 下载最新代码，解压后安装到 `$GOPATH/src/github.com/tencentcloud` 目录下。

4. 运行项目
进入 `examples/soe/v20180903/initOralProcess.go`，填入 SecretId 和 SecretKey。
![](https://qcloudimg.tencent-cloud.cn/raw/46229dd55d861a373d771c1a606c5466.png)
填入请求参数，参考 [InitOralProcess](https://cloud.tencent.com/document/product/884/19319)，运行项目，进行评测。
![](https://qcloudimg.tencent-cloud.cn/raw/2894c05e9778c47f91a23703dc6558d8.png)
获取评测结果，参考 [数据结构](https://cloud.tencent.com/document/product/884/19320)。 

## SDK 使用方法
### 临时密钥（推荐）
客户端为了密钥安全性，需要考虑在服务端使用临时密钥，对密钥进行加密处理。Go 临时密钥参考如下（填入密钥信息使用）：
```
package main

import (
    "fmt"
    "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
    "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/errors"
    "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile"
    sts "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/sts/v20180813"
)

func main() {
    // 必要步骤：
    // 实例化一个认证对象，入参需要传入腾讯云账户密钥对secretId，secretKey。
    // 这里采用的是从环境变量读取的方式，需要在环境变量中先设置这两个值。
    // 你也可以直接在代码中写死密钥对，但是小心不要将代码复制、上传或者分享给他人，
    // 以免泄露密钥对危及你的财产安全。
    credential := common.NewCredential(
        "secretId",
        "secretKey",
    )

    // 非必要步骤
    // 实例化一个客户端配置对象，可以指定超时时间等配置
    cpf := profile.NewClientProfile()
    // SDK默认使用POST方法。
    // 如果你一定要使用GET方法，可以在这里设置。GET方法无法处理一些较大的请求。
    cpf.HttpProfile.ReqMethod = "POST"
    // SDK有默认的超时时间，非必要请不要进行调整。
    // 如有需要请在代码中查阅以获取最新的默认值。
    cpf.HttpProfile.ReqTimeout = 30
    // SDK会自动指定域名。通常是不需要特地指定域名的
    cpf.HttpProfile.Endpoint = "sts.tencentcloudapi.com"

    // 实例化要请求产品的client对象
    // 第二个参数是地域信息
    client, _ := sts.NewClient(credential, "ap-guangzhou", cpf)
    // 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
    // 你可以直接查询SDK源码确定InitOralProcessRequest有哪些属性可以设置，
    // 属性可能是基本类型，也可能引用了另一个数据结构。
    // 推荐使用IDE进行开发，可以方便的跳转查阅各个接口和数据结构的文档说明。
    request := sts.NewGetFederationTokenRequest()

    // 基本类型的设置。
    // 此接口允许设置返回的实例数量。此处指定为只返回一个。
    // SDK采用的是指针风格指定参数，即使对于基本类型你也需要用指针来对参数赋值。
    // SDK提供对基本类型的指针引用封装函数
    request.Name = common.StringPtr("soe")
    request.Policy = common.StringPtr("{\"version\": \"2.0\",\"statement\": {\"effect\": \"allow\", \"action\": [\"soe:TransmitOralProcessWithInit\"], \"resource\": \"*\"}}")


    // 通过client对象调用想要访问的接口，需要传入请求对象
    response, err := client.GetFederationToken(request)
    // 处理异常
    fmt.Println(err)
    if _, ok := err.(*errors.TencentCloudSDKError); ok {
        fmt.Printf("An API error has returned: %s", err)
        return
    }
    // 非SDK异常，直接失败。实际代码中可以加入其他的处理。
    if err != nil {
        panic(err)
    }
    // 打印返回的json字符串
    fmt.Printf("%s", response.ToJsonString())
}

```

### 内部签名（推荐）
#### 发音数据传输接口附带初始化过程(推荐)
[TransmitOralProcessWithInit](https://cloud.tencent.com/document/api/884/32605) 接口使用示例：
```
package main

import (
	b64 "encoding/base64"
	"fmt"
	"github.com/satori/go.uuid"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/errors"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile"
	soe "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/soe/v20180724"
	"io/ioutil"
)

func main() {
	// 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey,此处还需注意密钥对的保密
	// 密钥可前往https://console.cloud.tencent.com/cam/capi网站进行获取
	
	//check(err)
	//fmt.Print(string(dat))

	//文件转base64
    dat, err := ioutil.ReadFile("") //本地音频地址
	sEnc := b64.StdEncoding.EncodeToString(dat)
	fmt.Println(sEnc)
    
    //获取uuid
	id := uuid.NewV4()
	ids := id.String()

	credential := common.NewCredential(
		"secretId",
		"secretKey",
	)
	// 实例化一个client选项，可选的，没有特殊需求可以跳过
	cpf := profile.NewClientProfile()
	cpf.HttpProfile.Endpoint = "soe.tencentcloudapi.com"
	// 实例化要请求产品的client对象,clientProfile是可选的
	client, _ := soe.NewClient(credential, "", cpf)

	// 实例化一个请求对象,每个接口都会对应一个request对象
	request := soe.NewTransmitOralProcessWithInitRequest()
	request.SeqId = common.Int64Ptr(1)
	request.IsEnd = common.Int64Ptr(1)
	request.VoiceFileType = common.Int64Ptr(3)
	request.VoiceEncodeType = common.Int64Ptr(1)
	request.UserVoiceData = common.StringPtr(sEnc)
	request.SessionId = common.StringPtr(ids)
	request.RefText = common.StringPtr("hello")
	request.WorkMode = common.Int64Ptr(0)
	request.EvalMode = common.Int64Ptr(0)
	request.StorageMode = common.Int64Ptr(5)
	request.ScoreCoeff = common.Float64Ptr(1)


	// 返回的resp是一个TransmitOralProcessWithInitResponse的实例，与请求对象对应
	response, err := client.TransmitOralProcessWithInit(request)
	if _, ok := err.(*errors.TencentCloudSDKError); ok {
		fmt.Printf("An API error has returned: %s", err)
		return
	}
	if err != nil {
		panic(err)
	}
	// 输出json格式的字符串回包
	fmt.Printf("%s", response.ToJsonString())
} 
```

#### 发音评估初始化和发音数据传输接口
[InitOralProcess]( https://cloud.tencent.com/document/api/884/19319) 和 [TransmitOralProcess](https://cloud.tencent.com/document/api/884/19318) 组合使用示例：
```
package main

import (
	b64 "encoding/base64"
	"encoding/json"
	"fmt"
	uuid "github.com/satori/go.uuid"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/errors"
	soe "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/soe/v20180724"
	"io/ioutil"
)

func main() {


	//文件转base64
	dat, err := ioutil.ReadFile("") // 本地音频地址
	sEnc := b64.StdEncoding.EncodeToString(dat)
	fmt.Println(sEnc)
	id := uuid.NewV4()
	ids := id.String()
	// 必要步骤：
	// 实例化一个认证对象，入参需要传入腾讯云账户密钥对secretId，secretKey。
	// 这里采用的是从环境变量读取的方式，需要在环境变量中先设置这两个值。
	// 你也可以直接在代码中写死密钥对，但是小心不要将代码复制、上传或者分享给他人，
	// 以免泄露密钥对危及你的财产安全。
	credential := common.NewCredential(
		// os.Getenv("TENCENTCLOUD_SECRET_ID"),
		// os.Getenv("TENCENTCLOUD_SECRET_KEY"),
		"",
		"",
	)

	// 非必要步骤
	// 实例化一个客户端配置对象，可以指定超时时间等配置
	cpf := profile.NewClientProfile()
	// SDK默认使用POST方法。
	// 如果你一定要使用GET方法，可以在这里设置。GET方法无法处理一些较大的请求。
	cpf.HttpProfile.ReqMethod = "POST"
	// SDK有默认的超时时间，非必要请不要进行调整。
	// 如有需要请在代码中查阅以获取最新的默认值。
	cpf.HttpProfile.ReqTimeout = 30
	// SDK会自动指定域名。通常是不需要特地指定域名的
	cpf.HttpProfile.Endpoint = "soe.tencentcloudapi.com"

	// 实例化要请求产品的client对象
	// 第二个参数是地域信息
	client, _ := soe.NewClient(credential, "ap-guangzhou", cpf)
	// 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
	// 你可以直接查询SDK源码确定InitOralProcessRequest有哪些属性可以设置，
	// 属性可能是基本类型，也可能引用了另一个数据结构。
	// 推荐使用IDE进行开发，可以方便的跳转查阅各个接口和数据结构的文档说明。
	request := soe.NewInitOralProcessRequest()

	// 基本类型的设置。
	// 此接口允许设置返回的实例数量。此处指定为只返回一个。
	// SDK采用的是指针风格指定参数，即使对于基本类型你也需要用指针来对参数赋值。
	// SDK提供对基本类型的指针引用封装函数
	request.WorkMode = common.Int64Ptr(1)
	request.EvalMode = common.Int64Ptr(0)
	request.ScoreCoeff = common.Float64Ptr(2.0)
	request.SessionId = common.StringPtr(ids)
	request.RefText = common.StringPtr("since")

	// 通过client对象调用想要访问的接口，需要传入请求对象
	response, err := client.InitOralProcess(request)
	// 处理异常
	fmt.Println(err)
	if _, ok := err.(*errors.TencentCloudSDKError); ok {
		fmt.Printf("An API error has returned: %s", err)
		return
	}
	// 非SDK异常，直接失败。实际代码中可以加入其他的处理。
	if err != nil {
		panic(err)
	}
	// 打印返回的json字符串
	fmt.Printf("%s", response.ToJsonString())

	Transclient, _ := soe.NewClient(credential, "ap-guangzhou", cpf)

	Transrequest := soe.NewTransmitOralProcessRequest()

	// 基本类型的设置。
	// 此接口允许设置返回的实例数量。此处指定为只返回一个。
	// SDK采用的是指针风格指定参数，即使对于基本类型你也需要用指针来对参数赋值。
	// SDK提供对基本类型的指针引用封装函数
	Transrequest.SeqId = common.Int64Ptr(1)
	Transrequest.IsEnd = common.Int64Ptr(1)
	Transrequest.SessionId = common.StringPtr(ids)
	Transrequest.VoiceFileType = common.Int64Ptr(1)
	Transrequest.VoiceEncodeType = common.Int64Ptr(1)
	// 使用json字符串设置一个request，注意这里实际是更新request，上述字段将会被保留，
	// 如果需要一个全新的request，soe.TransmitOralProcessRequest()创建。

	// userVoiceData := base64.StdEncoding.EncodeToString([]byte("智聆口语评测"))

	// 设置base64加密后的语音数据
	Transrequest.UserVoiceData = common.StringPtr(sEnc)

	// 通过client对象调用想要访问的接口，需要传入请求对象
	Transrequest.SetHttpMethod("POST")
	Transresponse, Transerr := Transclient.TransmitOralProcess(Transrequest)
	// 处理异常
	if _, ok := Transerr.(*errors.TencentCloudSDKError); ok {
		fmt.Printf("An API error has returned: %s", err)
		return
	}
	// 非SDK异常，直接失败。实际代码中可以加入其他的处理。
	if Transerr != nil {
		//panic(err)
	}
	// 打印返回的json字符串
	b, _ := json.Marshal(Transresponse.Response)
	fmt.Printf("%s", b)
}
```
#### 关键词评测
[KeywordEvaluate](https://cloud.tencent.com/document/api/884/35587) 接口使用示例：
```
package main

import (
	b64 "encoding/base64"
	"fmt"
	uuid "github.com/satori/go.uuid"
	"io/ioutil"

	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/errors"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile"
	soe "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/soe/v20180724"
)

func main() {
	//文件转base64
	dat, err := ioutil.ReadFile("") //本地音频文件地址
	sEnc := b64.StdEncoding.EncodeToString(dat)
	fmt.Println(sEnc)
	// 获取uuid
	id := uuid.NewV4()
	ids := id.String()

	// 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey,此处还需注意密钥对的保密
	// 密钥可前往https://console.cloud.tencent.com/cam/capi网站进行获取
	credential := common.NewCredential(
		"",
		"",
	)
	// 实例化一个client选项，可选的，没有特殊需求可以跳过
	cpf := profile.NewClientProfile()
	cpf.HttpProfile.Endpoint = "soe.tencentcloudapi.com"
	// 实例化要请求产品的client对象,clientProfile是可选的
	client, _ := soe.NewClient(credential, "", cpf)

	// 实例化一个请求对象,每个接口都会对应一个request对象
	request := soe.NewKeywordEvaluateRequest()

	request.SeqId = common.Uint64Ptr(1)
	request.IsEnd = common.Uint64Ptr(1)
	request.VoiceFileType = common.Uint64Ptr(3)
	request.VoiceEncodeType = common.Uint64Ptr(1)
	request.UserVoiceData = common.StringPtr(sEnc)
	request.SessionId = common.StringPtr(ids)
	request.Keywords = []*soe.Keyword {
		&soe.Keyword {
			RefText: common.StringPtr("hello"),
			EvalMode: common.Uint64Ptr(0),
			ServerType: common.Uint64Ptr(0),
			ScoreCoeff: common.Float64Ptr(1),
		},
		&soe.Keyword {
			RefText: common.StringPtr("我"),
			EvalMode: common.Uint64Ptr(0),
			ServerType: common.Uint64Ptr(1),
			ScoreCoeff: common.Float64Ptr(1),
		},
	}

	// 返回的resp是一个KeywordEvaluateResponse的实例，与请求对象对应
	response, err := client.KeywordEvaluate(request)
	if _, ok := err.(*errors.TencentCloudSDKError); ok {
		fmt.Printf("An API error has returned: %s", err)
		return
	}
	if err != nil {
		panic(err)
	}
	// 输出json格式的字符串回包
	fmt.Printf("%s", response.ToJsonString())
}

```

### 外部签名（不推荐）
使用 [TransmitOralProcessWithInit](https://cloud.tencent.com/document/api/884/32605) 接口演示：
1. 生成 curl
```
package main

import (
	"crypto/hmac"
	"crypto/sha256"
	"encoding/hex"
	"fmt"
	"time"
)

func sha256hex(s string) string {
	b := sha256.Sum256([]byte(s))
	return hex.EncodeToString(b[:])
}

func hmacsha256(s, key string) string {
	hashed := hmac.New(sha256.New, []byte(key))
	hashed.Write([]byte(s))
	return string(hashed.Sum(nil))
}

func main() {
	secretId := ""
	secretKey := ""
	host := "soe.tencentcloudapi.com"
	algorithm := "TC3-HMAC-SHA256"
	service := "soe"
	version := "2018-07-24"
	action := "TransmitOralProcessWithInit"
	region := "ap-guangzhou"
	var timestamp int64 = time.Now().Unix()
	//var timestamp int64 = 1551113065

	// step 1: build canonical request string
	httpRequestMethod := "POST"
	canonicalURI := "/"
	canonicalQueryString := ""
	canonicalHeaders := "content-type:application/json; charset=utf-8\n" + "host:" + host + "\n"
	signedHeaders := "content-type;host"

	payload := `{"SeqId": 1, "IsEnd": 1, "VoiceFileType": 3, "VoiceEncodeType": 1, "UserVoiceData": "//MoxAALuN4gAUkwAYQh1xWKzZAAMDZPRAKCRiYoJEEP/c4jHPJk0zAGA02ghGPERnaPZARHP8f+BkQQ/CqjfIxQLhkl2RAz//MoxAwPgNqoAZp4ADtQSTWOF1F+AEmTEImdt6jsb6WhXxTCvtkfiVUSLYdfX7hHvulYVqRfAZ+XOecxF//ph/+HbmNezSs8//MoxAkO4Oq4y9pQACMIy2HqbczDokotX71inxey/+udQMhypprA6IdjTWZWb0/QeaAFihx9/dr6NrdmgLOhat/++GIFmkGq//MoxAgOOO7UAHvKcD4u3EwOF9XNMK99Nu9Malj/0ERAqKi6tqYOCnGMAYuPg4il3/+fNB4QBhqZkYLEFC36InsC0mtHtEHf//MoxAoNYPLQAIPScBN69jsHpVNf/FFkPLf/UQ5X6QoAgm+QLisHkaUGoJEMFc///21mX2f9aRil/+KtwSkZ0XEtUWAzE23n//MoxA8Q4OrAAHvecHuoXU9pmuMRsAAl5kxR+iGa25Xy5K5DZndk+5GjFi4ruA3Po3Y////6CJMIhNvYgUhIGXFlFdljblAF//MoxAYOOLcWXmrSTqAB3RCZhvPpqgorarEywEZfpMLiImr/EbP9oFSJ/tRkmWkyCqSB7////ZGIiBim4gD60h/bQ8PAPWCj//MoxAgNMK7dlGveTCGa8yD4Mq/3dFs2/HPQW1XSttIJyKLf22MNsUyxqRmPUuHgi0b////9eQ9wkusmAPBsncNhPkwKoUqn//MoxA4MyK7IAGteTC6OJRT0Ugvx6Ur7OCiUV3r9HnSoYlWVg6oBkf////vLEFNRFMnV8nAFvQwtRZv2MBA4/bybO662jmbd//MoxBUMWNrIAGvMcOK8QpNEgWIosuBaLtuJf9k8M////7UF2StBPfNK6hDgnRvqAyTP/SiQH8hU31/HJqzWg1N61Y0lmoYI//MoxB4NINbEAGvQcGCCb5XfJDJD///1PwmCwKnlG36HrNEa6iqFSihJgRArUoxkzNS9Nr7hnHzGj4peHNfx0dx3LDJ2SFjN//MoxCQMcMrEAIvMcFl0ir////A6xOIktb+mtyEzawnALISGYieXWnFQ5AFCGKxU3XkVteSTc2uUS0oUBAWA0eU+W/t/9QVD//MoxC0NKMa8KmIEcEDQPB2WBqDVr/8/52mU2Dx0NTL1rqQqpzzbAf/0iBIOu37LJ1HPQzcM7dkKXYXETT9ZXqET//UHZbrV//MoxDMMkN6QUNJEcCkoBAN01mbKkI1yPAyqjxXtZltKeAxYa4aAqf+eSGHFlLlKD6m2O9vnhi9qmO////s/+lVRTMnty4ke//MoxDsM0Dp4H1kQABcA/8JwUE/8ciCyT/8YceY5ETf/8RgchQJAcBKf/5OGEHIPMwJQTP//83QGHJdyTGHHmQP///yTJceB//MoxEIXmxqkAYdoAdL49B6EoTBLB4BaP////wtAwA80jQvqY+XDQvrKtXQiaPYkjALhtQTGjWUR4g9zGdfMjohS5vsRp3Xo//MoxB4UcuLQAYcoAb+onWzt9f+RhpFP7qevrbvcyIFMkVE+uYqgxxbzTrFaiZ27KGnYnMR+UYQwfHKYo78ih2r+1cO1qvRa//MoxAcNkp68AYIoAHv6P9ef7/qHBTqpfQWY1u230+YsSHE+2/2RH7SlnoAx0+tLJ/r6CcvMYWMVd9n66oKbdTGxwbruYXOO//MoxAsOchKQAYI4ACXC5rVY5PHD9jnod+arRqj5hL80xXnzl9f+sgPH/uPP/+3lHRircOlTv5Fm0l+qx+zHquq7CjCgJhQE//MoxAwNqSGQA8MQAEkzN/+hjPq1W//qygIlAICFKAnvBpZ0sWPCV1WCpU6DQ87/Ue6vyUGiwNVMQU1FMy45OS41VVVVVVVV", "SessionId": "test_1432543", "RefText": "bick sdfad", "WorkMode": 1, "EvalMode": 1, "ScoreCoeff": 1}`
	hashedRequestPayload := sha256hex(payload)
	canonicalRequest := fmt.Sprintf("%s\n%s\n%s\n%s\n%s\n%s",
		httpRequestMethod,
		canonicalURI,
		canonicalQueryString,
		canonicalHeaders,
		signedHeaders,
		hashedRequestPayload)
	fmt.Println(canonicalRequest)

	// step 2: build string to sign
	date := time.Unix(timestamp, 0).UTC().Format("2006-01-02")
	credentialScope := fmt.Sprintf("%s/%s/tc3_request", date, service)
	hashedCanonicalRequest := sha256hex(canonicalRequest)
	string2sign := fmt.Sprintf("%s\n%d\n%s\n%s",
		algorithm,
		timestamp,
		credentialScope,
		hashedCanonicalRequest)
	fmt.Println(string2sign)

	// step 3: sign string
	secretDate := hmacsha256(date, "TC3"+secretKey)
	secretService := hmacsha256(service, secretDate)
	secretSigning := hmacsha256("tc3_request", secretService)
	signature := hex.EncodeToString([]byte(hmacsha256(string2sign, secretSigning)))
	fmt.Println(signature)

	// step 4: build authorization
	authorization := fmt.Sprintf("%s Credential=%s/%s, SignedHeaders=%s, Signature=%s",
		algorithm,
		secretId,
		credentialScope,
		signedHeaders,
		signature)
	fmt.Println(authorization)

	curl := fmt.Sprintf(`curl -X POST https://%s\
 -H "Authorization: %s"\
 -H "Content-Type: application/json; charset=utf-8"\
 -H "Host: %s" -H "X-TC-Action: %s"\
 -H "X-TC-Timestamp: %d"\
 -H "X-TC-Version: %s"\
 -H "X-TC-Region: %s"\
 -d '%s'`, host, authorization, host, action, timestamp, version, region, payload)
	fmt.Println(curl)
}
```

2. 根据签名信息，使用进行调用
```
package main

import (
  "fmt"
  "strings"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://soe.tencentcloudapi.com"
  method := "POST"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Authorization", authorization)
  req.Header.Add("Content-Type", "application/json; charset=utf-8")
  req.Header.Add("Host", "soe.tencentcloudapi.com")
  req.Header.Add("X-TC-Action", "TransmitOralProcessWithInit")
  req.Header.Add("X-TC-Timestamp", timestamp)
  req.Header.Add("X-TC-Version", "2018-07-24")
  req.Header.Add("X-TC-Region", "ap-guangzhou")

  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer res.Body.Close()

  body, err := ioutil.ReadAll(res.Body)
  if err != nil {
    fmt.Println(err)
    return
  }
  fmt.Println(string(body))
}
```

## 参数说明
### 请求参数说明

| 接口名称 | 接口功能 | 
|---------|---------|
| [TransmitOralProcessWithInit](https://cloud.tencent.com/document/api/884/32605) 	| 发音数据传输接口附带初始化过程（常用实践）| 
| [InitOralProcess](https://cloud.tencent.com/document/api/884/19319)	| 发音评估初始化| 
| [KeywordEvaluate](https://cloud.tencent.com/document/api/884/35587) 	| 关键词评测| 
|[TransmitOralProcess](https://cloud.tencent.com/document/api/884/19318)	|发音数据传输接口|
 
### 返回结果说明
参考 API 文档 [数据结构](https://cloud.tencent.com/document/api/884/19320)。

## 错误码
参考 API 文档 [错误码](https://cloud.tencent.com/document/api/884/30658)。

## 常见问题
参考 [常见问题](https://cloud.tencent.com/document/product/884/32593)。 


