
## 概述
一键 HTTPS 是 SSL 证书结合腾讯云 Web 应用防火墙（WAF）服务开发的快速部署 HTTPS 功能，帮助用户网站的 HTTPS 访问升级。
使用该功能，您无需进行繁琐的 SSL 证书部署操作，仅需配置一个CNAME 解析，即可实现从 HTTP 到 HTTPS 的能力升级。
本文将指导您如何在 [证书管理控制台](https://console.cloud.tencent.com/https) 一键添加 WAF 接入域名并配置 HTTPS。
>! 一键 HTTPS 功能目前为免费，可免费使用至2021年12月31日。


## 一键 HTTPS 与传统服务器部署 SSL 证书的区别
- 传统服务器部署 SSL 证书除了需具备基础技术知识的同时，整个部署过程中您还需要输入一系列操作命令和编辑相关配置文件，整个过程的繁琐性不仅增加了维护成本，同时也容易出现操作性事故，造成不可挽回的损失。如下图所示：
![](https://main.qcloudimg.com/raw/11beba8cca8e1126bafbff88142424f2.png)
- 一键 HTTPS 是结合腾讯云 Web 应用防火墙（WAF）服务开发的快速部署 HTTPS 功能，整个部署过程相对传统服务器部署要简单易操作，仅需配置一个 CNAME 解析，即可实现从 HTTP 到 HTTPS 的能力升级。不仅能够降低维护成本，简单的配置方式也可降低操作性事故发生的可能性。如下图所示：
![](https://main.qcloudimg.com/raw/5ee7958ff92149e6dad471378182db7d.png)

## 前提条件
已在 [证书管理控制台](https://console.cloud.tencent.com/ssl) 申请颁发 SSL 证书。


## 限制说明
- SSL 证书默认开通 WAF 小微版。支持1个二级域名、3个子域名、50 QPS。
>! www 子域名占用一个子域名名额，例如 `www.tencent.com` 。
- 若您一键 HTTPS 域名已使用腾讯云 CDN 或 CLB ，则无法使用一键 HTTPS 功能。




## 操作指南
### 步骤1：添加一键 HTTPS 域名
1. 登录 [证书管理控制台](https://console.cloud.tencent.com/ssl)，并单击左侧菜单栏**一键 HTTPS**，进入**一键 HTTPS**管理页面。
2. 在**一键 HTTPS**管理页面中，单击**一键添加**。如下图所示：
>?若您是首次使用，请在弹出的授权窗口中，授予对应权限。
>
![](https://main.qcloudimg.com/raw/e327528f08706299fef120e04c993099.png)
3. 在弹出的 “一键添加” 窗口中，配置相关信息。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/efb4e419723d263b035c2c9ffb6b625b.png)
 - **填写域名：**请输入您需要进行一键 HTTPS 的域名。
<dx-alert infotype="explain" title="">
 填写的域名需要在工信部完成备案，否则将无法进行接入。详情请参见 [备案概述](https://cloud.tencent.com/document/product/243/18907)。
</dx-alert>
 - **选择证书：**请选择已成功申请的证书。
<dx-alert infotype="explain" title="">
选择的证书需与**填写域名输入框**填写的域名对应。例如，填写的域名为 `cloud.tencent.com`，则选择绑定域名为 `cloud.tencent.com` 的证书。
</dx-alert>
 - **源站地址：**请根据您的实际需求选择**IP**与**域名**。
    - **IP**：请输入需要防护网站的真实 IP 源站地址，即源站的公网 IP 地址。
    - **域名**：请输入需要防护网站的真实源站域名。
 - **强制 HTTPS：**开启该功能，浏览器端的每个 HTTP 请求都会被跳转成 HTTPS 请求。例如，当浏览器使用 HTTP 协议访问 `http://cloud.tencent.com ` 时，将返回302状态码重定向到 HTTPS 协议访问 `https://cloud.tencent.com`。
 - **回源协议：**	开启该功能，腾讯云将使用 HTTP 协议访问源站。例如，当浏览器使用 HTTP 或 HTTPS 协议访问 `cloud.tencent.com` 时，无论 HTTP 或 HTTPS 协议都将使用 HTTP 协议访问源站。

>!若源站尚不支持HTTPS访问，请务必使用 HTTP 作为回源协议。

- **回源端口：**请根据您的实际需求选择回源端口。默认情况下支持80与8080d端口，若回源协议勾选 HTTPS ，则为443与8443。
- **高级选项（可选）**：
![](https://qcloudimg.tencent-cloud.cn/raw/a12a55c0bf89753cfb30fda0bf0fa2ca.png)
 -  **回源连接方式**：默认使用长连接回源，请确认源站是否支持长连接，若不支持，即使设置长连接，也会使用短连接回源。
 -  **开启HTTP2.0**：若您的源站不支持HTTP2.0，从腾讯云到源站链路将降级为HTTP1.1。源站支持 HTTP2.0 情况下建议您选择是，将提高您网站的访问速率。
 -  **开启WebSocket**：如果您的网站使用了Websocket，建议您选择是。将提高轮询的效率以及降低资源浪费。

4. 单击**确定**，即可生成配置实例。如下图所示：
![](https://main.qcloudimg.com/raw/2c548a3cf3bc61f73512a57150319cec.png)
### 步骤2：配置 CNAME 记录

>?
>- 添加一键 HTTPS 域名后，还需配置对应的 CNAME 记录后，接入才可正常生效。
>- 配置 CNAME 记录步骤以腾讯云配置 CNAME 记录为例，若您的一键 HTTPS 域名解析未在 DNSPod DNS 解析托管，具体操作请咨询您的域名解析商或将域名托管至 DNSPod DNS 解析后，再进行配置 CNAME 记录。详情请参见 [域名托管至 DNSPod DNS 解析](https://docs.dnspod.cn/dns/60b99ba0e90008112f815bde/)。

<dx-tabs>
::: 一键添加\sCNAME\s记录

<dx-alert infotype="explain" title="">
若您的域名解析已在 DNSPod DNS 解析进行托管，可直接一键添加 CNAME 记录。
</dx-alert>
1. 在 "一键 HTTPS" 管理页面，查看您需要进行配置 CNAME 记录的实例，单击<span ><img src="https://main.qcloudimg.com/raw/f5894edcb2045215d93c7c20ad8c1b0b.png" style="margin-bottom:-5px;"/></span>。如下图所示：
![](https://main.qcloudimg.com/raw/29802e182d7b4ea87573c07df81ec119.png)
2. 在弹出的 “温馨提示” 窗口中，单击**确定**。即可添加记录。如下图所示：
![](https://main.qcloudimg.com/raw/c0efc2dc88bb465e19f3b58e960f7c1e.png)
:::
::: 手动添加\sCNAME\s记录
1. 登录  [DNSPod 管理控制台](https://console.dnspod.cn/dns/list)。
2. 在 “我的域名” 中，选择需要配置记录的一键 HTTPS 域名，单击域名名称，即可进入该域名的**记录管理**页面。如下图所示：
![](https://main.qcloudimg.com/raw/3888e10fc99f01d0cbb0058411f0e662.png)
3. 单击**添加记录**，填写记录信息。如下图所示：
![](https://main.qcloudimg.com/raw/489791e8d992b47ed300e30899050c67.png)
 - **主机记录**：填写子域名。例如，添加 `cs.dnspod.com` 的一键 HTTPS 域名，您在 “主机记录” 处填写 “cs” 即可。
 - **记录类型**：选择 “CNAME”。
 - **线路类型**：选择 “默认” 类型，否则会导致部分用户无法解析。
 - **记录值**：填写证书控制台新增实例提供的 CNAME 域名。如下图所示：
![](https://main.qcloudimg.com/raw/a0cdf6f3df54548fb0c89c594267a9fe.png)
 - **权重**：同一条主机记录相同的线路，可以针对不同的记录值设置权重，解析时将根据设置的权重比例进行返回。输入范围为0 - 100的整数。
 - **MX 优先级**：不需要填写。
 - **TTL**：为缓存时间，数值越小，修改记录各地生效时间越快，默认为600秒。
4. 单击**确定**，即可添加记录。
5. 完成添加后，请耐心等待解析生效，解析生效后即可接入成功。
<dx-alert infotype="explain" title="">
一般情况下，解析生效时间与您设置 TTL 值相同。
</dx-alert>
:::
</dx-tabs>

>?防护配置是对 WAF 防护进行策略调整，如需进行防护配置，请您参考 [Web 应用防火墙产品文档](https://cloud.tencent.com/document/product/627/17470) 进行设置。













