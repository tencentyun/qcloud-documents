## 简介

本文介绍如何实现跨账户访问云 HDFS（Cloud HDFS，CHDFS）。

在 CHDFS 的使用情景中，可能需要使用不同的主账户访问同一个 CHDFS，例如账户 B 的 EMR 集群访问账户 A 的 CHDFS。但在常用的 [云 HDFS 控制台](https://console.cloud.tencent.com/chdfs) 中不同主账户之间的权限组不能绑定对方的挂载点，无法实现跨账户访问。这时可以使用 [云 HDFS API](https://cloud.tencent.com/document/product/1105/51166)：

- CHDFS 提供功能全面的云 HDFS API，只需少量代码您就可以操作 CHDFS，并且云 API 允许将账户 B 的权限组绑定账户 A 的挂载点以此实现 CHDFS 的跨账户访问。
- 在绑定的过程中，挂载点是主要资源，**会鉴权调用方是否拥有操作挂载点 ID 的权限，而权限组 ID 不做鉴权**。

## 前提条件

- 账户 A 已创建好文件系统，详情请参考 [创建 CHDFS](https://cloud.tencent.com/document/product/1105/37234)。
- 账户 A 已创建好 [挂载点](https://cloud.tencent.com/document/product/1105/37237)。
![](https://qcloudimg.tencent-cloud.cn/raw/ad98739482417c5be912e13285eb4145.jpg)
- 账户 B 已创建好 [权限组](https://cloud.tencent.com/document/product/1105/37235) 和 [权限规则](https://cloud.tencent.com/document/product/1105/37236)。
![](https://qcloudimg.tencent-cloud.cn/raw/5cf1934cdc6367f108c4319d34167196.jpg)
- 账户 B 的 EMR 集群配置好 [CHDFS 环境](https://cloud.tencent.com/document/product/1105/36368)。

## 操作步骤

CHDFS 提供功能全面的 [云HDFS API](https://cloud.tencent.com/document/product/1105/51166)，通过云 HDFS API 可以实现 [绑定权限组列表](https://cloud.tencent.com/document/product/1105/51155)。本文以 Golang 代码为例，实现将账户 B 的权限组绑定账户 A 的挂载点。实行绑定动作的主体为账户 A 或拥有权限的 A 的子账户。

1. 在以下代码配置账户 A 的密钥、账户A的挂载点 ID、账户 B 的权限组 ID：
```go
package main

import (
        "fmt"

        "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
        "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/errors"
        "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile"
        chdfs "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/chdfs/v20201112"
)

func main() {
        // 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey,此处还需注意密钥对的保密
        // 密钥可前往https://console.cloud.tencent.com/cam/capi网站进行获取
        credential := common.NewCredential(
                "SecretId",
                "SecretKey",
        )
        // 实例化一个client选项，可选的，没有特殊需求可以跳过
        cpf := profile.NewClientProfile()
        cpf.HttpProfile.Endpoint = "chdfs.tencentcloudapi.com"
        // 实例化要请求产品的client对象,clientProfile是可选的
        client, _ := chdfs.NewClient(credential, "", cpf)

        // 实例化一个请求对象,每个接口都会对应一个request对象
        request := chdfs.NewAssociateAccessGroupsRequest()
        
  			//账户A的挂载点ID
        request.MountPointId = common.StringPtr("f4maxxxx-xxS3")
  			//账户B的权限组ID
        request.AccessGroupIds = common.StringPtrs([]string{ "ag-xxxxxzm" })

        // 返回的resp是一个AssociateAccessGroupsResponse的实例，与请求对象对应
        response, err := client.AssociateAccessGroups(request)
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
2. 运行代码后，再次查看账户 A 的挂载点，即可看到账户 B 的权限组成功绑定在本挂载点上。
![](https://qcloudimg.tencent-cloud.cn/raw/71259b5cbdd5a4012a0d3b13b3fbf3e1.jpg)
3. 在账户 B 的 EMR 集群机器中通过 `hadoop fs -ls` 命令查看到文件列表，即表示挂载成功。账户 B 可以访问账户 A 的 CHDFS，成功实现跨账户访问 CHDFS。
![](https://qcloudimg.tencent-cloud.cn/raw/141c44cf739af33980b8e44c7e1b183b.jpg)
若未通过云 API 执行上述绑定操作，在账户 B 的 EMR 集群中通过 `hadoop fs -ls` 命令则查看到访问文件列表失败，显示**“*Permisson denied: No access rules matched*”** 错误，账户 B 无法访问账户 A 的 CHDFS。
![](https://qcloudimg.tencent-cloud.cn/raw/786732c493c08ce11fe3ad8f2d046dd9.jpg)
