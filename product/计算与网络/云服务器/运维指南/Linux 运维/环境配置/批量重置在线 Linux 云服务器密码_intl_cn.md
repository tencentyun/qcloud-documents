如果您有一批Linux的云服务器需要批量进行不关机的情况下重置密码操作。您可以下载该重置脚本（[点击这里下载](http://batchchpasswd-10016717.file.myqcloud.com/batch-chpasswd.tgz)），可方便的批量在线重置。

>注：若您在公网的机器上，运行该脚本，填到hosts.txt的文件内的ip需为主机的<font color="red">公网IP</font>，若是腾讯云内网CVM上使用该脚本，则可以填写主机<font color="red">内网IP</font>。


脚本使用方法如下。

将需要操作的云主机的ip，ssh的端口，账号，旧密码和新密码写到hosts.txt文件中，每一行代表一个主机，比如：

```
10.0.0.1 22 root old_passwd new_passwd 
10.0.0.2 22 root old_passwd new_passwd
```


执行如下代码：

```
./batch-chpasswd.py
```

返回示例：

```
-----------------------------------------------------------------
change password for root@10.0.0.1
spawn ssh root@10.0.0.1 -p 22
root's password: 
Authentication successful.
Last login: Tue Nov 17 20:22:25 2015 from 10.181.225.39
[root@VM_18_18_centos ~]# echo root:root | chpasswd
[root@VM_18_18_centos ~]# exit
logout
-----------------------------------------------------------------
change password for root@10.0.0.2
spawn ssh root@10.0.0.2 -p 22
root's password: 
Authentication successful.
Last login: Mon Nov  9 15:19:22 2015 from 10.181.225.39
[root@VM_19_150_centos ~]# echo root:root | chpasswd
[root@VM_19_150_centos ~]# exit
logout
```