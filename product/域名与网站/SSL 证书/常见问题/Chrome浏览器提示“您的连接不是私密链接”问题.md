自2016年11月起，部分 chrome 浏览器用户反馈访问 Https 站点时出现 **NET::ERR_CERTIFICATE_TRANSPARENCY_REQUIRED** 错误情况，提示 “您的连接不是私密链接”。如下图所示：
![](https://mc.qcloudimg.com/static/img/0fdf027303e53946698dcb377431597e/0.png)

该 CT 错误经确认是 chrome 浏览器53、54版本的内核问题，该 BUG 导致与 Symantec CA 机构颁发的 SSL 证书出现不兼容问题，Symantec CA 机构所有2016年6月1日之后的证书都会被此问题影响出现 CT 错误的情况，Chrome 方面在第一时间通过自动补丁方式处理了此问题，并在55版本修复此问题。

在能正常连接 Chrome 的服务器的客户都不会被此问题影响，但因中国大部分用户不能访问到 Chrome 的服务器，所以建议用户升级至55+版本来解决这个问题。

![](https://mc.qcloudimg.com/static/img/25a818d9e80a02c2b8b7c90f0e1c93df/1.png)

Symantec 官方声明：	https://www.symantec.com/connect/blogs/chrome-53-bug-affecting-symantec-ssltls-certificates

以及 Chrome 官方公告：https://bugs.chromium.org/p/chromium/issues/detail?id=664177

另外，使用了 Chromium 53 内核的 QQ 浏览器也会存在这个问题，已经在新版本中修复，建议使用旧版本 QQ 浏览器的用户更新到最新版本。
