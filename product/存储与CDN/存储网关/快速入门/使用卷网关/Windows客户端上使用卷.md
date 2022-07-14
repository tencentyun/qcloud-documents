
您需要使用 Microsoft Windows iSCSI 启动程序来连接到卷，将卷作为 Windows 客户端上的本地设备。

>!由于 iSCSI 协议限制，不支持将多个主机连接到同一个 iSCSI 目标。

### 找到并启动 iSCSI 发起程序
在 Windows 开始菜单的搜索框中输入 iscsicpl.exe （iSCSI 发起程序），选中该程序。如果出现提示，则单击 YES 以运行 iSCSI 发起程序。
![](https://mc.qcloudimg.com/static/img/ae9a867a22344c46d54d06f8684942c2/image.png)


### 设置 iSCSI 门户
在弹出的 iSCSI 发起程序对话框中选择【发现】选项卡，并单击【发现门户】按钮。

![](https://mc.qcloudimg.com/static/img/92e517e7d4d977370504c31ab7ca969a/image.png)

在弹出的窗口中输入目标的 IP 地址，然后单击【确认】添加该目标门户。
>?网关 IP 地址即安装网关的服务器地址，也可以在网关的详细信息中获取。如果您是使用 CVM 作为网关，则可以到 CVM 控制台获取该主机的 IP 地址*
![](https://mc.qcloudimg.com/static/img/9bb7de1aea7642b67d4a0b98bdf40213/image.png)


### 连接到 iSCSI Target
选中【目标】选项卡，上一步中添加的目标门户仍为未激活状态。选中该目标后单击【连接】按钮。
![](https://mc.qcloudimg.com/static/img/659962a9f392eeee1bd70433bf7b566c/iscsi+taget.png)

在弹出的对话窗中确认 target 名称并勾选 “将此连接添加到收藏目标列表” ，单击【确认】。
![](https://mc.qcloudimg.com/static/img/700ce70c906dc28dd7a39a0ec4c93383/image.png)

在确认状态为 “已连接” 之后，单击【确认】按钮并退出。
![](https://mc.qcloudimg.com/static/img/ee71b2ba01d5227473296094c02ef0ec/image.png)



### 后续
- 初始化卷
  在 Windows 开始菜单的搜索框中输入 "diskmgmt.msc" ， 打开 “创建并格式化硬盘分区”。
  ![](https://mc.qcloudimg.com/static/img/9d8e1b3870599628ed94f5e0c072e849/image.png)
  弹出初始化磁盘窗口，选择 MBR (Master Boot Record) 作为分区形式，单击【确认】按钮。
  ![](https://mc.qcloudimg.com/static/img/5a0cbaffe94b8b980f2e6ab567a33c59/image.png)
  
- 创建简单卷
  在磁盘管理界面，找到刚刚发现的磁盘，在下面区域单击鼠标右键后出现菜单，单击【新建简单卷】按钮。然后，根据向导来分区并格式化磁盘。
  ![](https://mc.qcloudimg.com/static/img/5ca6d71637809651ba9c00ba5dc1d2f1/image.png)
	
- 往上面步骤添加的磁盘中进行数据写入、通过 CSG 控制台创建卷快照、将快照还原为一个卷。

### 优化配置
为了保证您使用存储网关读写数据的稳定性，我们强烈建议您按照下列步骤进行优化配置。

1. 修改请求排队的最长时间
	a.	启动注册表编辑器 (Regedit.exe)。
	b.	导航到设备类别的全局唯一标识符 (GUID) 密钥，其中包含 iSCSI 控制器设置，如下所示。
```
HKEY_Local_Machine\SYSTEM\CurrentControlSet\Control\Class\{4D36E97B-E325-11CE-BFC1-08002BE10318}
```
		
	>!确保处于 CurrentControlSet 子项内，而非 ControlSet001 或 ControlSet002 等其他控制集内。
	
	c. 查找 Microsoft iSCSI 启动程序的子项，以下显示为 <实例编号>。该项由四位数字表示，例如 0000。
	```
	HKEY_Local_Machine\SYSTEM\CurrentControlSet\Control\Class\{4D36E97B-E325-11CE-BFC1-08002BE10318}\<Instance Number>
	```		
根据计算机上安装的内容，Microsoft iSCSI 启动程序可能不是子项 0000。可通过验证字符串 DriverDesc 是否具有以下示例所示的 Microsoft iSCSI Initiator 值来确保选择了纠正的子项。
![](https://mc.qcloudimg.com/static/img/344ceb4fedcb91867d2090a03d5466ed/iscsi-windows-registry-10.png)
	d. 要显示 iSCSI 设置，请选择 Parameters 子项。
	e. 打开 MaxRequestHoldTime DWORD (32-bit) 值的菜单 (右键单击) ，选择 ”修改“，然后将该值改为 600。以下示例显示为 600 的 MaxRequestHoldTime DWORD 值。该值表示 600 秒的保持时间。
![](https://mc.qcloudimg.com/static/img/d72cb08e6a9e92f61254f79a6d1b77f6/iscsi-windows-registry-20.png)
		

2. 修改磁盘超时配置
	a.	如果您尚未启动注册表编辑器 (Regedit.exe)，请将其启动。
	b.	导航到 CurrentControlSet 的 Services (服务) 子项中的 Disk (磁盘) 子项，如下所示。
	```
	HKEY_Local_Machine\SYSTEM\CurrentControlSet\Services\Disk
	```
	c. 打开 TimeOutValue DWORD (32 位) 值的上下文 (右键单击) 菜单，选择 Modify，然后将该值改为 600。以下示例显示了值为 600 的 TimeOutValue DWORD 值。该值表示 600 秒的超时时间。
![](https://mc.qcloudimg.com/static/img/e5c42772f04772539a99825c3d4fe72b/iscsi-windows-registry-30.png)
3. 重新启动系统，让上述修改的配置生效。
	重新启动之前，必须确保刷新了对卷进行的所有写入操作的结果。请在重启前将任何映射的存储卷磁盘脱机。




