完成磁带网关及磁带的创建之后，您可以通过 Symantec NetBackup 备份软件将数据备份到虚拟磁带、对磁带进行存档以及管理虚拟磁带库 （VTL） 设备。下面将以 NetBackup 8 为例介绍如何通过 NBU 程序配置存储、将数据写入磁带、存档磁带以及还原数据。

有关如何使用 NetBackup 的详细信息，请参考 Veritas 网站上的 [使用帮助](https://www.veritas.com/content/support/zh_CN/search-results.html?q=*&fq=((document_type%3A%22document%22)%20AND%20(product_name%3A%22NetBackup%22)%20AND%20(locale%3A%22zh_CN%22))%20AND%20version%3A(%228.1.2%22)&docRepo=true&requestedRecords=20)。

## 连接 VTL 设备

### 在 Windows 客户端中连接到 VTL 设备
1. 在 Windows 开始菜单的搜索框中输入 iscsicpl.exe （iSCSI 发起程序），选中该程序。如果出现提示，则单击 YES 以运行 iSCSI 发起程序。
2. 在弹出的 iSCSI 发起程序对话框中选择，选择 【发现】选项卡，然后单击【发现门户】按钮。 
3. 在弹出的窗口中输入目标的 IP 地址，然后单击【确认】添加该目标门户。
  >?网关 IP 地址即安装网关的服务器地址，也可以在网关的详细信息中获取。如果您是使用 CVM 作为网关，则可以到 CVM 控制台获取该主机的 IP 地址 。
4. 选择【目标】选项卡，然后单击【刷新】。随后在【已发现的目标】框中显示所有十个磁带驱动器和介质更换器。目标的状态为 "未激活" 状态。 
5. 选择第一个设备，然后单击【连接】。然后重复，一次连接一个设备，将列出的设备均连接上。 
6. 在 Windows 客户端上，磁带驱动器的驱动程序提供商必须为 Microsoft。按以下过程验证驱动程序提供商，并在必要时更新驱动程序和提供商。
1）在 Windows 客户端上，启动 "设备管理器"。
2）展开 "磁带驱动器"，选中一个驱动，单击鼠标右键，在菜单展开菜单中单击【属性】。 
3）弹出 "设备属性" 对话框, 选中 "驱动程序" ，确认 "驱动程序提供商" 为 Microsoft。 
4）如果 "驱动程序提供商" 不是 Microsoft，则设置如下值： 
 1. 单击【更新驱动程序】。 
 2. 更新驱动程序软件" 对话框中，单击 "浏览计算机以查找驱动程序软件"。 
 3. 在 "浏览计算机以查找驱动程序软件" 对话框中，单击 "从计算机的设备驱动程序列表中选取"。 
 4. 选择 LTO Tape drive，然后单击 【下一步】。更新完成后，即可关闭窗口。 

 5）关闭 "更新驱动程序软件" 窗口，然后确认 "驱动程序提供商" 值现在设置为 Microsoft。  
 6）重复以上步骤以更新所有磁带驱动器。


### 在 Linux 客户端中连接到 VTL 设备
1. 安装 iscsi-initiator-utils RPM 包, 请使用下面的命令来安装该包。
	```
	sudo yum install iscsi-initiator-utils
	```
	
2. 确保 iSCSI 守护进程正在运行。对于 RHEL 5 或 RHEL 6，请使用以下命令。
	```
	##RHEL 5 或 RHEL 6，请使用以下命令
	sudo /etc/init.d/iscsi status
	
	##对于 RHEL 7，请使用以下命令
	sudo service iscsid status
	```
	
3. 使用以下发现命令发现 VTL 设备。
	```
	sudo /sbin/iscsiadm --mode discovery --type sendtargets --portal [网关IP]:3260
	```
	
	命令的输出内容类似如下示例输出内容：
	磁带网关：iqn.2003-07.com.qcloud:csg-022ef55-tapedrive-01
	
4. 请使用以下命令连接到目标。 请注意，您需要在连接命令中指定正确的[介质转换器目标名称/驱动目标名称]和[网关IP]。 
	```
	sudo /sbin/iscsiadm --mode node --targetname [介质转换器目标名称/驱动目标名称] --portal [网关IP]:3260,1 --login
	
	例如
	sudo /sbin/iscsiadm --mode node --targetname iqn.2003-07.com.qcloud:csg-022ef55-tapedrive-01 --portal 10.10.192.11:3260,1 --login
	```
	 "介质转换器目标名称" 及 "驱动目标名称" 可以在磁带网关详情获取。
	![](https://mc.qcloudimg.com/static/img/2b70d455091b26d10128faa2514c54ad/image.png) 
5. 验证卷是否已附加到客户端机器 (启动程序)。使用以下命令。
	```
	ls -l /dev/disk/by-path
	```
	 	命令的输出如下面的示例输出所示，
	```
	lrwxrwxrwx. 1 root root 9 Apr 16 19:31 ip-[网关IP]:iqn.2003-07.com.qcloud:csg-022ef55-tapedrive-01 -> ../../sda
	```
	启动程序设置完毕后，我们强烈建议您按[在 Linux 客户端上使用卷-优化配置](https://cloud.tencent.com/document/product/581/12272#.E4.BC.98.E5.8C.96.E9.85.8D.E7.BD.AE)中推荐的设置进行 iSCSI 配置调优。
	
## 配置 NetBackup
### 发现磁带网关驱动

1. 以管理员身份打开 NetBackup 管理控制台。
2. 单击 "Configure Storage Devices" 以打开设备配置向导。
	![](https://mc.qcloudimg.com/static/img/44b63cd016a09aa6118d2caebb3ce064/NBU01.png)
3. 单击【Next】。 
   ![](https://mc.qcloudimg.com/static/img/029e0cfa3d9ea4eae0f0ad8dd1eda738/NBU02.png)
4. 在 Device Hosts 列中，勾选您的计算机，然后单击 【Next】。NetBackup 程序将扫描您的计算机，并发现所有设备。
	![](https://mc.qcloudimg.com/static/img/8b052a75fba490bffe3212861ef7416c/NBU03.png) 
5. 扫描完成后，在 "Scanning Hosts" 页面上，单击 【Next】，在新的页面上，继续单击 【Next】。页面将列出找到的 10 个磁带驱动器以及您计算机上的介质转换器。
	![](https://mc.qcloudimg.com/static/img/c46bec6b7598e137d0db40e83473d1ab/NBU05.png) 
6. 在 "Backup Devices" 窗口中，单击 【Next】。 
7. 在 "Drag and Drop Configuration" 窗口中，确认已经勾选网关提供的介质更换器，然后单击 【Next】。 
	![](https://mc.qcloudimg.com/static/img/7cab243b2893c912526eaad17eecd6e5/NBU06.png)
8. 在随后显示的对话框中，单击【Yes】以将配置保存到您的计算机上。NetBackup 程序将更新设备配置。 在二次确认的对话框中单击 【Continue】。
   ![](https://mc.qcloudimg.com/static/img/4a7ccc2f31ca15a76efd7b573dd44594/NBU07.png)
9. 更新完成后，单击【Next】以使这些设备对 NetBackup 程序可用。
	![](https://mc.qcloudimg.com/static/img/5dfca347fc025606ab26c4ba5810159b/NBU09.png)
10. 单击 【Finish】以完成设置。


### 验证您的设备
1. 在 NetBackup 控制台中，展开 "Media and Device Management" 节点，然后展开 "Devices" 节点。选择 "Drives" 以显示所有磁带驱动器。 
![](https://mc.qcloudimg.com/static/img/ed8f57139f9ea6a00ed2a93690b56cfb/NBU10.png)
2. 在 "Devices" 节点中，选择 "Robots" 以显示您的所有介质更换器。 
![](https://mc.qcloudimg.com/static/img/0e2bf5e5248fa561be47ae63612736e9/NBU11.png)
3. 在 "All Robots" 窗格中，选中 TLD(0) (即您的机械手)，鼠标右键弹出菜单，然后选择 【Inventory Robot】。 
4. 在 "Robot Inventory" (机械手清点) 窗口中，确认 Select robot (选择机械手) 项目中的 Device-Host (设备主机) 列表中选择了您的主机。 
5. 确认从 "Robot" (机械手) 列表中选择了您的机械手。 
6. 在 "Robot Inventory" 窗口中，依次选择 "Update volume configuration"、"Empty media access port prior to update"，然后单击 【Start】 按钮。 
![](https://mc.qcloudimg.com/static/img/dfae26a009432ca616ae225dd91b354f/NBU23.png)  	 此过程随后将清点您在 NetBackup 企业介质管理 (EMM) 数据库中的介质更换器和虚拟磁带。NetBackup 将介质信息、设备配置和磁带状态存储在 EMM 中。 

7. 清点完成后，在 "Robot Inventory" 窗口中将出现磁带网关上已经创建的磁带，请单击 【Yes】。在此处选择 Yes 将更新配置，并将在导入/导出槽中找到的虚拟磁带移至虚拟磁带库。 
8. 关闭 Robot Inventory (机械手清点) 窗口。 
9. 在 Media 节点中，展开 Robots 节点，然后选择 TLD(0) 以显示对您的机械手 (介质更换器) 可用的所有虚拟磁带。 说明，如果您以前已将其他设备连接到 NetBackup 应用程序，则可能会有多个机械手。确保所选的机械手正确无误。  完成上述步骤后，您的 NetBackup 程序已连接到磁带网关设备，并使这些设备可供备份程序使用。

## 备份数据到磁带网关

### 创建卷池
#### 卷池是要用于备份的虚拟磁带的集合。

1. 打开 NetBackup 控制台。
2. 展开 "Media" 节点，鼠标右键单击 【Volume Pools】，选择 【New Volume Pool】。 
3. 在弹出的 "New Volume Pool" 对话框中，输入卷池的名称及描述，键入卷池的说明，单击【OK】。创建的卷池即添加到卷池列表。   ![](https://mc.qcloudimg.com/static/img/a2b2e6583523ae10ef4be1c910885d48/NBU13.png)

#### 将虚拟磁带添加到卷池
1. 选中 "Media", 页面会列出之前发现的 Volumes。
2. 鼠标右键单击需要加入卷池的 Volume，在弹出的窗口中单击【Change】，在弹出的窗口中更改 Volume Pool,然后单击【OK】。
![](https://mc.qcloudimg.com/static/img/76b71d3fde55f22e11ce93bb49016fc6/NBU24.png)
3. 此时可通过展开 "Volume Pools" 节点并刚刚创建的卷池，确认新建的 Volume 已经在您的卷池中。 


#### 创建备份策略
备份策略中将会指定何时执行备份操作、备份什么数据以及备份数据存储至哪个卷池。

1. 选中 "NetBackup Management", 单击 "Create a Policy" 以打开 Policy Configuration Wizard 窗口。 
![](https://mc.qcloudimg.com/static/img/de6f7daf3c2e306c52fd6366db956239/NBU18.png)
2. 选择 File systems, databases, applications，然后单击【Next】。 
3. 输入策略的名称，"Select the policy type"列表中选择 "MS-Windows"，然后单击 【Next】。 
4. 在 Client List 窗口中，单击【Add】，在 Name 列中输入您的计算机的主机名，然后单击 【Next】。本步骤将您定义的策略应用于本地主机 (客户端计算机)。 
5. 在 "Backup Selection" 窗口中，单击【Add】，然后单击文件夹图标。 在 Browse 窗口中，浏览到要备份的文件夹或文件，单击【OK】，然后单击【Next】。 
![](https://mc.qcloudimg.com/static/img/52351ea25943c88fd21b45b8b3f57d96/NBU19.png)
6. 在 "Backup Types" 窗口中，接受默认值，然后单击 【Next】。若您要自行开始备份，则选择 User Backup (用户备份)。 
![](https://mc.qcloudimg.com/static/img/6ff080e3bb32de65cbba32932b8a4349/NBU20.png)
7. 在 "Frequency and Retention"窗口中，选择要应用于备份的频率和保留策略。根据您的需要设置备份频率，然后单击 【Next】。 
8. 在 "Start" 窗口中，选择 Off hours（仅在业余时间备份您的文件夹），然后单击【Next】。
![](https://mc.qcloudimg.com/static/img/a436b3674b5e5beffa2799e51a525b4a/NBU21.png) 
9. 在 Policy Configuration 向导中，选择 Finish。 

#### 执行手动备份
除了自动备份策略以外，您还可以随时执行手动备份，手动备份操作步骤如下。

1. 在 NetBackup 控制台的导航窗格上，展开 NetBackup Management 节点。 
2. 展开 Policies (策略) 节点。 
3. 右键菜单，然后单击 【Manual Backup】。
![](https://mc.qcloudimg.com/static/img/f697db1611516a1014b34a4248e9fdf9/NBU22.png) 
4. 在 Manual Backup 窗口中，输入计划名称，再选择一个客户端，然后单击【OK】。 
5. 在随后确认对话框中，选择 "差量备份" 或 "全量备份"，单击 【OK】并退出设置。 
6. 在导航窗格上，选择 Activity Monitor 以在 Job ID 列中查看备份的状态。   
要查找 NetBackup 在备份期间写入到文件数据的虚拟磁带的条码，请查看 Job Details 窗口 (如以下过程中所述)。在下一部分中的对磁带进行存档的过程中，将需要用到此条码。

#### 查找磁带的条码
1. 在 Activity Monitor 中，鼠标右键单击打开 Job ID 列中您的备份作业的标识符菜单，然后单击【Details】。 
2. 在 Job Details 窗口中，单击【Detailed Status】选项卡。 
3. 在 Status 框中，找到介质 ID。介质 ID 可帮助您确定已将数据写入到哪个磁带。   
通过上面的步骤，您已成功部署了磁带网关、创建了虚拟磁带并备份了您的数据。

## 将磁带归档
对磁带进行存档时，磁带网关会将磁带从网关的虚拟磁带库 (VTL) 移至存档，这将提供脱机存储。通过使用备份应用程序弹出磁带，来将磁带进行存档。 操作步骤如下：

1. 在 NetBackup 管理控制台中，展开 Media and Device Management (介质和设备管理) 节点，然后展开 Media (介质) 节点。 
2. 在列出的磁带中，鼠标右键单击需要弹出的磁带，单击 【Eject Volume From Robot】。 
![](https://mc.qcloudimg.com/static/img/c56830bab8e729835590388ec2e2d70e/NBU25.png)
3. 在 Eject Volumes 窗口中，再次确认 Media ID，然后单击【Eject】。 
4. 在弹出对话框中，单击【Yes】。弹出过程完毕后，Eject Volumes 对话框中磁带的状态指示弹出已成功。 
5. 单击【Close】，关闭 Eject Volumes 窗口。 
6. 当执行弹出磁带的操作后，在 CSG 控制台中，该磁带状态会由 "正常" 转变为 "归档中"。当磁带弹出后数据会转存入归档存储中，此时磁带状态会转变为 "已归档"。 

## 已归档磁带的取回

应用程序是无法从已归档磁带中取出数据。为了读取归档数据，您需要磁带数据取回。

1. 要将已归档磁带取回到磁带网关。您可以在 CSG 控制台，选中 "磁带列表", 找到相应的已归档磁带，单击【取回】，详细操作步骤请参考 [磁带取回](https://cloud.tencent.com/document/product/581/12507#.E7.A3.81.E5.B8.A6.E5.8F.96.E5.9B.9E)。 
2. 等待磁带取回后， 您可使用随 Symantec NetBackup 应用程序一起安装的“备份、存档和还原”软件。此过程与从物理磁带还原数据相同。

