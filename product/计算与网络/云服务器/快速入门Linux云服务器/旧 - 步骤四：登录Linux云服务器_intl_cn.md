本文档介绍了用户从本地登录Linux云服务器的几种方法。更多登录方法请参见【Linux云服务器运维手册】-【登录Linux云服务器】。

1) 不管是否购买了公网带宽/流量，不管您本地客户端是何种操作系统，云服务器均可从控制台登录。在云服务器列表的操作列，点击【登录】按钮即可通过VNC连接至Linux云服务器。

![](//mccdn.qcloud.com/img56b1a6cb7b3e8.png)

输入帐号（除Ubuntu系统用户为ubuntu外，其余系统均为root）和站内信中的初始密码（或您修改后的密码）即可登录。

>注：该终端为独享，即同一时间只有一个用户可以使用控制台登录。


2) 对于有购买公网带宽/流量的Linux云服务器，这里介绍一种使用密码从本地Windows登录的方法：

购买云服务器成功后，登录[腾讯云控制台](https://console.qcloud.com/)，点击右侧站内信按钮，查收新购买的服务器页面中将包含云主机登录管理员帐号及初始密码，如下图所示。
![](//mccdn.qcloud.com/img56a20f10a373a.png)

下载远程链接软件Putty，参考下载地址：http://www.chiark.greenend.org.uk/~sgtatham/putty/

打开Putty客户端，在PuTTY Configuration 窗口中输入以下内容：
- Host Name：Linux云服务器的公网IP。
- Port：云服务器的端口，必须填22。（请确保云主机22端口已开放）
- Connect type：选择“SSH”。

全部输入完后，点击“Open”，创建一个新对话。
![](//mccdn.qcloud.com/img56a5d38a4ffbc.png)

在Putty会话窗口中， 输入管理员帐号，按回车键。
>管理员帐号：
SUSE/CentOS/Debian：root
ubuntu：ubuntu 

再输入初始密码，回车完成登录过程。
![](//mccdn.qcloud.com/img56a5d47b8b5da.png)

3) 从本地Linux或Mac OS登录Linux云服务器，直接使用SSH命令进行连接，如：ssh root@Linux云服务器公网IP，然后输入root用户的初始密码，即可完成登录。