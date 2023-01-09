## 操作场景
本文档指导您如何在群晖（Synology）NAS 上安装免费 SSL 证书。


<dx-alert infotype="explain" title="">
免费 SSL 证书由顶级 CA 机构 TrustAsia 免费提供。
</dx-alert>

## 前提条件
- 具备群晖（Synology） NAS 管理员权限的账号。
- 具备 DNSPod 账号并完成 [实名认证](https://docs.dnspod.cn/account/5f3c8dffab35dc34f5791414/)。
- 已在群晖（Synology）NAS 上正确 [部署 DNSPod DDNS 服务](https://docs.dnspod.cn/dns/dnspod-synology-nas-ddns/)。

## 操作步骤

### 申请及下载证书

1. 登录 DNSPod，并进入 [我的域名](https://console.dnspod.cn/dns/list) 管理页面。
2. 单击 DDNS 域名，进入“记录管理”页面，检查该域名的 DDNS 记录值是否为群晖 NAS（Synology）中获取到的公网 IP 地址。确认无误后鼠标覆盖在 **SSL** 上，单击悬浮框中的**免费申请**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/2ebbfd8558256e232f0250b1d6f43dc8.png)
3. 在弹出的“申请 SSL 证书”窗口中，选择左侧 **SSL 证书免费版**，并单击**免费申请**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/e9cb48f53780be384f8f8176042e9a65.png)
4. 系统将自动在记录中添加一条“主机记录”为 `_dnsauth` 的 TXT 记录，同时 SSL 证书状态变更为“待验证”。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/a1809ae0b61f3addab57b59a0b3a4fde.png)
域名身份验证通过后，您将收到短信、邮件等审核通过通知。 
5. 鼠标覆盖在 **SSL** 上，单击悬浮框中的**查看详情**进入证书详情页。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/2999346fd09d575743f4944addd7d98c.png)
6. 在证书详情页，单击**下载证书**，将证书的压缩包文件下载到本地。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/9ccb056bf3b30bb3dc1b096c63c0efef.png)


### 安装证书
1. 在本地解压后，打开 Nginx 文件夹。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/08289a4171a0ef30be381ba804d8e489.png)
<dx-alert infotype="explain" title="">
文件夹内的 `.crt` 后缀文件为证书，`.key` 后缀文件为私钥。
</dx-alert>
2. 请使用具有管理员权限的账号登录您的群晖（Synology）NAS，选择**控制面板** > **安全性**，选择**证书**页签并单击**新增**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/97ef6a747761e33318b119c850b7b777.png)
3. 在弹出的“创建证书”窗口中，选择**添加新证书**，并单击**下一步**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/994ca0e9656ece2d99961b36afe921fb.png)
4. 请填入您的自定义描述，选择**导入证书**，并单击**下一步**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/5af9c117a88e95d31a0199e83e190d0b.png)
5. 导入下载至本地的证书与私钥文件，上传后并单击**确定**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/11da3aac90cc5cc8ab3fdbfc31229c84.png)
6.  单击控制面板中的**配置**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/367ca7d2158bb67b219503d07c60634a.png)
7. 在弹出的“配置”窗口中，将所有证书替换为新添加的 SSL 证书，并单击**确定**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/787c1da1a3f693ad4a07a0826d993c2e.png)
8. 使用 `https://域名:5001` 访问您的群晖（Synology）NAS，即可查看证书已被浏览器信任。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/6601ba22b17cba0f29d61165c86d29a4.png)
<dx-alert infotype="notice" title="">
若访问失败，请检查端口转发是否正确设置及 DSM 是否开启了 https 5001端口访问。
</dx-alert>

