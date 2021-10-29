## 操作场景
当企业内部使用 LDAP 时，用户可以使用 LDAP 账号登录堡垒机，管理人员也可以直接从 LDAP 同步用户到堡垒机，这样就不需要单独维护堡垒机的用户管理体系，简化管理流程。
>?如果您有 LDAP 认证的需求，请 [联系我们](https://cloud.tencent.com/online-service?from=connect-us) 开通该功能。

## 操作步骤
1. 登录 [堡垒机控制台](https://console.cloud.tencent.com/dsgc/bh)，单击**进入**，进入 SaaS 型堡垒机控制台。
![](https://main.qcloudimg.com/raw/c4d6945d8c76ed1ae7bb8821fde8b41d.png)
2. 在左侧导航选择**系统设置** > **认证设置**，进入认证设置页面。
![](https://main.qcloudimg.com/raw/8a3ecc4e4d96eebaffa38dd1134153a3.png)
3. 默认会进入到本地认证页面，单击**LDAP**，切换到 LDAP 设置页面。
![](https://main.qcloudimg.com/raw/a89a544c54b51550aa7374e70a9d6ac9.png)
4. 默认情况下，LDAP 状态为禁用状态，可单击![](https://main.qcloudimg.com/raw/f6fde0ec127d1f49dce725a2b8270fa0.png)图标启用 LDAP，需配置如下 LDAP 信息。
>!页面标*的为必填项。
>
![](https://main.qcloudimg.com/raw/cb94097fc2a91a6659340ef0a20b56bc.png)

**参数列表：**

| 参数名称           | 参数说明                                                     |
| ------------------ | :----------------------------------------------------------- |
| 服务器 IP 地址     | 输入 LDAP 服务器的 IP 地址。                                 |
| 备用服务器 IP 地址 | 如果您的 LDAP 服务器有多个 IP，可以输入一个备用的 IP 地址。  |
| SSL                | 设置是否启用 SSL。                                           |
| 服务端口           | 输入 LDAP 服务器的端口。                                     |
| Base DN            | 输入 LDAP 服务器的 Base DN 信息，格式为：ou=ouname,dc=test,do=com。 |
|	管理员账号          | 输入管理员的账号信息，格式为：cn=admin, ou=ouname,dc=test,dc=com。 |
| 管理员密码         | 输入管理员账号的密码信息。                                   |
| 用户过滤           | 输入用户过滤条件。                                           |
| 用户名属性映射     | 输入在 LDAP 里面表示用户名的属性。                     |
| 自动同步           | 设置是否启用自动同步用户。                                   |
| 覆盖已存在的用户   | 设置是否当用户名相同时，使用 LDAP 内的用户信息覆盖堡垒机内已存在的用户信息。 |
| 同步周期           | 输入自动同步 LDAP 用户的周期。                               |
| 部门过滤           | 设置部门过滤条件。                                           |
| 同步OU             | 选择要同步用户所在的 OU。                                    |
| 姓名属性映射       | 输入在 LDAP 里面表示用户姓名的属性。                       |
| 手机号属性映射     | 输入在 LDAP 里面表示用户手机号的属性。                             |
| 邮箱属性映射       |输入在 LDAP 里面表示用户邮箱的属性。                         |

5. 输入所需信息后，单击**确定**，即可保存设置。
6. 如果开启了自动同步，单击**确定**之后，会弹出弹窗询问是否立即同步，根据实际需要选择“是”或“否”即可。
![](https://main.qcloudimg.com/raw/1d32214d1cce386f10346f4ee1de8d39.png)
