## 现象描述
访问 Linux 资源，使用选择远程工具进行登录，提示“invalid password/key”，如下图所示：
![](https://main.qcloudimg.com/raw/fbe125454272f5a775f76dd6f0bc97be.png)

## 可能原因
资源账户信息录入错误，或者资源进行了 SSH 登录限制策略。

## 解决思路
1. 检查资源录入的账号密码是否正确，如果有误进行重新录入。
2. 确认资源是否设置了只允许通过密钥的方式进行登录，不允许通过密码进行登录，可以在堡垒机设置托管密钥的方式登录，或者在资源系统内取消登录限制。

## 处理步骤
1. 登录 [ SaaS 型堡垒机控制台](https://console.cloud.tencent.com/bh)，在左侧导航选择【主机管理】>【主机】，进入主机页面。
2. 在主机页面，找到相关账号，单击【主机账号】，弹出账号管理弹窗。
![](https://main.qcloudimg.com/raw/cb3090c0e36b92ffd3fe5587bd63d235.png)
3. 在账号管理弹窗，单击密码的【设置】，重新设置密码。
![](https://main.qcloudimg.com/raw/ca183a99de22514e405710f23aad7f46.png)
4. 在账号管理弹窗，单击私钥的【设置】，设置托管私钥。
![](https://main.qcloudimg.com/raw/28552914c789ead1032f4f609c9d7022.png)
5. 如若以上设置托管账号密码密钥无误，请检查资源 SSH 配置文件，设置资源允许密码登录：修改`/etc/ssh/sshd_config` 配置文件，将 PasswordAuthentication 所在行选项改为 yes。具体情况如下所示：
 - **情况1**
    - 故障原因：如果资源设置了不允许 root 账号通过 SSH 登录，将会导致使用 root 用户登录资源失败。
    - 解决方法：在修改 `/etc/ssh/sshd_config ` 配置文件中，找到 PermitRootLogin 所在行，并修改对应的值为 yes。
 - **情况2**
    - 故障原因：如果资源设置了 SSH 白名单，将会导致只允许部分用户登录，此时，需要把对应的账号加入到白名单中。
	- 解决方法：在  `/etc/ssh/sshd_config` 配置文件中，设置 AllowUsers 选项，添加对应的账号。
