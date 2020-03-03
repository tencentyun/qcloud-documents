If the following prompt appears when applying for a Domain Validation (DV) SSL certificate, it indicates that the domain name failed to pass the security verification. **DV SSL certificates cannot be issued via the rapid review process of Symantec CA for the domain name**. Please purchase paid certificates.

![](https://mc.qcloudimg.com/static/img/25451d24cf3c717454830a44925642ec/1.png)

__The specific reasons for failed security verification:__<br/>

According to the anti-phishing mechanism of CAs, sensitive words contained in domain names, such as bank and pay, can cause failed security verifications. Specific sensitive words are defined by CAs. And some less commonly used root domain names may also fail to pass verifications. For example, root domain names with .pw suffix, such as `www.qq.pw` and `www.qcloud.pw`, will fail to pass the verification.


Because DV SSL certificates are quickly issued through automatic authentication without manual intervention, the verification standards are strengthened with more stringent sensitive words.

