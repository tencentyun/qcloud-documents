## 操作场景
云服务器购买或重装后，需要进行数据盘的分区与格式化。本文档介绍 Windows 系统云服务器进行数据盘分区与格式化操作。
不同 Windows 系统版本（如 Windows 2012、Windows 2008、Windows 2003等）仅在进入“磁盘管理”界面路径不同，其他格式化与分区操作基本一致。本文档以 Windows 2012 R2 为例进行格式化与分区操作说明。

## 操作步骤
<span id="OnlineSettings"></span>
### 联机设置
在 Windows 操作系统下，常需要在磁盘管理中设置联机。为更方便使用弹性云硬盘，建议您对操作系统执行以下修改：
1. 登录 Windows 云服务器。
2. 单击  <img src="https://main.qcloudimg.com/raw/f0c84862ef30956c201c3e7c85a26eec.png" style="margin:0;"></img>，打开命令行窗口。
3. 输入 `diskpart` 命令，按 **Enter**。
4. 输入 `san policy=onlineall` 命令，按 **Enter**。如下图所示：
![](//mc.qcloudimg.com/static/img/d0b5082e73aad74d104980fbe74fe6dd/image.png)
执行操作后，弹性云硬盘将重新挂载到 Windows 云服务器上。若已包含有效的文件系统，则可以直接开始使用。

### 格式化数据盘
>! 如果您购买了数据盘，则需要格式化数据盘才可使用。如果您未购买数据盘，请跳过此操作。
>
1. 登录 Windows 云服务器。
2. 单击 <img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin:0;"></img> >【服务器管理器】>【工具】>【计算机管理】>【存储】>【磁盘管理】。
3. 右键单击磁盘1，选择【联机】。如下图所示：
![](//mc.qcloudimg.com/static/img/1217193557509925a622dcdb81aa2e35/image.png)
4. 右键单击磁盘1，选择【初始化磁盘】。如下图所示：
![](//mc.qcloudimg.com/static/img/94ab92867d77ea69bc803a0b20f2b941/image.png)
5. 在弹出的“初始化磁盘”窗口中，根据分区方式的不同，选择【GPT】或【MBR】，单击【确定】。如下图所示：
>! 若磁盘大于2TB ，请选择 GPT 分区形式。
> 
![](//mc.qcloudimg.com/static/img/1f7b0f72767193cfa662e188c86cf31b/image.png)

### 磁盘分区

1. 在未分配的空间处右键单击，选择【新建简单卷】。如下图所示：
![](https://main.qcloudimg.com/raw/3dfc7ff72b00643d23792961d828a1a0.png)	
2. 在弹出的“新建简单卷向导”窗口中，单击【下一步】。如下图所示：
![](https://main.qcloudimg.com/raw/820dc00db75829dfec3d1317e1d94dab.png)
3. 根据实际需求，设置分区所需磁盘大小，单击【下一步】。如下图所示：
![](https://main.qcloudimg.com/raw/b4ccf0bb8335a62ae7b12f6fa1690173.png)
4. 根据实际需求，分配驱动器号，单击【下一步】。如下图所示：
![](https://main.qcloudimg.com/raw/ad062088d9e4d23ce9ca7f0dff2bc01e.png)	
5. 根据实际需求，选择文件系统，勾选【执行快速格式化】，单击【下一步】。如下图所示：
![](https://main.qcloudimg.com/raw/eeb70c5715a6d009669bc906c0e8e885.png)
6. 完成新建简单卷，单击【完成】。如下图所示：
![](https://main.qcloudimg.com/raw/25bd898931fdfa31976c0659e747429d.png)
7. 打开【这台电脑】，查看新分区。如下图所示：
![](https://main.qcloudimg.com/raw/dff297cdee73ea2367332498dfb70015.png)


