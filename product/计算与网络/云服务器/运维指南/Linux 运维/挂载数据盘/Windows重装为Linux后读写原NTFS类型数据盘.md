## 操作场景

Windows 的文件系统通常使用 NTFS 或者 FAT32 格式，Linux 的文件系统通常使用 EXT 系列的格式。当云服务器的操作系统从 Windows 重装为 Linux，操作系统的类型虽然发生了改变，但是云服务器中的数据盘仍为原系统所使用的格式。因此，重装系统后的云服务器可能会出现无法访问数据盘文件系统的情况。本文档指导您在重装系统后的 Linux 云服务器上，读取原 Windows 系统下的数据盘数据。

## 操作步骤

### 配置 Linux 系统支持 NTFS 

1. 登录重装系统后的 Linux 云服务器。
2. 执行以下命令，安装 ntfsprogs 软件，使得 Linux 云服务器支持访问 NTFS 文件系统。
```
yum install ntfsprogs
```

###  将 Windows 云服务器下的数据盘挂载至 Linux 云服务器

>? 若您 Windows 云服务器下的数据盘已挂载至 Linux 云服务器，则可跳过此操作。
>
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。
2. 在左侧导航栏中，单击【[云硬盘](https://console.cloud.tencent.com/cvm/cbs)】，进入云硬盘管理页面。
3. 选择需要进行挂载的 Windows 数据盘，单击【更多】>【挂载】。如下图所示：
![](https://main.qcloudimg.com/raw/d227d87d0b750ddaf38295b2e20ccb39.png)
4. 在弹出的 “挂载到实例” 窗口中，选择需要挂载至的 Linux 云服务器，单击【确定】。
5. 登录已挂载 Windows 数据盘的 Linux 云服务器。
6. 执行以下命令，查看从 Windows 云服务器中挂载过来的数据盘。
```
parted -l
```
返回类似如下信息：
```
Model: Virtio Block Device (virtblk)
Disk /dev/vdb: 53.7GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags: 
Number  Start   End     Size    File system  Name                          Flags
 1      17.4kB  134MB   134MB                Microsoft reserved partition  msftres
 2      135MB   53.7GB  53.6GB  ntfs         Basic data partition
```
7. 执行以下命令，挂载数据盘。
```
mount -t ntfs-3g 数据盘路径 挂载点
```
例如，您需要将路径为 `/dev/vdb1` 的数据盘挂载至 `/mnt`，则执行以下命令：
```
mount -t ntfs-3g /dev/vdb1 /mnt
```
由于此时的文件系统可识别，挂载的数据盘可直接被 Linux 系统读写。

