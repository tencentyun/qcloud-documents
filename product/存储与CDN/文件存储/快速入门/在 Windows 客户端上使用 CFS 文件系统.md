## 简介

本文为您详细介绍如何在 Windows 客户端上使用 CFS 文件系统。本指引以 Windows Server 2012 R2 为示例截图，其他版本操作系统，例如 Windows Server 2008 及 Windows Server 2016 操作方法相同。

## 操作步骤

使用 CFS 文件系统操作流程：“[创建文件系统及挂载点](#.E5.88.9B.E5.BB.BA.E6.96.87.E4.BB.B6.E7.B3.BB.E7.BB.9F.E5.8F.8A.E6.8C.82.E8.BD.BD.E7.82.B9)” > “[连接实例](#.E8.BF.9E.E6.8E.A5.E5.AE.9E.E4.BE.8B)” > “[挂载文件系统](#.E6.8C.82.E8.BD.BD.E6.96.87.E4.BB.B6.E7.B3.BB.E7.BB.9F)” > “[卸载共享文件系统](#.E5.8D.B8.E8.BD.BD.E6.96.87.E4.BB.B6.E7.B3.BB.E7.BB.9F)” > “[终止资源](#.E7.BB.88.E6.AD.A2.E8.B5.84.E6.BA.90)”。详细操作步骤请阅读本文以下章节。

### 创建文件系统及挂载点

#### 1. 进入文件系统界面

登录文件存储 [CFS 控制台](https://console.cloud.tencent.com/cfs)，在左侧导航栏单击【文件系统】，进入文件系统列表页。

#### 2. 创建文件系统及挂载点

单击【新建】，弹出创建文件系统弹窗，在弹窗中配置如下信息，操作无误后，单击【确定】即可创建文件系统及挂载点。

<table>
  <tr>
    <th>字段</th>
    <th>含义</th>
  </tr>
  <tr>
    <td>地域</td>
    <td>选择所需要创建 CFS 文件系统的地域</td>
  </tr>
  <tr>
    <td>可用区</td>
    <td>选择所需要创建 CFS 文件系统的可用区</td>
  </tr>
  <tr>
    <td>文件服务协议</td>
    <td>选择文件系统的协议类型，NFS 或 CIFS/SMB 。其中，NFS 协议更适合于 Linux/Unix 客户端，CIFS/SMB 协议更适合于 Windows 客户端（CIFS/SMB 协议近期公测已结束，后续开放时间敬待通知，更多信息请参见 <a href="https://cloud.tencent.com/document/product/582/9553#cifs.2Fsmb-.E5.85.AC.E6.B5.8B.E8.AF.B4.E6.98.8E">CIFS/SMB 公测说明</a>）。</td>
  </tr>
  <tr>
    <td>客户端类型</td>
    <td>选择需要访问 CFS 文件系统的客户端类型，云服务器（含容器、批量计算）或黑石服务器。 因为云服务器和黑石主机分别属于不同的网络，系统会根据您的客户端类型分配该文件系统到指定网络中。</td>
  </tr>
  <tr>
    <td>网络类型</td>
    <td> 
    <p>私有网络（VPC）或者是基础网络。请根据您的 CVM 实例所在网络来创建并挂载文件系统，否则可能因为网络不通导致无法访问。</p>
    <li>若您要实现私有网络（VPC） 下 CVM 对文件系统的共享，您需要在创建文件系统时选择私有网络。当文件系统属于私有网络时，如果未进行特殊网络设置，则只有同一私有网络内的 CVM 实例能够挂载。</p>
    <li>若您要实现基础网络下 CVM 对文件系统的共享，您需要在创建文件系统时选择基础网络。当文件系统属于基础网络时，如果未进行特殊网络设置，则只有同在基础网络内的 CVM 实例能够挂载。</p>
    <li>如果有多网络共享文件系统需求，请查见 <a href="https://cloud.tencent.com/document/product/582/9764">跨网络访问文件系统</a> 文档</p>
    </td>
  </tr>  
  <tr>
    <td>权限组</td>
    <td>每个文件系统必须绑定一个权限组，权限组规定了一组可来访白名单及读、写操作权限。
    </td>
  </tr>
</table>

#### 3. 获取挂载点信息

获取挂载点信息。当文件系统及挂载点创建完毕后，单击实例 ID 进入到文件系统详情，单击【挂载点信息】，获取 Windows 客户端上使用文件系统的挂载命令。请按照推荐的挂载命令执行挂载操作。
**数量**指挂载源数量，即可以挂载的方式数量，目前只支持通过 IP 挂载，故该值为1。


### 连接实例

本部分操作介绍登录 Windows 云服务器的常用方法，不同情况下可以使用不同的登录方式，此处介绍控制台登录，更多登录方式请见 [登录 Windows 实例](/doc/product/213/5435) 。

#### 前提条件

登录到云服务器时，需要使用管理员帐号和对应的密码。

- 管理员账号：对于 Windows 类型的实例，管理员帐号统一为 Administrator。
- 密码：密码为购买云服务器时设置的密码。

#### 控制台登录云服务器

1. 在云服务器列表的操作列，单击【登录】即可通过 VNC 连接至 Windows 云服务器。
2. 通过单击左上角发送【Ctrl-Alt-Delete】命令进入系统登录界面。
3. 输入帐号（Administrator）和密码即可登录。

> !该终端为独享，即同一时间只有一个用户可以使用控制台登录。

#### 验证网络通信

挂载前，需要确认客户端与文件系统的网络可达性（需要在 Windows 客户端启用 Telnet服务）。可以通过 telnet 命令验证，具体各个协议及客户端要求开放端口信息如下：

| 文件系统协议 | 客户端开放端口 | 确认网络联通性            |
| ------------ | -------------- | ------------------------- |
| NFS 3.0      | 111，892，2049 | telnet 111或者892或者2049 |
| NFS 4.0      | 2049           | telnet 2049               |
| CIFS/SMB     | 445            | telnet 445                |

> !CFS 暂不支持 ping。

### 挂载文件系统

#### 挂载 NFS 文件系统

#### 1. 开启 NFS 服务

挂载前，请确保系统已经启动 NFS 服务。
1.1 选择【控制面板】>【程序】>【打开或关闭 Windows 功能】>【服务器角色】页签中勾选【NFS server】。
![](https://mc.qcloudimg.com/static/img/eaeed922e9d1f673e47137d80a88fa70/image.png)
1.2 选择【控制面板】>【程序】>【打开或关闭 Windows 功能】>【特性】页签中勾选【NFS 客户端】，勾选【NFS 客户端】即可开启 Windows NFS 客户端服务。
![](https://mc.qcloudimg.com/static/img/4f9d7ac7b877ceffc5bc2b1d7c050a24/image.png)

#### 2. 验证 NFS 服务是否启动

打开 Windows 下的命令行工具，在面板中执行如下命令，若返回 NFS 相关信息则表示 NFS 客户端正常运行中。
```bash
mount -h
```
![](https://mc.qcloudimg.com/static/img/4e4f9db217874ccec91ac1f888c8e451/image.png)

#### 3. 添加匿名访问用户和用户组

3.1 打开注册表
在命令行窗口输入 regedit 命令，回车即可打开注册表窗口。
![](https://mc.qcloudimg.com/static/img/c9fca9a1b123a5b2dbc69b0ce66d539f/image.png)

3.2 添加配置项 AnonymousUid 和 AnonymousGid
在打开的注册表中找到如下路径并选中。 
```bash
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Default
```

在右边空白处右键单击，弹出【new】, 在菜单中选择【DWORD(32-bit) Value】 或者【QWORD(64-bit) Value】（根据您的操作系统位数选择）。此时，在列表中会出现一条新的记录，把名称栏修改为 AnonymousUid 即可，数据值采用默认的0。使用同样方法继续添加一条名称为 AnonymousGid 的记录，数据也采用默认的0。
![](https://mc.qcloudimg.com/static/img/381cdc3b68fb35be5dcceb2a4c962e33/image.png)

添加完毕如下图所示：
![](https://main.qcloudimg.com/raw/9af3f35d4b78a2e17cf2ef44fa6863d7.png)

3.3 重启使配置生效
关闭注册表并重启 Windows 系统，完成注册表修改。

#### 4. 挂载文件系统

挂载文件系统有两种方式：通过图形界面挂载和通过 CMD 命令行挂载。

- 通过图形界面挂载
  a. 打开 "映射网络驱动器"
  登录到需要挂载文件系统的 Windows 上，在 "开始" 菜单中找到 "计算机"，单击鼠标右键出现菜单，单击菜单中的 "映射网络驱动器"。 
  ![](https://main.qcloudimg.com/raw/515b5b21a19e3f3518c75441326e1800.png)
  ![](https://main.qcloudimg.com/raw/b0396ce0f8f108f3e89a2f2bfb3d7f71.png)
  b. 输入访问路径
  在弹出的设置窗口中设置 "驱动器" 盘符名称及文件夹（即在 NFS 文件系统中看到的挂载目录）。
  ![](https://main.qcloudimg.com/raw/8d58ee713b9e072156caf8019b4242d5.png)
  ![](https://mc.qcloudimg.com/static/img/caa18888e6da73b19de8eefc18ff3680/image.png)
  c. 验证读写
  确认后，页面直接进入到已经挂载的文件系统中。可以右键新建一个文件来验证读写的正确性。
  ![](https://mc.qcloudimg.com/static/img/60b9388885536ec7d81b1cf7f76c39d5/image.png)
- 通过 CMD 命令行挂载
  在 Windows 的命令行工具中输入如下命令，挂载文件系统。其中，系统缺省子目录为 FSID。
```bash
mount  <挂载点IP>:/<FSID> <共享目录名称>:
```
示例：
```bash
mount 10.10.0.12:/z3r6k95r X:
```
> ! FSID 挂载命令可以到【文件存储控制台】>【文件系统详情】>【挂载点信息】中获取。

#### 挂载 CIFS/SMB 文件系统

挂载 CIFS/SMB 文件系统有两种方式：通过图形界面挂载和通过命令行挂载。

#### 通过图形界面挂载文件系统

> !CIFS/SMB 协议文件系统公测中，更多信息请参阅 [CIFS/SMB公测说明](https://cloud.tencent.com/document/product/582/9553#cifs.2Fsmb-.E5.85.AC.E6.B5.8B.E8.AF.B4.E6.98.8E)。

1. 打开 "映射网络驱动器"
   登录到需要挂载文件系统的 Windows 上，在 "开始" 菜单中找到 "计算机"，单击鼠标右键出现菜单，单击菜单中的 "映射网络驱动器"。 
   ![](https://main.qcloudimg.com/raw/515b5b21a19e3f3518c75441326e1800.png)
   ![](https://main.qcloudimg.com/raw/b0396ce0f8f108f3e89a2f2bfb3d7f71.png)
2. 输入访问路径
   在弹出的设置窗口中设置 "驱动器" 盘符名称及文件夹（即在 CIFS/SMB 文件系统中看到的挂载目录）。
   ![](https://main.qcloudimg.com/raw/8d58ee713b9e072156caf8019b4242d5.png)
   ![](https://main.qcloudimg.com/raw/939aafe4bca9907bc391d41e8798c4a6.png)
3. 验证读写
   确认后，页面直接进入到已经挂载的文件系统中。可以右键新建一个文件来验证读写的正确性。
   ![](https://mc.qcloudimg.com/static/img/60b9388885536ec7d81b1cf7f76c39d5/image.png)

#### 通过命令行挂载文件系统
请使用 FSID 进行挂载文件系统，挂载命令如下。
```bash
net use <共享目录名称>: \\10.10.11.12\FSID 
```

示例：
```bash
net use X: \\10.10.11.12\fjie120
```

> ! FSID 可以到【控制台】>【文件系统详情】>【挂载点信息】中获取。
> ![](https://main.qcloudimg.com/raw/939aafe4bca9907bc391d41e8798c4a6.png)



### 卸载文件系统
#### 通过图形界面卸载共享目录

要断开已经挂载的文件系统，只需鼠标右键单击磁盘，再出现的菜单中单击【断开】选项，即可断开文件系统的连接。
![](https://mc.qcloudimg.com/static/img/376cd0547aa64f4d519e5444c5a58f93/image.png)

#### 通过 CMD 命令卸载 NFS 共享目录 

当某些情况下需要卸载共享目录，请打开命令行终端后使用如下命令。其中 "目录名称" 为根目录或者文件系统的完整路径。
```bash
umount <目录名称>：
```

示例：
```bash
umount X：
```

### 终止资源

您可以从腾讯云控制台终止文件系统。进入腾讯云文件存储 [控制台](https://console.cloud.tencent.com/cfs)，选中需要终止的文件系统，单击【删除】并【确认】，即可删除文件系统。
