本文介绍如何为您的轻量应用服务器安装 SSL 证书。

## 准备工作
您需完成以下准备工作：
- 已准备文件远程拷贝软件，例如 WinSCP（建议从官方网站获取最新版本）。
- 已准备远程登录工具，例如 PuTTY 或者 Xshell（建议从官方网站获取最新版本）。
- 轻量应用服务器创建完成后，防火墙默认已开启 `443` 端口。
建议您在安装 SSL 证书前，前往防火墙页面确认已开启 `443` 端口，避免证书安装后无法启用 HTTPS。详情请参见 [管理防火墙](https://cloud.tencent.com/document/product/1207/44577)。
- 安装 SSL 证书前需准备的数据如下：
<table>
<tr>
<th style="width:35%">名称</th>
<th>说明</th>
</tr>
<tr>
<td>轻量应用服务器的公网 IP 地址</td>
<td>服务器的 IP 地址，用于本地计算机连接到服务器。</td>
</tr>
<tr>
<td>用户名</td>
<td>登录轻量应用服务器操作系统的用户名，例如 root。</td>
</tr>
<tr>
<td>密码或 SSH 密钥</td>
<td>登录轻量应用服务器操作系统所使用的用户名对应的密码，或者已绑定的 SSH 密钥。</td>
</tr>
</table>

>!您可以登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse) 找到对应的服务器实例，进入实例详情页查看服务器的公网 IP 地址。如果该实例创建后未执行重置密码或者绑定 SSH 密钥操作，请您执行重置密码操作并牢记密码，或绑定 SSH 密钥并保存私钥文件。详情请参见 [重置密码](https://cloud.tencent.com/document/product/1207/44575) 和 [绑定密钥](https://cloud.tencent.com/document/product/1207/44573)。


## 选择证书安装方式
您可参考下表，根据轻量应用服务器实际搭建的网站类型，选择不同的 SSL 证书安装方式：
<table>
<tr>
<th>证书类型</th><th>轻量应用服务器操作系统</th><th>证书安装方式</th>
</tr>
<tr>
<td rowspan=2>国际标准证书</td><td rowspan=2>Linux 系统</td>
<td><a href="https://cloud.tencent.com/document/product/1207/47027">Nginx 服务器证书安装</a></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/1207/50330">Apache 服务器证书安装</a></td>
</tr>
</table>

## 相关文档
- [SSL 证书产品介绍](https://cloud.tencent.com/document/product/400/7572)
- [SSL 证书购买指南](https://cloud.tencent.com/document/product/400/7994)
- [申请免费 SSL 证书](https://cloud.tencent.com/document/product/400/6814)
