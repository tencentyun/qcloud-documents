## 简介
- 欢迎使用腾讯云开发者工具套件（SDK），此 SDK 是云 API 3.0 平台的配套开发工具。
- 本文以 GO SDK 3.0 为例，介绍如何使用、调试并接入腾讯云产品 API。
- 目前已支持云服务器 CVM、私有网络 VPC 、云硬盘 CBS 等 [腾讯云产品](https://cloud.tencent.com/document/sdk/Description)，后续会支持其他云产品接入。

## 依赖环境

- Go 1.9 版本及以上（如使用 go mod 需要 Go 1.14）。
- 部分产品需要在腾讯云控制台开通后，才能正常调用此产品的接口。
- 在腾讯云控制台 [访问管理](https://console.cloud.tencent.com/cam/capi) 页面获取密钥 SecretID 和 SecretKey，请务必妥善保管，或者使用更安全的临时安全凭证。


## 安装 SDK

### 通过 go get 安装（推荐）
推荐使用腾讯云镜像加速下载：

- Linux 或 MacOS：
```bash
export GOPROXY=https://mirrors.tencent.com/go/
```

- Windows：
```cmd
set GOPROXY=https://mirrors.tencent.com/go/
```

### 按需安装（推荐）
>!
>- 此安装方式仅支持使用 **Go Modules** 模式进行依赖管理，即环境变量 `GO111MODULE=auto`或者`GO111MODULE=on`, 并且在您的项目中执行了 `go mod init xxx`。
>- 为了支持 go mod，SDK 版本号从 v3.x 降到了 v1.x。并于2021.05.10移除了所有`v3.0.*`和`3.0.*`的tag，如需追溯以前的tag，请参考项目根目录下的 `commit2tag` 文件。

v1.0.170 后可以按照产品下载，您只需下载基础包和对应的产品包（如 CVM）即可，不需要下载全部的产品，从而加快您构建镜像或者编译的速度：

1. 安装公共基础包：
```bash
go get -v -u github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common
```

2. 安装对应的产品包（如 CVM）：
```bash
go get -v -u github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cvm
```



### 通过源码安装

1. 前往代码托管地址 [Github](https://github.com/tencentcloud/tencentcloud-sdk-go) 或者 [Gitee](https://gitee.com/tencentcloud/tencentcloud-sdk-go) 下载最新代码。
2. 解压后安装到 `$GOPATH/src/github.com/tencentcloud` 目录下。


## 使用 SDK 

每个接口都有一个对应的 Request 结构和一个 Response 结构。例如云服务器的查询实例列表接口 DescribeInstances 有对应的请求结构体 DescribeInstancesRequest 和返回结构体 DescribeInstancesResponse 。

下面以云服务器查询实例列表接口为例，介绍 SDK 的基础用法。

<dx-tabs>
::: 简化版
```go
package main

import (
	"fmt"
    "os"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/errors"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/regions"
	cvm "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cvm/v20170312"
)

func main() {
    // 硬编码密钥到代码中有可能随代码泄露而暴露，有安全隐患，并不推荐。
    // 为了保护密钥安全，建议将密钥设置在环境变量中或者配置文件中，请参考本文凭证管理章节。
    // credential := common.NewCredential("SecretId", "SecretKey")
    credential := common.NewCredential(
        os.Getenv("TENCENTCLOUD_SECRET_ID"),
        os.Getenv("TENCENTCLOUD_SECRET_KEY"),
    )
	client, _ := cvm.NewClient(credential, regions.Guangzhou, profile.NewClientProfile())

	request := cvm.NewDescribeInstancesRequest()
	response, err := client.DescribeInstances(request)

	if _, ok := err.(*errors.TencentCloudSDKError); ok {
		fmt.Printf("An API error has returned: %s", err)
		return
	}
	if err != nil {
		panic(err)
	}
	fmt.Printf("%s\n", response.ToJsonString())
}
```
:::
::: 详细版
```go
package main

import (
	"fmt"
    "os"

	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/errors"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/regions"
	cvm "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cvm/v20170312"
)

func main() {
        // 必要步骤：
        // 实例化一个认证对象，入参需要传入腾讯云账户密钥对 SecretId，SecretKey。
        // 硬编码密钥到代码中有可能随代码泄露而暴露，有安全隐患，并不推荐。
        // 为了保护密钥安全，建议将密钥设置在环境变量中或者配置文件中，请参考本文凭证管理章节。
        // credential := common.NewCredential("SecretId", "SecretKey")
        credential := common.NewCredential(
            os.Getenv("TENCENTCLOUD_SECRET_ID"),
            os.Getenv("TENCENTCLOUD_SECRET_KEY"),
        )

        // 非必要步骤
        // 实例化一个客户端配置对象，可以指定超时时间等配置
        cpf := profile.NewClientProfile()
        // SDK默认使用POST方法。
        // 如果您一定要使用GET方法，可以在这里设置。GET方法无法处理一些较大的请求。
        // 如非必要请不要修改默认设置。
        cpf.HttpProfile.ReqMethod = "POST"
        // SDK有默认的超时时间，如非必要请不要修改默认设置。
        // 如有需要请在代码中查阅以获取最新的默认值。
        cpf.HttpProfile.ReqTimeout = 30
        // SDK会自动指定域名。通常是不需要特地指定域名的，但是如果您访问的是金融区的服务，
        // 则必须手动指定域名，例如云服务器的上海金融区域名： cvm.ap-shanghai-fsi.tencentcloudapi.com
        cpf.HttpProfile.Endpoint = "cvm.tencentcloudapi.com"
        // SDK默认用TC3-HMAC-SHA256进行签名，它更安全但是会轻微降低性能。
        // 如非必要请不要修改默认设置。
        cpf.SignMethod = "TC3-HMAC-SHA256"
        // SDK 默认用 zh-CN 调用返回中文。此外还可以设置 en-US 返回全英文。
        // 但大部分产品或接口并不支持全英文的返回。
        // 如非必要请不要修改默认设置。
        cpf.Language = "en-US"
        //打印日志，默认是false
        // cpf.Debug = true


        // 实例化要请求产品(以cvm为例)的client对象
        // 第二个参数是地域信息，可以直接填写字符串ap-guangzhou，或者引用预设的常量
        client, _ := cvm.NewClient(credential, regions.Guangzhou, cpf)
        // 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
        // 您可以直接查询SDK源码确定DescribeInstancesRequest有哪些属性可以设置，
        // 属性可能是基本类型，也可能引用了另一个数据结构。
        // 推荐使用IDE进行开发，可以方便的跳转查阅各个接口和数据结构的文档说明。
        request := cvm.NewDescribeInstancesRequest()

        // 基本类型的设置。
        // 此接口允许设置返回的实例数量。此处指定为只返回一个。
        // SDK采用的是指针风格指定参数，即使对于基本类型您也需要用指针来对参数赋值。
        // SDK提供对基本类型的指针引用封装函数
        request.Limit = common.Int64Ptr(1)

        // 数组类型的设置。
        // 此接口允许指定实例 ID 进行过滤，但是由于和接下来要演示的 Filter 参数冲突，先注释掉。
        // request.InstanceIds = common.StringPtrs([]string{"ins-r8hr2upy"})

        // 复杂对象的设置。
        // 在这个接口中，Filters是数组，数组的元素是复杂对象Filter，Filter的成员Values是string数组。
        request.Filters = []*cvm.Filter{
            &cvm.Filter{
                Name: common.StringPtr("zone"),
                Values: common.StringPtrs([]string{"ap-guangzhou-1"}),
            },
        }

        // 通过client对象调用想要访问的接口，需要传入请求对象
        response, err := client.DescribeInstances(request)
        // 处理异常
        if _, ok := err.(*errors.TencentCloudSDKError); ok {
            fmt.Printf("An API error has returned: %s", err)
            return
        }
        // 非SDK异常，直接失败。实际代码中可以加入其他的处理。
        if err != nil {
            panic(err)
        }
        // 打印返回的json字符串
        fmt.Printf("%s\n", response.ToJsonString())
}
```
:::
</dx-tabs>

>? 出于演示的目的，有一些非必要的代码，例如对默认配置的修改，以尽量展示 SDK 的功能。在实际编写代码使用 SDK 的时候，建议尽量使用默认配置，酌情修改。
>

## 更多示例
更多示例参见 [examples](https://github.com/TencentCloud/tencentcloud-sdk-go/tree/master/examples) 目录。对于复杂接口的 Request 初始化例子，可以参考 [例一](https://github.com/TencentCloud/tencentcloud-sdk-go/blob/master/examples/cvm/v20170312/run_instances.go) 。对于使用 json 字符串初始化 Request 的例子，可以参考 [例二](https://github.com/TencentCloud/tencentcloud-sdk-go/blob/master/examples/cvm/v20170312/describe_instances.go) 。

## 相关配置

**如无特殊需要，建议您使用默认配置。**

在创建客户端前，如有需要，您可以通过修改 `profile.ClientProfile` 中字段的值进行一些配置。

```go
// 非必要步骤
// 实例化一个客户端配置对象，可以指定超时时间等配置
cpf := profile.NewClientProfile()
```

具体的配置项说明如下：

### 请求方式

SDK 默认使用 POST 方法。 如果您一定要使用 GET 方法，可以在这里设置。**GET 方法无法处理一些较大的请求**。
```go
cpf.HttpProfile.ReqMethod = "POST"
```

### 超时时间

SDK 有默认的超时时间，如非必要请不要修改默认设置。如有需要请在代码中查阅以获取最新的默认值。  
单位：秒
```go
cpf.HttpProfile.ReqTimeout = 30
```

### 指定域名

SDK 会自动指定域名。通常是不需要特地指定域名的，但是如果您访问的是金融区的服务，则必须手动指定域名，例如：云服务器的上海金融区域名为 `cvm.ap-shanghai-fsi.tencentcloudapi.com`。

```go
cpf.HttpProfile.Endpoint = "cvm.tencentcloudapi.com"
```

### 签名方式

SDK 默认用 `TC3-HMAC-SHA256` 进行签名，它更安全但是会轻微降低性能。

```go
cpf.SignMethod = "HmacSHA1"
```

### DEBUG 模式

DEBUG 模式会打印更详细的日志，当您需要进行详细的排查错误时可以开启。  
默认为 `false`

```go
cpf.Debug = true
```

### 禁用长连接（Keep-alive）

SDK 的每一个 client 默认使用长连接模式，即请求的头部 Connection 字段的值为 keep-alive。

如果您需要使用短连接，可以按照以下方式进行设置：

```go
...
    client, _ := cvm.NewClient(credential, regions.Guangzhou, cpf)
    tp := &http.Transport{
        DisableKeepAlives: true,
    }
    client.WithHttpTransport(tp)
...
```

设置后，则此 client 发出的每个请求头部的 Connection 字段的值为 close。


### 地域容灾

从 `v1.0.227`开始，腾讯云 GO SDK 支持地域容灾功能：

当请求满足以下条件时：

1. 失败次数 >= 5 次
2. 失败率 >= 75%

SDK 会自动将您请求的地域设置为备选地域。

相关设置如下：

```golang
    // 开启
    cpf.DisableRegionBreaker = false
    // 设置备用请求地址，不需要指定服务，SDK 会自动在头部加上服务名(如cvm)
    // 例如，设置为 ap-guangzhou.tencentcloudapi.com，则最终的请求为 cvm.ap-guangzhou.tencentcloudapi.com
    cpf.BackupEndpoint = "ap-guangzhou.tencentcloudapi.com"
```

此功能仅支持单个客户端的同步请求。

### 代理

如果是有代理的环境下，需要设置系统环境变量 `https_proxy` ，否则可能无法正常调用，抛出连接超时的异常。或者自定义 Transport 指定代理，通过 client.WithHttpTransport 覆盖默认配置。

### 开启 DNS 缓存

当前 GO SDK 总是会去请求 DNS 服务器，而没有使用到 nscd 的缓存，可以通过导出环境变量 `GODEBUG=netdns=cgo`，或者 `go build` 编译时指定参数`-tags 'netcgo'`控制读取 nscd 缓存。


### 忽略服务器证书校验

虽然使用 SDK 调用公有云服务时，必须校验服务器证书，以识破他人伪装的服务器，确保请求的安全。
但是某些极端情况下，例如测试时，您可能会需要忽略自签名的服务器证书。
以下是其中一种可能的方法：

```golang
import "crypto/tls"
...
    client, _ := cvm.NewClient(credential, regions.Guangzhou, cpf)
    tr := &http.Transport{
        TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
    }
    client.WithHttpTransport(tr)
...
```

>!除非您知道自己在做什么，并明白由此带来的风险，否则不要尝试关闭服务器证书校验。


## 凭证管理

从版本 `v1.0.217` 开始，腾讯云 GO SDK 支持以下几种方式进行凭证管理：

### 环境变量
默认读取环境变量 `TENCENTCLOUD_SECRET_ID` 和 `TENCENTCLOUD_SECRET_KEY` 获取 secretId 和 secretKey。
相关代码如下：

```go
provider := common.DefaultEnvProvider()
credential, err := provider.GetCredential()
```

### 配置文件

配置文件路径为：
1. 环境变量 `TENCENTCLOUD_CREDENTIALS_FILE` 所指定的路径
2. Linux or MacOS：`~/.tencentcloud/credentials`
3. Windows：`c:\Users\NAME\.tencentcloud\credentials`


配置文件格式如下：
```ini
[default]
secret_id = xxxxx
secret_key = xxxxx
```

相关代码如下：
```go
provider := common.DefaultProfileProvider()
credential, err := provider.GetCredential()
```

### 角色扮演

有关角色扮演的相关概念请参考 [腾讯云角色概述](https://cloud.tencent.com/document/product/598/19420)。

要使用此种方式，您必须在腾讯云访问管理控制台上创建了一个角色，具体创建过程请参考 [腾讯云角色创建](https://cloud.tencent.com/document/product/598/19381)。

在您拥有角色后，可以通过如下方式获取凭证：
```go
provider := common.DefaultRoleArnProvider(secretId, secretKey, roleArn)
credential, err := provider.GetCredential()
```

### 实例角色

有关实例角色的相关概念请参考 [腾讯云实例角色](https://cloud.tencent.com/document/product/213/47668)。

在您为实例绑定角色后，您可以在实例中访问相关元数据接口获取临时凭证。相关代码如下：

```go
provider := common.DefaultCvmRoleProvider()
credential, err := provider.GetCredential()
```

### 凭证提供链

腾讯云 GO SDK 提供了 凭证提供链，它会默认以 `环境变量->配置文件->实例角色` 的顺序尝试获取凭证，并返回第一个获取到的凭证。相关代码如下：

```go
provider := common.DefaultProviderChain()
credential, err := provider.GetCredential()
```

您也可以自定义自己的凭证提供链，从而改变其调用顺序：

```go
provider1 := common.DefaultCvmRoleProvider()
provider2 := common.DefaultEnvProvider()
customProviderChain := []common.Provider{provider1, provider2}
provider := common.NewProviderChain(customProviderChain)
credential, err := provider.GetCredential()
```

更详细的使用方式请参考示例：[使用ProviderChain](https://github.com/TencentCloud/tencentcloud-sdk-go/blob/master/testing/integration/provider_chain_test.go)

## 错误处理

从 `v1.0.181` 开始，腾讯云 Go SDK 会将各个产品的返回的错误码定义为常量，您可以直接调用处理，无需手动定义。如果您使用 IDE（如 Goland）进行开发，可以使用他们的代码提示功能直接选择。例如：

```go
...//Your other go code

// Handling errors
response, err := client.DescribeInstances(request)
if terr, ok := err.(*errors.TencentCloudSDKError); ok {
    code := terr.GetCode()
    if code == cvm.FAILEDOPERATION_ILLEGALTAGKEY{
        fmt.Printf("Handling error: FailedOperation.IllegalTagKey,%s", err)
    }else if code == cvm.UNAUTHORIZEDOPERATION{
        fmt.Printf("Handling error: UnauthorizedOperation,%s", err)
    }else{
        fmt.Printf("An API error has returned: %s", err)
    }
    return
}
...
```

同时，各个接口函数的注释部分也列出了此接口可能会返回的错误码，方便您进行处理：

```go
// DescribeInstances
// 本接口 (DescribeInstances) 用于查询一个或多个实例的详细信息。
//
// 
//
// * 可以根据实例`ID`、实例名称或者实例计费模式等信息来查询实例的详细信息。过滤信息详细请见过滤器`Filter`。
//
// * 如果参数为空，返回当前用户一定数量（`Limit`所指定的数量，默认为20）的实例。
//
// * 支持查询实例的最新操作（LatestOperation）以及最新操作状态(LatestOperationState)。
//
// 可能返回的错误码:
//  FAILEDOPERATION_ILLEGALTAGKEY = "FailedOperation.IllegalTagKey"
//  FAILEDOPERATION_ILLEGALTAGVALUE = "FailedOperation.IllegalTagValue"
//  FAILEDOPERATION_TAGKEYRESERVED = "FailedOperation.TagKeyReserved"
//  INTERNALSERVERERROR = "InternalServerError"
//  INVALIDFILTER = "InvalidFilter"
//  INVALIDFILTERVALUE_LIMITEXCEEDED = "InvalidFilterValue.LimitExceeded"
//  INVALIDHOSTID_MALFORMED = "InvalidHostId.Malformed"
//  INVALIDINSTANCEID_MALFORMED = "InvalidInstanceId.Malformed"
//  INVALIDPARAMETER = "InvalidParameter"
//  INVALIDPARAMETERVALUE = "InvalidParameterValue"
//  INVALIDPARAMETERVALUE_IPADDRESSMALFORMED = "InvalidParameterValue.IPAddressMalformed"
//  INVALIDPARAMETERVALUE_INVALIDIPFORMAT = "InvalidParameterValue.InvalidIpFormat"
//  INVALIDPARAMETERVALUE_INVALIDVAGUENAME = "InvalidParameterValue.InvalidVagueName"
//  INVALIDPARAMETERVALUE_LIMITEXCEEDED = "InvalidParameterValue.LimitExceeded"
//  INVALIDPARAMETERVALUE_SUBNETIDMALFORMED = "InvalidParameterValue.SubnetIdMalformed"
//  INVALIDPARAMETERVALUE_TAGKEYNOTFOUND = "InvalidParameterValue.TagKeyNotFound"
//  INVALIDPARAMETERVALUE_VPCIDMALFORMED = "InvalidParameterValue.VpcIdMalformed"
//  INVALIDSECURITYGROUPID_NOTFOUND = "InvalidSecurityGroupId.NotFound"
//  INVALIDSGID_MALFORMED = "InvalidSgId.Malformed"
//  INVALIDZONE_MISMATCHREGION = "InvalidZone.MismatchRegion"
//  RESOURCENOTFOUND_HPCCLUSTER = "ResourceNotFound.HpcCluster"
//  UNAUTHORIZEDOPERATION_INVALIDTOKEN = "UnauthorizedOperation.InvalidToken"
func (c *Client) DescribeInstances(request *DescribeInstancesRequest) (response *DescribeInstancesResponse, err error){
    ...
}
```

## Common Client

从  `v1.0.189` 开始，腾讯云 GO SDK 支持使用 `泛用型的 API 调用方式（Common Client）` 进行请求。您只需安装 `common` 包, 即可向任何产品发起调用。

>!您必须明确知道您调用接口的参数内容，否则会调用失败。

目前仅支持使用 POST 方式发送请求，且签名方法必须使用 签名方法 v3。

详细使用请参阅示例：[使用 Common Client 进行调用](https://github.com/TencentCloud/tencentcloud-sdk-go/blob/master/examples/common/common_client.go)。

### 自定义 Header

[RunInstancesRequest 示例](https://github.com/TencentCloud/tencentcloud-sdk-go/blob/master/examples/cvm/v20170312/run_instances.go)
```go
    request := cvm.NewRunInstancesRequest()
	request.SetHeader(map[string]string{
        "X-TC-TraceId": "ffe0c072-8a5d-4e17-8887-a8a60252abca",
    })
```

[CommonRequest 示例](https://github.com/TencentCloud/tencentcloud-sdk-go/blob/master/examples/common/common_client.go)
```go
    request := tchttp.NewCommonRequest("cvm", "2017-03-12", "DescribeZones")
    request.SetHeader(map[string]string{
        "X-TC-TraceId": "ffe0c072-8a5d-4e17-8887-a8a60252abca",
    })
```

### HTTP 代理
[DescribeInstances 示例](https://github.com/TencentCloud/tencentcloud-sdk-go/blob/master/examples/cvm/v20170312/describe_instances.go)
```go
    // with authentication
    clientProfile.HttpProfile.Proxy = "http://username:password@127.0.0.1:1080"
    // without authentication
    clientProfile.HttpProfile.Proxy = "http://127.0.0.1:1080"
```

## 请求重试

### 网络错误重试

当发生临时网络错误或超时时，SDK可以被配置为自动重试。默认不开启。
通过 `ClientProfile` 配置重试次数和重试间隔时间。

>?
>- 通过反射检查 `Request` 结构体是否存在 `ClientToken` 字段，存在该字段则认为是幂等请求。
>- 幂等请求才会在网络错误时自动重试，非幂等请求会抛出异常，防止请求多次重放造成结果不一致。

```golang
package main

import (
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/regions"
	cvm "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cvm/v20170312"
)

func main() {
	credential := common.NewCredential("secretId", "secretKey")
	prof := profile.NewClientProfile()
	prof.NetworkFailureMaxRetries = 3                               // 定义最大重试次数
	prof.NetworkFailureRetryDuration = profile.ExponentialBackoff   // 定义重试间隔时间
	client, _ := cvm.NewClient(credential, regions.Guangzhou, prof)

	// ...
}
```

更多用法参考 [测试文件](https://github.com/TencentCloud/tencentcloud-sdk-go/tree/master/tencentcloud/common/netretry_test.go)。

### 限频重试

当发生 API 限频时，SDK 可以被配置为自动重试。默认不开启。
通过 `ClientProfile` 配置重试次数和重试间隔时间。

```golang
package main

import (
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/regions"
	cvm "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cvm/v20170312"
)

func main() {
    // ...

	prof := profile.NewClientProfile()
	prof.RateLimitExceededMaxRetries = 3                               // 定义最大重试次数
	prof.RateLimitExceededRetryDuration = profile.ExponentialBackoff   // 定义重试间隔时间
	client, _ := cvm.NewClient(credential, regions.Guangzhou, prof)

	// ...
}
```

### 幂等标识符

当网络超时重试或限频重试开启时，会自动向请求中注入 `ClientToken` 参数（如果请求存在 `ClientToken` 字段且为空）。
当用户手动指定 `ClientToken` 时，会跳过注入流程。

>?注入的 `ClientToken` 在 `100000/s` 并发量以下提供全局唯一性。

## 支持产品列表

参见 [产品列表文档](https://github.com/TencentCloud/tencentcloud-sdk-go/blob/master/products.md)。
