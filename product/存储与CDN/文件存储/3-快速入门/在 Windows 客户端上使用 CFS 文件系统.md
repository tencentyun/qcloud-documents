## 简介

本文为您详细介绍如何在 Windows 客户端上使用文件存储（Cloud File Storage，CFS）系统。本指引以 Windows Server 2012 R2 为例，其他版本操作系统，例如 Windows Server 2008 及 Windows Server 2016 操作方法相同。


## 步骤1：创建文件系统及挂载点

详细步骤请参见 [创建文件系统及挂载点](https://cloud.tencent.com/document/product/582/9132)。


## 步骤2：连接实例

1. [使用标准方式登录 Windows 实例](https://cloud.tencent.com/document/product/213/57778)。
如需使用其他登录方式，请参见 [登录 Windows 实例](https://cloud.tencent.com/document/product/213/35697) 文档。
2. 验证网络通信。
挂载前，需要确认客户端与文件系统的网络可达性（需要在 Windows 客户端启用 Telnet 服务）。可以通过 telnet 命令验证（例如 telnet 192.168.1.1 445），具体各个协议及客户端要求开放端口信息如下：
<table>
	<tr><th>文件系统协议</th><th>客户端开放端口</th><th>确认网络联通性</th></tr>
	<tr><td>NFS 3.0</td><td>111，892，2049</td><td>telnet 111或者892或者2049</td></tr>
	<tr><td>NFS 4.0</td><td>2049</td><td>telnet 2049</td></tr>
	<tr><td>CIFS/SMB</td><td>445</td><td>telnet 445</td></tr>
</table>


## 步骤3：挂载文件系统

>? 建议使用 SMB 挂载 CFS。
>

### 挂载 CIFS/SMB 文件系统

挂载 CIFS/SMB 文件系统有两种方式：通过命令行挂载和通过图形界面挂载。

#### 通过命令行挂载文件系统

使用 FSID 进行挂载文件系统，挂载命令如下：
```bash
net use <共享目录名称>: \\<挂载点 IP>\FSID 
```
示例：
```bash
net use X: \\10.10.11.12\fjie120
```
>! FSID 可以到 **[文件存储控制台](https://console.cloud.tencent.com/cfs) > 文件系统详情 > 挂载点信息**中获取。
>

#### 通过图形界面挂载文件系统

1. 单击 ![](https://qcloudimg.tencent-cloud.cn/raw/87424b64a5a4e1eccc091598bc74dd80.png)，进入开始菜单界面。
2. 在**这台电脑**单击右键，选择**映射网络驱动器**。 
![](https://qcloudimg.tencent-cloud.cn/raw/4c83cd3c42e4baef67471acac5663872.png)
3. 在弹出的窗口中，设置"驱动器"盘符名称及文件夹（即在 CIFS/SMB 文件系统中看到的挂载目录），单击**完成**。
![](https://qcloudimg.tencent-cloud.cn/raw/d3367db4c535db5533f8b1a137a7ccfc.png)
4. 进入已经挂载的文件系统中，右键新建一个文件验证读写的正确性。
<img src="https://main.qcloudimg.com/raw/208537681d0ab96cd801e22332a419a9.jpeg" width="80%">


### 挂载 NFS 文件系统

#### 1. 开启 NFS 服务
>? 挂载前，需确保系统已经启动 NFS 服务。
>

1. 单击 ![](https://qcloudimg.tencent-cloud.cn/raw/87424b64a5a4e1eccc091598bc74dd80.png)，选择**控制面板 > 程序 > 启用或关闭 Windows 功能**。
2. 在打开的添加角色和功能向导窗口，保持默认配置，连续单击5次**下一步**。
3. 在**功能**界面，勾选 **NFS 客户端**，单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/097f353af729280642de8347d7ff47cf.png)
4. 单击**安装**。
5. 重启云服务器，即可完成开启 Windows NFS 客户端服务。


#### 2. 验证 NFS 服务是否启动

1. 打开 CMD 命令行工具，并执行如下命令：
```bash
mount -h
```
若返回 NFS 相关信息则表示 NFS 客户端正常运行中。
![](https://qcloudimg.tencent-cloud.cn/raw/9c11e2ab753e0ff81cba793cdd066889.png)


#### 3. 添加匿名访问用户和用户组

1. 在  ![](https://qcloudimg.tencent-cloud.cn/raw/87424b64a5a4e1eccc091598bc74dd80.png) 上单击右键，选择**运行**。
2. 在运行窗口中，输入 regedit 命令，单击**确定**，打开注册表窗口。
![](https://qcloudimg.tencent-cloud.cn/raw/56dbb35c25d52e8610321e51ab2b10cf.png)
3. 在打开的注册表中，找到并进入 `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Default` 路径。 
4. 在右边空白处单击右键，选择**新建 > DWORD(32 位)值**或者 **QWORD(64 位)值**（根据您的操作系统位数选择）。
5. 在列表中出现的新记录中，将名称设置为 **AnonymousUid**，数据值采用默认的0。
6. 重复执行**步骤4**，再添加一条新记录，并将名称设置为 **AnonymousGid**，数据采用默认的0。
![](https://qcloudimg.tencent-cloud.cn/raw/f1d86f18ccbae6664065a2d9d6bc585e.png)
7. 关闭注册表，并在 CMD 命令行工具中依次执行如下命令，重启 NFS 客户端服务，使修改的注册表生效。或者通过重启 Windows 系统，使修改的注册表生效。
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

挂载文件系统有两种方式：通过 CMD 命令行挂载和通过图形界面挂载。

#### 通过命令行挂载文件系统

在 CMD 命令行工具中，输入如下命令，挂载文件系统。其中，系统缺省子目录为 FSID。
```bash
mount  <挂载点IP>:/<FSID> <共享目录名称>:
```
示例：
```bash
mount 10.10.0.12:/z3r6k95r X:
```
>! FSID 挂载命令可以到**文件存储控制台 > 文件系统详情 > 挂载点信息**中获取。
>


#### 通过图形界面挂载文件系统

1. 单击 ![](https://qcloudimg.tencent-cloud.cn/raw/87424b64a5a4e1eccc091598bc74dd80.png)，进入开始菜单界面。
2. 在**这台电脑**单击右键，选择**映射网络驱动器**。 
![](https://qcloudimg.tencent-cloud.cn/raw/4c83cd3c42e4baef67471acac5663872.png)
3. 在弹出的窗口中，设置"驱动器"盘符名称及文件夹（即在 NFS 文件系统中看到的挂载目录），单击**完成**。
![](https://qcloudimg.tencent-cloud.cn/raw/d3367db4c535db5533f8b1a137a7ccfc.png)
4. 打开 CMD 命令行工具，输入`mount`命令，检查上述文件系统是否使用了 root 权限进行挂载。
![](https://qcloudimg.tencent-cloud.cn/raw/99f9f7193c869d5f5dc3a61c2f4cf83e.png)
UID 与 GID 分别为0，即表示文件系统使用了 root 权限挂载，此时可以开始正常使用文件系统了。若 UID 与GID 分别为 -2 等其他值，则可能导致无法正常写入数据等，请重复前面的步骤、保证文件系统是以 root 权限挂载。

 若以上界面中出现" locking=yes"，为了避免文件锁导致读写异常（NFS v3 暂不支持锁），请按以下步骤修改注册表：
 1. 找到如下注册表路径 **HKEY_LOCAL_MACHINE > SOFTWARE > Microsoft > ClientForNFS > CurrentVersion > User > Default > Mount**。
 2. 在右侧内容区右键新建 **DWORD (32 位)值**，名称为“Locking”，值为“0”。
5. 进入已经挂载的文件系统中，右键新建一个文件验证读写的正确性。
<img src="https://main.qcloudimg.com/raw/208537681d0ab96cd801e22332a419a9.jpeg" width="80%">


## 步骤4：卸载文件系统

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


## 步骤5：终止资源

>! 文件系统删除后，资源不可恢复，建议您删除文件系统之前，先备份资源。
>

您可以从腾讯云控制台终止文件系统。进入腾讯云 [文件存储控制台](https://console.cloud.tencent.com/cfs/fs)，选中需要终止的文件系统，单击**删除**并**确认**，即可删除文件系统。


