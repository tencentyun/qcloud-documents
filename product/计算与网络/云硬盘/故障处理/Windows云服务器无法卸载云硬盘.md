## 现象描述
Windows 云服务器在执行磁盘脱机操作后，通过控制台 [卸载云硬盘](https://cloud.tencent.com/document/product/362/6740) 时失败，云硬盘未成功卸载。

## 可能原因
操作系统的进程（例如 Taskmgr.exe、svchost.exe、System 等）占用磁盘，导致无法成功卸载。

## 解决思路
1. 检查磁盘是否为“脱机”状态。
2. 通过“事件查看器”查看占用磁盘的进程，结束进程后再次尝试卸载。

## 处理步骤

<dx-alert infotype="explain" title="">
本文使用的 Windows 云服务器操作系统以 Windows Server 2012 R2 数据中心版 64位中文版为例，不同版本操作系统步骤有一定区别，请您结合实际情况进行操作。
</dx-alert>

### 检查磁盘状态
1. 以管理员身份登录 Windows 云服务器，详情请参见 [使用标准方式登录 Windows 实例](https://cloud.tencent.com/document/product/213/57778)。
2. 在云服务器操作系统界面中，右键单击左下角的 <img src="https://main.qcloudimg.com/raw/3d815ac1c196b47b2eea7c3a516c3d88.png" style="margin:-3px 0px">。
3. 在弹出菜单中，选择**磁盘管理**。
4. 在“磁盘管理”窗口中，查看需卸载的云硬盘是否为“脱机”状态。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/78bf6ef8b59a76cbebfd84b0527fd995.png)
 - 是，则进行下一步。
 - 否，请右键单击磁盘状态区域，在弹出菜单中单击**脱机**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/c0c14c1f0f2c8c1ef31b89ea8975d6ec.png)

### 定位并结束相关进程
1. 在云服务器操作系统界面中，右键单击左下角的 <img src="https://main.qcloudimg.com/raw/3d815ac1c196b47b2eea7c3a516c3d88.png" style="margin:-3px 0px">。
2. 在弹出菜单中，选择**事件查看器**。
3. 在“事件查看器”窗口中，选择左侧目录 **Windows 日志** > **系统**。
4. 在系统日志中，单击查看告警信息，可定位占用磁盘的进程为 Taskmgr.exe。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/2a1104135e1795a450fc81d9751d382e.png)
5. 结束该进程，并再次尝试 [使用控制台卸载云硬盘](https://cloud.tencent.com/document/product/362/6740#useConsole)。
若您无法手动结束问题进程（例如 svchost.exe、System 等系统进程），则请参考 [关机实例](https://cloud.tencent.com/document/product/213/4929) 将云服务器关机后，再次尝试 [使用控制台卸载云硬盘](https://cloud.tencent.com/document/product/362/6740#useConsole)。
