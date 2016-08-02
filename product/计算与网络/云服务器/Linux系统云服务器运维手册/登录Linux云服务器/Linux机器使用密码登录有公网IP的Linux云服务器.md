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

## 2. 下载并安装客户端软件
从本地linux机器登录到linux云服务器时，需要使用客户端软件建立连接。

建议使用OpenSSH发布的ssh工具进行登录。 

在本地机器上下载并安装OpenSSH客户端（下载地址：http://www.openssh.com/portable.html ）。 

## 3. 登录到Linux云服务器
操作示例：
![](//mccdn.qcloud.com/img56a5965a017c5.png)

1) 使用命令行连接linux云服务器：

```
ssh -q -l [云服务器登录账号] -p 22 [云服务器的公网IP]
```

参数说明：
- 云服务器登录账号：输入第一步中获取的管理员账号。
SUSE/CentOS/Debian：root
Windows：Administrator
ubuntu：ubuntu 

- 云服务器的公网IP：登录[腾讯云控制台云服务器页面](https://console.qcloud.com/cvm)，可在列表页及详情页中获取主机公网IP。

2) 回车后，如果控制台询问是否继续链接“Are you sure you want to continue connecting（yes/no）?”，输入”yes“。

3) 在Password后输入密码，密码为第一步中获取的管理员账号的密码，回车后即完成登录。

>注：管理员账号的初始密码由系统分配，用户可以重置密码，详见[重置主机密码](http://www.qcloud.com/doc/product/213/CVM%E5%AE%9E%E4%BE%8B%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97#6.-重置主机密码)。 