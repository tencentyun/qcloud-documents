
云服务器购买或重装后，需要进行数据盘的分区与格式化。本文档介绍 Windows 系统云服务器进行数据盘分区与格式化操作。
不同 Windows 系统版本（如 Windows 2012、Windows 2008、Windows 2003等）仅在进入“磁盘管理”界面路径不同，其他格式化与分区操作基本一致。本文档以 Windows 2012 R2 为例进行格式化与分区操作说明。

## 前提条件
 - 已购买数据盘的用户，需要格式化数据盘才可使用。未购买数据盘的用户可以跳过此步骤。
 - 请确保您已完成步骤三操作，登录到云服务器。

## 格式化数据盘

 1. 登录 Windows 云服务器。

 2. 单击【开始】-【服务器管理器】-【工具】-【计算机管理】-【存储】-【磁盘管理】。

 3. 在磁盘 1 上右键单击，选择【联机】：
	![](//mc.qcloudimg.com/static/img/1217193557509925a622dcdb81aa2e35/image.png)

 4. 右键单击，选择【初始化磁盘】：
	![](//mc.qcloudimg.com/static/img/94ab92867d77ea69bc803a0b20f2b941/image.png)

 5. 根据分区方式的不同，选择【GPT】或【MBR】，单击【确定】按钮：
 > **注意：**
 > 磁盘大于 2TB ，一定要选择 GPT 分区形式。
	![](//mc.qcloudimg.com/static/img/1f7b0f72767193cfa662e188c86cf31b/image.png)

## 磁盘分区

 1. 在未分配的空间处右击，选择【新建简单卷】：
	![](//mc.qcloudimg.com/static/img/a6ca720af2082d7a470ece17a8e13f5d/image.png)
	
 2. 在弹出的“新建简单卷向导”窗口中，单击【下一步】：
	![](//mc.qcloudimg.com/static/img/10fdcd70b510a57919c6a40cf43452a7/image.png)
	
 3. 输入分区所需磁盘大小，单击【下一步】：
	![](//mc.qcloudimg.com/static/img/05c8d1425a0208597b1d2c75a9c811b6/image.png)
	
 4. 输入驱动器号，单击【下一步】：
	![](//mc.qcloudimg.com/static/img/737ed569049ad617715efb06fe44e7b2/image.png)
	
 5. 选择文件系统，格式化分区，单击【下一步】：
	![](//mc.qcloudimg.com/static/img/896cb3f2705fb9fcd04c236b8fb9ec59/image.png)
	
 6. 完成新建简单卷，单击【完成】：
	![](//mc.qcloudimg.com/static/img/1e257b9c76d80f30b34f612496b8007b/image.png)
	
 7. 在【开始】中打开【这台电脑】，查看新分区：
	![](//mc.qcloudimg.com/static/img/1cbb4ad1c3c01852a00a1415526a3e12/image.png)

## 联机设置
在 Windows 操作系统下，常需要在磁盘管理中设置联机。为更方便使用弹性云硬盘，建议您对操作系统执行修改。
 1. 登录 Windows 云服务器。
 2. 键盘快捷键【Windows + R】，在弹出框中输入【cmd】，单击【确定】进入命令行。
 3. 输入命令`diskpart`回车。
 4. 输入命令`san policy=onlineall`回车
 ![](//mc.qcloudimg.com/static/img/d0b5082e73aad74d104980fbe74fe6dd/image.png)

执行操作后，弹性云硬盘重新挂载到 Windows 云服务器上，如已包含有效的文件系统，则可以直接开始使用。
