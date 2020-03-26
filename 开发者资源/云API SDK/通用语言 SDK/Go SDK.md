本文主要介绍适用于 GO 的腾讯云开发工具包，并提供首次使用开发工具包的简单示例，让 GO 开发者快速掌握如何调试和接入腾讯云产品 API。
支持 SDK 3.0 版本的云产品列表请参见 [SDK 简介](https://cloud.tencent.com/document/product/494/42698)。

## 依赖环境
- Go 1.9 版本及以上，并设置好 GOPATH 等必须的环境变量。
- 在访问管理控制台 >【[API密钥管理](https://console.cloud.tencent.com/cam/capi)】页面获取 SecretID 和 SecretKey。
 - SecretID 用于标识 API 调用者的身份。
 - SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥，**SecretKey 需妥善保管，避免泄露**。
- 获取调用地址（endpoint），endpoint 一般格式为`*.tencentcloudapi.com`，例如 CVM 的调用地址为`cvm.tencentcloudapi.com`，具体地址请参考各云产品说明。

## 获取安装

### 通过 go get 安装（推荐）
推荐使用语言自带的工具安装 SDK：
```
 go get -u github.com/tencentcloud/tencentcloud-sdk-go
```

### 通过源码安装
1. 前往 [Github 代码托管地址](https://github.com/tencentcloud/tencentcloud-sdk-go) 或者 [快速下载地址](https://tencentcloud-sdk-1253896243.file.myqcloud.com/tencentcloud-sdk-go/tencentcloud-sdk-go.zip) 下载最新代码。
2. 解压后安装到 `$GOPATH/src/github.com/tencentcloud` 目录下。

## 示例
每个接口都有一个对应的 Request 结构和一个 Response 结构。例如，查询可用区 DescribeZones 有对应的请求结构体 DescribeZonesRequest 和返回结构体 DescribeZonesResponse 。
本文以云服务器查询可用区为例，介绍 SDK 的基础用法，更多示例请参考 [examples 目录](https://github.com/TencentCloud/tencentcloud-sdk-go/tree/master/examples)。
>?对于复杂接口的 Request 初始化示例，可以参考 examples/cvm/v20170312/run_instances.go。对于使用 JSON 字符串初始化 Request 的示例，可以参考 examples/cvm/v20170312/describe_instances.go。


```
package main

import (
        "fmt"

        "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
        "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/errors"
        "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile"
        cvm "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cvm/v20170312"
)

func main() {
        // 实例化一个认证对象，入参需要传入腾讯云账户 secretId，secretKey
        credential := common.NewCredential(
                "your-secret-id",
                "your-secret-key",
        )

        // 实例化一个客户端配置对象，可以指定超时时间等配置
        cpf := profile.NewClientProfile()
        cpf.HttpProfile.ReqMethod = "GET"
        cpf.HttpProfile.ReqTimeout = 5
        cpf.SignMethod = "HmacSHA1"

        // 实例化要请求产品（以 CVM 为例）的 client 对象
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
        // 打印返回的 JSON 字符串
        fmt.Printf("%s", response.ToJsonString())
}
```

## 相关配置
### 代理
在有代理的环境下，需要设置系统环境变量 `https_proxy`，否则可能无法正常调用，抛出连接超时的异常。

### 开启 DNS 缓存
若 GO SDK 直接请求 DNS 服务器，而非使用 nscd 的缓存，您可以通过导出环境变量`GODEBUG=netdns=cgo`，或在`go build`编译时指定参数`-tags 'netcgo'`控制读取 nscd 缓存。

### 忽略服务器证书校验
使用 SDK 调用公有云服务时，必须校验服务器证书，以识破他人伪装的服务器，确保请求的安全。 
某些极端情况下，例如测试时，如果您需要忽略自签名的服务器证书，您可以采用以下方式：
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

>!请不要**轻易尝试关闭服务器证书校验**，除非您明白在做什么，并清楚由此带来的风险。
