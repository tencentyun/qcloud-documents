## 1. 获取云主机管理员帐号及初始密码
登录到云服务器时，需要使用管理员帐号和对应的密码。用户购买云服务器后，会通过消息中心的通知消息，告知用户管理员账号及初始密码。 
- 管理员账号：
服务器的操作系统不同，管理员帐号也会不一样，如下所示：
SUSE/CentOS/Debian：root
Windows：Administrator
ubuntu：ubuntu 
- 初始密码：
初始密码由系统随机分配，一个订单对应的服务器有一个初始密码，请及时修改密码。 

购买云服务器成功后，登录[腾讯云控制台](https://console.cloud.tencent.com/)，点击右侧站内信按钮，查收新购买的服务器页面中将包含云主机登录管理员帐号及初始密码，如下图所示。
![](//mccdn.qcloud.com/img56a20f10a373a.png)

## 2. 安装Windows客户端软件
从本地Windows机器登录到Linux云服务器时，需要使用客户端软件建立连接。

建议使用SecureCRT、putty客户端进行登录。

参考下载地址：https://www.chiark.greenend.org.uk/~sgtatham/putty/

## 3. 使用Putty连接Linux云服务器
打开Putty客户端，在PuTTY Configuration 窗口中输入以下内容：
- Host Name：云服务器的公网IP（登录[腾讯云控制台云服务器页面](https://console.cloud.tencent.com/cvm)，可在列表页及详情页中获取主机公网IP）。
- Port：云服务器的端口，必须填22。（请确保云主机22端口已开放，详见查看[安全组](http://cloud.tencent.com/doc/product/213/%E5%AE%89%E5%85%A8%E7%BB%84%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97)及网络ACL）
- Connect type：选择“SSH”。

全部输入完后，点击“Open”，创建一个新对话。
![](//mccdn.qcloud.com/img56a5d38a4ffbc.png)

在Putty会话窗口中， 输入管理员帐号，按回车键。
>管理员帐号：
SUSE/CentOS/Debian：root
ubuntu：ubuntu 

再输入第一步中获取的登录密码，回车完成登录过程。
![](//mccdn.qcloud.com/img56a5d47b8b5da.png)


## 4. 使用SecureCRT连接Linux云服务器
启动SecureCRT客户端，点击菜单栏“文件”->“连接”，打开“连接”对话框，点击对话框上的“新建会话”按钮，打开新建会话向导，协议选择“SSH2”，如下图所示：

![](//mccdn.qcloud.com/img56a2104a85e65.png)

点击“下一步”，在会话向导中进行如下配置：

1) 主机名：云服务器的公网IP（登录[腾讯云控制台云服务器页面](https://console.cloud.tencent.com/cvm)，可在列表页及详情页中获取主机公网IP）。

2) 端口：云服务器的端口，必须填22。（请确保云主机22端口已开放，详见查看[安全组](http://cloud.tencent.com/doc/product/213/%E5%AE%89%E5%85%A8%E7%BB%84%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97)及网络ACL）

3) 用户名：输入管理员账号。
SUSE/CentOS/Debian：root
Windows：Administrator
ubuntu：ubuntu 

如下图所示：
![](//mccdn.qcloud.com/img56a212155843e.png)

点击“下一步”，确定该会话的名字（默认为之前输入的云服务器公网IP），点击“完成”，即创建了1个会话。 

在“连接”窗口，右键点击新建的会话，选择“属性”后，在弹出的“会话选项”中，取消勾选“公钥”，如下图所示：

![](//mccdn.qcloud.com/img56a592adc21f0.png)

这里不对公钥进行鉴权，因此需要取消勾选“公钥”。

在“连接”窗口的会话列表中，可以看到之前创建的会话，选中后，点击“连接”按钮，即开始连接Linux云服务器。
![](//mccdn.qcloud.com/img56a5933ce992f.png)

在弹出的输入密码对话框中，输入密码，密码为管理员账号的密码。点击“确定”，即完成登录。
![](//mccdn.qcloud.com/img56a5935421274.png)

点击菜单“选项”->“会话选项”->“终端”，打开终端设置对话框，设置发送协议，可在网络环境正常的情况下空闲时保持会话不断开。
![](//mccdn.qcloud.com/img56a5944e4604e.png)