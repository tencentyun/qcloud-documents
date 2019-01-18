2016年11月份起，部分chrome浏览器用户反馈访问Https站点时的**NET::ERR_CERTIFICATE_TRANSPARENCY_REQUIRED**错误情况，提示“您的连接不是私密链接”。

内容如下：
![](https://mc.qcloudimg.com/static/img/0fdf027303e53946698dcb377431597e/0.png)

该CT错误经确认是chrome浏览器53、54版本的内核问题，该 BUG 导致与 Symantec CA机构颁发的SSL证书出现不兼容问题，Symantec CA机构所有2016年6月1日之后的证书都会被此问题影响出现CT错误的情况，Chrome方面在第一时间通过自动补丁方式处理了此问题，并在55版本修复此问题。

在能正常连接Chrome的服务器的客户都不会被此问题影响，但因中国大部分用户不能访问到Chrome的服务器，所以建议用户升级至55+版本来解决这个问题。

![](https://mc.qcloudimg.com/static/img/25a818d9e80a02c2b8b7c90f0e1c93df/1.png)

Symantec官方声明：	https://www.symantec.com/connect/blogs/chrome-53-bug-affecting-symantec-ssltls-certificates

以及Chrome官方公告：https://bugs.chromium.org/p/chromium/issues/detail?id=664177

另外，使用了 Chromium 53内核的QQ浏览器也会存在这个问题，已经在新版本中修复，使用了旧版本QQ浏览器的用户也建议更新到最新版本。
详情可查看QQ浏览器官方公告：http://bbs.browser.qq.com/thread-222732-1-1.html
