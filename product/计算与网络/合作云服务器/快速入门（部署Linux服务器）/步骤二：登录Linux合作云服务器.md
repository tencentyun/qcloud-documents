## 从本地登录Linux云服务器的几种方法。

### 获取密码

- 如果您选择的是自动生成密码，请登录控制台，单击右侧站内信按钮，查收新购买的服务器页面中将包含合作云服务器的登录管理员帐号和初始密码；如果您选择的是自定义密码，直接使用自定义密码即可。

### 远程密码登录

1） 下载远程链接软件Putty，参考下载地址：https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html

打开Putty客户端，在PuTTY Configuration 窗口中输入以下内容：
- Host Name：Linux合作云服务器的公网IP。
- Port：与合作云服务器的通信端口，必须填22。（请确保合作云服务器的22端口已开放）
- Connection type：选择“SSH”。

全部输入完后，单击“Open”，创建一个新对话。
![Alt text](http://mc.qcloudimg.com/static/img/2ddbfe58c5fd6e2a783bb92fa51124b8/image.png)

在Putty会话窗口中， 输入管理员帐号，按回车键。
>管理员帐号：
ubuntu/CentOS/Debian：root


再输入初始密码，回车完成登录。
![Alt text](https://mccdn.qcloud.com/img56a5d47b8b5da.png)

2) 从本地Linux或Mac OS登录Linux合作云服务器，直接使用SSH命令进行连接，如：ssh root@Linux云服务器公网IP，然后输入root用户的初始密码，即可完成登录。
