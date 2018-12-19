
## 一、创建和配置 CVM 实例
要访问文件系统，您需要将文件系统挂载在基于 Linux 或者 Windows 的腾讯云云服务器实例上。在此步骤中，您将创建和配置一个基于 Windows 的腾讯云 CVM 实例。如果您想要使用基于 Linux 的云服务器，请参考文档 [使用 CFS 创建网络文件系统（Linux）](/doc/product/582/11523)。如果已经创建 CVM 实例，请跳转至步骤二 [创建文件系统及挂载点](#1)。

登录腾讯云官网，选择【云产品】>【计算与网络】>【云服务器】，单击【立即选购】，进入 [云服务器购买页面](https://buy.cloud.tencent.com/buy/cvm)。

### 1. 选择地域与机型
![](//mc.qcloudimg.com/static/img/3ed8bab8cce3dde578a6e3fb14267ea5/image.png)
- 选择计费模式：包年包月或按量付费（无法购买按量付费云服务器的用户请先进行 [实名认证](https://console.cloud.tencent.com/developer/auth)）。更多信息请看 [计费模式说明](/doc/product/213/2180)。
- 选择地域和可用区。当您需要多台云服务器时，选择不同可用区可实现容灾效果。
- 选择机型和配置。实例类型详细说明，请参见 [实例类型概述](/doc/product/213/7153) 。

### 2. 选择镜像
![](//mc.qcloudimg.com/static/img/56c4ecbdb12dd0a366ecf701153fce1d/image.png)
- 选择镜像提供方。
腾讯云提供公共镜像、自定义镜像、共享镜像、服务市场，您可参考 [镜像类型](/doc/product/213/4941) 文档进行选择。对于刚开始使用腾讯云的用户，推荐选择公共镜像，其中包含了正版 Windows 操作系统，后续运行环境自行搭建。
- 选择操作系统：选择 Windows Server 。
- 选择系统版本。

### 3. 选择存储与网络
![](//mc.qcloudimg.com/static/img/e95a5bf7bf47c60f43dd0ee62946b67a/image.png)
- 选择硬盘类型和数据盘大小。
腾讯云提供云硬盘和本地硬盘两种类型（均默认 50GB 系统盘，系统盘大小任选）。
 - 云硬盘：采用一盘三备的分布式存储方式，数据可靠性高。
 - 本地硬盘：处在云服务器所在的物理机上的存储设备，可以获得较低的时延，但存在单点丢失风险。具体对比可以参考 [产品分类](/doc/product/362/2353) 。
- 选择网络类型。
腾讯云提供基础网络或私有网络两种可选。
 - 基础网络：适合新手用户，同一用户的云服务器内网互通。
 - 私有网络：适合更高阶的用户，不同私有网络间逻辑隔离。
- 选择公网带宽。
腾讯云提供按带宽计费或按使用流量计费两种选择。
 - 按带宽计费：选择固定带宽，超过本带宽时将丢包。适合网络波动较小的场景。
 - 按使用流量计费：按实际使用流量收费。可限制峰值带宽避免意外流量带来的费用，当瞬时带宽超过该值时将丢包。适合网络波动较大的场景。
- 选择服务器数量。
- 选择购买时长与续费方式（仅限包年包月云服务器）。

### 4. 设置信息
![](//mc.qcloudimg.com/static/img/fbc4230b5e6a19ef6ec60ffebfc62aaa/image.png)
- 命名主机：您可选择创建后命名，也可立即命名。
- 登录信息设置：您可设置密码，也可自动生成。设置的密码可在创建后修改，自动生成的密码将会以站内信方式发送。
- 选择安全组（**确保登录端口 3389 开放**，更多信息见 [安全组](/doc/product/213/5221)） 。

单击【立即购买】按钮，完成支付后即可进入 [控制台](https://console.cloud.tencent.com/cvm) 查收您的云服务器。
云服务器创建好后将会收到站内信，内容包括实例名称、公网 IP 地址、内网 IP 地址、登录名、初始登录密码等信息。您可以使用这些信息登录和管理实例。
 

<span id="1"></span>
## 二、创建文件系统及挂载点

1. 进入腾讯云 [控制台](https://console.cloud.tencent.com/)，单击【云产品】>【存储】>【文件存储】，即可进入 CFS 控制台。
![](//mc.qcloudimg.com/static/img/4fee6ea61cfba11927f6891527237610/image.png)

2. 在腾讯云 CFS 控制台，单击【新建】，弹出创建文件系统弹窗。在创建文件系统弹窗中填写相关信息，确认无误后，单击【确定】即可创建文件系统。
![](https://main.qcloudimg.com/raw/3797c04469bf0da994d2e2876a2a39ad.png)
 - 名称：您可以为创建的文件系统进行命名。
 - 地域和可用区：靠近您客户的地域可降低访问延迟，提高下载速度。
 - 文件协议：NFS（更适用于Linux、Unix客户端),CIFS/SMB（更适用于 Windows 客户端）。
 - 网络类型：腾讯云提供基础网络或私有网络两种可选。基础网络适合新手用户，同一用户的云服务器内网互通。私有网络适合更高阶的用户，不同私有网络间逻辑隔离。
  	
 > **注意：**
 > 请根据您的 CVM 实例所在网络来创建并挂载文件系统。
 > - 若您要实现私有网络（VPC）下 CVM 对文件系统的共享，您需要在创建文件系统时选择私有网络。当文件系统属于私有网络时，如果未进行特殊网络设置，则只有同一私有网络内的 CVM 实例能够挂载。
 > - 若您要实现基础网络下 CVM 对文件系统的共享，您需要在创建文件系统时选择基础网络。当文件系统属于基础网络时，如果未进行特殊网络设置，则只有同在基础网路内的 CVM 实例能够挂载。
 > - 如果有多网络共享文件系统需求，请查看 [跨可用区、跨网络访问指引](/doc/product/582/9764)。

3. 获取挂载点信息。当文件系统及挂载点创建完毕后，单击实例 ID 进入到文件系统详情，单击【挂载点信息】，获取 Windows 下的挂载命令。

NFS 文件系统挂载点信息如下:
![](https://mc.qcloudimg.com/static/img/f50435216defb4083874bc78d568001e/image.png)

CIFS/SMB 文件系统挂载点信息如下: 
![](https://main.qcloudimg.com/raw/939aafe4bca9907bc391d41e8798c4a6.png)



## 三、连接实例
本部分操作介绍登录 Windows 云服务器的常用方法，不同情况下可以使用不同的登录方式，此处介绍控制台登录，更多登录方式请见 [登录 Windows 实例](/doc/product/213/5435) 。

**前提条件**
登录到云服务器时，需要使用管理员帐号和对应的密码。
- 管理员账号：对于 Windows 类型的实例，管理员帐号统一为 Administrator。
- 密码：密码为购买云服务器时设置的密码。
   
**控制台登录云服务器**
1. 在云服务器列表的操作列，单击【登录】按钮即可通过 VNC 连接至 Windows 云服务器。
![](//mc.qcloudimg.com/static/img/d017c67c9f447c1441cf74ed4ac2b279/image.png)
2. 通过单击左上角发送【Ctrl-Alt-Delete】命令进入系统登录界面。
![](//mc.qcloudimg.com/static/img/e4dbc02ca9ae2a7cb9ada5316effd31a/image.png)
3. 输入帐号（Administrator）和密码即可登录。

>**注意：**
>该终端为独享，即同一时间只有一个用户可以使用控制台登录。


**验证网络通信**
挂载前，需要确认客户端与文件系统的网络可达性。可以通过 telnet 命令验证，具体各个协议及客户端要求开放端口信息如下：

文件系统协议 | 客户端开放端口 | 确认网络联通性
------- | ------- | ---------
NFS 3.0 | 111，892， 2049 |  telnet 111 或者 892 或者 2049
NFS 4.0 | 2049 |  telnet 2049
CIFS/SMB | 445 |  telnet 445 

注：CFS 暂不支持 ping。

## 四、挂载文件系统
### 挂载 CIFS/SMB 文件系统
#### 通过图形界面挂载文件系统
a.打开 "映射网路驱动器"
登录到需要挂载文件系统的 Windows 上，在 "开始" 菜单中找到 "计算机"，单击鼠标右键出现菜单，单击菜单中的 "映射网路驱动器"。 
![](https://main.qcloudimg.com/raw/515b5b21a19e3f3518c75441326e1800.png)
![](https://main.qcloudimg.com/raw/b0396ce0f8f108f3e89a2f2bfb3d7f71.png)

b.输入访问路径
在弹出的设置窗口中设置 "驱动器" 盘符名称及文件夹（即在 CIFS/SMB 文件系统中看到的挂载目录）。
![](https://main.qcloudimg.com/raw/8d58ee713b9e072156caf8019b4242d5.png)
![](https://main.qcloudimg.com/raw/939aafe4bca9907bc391d41e8798c4a6.png)



c.验证读写
确认后，页面直接进入到已经挂载的文件系统中。可以右键新建一个文件来验证读写的正确性。
![](https://mc.qcloudimg.com/static/img/60b9388885536ec7d81b1cf7f76c39d5/image.png)

#### 通过命令行挂载文件系统
请使用 FSID 进行挂载文件系统，挂载命令如下。
```
net use <共享目录名称>: \\10.10.11.12\FSID 
```
示例：
```
net use X: \\10.10.11.12\fjie120
```

> **注意：**
> FSID 可以到【控制台】>【文件系统详情】>【挂载点信息】中获取。
![](https://main.qcloudimg.com/raw/939aafe4bca9907bc391d41e8798c4a6.png)


### 挂载 NFS 文件系统
#### 1. 开启 NFS 服务
挂载前，请确保系统已经启动 NFS 服务。此处以 Windows Server 2012 R2 为示例，开启 NFS 服务。
1.1 打开【控制面板】>【程序】>【打开或关闭 Windows 功能】>【服务器角色】页签中勾选【NFS server】。
![](https://mc.qcloudimg.com/static/img/eaeed922e9d1f673e47137d80a88fa70/image.png)
1.2 打开【控制面板】>【程序】>【打开或关闭 Windows 功能】>【特性】页签中勾选【NFS 客户端】，勾选【NFS 客户端】即可开启 Windows NFS 客户端服务。
![](https://mc.qcloudimg.com/static/img/4f9d7ac7b877ceffc5bc2b1d7c050a24/image.png)

#### 2. 验证 NFS 服务是否启动
打开 Windows 下的命令行工具，在面板中执行如下命令，若返回 NFS 相关信息则表示 NFS 客户端正常运行中。
```
mount -h
```
![](https://mc.qcloudimg.com/static/img/4e4f9db217874ccec91ac1f888c8e451/image.png)

#### 3. 添加匿名访问用户和用户组
3.1 打开注册表
在命令行窗口输入 regedit 命令，回车即可打开注册表窗口。
![](https://mc.qcloudimg.com/static/img/c9fca9a1b123a5b2dbc69b0ce66d539f/image.png)

3.2 添加配置项 AnonymousUid 和 AnonymousGid
在打开的注册表中找到如下路径并选中。 
```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Default
```
在右边空白处右键单击，弹出【new】, 在菜单中选择【DWORD(32-bit) Value】 或者【QWORD(64-bit) Value】（根据您的操作系统位数选择）。此时，在列表中会出现一条新的记录，把名称栏修改为 AnonymousUid 即可，数据值采用默认的 0。使用同样方法继续添加一条名称为 AnonymousGid 的记录，数据也采用默认的 0。
![](https://mc.qcloudimg.com/static/img/381cdc3b68fb35be5dcceb2a4c962e33/image.png)
![](https://mc.qcloudimg.com/static/img/80bb0cfbffbed939522459a830df3eac/image.png)

3.3 重启使配置生效
关闭注册表并重启 Windows 系统，完成注册表修改。

#### 4. 挂载文件系统
挂载文件系统有两种方式：通过图形界面挂载和通过 CMD 命令行挂载。
1）通过图形界面挂载
a. 打开 "映射网路驱动器"
登录到需要挂载文件系统的 Windows 上，在 "开始" 菜单中找到 "计算机"，单击鼠标右键出现菜单，单击菜单中的 "映射网路驱动器"。 
![](https://main.qcloudimg.com/raw/515b5b21a19e3f3518c75441326e1800.png)
![](https://main.qcloudimg.com/raw/b0396ce0f8f108f3e89a2f2bfb3d7f71.png)
b. 输入访问路径
在弹出的设置窗口中设置 "驱动器" 盘符名称及文件夹（即在 NFS 文件系统中看到的挂载目录）。
![](https://main.qcloudimg.com/raw/8d58ee713b9e072156caf8019b4242d5.png)
![](https://mc.qcloudimg.com/static/img/caa18888e6da73b19de8eefc18ff3680/image.png)
c. 验证读写
确认后，页面直接进入到已经挂载的文件系统中。可以右键新建一个文件来验证读写的正确性。
![](https://mc.qcloudimg.com/static/img/60b9388885536ec7d81b1cf7f76c39d5/image.png)

2）通过 CMD 命令行挂载
在 Windows 的命令行工具中输入如下命令，挂载文件系统。其中，系统缺省子目录为 FSID。

```
mount  <挂载点IP>:/<FSID> <共享目录名称>:
```

示例：
```
mount 10.10.0.12:/z3r6k95r X:
```

> **注意：**
> FSID 挂载命令可以到【文件存储控制台】>【文件系统详情】>【挂载点信息】中获取。

### 5.卸载文件系统
#### 通过图形界面卸载共享目录
要断开已经挂载的文件系统，只需鼠标右键单击磁盘，再出现的菜单中单击【断开】选项，即可断开文件系统的连接。
![](https://mc.qcloudimg.com/static/img/376cd0547aa64f4d519e5444c5a58f93/image.png)

#### 通过 CMD 命令卸载 NFS 共享目录 

当某些情况下需要卸载共享目录，请使用如下命令。其中 "目录名称" 为根目录或者文件系统的完整路径。
```
umount <目录名称>：
```
示例：
```
umount X：
```


## 五、终止资源
您可以从腾讯云控制台轻松终止 CVM 实例和文件系统。事实上，最好终止不再使用的资源，以免继续为其付费。
1. 终止腾讯云实例。进入腾讯云云服务器 [控制台](https://console.cloud.tencent.com/cvm/index)，选中需要终止的实例，单击【更多】>【云主机状态】，可以选中【销毁】以终止 CVM 实例。
![](//mc.qcloudimg.com/static/img/76c588284e3b525702d748b5cd7b8b00/image.png)
2. 终止文件系统。进入腾讯云文件存储 [控制台](https://console.cloud.tencent.com/cfs)，选中需要终止的文件系统，单击【删除】并【确认】，即可删除文件系统。
![](//mc.qcloudimg.com/static/img/28cade4807a283ffdcb1fc2a39a7ad88/image.png)
