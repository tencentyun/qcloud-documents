If you need to reset password for a batch of Linux CVMs without shutting them down, you can download the reset script ([Click here to download](http://batchchpasswd-10016717.file.myqcloud.com/batch-chpasswd.tgz)) to batch reset password online.

>Note: If you run the script on a machine of public network, the ip added to the hosts.txt file must be the<font color="red"> Public IP </font>of the host. If the script is run on the private network CVM of Tencent Cloud, you can fill in the <font color="red">Private IP</font> of the host.


The using method of script is as follows.

Input the ip of CVM to be operate on, ssh port, account, old and new passwords into the hosts.txt file. Each line represents a host, for example:

```
10.0.0.1 22 root old_passwd new_passwd 
10.0.0.2 22 root old_passwd new_passwd
```


Run the following code:

```
./batch-chpasswd.py
```

Example of returned results:

```
-----------------------------------------------------------------
change password for root@10.0.0.1
spawn ssh root@10.0.0.1 -p 22
root's password: 
Authentication successful.
Last login:  Tue Nov 17 20:22:25 2015 from 10.181.225.39
[root@VM_18_18_centos ~]# echo root:root | chpasswd
[root@VM_18_18_centos ~]# exit
logout
-----------------------------------------------------------------
change password for root@10.0.0.2
spawn ssh root@10.0.0.2 -p 22
root's password: 
Authentication successful.
Last login:  Mon Nov  9 15:19:22 2015 from 10.181.225.39
[root@VM_19_150_centos ~]# echo root:root | chpasswd
[root@VM_19_150_centos ~]# exit
logout
```