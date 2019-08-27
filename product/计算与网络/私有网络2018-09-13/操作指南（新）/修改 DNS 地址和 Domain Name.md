>?目前配置 DNS 地址功能灰度中，仅2018年04月01日后创建的部分 VPC 支持，如有疑问和需要，请提交 [工单申请](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=168&level1_name=%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C&level2_name=%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%20VPC)。

1. 登录 [腾讯云控制台](https://console.cloud.tencent.com/) ，选择【云产品】>【网络】>【私有网络】，进入私有网络控制台。
2. 单击需要修改的私有网络 ID，进入详情页，即可在基本信息内配置 DNS 地址和 Domain Name。
 - DNS 地址
	 - DNS 最多支持4个 IP，IP 之间请用逗号隔开。
	 - DNS 可以指定4个 IP，但某些操作系统可能无法支持4个 DNS 地址。
	 - 腾讯云默认 DNS 为：`183.60.83.19`，`183.60.82.98`。如不使用腾讯云默认 DNS，将无法使用内部服务，如 Windows 激活、NTP、YUM 等。
 - Domain Name
	 - 云服务器 hostname 后缀，例如`example.com`。

![](https://main.qcloudimg.com/raw/b6c45b1894296513876be194d7ba086d.png)

>!
- 2018年4月1日前创建的私有网络暂不支持 DHCP 特性，若您在控制台无法修改 DNS 地址和 Domain Name，即说明您的私有网络不支持该特性。
- 为了保证配置修改后及时生效，重启云服务器或 dhclient，新增的云服务器修改该配置立即生效。
