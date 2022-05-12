## RAID 简介
RAID 可以将多个磁盘组合起来构成一个磁盘阵列组，提高数据的读写性能和可靠性。操作系统只会将磁盘阵列组当作一个硬盘来使用。目前 RAID 有多种等级，根据选择版本不同，磁盘阵列组相较于一块容量相当的大硬盘有增强数据集成度、增强容错功能、增加处理量或容量等优势。


<dx-alert infotype="notice" title="">
- 请及时对即将到期的弹性云硬盘进行 [续费](https://cloud.tencent.com/document/product/362/6739) 操作，以免由于弹性云硬盘到期被系统强制隔离对 RAID 产生影响。
- 建议创建 RAID 1、RAID 01、RAID 10 时，使用相同大小的分区，减少磁盘空间的浪费。
</dx-alert>



 RAID 0、RAID 1、RAID 01 和 RAID 10之间的相同点与差异点如下表所示：
<table>
     <tr>
         <th nowrap="nowrap">RAID 级别</th>  
         <th>简介</th>  
		 <th>优/缺点</th>
		 <th>使用场景（建议）</th>
     </tr>
	 <tr>
         <td>RAID 0</td>
				 <td>存储模式：数据分段存放在不同的磁盘中。<br /></br>虚拟盘大小：阵列中所有盘容量之和。</td>
		 <td>
		 <ul><li><b>优点</b>：读写可以并行。</br>理论上读写速率可达单个磁盘的 N 倍（N 为组成 RAID 0 的磁盘个数），但实际上受限于文件大小、文件系统大小等多种因素。</li>
		 <li><b>缺点</b>：没有数据冗余，即便只有单个磁盘损坏，在最严重的情况下也有可能导致所有数据的丢失。</li></ul></td>
		 <td>对 I/O 性能要求很高，并且已通过其他方式对数据进行备份处理或者不需要进行数据备份的场景。</td>
     </tr> 
	 <tr>
         <td>RAID 1</td>
         <td>存储模式：数据被镜像存储在多个磁盘中。<br /></br> 虚拟盘大小：阵列中容量最小的盘的容量。</td>
		 <td>
		 <ul><li><b>优点</b>：<ul>
		 <li>读取速度快。</li>
		 <li>数据可靠性较高，单个磁盘的损坏不会导致数据的不可修复。</li>
		 </ul>
		 <li><b>缺点</b>：<ul>
		 <li>磁盘利用率最低。</li>
		 <li>写入速度受限于单个磁盘的写入速度。</li>
		 </ul></ul>
		 </td>
		 <td>对读性能要求较高，并且需要对写入的数据进行备份处理的场景。</td>
     </tr>
	 <tr>
         <td>RAID 01</td>
         <td>先用多个盘构建成 RAID 0，再用多个 RAID 0 构建成 RAID 1。</td>
		 <td><ul><li><b>优点</b>：同时具备 RAID 0 和 RAID 1 的优点。</li>
		 <li><b>缺点</b>：<ul><li>成本相对较高，至少需要使用四块盘。</li><li>单磁盘的损坏会导致同组的磁盘都不可用。</li></td>
		 <td   rowspan="2">-</td>
     </tr>
	 <tr>
         <td>RAID 10</td>
         <td>先用多个盘构建成 RAID 1，再用多个 RAID 1 构建成 RAID 0。</td>
		 <td><ul><li><b>优点</b>：同时具备 RAID 0 和 RAID 1 的优点。</li>
		 <li><b>缺点</b>：成本相对较高，至少需要使用四块盘。</li></td>
     </tr>
</table>



## 构建 RAID


<dx-alert infotype="explain" title="">
本文以在 CentOS 云服务器中使用四块弹性云硬盘构建 RAID 0 为例。不同操作系统、不同 RAID 级别的操作可能不同，本文仅供参考，具体操作步骤和差异请参考对应操作系统的产品文档或 RAID 相关文档。
</dx-alert>



Linux 内核提供用于管理 RAID 设备的 md 模块，可以直接使用 mdadm 工具来调用 md 模块创建 RAID 0。
![](https://main.qcloudimg.com/raw/a7e717737b22456319cde4ec4bc0c8e1.png)

1. 以 root 用户 [登录云服务器](https://cloud.tencent.com/document/product/213/5436)。
2. 执行以下命令，安装 mdadm。
```
yum install mdadm -y
```
安装成功结果如下图所示：
![](https://main.qcloudimg.com/raw/9ae334a316638ebc8e8b95a587c6e8b5.png)
3. 执行以下命令，使用 mdadm 创建 RAID 0。
```
mdadm --create /dev/md0 --level=0 --raid-devices=4 /dev/vd[cdef]1
```
创建成功结果如下图所示：
![](https://main.qcloudimg.com/raw/7c2d92dc0cf8225d56c6696127e1a6ce.png)
4. 执行以下命令，使用 mkfs 创建文件系统（以使用 EXT3 文件系统为例）。
```
mkfs.ext3 /dev/md0
```
创建成功结果如下图所示：
![](https://main.qcloudimg.com/raw/ed6291597a03923a46914ff39005c90e.png)
5. 依次执行以下命令，挂载文件系统。
```
mkdir md0/
mount /dev/md0 md0/
tree md0
```
挂载成功结果如下图所示：
![](https://main.qcloudimg.com/raw/c77863517336227b6dc5dc0180935e46.png)
6. 执行以下命令，查看文件系统详情，并记录其 UUID（以`c5d8a204:c28853ba:3882e9f8:62d078de`为例）。如下图所示：
```
mdadm --detail --scan
```
![](https://main.qcloudimg.com/raw/bd258e727fc5ca5ee67ffe7ffeddea2a.png)
7. 执行以下命令，编辑 mdadm 配置文件。
```
vi /etc/mdadm.conf
```
8. 按 **i** 进入编辑模式，并输入相关内容。
对于弹性云硬盘，建议输入以下配置：
```
DEVICE /dev/disk/by-id/virtio-弹性云盘1ID-part1 
DEVICE /dev/disk/by-id/virtio-弹性云盘2ID-part1 
DEVICE /dev/disk/by-id/virtio-弹性云盘3ID-part1 
DEVICE /dev/disk/by-id/virtio-弹性云盘4ID-part1 
ARRAY 逻辑设备路径 metadata= UUID=
```
本文以逻辑设备路径是 /dev/md0，metadata 是1.2为例，则输入：
```
DEVICE /dev/disk/by-id/virtio-弹性云盘1ID-part1 
DEVICE /dev/disk/by-id/virtio-弹性云盘2ID-part1 
DEVICE /dev/disk/by-id/virtio-弹性云盘3ID-part1 
DEVICE /dev/disk/by-id/virtio-弹性云盘4ID-part1 
ARRAY /dev/md0 metadata=1.2 UUID=3c2adec2:14cf1fa7:999c29c5:7d739349
```
9. 按 Esc，输入`:wq`保存并退出。
