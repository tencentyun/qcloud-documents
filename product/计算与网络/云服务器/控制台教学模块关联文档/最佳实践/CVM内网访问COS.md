## 操作场景
本文介绍云服务器 CVM 访问对象存储 COS 时默认使用的访问方式及内网访问的判断方法，并提供了连通性测试示例。您可参考本文进一步了解 CVM 访问 COS 相关信息。

## 默认访问方式
腾讯云对象存储 COS 的访问域名使用了智能 DNS 解析，通过互联网在不同的运营商环境下，我们会检测并指向最优链路供您访问 COS。如果您在腾讯云内部署了服务用于访问 COS，则同地域范围内的访问将会自动被指向到内网地址，而跨地域暂不支持内网访问，默认将会解析到外网地址。
>!
>- 相同地域内腾讯云产品访问，将会自动使用内网连接，产生的内网流量不计费。因此选购腾讯云不同产品时，建议尽量选择相同地域，减少您的费用。
>- 公有云地域和金融云地域内网不互通。
>

## 操作步骤
### 内网访问判断方法
确认是否内网访问请参考如下方法：
以云服务器 CVM 访问 COS 为例，判断是否使用内网访问 COS ，可在 CVM 上使用 `nslookup` 命令解析 COS 域名，若返回内网 IP，则表明 CVM 和 COS 之间是内网访问，否则为外网访问。
1. 获取存储桶访问域名，并记录该地址。详情请参见 [存储桶概览](https://cloud.tencent.com/document/product/436/48921)。
2. 登录实例，并执行 nslookup 命令。假设 `examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com` 为目标存储桶地址，则执行以下命令：
```
nslookup examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com
```
返回如下图所示结果，其中`10.148.214.13`和`10.148.214.14`这两个 IP 就代表了是通过内网访问 COS。
>?内网 IP 地址一般形如`10.*.*.*`、`100.*.*.*` ，VPC 网络一般为`169.254.*.*` 等，这两种形式的 IP 都属于内网。
>
![](https://main.qcloudimg.com/raw/49a7d7429ec2a96d271f6a63926286ea.png)

### 测试连通性

#### 通过内网测试的说明
如果您通过同地域的 VPC 网络来访问 COS，则可能无法使用 ICMP 协议的 `ping` 或 `traceroute` 等工具来测试连通性。建议您使用基本连通测试中的 `telnet` 命令进行测试。
您亦可尝试使用 `psping` 或 `tcping` 等工具直接对访问域名的80端口进行时延测试，请在测试前确保已通过 `nslookup` 命令查询并确认访问域名已正确解析至内网地址。

#### 通过互联网测试的说明

由于通过互联网访问 COS 会经过运营商网络，运营商网络可能禁止您使用 ICMP 协议的 `ping` 或 `traceroute` 等工具来测试连通性，因此建议使用 TCP 协议的工具来测试连通性。
>!通过互联网访问可能受到多种网络环境的影响，如有访问不畅的情况，请排查本地网络链路或联系当地运营商进行反馈。
>
若您的运营商允许 ICMP 协议，您可以使用 `ping`、`traceroute` 或 `mtr` 工具来检视您的链路状况。运营商不允许使用 ICMP 协议，您可以使用 `psping`（Windows 环境，请前往微软官网下载）或 `tcping` （跨平台软件）等工具进行时延测试。


#### 基本连通测试示例
COS 使用了 HTTP 协议对外提供服务，您可使用最基本的 telnet 工具来对 COS 访问域名的80端口发起访问测试。

- 通过外网访问的示例如下：
```plaintext
telnet examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com 80
Trying 14.119.113.22...
Connected to gz.file.myqcloud.com.
Escape character is '^]'.
```
- 通过同地域的 CVM （基础网络）访问示例如下：
```plaintext
telnet examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com 80
Trying 10.148.214.14...
Connected to 10.148.214.14.
Escape character is '^]'.
```
- 通过同地域的 CVM （VPC 网络）访问示例如下：
```plaintext
telnet examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com 80
Trying 169.254.0.47....
Connected to 169.254.0.47.
Escape character is '^]'.
```
>?无论处于何种访问环境，命令返回 `Escape character is '^]'.` 字段则说明可成功连通。

