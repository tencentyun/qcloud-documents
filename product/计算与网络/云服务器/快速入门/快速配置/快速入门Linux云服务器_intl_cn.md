
本文档主要介绍如何快速使用 Linux 系统的云服务器实例的相关功能，引导新手快速了解腾讯云云服务器的创建和配置。

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

### 确定付费方式
腾讯云提供按量付费模式。详见 [计费模式说明](/doc/product/213/2180) 。
若您选择按量付费，则需先完成 [实名认证](https://console.cloud.tencent.com/developer/infomation) 。

<div id="page2"></div>
## 步骤二：创建 Linux 云服务器
本步骤介绍 Linux 云服务器的创建。本部分以快速简单配置为例说明，若快速配置不能满足您的需求，您可参考 [自定义配置 Linux 云服务器](/doc/product/213/10517) 文档进行详细选配。

![](//mc.qcloudimg.com/static/img/15b48516a605826fbc15d6775be04f20/image.png)

 1. 登录腾讯云官网，进入【Products】-【Computer】-【Cloud Virtual Machine】，单击【Experience】按钮，进入 [云服务器购买页面](https://console.cloud.tencent.com/cvm/index) 单击【+NEW】开始选购。

 2. 选择镜像。选择符合需求的 Linux 操作系统。
 
 3. 选择机型。
 
 4. 选择地域。靠近您客户的地域可降低访问延迟，提高下载速度。
 
 5. 选择公网带宽。若不需要连接到公网，带宽值选 0 。
 
 6.  选择服务器数量与购买时长。

 7. 设置账户名、登录方式。
 
查看站内信请见下一步骤。
 
<div id="Inter-Page">  </div>
## 步骤三：登录 Linux 云服务器
本部分操作介绍登录 Linux 云服务器的常用方法，不同情况下可以使用不同的登录方式，此处介绍控制台登录，更多登录方式请见 [登录 Linux 实例](/doc/product/213/5436) 。

### 前提条件
登录到云服务器时，需要使用管理员帐号和对应的密码。

 * 管理员账号：对于 Linux 类型的实例，管理员帐号统一为 root （ Ubuntu 系统用户为 ubuntu ）
 * 密码：快速配置中，初始密码由系统随机分配。在下一环节（查看站内信及云服务器信息）中，具体查看操作。
   更多内容请参考 [登录密码](/doc/product/213/6093) 。
   
### 查看站内信及云服务器信息
完成云服务器的购买和创建后，云服务器的实例名称、公网 IP 地址、内网 IP 地址、登录名、初始登录密码等信息都将以 [站内信](https://console.cloud.tencent.com/message) 的方式发送到账户上。

![](//mc.qcloudimg.com/static/img/da559439d58296f6da3ff28c2c1ab952/image.png)
 1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index) 。登录后即可看到公网 IP 地址、内网 IP 地址等信息。

 2. 单击右上角【站内信】。

 3. 站内信页面即可查看新创建的云服务器，及登录名与密码等信息。


### 控制台登录云服务器
 1. 在云服务器列表的操作列，单击【Log In】按钮即可通过 VNC 连接至 Linux 云服务器：
	![](//mc.qcloudimg.com/static/img/2458a30dd79da5762ea6cf474755319e/image.png)

 2. 通过单击左上角发送 Ctrl-Alt-Delete 命令进入系统登录界面：
	![](//mc.qcloudimg.com/static/img/e4dbc02ca9ae2a7cb9ada5316effd31a/image.png)
	
 3. 输入帐号（Administrator）和站内信中的初始密码（或您修改后的密码）即可登录。

>**注意：**
>该终端为独享，即同一时间只有一个用户可以使用控制台登录。

<div id="page4"></div>
## 步骤四：分区与格式化数据盘

### 前提条件
 - 已购买数据盘的用户，需要格式化数据盘才可使用。未购买数据盘的用户可以跳过此步骤。
 - 请确保您已完成步骤三操作，登录到云服务器。
 - 大于 2TB 的硬盘请使用 GPT 方式进行搭载数据盘操作。详情请参见 [使用 GPT 分区表分区并格式化](/doc/product/213/2043) 。
 
### 分区数据盘

 1. 通过步骤三介绍的方法登录 Linux 云服务器。

	> **注意：**
	> 仅支持对数据盘进行分区，不支持对系统盘进行分区。若您强行对系统盘分区可能导致系统崩溃等严重问题，针对此种情况腾讯云不承担赔偿责任。

 2. 输入命令`fdisk -l`查看您的数据盘信息。
	本示例中，有一个 54 GB 的数据盘`(/vdb)`需要挂载。
	>**注意：**
	>`fdisk -l`与`df -h` 都为拆看数据盘信息命令，但在没有分区和格式化数据盘之前，使用`df -h` 命令无法看到数据盘。

	![](//mc.qcloudimg.com/static/img/f26b5a092e1521556410afdc75a95474/image.png)

 3. 对数据盘进行分区。按照界面的提示，依次操作：

 	1. 输入`fdisk /dev/vdb`(对数据盘进行分区)，回车；
 	2. 输入`n`(新建分区)，回车；
 	3. 输入`p`(新建扩展分区)，回车；
 	4. 输入`1`(使用第 1 个主分区)，回车；
 	5. 输入回车(使用默认配置)；
 	6. 再次输入回车(使用默认配置)；
 	7. 输入`wq`(保存分区表)，回车开始分区。

	这里以创建 1 个分区为例，开发者也可以根据自己的需求创建多个分区。
	![](//mc.qcloudimg.com/static/img/8a9c8ff4db5a7e4622bf2968d0309129/image.png)

 4. 使用`fdisk -l`命令，即可查看到，新的分区 vdb1 已经创建完成。
	![](//mc.qcloudimg.com/static/img/304ccd9491f2a25b8d3b33b5213faa0e/image.png)

### 格式化数据盘

 1. 新分区格式化
 分区后需要对分好的区进行格式化，您可自行决定文件系统的格式，如 ext2、ext3 等。本例以 ext3 为例。
使用下面的命令对新分区进行格式化： 
	```
	mkfs.ext3 /dev/vdb1
	```
	![](//mc.qcloudimg.com/static/img/fce59c4aba93c688c429fe4760452264/image.png)

 2. 挂载分区
	使用以下命令创建 mydata 目录并将分区挂载在该目录下：
	```
	mkdir /mydata
	mount /dev/vdb1 /mydata
	```
	使用命令查看挂载：
	```
	df -h
	```
	出现如图框选的 vdb1 信息则说明挂载成功，即可以查看到数据盘了。
	![](//mc.qcloudimg.com/static/img/d6bc35b30b823c567812affd032bfedf/image.png)

 3. 设置启动自动挂载
如果希望云服务器在重启或开机时能自动挂载数据盘，必须将分区信息添加到 `/etc/fstab `中。
使用以下命令添加分区信息：
	```
	echo '/dev/vdb1 /mydata ext3 defaults 0 0' >> /etc/fstab
	```
	使用以下命令查看：
	```
	cat /etc/fstab
	```
	出现如图最下方框选的 vdb1 信息则说明添加分区信息成功。
	![](//mc.qcloudimg.com/static/img/39025e909cd849d5a34378a7d0078d13/image.png)
	
**至此，您已完成 Linux 系统的云服务器的创建和基础配置。**
