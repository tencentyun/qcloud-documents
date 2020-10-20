## 简介
* 欢迎使用腾讯云开发者工具套件（SDK）3.0，SDK 3.0 是云 API 3.0 平台的配套工具。SDK 3.0 实现了统一化，各个语言版本的 SDK 具备使用方法相同、接口调用方式相同、错误码和返回包格式相同等优点。
* 本文以 GO SDK 3.0 为例，介绍如何使用、调试并接入腾讯云产品 API。
* 目前已支持云服务器 CVM、私有网络 VPC 、云硬盘 CBS 等 [腾讯云产品](https://cloud.tencent.com/document/sdk/Description)，后续会支持其他云产品接入。

## 依赖环境

* Go 1.9版本及以上。
* 获取安全凭证。安全凭证包含 SecretId 及 SecretKey 两部分。SecretId 用于标识 API 调用者的身份，SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥。前往 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面，即可进行获取，如下图所示：
![](https://main.qcloudimg.com/raw/78145f9e6a830a188304991552a5c614.png)
>!**您的安全凭证代表您的账号身份和所拥有的权限，等同于您的登录密码，切勿泄露他人。**
* 获取调用地址。调用地址（endpoint）一般形式为`*.tencentcloudapi.com`，产品的调用地址有一定区别，例如，云服务器的调用地址为`cvm.tencentcloudapi.com`。具体调用地址可参考对应产品的 [API 文档](https://cloud.tencent.com/document/api)。

## 安装 SDK

### 通过 go get 安装（推荐）

推荐使用语言自带的工具安装 SDK：打开 cmd 命令窗口：
```
go get -u github.com/tencentcloud/tencentcloud-sdk-go
```

## 使用 SDK
每个接口都有一个对应的 Request 结构和一个 Response 结构。例如，云服务器的查询实例列表接口 DescribeInstances 有对应的请求结构体 DescribeInstancesRequest 和返回结构体 DescribeInstancesResponse。

下面以云服务器查询实例列表接口为例，介绍 SDK 的基础用法。出于演示目的，有一些非必要的内容也在示例中，以尽量展示 SDK 常用的功能，但也显得臃肿，在实际编写代码使用 SDK 的时候，应尽量简化。


### 示例1：查询可用区（DescribeZones）

```go
package main

import (
	"fmt"
	"os"

	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/errors"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile"
	cvm "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cvm/v20170312"
)

func main() {
	// 实例化一个认证对象，入参需要传入腾讯云账户 secretId、secretKey
	// 这里采用的是从环境变量读取的方式，需要在环境变量中先设置这两个值
	credential := common.NewCredential("secretId", "secretKey")

	// 实例化一个客户端配置对象，可以指定超时时间等配置
	cpf := profile.NewClientProfile()
	cpf.HttpProfile.ReqMethod = "GET"
	cpf.HttpProfile.ReqTimeout = 5
	cpf.Debug = true

	// 实例化要请求产品（以 cvm 为例）的 client 对象
	client, _ := cvm.NewClient(credential, "ap-beijing", cpf)
	// 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
	request := cvm.NewDescribeZonesRequest()
	// 通过 client 对象调用想要访问的接口，需要传入请求对象
	response, err := client.DescribeZones(request)
	// 处理异常
	if _, ok := err.(*errors.TencentCloudSDKError); ok {
		fmt.Printf("An API error has returned: %s", err)
		return
	}
	// unexpected errors
	if err != nil {
		panic(err)
	}
	// 打印返回的 json 字符串
	fmt.Printf("%s", response.ToJsonString())
}
```

在 cmd 窗口执行即可：
```
go run test.go
```

>!**此过程会真实发送请求，请不要测试消费等接口，以免造成财产损失**。

### 示例2：查询实例列表（DescribeInstances）

```go
package main

import (
        "fmt"

        "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
        "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/errors"
        "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile"
        "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/regions"
        cvm "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cvm/v20170312"
)

func main() {
        // 必要步骤：
        // 实例化一个认证对象，入参需要传入腾讯云账户密钥对 secretId、secretKey。
        // 这里采用的是从环境变量读取的方式，需要在环境变量中先设置这两个值。
        // 您也可以直接在代码中写死密钥对，但是小心不要将代码复制、上传或者分享给他人，
        // 以免泄露密钥对危及您的财产安全。
        credential := common.NewCredential("secretId","secretKey")

        // 非必要步骤
        // 实例化一个客户端配置对象，可以指定超时时间等配置
        cpf := profile.NewClientProfile()
        // SDK 默认使用 POST 方法。
        // 如果您一定要使用 GET 方法，可以在这里设置。GET 方法无法处理一些较大的请求。
        // 如非必要请不要修改默认设置。
        //cpf.HttpProfile.ReqMethod = "GET"
        // SDK 有默认的超时时间，如非必要请不要修改默认设置。
        // 如有需要请在代码中查阅以获取最新的默认值。
        //cpf.HttpProfile.ReqTimeout = 10
        // SDK 会自动指定域名。通常是不需要特地指定域名的，但是如果您访问的是金融区的服务，
        // 则必须手动指定域名，例如云服务器的上海金融区域名：cvm.ap-shanghai-fsi.tencentcloudapi.com
        cpf.HttpProfile.Endpoint = "cvm.tencentcloudapi.com"
        // SDK 默认用 HmacSHA256 进行签名，它更安全但是会轻微降低性能。
        // 如非必要请不要修改默认设置。
        //cpf.SignMethod = "HmacSHA1"
        // SDK 默认用 zh-CN 调用返回中文。此外还可以设置 en-US 返回全英文。
        // 但大部分产品或接口并不支持全英文的返回。
        // 如非必要请不要修改默认设置。
        //cpf.Language = "en-US"

        // 实例化要请求产品（以 cvm 为例）的 client 对象
        // 第二个参数是地域信息，可以直接填写字符串 ap-guangzhou，或者引用预设的常量
        client, _ := cvm.NewClient(credential, regions.Guangzhou, cpf)
        // 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
        // 您可以直接查询 SDK 源码确定 DescribeInstancesRequest 有哪些属性可以设置，
        // 属性可能是基本类型，也可能引用了另一个数据结构。
        // 推荐使用 IDE 进行开发，可以方便的跳转查阅各个接口和数据结构的文档说明。
        request := cvm.NewDescribeInstancesRequest()

        // 基本类型的设置。
        // 此接口允许设置返回的实例数量。此处指定为只返回一个。
        // SDK 采用的是指针风格指定参数，即使对于基本类型您也需要用指针来对参数赋值。
        // SDK 提供对基本类型的指针引用封装函数
        request.Limit = common.Int64Ptr(1)

        // 数组类型的设置。
        // 此接口允许指定实例 ID 进行过滤，但是由于和接下来要演示的 Filter 参数冲突，先注释掉。
        // request.InstanceIds = common.StringPtrs([]string{"ins-r8hr2upy"})

        // 复杂对象的设置。
        // 在这个接口中，Filters 是数组，数组的元素是复杂对象 Filter，Filter 的成员 Values 是 string 数组。
        request.Filters = []*cvm.Filter{
            &cvm.Filter{
                Name: common.StringPtr("zone"),
                Values: common.StringPtrs([]string{"ap-guangzhou-1"}),
            },
        }

        // 使用 json 字符串设置一个 request，注意这里实际是更新 request，即 Limit=1 将会被保留，
        // 而过滤条件的 zone 将会变为 ap-guangzhou-2。
        // 如果需要一个全新的 request，则需要用 cvm.NewDescribeInstancesRequest() 创建。
        err := request.FromJsonString(`{"Filters":[{"Name":"zone","Values":["ap-guangzhou-2"]}]}`)
        if err != nil {
                panic(err)
        }
        // 通过 client 对象调用想要访问的接口，需要传入请求对象
        response, err := client.DescribeInstances(request)
        // 处理异常
        if _, ok := err.(*errors.TencentCloudSDKError); ok {
                fmt.Printf("An API error has returned: %s", err)
                return
        }
        // 非 SDK 异常，直接失败。实际代码中可以加入其他的处理。
        if err != nil {
                panic(err)
        }
        // 打印返回的 json 字符串
        fmt.Printf("%s", response.ToJsonString())
}
```

### 更多示例

您可以在 [github](https://github.com/tencentcloud/tencentcloud-sdk-go) 中的`examples`目录下获取更多详细的示例。


## 相关配置

### 代理

如果是有代理的环境下，需要设置系统环境变量`https_proxy`，否则可能无法正常调用，抛出连接超时的异常。

### 忽略服务器证书校验

虽然使用 SDK 调用公有云服务时，必须校验服务器证书，以识别他人伪装的服务器，确保请求的安全。但某些极端情况下，例如测试时，您可能会需要忽略自签名的服务器证书。以下是其中一种可能的方法：

```
import "crypto/tls"
...
    client, _ := cvm.NewClient(credential, regions.Guangzhou, cpf)
    tr := &http.Transport{
        TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
    }
    client.WithHttpTransport(tr)
...
```

>!除非您知道自己在进行何种操作，并明白由此带来的风险，否则不要尝试关闭服务器证书校验。



## 常见问题

### import 导包失败
例如报错：`imported and not used: "os"`，说明“ os ”这个包并未在代码中使用到，去掉即可。
