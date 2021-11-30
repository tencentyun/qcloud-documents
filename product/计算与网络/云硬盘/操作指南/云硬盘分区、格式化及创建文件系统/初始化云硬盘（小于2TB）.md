## 操作场景
本文以云硬盘容量小于2TB为例，提供云硬盘的初始化操作指导。关于磁盘初始化场景的更多介绍，请参考 [初始化场景介绍](https://cloud.tencent.com/document/product/362/33065)。


## 前提条件
已 [挂载云硬盘](/doc/product/362/5745) 至云服务器。

## 注意事项
- 您可先了解 [云硬盘使用注意事项](https://cloud.tencent.com/document/product/362/17819#.E4.BA.91.E7.A1.AC.E7.9B.98.E4.BD.BF.E7.94.A8.E4.B8.8A.E6.9C.89.E4.BB.80.E4.B9.88.E6.B3.A8.E6.84.8F.E4.BA.8B.E9.A1.B9.EF.BC.9F) 后再对云硬盘进行相关操作，以免损坏重要数据。
- 格式化数据盘会将数据全部清空，请确保数据盘中没有数据或已备份重要数据。
- 为避免服务发生异常，格式化前请确保云服务器已停止对外服务。

## 操作步骤[](id:Steps)

<dx-tabs>
::: 初始化云硬盘（Windows） [](id:Windows2008)


<dx-alert infotype="explain" title="">
本文将以 Windows Server 2012 R2 操作系统为例，不同操作系统的格式化操作可能不同，本文仅供参考。
</dx-alert>


1. [登录 Windows 云服务器](https://cloud.tencent.com/document/product/213/5435)。
2. 在云服务器桌面，右键单击左下角的 <img src="https://main.qcloudimg.com/raw/3d815ac1c196b47b2eea7c3a516c3d88.png" style="margin:-6px 0px">。
3. 在弹出的菜单中，选择**磁盘管理**打开“磁盘管理”窗口。如下图所示：
![](https://main.qcloudimg.com/raw/fcf4fe5cafbbf4e3a52db750a4c3e2e2.png)
<dx-alert infotype="explain" title="">
若新增磁盘处于脱机状态（如上图），需要先执行 [步骤4](#online) 联机后再执行 [步骤5](#initialize) 进行初始化。否则直接执行 [步骤5](#initialize) 进行初始化。
</dx-alert>
4. [](id:online)在右侧窗格中出现磁盘列表，右键单击磁盘1区域，在菜单列表中选择**联机**，进行联机。联机后，磁盘1由**脱机**状态变为**没有初始化**。如下图所示：
![](https://main.qcloudimg.com/raw/4d3c952ca5ffdd3b1a4874191c33dc8c.png)
5. [](id:initialize)右键单击磁盘1区域，在菜单列表中选择**初始化磁盘**。如下图所示：
![](https://main.qcloudimg.com/raw/e20181dc979f1b018baba0ccaa0c5291.png)
6. 在**初始化磁盘**对话框中显示需要初始化的磁盘，选中 **MBR（主启动记录）**或 **GPT（GUID 分区表）**，单击**确定**。如下图所示：
<dx-alert infotype="notice" title="">
磁盘投入使用后再切换磁盘分区形式，磁盘上的原有数据将会清除，因此请根据实际需求合理选择分区形式。
</dx-alert>
![](https://main.qcloudimg.com/raw/688d59f40d9d26ae59ee201e433cee2e.png)
7. 右键单击磁盘上未分配的区域，选择**新建简单卷**。如下图所示：
![](https://main.qcloudimg.com/raw/912b77a52bb1e531d4c6bf5403841657.png)
8. 弹出**新建简单卷向导**对话框，根据界面提示，单击**下一步**。
9. 根据实际情况指定卷大小，默认为最大值，单击**下一步**。
10. 分配驱动器号，单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/1f61b5dcd5c965fa3e3bc11983475d38.png)
11. 选择**按下列设置格式化这个卷**，并根据实际情况设置参数，格式化新分区，单击**下一步**完成分区创建。
![](https://main.qcloudimg.com/raw/608ffc67e52b53691bf64f2b2411b948.png)
12. 单击**完成**完成向导。需要等待片刻让系统完成初始化操作，当卷状态为**状态良好**时，表示初始化磁盘成功。
![](https://main.qcloudimg.com/raw/148e9db3163df781b0832df1da25059f.png)
  初始化成功后，进入“计算机”界面可以查看到新磁盘。
![](https://main.qcloudimg.com/raw/05261659e6d9eed38da84a933c20ba12.png)
:::
::: 初始化云硬盘（Linux） [](id:Linux)
请根据您实际使用场景选择初始化方式：
- 若整块硬盘只呈现为一个独立的分区（即不存在多个逻辑盘，如 vdb1 和 vdb2 ），强烈推荐您不使用分区，直接 [在裸设备上构建文件系统](#CreateFileSystemOnBareDevice)。
- 若整块硬盘需要呈现为多个逻辑分区（即存在多个逻辑盘），则您需要先进行分区操作，再 [在分区上构建文件系统](#CreateFileSystemOnPartition)。


### 在裸设备上构建文件系统 [](id:CreateFileSystemOnBareDevice)

1. [登录 Linux 云服务器](https://cloud.tencent.com/document/product/213/5436)。
2. 以 root 用户执行以下命令，查看磁盘名称。
```
fdisk -l
``` 回显信息类似如下图，表示当前的云服务器有两块磁盘，“/dev/vda” 是系统盘，“/dev/vdb” 是新增数据盘。
 ![](https://main.qcloudimg.com/raw/aad842b12fec3ca583790bff609c9fb7.png)
3. 执行以下命令，对 “/dev/vdb” 裸设备直接创建文件系统格式。
```
mkfs -t <文件系统格式> /dev/vdb
``` 不同文件系统支持的分区大小不同，请根据实际需求合理选择文件系统。以设置文件系统为 `EXT4` 为例：
```
mkfs -t ext4 /dev/vdb
```
<dx-alert infotype="notice" title="">
格式化需要等待一段时间，请观察系统运行状态，不要退出。
</dx-alert>
4. 执行以下命令，新建挂载点。
```
mkdir <挂载点>
``` 以新建挂载点 `/data` 为例：
```
mkdir /data
```
5. 执行以下命令，将新建分区挂载至新建的挂载点。
```
mount /dev/vdb <挂载点>
``` 以新建挂载点 `/data` 为例：
```
mount /dev/vdb /data
```
6. 执行以下命令，查看挂载结果。
```
df -TH
```
<dx-alert infotype="explain" title="">
若无需设置开机自动挂载磁盘，则跳过后续步骤。
</dx-alert>
7. 确认挂载方式并获取对应信息。
您可以根据业务需求选择使用弹性云硬盘的软链接、文件系统的 UUID（universally unique identifier）或设备名称自动挂载磁盘，相关说明和信息获取方式如下：
<table>
 <tr>
      <th>挂载方式</th>
      <th>优缺点</th>
      <th>信息获取方式</th>
 </tr>
 <tr>
     <td nowrap="nowrap">使用弹性云硬盘的软链接<b>（推荐）</b></td>
     <td><b>优点</b>：每个弹性云硬盘的软链接固定且唯一，不会随卸载挂载、格式化分区等操作而改变。</br><b>缺点</b>：只有弹性云硬盘才有软链接。无法感知分区的格式化操作。</td>
		 <td nowrap="nowrap">执行以下命令，查看弹性云硬盘的软链接。</br><pre style="color:white;">ls -l /dev/disk/by-id</pre></td>
	</tr>
	<tr>
	   <td nowrap="nowrap">使用文件系统的 UUID</td>
		 <td>可能会因文件系统的 UUID 变化而导致自动挂载设置失效。</br>例如，重新格式化文件系统后，文件系统的 UUID 将会发生变化。</td>
		 <td nowrap="nowrap">执行以下命令，查看文件系统的 UUID。</br><pre style="color:white;">blkid /dev/vdb</pre></td>
  </tr>
	<tr>
	   <td nowrap="nowrap">使用设备名称</td>     
		 <td>可能会因设备名称变化而导致自动挂载设置失效。</br>例如，迁移数据时将云服务器上的弹性云硬盘卸载后再次挂载，操作系统再次识别到该文件系统时，名称可能会变化。</td>
		 <td nowrap="nowrap">执行以下命令，查看设备名称。</br><pre style="color:white;">fdisk -l</pre></td>
 </tr>
</table>
8. 执行以下命令，备份 `/etc/fstab`  文件。以备份到  `/home` 目录下为例：
```
cp -r /etc/fstab /home
```
9. 执行以下命令，使用 VI 编辑器打开 `/etc/fstab` 文件。
```
vi /etc/fstab
```
10. 按 **i** 进入编辑模式。
11. 将光标移至文件末尾，按 **Enter**，添加如下内容。
```plaintext
<设备信息> <挂载点> <文件系统格式> <文件系统安装选项> <文件系统转储频率> <启动时的文件系统检查顺序>
```
 - **（推荐）**以使用弹性云硬盘的软链接自动挂载为例，结合前文示例则添加：
```
/dev/disk/by-id/virtio-disk-drkhklpe /data ext4 defaults 0 0
```
<dx-alert infotype="explain" title="">
若您有多块弹性云硬盘，则可使用 `disk-xxxxx` 与 [控制台](https://console.cloud.tencent.com/cvm/cbs/index) 中的云硬盘 ID 对比以进行区分。
</dx-alert>
 - 以使用磁盘分区的 UUID 自动挂载为例，结合前文示例则添加：
```
UUID=d489ca1c-5057-4536-81cb-ceb2847f9954 /data  ext4 defaults     0   0
```
 - 以使用设备名称自动挂载为例，结合前文示例则添加：
```
/dev/vdb /data   ext4 defaults     0   0
```
12. 按 **Esc**，输入 **:wq**，按 **Enter**。
保存设置并退出编辑器。
13. 执行以下命令，检查 **/etc/fstab** 文件是否写入成功。
```
mount -a 
``` 如果运行通过则说明文件写入成功，新建的文件系统会在操作系统启动时自动挂载。


### 在分区上构建文件系统 [](id:CreateFileSystemOnPartition)



<dx-alert infotype="explain" title="">
本操作将以在 CentOS 7.5 操作系统中使用 fdisk 分区工具将数据盘 `/dev/vdb` 设置为主分区，分区形式默认设置为 MBR，文件系统设置为 EXT4 格式，挂载在 `/data/newpart` 下，并设置开机启动自动挂载为例，不同操作系统的格式化操作可能不同，本文仅供参考。
</dx-alert>



1. [登录 Linux 云服务器](https://cloud.tencent.com/document/product/213/5436)。
2. 以 root 用户执行以下命令，查看磁盘名称。
 ```
fdisk -l
```  回显信息类似如下图，表示当前的云服务器有两块磁盘，“/dev/vda” 是系统盘，“/dev/vdb” 是新增数据盘。
![](https://main.qcloudimg.com/raw/aad842b12fec3ca583790bff609c9fb7.png)
3. 执行以下命令，进入 fdisk 分区工具，开始对新增数据盘执行分区操作。
 ```
fdisk <新增数据盘>
```  以新挂载的数据盘 `/dev/vdb` 为例：
```
fdisk /dev/vdb
```  回显信息类似如下图：
 ![](https://main.qcloudimg.com/raw/db1fe212e2559ac635c52e5e397e7531.png)
4. 输入**n**，按 **Enter**，开始新建分区。
 回显信息类似如下图：
 ![](https://main.qcloudimg.com/raw/c89b572c0ac2af1302189f8e7e1a849e.png)
 表示磁盘有两种分区类型：
  - **p** 表示主要分区。
  - **e** 表示延伸分区。
5. 以创建一个主要分区为例，输入 **p**，按 **Enter**，开始创建一个主分区。
 回显信息类似如下图：
 ![](https://main.qcloudimg.com/raw/efb65b60631d95e9b0213e6fd6125bbb.png)
**Partition number** 表示主分区编号，可以选择1 - 4。
6. 以选择分区编号1为例，输入主分区编号 **1**，按 **Enter**。
 回显信息类似如下图：
 ![](https://main.qcloudimg.com/raw/e1a1a7755a3bb392ec6d623e6774c315.png)
**First sector** 表示初始磁柱区域，可以选择2048 - 20971519，默认为2048。
7. 以选择默认初始磁柱编号2048为例，按 **Enter**。
 回显信息类似如下图：
 ![](https://main.qcloudimg.com/raw/58a8202531b239a73fd3182d0ea0cf34.png)
**Last sector** 表示截止磁柱区域，可以选择2048 - 20971519，默认为20971519。
8. 以选择默认截止磁柱编号20971519为例，按 **Enter**。
 回显信息类似如下图：
 ![](https://main.qcloudimg.com/raw/ad3a6459a6eaf154aed578b37dfc89d0.png)
 表示分区完成，即为60GB的数据盘新建了1个分区。
9. 输入 **p**，按 **Enter**，查看新建分区的详细信息。
 回显信息类似如下图：
 ![](https://main.qcloudimg.com/raw/98427c11e0a181e02eb23a95fc1e908c.png)
 表示新建分区 `/dev/vdb1` 的详细信息。
<dx-alert infotype="explain" title="">
若上述分区操作有误，请输入 **q**，退出 fdisk 分区工具，之前的分区结果将不会被保留。
</dx-alert>
10. 输入 **w**，按 **Enter**，将分区结果写入分区表中。
 回显信息类似如下图，表示分区创建完成。
 ![](https://main.qcloudimg.com/raw/7011369be260150fcddf272b4a4ab2fa.png)
11. 执行以下命令，将新的分区表变更同步至操作系统。
```
partprobe
```
12. 执行以下命令，将新建分区文件系统设置为系统所需格式。
```
mkfs -t <文件系统格式> /dev/vdb1
``` 不同文件系统支持的分区大小不同，请根据实际需求合理选择文件系统。以设置文件系统为 EXT4 为例：
```
mkfs -t ext4 /dev/vdb1
``` 回显信息类似如下图：
![](https://main.qcloudimg.com/raw/6de097cea77634f8847816dd795292a7.png)
格式化需要等待一段时间，请观察系统运行状态，不要退出。
13. 执行以下命令，新建挂载点。
 ```
mkdir <挂载点>
```  以新建挂载点 `/data/newpart` 为例：
 ```
mkdir /data/newpart
```
14. 执行以下命令，将新建分区挂载至新建的挂载点。
 ```
mount /dev/vdb1 <挂载点>
```  以新建挂载点 `/data/newpart` 为例：
```
mount /dev/vdb1 /data/newpart
```
15. 执行以下命令，查看挂载结果。
```
df -TH
```  回显信息类似如下图：
 ![](https://main.qcloudimg.com/raw/b7e5501fed8d7d648b48dc66685baf94.png)
 表示新建分区 `/dev/vdb1` 已挂载至 `/data/newpart`。
<dx-alert infotype="explain" title="">
若无需设置开机自动挂载磁盘，则跳过后续步骤。
</dx-alert>
16. 确认挂载方式并获取对应信息。
 您可以根据业务需求选择使用弹性云硬盘的软链接、文件系统的 UUID（universally unique identifier）或设备名称自动挂载磁盘，相关说明和信息获取方式如下：
 <table>
     <tr>
         <th>挂载方式</th>  
         <th>优缺点</th>  
         <th>信息获取方式</th>  
     </tr>
	   <tr>      
         <td nowrap="nowrap">使用弹性云硬盘的软链接<b>（推荐）</b></td>   
	       <td><b>优点</b>：每个弹性云硬盘的软链接固定且唯一，不会随卸载挂载、格式化分区等操作而改变。<br><b>缺点</b>：只有弹性云硬盘才有软链接。无法感知分区的格式化操作。</td>
	       <td nowrap="nowrap">执行以下命令，查看弹性云硬盘的软链接。</br><pre style="color:white;">ls -l /dev/disk/by-id</pre></td>
     </tr> 
	   <tr>      
         <td nowrap="nowrap">使用文件系统的 UUID</td>   
	       <td>可能会因文件系统的 UUID 变化而导致自动挂载设置失效。<br>例如，重新格式化文件系统后，文件系统的 UUID 将会发生变化。</td>
	       <td nowrap="nowrap">执行以下命令，查看文件系统的 UUID。</br><pre style="color:white;">blkid /dev/vdb1</pre></td>
     </tr> 
	   <tr>      
         <td nowrap="nowrap">使用设备名称</td>   
	       <td>可能会因设备名称变化而导致自动挂载设置失效。<br>例如，迁移数据时将云服务器上的弹性云硬盘卸载后再次挂载，操作系统再次识别到该文件系统时，名称可能会变化。</td>
	       <td>执行以下命令，查看设备名称。</br><pre style="color:white;">fdisk -l</pre></td>
     </tr> 
</table>
17. 执行以下命令，备份 `/etc/fstab 文件`。以备份到 `/home` 目录下为例：
```
cp -r /etc/fstab /home
```
18. 执行以下命令，使用 VI 编辑器打开 `/etc/fstab` 文件。
 ```
vi /etc/fstab
```
19. 按 **i** 进入编辑模式。 
20. 将光标移至文件末尾，按 **Enter**，添加如下内容。
```plaintext
<设备信息> <挂载点> <文件系统格式> <文件系统安装选项> <文件系统转储频率> <启动时的文件系统检查顺序>
```
 - **（推荐）**以使用弹性云硬盘的软链接自动挂载为例，结合前文示例则添加：
 ```
/dev/disk/by-id/virtio-disk-drkhklpe-part1 /data/newpart   ext4 defaults     0   2
```
<dx-alert infotype="explain" title="">
若您有多块弹性云硬盘，则可使用 `disk-xxxxx` 与 [控制台](https://console.cloud.tencent.com/cvm/cbs/index) 中的云硬盘 ID 对比以进行区分。
</dx-alert>
 - 以使用磁盘分区的 UUID 自动挂载为例，结合前文示例则添加：
```
UUID=d489ca1c-5057-4536-81cb-ceb2847f9954 /data/newpart   ext4 defaults     0   2
```
 - 以使用设备名称自动挂载为例，结合前文示例则添加：
```
/dev/vdb1 /data/newpart   ext4 defaults     0   2
```
20. 按 **Esc**，输入 **:wq**，按 **Enter**。
 保存设置并退出编辑器。
21. 执行以下命令，检查 `/etc/fstab` 文件是否写入成功。
```
 mount -a 
``` 如果运行通过则说明文件写入成功，新建的文件系统会在操作系统启动时自动挂载。
:::
</dx-tabs>



## 相关操作
[初始化云硬盘（大于等于2TB）](https://cloud.tencent.com/document/product/362/6735)


