Windows的文件系统通常使用NTFS或者FAT32格式，而Linux的文件系统格式通常是EXT系列。当操作系统从Linux重装为Windows后，操作系统类型发生了变化，而数据盘仍然是原来的格式，重装后的系统可能出现无法访问数据盘文件系统的情况。可在重装后的Windows云服务器上执行以下操作读取原Linux系统下数据盘数据：

1) 假设重装前Linux云服务器数据盘有以下两个分区：
![](//mccdn.qcloud.com/static/img/4a77fec831a1ad58b18cd86c31952789/image.png)

2) 在重装后的Windows云服务器上下载并安装DiskInternals Linux Reader软件（下载地址请点[这里](http://www.diskinternals.com/download/Linux_Reader.exe)）。

3) 将Linux下的该数据盘挂载至Windows云服务器，若数据盘已挂载则可跳过此步骤：

登录腾讯云控制台，进入【云服务器】-【云硬盘】选项卡，点击该Linux数据盘【更多】-【挂载到云主机】按钮。在弹出框中选择重装后的Windows云服务器，点击【确定】按钮。

4) 点击运行DiskInternals，可以看到刚挂载的数据盘信息，/root/mnt和/root/mnt1分别对应分区vdb1和vdb2：
![](//mccdn.qcloud.com/static/img/de1d02ddf0793da5911e0bece70a4993/image.png)

5) 点击进入/root/mnt，右键点击想要拷贝的文件，选择save保存文件。
![](//mccdn.qcloud.com/static/img/9d95772257f0c000c47dbd5dfdf5d8ed/image.png)

6) 请注意，此时的Linux数据盘是只读的。需要将此数据盘作为Windows数据盘进行读写操作时，请先将需要的文件备份出来后，重新格式化成Windows操作系统支持的标准类型，具体操作见[这里](http://www.qcloud.com/doc/product/213/Windows%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%95%B0%E6%8D%AE%E7%9B%98%E5%88%86%E5%8C%BA%E5%92%8C%E6%A0%BC%E5%BC%8F%E5%8C%96)。



