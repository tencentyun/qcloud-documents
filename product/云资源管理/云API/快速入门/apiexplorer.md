[腾讯云 API Explorer 工具]( https://console.cloud.tencent.com/api/explorer) 是一款自动化工具，目前已支持云服务器 CVM、私有网络 VPC、云硬盘 CBS 等 [腾讯云产品](https://cloud.tencent.com/product) 的 API 接口调用自动化。可实现自动生成 Java、Python、Node.js、PHP、GO 及 .NET 语言的 SDK 代码、在线调用、发送真实请求及签名串自动生成等功能，降低了 SDK 的使用难度。



## API Explorer 工具详细介绍

本文将以 API Explorer 工具整体页面从左至右顺序依次详细介绍。如下图所示：
![](https://main.qcloudimg.com/raw/6aab26c6bdbfca74549c30e2bf4883c7.png)
1. **产品区域**：目前已支持的所有产品。
2. **产品接口区域**：当前产品下已支持的所有功能接口。
3. **接口名**：所选择的接口名。
4. **产品版本**：各产品版本有一定区别，详情请参见各接口文档。图中为云服务器接口版本 2017-03-12。
5. **密钥对（SecretId、SecretKey）**：输入账户的安全凭证，可单击【查看密钥】进行获取。
>!密钥代表您的账号身份和所拥有的权限，等同于您的登录密码，切勿泄露他人。
>
6. **更多选项**：单击【更多选项】，其中包含 Timestamp、Token、请求方式及 Endpoint。各参数说明如下：
 - **Timestamp（仅在验证签名串生成时有效）**：当前 UNIX 时间戳，精确到秒，用于记录发起 API 请求的时间。
   Timestamp 必须为当前系统时间，且需确保系统时间与标准时间同步，若相差超过5分钟则会发生请求失败。若长时间不和标准时间同步，则可能导致运行一段时间后，请求失败并返回签名过期错误。
 - **Token**：用于认证用户身份。各产品对该参数要求可能有一定区别，如有需要会注明获取方式，详情请参见各接口文档。
 - **请求方式（仅在验证签名串生成时有效）**：默认为 POST 请求，请结合接口文档进行选择。
 - **Endpoint（请求域名）**：选择接入地域，默认就近接入。
7. **接口所需参数**：仅展示接口所需参数，您可勾选“只看必填参数”进行筛选。具体参数说明可通过选择右侧的【参数说明】进行查看。
8. **功能区**：
 - **代码生成**：可通过此功能自动生成多语言版本代码，降低使用难度。
 - **在线调用**：在填写参数后，选择【发送请求】，系统会发送您在左侧填写的参数到对应的接口。该操作等同于真实操作，同时系统会展示请求结果、响应头等相关信息。
 - **签名串生成**：可通过此功能自动生成签名串，默认使用 API 3.0 v3 版本，您可按需选择其他版本。如下图所示：
   ![](https://main.qcloudimg.com/raw/36b7cae1293d8b924c9c32048078e5a6.png)
9. **TCCLI 命令行生成**：可根据用户左侧填写的参数自动生成命令行参数（此处采用复杂类型点连接方式调用的命令行），用户可选择自行复制其内容到 TCCLI 工具中使用。
10. **子功能区**：可切换语言版本，生成对应代码。
11. **SDK 使用说明**：如需了解 SDK 更多信息，例如所需环境及调用示例，可查阅相应的 SDK 使用说明。
12. **响应区**：此处根据8和10的选择不同，展示生成 SDK 调用代码、在线调用结果等响应信息。


## 调用接口

本文以 [查询可用区列表](https://cloud.tencent.com/document/product/213/15707) 接口为例，使用 API Explorer 工具进行调用：

1. 获取个人密钥（SecretId、SecretKey），并填入对应位置。
2. 填写所需参数，可选择右侧功能区中的【参数说明】查看接口具体参数信息。
3. 选择右侧功能区中的【在线调用】>【发送请求】，即可在响应区查看请求结果。如下图所示：
   ![](https://main.qcloudimg.com/raw/d27e5b4d17bb651b0edb543af955334b.png)



## 生成签名串

本文以 [查询可用区列表](https://cloud.tencent.com/document/product/213/15707) 接口为例，使用 API Explorer 工具进行签名串生成：

1. 获取个人密钥（SecretId、SecretKey），并填入对应位置。
2. （可选）填写签名需参数，您可按需进行填写。若不填写，系统在生成签名串时会自动输入签名所需参数。
3. 填写接口所属参数，可选择右侧功能区中的【参数说明】查看接口具体参数信息。
4. 选择右侧功能区中的【签名串生成】>【生成签名】，即可在响应区查看签名的详细步骤与结果。如下图所示：
   ![](https://main.qcloudimg.com/raw/8c2ad278347d6d6e54cc6cbb58155530.png)

## 相关问题

### 使用工具如何验证 API 签名

当您遇到如下报错信息时，可使用 API Explorer 工具进行验证：

```
[TencentCloudSDKException] code:AuthFailure.SecretIdNotFound message:The SecretId is not found, please ensure that your SecretId is correct. requestId:234a93fe-9024-488e-87a8-48e4f3c3548e
```

1. 将参数填写在 API Explorer 工具中，Timestamp 等可变参数请与所需验证的签名（API 错误签名）使用的参数保持一致，并选择功能区的【签名串生成】>【生成签名】。如下图所示：
   ![](https://main.qcloudimg.com/raw/aea834e5c57957c59a1e5471e82ff520.png)
2. 在响应区获得签名步骤及结果后，即可进行前后数据对比。


### 签名错误

如您在签名过程中出现错误，则可能收到以下签名失败的错误代码，请对应实际情况进行处理：

<table>
<tr>
<th>错误代码</th><th>错误描述</th>
</tr>
<tr>
<td><code>AuthFailure.SignatureExpire</code></td><td>签名过期。</td>
</tr>
<tr>
<td><code>AuthFailure.SecretIdNotFound</code></td><td>密钥不存在。</td>
</tr>
<tr>
<td><code>AuthFailure.SignatureFailure</code></td><td>签名错误。</td>
</tr>
<tr>
<td><code>AuthFailure.TokenFailure</code></td><td>token 错误。</td>
</tr>
<tr>
<td><code>AuthFailure.InvalidSecretId</code></td><td>密钥非法（不是云 API 密钥类型）。</td>
</tr>
</table>




## 联系我们

- 若您在使用过程中发现问题，可通过选择功能区【问题反馈】进行反馈。
- 您也可以单击右下角的<img src="https://main.qcloudimg.com/raw/0a0610eb176a4e0d07eb9b902381c5fc.png" style="margin:-6px 0px">，在“帮助中心”查询相关信息。
