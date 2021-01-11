本文将为您详细介绍 LDAP/AD 数据源配置。
## 操作场景
腾讯云 IDaaS 支持通过 LDAP 从 AD 中拉取组织机构和账户信息至 IDaaS 用户目录，本文将为您详细介绍 LDAP/AD 数据源配置与同步方法。目前仅支持 Windows AD。
## 操作步骤
1. 管理员登录 [IDaaS 控制台](https://console.cloud.tencent.com/idaas)，单击左侧菜单中的【数据源管理】。
2. 单击【启用】LDAP/AD 数据源，即可进入 LDAP/AD 数据源设置页面。  
![](https://main.qcloudimg.com/raw/a37b424e05a4ec3e89b65d5a95c83538.png)
3. 配置 LDAP/AD 数据源。
	1. 填写 LDAP 服务器配置信息。
	 ![](https://main.qcloudimg.com/raw/559441c8a2c4dd8497fa6a0b258ca1a6.png)
		- 服务器地址：请填写 LDAP 服务器 IP。例如100.0.0.1，目前暂不支持 IPv6。
		- 端口号：请填写 LDAP 服务器端口号。例如389。
		- Base DN：请填写 LDAP 服务器的 Base DN。例如 OU=testcompany,DC=test。
		- 连接方式：请选择是否使用 SSL 连接。
		- 管理员 DN：请填写 LDAP 服务器的管理员 DN。例如 CN=administrator,CN=Users,DC=test,DC=com。
		- 密码：请填写 LDAP 服务器的管理员密码。
	2. 填写字段匹配信息，即 IDaaS 中字段与 LDAP/AD 中字段的匹配关系。
	 ![](https://main.qcloudimg.com/raw/b56df20170a79273a98daa2a7036885b.png)
		- 用户 ID：此字段将对应 IDaaS 用户目录中的用户名字段，一般选择 CN。**注意：若您的 CN 字段值为中文，将无法同步 AD 数据源信息至 IDaaS，此时建议您选择 sAMAccountName 字段。**
		- 姓名：此字段将对应 IDaaS 用户目录中的姓名字段，一般选择 Name。
		- 手机字段：此字段将对应 IDaaS 用户目录中的手机字段，一般选择 TelephoneNumber。
		- 邮箱字段：此字段将对应 IDaaS 用户目录中的邮箱字段，一般选择 Mail。
	3. 进行密码设置，可选自动生成密码或自定义密码。
	 ![](https://main.qcloudimg.com/raw/c0c4830e62cb975e55ffd38354c6ced5.png)
	4. 进行数据同步设置，目前支持手动同步和自动定时同步。若选择定时同步，可选同步频率。
	![](https://main.qcloudimg.com/raw/a0fd46c7480c94177e28e8492a7ffff5.png)
	5. 配置完成后，单击【保存并启用】完成。之后下载并安装 Qcloud AD Agent。
	![](https://main.qcloudimg.com/raw/f929f795320f5b3ce5d8ea39dd54625b.png)
4. 下载并安装 Qcloud AD Agent。
	1. 在 LDAP/AD 数据源详情页下载 AD Agent。
	 ![](https://main.qcloudimg.com/raw/0821edb53760d8b8153b17d15b8ae0a2.png)
	2. 下载好安装文件后，安装 AD Agent。过程中需输入 Agent 配置信息中的同步 ID、同步 Token、同步加密 Key 和同步 URL。
	 ![](https://main.qcloudimg.com/raw/fda0a4a46ef84bfa0c85b47887719373.png)
5. 至此，您已完成 LDAP/AD 数据源的配置。
>! 若想使用 AD 账号登录 IDaaS 门户，还需将 LDAP/AD 数据源同步至 IDaaS 并配置 [LDAP 认证源](https://cloud.tencent.com/document/product/1106/47049)。

