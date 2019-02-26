Windows 的文件系统通常使用 NTFS 或者 FAT32 格式，而 Linux 的文件系统格式通常是 EXT 系列。当操作系统从 Windows 重装为 Linux 后，操作系统类型发生了变化，而数据盘仍然是原来的格式，因此重装后的系统可能出现无法访问数据盘文件系统的情况。
用户可在重装后的 Linux 云服务器上执行以下操作读取原 Windows 系统下的数据盘数据：

1. 在 Linux 系统上使用以下命令安装 ntfsprogs 软件使得 Linux 系统能够支持 NTFS 文件系统：
```
yum install ntfsprogs
```
2. 将 Windows 下的数据盘挂载至 Linux 云服务器。若数据盘已挂载则可跳过此步骤。
登录 [腾讯云控制台](https://console.cloud.tencent.com/cvm/overview)，进入左侧【云硬盘】选项卡，单击需要进行挂载的 Windows 数据盘对应的【更多】>【挂载到云主机】按钮。在弹出框中选择重装后的 Linux 云服务器，单击 【确定】 按钮即可完成挂载。
3. 在 Linux 云服务器上使用命令  查看从 Windows 中挂载过来的数据盘。
```
parted -l
```
![](//mccdn.qcloud.com/static/img/f0839d9209bc0927bd5293b45fdc7608/image.png)
4. 使用命令挂载数据盘。
命令格式
```
mount -t ntfs-3g 数据盘路径 挂载点
```
命令示例：
```
mount -t ntfs-3g /dev/vdb1 /mnt
```

由于此时的文件系统可识别，挂载的数据盘可直接被 Linux 系统读写。
