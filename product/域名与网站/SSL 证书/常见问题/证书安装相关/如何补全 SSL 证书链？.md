通常情况下 PC 端浏览器都可以通过 Authority Info Access（权威信息访问）的 URL 链接获得中间证书，但在部分 Android 系统的浏览器上访问时会出现证书不可信或无法访问等问题。
主要原因在于部分 Android 系统的浏览器并不支持通过 Authority Info Access（权威信息访问）的 URL 链接获得中间证书，这时您需要把证书链文件按照 SSL 证书链的结构合并为一个文件重新部署到服务器上，浏览器在与服务器连接时将会下载用户证书和中间证书，使您的浏览器访问时显示为可信证书。SSL 证书链结构如下所示：

```
-----BEGIN CERTIFICATE-----
网站证书
-----END CERTIFICATE-----

-----BEGIN CERTIFICATE-----

CA 中间证书机构
-----END CERTIFICATE-----

-----BEGIN CERTIFICATE-----

CA 根证书机构

-----END CERTIFICATE-----
```

>?
>- SSL 证书链的结构，一般是由**网站证书 > CA 中间证书机构 > CA 根证书机构**构成，中间证书还可能存在多层关系。
>- 腾讯云提供的 SSL 国际标准证书为完整的证书链，无需进行补齐即可正常使用。



### 如何查看 SSL 证书链？
1. 打开 Chrome 浏览器访问安装部署 SSL 证书成功的网站。此处以 Chrome 浏览器为例。
2. 在浏览器地址栏单击![](https://main.qcloudimg.com/raw/f338bd1d67db54ba1928bc4fd37e3e13.png)小锁图标，并在弹出的信息卡片中，单击**证书**。如下图所示：
![](https://main.qcloudimg.com/raw/cc32ffca699af20dda94cd81cb4ea86b.png)
3. 在弹出的 “证书” 信息窗口中，单击**证书路径**，即可查看 SSL 证书链。如下图所示：
![](https://main.qcloudimg.com/raw/1ee2b85767678fb184ead9aeb3b3726d.png)




