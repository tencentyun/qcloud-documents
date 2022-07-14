2020年9月17日，腾讯安全团队检测到 Microsoft 发布了 Exchange Server 命令执行漏洞的安全公告，该漏洞编号为 CVE-2020-16875。
>?Microsoft Exchange Server 是美国微软（Microsoft）公司的一套电子邮件服务程序，它提供邮件存取、储存、转发、语音邮件及邮件过滤筛选等功能。
>
目前该漏洞 POC 已经在网络上流传，腾讯安全团队建议及时将 Exchange 升级到最新版本，做好资产自查以及相关防护工作，以免遭受黑客恶意攻击。目前腾讯云 Web 应用防火墙已支持防御。 

## 漏洞详情


Microsoft Exchange 服务器中存在一个远程执行代码漏洞。此次漏洞是由于 Exchange 对 cmdlet 参数的验证不全面，使攻击者成功利用此漏洞在系统用户的上下文中运行任意代码。此漏洞需要通过 Exchange 身份验证才能利用。由于 Exchange 服务以 SYSTEM 权限运行，攻击者可通过利用该漏洞获得系统最高权限。


## 影响版本
- Microsoft Exchange Server 2016 Cumulative Update 16
- Microsoft Exchange Server 2016 Cumulative Update 17
- Microsoft Exchange Server 2019 Cumulative Update 5
- Microsoft Exchange Server 2019 Cumulative Update 6

## 修复建议
根据漏洞通告信息，腾讯安全建议您：
- 及时更新漏洞补丁。
- 推荐采取腾讯云 Web 应用防火墙检测并防御此次攻击。

## 参考信息
[CVE-2020-16875](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16875) 

