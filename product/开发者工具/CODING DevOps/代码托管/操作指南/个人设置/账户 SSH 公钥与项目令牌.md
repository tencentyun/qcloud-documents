SSH 公钥在 CODING 中会因使用场景的差异而有不同的权限范围。本文为您介绍账户 SSH 公钥与项目令牌的区别。

## 功能介绍[](id:intro)

SSH 公钥文件与 CODING 账户关联，便称为**账户 SSH 公钥**，配置后拥有账户下所有项目的读写权限；如果和某一个项目关联，则称为**项目令牌**，配置后默认拥有该项目的只读权限。

## 生成公钥[](id:generate)

执行命令：
<dx-codeblock>
:::  shell
ssh-keygen -m PEM -t rsa -b 4096 -C "your.email@example.com"
# Creates a new ssh key, using the provided email as a label
# Generating public/private rsa key pair.
Enter file in which to save the key (/Users/you/.ssh/id_rsa): [Press enter]  // 推荐使用默认地址
Enter passphrase (empty for no passphrase):   // 此处不填写，回车即可；如果填写密码，则每次使用 SSH 方式推送代码时都会要求输入密码。
:::
</dx-codeblock>

若需要使用多个 SSH 密钥对（您可能同时在多个代码托管平台工作），在提示“Enter file in which to save the key” 时输入一个新的文件名称就不会覆盖默认的密钥对。

成功之后显示如下信息：
<dx-codeblock>
:::  shell
Your identification has been saved in /Users/you/.ssh/id_rsa.
# Your public key has been saved in /Users/you/.ssh/id_rsa.pub.
# The key fingerprint is:
# 01:0f:f4:3b:ca:85:d6:17:a1:7d:f0:68:9d:f0:a2:db your.email@example.com
:::
</dx-codeblock>


## 添加账户 SSH 公钥[](id:account-ssh)

1.  在终端输入 `open ~/.ssh`，用文本编辑器打开 `id_rsa.pub` 文件（此处是生成公钥的默认名称，如果生成公钥时采用了其他名称，打开相对应的文件即可），复制全部内容。
2.  单击页面右上角个人头像，选择**个人账户设置**。进入**个人账户设置** > **个人设置** > **SSH 公钥**页面。
![](https://main.qcloudimg.com/raw/71acf741ab2defb581f00ff8db1e4ba3.png)
3.  将第一步中复制的内容填写到**公钥内容**一栏，公钥名称按需填写即可。
4.  设定公钥有效期，可选择具体日期或设置永久有效。
![](https://main.qcloudimg.com/raw/c810b6aeed57ebf265e3a6ce675d8c8f.png)
5.  单击**添加**，然后输入账户密码即可成功添加公钥。
6.  完成后在命令行测试，首次建立链接会要求信任主机。命令 `ssh -T git@e.coding.net`。您也可以通过 [密钥指纹鉴权](/docs/repo/ssh/fingerprint.html) 验证是否与真正的 CODING 远程仓库所连接。

## 添加部署公钥[](id:project-ssh)

1.  在终端输入 `open ~/.ssh`，用文本编辑器打开 `id_deploy.pub` 文件（此处部署公钥名称为 `id_deploy.pub`，您在生成部署公钥的时候可以自定义名称），复制全部内容。
2.  进入目标项目内的代码仓库 > **部署公钥**页面，单击**新建部署公钥**。
![](https://main.qcloudimg.com/raw/9c44450f435bb267f05fa21b4d27dbcc.png)
3.  将第一步中复制的内容填写到**公钥内容**一栏，公钥名称自定义。
4.  单击**新建**，然后输入账户密码即可成功添加部署公钥。

>?部署公钥默认拥有该项目的只读权限，如果需要获取推送权限，请勾选**授予推送权限**。
