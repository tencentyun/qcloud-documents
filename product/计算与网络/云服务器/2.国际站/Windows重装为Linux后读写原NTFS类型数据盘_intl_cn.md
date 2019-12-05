Windows的文件系统通常使用NTFS或者FAT32格式，而Linux的文件系统格式通常是EXT系列。当操作系统从Windows重装为Linux后，操作系统类型发生了变化，而数据盘仍然是原来的格式，重装后的系统可能出现无法访问数据盘文件系统的情况。可在重装后的Linux云服务器上执行以下操作读取原Windows系统下数据盘数据：

1) 在Linux系统上使用以下命令安装ntfsprogs软件使得Linux能够支持NTFS文件系统：

```
yum install ntfsprogs
```

2) 将Windows下的数据盘挂载至Linux云服务器，若数据盘已挂载则可跳过此步骤：

登录腾讯云控制台，进入【云服务器】-【云硬盘】选项卡，点击需要挂载的Windows数据盘【更多】-【挂载到云主机】按钮。在弹出框中选择重装后的Linux云服务器，点击【确定】按钮。

3) 使用命令`parted -l`查看从Windows中挂载过来的数据盘：
![](//mccdn.qcloud.com/static/img/f0839d9209bc0927bd5293b45fdc7608/image.png)

4) 使用命令`mount -t ntfs-3g 数据盘路径 挂载点` 挂载数据盘：
![](//mccdn.qcloud.com/static/img/cab81165b08034f2c300a2f30fccc8a4/image.png)

5) 由于可识别此文件系统，挂载的数据盘可直接被Linux系统读写。