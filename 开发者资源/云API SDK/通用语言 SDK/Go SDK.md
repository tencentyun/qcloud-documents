## 简介
欢迎使用腾讯云软件开发工具集 ( SDK )，本 SDK 能帮助开发者使用 Go 语言便捷地调用包括云服务器、虚拟网络在内的云服务 API ，管理腾讯云的资源。
## 依赖环境
1. Go 1.9 版本及以上。
2. 使用相关产品前需要在腾讯云控制台已开通相应产品。
3. 在腾讯云控制台 [访问管理](https://console.cloud.tencent.com/cam/capi) 页面获取 SecretID 和 SecretKey 。

## 获取安装
安装 Go SDK 前，先获取安全凭证。在第一次使用云 API 之前，用户首先需要在腾讯云 [控制台](https://console.cloud.tencent.com/) 上申请安全凭证，安全凭证包括 SecretID 和 SecretKey, SecretID 是用于标识 API 调用者的身份，SecretKey 是用于加密签名字符串和服务器端验证签名字符串的密钥。SecretKey 必须严格保管，避免泄露。
### 通过源码安装
前往 [Github 代码托管地址](https://github.com/tencentcloud/tencentcloud-sdk-go) 下载最新代码，解压后安装到 `$GOPATH/src/github.com/tencentcloud` 目录下

## 示例
下面以查询可用区为例，介绍 SDK 的基础用法。
```
package main
import (
        "encoding/json"
        "fmt"
        "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
        "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/errors"
        "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile"
        cvm "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cvm/v20170312"
)
func main() {
        credential := common.NewCredential(
                "your-secret-id",
                "your-secret-key,
        )
        cpf := profile.NewClientProfile()
        cpf.HttpProfile.ReqMethod = "GET"
        cpf.HttpProfile.ReqTimeout = 5
        cpf.HttpProfile.Endpoint = "cvm.ap-guangzhou.tencentcloudapi.com"
        cpf.SignMethod = "HmacSHA1"
        client, _ := cvm.NewClient(credential, "ap-beijing", cpf)
        request := cvm.NewDescribeZonesRequest()
        // get response structure
        response, err := client.DescribeZones(request)
        // API errors
        if _, ok := err.(*errors.TencentCloudSDKError); ok {
                fmt.Printf("An API error has returned: %s", err)
                return
        }
        // unexpected errors
        if err != nil {
                panic(err)
        }
        b, _ := json.Marshal(response.Response)
        fmt.Printf("%s", b)
}
```