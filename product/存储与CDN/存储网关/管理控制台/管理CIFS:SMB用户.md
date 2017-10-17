# 管理 CIFS/SMB 用户

登录控制台后，可以到 "文件共享->CIFS/SMB用户" 菜单下管理 SMB 文件网关的用户。
![](https://mc.qcloudimg.com/static/img/1844afdea6b5c428eb5e5cb204e52025/image.png)

## 查看用户信息

点击列表中 “用户名” 可以进入用户详情页面，查看用户详细信息。
![](https://mc.qcloudimg.com/static/img/eb6ea81fd40aec4aed6a056846467e1b/image.png)


## 编辑用户信息

在用户详细信息页面，点击编辑图标修改用户详情和文件系统权限。**注意，若有客户端正使用该用户挂载或访问文件系统，此时修改密码或文件系统权限可能导致正在使用的文件系统因为失去权限而不可用。另，若使用 Linux 挂载 SMB 文件系统，由于协议限制，修改用户权限或密码后需要重启客户端才能生效。**
![](https://mc.qcloudimg.com/static/img/aaf0bd8aa9ace5c98df757ca7f792ff9/image.png)
![](https://mc.qcloudimg.com/static/img/188df01176ce3697658675abf43e2ea1/image.png)

## 禁用/启用用户

当需要禁用用户账户时，可以从 CIFS/SMB 用户列表的 “操作” 栏中找到【禁用】或【启用】按钮。在弹窗中点击【立即禁用】或者【立即启用】按钮来改变用户状态。**注意，若有客户端正使用该用户挂载或访问文件系统，此时修改密码或文件系统权限可能导致正在使用的文件系统因为失去权限而不可用。另，若使用 Linux 挂载 SMB 文件系统，由于协议限制，修改用户权限或密码后需要重启客户端才能生效。**
![](https://mc.qcloudimg.com/static/img/00ccf74c97a308ca95f7eef325f2ebd6/image.png)
![](https://mc.qcloudimg.com/static/img/55a2f0e5cd77217355f00fd845e27665/image.png)

## 删除用户

当需要删除用户时，可以从 CIFS/SMB 用户列表的 “操作” 栏中找到【删除】按钮。在弹窗中点击【立即删除】按钮删除该用户。
![](https://mc.qcloudimg.com/static/img/3e79cdb1989efa6d68c86b0151cda0c5/image.png)



