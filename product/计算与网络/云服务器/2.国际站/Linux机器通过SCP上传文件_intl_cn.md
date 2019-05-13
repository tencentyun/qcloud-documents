Linux机器可通过以下命令向Linux云服务器上传文件：

```
scp 本地文件地址 云服务器登录名@云服务器公网IP/域名 云服务器文件地址
```

例如，将本地文件”/home/lnmp0.4.tar.gz“上传到IP为129.20.0.2的CentOS云服务器对应目录下：

```
scp /home/Inmp0.4.tar.gz root@129.20.0.2 /home/Inmp0.4.tar.gz
```

按回车键并输入登录密码即可完成上传。