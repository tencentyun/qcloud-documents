
## 1. 创建和配置 CVM 实例
要访问文件系统，您需要将文件系统挂载在基于 Linux 或者 Windows 的腾讯云云服务器实例上。在此步骤中，您将创建和配置一个腾讯云 CVM 实例。如果已经创建 CVM 实例，请跳转至步骤 2 创建文件系统及挂载点。

### 1.1 Linux 云服务器
本步骤引导新手快速了解腾讯云 Linux 云服务器的创建和配置。如果需要使用 Windows 系统的云服务器，请参考步骤 1.2 Windows 云服务器。
登录腾讯云官网，选择【云产品】-【计算与网络】-【云服务器】，单击【立即选购】，进入 [云服务器购买页面](https://buy.qcloud.com/buy/cvm)。
#### 1.1.1 选择地域与机型
![](//mc.qcloudimg.com/static/img/3ed8bab8cce3dde578a6e3fb14267ea5/image.png)
- 选择计费模式。包年包月或按量付费（无法购买按量付费云服务器的用户请先进行  [实名认证](https://console.qcloud.com/developer/infomation)）。更多信息请看 [计费模式说明](http://www.qcloud.com/doc/product/213/%E8%AE%A1%E8%B4%B9%E6%A8%A1%E5%BC%8F%E8%AF%B4%E6%98%8E) 。
- 选择地域和可用区。当您需要多台云服务器时，选择不同可用区可实现容灾效果。
- 选择机型和配置。实例类型详细说明，请参见 [实例类型概述](https://www.qcloud.com/document/product/213/7153) 。

#### 1.1.2 选择镜像
![](//mc.qcloudimg.com/static/img/fd40922e47525453a58de73d0ffa266c/image.png)
- 选择镜像提供方。腾讯云提供公共镜像、自定义镜像、共享镜像、服务市场，您可参考 [镜像类型](https://www.qcloud.com/document/product/213/4941) 进行选择。对于刚开始使用腾讯云的用户，推荐选择公共镜像。
- 选择操作系统。腾讯云提供了 CentOS、 CoreOS、 Debian、 FreeBSD、 OpenSUSE、 SUSE、 Ubuntu 等操作系统，后续运行环境请您自行搭建。
- 选择系统版本。 

#### 1.1.3 选择存储与网络
![](//mc.qcloudimg.com/static/img/e95a5bf7bf47c60f43dd0ee62946b67a/image.png)
- 选择硬盘类型和数据盘大小。
腾讯云提供云硬盘和本地硬盘两种类型。（均默认 50GB 系统盘，系统盘大小任选）
  - 云硬盘：采用一盘三备的分布式存储方式，数据可靠性高
  - 本地硬盘：处在云服务器所在的物理机上的存储设备，可以获得较低的时延，但存在单点丢失风险。具体对比可以参考 [产品分类](https://www.qcloud.com/document/product/362/2353#.E5.90.84.E7.A7.8D.E5.9D.97.E5.AD.98.E5.82.A8.E8.AE.BE.E5.A4.87.E7.9A.84.E5.AF.B9.E6.AF.94) 。
- 选择网络类型。
腾讯云提供基础网络或私有网络两种可选。
 - 基础网络：适合新手用户，同一用户的云服务器内网互通。
 - 私有网络：适合更高阶的用户，不同私有网络间逻辑隔离。
- 选择公网带宽。
腾讯云提供按带宽计费或按使用流量计费两种可选。
 - 按带宽计费：选择固定带宽，超过本带宽时将丢包。适合网络波动较小的场景。
 - 按使用流量计费：按实际使用流量收费。可限制峰值带宽避免意外流量带来的费用，当瞬时带宽超过该值时将丢包。适合网络波动较大的场景。
- 选择服务器数量。
- 选择购买时长与续费方式（仅限包年包月云服务器）。

#### 1.1.4 设置信息
![](//mc.qcloudimg.com/static/img/1c463db6e3b31abd6c1d3163f1c3108f/image.png)
- 命名主机：您可选择创建后命名，也可立即命名。
- 登录信息设置：
 - 设置密码：输入主机密码设置。
 - 立即关联密钥：关联 SSH 密钥。如您没有密钥或现有的密钥不合适，可以单击【现在创建】按钮创建，参考 [创建密钥](http://www.qcloud.com/doc/product/213/%E5%AF%86%E9%92%A5%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97#1.-创建密钥) 指南。更多 SSH 密钥请见 [SSH密钥](http://www.qcloud.com/doc/product/213/SSH%E5%AF%86%E9%92%A5) 。
 - 自动生成密码：自动生成的密码将会以站内信方式发送。
- 选择安全组（**确保登录端口 22 开放**，更多信息见 [安全组](http://www.qcloud.com/doc/product/213/%E5%AE%89%E5%85%A8%E7%BB%84)） 。

单击【立即购买】按钮，完成支付后即可进入 [控制台](https://console.qcloud.com/cvm) 查收您的云服务器。
云服务器创建好后将会收到站内信，内容包括实例名称、公网 IP 地址、内网 IP 地址、登录名、初始登录密码等信息。您可以使用这些信息登录和管理实例，也请尽快更改您的 Linux 登录密码保障主机安全性。
 
### 1.2 Windows 云服务器
本步骤引导新手快速了解腾讯云 Windows 云服务器的创建和配置。如果需要使用 Linux 系统的云服务器，请参考步骤 1.1 Linux 云服务器。
登录腾讯云官网，选择【云产品】-【计算与网络】-【云服务器】，单击【立即选购】按钮，进入 [云服务器购买页面](https://buy.qcloud.com/buy/cvm) 。

#### 1.2.1 选择地域与机型
![](//mc.qcloudimg.com/static/img/3ed8bab8cce3dde578a6e3fb14267ea5/image.png)
- 选择计费模式：包年包月或按量付费（无法购买按量付费云服务器的用户请先进行 [实名认证](https://console.qcloud.com/developer/infomation) ）。更多信息请看 [计费模式说明](http://www.qcloud.com/doc/product/213/%E8%AE%A1%E8%B4%B9%E6%A8%A1%E5%BC%8F%E8%AF%B4%E6%98%8E) 。
- 选择地域和可用区。当您需要多台云服务器时，选择不同可用区可实现容灾效果。
- 选择机型和配置。实例类型详细说明，请参见 [实例类型概述](https://www.qcloud.com/document/product/213/7153) 。

#### 1.2.2 选择镜像
![](//mc.qcloudimg.com/static/img/56c4ecbdb12dd0a366ecf701153fce1d/image.png)
- 选择镜像提供方。
腾讯云提供公共镜像、自定义镜像、共享镜像、服务市场，您可参考 [镜像类型](https://www.qcloud.com/document/product/213/4941) 文档进行选择。对于刚开始使用腾讯云的用户，推荐选择公共镜像，其中包含了正版 Windows 操作系统，后续运行环境自行搭建。
- 选择操作系统：选择 Windows Server 。
- 选择系统版本。

#### 1.2.3 选择存储与网络
![](//mc.qcloudimg.com/static/img/e95a5bf7bf47c60f43dd0ee62946b67a/image.png)
- 选择硬盘类型和数据盘大小。腾讯云提供云硬盘和本地硬盘两种类型。（均默认 50GB 系统盘，系统盘大小任选）
 - 云硬盘：采用一盘三备的分布式存储方式，数据可靠性高
 - 本地硬盘：处在云服务器所在的物理机上的存储设备，可以获得较低的时延，但存在单点丢失风险。具体对比可以参考 [产品分类](https://www.qcloud.com/document/product/362/2353#.E5.90.84.E7.A7.8D.E5.9D.97.E5.AD.98.E5.82.A8.E8.AE.BE.E5.A4.87.E7.9A.84.E5.AF.B9.E6.AF.94) 。
- 选择网络类型。腾讯云提供基础网络或私有网络两种可选。
 - 基础网络：适合新手用户，同一用户的云服务器内网互通。
 - 私有网络：适合更高阶的用户，不同私有网络间逻辑隔离。
- 选择公网带宽。腾讯云提供按带宽计费或按使用流量计费两种选择。
 - 按带宽计费：选择固定带宽，超过本带宽时将丢包。适合网络波动较小的场景。
 - 按使用流量计费：按实际使用流量收费。可限制峰值带宽避免意外流量带来的费用，当瞬时带宽超过该值时将丢包。适合网络波动较大的场景。
- 选择服务器数量。
- 选择购买时长与续费方式（仅限包年包月云服务器）。

#### 1.2.4 设置信息
![](//mc.qcloudimg.com/static/img/fbc4230b5e6a19ef6ec60ffebfc62aaa/image.png)
- 命名主机：您可选择创建后命名，也可立即命名。
- 登录信息设置：您可设置密码，也可自动生成。设置的密码可在创建后修改，自动生成的密码将会以站内信方式发送。
- 选择安全组（**确保登录端口 3389 开放**，更多信息见 [安全组](http://www.qcloud.com/doc/product/213/%E5%AE%89%E5%85%A8%E7%BB%84)） 。

单击【立即购买】按钮，完成支付后即可进入 [控制台](https://console.qcloud.com/cvm) 查收您的云服务器。云服务器创建好后将会收到站内信，内容包括实例名称、公网 IP 地址、内网 IP 地址、登录名、初始登录密码等信息。您可以使用这些信息登录和管理实例，也请尽快更改您的 Windows 登录密码保障主机安全性。

## 2. 创建文件系统及挂载点
2.1 进入腾讯云 [控制台](https://console.cloud.tencent.com/)，单击【云产品】->【存储】->【文件存储】，即可进入 CFS 控制台。
![](//mc.qcloudimg.com/static/img/2985f36369578c2f0662735748532620/image.png)

2.2 在腾讯云 CFS 控制台，单击【新建】，弹出创建文件系统弹窗。在创建文件系统弹窗中填写相关信息，确认无误后，单击【确定】即可创建文件系统。
![](//mc.qcloudimg.com/static/img/8702bd75495c4f372a33f02bbaa865ff/image.png)

> **注意：**
> 请根据您的 CVM 实例所在网络来创建并挂载文件系统。
> - 若您要实现私有网络（VPC） 下 CVM 对文件系统的共享，您需要在创建文件系统时选择私有网络。当文件系统属于私有网络时，如果未进行特殊网络设置，则只有同一私有网络内的 CVM 实例能够挂载。
> - 若您要实现基础网络下 CVM 对文件系统的共享，您需要在创建文件系统时选择基础网络。当文件系统属于基础网络时，如果未进行特殊网络设置，则只有同在基础网路内的 CVM 实例能够挂载。
> - 如果有多网络共享文件系统需求，请查看[跨可用区、跨网络访问指引](https://www.qcloud.com/document/product/582/9764)

2.3 获取挂载点信息。当文件系统及挂载点创建完毕后，单击实例 ID 进入到文件系统详情，单击【挂载点信息】，获取 Linux 下的挂载命令及 Windows 下的挂载命令。
![](//mc.qcloudimg.com/static/img/1009d4e7eb33ca89eda92f3beba6fb4b/image.png)

## 3. 连接实例
### 3.1 登录 Linux 云服务器
本部分操作介绍登录 Linux 云服务器的常用方法，不同情况下可以使用不同的登录方式，此处介绍控制台登录，更多登录方式请见   [登录 Linux 实例](/doc/product/213/5436) 。

**前提条件**
登录到云服务器时，需要使用管理员帐号和对应的密码。
 - 管理员账号：对于 Linux 类型的实例，管理员帐号统一为 root （ Ubuntu 系统用户为 ubuntu ）
 - 密码：快速配置中，初始密码由系统随机分配。在下一环节（查看站内信及云服务器信息）中，具体查看操作。更多内容请参考 [登录密码](/doc/product/213/6093) 。
   
**查看站内信及云服务器信息**
完成云服务器的购买和创建后，云服务器的实例名称、公网 IP 地址、内网 IP 地址、登录名、初始登录密码等信息都将以 [站内信](https://console.qcloud.com/message) 的方式发送到账户上。
- 登录 [云服务器控制台](https://console.qcloud.com/cvm) 。登录后即可看到公网 IP 地址、内网 IP 地址等信息。
- 单击右上角【站内信】。
- 站内信页面即可查看新创建的云服务器，及登录名与密码等信息。
![](//mc.qcloudimg.com/static/img/d2d6900e58fc4f7b141b770de23cd3d8/image.png)

**控制台登录云服务器**
- 在云服务器列表的操作列，单击【登录】按钮即可通过VNC连接至 Linux 云服务器：
![](//mccdn.qcloud.com/img56b1a6cb7b3e8.png)
- 输入帐号（root ，Ubuntu 系统用户为 ubuntu）和站内信中的初始密码（或您修改后的密码）即可登录。

>**注意：**
>该终端为独享，即同一时间只有一个用户可以使用控制台登录。

### 3.2 登录 Windows 云服务器
本部分操作介绍登录 Windows 云服务器的常用方法，不同情况下可以使用不同的登录方式，此处介绍控制台登录，更多登录方式请见   [登录 Windows 实例](/doc/product/213/5435) 。

**前提条件**
登录到云服务器时，需要使用管理员帐号和对应的密码。
- 管理员账号：对于 Windows 类型的实例，管理员帐号统一为 Administrator
- 密码：快速配置中，初始密码由系统随机分配。在下一环节（查看站内信及云服务器信息）中，具体查看操作。更多内容请参考 [登录密码](/doc/product/213/6093) 。
   
**查看站内信及云服务器信息**
完成云服务器的购买和创建后，云服务器的实例名称、公网 IP 地址、内网 IP 地址、登录名、初始登录密码等信息都将以 [站内信](https://console.qcloud.com/message) 的方式发送到账户上。
- 登录 [云服务器控制台](https://console.qcloud.com/cvm) 。登录后即可看到公网 IP 地址、内网 IP 地址等信息。
- 单击右上角【站内信】。
- 站内信页面即可查看新创建的云服务器，及登录名与密码等信息。
![](//mc.qcloudimg.com/static/img/1385695211763c620c31d603136c3128/image.png)

**控制台登录云服务器**
- 在云服务器列表的操作列，单击【登录】按钮即可通过 VNC 连接至 Windows 云服务器：
![](//mccdn.qcloud.com/img56b1a6cb7b3e8.png)
- 通过单击左上角发送 Ctrl-Alt-Delete 命令进入系统登录界面：
![](//mc.qcloudimg.com/static/img/e4dbc02ca9ae2a7cb9ada5316effd31a/image.png)
- 输入帐号（Administrator）和站内信中的初始密码（或您修改后的密码）即可登录。

>**注意：**
>该终端为独享，即同一时间只有一个用户可以使用控制台登录。

## 4. 挂载文件系统

### 4.1 Linux 操作系统
#### 4.1.1 启动 NFS 客户端
挂载前，请确保系统中已经安装了`nfs-utils`或`nfs-common`,安装方法如下：
> - CentOS：
>  `sudo yum install nfs-utils`
> - Ubuntu 或 Debian
> `sudo apt-get install nfs-common`

#### 4.1.2 NFS 挂载
**NFS v4.0 挂载**
使用下列命令实现 NFS v4.0 挂载。
`sudo mount -t nfs4 <挂载点IP>:/ <待挂载目标目录>`
- 挂载点IP：指创建文件系统时，自动的生成的挂载点 IP。
- 目前默认挂载的是文件系统的根目录 "/"。 在文件系统中创建子目录后，可以挂载该子目录。
- 待挂载目标目录： 在当前服务器上，需要挂载的目标目录，需要用户事先创建。

> **注意：**
> `<挂载点IP>:/`与`<待挂载目标目录>`之间有一个空格。

示例：
- 挂载 CFS 根目录：
`mount -t nfs4 10.0.0.1:/ /local/test`。
- 挂载 CFS 子目录 subfolder：
`mount -t nfs4 10.10.19.12:/subfolder /local/test`

![](https://mc.qcloudimg.com/static/img/4ce4a81c90b9ecdc19a4396720a46330/image.png)

**NFS v3.0 挂载**
使用下列命令实现 NFS v3.0 挂载。
`sudo mount -t nfs -o vers=3,nolock,proto=tcp <挂载点IP>:/ <待挂载目标目录>`
- 挂载点IP：指创建文件系统时，自动的生成的挂载点 IP。
- NFS v3.0 仅支持子目录挂载，缺省文件系统子目录为 FSID 或者 "nfs" 。
- 待挂载目标目录： 在当前服务器上，需要挂载的目标目录，需要用户事先创建。
示例

> **注意：**
> `<挂载点IP>:/`与`<待挂载目标目录>`之间有一个空格。

示例：
- 挂载 CFS 子目录 subfolder：
`mount -t nfs -o vers=3,nolock,proto=tcp 10.10.19.12:/z3r6k95r /local/test`
- 挂载 CFS 子目录 subfolder：
`mount -t nfs -o vers=3,nolock,proto=tcp 10.10.19.12:/nfs /local/test`

![](https://mc.qcloudimg.com/static/img/4ce4a81c90b9ecdc19a4396720a46330/image.png)

#### 4.1.3 查看挂载点信息
挂载完成后，请使用如下命令查看已挂载的文件系统：
`mount -l`
也可以使用如下命令查看该文件系统的容量信息：
`df -h`

#### 4.1.4 卸载共享目录
当某些情况下需要卸载共享目录，请使用如下命令。其中 "目录名称" 为根目录或者文件系统的完整路径。
`umount <目录名称>`
示例： 
`umount /local/test`

### 4.2 Windows 操作系统
#### 4.2.1 开启 NFS 服务
挂载前，请确保系统已经启动 NFS 服务。此处以 Windows Server 2012 R2 为示例，开启 NFS 服务。
打开控制面板 -> 程序 -> 打开或关闭 windows 功能 -> 【服务器角色】页签中勾选 "NFS server" -> 【特性】中勾选 "NFS 客户端"，勾选 NFS 客户端即可开启 windows NFS 客户端服务。
![](https://mc.qcloudimg.com/static/img/eaeed922e9d1f673e47137d80a88fa70/image.png)
![](https://mc.qcloudimg.com/static/img/4f9d7ac7b877ceffc5bc2b1d7c050a24/image.png)

#### 4.2.2 验证 NFS 服务是否启动
打开 windows 下的命令行工具，在面板中执行如下命令，若返回 NFS 相关信息则表示 NFS 客户端正常运行中。
`mount -h`

![](https://mc.qcloudimg.com/static/img/4e4f9db217874ccec91ac1f888c8e451/image.png)

#### 4.2.3 添加匿名访问用户和用户组
**打开注册表**
在命令行窗口输入 regedit命令，回车即可打开注册表窗口。
![](https://mc.qcloudimg.com/static/img/c9fca9a1b123a5b2dbc69b0ce66d539f/image.png)

**添加配置项 AnonymousUid 和 AnonymousGid**
在打开的注册表中找到如下路径并选中 
> HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Default

在右边空白处右键点击，弹出 "new", 在菜单中选择 "DWORD(32-bit) Value" 或者 "QWORD(64-bit) Value"（根据您的操作系统位数选择）。此时，在列表中会出现一条新的记录，把名称栏修改为 AnonymousUid 即可，数据值采用默认的 0。使用同样方法继续添加一条名称为 AnonymousGid 的记录，数据也采用默认的0。
![](https://mc.qcloudimg.com/static/img/381cdc3b68fb35be5dcceb2a4c962e33/image.png)
![](https://mc.qcloudimg.com/static/img/80bb0cfbffbed939522459a830df3eac/image.png)

**重启使配置生效**
关闭注册表并重启 windows 系统，完成注册表修改。

#### 4.2.4 挂载文件系统
在 windows 的命令行工具中输入如下命令，挂载文件系统。其中，系统缺省子目录为 "nfs"。
`mount  <挂载点IP>:/<子目录> <共享目录名称>:`
示例：
`mount 10.10.0.12:/nfs X:`

若使用上述命令挂载，出现文件夹无法重命名的情况，请使用 FSID 进行挂载，挂载命令如下。
`mount <挂载点IP>:/FSID <共享目录名称>:`
示例：
`mount 10.10.0.12:/z3r6k95r X:`

> **注意：**
> FSID 可以到 "控制台->文件系统详情->挂载点信息" 中获取。

![](https://mc.qcloudimg.com/static/img/4ce4a81c90b9ecdc19a4396720a46330/image.png)

#### 4.2.5 卸载共享目录 

当某些情况下需要卸载共享目录，请使用如下命令。其中 "目录名称" 为根目录或者文件系统的完整路径。
`umount <目录名称>：`
示例：
`umount X：` 

## 5. 终止资源
您可以从腾讯云控制台轻松终止 CVM 实例和文件系统。事实上，最好终止不再使用的资源，以免继续为其付费。
- 终止腾讯云实例。进入腾讯云云服务器 [控制台](https://console.cloud.tencent.com/cvm/index)，选中需要终止的实例，单击【更多】-【云主机状态】，可以选中“销毁”以终止 CVM 实例。
![](//mc.qcloudimg.com/static/img/0b0d631ceb9c94433d9302ca62b59e87/image.png)
- 终止文件系统。进入腾讯云文件存储 [控制台](https://console.cloud.tencent.com/cfs)，选中需要终止的文件系统，单击【删除】并【确认】，即可删除文件系统。
![](//mc.qcloudimg.com/static/img/506fd3cb3b4ed7cf8cb0cbff4715a2ee/image.png)
