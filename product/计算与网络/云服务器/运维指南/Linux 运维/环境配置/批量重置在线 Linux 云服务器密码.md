## 操作场景

本文档介绍在非关机状态下，多个 Linux 系统云服务器进行批量重置密码的操作。

## 下载脚本
腾讯云已为您编写好重置操作的脚本，下载并解压缩该重置脚本至云服务器中，可方便的批量在线重置。
获取路径：`http://batchchpasswd-10016717.file.myqcloud.com/batch-chpasswd.tgz`

## 操作步骤

### CentOS / SUSE 系统的操作方法

1. 执行以下命令，打开 `hosts.txt` 文件。
```
vi /etc/hosts
```
2. 按 **i** 或 **Insert** 切换至编辑模式，按照【云服务器 IP + SSH 端口号 + 帐号 + 旧密码 + 新密码】格式，将需要修改的云服务器信息添加到 `hosts.txt` 文件内。如下所示：
```
10.0.0.1 22 root old_passwd new_passwd 
10.0.0.2 22 root old_passwd new_passwd
```
>? 每一行信息即代表一个云服务器。若您在公网上运行该脚本，云服务器 IP 填写**公网 IP**；若您在内网上运行该脚本，云服务器 IP 填写**内网 IP**。
>
3. 按 **Esc**，输入 **:wq**，保存文件并返回。
4. 执行以下命令，运行脚本文件。
```
./batch-chpasswd.py
```
返回类似以下结果，即表示重置成功。
```
change password for root@10.0.0.1
spawn ssh root@10.0.0.1 -p 22
root password: 
Authentication successful.
Last login: Tue Nov 17 20:22:25 2015 from 10.181.XXX.XXX
[root@VM_18_18_centos ~]# echo root:root | chpasswd
[root@VM_18_18_centos ~]# exit
logout
change password for root@10.0.0.2
spawn ssh root@10.0.0.2 -p 22
root password: 
Authentication successful.
Last login: Mon Nov  9 15:19:22 2015 from 10.181.XXX.XXX
[root@VM_19_150_centos ~]# echo root:root | chpasswd
[root@VM_19_150_centos ~]# exit
logout
```

### Ubuntu 系统的操作方法

1. 执行以下命令，打开 `hosts.txt` 文件。
>? 此处调用系统默认编辑器，您也可以使用其它文本编辑器编辑。
>
```
sudo gedit /etc/hosts
```
2. 按 **i** 或 **Insert** 切换至编辑模式，按照【云服务器 IP + SSH 端口号 + 帐号 + 旧密码 + 新密码】格式，将需要修改的云服务器信息添加到 `hosts.txt` 文件内。如下所示：
```
10.0.0.1 22 root old_passwd new_passwd 
10.0.0.2 22 root old_passwd new_passwd
```
>? 每一行信息即代表一个云服务器。若您在公网上运行该脚本，云服务器 IP 填写**公网 IP**；若您在内网上运行该脚本，云服务器 IP 填写**内网 IP**。
>
3. 执行以下命令，重启网络。
```
sudo rcnscd restart
```
4. 执行以下命令，运行脚本文件。
```
python batch-chpasswd.py
```
