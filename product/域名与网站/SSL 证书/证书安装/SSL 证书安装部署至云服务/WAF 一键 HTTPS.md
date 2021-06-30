
## 概述
一键 HTTPS 是 SSL 证书结合腾讯云 Web 应用防火墙（WAF）服务开发的快速部署 WAF 的 HTTPS 功能。使用该功能，您可以快捷的在 [证书控制台](https://console.cloud.tencent.com/https) 将您申请到的 SSL 证书接入部署至腾讯云 Web 应用防火墙（WAF）提供的 SaaS 型 WAF 域名接入服务。SaaS 型 WAF 通过为防护域名分配 CNAME，修改网站的 DNS 解析记录，将网站收到的 Web 请求转发给 WAF，从而对网站进行安全防护。具体详情参见 [Web 应用防火墙产品概述](https://cloud.tencent.com/document/product/627/17470)。
本文将指导您如何在 [证书控制台](https://console.cloud.tencent.com/https) 一键添加 WAF 接入域名并配置 HTTPS。

## 前提条件
已在 [证书管理控制台](https://console.cloud.tencent.com/ssl) 颁发 SSL 证书。


## 操作指南
### 添加一键 HTTPS 域名
1. 登录 [证书管理控制台](https://console.cloud.tencent.com/ssl) ，单击侧边栏【一键 HTTPS】。
2. 在 “一键HTTPS” 页面中，单击【一键添加】。如下图所示：
>?若您是第一次使用，在弹出的授权页面中，授予对应权限。
>
![](https://main.qcloudimg.com/raw/7fe3045747a78bab70a9531041d96211.png)
3. 在弹出的“一键添加”窗口中，配置相应信息。如下图所示：
![](https://main.qcloudimg.com/raw/f233865676094233797f3590a921e770.png)
- **填写域名：**请输入您需要进行一键 HTTPS 的域名，支持通配符域名。
- **选择证书：**请选择在证书控制台申请成功的证书。
>? 选择的证书需与【填写域名】填写的域名对应。单域名对应相同域名名称的单域名证书，通配符域名对应相同域名名称的通配符证书，多域名选择包含域名名称的多域名证书。
- **源站地址：**可选【IP】与【域名】两个选项。您可根据您的具体情况选择。
-**IP**：在源站 IP 输入框内输入需要防护网站的真实 IP 源站地址，即源站的公网 IP 地址。
- **域名**：在源站域名输入框内输入需要防护网站的真实源站域名。
- **强制HTTPS：**开启该功能，浏览器端的每个 HTTP 请求都会被跳转成 HTTPS 请求。如当浏览器使用 HTTP 协议访问 `http://cloud.tencent.com ` 时，将返回 302 状态码重定向到 HTTPS 协议访问 `https://cloud.tencent.com`。
**回源协议：**	开启该功能，腾讯云将使用 HTTP 协议访问源站。如当浏览器使用 HTTP 或 HTTPS 协议访问 `cloud.tencent.com` 时，无论 HTTP 或 HTTPS 协议都将使用 HTTP 协议访问源站。
**回源端口：**请选择回源端口。默认情况下支持 443 与 8443，若您开启回源协议，则为80与8080。
4. 单击【确定】。控制台将会生成添加的配置实例。如下图所示：
![](https://main.qcloudimg.com/raw/5bd3f2ffde6f461f7ea1d2d0e6792018.png)

### 配置 CNAME 记录
添加一键 HTTPS 域名后，还需配置对应的CNAME 记录后，接入才可正常生效。
以下以在腾讯云 DNSPod DNS 解析控制台配置 CNAME 记录为例，若您的一键 HTTPS 域名未在 DNSPod 解析解析托管，具体操作请咨询您的域名解析商或将域名托管至 DNSPod DNS 解析后，在进行配置 CNAME 记录。详情参见：[域名托管至 DNSPod DNS 解析](https://docs.dnspod.cn/dns/60b99ba0e90008112f815bde/)。

1. 登录  [DNSPod 管理控制台](https://console.dnspod.cn/dns/list)。
2. 在 “我的域名” 中，选择需要进行一键 HTTPS 域名，单击“域名”，进入该域名的【记录管理】页面。如下图所示：
![](https://main.qcloudimg.com/raw/3888e10fc99f01d0cbb0058411f0e662.png)
3. 单击【添加记录】，填写以下记录信息。如下图所示：
![](https://main.qcloudimg.com/raw/489791e8d992b47ed300e30899050c67.png)
 - **主机记录**：填写子域名。例如，添加 `cs.dnspod.com` 的一键 HTTPS 域名，您在 “主机记录” 处填写 “cs” 即可。
 - **记录类型**：选择 “CNAME”。
 - **线路类型**：选择 “默认” 类型，否则会导致部分用户无法解析。
 - **记录值**：填写证书控制台提供的 CNAME 域名。如下图所示：
![](https://main.qcloudimg.com/raw/7e3d20faeccf2e793802d9fbc1fe6ed0.png)
 - **权重**：同一条主机记录相同的线路,可以针对不同的记录值设置权重,解析时将根据设置的权重比例进行返回。输入范围
为0~100的整数。
 - **MX 优先级**：不需要填写。
 - **TTL**：为缓存时间，数值越小，修改记录各地生效时间越快，默认为600秒。
4. 单击【确定】，完成添加。
5. 完成添加后，请耐心等待解析生效，解析生效后即可接入成功。
>?一般情况下，解析生效时间与您设置 TTL 值相同。
>











