## 常见问题

+ 配置了HTTPS证书后，浏览器反馈证书不受信任？
	+ 检查您的证书颁发机构及浏览器：
		+ 谷歌已经停止信任沃通WoSign和StartCom，[查看详情](https://security.googleblog.com/2016/10/distrusting-wosign-and-startcom.html)；
		+ 苹果已经停止信任沃通，[查看详情](https://support.apple.com/en-us/HT204132)；
		+ Mozilla发布的针对沃通的13项调查报告：[查看详情](https://docs.google.com/document/d/1C6BlmbeQfn4a9zydVi2UvjBGv6szuSB4sMYUcVrR8vQ/preview#)。
	+ 您可以申请腾讯云提供的免费证书，或在腾讯云上购买证书，[点击前往](https://console.cloud.tencent.com/ssl)。

+ HTTPS 支持哪些版本的SSL/TSL安全协议？
	+ CDN HTTPS目前支持的 ssl\_protocols：TLSv1、TLSv1.1、TLSv1.2。

+ 配置证书时，提示证书链不齐全？
	+ CDN 目前支持的是 PEM 格式的证书，在上传时，需要把CA的证书贴在域名证书后，进行上传，具体方法 [点击查看](https://cloud.tencent.com/document/product/228/6303#.E8.AF.81.E4.B9.A6.E9.93.BE.E8.A1.A5.E9.BD.90) 。

+ 配置证书时，提示证书不匹配？
	+ 您可以采用【批量上传】方式，将证书贴入后，CDN会为您分析能够使用该证书的域名，检查是否上传错误证书，或要配置的域名尚未接入CDN。

+ CDN支持ECC加密的证书么？
	+ CDN暂时不支持 ECC加密证书。

+ 配置了证书后，页面无法打开？
	+ 检查您是否设置了HTTPS回源，设置了HTTPS回源但源站未配置证书，会导致回源失败。您可以修改回源方式为HTTP，或为源站配置证书进行修复。





