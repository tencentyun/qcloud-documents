## 1. 获取云主机管理员帐号及初始密码
登录到云服务器时，需要使用管理员帐号和对应的密码。用户购买云服务器后，会通过消息中心的通知消息，告知用户管理员账号及初始密码。 
- 管理员账号：
服务器的操作系统不同，管理员帐号也会不一样，如下所示：
SUSE/CentOS/Debian：root
Windows：Administrator
ubuntu：ubuntu 
- 初始密码：
初始密码由系统随机分配，一个订单对应的服务器有一个初始密码，请及时修改密码。 

购买云服务器成功后，登录[腾讯云控制台](https://console.qcloud.com/)，点击右侧站内信按钮，查收新购买的服务器页面中将包含云主机登录管理员帐号及初始密码，如下图所示。
![](//mccdn.qcloud.com/img56a20f10a373a.png)

## 2. 远程桌面连接
在本地Windows机器上，点击开始菜单 -> Run，输入"mstsc"命令，即可打开远程桌面连接对话框。

在输入框输入Windows服务器的公网IP（登录[云服务器控制台](https://console.qcloud.com/cvm)可查看云服务器的公网IP），如下图所示：
![](//mccdn.qcloud.com/img56b1a11a3c31f.png)

点击“连接”，在新打开的界面中输入上一步骤中获取的管理员账号和对应的密码（Windows服务器管理员账号固定为Administrator），如下图所示：
![](//mccdn.qcloud.com/static/img/878a0e8ef1a0bcc51ad5de2bcce4e353/image.png)
![](//mccdn.qcloud.com/static/img/e140d3151ac8747014313b33e6413568/image.png)

点击【确定】，即可登录到Windows云服务器。 