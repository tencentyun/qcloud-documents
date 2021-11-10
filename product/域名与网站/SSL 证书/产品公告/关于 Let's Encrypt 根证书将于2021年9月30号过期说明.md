
Let's Encrypt 品牌 SSL 证书根证书将于**2021年9月30日**停用旧版根证书（Root CA）。若您的网站已部署 Let's Encrypt 品牌的 SSL 证书并在过期前未及时更新，将导致您的网站面临不受计算机、设备或 Web 浏览器信任，网站兼容性降低，甚至部分网站不能访问的现象，将会影响您的使用。如下图所示：
![](https://main.qcloudimg.com/raw/d0ec3d4ac185213d201ebfd5ca048bb8.png)

为避免您的业务受到影响，建议您尽快自查正在使用的 Let's Encrypt 品牌 SSL 证书是否存在该问题。您可通过证书监控 SSLPod 进行检查并查看报告详情。操作详情参见：[证书监控 SSLPod 操作指南](https://cloud.tencent.com/document/product/1084/34883)。

>?
>- 若存在以上问题，建议您尽快更新为其他品牌的 SSL 证书，从源头上避免 Let's Encrypt 根证书过期带来的一系列问题。
>- 因腾讯云未售卖颁发 Let's Encrypt 品牌证书，若您使用腾讯云颁发的 SSL 证书，可忽略该说明。
