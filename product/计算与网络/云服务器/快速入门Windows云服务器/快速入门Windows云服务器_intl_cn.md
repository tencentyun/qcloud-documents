
本文档主要介绍如何快速使用 Windows 系统的云服务器实例的相关功能，引导新手快速了解腾讯云云服务器的创建和配置。

<div id="page1"></div>
## 步骤一：准备与选型
### 注册腾讯云账号
新用户需在腾讯云官网进行 [注册](https://intl.cloud.tencent.com/register) ，注册指引可参考 [如何注册腾讯云](/doc/product/378/9603) 。

### 确定云服务器所在地域及可用区
地域选择原则：
 - 靠近用户原则。
请根据您的用户所在地理位置选择云服务器地域。云服务器越靠近访问客户，越能获得较小的访问时延和较高的访问速度。比如：您的用户大部分位于北美洲时，多伦多地域是较好的选择。
 - 内网通信同地域原则。
同地域内，内网互通；不同地域，内网不通。需要多个云服务器内网通信的用户须选择相同云服务器地域。
相同地域下的云服务器可以通过内网相互通信（内网通信，免费）。
不同地域之间的云服务器不能通过内网互相通信（通信需经过公网，收费）。

### 确定云服务器配置方案
您可以在[【更多机型】](https://intl.cloud.tencent.com/document/product/213/7153)中根据实际需要比较各配置方案。当然您也可以在购买云服务器之后，根据您的需求随时进行 [配置升级](/doc/product/213/%E8%B0%83%E6%95%B4CVM%E5%AE%9E%E4%BE%8B%E9%85%8D%E7%BD%AE#1.-配置升级) 或 [配置降级](/doc/product/213/%E8%B0%83%E6%95%B4CVM%E5%AE%9E%E4%BE%8B%E9%85%8D%E7%BD%AE#2.-配置降级) 。
>**注意：**
> Windows 云服务器无法作为 [公网网关](/doc/product/215/%E7%BD%91%E5%85%B3#1.-公网网关) 使用，需要公网网关的用户请参考 [快速入门 Linux 云服务器](/doc/product/213/2936) 。

### 确定付费方式
腾讯云提供按量付费模式。详见 [计费模式说明](/doc/product/213/2180) 。
若您选择按量付费，则需先完成 [实名认证](https://console.cloud.tencent.com/developer/infomation) 。

<div id="page2"></div>
## 步骤二：创建 Windows 云服务器
本步骤介绍 Windows 云服务器的创建。本部分以快速简单配置为例说明，若快速配置不能满足您的需求，您可参考 [自定义配置 Windows 云服务器](/doc/product/213/10516) 文档进行详细选配。

![](//mc.qcloudimg.com/static/img/fa3a62404421c2fab5c8e08b6fe40588/image.png)

 1. 登录腾讯云官网，进入【Products】-【Computer】-【Cloud Virtual Machine】，单击【Experience】按钮，进入 [云服务器购买页面](https://console.cloud.tencent.com/cvm/index) 单击【+NEW】开始选购。

 2. 选择镜像。选择符合需求的 Windows 操作系统。
 
 3. 选择机型。
 
 4. 选择地域。靠近您客户的地域可降低访问延迟，提高下载速度。
 
 5. 选择公网带宽。若不需要连接到公网，带宽值选 0 。
 
 6.  选择服务器数量与购买时长。

 7. 设置账户名、登录方式。
 
查看站内信请见下一步骤。
 
<div id="Inter-Page">  </div>
## 步骤三：登录 Windows 云服务器
本部分操作介绍登录 Windows 云服务器的常用方法，不同情况下可以使用不同的登录方式，此处介绍控制台登录，更多登录方式请见 [登录 Windows 实例](/doc/product/213/5435) 。

### 前提条件
登录到云服务器时，需要使用管理员帐号和对应的密码。

 * 管理员账号：对于 Windows 类型的实例，管理员帐号统一为 Administrator
 * 密码：快速配置中，初始密码由系统随机分配。在下一环节（查看站内信及云服务器信息）中，具体查看操作。
   更多内容请参考 [登录密码](/doc/product/213/6093) 。
   
### 查看站内信及云服务器信息
完成云服务器的购买和创建后，云服务器的实例名称、公网 IP 地址、内网 IP 地址、登录名、初始登录密码等信息都将以 [站内信](https://console.cloud.tencent.com/message) 的方式发送到账户上。

![](//mc.qcloudimg.com/static/img/da559439d58296f6da3ff28c2c1ab952/image.png)
 1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index) 。登录后即可看到公网 IP 地址、内网 IP 地址等信息。

 2. 单击右上角【站内信】。

 3. 站内信页面即可查看新创建的云服务器，及登录名与密码等信息。


### 控制台登录云服务器
 1. 在云服务器列表的操作列，单击【Log In】按钮即可通过 VNC 连接至 Windows 云服务器：
	![](//mc.qcloudimg.com/static/img/2458a30dd79da5762ea6cf474755319e/image.png)

 2. 通过单击左上角发送 Ctrl-Alt-Delete 命令进入系统登录界面：
	![](//mc.qcloudimg.com/static/img/e4dbc02ca9ae2a7cb9ada5316effd31a/image.png)
	
 3. 输入帐号（Administrator）和站内信中的初始密码（或您修改后的密码）即可登录。

>**注意：**
>该终端为独享，即同一时间只有一个用户可以使用控制台登录。

<div id="page4"></div>
## 步骤四：格式化与分区数据盘

这里以 Windows 2012 R2 为例进行格式化说明。

### 前提条件
 - 已购买数据盘的用户，需要格式化数据盘才可使用。未购买数据盘的用户可以跳过此步骤。
 - 请确保您已完成步骤三操作，登录到云服务器。

### 格式化数据盘

 1. 通过步骤三介绍的方法登录 Windows 云服务器。

 2. 单击【Start】-【Server manager】-【tool】-【Computer management】-【storage】-【Disk management】。

 3. 在磁盘1上右键单击，选择【Online】：
	![](//mc.qcloudimg.com/static/img/1217193557509925a622dcdb81aa2e35/image.png)

 4. 右键单击，选择【Initialize disk】：
	![](//mc.qcloudimg.com/static/img/94ab92867d77ea69bc803a0b20f2b941/image.png)

 5. 根据分区方式的不同，选择【GPT】或【MBR】，单击【OK】按钮：
 > **注意：**
 > 磁盘大于 2TB ，一定要选择 GPT 分区形式。
	![](//mc.qcloudimg.com/static/img/1f7b0f72767193cfa662e188c86cf31b/image.png)

### 磁盘分区（可选）

 1. 在未分配的空间处右击，选择【New Simple Volume】：
	![](//mc.qcloudimg.com/static/img/a6ca720af2082d7a470ece17a8e13f5d/image.png)

 2. 在弹出的“新建简单卷向导”窗口中，单击【Next】：
	![](//mc.qcloudimg.com/static/img/10fdcd70b510a57919c6a40cf43452a7/image.png)

 3. 输入分区所需磁盘大小，单击【Next】：
	![](//mc.qcloudimg.com/static/img/05c8d1425a0208597b1d2c75a9c811b6/image.png)

 4. 输入驱动器号，单击【Next】：
	![](//mc.qcloudimg.com/static/img/737ed569049ad617715efb06fe44e7b2/image.png)

 5. 选择文件系统，格式化分区，单击【Next】：
	![](//mc.qcloudimg.com/static/img/896cb3f2705fb9fcd04c236b8fb9ec59/image.png)

 6. 完成新建简单卷，单击【Complete】：
	![](//mc.qcloudimg.com/static/img/1e257b9c76d80f30b34f612496b8007b/image.png)

 7. 在【Win】中打开【Computer】，查看新分区：
	![](//mc.qcloudimg.com/static/img/1cbb4ad1c3c01852a00a1415526a3e12/image.png)

**至此，您已完成 Windows 系统的云服务器的创建和基础配置。**
