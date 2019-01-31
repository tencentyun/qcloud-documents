## 操作场景
本文以云硬盘容量大于等于2TB为例，提供云硬盘的初始化操作指导。关于云磁盘初始化场景的更多介绍，请参考 [初始化场景介绍](https://cloud.tencent.com/document/product/362/33065)。
MBR 支持的磁盘最大容量为2TB，因此当为容量大于2TB的磁盘分区时，请采用GPT 分区形式。对于 Linux 操作系统而言，当磁盘分区形式选用 GPT 时，fdisk 分区工具将无法使用，需要采用 parted 工具。

## 注意事项
- 格式化数据盘会将数据将被全部清空。请确保数据盘中没有数据或已备份重要数据。
- 为避免服务发生异常，格式化前请确保云服务器已停止对外服务。

## 前提条件
已 [挂载云硬盘](/doc/product/362/5745) 至云服务器。

## 操作步骤
<span id="2TBWindows2012"></span>
### 初始化云硬盘（Windows）
>?本文将以 Windows Server 2012 操作系统为例，不同操作系统的格式化操作可能不同，本文仅供参考。

1. [登录 Windows 云服务器](https://cloud.tencent.com/document/product/213/5435)。
2. 在云服务器桌面，单击<img src="https://main.qcloudimg.com/raw/0a02193a82217974f650bbcaf4e1ed2d.png"  style="margin:0;">。进入【服务器管理器】页面。
3. 在左侧导航树中，单击【文件和存储服务】。
4. 在左侧导航树中，选择【卷】>【磁盘】。
 ![](https://main.qcloudimg.com/raw/e21c6ae7dbd7b41a3bfe9c5e2fd25c50.png)

>?若新增磁盘处于脱机状态（如上图），需要先执行 [步骤5](#online) 联机后再执行 [步骤6](#initialize) 进行初始化。否则直接执行 [步骤6](#initialize) 进行初始化。

<span id="online"></span>
5. 在右侧窗格中出现磁盘列表，右键单击1所在行，在菜单列表中选择【联机】，进行联机。联机后，1由【脱机】状态变为【联机】。
 ![](https://main.qcloudimg.com/raw/e8bf6970a2b203a3fc926a35322680c2.png)
<span id="initialize"></span>
6. 右键单击1所在行，在菜单列表中选择【初始化】。
 ![](https://main.qcloudimg.com/raw/9cb41b9ea7d29115035e15924e65a86f.png)
7. 根据界面提示，单击【是】。
 ![](https://main.qcloudimg.com/raw/4bd1346cb8f15bda39fb6ab399a3b2e2.png)
8. 初始化后，1由【未知】分区变为【GPT】，右键单击1所在行，在菜单列表中选择【新建简单卷】。
 ![](https://main.qcloudimg.com/raw/d9dbae385dee6e92534db02b3a1cf443.png)
9. 弹出【新建卷向导】对话框，根据界面提示，单击【下一步】。
 ![](https://main.qcloudimg.com/raw/896583a11d0004c9172c0d1a31f0ff74.png)
10. 选择服务器和磁盘，单击【下一步】。
 ![](https://main.qcloudimg.com/raw/368ee2e2a5b858504a931d0aa0888915.png)
11. 根据实际情况指定卷大小，默认为最大值，单击【下一步】。
 ![](https://main.qcloudimg.com/raw/4a6b81ca6a0034fd409289fee70374a1.png)
12. 分配驱动器号，单击【下一步】。
 ![](https://main.qcloudimg.com/raw/4c6f82f8e0027ffbbf20869ed4df5dfb.png)
13. 选择【按下列设置格式化这个卷】，并根据实际情况设置参数，格式化新分区，单击【下一步】完成分区创建。
 ![](https://main.qcloudimg.com/raw/952b5425be9d7b3c44730801b3563d6b.png)
14. 确认信息无误后，单击【创建】。
 ![](https://main.qcloudimg.com/raw/61f81b09d6244962379dda362e07b660.png)
15. 需要等待片刻让系统完成新建卷操作，单击【关闭】。
 初始化成功后，进入【这台电脑】界面可以查看到新磁盘。
 ![](https://main.qcloudimg.com/raw/1053f9ea5f3ab8cf85f7c81ba1bf53b8.png)

<span id="2TBLinux"></span>
### 初始化云硬盘（Linux）
>?本文将以在 CentOS 7.5 操作系统中使用 parted 分区工具将数据盘 `/dev/vdc`设置为主分区，分区形式默认设置为 GPT，文件系统设置为 EXT4 格式，挂载在`/data/newpart2`下，并设置开机启动自动挂载为例，不同操作系统的格式化操作可能不同，本文仅供参考。

1. [登录 Linux 云服务器](https://cloud.tencent.com/document/product/213/5436)
2. 以 root 用户执行以下命令，查看磁盘名称。
 ```
lsblk
```
回显信息类似如下图，表示当前的云服务器有两块磁盘，“/dev/vda”是系统盘，“/dev/vdc”是新增数据盘。
	![](https://main.qcloudimg.com/raw/72a7a48c59c13a44958a6b1aa0407ac2.png)
3. 执行以下命令，进入 fdisk 分区工具，开始对新增数据盘执行分区操作。
```
parted <新增数据盘>
```
以新挂载的数据盘`/dev/vdc`为例：
```
parted /dev/vdc
```
回显信息类似如下图：
![](https://main.qcloudimg.com/raw/0b2c9164f9fec125a72dee8861b7327d.png)
4. 输入`p`，按 Enter，查看当前磁盘分区形式。
 回显信息类似如下图：
 ![](https://main.qcloudimg.com/raw/af906521dd6a7f3b948cfad42745aaba.png)
 【Partition Table: unknown】表示磁盘分区形式未知。
5. 执行以下命令，设置磁盘分区形式。
```
mklabel <磁盘分区方式>
```
磁盘容量大于等于2TB时，只能使用 GPT 分区方式：
```
mklabel gpt
```
6. 输入`p`，按 Enter，查看磁盘分区形式是否设置成功。
 回显信息类似如下图：
	![](https://main.qcloudimg.com/raw/3dfec9aba75cd3cb6dcfb06729f5ff26.png)
 【Partition Table: gpt】表示磁盘分区形式为 GPT。
7. 输入“unit s”，按“Enter”，设置磁盘的计量单位为磁柱。
8. 以为整个磁盘创建一个分区为例，输入“mkpart opt 2048s 100%”，按 Enter。
 2048s表示磁盘起始容量，100%表示磁盘截止容量，此处仅供参考，您可以根据业务需要自行规划磁盘分区数量及容量。
9. 输入`p`，按 Enter，查看新建分区的详细信息。
  回显信息类似如下图：
 ![](https://main.qcloudimg.com/raw/ee406e75c689f48d59e863adc768aa36.png)
 表示新建分区`/dev/vdc1`的详细信息。
10. 输入`q`，按 Enter，退出 parted 分区工具
11. 执行以下命令，查看磁盘名称。
 ```
lsblk
```
回显信息类似如下图，此时可看到新分区“/dev/vdc1”。
![](https://main.qcloudimg.com/raw/f95f599f11f88b8bcb89d4f02bb41292.png)
12. 执行以下命令，将新建分区文件系统设置为系统所需格式。
```
mkfs -t <文件系统格式> /dev/vdc1
```
不同文件系统支持的分区大小不同，请根据实际需求合理选择文件系统。以设置文件系统为 EXT4 为例：
```
mkfs -t ext4 /dev/vdc1
```
 回显信息类似如下图：
 ![](https://main.qcloudimg.com/raw/3cd6bbd019dd9bdc85ad4ed11ba64f0b.png)
 格式化需要等待一段时间，请观察系统运行状态，不要退出。
13. 执行以下命令，新建挂载点。
```
mkdir <挂载点>
```
以新建挂载点`/data/newpart2`为例：
```
mkdir /data/newpart2
```
14. 执行以下命令，将新建分区挂载至新建的挂载点。
```
mount /dev/vdb1 <挂载点>
```
以新建挂载点`/data/newpart2`为例：
```
mount /dev/vdb1 /data/newpart2
```
15. 执行以下命令，查看挂载结果。
```
df -TH
```
 回显信息类似如下图：
 ![](https://main.qcloudimg.com/raw/774c2d9ff266634c4836df6456b9dd4d.png)
 表示新建分区`/dev/vdc1`已挂载至`/data/newpart2`。
 
>?若无需设置开机自动挂载磁盘，则跳过后续步骤。

16. 执行以下命令，查询磁盘分区的 UUID。
```
blkid <磁盘分区>
```
以查询磁盘分区`/dev/vdc1`的 UUID 为例：
```
blkid /dev/vdc1
```
 回显信息类似如下图：
 ![](https://main.qcloudimg.com/raw/0423400e7e8dc7f5ab21927895b3ec85.png)
17. 执行以下命令，使用 VI 编辑器打开`fstab`文件。
```
vi /etc/fstab
```
18.按`i`，进入编辑模式。 
19.将光标移至文件末尾，按 Enter，添加如下内容。
```
UUID=<UUID> <挂载点>   <文件系统格式> defaults     0   2
```
结合前文示例，则添加：
```
UUID=fc3f42cc-2093-49c7-b4fd-c616ba6165f4 /data/newpart2   ext4 defaults     0   2
```
![](https://main.qcloudimg.com/raw/66e80816c9a952f86387d4359386b764.png)
20. 按 Esc，输入`:wq`，按 Enter。
保存设置并退出编辑器。
