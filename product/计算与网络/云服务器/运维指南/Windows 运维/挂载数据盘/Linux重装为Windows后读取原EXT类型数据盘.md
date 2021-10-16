
## 操作场景
Windows 文件系统格式通常是 NTFS 或 FAT32 ，Linux 文件系统格式通常是 EXT 系列。当操作系统从 Linux 重装为 Windows，操作系统类型虽然发生了变化，但数据盘仍然是原来的格式。重装后的系统可能出现无法访问数据盘文件系统的情况，此时，您需要格式转换软件对原有的数据进行读取。

本文档介绍 Linux [重装系统](https://cloud.tencent.com/document/product/213/4933) 为 Windows 后，在云服务器上读取原 Linux 系统下数据盘数据的操作方法。


## 前提条件
- 已在重装为 Windows 的云服务器上安装 DiskInternals Linux Reader 软件。
DiskInternals Linux Reader 软件的获取方式：`http://www.diskinternals.com/download/Linux_Reader.exe `
- 已知重装前挂载至 Linux 云服务器数据盘有 vdb1 和 vdb2 两个分区。如下图所示：
![](https://main.qcloudimg.com/raw/ef515a31c27e5ea96993af60dfc9ab55.png)

## 操作步骤
### 挂载数据盘

<dx-alert infotype="notice" title="">
若数据盘已挂载则可跳过此步骤。
</dx-alert>


1. 登录 [腾讯云云服务器控制台](https://console.cloud.tencent.com/cvm/)。
2. 在左侧导航栏中，选择**云硬盘**，进入云硬盘管理页面。
3. 选择已重装系统的实例行，单击右侧的**更多** > **挂载**。如下图所示：
![](https://main.qcloudimg.com/raw/810d9328e0b8d91ed5912b4f7183edd4.png)
4. 在弹出的窗口中，选择重装后的 Windows 云服务器，单击**确定**。

### 查看数据盘信息 
1. 运行 DiskInternals Linux Reader 软件，即可查看刚挂载的数据盘信息。`/root/mnt`和`/root/mnt1`分别为重装前 Linux 云服务器数据盘的 vdb1 和 vdb2 两个分区。如下图所示：
<dx-alert infotype="notice" title="">
此时 Linux 数据盘为只读。若需要将此数据盘作为 Windows 数据盘进行读写操作，请先将需要的文件备份，重新格式化成 Windows 操作系统支持的标准类型，具体操作见 [Windows 实例：初始化数据盘](https://cloud.tencent.com/document/product/213/2158)。
</dx-alert>
<img src="https://main.qcloudimg.com/raw/490428b0668dcd61c4c60bcb75121462.png"/>
2. 双击进入`/root/mnt`目录内，右键单击要拷贝的文件，选择 **Save**，保存文件。如下图所示：
![](https://main.qcloudimg.com/raw/2d2f39e89014f72aaef1bfc3d1d101f3.png)






