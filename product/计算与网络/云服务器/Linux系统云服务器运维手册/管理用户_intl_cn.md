腾讯云的 Linux 类型实例均使用默认的 Linux 系统用户账户启动。对于CentOS、CoreOS、Debian、SUSE 等系统，用户名称是 root；对于 Ubuntu 系统，用户名称是 ubuntu；对于 Windows 系统，用户名称是 Administrator。

在一般的应用场景下，使用默认用户账户就可以满足应用需求。添加系统用户可以使不同的用户拥有私有文件和对系统的访问权限。为一些操作人员创建用户帐号并赋予特定权限比告知密码并使用系统默认帐号 更加安全。

> 注意：Linux 系统用户与 [协作者用户]() 是两个概念，请勿混淆。

## 添加新用户

要将新用户添加到系统，请使用 `useradd` 命令，后跟所有相关选项和要创建的用户名称。

```
adduser newuser
```
上述命令将 newuser 用户添加到系统，并创建 newuser 组，在 /home/newuser 中为该用户创建主目录。

## 设置新用户密码
使用 `passwd` 命令设置用户密码。

```
passwd newuser userpassword
```
上述命令将 newuser 用户的密码设置为 `userpassword`。这时用户 `newuser` 就可以通过密码 `userpassword`来登录系统了。

## 从系统中删除用户

如果不再需要某个用户账户，可以将其删除，root 用户运行 `userdel -r <newuser> `命令即可将用户名为 `newuser` 的用户帐号删除。