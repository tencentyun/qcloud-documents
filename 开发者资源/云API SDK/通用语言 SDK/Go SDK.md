## 简介 
欢迎使用腾讯云开发者工具套件（SDK）3.0，SDK3.0 是云 API3.0 平台的配套工具。后续所有的云服务产品都会接入进来。新版 SDK 实现了统一化，具有各个语言版本的 SDK 使用方法相同，接口调用方式相同，统一的错误码和返回包格式这些优点。
为方便 GO 开发者调试和接入腾讯云产品 API，这里向您介绍适用于 GO 的腾讯云开发工具包，并提供首次使用开发工具包的简单示例。让您快速获取腾讯云 GO SDK 并开始调用。
## 依赖环境
1. Go 1.9 版本及以上，并设置好 GOPATH 等必须的环境变量。
2. 使用相关产品前需要在腾讯云 [控制台](https://console.cloud.tencent.com/) 已开通相应产品。
3. 在腾讯云控制台 [访问管理](https://console.cloud.tencent.com/cam/capi) 页面获取 SecretID 和 SecretKey 。

## 获取安装
安装 Go SDK 前，先获取安全凭证。在第一次使用云 API 之前，您首先需要在腾讯云控制台上申请安全凭证，安全凭证包括 SecretID 和 SecretKey，SecretID 是用于标识 API 调用者的身份，SecretKey 是用于加密签名字符串和服务器端验证签名字符串的密钥。SecretKey 必须严格保管，避免泄露。
### 通过 go get 安装（推荐）
推荐使用语言自带的工具安装 SDK ：
```
go get -u github.com/tencentcloud/tencentcloud-sdk-go
```
### 通过源码安装
前往 [Github 代码托管地址](https://github.com/tencentcloud/tencentcloud-sdk-go) 下载最新代码，解压后安装到 `$GOPATH/src/github.com/tencentcloud` 目录下。

## 示例
下面以查询可用区为例，介绍 SDK 的基础用法。
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
        // 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
        credential := common.NewCredential(
                "your-secret-id",
                "your-secret-key",
        )
        // 实例化一个客户端配置对象，可以指定超时时间等配置
        cpf := profile.NewClientProfile()
        cpf.HttpProfile.ReqMethod = "GET"
        cpf.HttpProfile.ReqTimeout = 5
        cpf.SignMethod = "HmacSHA1"
        // 实例化要请求产品(以cvm为例)的client对象
        client, _ := cvm.NewClient(credential, "ap-beijing", cpf)
        // 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
        request := cvm.NewDescribeZonesRequest()
        // 通过client对象调用想要访问的接口，需要传入请求对象
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
        // 打印返回的json字符串
        fmt.Printf("%s", response.ToJsonString())
}
```
