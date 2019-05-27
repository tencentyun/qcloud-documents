
## 操作场景
本文档介绍 Linux [重装系统](https://cloud.tencent.com/document/product/213/4933) 为Windows 后，云服务器上读取原 Linux 系统下数据盘数据的操作方法。
Windows 文件系统格式通常是 NTFS 或 FAT32 ，而 Linux 文件系统格式通常是 EXT 系列。当操作系统从 Linux 重装为 Windows 后，操作系统类型发生了变化，而数据盘仍然是原来的格式，重装后的系统可能出现无法访问数据盘文件系统的情况。需要格式转换软件对原有的数据进行读取。
## 操作步骤

 1. 在重装为 Windows 的云服务器上，下载并安装 DiskInternals Linux Reader 软件。下载地址为：
 `
 http://www.diskinternals.com/download/Linux_Reader.exe 
 `
 
 2. 将原 Linux 云服务器下数据盘挂载至 Windows 云服务器。
 >! 若数据盘已挂载则可跳过此步骤
 
 登录 [腾讯云 CVM 控制台](https://console.cloud.tencent.com/cvm/) ，单击左侧【云硬盘】选项卡，单击原 Linux 数据盘右侧【更多】-【挂载】选项，如下图。
![](https://main.qcloudimg.com/raw/810d9328e0b8d91ed5912b4f7183edd4.png)
在弹出框中选择重装后的 Windows 云服务器，单击【确定】。

4. 查看数据盘信息 
假设重装前 Linux 云服务器数据盘有 vdb1 和 vdb2 两个分区：
![](//mc.qcloudimg.com/static/img/b964b6d45ceb0fa4d8835ddfa88db246/image.png)

 运行 DiskInternals Linux Reader 软件，即可查看刚挂载的数据盘信息。本例中，`/root/mnt`和`/root/mnt1`分别对应分区 vdb1 和 vdb2 。
![](//mccdn.qcloud.com/static/img/de1d02ddf0793da5911e0bece70a4993/image.png)

>**注意:**
>此时 Linux 数据盘为只读。若需要将此数据盘作为 Windows 数据盘进行读写操作，请先将需要的文件备份，重新格式化成 Windows 操作系统支持的标准类型，具体操作见 [Windows 云服务器数据盘分区和格式化](/doc/product/213/2158) 。

5. 双击进入`/root/mnt`目录内，右键单击要拷贝的文件，选择【Save】保存文件。
![](//mc.qcloudimg.com/static/img/b8b520159cf23b8450bc38de377a4e0f/image.png)




