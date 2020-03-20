## 操作场景

[扩容云硬盘](https://cloud.tencent.com/document/product/362/5747) 完成后，需要将扩容部分的容量划分至已有分区内，或者将扩容部分的容量格式化成一个独立的新分区。
如果您在 [扩容云硬盘](https://cloud.tencent.com/document/product/362/5747) 时，云服务器及云硬盘状态符合下表中的情形，请执行对应操作：
<table>
	<tr>
	<th>云服务器状态</th><th>云硬盘状态</th><th>需执行操作</th>
	</tr>
	<tr>
	<td>正常运行状态</td>
	<td>已挂载</td>
	<td><a href="https://cloud.tencent.com/document/product/213/4928">重启实例</a> 或  <a href="Scaning">重新扫描磁盘</a> 待识别扩容后的云硬盘空间后再 <a href="Extending">扩展卷</a>。</td>
	</tr>
	<tr>
	<td rowspan=2>关机状态</td>
	<td>待挂载</td>
	<td>扩容后的硬盘空间将自动识别，请 <a href="https://cloud.tencent.com/document/product/362/32402">挂载</a> 后 <a href="https://cloud.tencent.com/document/product/362/32403">初始化云硬盘</a>。</td>
	</tr>
	<tr>
	<td>已挂载</td>
	<td>扩容后的硬盘空间将自动识别，云服务器开机后及可正常使用。</td>
	</tr>
</table>

>!
>- 扩容文件系统操作不慎可能影响已有数据，因此强烈建议您在操作前手动 [创建快照](https://cloud.tencent.com/document/product/362/5755) 备份数据。
>- 扩容文件系统需要 [重启实例](https://cloud.tencent.com/document/product/213/4928) 或进行重新扫描磁盘及扩展卷操作，将导致一定时间的业务中断，建议您选择合适的时间谨慎操作。
>


## 前提条件

- 已 [扩容云硬盘](https://cloud.tencent.com/document/product/362/5747)  空间。
- 该云硬盘已 [挂载](https://cloud.tencent.com/document/product/362/5745) 到 Windows 云服务器且已创建文件系统。
- 已 [登录](https://cloud.tencent.com/document/product/213/5435) 待扩展分区及文件系统的 Windows 云服务器。
>?本文以 Windows Server 2008 操作系统的云服务器，且云硬盘已挂载至该云服务器为例，不同操作系统的扩容操作可能不同，本文仅供参考。
>

## 操作步骤

<span id="Scaning"></span>
### （可选）重新扫描磁盘

1. 打开【计算机管理】。
2. 在左侧导航栏中，选择【存储】>【磁盘管理】。
3. 右键单击 【磁盘管理】，选择 【重新扫描磁盘】。如下图所示：
![](https://main.qcloudimg.com/raw/08bc972c1461a316300ab5b21ffb452b.png)
4. 扫描完成后，查看数据盘是否已经变为扩容后的大小（本例中执行扫描操作后识别到硬盘由原来的10GB扩容到了50GB）。如下图所示：
![](https://main.qcloudimg.com/raw/f1846bb0f53f025bc781eacc2706d7ed.png)

<span id="Extending"></span>
### 扩展卷

1. 右键单击磁盘空间的任一空白处，选择【扩展卷】。
2. 根据扩展卷向导的指引完成扩展卷操作。完成后新增的数据盘空间将会合入原有卷中。如下图所示：
![](https://main.qcloudimg.com/raw/f2be002e959f6b309ff3b674dee9078f.png)

## 相关操作
[扩展分区及文件系统（Linux）](https://cloud.tencent.com/document/product/362/6738)
