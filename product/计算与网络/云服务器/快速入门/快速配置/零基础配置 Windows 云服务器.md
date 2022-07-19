<dx-alert infotype="explain" title="">
如果您是首次使用云服务器，建议您先选择轻量应用服务器（Lighthouse）来作为云服务器使用的入门途径，详情请参见 [快速配置轻量应用服务器 Windows 实例](https://cloud.tencent.com/document/product/1207/44549)。轻量应用服务器专为云开发者及云计算入门者设计，您可前往 [与云服务器 CVM 对比](https://cloud.tencent.com/document/product/1207/49819) 了解云服务器与轻量应用服务器的区别。
</dx-alert>

本文主要介绍如何从零开始，以最简单的方式搭建一个 Windows 云服务器。您可按照以下文档，购买和配置您的第一台包年包月 Windows 云服务器。
若想了解搭建 Linux 云服务器的入门教程，可以参考 <a href="https://cloud.tencent.com/document/product/213/2936" hotrep="document.guide.2764.link1">快速配置 Linux 云服务器</a>。


## 步骤1：注册腾讯云账号
如果您已在腾讯云注册，可忽略此步骤。
<div style="background-color:#00A4FF; width: 170px; height: 35px; line-height:35px; text-align:center;"><a href="https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F" target="_blank"  style="color: white; font-size:16px;" hotrep="document.guide.2764.btn1">点此注册腾讯云账号</a></div>


## 步骤2：购买 Windows 云服务器

<div style="background-color:#00A4FF; width: 190px; height: 35px; line-height:35px; text-align:center;"><a href="https://buy.cloud.tencent.com/cvm?tab=lite" target="_blank"  style="color: white; font-size:16px;" hotrep="document.guide.2764.btn2">点此进入快速购买页面</a></div>
</br>

![](https://qcloudimg.tencent-cloud.cn/raw/9e106e722a84b850dfe0f848b877a19e.png)

配置说明如下：
<table>
<tr>
<th>配置项</th>
<th>说明</th>
</tr>
<tr>
<td>地域</td>
<td>选择与您最近的一个地区，例如我在 “深圳”，地域选择 “广州”。</td>
</tr>
<tr>
<td>实例</td>
<td>选择您需要的云服务器机型配置。这里我们选择 “普及配置（2核4GB）”。 </td>
</tr>
<tr>
<td>操作系统</td>
<td>选择您需要的云服务器操作系统。这里我们选择 “Windows Server 2012 R2 数据中心版 64位中文版”。</td>
</tr>
<tr>
<td>公网 IP</td>
<td>勾选后会为您分配公网 IP，默认公网带宽为 “1Mbps”，您可以根据需求调整。</td>
</tr>
<tr>
<td>登录方式</td>
<td>自动生成的密码将在服务器创建完成后通过 <a href="https://console.cloud.tencent.com/message">站内信</a> 发送。</td>
</tr>
<tr>
<td>默认配置</td>
<td>可展开查看可用区、安全组等6项默认配置。</td>
</tr>
<tr>
<td>自动续费</td>
<td>勾选后，若账户余额足够，则将在云服务器到期时按月自动续费。</td>
</tr>
<tr>
<td>协议</td>
<td>查阅并了解相关协议后勾选。</td>
</tr>
<tr>
<td>时长</td>
<td>购买时长，默认为 “1个月”。</td>
</tr>
<tr>
<td>数量</td>
<td>购买数量，默认为 “1台”。</td>
</tr>
</table>

单击**立即购买**，并付费完成后，即完成了云服务器的购买。
云服务器可以作为个人虚拟机或者您建站的服务器。接下来，您可以登录您购买的这台服务器。



## 步骤3：登录云服务器



<dx-alert infotype="notice" title="">
通过快速配置购买的云服务器，系统将为您自动分配云服务器登录密码并发送到您的站内信中。此密码为登录云服务器的凭据。<div style="background-color:#00A4FF; width: 160px; height: 35px; line-height:35px; text-align:center;"><a href="https://console.cloud.tencent.com/message" target="_blank"  style="color: white; font-size:16px;" hotrep="document.guide.2764.btn3">点此获取初始密码</a></div>
</dx-alert>


 
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm)，在实例列表中找到您刚购买的云服务器，在右侧操作栏中单击**登录**。
![](https://main.qcloudimg.com/raw/af462e19818656510615a663e6aae536.png)
2. 参考 [使用标准方式登录 Windows 实例（推荐）](https://cloud.tencent.com/document/product/213/5435)，登录云服务器。
登录成功后将打开 Windows 云服务器界面，如下图所示：
![](https://main.qcloudimg.com/raw/5a524210acd13624af7263b6de3aea54.png)

## 下一步操作：使用云服务器

当您登录云服务器后，即可在云服务器上进行您所需要的操作。常用的任务包括：
- <a href="https://cloud.tencent.com/document/product/213/39138" hotrep="document.guide.2764.link2">将您本地的文件上传到云服务器上</a>
- <a href="https://cloud.tencent.com/document/product/213/39130" hotrep="document.guide.2764.link3">在云服务器上搭建网站</a>

您可以根据需要，按照文档指引进行下一步操作。

## 出现问题？
非常抱歉您在使用时出现问题，您可以第一时间通过 <a href="https://cloud.tencent.com/online-service?from=doc_213" hotrep="document.guide.2764.link4">在线支持</a> 联系我们，也可以先参考相关文档进行问题定位和解决。
以下是用户在使用云服务器时出现的常见问题，建议您先参考文档进行问题定位和解决。
- 忘记云服务器登录密码？
请参考 <a href="https://cloud.tencent.com/document/product/213/16566" hotrep="document.guide.2764.link5">重置实例密码</a>。
- 登录不成功？如何定位问题？
请参考 <a href="https://cloud.tencent.com/document/product/213/10339" hotrep="document.guide.2764.link6">无法登录 Windows 实例</a>。
