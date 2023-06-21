云服务器（Cloud Virtual Machine，CVM）是腾讯云提供的可扩展的计算服务。使用云服务器避免了使用传统服务器时需要预估资源用量及前期投入，帮助您在短时间内快速启动任意数量的云服务器并即时部署应用程序。

本文为您介绍如何从零开始，以最简单的方式搭建一个 Windows 云服务器。您可按照以下文档，购买和配置您的第一台云服务器。若想了解搭建 Linux 云服务器的入门教程，可以参考 [快速配置 Linux 云服务器](https://cloud.tencent.com/document/product/1003/79661)。

## 前提条件
已注册腾讯云账号，详细方法请参见 [注册腾讯云账号](https://cloud.tencent.com/document/product/1003/79164)。

## 配置 Windows 云服务器
>!为确保成功连接到 TDSQL-C MySQL 版，建议购买的云服务器 CVM 与 TDSQL-C MySQL 版满足以下几点：
>- CVM 和 TDSQL-C MySQL 版属于同一个腾讯云主账号。
>- CVM 和 TDSQL-C MySQL 版位于同一地域。
>- CVM 和 TDSQL-C MySQL 版的网络类型都是 VPC 且处于同一个 VPC 内。
>

### 步骤一：购买 Windows 云服务器
1. 进入 [快速购买页面](https://buy.cloud.tencent.com/cvm?tab=lite&ltCreateMode=createLt)。
2. 在购买页 > **快速配置**分页，完成云服务器配置后，单击**立即购买**。
![](https://qcloudimg.tencent-cloud.cn/raw/c2c6bda12418a454cf93caf29e11417c.png)
配置说明如下：
<table>
<thead><tr><th>配置项</th><th>说明</th></tr></thead>
<tr>
<td>地域</td>
<td>选择与您的 TDSQL-C MySQL 版集群所在同一个地域。</td></tr>
<tr>
<td>实例</td>
<td>选择您需要的云服务器机型配置。这里我们选择 “普及配置（2核4GB）”。 </td></tr>
<tr>
<td>操作系统</td>
<td>选择您需要的云服务器操作系统。这里我们选择 “Windows Server 2022 数据中心版 64位中文版”。</td></tr>
<tr>
<td>公网 IP</td>
<td>勾选后会为您分配公网 IP，默认公网带宽为 “1Mbps”，您可以根据需求调整。</td></tr>
<tr>
<td>登录方式</td>
<td>自动生成的密码将在服务器创建完成后通过 <a href="https://console.cloud.tencent.com/message">站内信</a> 发送。</td></tr>
<tr>
<td>默认配置</td>
<td>可展开查看可用区、安全组等6项默认配置。</td></tr>
<tr>
<td>自动续费</td>
<td>勾选后，若账户余额足够，则将在云服务器到期时按月自动续费。</td></tr>
<tr>
<td>协议</td>
<td>查阅并了解相关协议后勾选。</td></tr>
<tr>
<td>时长</td>
<td>购买时长，默认为 “1个月”。</td></tr>
<tr>
<td>数量</td>
<td>购买数量，默认为 “1台”。</td></tr>
</table>

当您付费完成后，即完成了云服务器的购买。云服务器可以作为个人虚拟机或者您建站的服务器。接下来，您可以登录您购买的这台服务器。

### 步骤二：登录云服务器
>!通过快速配置购买的云服务器，系统将为您自动分配云服务器登录密码并发送到您的站内信中。此密码为登录云服务器的凭据。您可至 [站内信](https://console.cloud.tencent.com/message) 查收您的密码。

1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。
2. 在实例的管理页面，根据实际使用的视图模式进行操作：
<dx-tabs>
::: 列表视图
找到需要登录的 Windows 云服务器，单击右侧的**登录**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/d7d05d0afadafea69e6fc606a942dd19.png)

:::
::: 页签视图
选择需要登录的 Windows 云服务器页签，单击**登录**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/986818e2c39ac3745d2c58ad88d61464.png)

:::
</dx-tabs>
3. 在打开的“标准登录 | Windows 实例”窗口中，根据实际情况填写登录信息。如下图所示：
![](https://main.qcloudimg.com/raw/5ebd8128311bb94edbacbd8cc5763793.png)
 - **端口**：默认为3389，请按需填写。
 - **用户名**：Windows 实例用户名默认为 `Administrator`，请按需填写。
 - **密码**：填写已从 [站内信](https://console.cloud.tencent.com/message) 中获取的登录密码。
5. 单击**登录**，即可登录 Windows 实例。
本文以登录操作系统为 Windows Server 2016 数据中心版64位中文版的云服务器为例，登录成功则出现类似如下图所示界面：
![](https://main.qcloudimg.com/raw/a68deed91b8d73db1e6b2f931c6689c1.png)
