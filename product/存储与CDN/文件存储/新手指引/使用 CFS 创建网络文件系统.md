
## 1. 创建和配置 CVM 实例
要访问文件系统，您需要将文件系统挂载在基于 Linux 或者 Windows 的腾讯云云服务器实例上。在此步骤中，您将创建和配置一个腾讯云 CVM 实例。如果已经创建 CVM 实例，请跳转至步骤 2 创建文件系统及挂载点。

### 1.1 Linux 云服务器
本步骤主要介绍如何快速使用 Linux 系统的云服务器实例的相关功能，引导新手快速了解腾讯云云服务器的创建和配置。如果需要使用 Windows 系统的云服务器，请参考步骤 1.2 Windows 云服务器。
#### 1.1.1 准备与选型

**注册腾讯云账号**
新用户需在腾讯云官网 [注册](https://www.qcloud.com/register?s_url=https%3A%2F%2Fwww.qcloud.com%2Fdocument%2Fproduct%2F213) 账户，注册指引可参考 [如何注册腾讯云](/doc/product/378/9603) 。

**确定云服务器所在地域及可用区**
地域选择原则：
 - 靠近用户原则。
请根据您的用户所在地理位置选择云服务器地域。云服务器越靠近访问客户，越能获得较小的访问时延和较高的访问速度。比如：您的用户大部分位于长江三角洲附近时，上海地域是较好的选择。
 - 内网通信同地域原则。
同地域内，内网互通；不同地域，内网不通。需要多个云服务器内网通信的用户须选择相同云服务器地域。
相同地域下的云服务器可以通过内网相互通信（内网通信，免费）。
不同地域之间的云服务器不能通过内网互相通信（通信需经过公网，收费）。

**确定云服务器配置方案**
腾讯云提供如下 [推荐配置](https://www.qcloud.com/act/recommended)：
- 入门型：适用于起步阶段的个人网站。如：个人博客等小型网站。
- 基础型：适合有一定访问量的网站或应用。如：较大型企业官网、小型电商网站。
- 普及型：适合常使用云计算等一定计算量的需求。如：门户网站、SaaS 软件、小型 App 。
- 应用型：适用于并发要求较高的应用及适合对云服务器网络及计算性能有一定要求的应用场景。如：大型门户、电商网站、游戏 App 。

若推荐的配置不能满足您的需求，您可以在 [更多机型](https://buy.qcloud.com/cvm?tabIndex=1) 中根据实际需要比较各配置方案。当然您也可以在购买云服务器之后，根据您的需求随时进行 [配置升级](/doc/product/213/%E8%B0%83%E6%95%B4CVM%E5%AE%9E%E4%BE%8B%E9%85%8D%E7%BD%AE#1.-配置升级)  或  [配置降级](/doc/product/213/%E8%B0%83%E6%95%B4CVM%E5%AE%9E%E4%BE%8B%E9%85%8D%E7%BD%AE#2.-配置降级) 。

**确定付费方式**
腾讯云提供“包年包月”和“按量付费”两种付费模式。详见 [计费模式说明](/doc/product/213/2180) 。若您选择按量付费，则需先完成 [实名认证](https://console.qcloud.com/developer/infomation) 。

#### 1.1.2 创建 Linux 云服务器
本步骤介绍 Linux 云服务器的创建，腾讯云提供快速配置和自定义配置两种方式。本部分以快速配置为例说明，若快速配置不能满足您的需求，您可参考 [自定义配置 Linux 云服务器](/doc/product/213/10517) 文档进行配置。
登录腾讯云官网，选择【云产品】-【计算与网络】-【云服务器】，单击【立即选购】，进入 [云服务器购买页面](https://buy.qcloud.com/buy/cvm)。

 > **注意：**
 > 初次购买的账户默认进入【快速配置】页面，购买过的用户默认进入【自定义配置】页面。

![](//mc.qcloudimg.com/static/img/4daa9004a9b40bd378f0486b92f2a4d3/image.png)

- 选择镜像。快速配置向您推荐 Ubuntu Server 16.04.1 LTS 64位 与 CentOS 7.2 64位 的操作系统方案。
- 选择机型。
- 选择地域。靠近您客户的地域可降低访问延迟，提高下载速度。
- 选择公网带宽。若不需要连接到公网，带宽值选 0 。
- 选择服务器数量与购买时长。
 
### 1.2 Windows 云服务器
本文档主要介绍如何快速使用 Windows 系统的云服务器实例的相关功能，引导新手快速了解腾讯云云服务器的创建和配置。如果需要使用 linux 系统的云服务器，请参考步骤 1.1 Linux 云服务器。

#### 1.2.1 准备与选型
**注册腾讯云账号**
新用户需在腾讯云官网 [注册](https://www.qcloud.com/register?s_url=https%3A%2F%2Fwww.qcloud.com%2Fdocument%2Fproduct%2F213)账户，注册指引可参考 [如何注册腾讯云](/doc/product/378/9603) 。

**确定云服务器所在地域及可用区**
地域选择原则：
 - 靠近用户原则。
请根据您的用户所在地理位置选择云服务器地域。云服务器越靠近访问客户，越能获得较小的访问时延和较高的访问速度。比如：您的用户大部分位于长江三角洲附近时，上海地域是较好的选择。
 - 内网通信同地域原则。
同地域内，内网互通；不同地域，内网不通。需要多个云服务器内网通信的用户须选择相同云服务器地域。
相同地域下的云服务器可以通过内网相互通信（内网通信，免费）。
不同地域之间的云服务器不能通过内网互相通信（通信需经过公网，收费）。

**确定云服务器配置方案**
腾讯云提供如下 [推荐配置](https://www.qcloud.com/act/recommended)：
- 入门型：适用于起步阶段的个人网站。如：个人博客等小型网站。
- 基础型：适合有一定访问量的网站或应用。如：较大型企业官网、小型电商网站。
- 普及型：适合常使用云计算等一定计算量的需求。如：门户网站、SaaS 软件、小型 App 。
- 应用型：适用于并发要求较高的应用及适合对云服务器网络及计算性能有一定要求的应用场景。如：大型门户、电商网站、游戏 App 。

若推荐的配置不能满足您的需求，您可以在 [更多机型](https://buy.qcloud.com/cvm?tabIndex=1) 中根据实际需要比较各配置方案。当然您也可以在购买云服务器之后，根据您的需求随时进行 [配置升级](/doc/product/213/%E8%B0%83%E6%95%B4CVM%E5%AE%9E%E4%BE%8B%E9%85%8D%E7%BD%AE#1.-配置升级) 或 [配置降级](/doc/product/213/%E8%B0%83%E6%95%B4CVM%E5%AE%9E%E4%BE%8B%E9%85%8D%E7%BD%AE#2.-配置降级) 。
>**注意：**
> Windows 云服务器无法作为 [公网网关](/doc/product/215/%E7%BD%91%E5%85%B3#1.-公网网关) 使用，需要公网网关的用户请参考 [快速入门 Linux 云服务器](/doc/product/213/2936) 。

**确定付费方式**
腾讯云提供“包年包月”和“按量付费”两种付费模式。详见 [计费模式说明](/doc/product/213/2180) 。若您选择按量付费，则需先完成 [实名认证](https://console.qcloud.com/developer/infomation) 。

#### 1.2.2 创建 Windows 云服务器
本步骤介绍 Windows 云服务器的创建，腾讯云提供快速配置和自定义配置两种方式。本部分以快速配置为例说明，若快速配置不能满足您的需求，您可参考 [自定义配置 Windows 云服务器](/doc/product/213/10516) 文档进行配置。
登录腾讯云官网，选择【云产品】-【计算与网络】-【云服务器】，单击【立即选购】按钮，进入 [云服务器购买页面](https://buy.qcloud.com/buy/cvm) 。
> 注意：
 > 初次购买的账户默认进入【快速配置】页面，购买过的用户默认进入【自定义配置】页面。

![](//mc.qcloudimg.com/static/img/377368de9e85b21bf90632480dad903c/image.png)
 - 选择镜像。选择符合需求的 Windows 操作系统。
 - 选择机型。
 - 选择地域。靠近您客户的地域可降低访问延迟，提高下载速度。
 - 选择公网带宽。若不需要连接到公网，带宽值选 0 。
 - 选择服务器数量与购买时长。
 
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

