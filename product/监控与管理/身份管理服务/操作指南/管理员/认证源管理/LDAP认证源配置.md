
## 操作场景
IDaaS 支持企业成员通过 LDAP/AD 用户名密码登录门户，本文将为您详细介绍如何进行 LDAP 认证源配置。

## 配置步骤
1.	管理员登录 [IDaaS 控制台](https://console.cloud.tencent.com/idaas)，单击左侧菜单中的【认证源管理】。
2.	选择【启用】LDAP 认证源，即进入 LDAP 认证源设置页面。
3.	填写认证源配置信息。
 ![](https://main.qcloudimg.com/raw/bb3fc05186d30d5d5614691dad86b9ce.png)
	- LDAP URL：请填写 LDAP 服务器 IP 与端口号。若服务器 IP 为196.0.0.0，端口号为389，则填写`ldap://196.0.0.0:389/`，目前暂不支持 IPv6。
	- LDAP Base：LDAP 中的节点，认证时将会从该节点下匹配用户节点进行认证，如：`dc=users,dc=com`。
	- LDAP 账户：请填写有上述 LDAP Base 管理权限的节点，认证过程需有管理权限才能进行，如：`cn=administrator,dc=users,dc=com`。
	- LDAP 账户密码：请填写上述 LDAP 账户对应的密码。
	- 用户过滤条件：请填写 LDAP 匹配腾讯云 IDaaS 用户 ID 的过滤条件，如：`sAMAccountName=$userId$`，$userId$ 为本系统用户 ID 参数，是目录用户唯一标识符。具体规则可参考 [LDAP 官方文档](https://ldap.com/ldap-filters/)。
4.	单击【提交】，LDAP 认证源配置成功！

