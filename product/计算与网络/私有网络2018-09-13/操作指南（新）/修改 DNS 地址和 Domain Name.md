本文将介绍如何修改 VPC 名称、DNS 地址、Domain Name、标签等信息。

## 背景信息
动态主机设置协议（Dynamic Host Configuration Protocol，DHCP）是一种局域网的网络协议， 提供了将配置信息传递到 TCP / IP 网络服务器的标准。 
腾讯云私有网络内的云服务器支持 DHCP 协议，支持配置的 DHCP Options 字段包括：DNS 地址、Domain Name。您可在私有网络配置 DNS 地址和 Domain Name，该配置将对该私有网络下的所有云服务器生效。

>?
> - 2018年4月1日前创建的私有网络暂不支持 DHCP 特性，若您在控制台无法修改 DNS 地址和 Domain Name，即说明您的私有网络不支持该特性。
> - 配置修改后，对该私有网络内所有云服务器生效：
>  - 新建的云服务器：直接生效。
>  - 存量的云服务器：重启云服务器或重启网络服务生效。

## 操作步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在【私有网络】页面顶部，选择 VPC 所属地域。
3. 单击 VPC 名称旁的编辑图标，可对 VPC 的名称进行修改。
   ![](https://main.qcloudimg.com/raw/23b4b68055078a14515cc47d95e68c6f.png)
4. 单击 VPC ID，进入 VPC 详情的【基本信息】界面。
5. 分别单击如下编辑图标，可修改 DNS、Domain Name、标签参数。
   + DNS：DNS 服务器地址。
     + 腾讯云默认 DNS 为：183.60.83.19，183.60.82.98，如果不使用腾讯云默认 DNS，将无法使用内部服务，如windows 激活、NTP、YUM 等。
     + 目前 DNS 最多支持4个 IP，多个 IP 之间请用逗号隔开。
     + DNS 可以指定4个 IP，但某些操作系统可能无法支持4个 DNS 地址。
   + Domain Name：云服务器 hostname 后缀，例如 `example.com` 。最多支持60个字符，如无特殊需求，也可保持默认。
   + 标签：主要用于资源标识，以便后期管理，可根据实际情况选择设置，支持增、删多条标签。
   ![](https://main.qcloudimg.com/raw/b5b7934a8ff07585fd198e6f297b84fc.png)
