本文档介绍在多个 Linux 系统云服务器非关机状态下批量进行重置密码的操作。

## 脚本下载
腾讯云已为您编写好重置操作的脚本，下载该重置脚本，可方便的批量在线重置。下载地址：`http://batchchpasswd-10016717.file.myqcloud.com/batch-chpasswd.tgz`

## CentOS / SUSE 系统操作方法
1. 修改 hosts.txt 文件。输入命令：`vi /etc/hosts`
将需要修改的信息按照【云服务器 IP + SSH端口号 + 账号 + 旧密码 + 新密码】格式添加到文件内，每一行代表一个主机，如：
```
10.0.0.1 22 root old_passwd new_passwd 
10.0.0.2 22 root old_passwd new_passwd
```
>**注意：**
>若在公网上运行该脚本，云服务器 IP 填写** 公网 IP** ；
>若在内网上运行该脚本，云服务器 IP 填写** 内网 IP** 。

2. 执行脚本文件。输入命令：`./batch-chpasswd.py`

3. 返回示例：

```
-----------------------------------------------------------------
change password for root@10.0.0.1
spawn ssh root@10.0.0.1 -p 22
root password: 
Authentication successful.
Last login: Tue Nov 17 20:22:25 2015 from 10.181.XXX.XXX
[root@VM_18_18_centos ~]# echo root:root | chpasswd
[root@VM_18_18_centos ~]# exit
logout
-----------------------------------------------------------------
change password for root@10.0.0.2
spawn ssh root@10.0.0.2 -p 22
root password: 
Authentication successful.
Last login: Mon Nov  9 15:19:22 2015 from 10.181.XXX.XXX
[root@VM_19_150_centos ~]# echo root:root | chpasswd
[root@VM_19_150_centos ~]# exit
logout
```

## Ubuntu 系统操作方法
1. 修改 hosts.txt 文件。输入命令：`sudo gedit /etc/hosts`。此处调用系统默认编辑器，也可以使用其它文本编辑器编辑。
将需要修改的信息按照【云服务器 IP + SSH端口号 + 账号 + 旧密码 + 新密码】格式添加到文件内，每一行代表一个主机，如：
```
10.0.0.1 22 root old_passwd new_passwd 
10.0.0.2 22 root old_passwd new_passwd
```
>**注意：**
>若在公网上运行该脚本，云服务器 IP 填写** 公网 IP** ；
>若在内网上运行该脚本，云服务器 IP 填写** 内网 IP** 。

2. 重启网络。输入命令：`sudo rcnscd restart`

3. 执行脚本文件。输入命令：`python batch-chpasswd.py`
