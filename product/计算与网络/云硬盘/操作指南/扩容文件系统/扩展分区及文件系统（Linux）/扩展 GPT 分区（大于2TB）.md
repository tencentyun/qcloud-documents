## 操作场景
请参考下表，根据您的云硬盘实际扩容情况选择对应扩展分区及文件系统方式。

<table>
	<tr>
		<th>扩容前容量</th>
		<th>扩容容量</th>
		<th>可选方式</th>
	</tr>
	<tr>
		<td>小于2TB</td>
		<td>大于2TB</td>
		<td>建议将扩容部分新建一块云硬盘，挂载后请参照 <a href="https://cloud.tencent.com/document/product/362/6735#.E5.88.9D.E5.A7.8B.E5.8C.96.E4.BA.91.E7.A1.AC.E7.9B.98.EF.BC.88linux.EF.BC.89">初始化云硬盘（大于2TB）</a> 创建分区及文件系统后，将数据拷至新盘。</td>
	</tr>
		<tr>
		<td>大于2TB</td>
		<td>任意</td>
		<td>
			<ul style="margin-bottom:0px;">
			<li>将扩容部分 <a href="#Add">划分至原有 GRT 分区</a></li>
				<li>将扩容部分 <a href="#New">新建 GRT 分区</a></li>
			</ui>
		</td>
	</tr>
</table>

## 前提条件
e2fsck/resize2fs 自动扩容工具适用于 Linux 操作系统，用于将新扩容的云硬盘空间添加到已有的文件系统中，扩容能够成功必须满足以下条件：
- 文件系统是 EXT2/EXT3/EXT4/XFS。
- 当前文件系统不能有错误。
- 当前工具仅支持 Python 2 版本，不支持 Python 3 版本。


## 操作步骤

<span id="Add"></span>
### 将扩容部分的容量划分至原有 GPT 分区
1. 以 root 用户执行以下命令，确认云硬盘的容量变化。
```
parted <磁盘路径> print
```
本文以磁盘路径是 `/dev/vdb` 为例，则执行：
```
parted /dev/vdb print
```
若在过程中提示如下图所示信息，请输入 `Fix`。
![](https://main.qcloudimg.com/raw/ec2ec164e146e46c2a4d11489dceecfa.png)
如下图所示，扩容后的云硬盘大小为2169GB，已有分区的大小为10.7GB。
![](https://main.qcloudimg.com/raw/d902d173106fdb9b5ff44c494ba8147a.png)
<span id="step2"></span>
2. 执行以下命令，确认该云硬盘是否还有分区已挂载。
```
mount | grep '<磁盘路径>' 
```
本文以磁盘路径是`/dev/vdb`为例，则执行：
```
mount | grep '/dev/vdb'
```
执行结果如下，则说明云硬盘上有一个分区（vdb1）挂载在 `/data` 上。
![](https://main.qcloudimg.com/raw/3b786b5ccc36f2819b2659cf47afb422.png)
<span id="step3"></span>
3. 执行以下命令，解挂该分区的文件系统。
```
umount <挂载点>
```
本文以挂载点是 `/data` 为例，则执行：
```
umount /data
```
>? 请将云硬盘上**所有分区的文件系统**都解挂，可重复执行 [步骤2](#step2) 查看是否还有挂载。
> - 若有挂载，执行 [步骤3](#step3) 进行卸载。
> - 若无挂载，则如下图所示：
> 
![](https://main.qcloudimg.com/raw/c51d1e9215493837b4b0968aecb94f5c.png)
<span id="step4"></span>
4. 执行以下命令，进入 parted 分区工具。
```
parted '<磁盘路径>'
```
本文以磁盘路径是`/dev/vdb`为例，则执行：
```
parted '/dev/vdb'
```
5. 执行以下命令，将显示和操纵单位变成 sector（默认为GB）。
```
unit s
```
<span id="step6"></span>
6. 执行以下命令，查看分区信息，并记录已有分区的 Start 值。
```
print
```
>! 删除分区并新建后，Start 值必须保持不变，否则将会引起数据丢失。
>
![](https://main.qcloudimg.com/raw/47e0e8ae7f2c085cd4ff5d0d9cb97a69.png)
7. 执行以下命令，删除原有分区。
```
rm <分区 Number>
```
例如，由上图可知云硬盘上有一个分区，Number 为“1”，则执行：
```
 rm 1
```
分区已删除，回显信息如下图所示。
![](https://main.qcloudimg.com/raw/22477795f49dc195fa2447e821c5bfa3.png)
5. 执行以下命令，新建一个主分区。
```
mkpart primary <原分区起始扇区> 100%
```
其中，100%表示此分区到磁盘的最末尾。
由 [步骤6](#step6) 可得，本文中原分区删除前扇区由2048s开始，则 Start 值为2048。请根据您的实际情况填写 Start 值并执行以下命令：
```
mkpart primary 2048s 100%
```
如果出现如下图所示的状态，请输入`Ignore`。
![](//mccdn.qcloud.com/static/img/c45966e20dc856817c65fd6b81155e4a/image.png)
9. 执行以下命令，查看新分区是否已创建成功。
```
print
```
返回结果如下图所示，即表示新分区已创建成功。
![](https://main.qcloudimg.com/raw/436896f6b8c0c4fffa52162c10d4abf2.png)
10. 执行以下命令，退出 parted 工具。
```
quit
```
11. 执行以下命令，检查扩容后的分区。
```
e2fsck -f <分区路径>
```
本文以新建分区是1（即分区路径是`/dev/vdb1`）为例，则执行：
```
e2fsck -f /dev/vdb1
```
返回如下图所示结果。
![](//mccdn.qcloud.com/static/img/307f7a0c98eea05ca1d4560fe4e96f57/image.png)
12. 请根据您的实际情况，对新建分区上的文件系统进行扩容操作。
 - **EXT 文件系统**执行以下命令：
```
resize2fs <分区路径>
```
本文以分区路径是`/dev/vdb1`为例，则执行：
```
resize2fs /dev/vdb1
```
扩容成功则如下图所示：
![](//mccdn.qcloud.com/static/img/57d66da9b5020324703498dbef0b12f9/image.png)
 -  **XFS 文件系统**执行以下命令：
```
xfs_growfs <分区路径>
```
本文以分区路径是`/dev/vdb1`为例，则执行：
```
xfs_growfs /dev/vdb1
```
13. 执行以下命令，手动挂载新分区。
```
mount <分区路径> <挂载点>
```
本文以分区路径是`/dev/vdb1`，挂载点是`/data`为例，则执行：
```
mount /dev/vdb1 /data
```
14. 执行以下命令，查看新分区。
```
df -h
```
返回如下图信息说明挂载成功，即可以查看到数据盘。
![](https://main.qcloudimg.com/raw/b99b58b68ae1d156325392767cdc5c72.png)

<span id="Add"></span>
### 将扩容部分的容量格式化成独立的 GPT 分区
1. 以 root 用户执行以下命令， 确认云硬盘的容量变化。
```
parted <磁盘路径> print
```
本文以磁盘路径是`/dev/vdb`为例，则执行：
```
parted /dev/vdb print
```
若在过程中提示如下图所示信息，请输入 `Fix`。
![](https://main.qcloudimg.com/raw/69791b332c9237f5b4b4b392a4f0001f.png)
如下图所示，扩容后的云硬盘大小为2169GB，已有分区的大小为10.7GB。
![](https://main.qcloudimg.com/raw/26ddf5d567cb6d28c87ed40222ffede6.png)
<span id="Step2"></span>
2. 执行以下命令，确认该云硬盘是否还有分区已挂载。
```
mount | grep '<磁盘路径>' 
```
本文以磁盘路径是`/dev/vdb`为例，则执行：
```
mount | grep '/dev/vdb'
```
如下图所示，云硬盘上有一个分区（vdb1）挂载在 `/data` 上。
![](https://main.qcloudimg.com/raw/71e89299483c2fa21975fa6f3e112314.png)
<span id="Step3"></span>
3. 执行以下命令，解挂该分区的文件系统。
```
umount <挂载点>
```
本文以挂载点是`/data`为例，则执行：
```
umount /data
```
>? 请将云硬盘上**所有分区的文件系统**都解挂，可重复执行 [步骤2](#Step2) 查看是否还有挂载。
> - 若有挂载，执行 [步骤3](#Step3) 进行卸载。
> - 若无挂载，则如下图所示：
> 
![](https://main.qcloudimg.com/raw/cc22a30e399c428e8580ef1425729f4d.png)

4. 执行以下命令，进入 parted 分区工具。
```
parted '<磁盘路径>'
```
本文以磁盘路径是 `/dev/vdb` 为例，则执行：
```
parted '/dev/vdb'
```
<span id="Step5"></span>
5. 执行以下命令，查看分区信息，并记录已有分区的 End 值，以此值作为下一个分区的起始偏移值。
```
print
```
![](https://main.qcloudimg.com/raw/89e8e0e17f6fe713f5160267ee32348d.png)
6. 执行以下命令，新建一个主分区。此分区将从已有分区的末尾开始，覆盖硬盘所有的新增空间。
```
mkpart primary start end
```
由 [步骤5](#Step5) 可得，本文中 End 值为10.7GB，请您根据实际情况填写 End 值并执行以下命令：
```
mkpart primary 10.7GB 100%
```
7. 执行以下命令，查看新分区是否已创建成功。
```
print
```
输出结果如下，则已成功新建分区：
![](https://main.qcloudimg.com/raw/ccf3226b3efa667f8d098bc9d809e6a5.png)
8.  执行以下命令，退出 parted 工具。
```
quit
```
9. 执行以下命令，格式化新建的分区。
```
mkfs.<fstype> <分区路径> 
```
您可以自行选择文件系统的格式，例如 EXT2、EXT3 等。
本文以文件系统是 EXT3 为例，则执行： 
```
mkfs.ext3 /dev/vdb2
```
10. 执行以下命令，手动挂载新分区。
```
mount <分区路径> <挂载点>
```
本文以分区路径是`/dev/vdb2`，挂载点是`/data`为例，则执行：
```
mount /dev/vdb2 /data
```
14. 执行以下命令，查看新分区。
```
df -h
```
返回如下图信息说明挂载成功，即可以查看到数据盘。
![](https://main.qcloudimg.com/raw/52dc0e48943bb4d8635f1529c03bcdba.png)
