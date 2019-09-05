## 操作场景
云硬盘是云上可扩展的存储设备，同时不失去云硬盘上原有的数据。而 [扩容云硬盘](https://cloud.tencent.com/document/product/362/5747) 完成后，您还需要将扩容部分的容量划分至已有分区内，但在此之前需要对云硬盘的扩展方式进行确认，再结合您的实际需求选择最佳的扩展方式。本文档介绍了在 Linux 云服务器上如何确定云硬盘的扩展方式。



## 前提条件
>!扩容文件系统操作不慎可能影响已有数据，因此建议您在操作前手动 [创建快照](https://cloud.tencent.com/document/product/362/5755) 备份数据。
>
- 已 [扩容云硬盘](https://cloud.tencent.com/document/product/362/5747)。
- 该云硬盘已 [挂载](https://cloud.tencent.com/document/product/362/5745) 到 Linux 云服务器并已创建文件系统。
- 已 [登录](https://cloud.tencent.com/document/product/213/5436) 待扩展分区及文件系统的 Linux 云服务器。

## 操作步骤
1. 以 root 用户执行以下命令，查询云硬盘使用的分区形式。
```
fdisk -l
```
 - 若结果如下图所示无分区（如仅展示 /dev/vdb），则说明使用扩容文件系统形式。
 ![](https://main.qcloudimg.com/raw/661ad0745c10a44035697cf4d03759f5.png)
 - 若结果如下两图所示（根据操作系统不同略有不同），则说明使用 GPT 分区形式。
![](https://main.qcloudimg.com/raw/5ff70adb58a223d32d334470c5b29e0e.png)
![](https://main.qcloudimg.com/raw/ce19715fc8494a9735b714d86f0cccfa.png)
 - 若结果如下图所示（根据操作系统不同略有不同），则说明使用 MBR 分区形式。
![](https://main.qcloudimg.com/raw/0e336cd3354c098cf5e70d0672e6f625.png)
2. 根据 [步骤1](#fdisk) 查询到的云硬盘分区形式，结合云硬盘实际情况选择对应的扩容方式。
>!
>- MBR 分区方式支持的磁盘最大容量为2TB。
>- 若您的磁盘使用 MBR 分区方式，且需要扩容至超过2TB时，建议您重新创建并挂载一块数据盘，并采用 GPT 方式进行分区后将原有数据拷贝至新数据盘上。 
>
<table>
     <tr>
         <th nowrap="nowrap">分区形式</th>  
				 <th>扩容方式</th>  
         <th>说明</th>  
     </tr>
		 	 <tr>      
         <td>-</td>   
	     <td nowrap="nowrap"><a href="https://cloud.tencent.com/document/product/362/37740">扩容文件系统</a></td>
			 <td>适用于<b>没有创建分区</b>、直接在裸设备上创建了文件系统的场景。</td>
     </tr>
	 <tr>      
         <td rowspan="2">GPT</td>   
	     <td nowrap="nowrap"><a href="https://cloud.tencent.com/document/product/362/37667?!preview&!editLang=zh#.E5.B0.86.E6.89.A9.E5.AE.B9.E9.83.A8.E5.88.86.E7.9A.84.E5.AE.B9.E9.87.8F.E5.88.92.E5.88.86.E8.87.B3.E5.8E.9F.E6.9C.89-gpt-.E5.88.86.E5.8C.BA">将扩容部分的容量划分至原有 GPT 分区</a></td>
	     <td>可用于格式化后未分区的云硬盘。</td>
     </tr> 
	 <tr>
         <td><a href="https://cloud.tencent.com/document/product/362/37667?!preview&!editLang=zh#.E5.B0.86.E6.89.A9.E5.AE.B9.E9.83.A8.E5.88.86.E7.9A.84.E5.AE.B9.E9.87.8F.E6.A0.BC.E5.BC.8F.E5.8C.96.E6.88.90.E7.8B.AC.E7.AB.8B.E7.9A.84-gpt-.E5.88.86.E5.8C.BA">将扩容部分的容量格式化成独立的 GPT 分区</a></td> 
	     <td>可保持原有分区不变，使用扩容部分新建 GPT 分区。</td>
     </tr> 
	 <tr>
         <td rowspan="2">MBR</td>   
	     <td><a href="https://cloud.tencent.com/document/product/362/37668?!preview&!editLang=zh#.E5.B0.86.E6.89.A9.E5.AE.B9.E9.83.A8.E5.88.86.E7.9A.84.E5.AE.B9.E9.87.8F.E5.88.92.E5.88.86.E8.87.B3.E5.8E.9F.E6.9C.89-mbr-.E5.88.86.E5.8C.BA">将扩容部分的容量划分至原有 MBR 分区</a></td> 
	     <td>可用于格式化后未分区的云硬盘。</td>
     </tr> 
	 <tr>
         <td><a href="https://cloud.tencent.com/document/product/362/37668?!preview&!editLang=zh#.E5.B0.86.E6.89.A9.E5.AE.B9.E9.83.A8.E5.88.86.E7.9A.84.E5.AE.B9.E9.87.8F.E6.A0.BC.E5.BC.8F.E5.8C.96.E6.88.90.E7.8B.AC.E7.AB.8B.E7.9A.84-mbr-.E5.88.86.E5.8C.BA">将扩容部分的容量格式化成独立的 MBR 分区</a></td> 
	     <td>可保持原有分区不变，使用扩容部分新建 MBR 分区。</td>
     </tr> 
</table>






