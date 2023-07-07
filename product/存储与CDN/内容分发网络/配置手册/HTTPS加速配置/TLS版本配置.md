## 背景信息

传输层安全性协议（TLS：Transport Layer Security），目的是为了保证两个应用程序在通信过程中数据的安全性和保密性，目前有四个版本的 TLS 协议：TLS1.0/1.1/1.2/1.3，版本越低兼容性越好，但是安全性越差；版本越高安全性越强，但是兼容性会弱一些。

<table>
<thead>
<tr>
<th>TLS 协议版本</th>
<th>支持的主流浏览器</th>
</tr>
</thead>
<tbody><tr>
<td rowspan="3">TLS 1.0</td>
<td>IE6+</td>
</tr>
<tr>
<td>Chrome 1+</td>
</tr>
<tr>
<td>Firefox 2+</td>
</tr>
<tr>
<td rowspan="6">TLS 1.1</td>
<td>IE 11+</td>
</tr>
<tr>
<td>Chrome 22+</td>
</tr>
<tr>
<td>Firefox 24+</td>
</tr>
<tr>
<td>ME 12+</td>
</tr>
<tr>
<td>Safari 7+</td>
</tr>
<tr>
<td>Opera 12.1+</td>
</tr>
<tr>
<td rowspan="6">TLS 1.2</td>
<td>IE 11+</td>
</tr>
<tr>
<td>Chrome 30+</td>
</tr>
<tr>
<td>ME 12+</td>
</tr>
<tr>
<td>Firefox 27+</td>
</tr>
<tr>
<td>Safari 7+</td>
</tr>
<tr>
<td>Opera 16+</td>
</tr>
<tr>
<td rowspan="5">TLS 1.3</td>
<td>Chrome 70+</td>
</tr>
<tr>
<td>Firefox 63+</td>
</tr>
<tr>
<td>ME 79+</td>
</tr>
<tr>
<td>Safari 14+</td>
</tr>
<tr>
<td>Opera 57+</td>
</tr>
</tbody></table>

## 功能介绍

腾讯云 CDN 默认开启 TLS 1.0/1.1/1.2 ，关闭 TLS 1.3，您可按需关闭/开启指定 TLS 版本。

>! 配置前需确保已成功配置 HTTPS 证书。




## 配置指南

### 查看配置

登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在左侧菜单栏选择【域名管理】，单击域名操作列的【管理】，进入域名配置页面，切换 Tab 至【HTTPS 配置】，即可找到【TLS 版本配置】。

默认情况下，TLS 1.0/1.1/1.2为开启状态，TLS 1.3为关闭状态：

![](https://main.qcloudimg.com/raw/62bfd147322215f5bcb5ce745505415b.png)


### 修改配置

您可按需关闭/开启指定 TLS 版本，单击【修改配置】：
<img src="https://main.qcloudimg.com/raw/82b93c2c47ded2029793b4931a098b29.png"/ style="height:280px">


**配置约束**

- 只可开启连续或单个版本号。例如，不可仅开启1.0和1.2而关闭1.1。
- 不可关闭全部版本。
