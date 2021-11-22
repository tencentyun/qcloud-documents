## 简介

本文为您详细介绍如何在 Windows 客户端上使用 CFS 文件系统。本指引以 Windows Server 2012 R2 为示例截图，其他版本操作系统，例如 Windows Server 2008 及 Windows Server 2016 操作方法相同。


## 步骤一: 创建文件系统及挂载点

详细步骤请参见 [创建文件系统及挂载点](https://cloud.tencent.com/document/product/582/9132)。


## 步骤二: 连接实例

本部分操作介绍登录 Windows 云服务器的常用方法，不同情况下可以使用不同的登录方式，此处介绍控制台登录，更多登录方式请见 [登录 Windows 实例](https://cloud.tencent.com/document/product/213/5435) 。

#### 前提条件

登录到云服务器时，需要使用管理员帐号和对应的密码。

- 管理员账号：对于 Windows 类型的实例，管理员帐号统一为 Administrator。
- 密码：密码为购买云服务器时设置的密码。

#### 控制台登录云服务器

1. 在 [云服务器](https://console.cloud.tencent.com/cvm/index) 列表的操作列，单击**登录**即可通过 VNC 连接至 Windows 云服务器。
2. 通过单击左上角发送**Ctrl-Alt-Delete**命令进入系统登录界面。
3. 输入帐号（Administrator）和密码即可登录。

>! 该终端为独享，即同一时间只有一个用户可以使用控制台登录。
>

#### 验证网络通信

挂载前，需要确认客户端与文件系统的网络可达性（需要在 Windows 客户端启用 Telnet 服务）。可以通过 telnet 命令验证（例如 telnet 192.168.1.1 445），具体各个协议及客户端要求开放端口信息如下：

| 文件系统协议 | 客户端开放端口 | 确认网络联通性            |
| ------------ | -------------- | ------------------------- |
| NFS 3.0      | 111，892，2049 | telnet 111或者892或者2049 |
| NFS 4.0      | 2049           | telnet 2049               |
| CIFS/SMB     | 445            | telnet 445                |


## 步骤三: 挂载文件系统

从最佳实践的角度建议您使用 SMB 挂载 CFS 文件系统。

### 挂载 CIFS/SMB 文件系统

挂载 CIFS/SMB 文件系统有两种方式：通过图形界面挂载和通过命令行挂载。

#### 通过命令行挂载文件系统

请使用 FSID 进行挂载文件系统，挂载命令如下：
```bash
net use <共享目录名称>: \\<挂载点 IP>\FSID 
```

示例：
```bash
net use X: \\10.10.11.12\fjie120
```

>! FSID 可以到**[文件存储控制台](https://console.cloud.tencent.com/cfs) > 文件系统详情 > 挂载点信息**中获取。
>

#### 通过图形界面挂载文件系统

1. 打开 "映射网络驱动器"
   登录到需要挂载文件系统的 Windows 上，在 "开始" 菜单中找到 "计算机"，单击鼠标右键出现菜单，单击菜单中的 "映射网络驱动器"。 
   ![](https://main.qcloudimg.com/raw/515b5b21a19e3f3518c75441326e1800.png)
   ![](https://main.qcloudimg.com/raw/b0396ce0f8f108f3e89a2f2bfb3d7f71.png)
2. 输入访问路径
   在弹出的设置窗口中设置 "驱动器" 盘符名称及文件夹（即在 CIFS/SMB 文件系统中看到的挂载目录）。
   ![](https://main.qcloudimg.com/raw/8d58ee713b9e072156caf8019b4242d5.png)
3. 验证读写
   确认后，页面直接进入到已经挂载的文件系统中。可以右键新建一个文件来验证读写的正确性。
	 <img src="https://main.qcloudimg.com/raw/208537681d0ab96cd801e22332a419a9.jpeg" width="80%">


### 挂载 NFS 文件系统

#### 1. 开启 NFS 服务

挂载前，请确保系统已经启动 NFS 服务。

选择**控制面板 > 程序 > 打开或关闭 Windows 功能 > 特性**页签中勾选**NFS 客户端**，勾选 **NFS 客户端**即可开启 Windows NFS 客户端服务。
<img src="https://mc.qcloudimg.com/static/img/4f9d7ac7b877ceffc5bc2b1d7c050a24/image.png" width="80%">

#### 2. 验证 NFS 服务是否启动

打开 Windows 下的命令行工具，在面板中执行如下命令，若返回 NFS 相关信息则表示 NFS 客户端正常运行中。
```bash
mount -h
```
<img src="https://mc.qcloudimg.com/static/img/4e4f9db217874ccec91ac1f888c8e451/image.png" width="80%">


#### 3. 添加匿名访问用户和用户组

3.1 打开注册表
在命令行窗口输入 regedit 命令，回车即可打开注册表窗口。
<img src="https://mc.qcloudimg.com/static/img/c9fca9a1b123a5b2dbc69b0ce66d539f/image.png" width="80%">

3.2 添加配置项 AnonymousUid 和 AnonymousGid
在打开的注册表中找到如下路径并选中。 
```bash
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Default
```

在右边空白处右键单击，弹出**new**, 在菜单中选择 **DWORD(32-bit) Value** 或者 **QWORD(64-bit) Value**（根据您的操作系统位数选择）。此时，在列表中会出现一条新的记录，把名称栏修改为 AnonymousUid 即可，数据值采用默认的0。使用同样方法继续添加一条名称为 AnonymousGid 的记录，数据也采用默认的0。
<img src="https://mc.qcloudimg.com/static/img/381cdc3b68fb35be5dcceb2a4c962e33/image.png" width="80%">

添加完毕如下图所示：
<img src="https://main.qcloudimg.com/raw/9af3f35d4b78a2e17cf2ef44fa6863d7.png" width="80%">

3.3 重启使配置生效
关闭注册表，在命令行工具中依次执行如下命令，重启 NFS 客户端服务，使修改的注册表生效。或者通过重启 Windows 系统，使修改的注册表生效。
```
net stop nfsclnt
```
```
net stop nfsrdr
```
```
net start nfsrdr
```
```
net start nfsclnt
```

#### 4. 挂载NFS文件系统

挂载文件系统有两种方式：通过图形界面挂载和通过 CMD 命令行挂载。

#### 通过命令行挂载文件系统
  在 Windows 的命令行工具中输入如下命令，挂载文件系统。其中，系统缺省子目录为 FSID。
```bash
mount  <挂载点IP>:/<FSID> <共享目录名称>:
```
示例：
```bash
mount 10.10.0.12:/z3r6k95r X:
```
> ! FSID 挂载命令可以到**文件存储控制台 > 文件系统详情 > 挂载点信息**中获取。


#### 通过图形界面挂载文件系统

  a. 打开 "映射网络驱动器"
  登录需要挂载文件系统的 Windows 上，在 "开始" 菜单中找到 "计算机"，单击鼠标右键，单击菜单中的 "映射网络驱动器"。 
  ![](https://main.qcloudimg.com/raw/515b5b21a19e3f3518c75441326e1800.png)
  ![](https://main.qcloudimg.com/raw/b0396ce0f8f108f3e89a2f2bfb3d7f71.png)
  
b. 输入访问路径
  在弹出的设置窗口中设置 "驱动器" 盘符名称及文件夹（即在 NFS 文件系统中看到的挂载目录）。
  ![](https://main.qcloudimg.com/raw/8d58ee713b9e072156caf8019b4242d5.png)
	<img src="https://main.qcloudimg.com/raw/cef8f3bbd2df72a37590ce5605a9732d.png" width="80%">
	
c. 检查文件系统权限
	检查上述文件系统是否使用了 root 权限进行挂载，打开 Windows 系统命令行工具，输入`mount`命令：
	在命令行中确认，若 UID 与 GID 分别为0，则表示文件系统是使用 root 权限挂载，此时可以开始正常使用文件系统了；若 UID 与GID 分别为 -2 等其他值，则可能导致无法正常写入数据等，请重复前面的步骤、保证文件系统是以 root 权限挂载。
	<img src="https://main.qcloudimg.com/raw/3ccc26279bb8d73c16eae43f89fea8c7.png" width="80%">
  
若以上界面中出现" locking=yes"，为了避免文件锁导致读写异常（NFS v3 暂不支持锁），请按以下步骤修改注册表：

（1）找到如下注册表路径 **HKEY_LOCAL_MACHINE > SOFTWARE > Microsoft > ClientForNFS > CurrentVersion > User > Default > Mount**。

（2）在右侧内容区右键新建 **DWORD (32-位)值**，名称为“Locking”，值为“0”。


d. 验证读写
  确认后，页面直接进入到已经挂载的文件系统中。可以右键新建一个文件来验证读写的正确性。
	<img src="https://main.qcloudimg.com/raw/208537681d0ab96cd801e22332a419a9.jpeg" width="80%">


## 步骤四: 卸载文件系统

#### 通过 CMD 命令卸载共享目录 

当某些情况下需要卸载共享目录，请打开命令行终端后使用如下命令。其中 "目录名称" 为根目录或者文件系统的完整路径。

NFS示例：
```bash
umount X：
```

SMB示例：
```net use x: /del
```

#### 通过图形界面卸载共享目录

要断开已经挂载的文件系统，只需鼠标右键单击磁盘，再出现的菜单中单击**断开**选项，即可断开文件系统的连接。
 <img src="https://mc.qcloudimg.com/static/img/376cd0547aa64f4d519e5444c5a58f93/image.png" width="80%">


## 步骤五: 终止资源

>! 文件系统删除后，资源不可恢复，建议您删除文件系统之前，先备份资源。
>

您可以从腾讯云控制台终止文件系统。进入腾讯云 [文件存储控制台](https://console.cloud.tencent.com/cfs/fs)，选中需要终止的文件系统，单击**删除**并**确认**，即可删除文件系统。


