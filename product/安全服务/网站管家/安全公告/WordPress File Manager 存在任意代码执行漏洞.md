2020年9月6日，腾讯安全团队检测到 WordPress 插件 File Manager 存在任意代码执行漏洞，攻击者利用该漏洞可以在含有 File Manager 的 WordPress 网站中上传木马、执行任意命令和恶意脚本。

腾讯安全已捕获在野利用（现网利用），目前腾讯云 Web 应用防火墙已支持防御。

## 漏洞详情
腾讯安全团队检测到 WordPress 插件 File Manager 被曝存在任意代码执行漏洞，攻击者利用该漏洞可以在含有 File Manager 的 WordPress 网站中上传木马、执行任意命令和恶意脚本。在 wordpress.org 的插件库中， File Manager 在2020年9月1日之前提供的 v6.8 版本为受影响版本，可以被攻击者用于破坏网站。

默认情况下，无需认证可以直接打开文件 lib/php/\*.php ，并且该文件加载 lib/php/\*.php，该文件读取 POST/GET 变量，并允许执行一些内部功能，例如上传文件等，由于允许使用 PHP 代码，因此会导致未经身份验证的任意文件上传和远程代码执行。


## 影响版本

WordPress File Manager < 6.9

## 修复建议
官方发布升级插件修复该漏洞，腾讯安全建议您：
- 更新 WordPress File Manager  版本至6.9及以上。
- 推荐采取腾讯云 Web 应用防火墙检测并拦截此次攻击。



## 参考信息
[CVE 2020-25213](https://wpvulndb.com/vulnerabilities/10389) 
