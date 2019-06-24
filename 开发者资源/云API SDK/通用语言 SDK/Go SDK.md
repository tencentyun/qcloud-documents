## 简介
欢迎使用腾讯云开发者工具套件（SDK）3.0，SDK3.0 是云 API3.0 平台的配套工具。后续所有的云服务产品都会接入进来。新版 SDK 实现了统一化，具有各个语言版本的 SDK 使用方法相同，接口调用方式相同，统一的错误码和返回包格式这些优点。
为方便 GO 开发者调试和接入腾讯云产品 API，这里向您介绍适用于 GO 的腾讯云开发工具包，并提供首次使用开发工具包的简单示例。让您快速获取腾讯云 GO SDK 并开始调用。

## 支持 3.0 版本的产品列表

SDK3.0支持全部 API3.0下的产品，本列表可能滞后于实际代码，如有疑问请咨询具体的产品。

<table>
  <tr>
<td><a href="https://cloud.tencent.com/document/api/213/15689">云服务器</a></td>
<td><a href="https://cloud.tencent.com/document/api/386/18637">黑石物理服务器</a></td>
<td><a href="https://cloud.tencent.com/document/api/362/15634">云硬盘</a></td>
<td><a href="https://cloud.tencent.com/document/api/457/31853">容器服务</a></td>
<td><a href="https://cloud.tencent.com/document/api/858/17761">容器实例服务</a></td>
</tr>
<tr>
 <td><a href="https://cloud.tencent.com/document/api/377/20423">弹性伸缩</a></td>
  <td><a href="https://cloud.tencent.com/document/api/583/17235">无服务器云函数</a></td>
  <td><a href="https://cloud.tencent.com/document/api/599/15880">批量计算</a></td>
  <td><a href="https://cloud.tencent.com/document/api/214/30667">负载均衡</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/15755">私有网络</a></td>
  </tr>
  <tr>
 <td><a href="https://cloud.tencent.com/document/api/216/18404">专线接入</a></td>
 <td><a href="https://cloud.tencent.com/document/api/236/15830">云数据库 MySQL</a></td>
    <td><a href="https://cloud.tencent.com/document/api/239/20002">云数据库 Redis</a></td>
 <td><a href="https://cloud.tencent.com/document/api/240/31797">云数据库 MongoDB</a></td>
  <td><a href="https://cloud.tencent.com/document/api/571/18122">数据传输服务 DTS</a></td>
 </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/237/16144">云数据库 MariaDB</a></td>
<td><a href="https://cloud.tencent.com/document/api/557/16124">分布式数据库 DCDB</a></td>
 <td><a href="https://cloud.tencent.com/document/api/238/19927">云数据库 SQL Server</a></td>
  <td><a href="https://cloud.tencent.com/document/api/409/16761">云数据库 PostgreSQL</a></td>
   <td><a href="https://cloud.tencent.com/document/api/228/30974">内容分发网络</a></td>
   </tr>
   <tr>
<td><a href="https://cloud.tencent.com/document/api/296/19825">主机安全</a></td>
  <td><a href="https://cloud.tencent.com/document/api/692/16733">Web 漏洞扫描</a></td>
   <td><a href="https://cloud.tencent.com/document/api/283/17742">应用安全</a></td>
   <td><a href="https://cloud.tencent.com/document/api/266/31753">云点播</a></td>
     <td><a href="https://cloud.tencent.com/document/api/267/20456">云直播</a></td>
   </tr>
   <tr>
<td><a href="https://cloud.tencent.com/document/api/441/17362">智能语音服务</a></td>
 <td><a href="https://cloud.tencent.com/document/api/551/15612">机器翻译</a></td>
<td><a href="https://cloud.tencent.com/document/api/656/18281">催收机器人</a></td>
<td><a href="https://cloud.tencent.com/document/api/884/19310">智聆口语评测</a></td>
<td><a href="https://cloud.tencent.com/document/api/853/18384">腾讯优评</a></td>
 </tr>
<tr>
  <td><a href="https://cloud.tencent.com/document/api/845/30620">Elasticsearch Service</a></td>
<td><a href="https://cloud.tencent.com/document/api/634/19469">物联网通信</a></td>
<td><a href="https://cloud.tencent.com/document/api/663/19455">TBaaS</a></td>
<td><a href="https://cloud.tencent.com/document/api/248/30343">云监控</a></td>
 <td><a href="https://cloud.tencent.com/document/api/659/18591">迁移服务平台</a></td>
 </tr>
 <tr>
<td><a href="https://cloud.tencent.com/document/api/869/17778">电子合同服务</a></td>
 <td><a href="https://cloud.tencent.com/document/api/555/19170">计费相关</a></td>
 <td><a href="https://cloud.tencent.com/document/api/563/16034">渠道合作伙伴</a></td>
  <td><a href="https://cloud.tencent.com/document/api/1007/31320">人脸核身-云智慧眼</a></td>
   <td><a href="https://cloud.tencent.com/document/api/1013/31737">威胁情报云查</a></td>
  </tr>
  <tr>
 <td><a href="https://cloud.tencent.com/document/api/1012/31720">样本智能分析平台</a></td>
  <td><a href="https://cloud.tencent.com/document/api/1004/30607">数学作业批改</a></td>
   <td><a href="https://cloud.tencent.com/document/api/670/31052">人脸融合</a></td>
   <td><a href="https://cloud.tencent.com/document/api/867/32770">人脸识别</a></td>
<td><a href="https://cloud.tencent.com/document/api/1000/30698">数字版权管理</a></td>
   </tr>
  </table>


## API Explorer
[API Explorer](https://console.cloud.tencent.com/api/explorer) 提供了在线调用、签名验证、 SDK 代码生成和快速检索接口等能力，能显著降低使用云 API 的难度，推荐使用。

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
前往 [Github 代码托管地址](https://github.com/tencentcloud/tencentcloud-sdk-go) 或者 [快速下载地址](https://tencentcloud-sdk-1253896243.file.myqcloud.com/tencentcloud-sdk-go/tencentcloud-sdk-go.zip) 下载最新代码，解压后安装到 `$GOPATH/src/github.com/tencentcloud` 目录下。

## 示例
每个接口都有一个对应的 Request 结构和一个 Response 结构。例如查询可用区 DescribeZones 有对应的请求结构体 DescribeZonesRequest 和返回结构体 DescribeZonesResponse 。
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

        // 实例化要请求产品(以 CVM 为例)的 client 对象
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

## 更多示例

更多示例参见 [examples](https://github.com/TencentCloud/tencentcloud-sdk-go/tree/master/examples) 目录。对于复杂接口的 Request 初始化例子，可以参考 examples/cvm/v20170312/run_instances.go 。对于使用 JSON 字符串初始化 Request 的例子，可以参考 examples/cvm/v20170312/describe_instances.go 。
