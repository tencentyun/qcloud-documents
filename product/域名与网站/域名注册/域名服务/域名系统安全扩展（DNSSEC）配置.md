## 操作场景
域名系统安全扩展（DNSSEC）是域名系统（DNS）的一项功能，用于确定源域名可靠性的数字签名。DNSSEC 验证可以保护 DNS 数据，也可使这类数据在 DNS 以外的应用程序中值得信赖，因此，为域名部署 DNSSEC，有利于互联网安全，并可加强应对攻击能力。
本文为您介绍如何在腾讯云域名注册控制台添加及同步 DNSSEC 记录。

## 前提条件
已登录 [腾讯云域名注册控制台](https://console.cloud.tencent.com/domain)，并进入 “我的域名” 管理页面。
>!.中国、.cn、.ac.cn、.com.cn、.net.com 的中文域名后缀不支持添加 DNSSEC 记录。

## 操作指南
1. 在 “我的域名” 管理页面，选择您需要配置的域名，并单击【管理】。如下图所示：
![](https://main.qcloudimg.com/raw/d19438c7800e49ec15bfa09a61337b86.png)
2. 进入 “域名信息” 管理页面，选择【域名安全】页签，并单击【DNSSEC 设置】>【管理】。如下图所示：
![](https://main.qcloudimg.com/raw/805d5bf566ca4476acaf6306e2db1cf0.png)
3. 请单击【我已了解】，并进入 “DNSSEC 设置” 管理页面。如下图所示：
![](https://main.qcloudimg.com/raw/0f1804270c99e98ba11d3704575d8a21.png)
4. 在 “DNSSEC 设置” 管理页面，您可以通过以下两种方式添加 DNSSEC 记录。如下图所示：
  ![](https://main.qcloudimg.com/raw/0e8f317ea98d43c15e64ba0cf94e2808.png)
  - **添加 DNSSEC**：单击【添加 DNSSEC】，在弹出的 “添加 DNSSEC 记录” 窗口中填写以下参数信息。如下图所示：
    >? 
    >- 如该域名未添加过 DNSSEC 记录，添加记录时，参数信息请您至**域名解析商**处获取。
    >- 如您的域名在 [DNSPod 控制台](https://console.dnspod.cn/dns) 进行解析，参数信息您可以通过 [域名系统安全扩展（DNSSEC）配置指南（DNSPod）](https://docs.dnspod.cn/p/7c0da849-3160-493c-bd52-b31da391aebc/) 获取。
    >
    ![](https://main.qcloudimg.com/raw/835a0e9bbc97601287f6613c75d56c45.png)
		- **关键标签**：用于标识域名的 DNSSEC 记录，请填写小于 65536 的整数值。
		- **加密算法**：选择生成签名的加密算法。
		- **摘要类型**：选择构建摘要的算法类型。
		- **摘要**：填写从域名解析商处获取到的摘要内容。
 - **同步 DNSSEC** ：若您的域名是从其他域名注册商转入腾讯云，且在原注册商处添加过 DNSSEC 记录，可单击【同步 DNSSEC】，将之前添加的 DNSSEC 记录同步至腾讯云。

