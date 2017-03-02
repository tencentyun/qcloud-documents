2016年11月份起，部分chrome浏览器用户反馈访问Https站点时的**NET::ERR_CERTIFICATE_TRANSPARENCY_REQUIRED**错误情况，提示“您的连接不是私密链接”。

内容如下：
![](https://mc.qcloudimg.com/static/img/0fdf027303e53946698dcb377431597e/0.png)

经确认是chrome浏览器53、54版本的内核问题，该BUG导致与赛门铁克CA机构颁发的SSL证书出现不兼容问题，已经在55版本进行了修复。建议用户升级最新版本chrome浏览器。
![](https://mc.qcloudimg.com/static/img/25a818d9e80a02c2b8b7c90f0e1c93df/1.png)

详情可查看赛门铁克官网的公告：
https://knowledge.symantec.com/support/ssl-certificates-support/index?page=content&id=ALERT2160

另外，只用了53内核的QQ浏览器也会存在这个问题，已经在新版本中修复，使用了旧版本QQ浏览器的用户也建议更新到最新版本。
详情可查看QQ浏览器官网公告：http://bbs.browser.qq.com/thread-222732-1-1.html
