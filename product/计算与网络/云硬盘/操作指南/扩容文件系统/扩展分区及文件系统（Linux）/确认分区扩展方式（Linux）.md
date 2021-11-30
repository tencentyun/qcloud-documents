## 操作场景
云硬盘是云上可扩展的存储设备，您可以在创建云硬盘后随时扩展其大小，以增加存储空间，同时不失去云硬盘上原有的数据。
在通过控制台完成 [扩容云硬盘](https://cloud.tencent.com/document/product/362/5747) 后，您还需要在云服务器实例内部将扩容部分的容量划分至已有分区内，您需要结合实际需求选择最佳的云硬盘扩展方式。本文档介绍了在 Linux 云服务器上如何确定云硬盘的扩展方式。

<dx-alert infotype="notice" title="">
扩容文件系统操作不慎可能影响已有数据，因此建议您在操作前手动 [创建快照](https://cloud.tencent.com/document/product/362/5755) 备份数据。
</dx-alert>



## 前提条件
- 已通过控制台 [扩容云硬盘](https://cloud.tencent.com/document/product/362/5747)。
- 该云硬盘已挂载到 Linux 云服务器并已创建文件系统。详情请参见 [挂载云硬盘](https://cloud.tencent.com/document/product/362/5745)。
- 已登录待扩展分区及文件系统的 Linux 云服务器。详情请参见 [使用标准登录方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。

## 操作步骤
1. 以 root 用户执行以下命令，查询云硬盘使用的分区形式。[](id:fdisk)
```
fdisk -l
```
 - 若结果如下图所示无分区（仅展示 /dev/vdb），则说明需使用扩容文件系统形式。
 ![](https://main.qcloudimg.com/raw/661ad0745c10a44035697cf4d03759f5.png)
 - 若结果如下两图所示（根据操作系统不同略有不同），则说明需使用 GPT 分区形式。
![](https://main.qcloudimg.com/raw/5ff70adb58a223d32d334470c5b29e0e.png)
![](https://main.qcloudimg.com/raw/ce19715fc8494a9735b714d86f0cccfa.png)
 - 若结果如下图所示（根据操作系统不同略有不同），则说明需使用 MBR 分区形式。
![](https://main.qcloudimg.com/raw/0e336cd3354c098cf5e70d0672e6f625.png)
2. 根据 [步骤1](#fdisk) 查询到的云硬盘分区形式，结合云硬盘实际情况选择对应的扩容方式。
<dx-alert infotype="notice" title="">
- MBR 分区方式支持的磁盘最大容量为2TB。
- 若您的磁盘使用 MBR 分区方式，且需要扩容至超过2TB时，建议您重新创建并挂载一块数据盘，并采用 GPT 方式进行分区后将原有数据拷贝至新数据盘上。 
</dx-alert>
<table>
     <tr>
         <th nowrap="nowrap">分区形式</th>  
				 <th>扩容方式</th>  
         <th>说明</th>  
     </tr>
		 	 <tr>      
         <td>-</td>   
	     <td nowrap="nowrap"><a href="https://cloud.tencent.com/document/product/362/53364">扩容文件系统</a></td>
			 <td>适用于<b>没有创建分区</b>、直接在裸设备上创建了文件系统的场景。</td>
     </tr>
	 <tr>      
         <td rowspan="2">GPT</td>   
	     <td nowrap="nowrap"><a href="https://cloud.tencent.com/document/product/362/53366#Add">将扩容部分的容量划分至原有 GPT 分区</a></td>
	     <td>可用于格式化后未分区的云硬盘。</td>
     </tr> 
	 <tr>
         <td><a href="https://cloud.tencent.com/document/product/362/53366#New">将扩容部分的容量格式化成独立的 GPT 分区</a></td> 
	     <td>可保持原有分区不变，使用扩容部分新建 GPT 分区。</td>
     </tr> 
	 <tr>
         <td rowspan="2">MBR</td>   
	     <td><a href="https://cloud.tencent.com/document/product/362/53365#Add">将扩容部分的容量划分至原有 MBR 分区</a></td> 
	     <td>可用于格式化后未分区的云硬盘。</td>
     </tr> 
	 <tr>
         <td><a href="https://cloud.tencent.com/document/product/362/53365#New">将扩容部分的容量格式化成独立的 MBR 分区</a></td> 
	     <td>可保持原有分区不变，使用扩容部分新建 MBR 分区。</td>
     </tr> 
</table>






