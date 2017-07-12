
本文档主要介绍如何快速使用 Windows 系统的云服务器实例的相关功能，引导新手快速了解腾讯云云服务器的创建和配置。

## 步骤一：准备与选型
### 注册腾讯云账号
新用户需在腾讯云官网进行[【注册】](https://www.qcloud.com/register?s_url=https%3A%2F%2Fwww.qcloud.com%2Fdocument%2Fproduct%2F213)，注册指引可参考[如何注册腾讯云](https://www.qcloud.com/document/product/378/9603)。

### 确定云服务器所在地域
地域选择原则：
 - 靠近用户原则。
请根据您的用户所在地理位置选择云服务器地域。云服务器越靠近访问客户，越能获得较小的访问时延和较高的访问速度。比如：您的用户大部分位于长江三角洲附近时，上海地域是较好的选择。
 - 同地域内，内网互通；不同地域，内网不通。
相同地域下的云服务器可以通过内网相互通信（内网通信，免费）。
不同地域之间的云服务器不能通过内网互相通信（通信需经过公网，收费）。

### 确定云服务器配置需求
腾讯云提供如下推荐配置：[【推荐配置】](https://www.qcloud.com/act/event/recommand.html)
- 入门型：适用于起步阶段的个人网站。如：个人博客等小型网站。
- 基础型：适合有一定访问量的网站或应用。如：企业官网等简单的 Web 应用。
- 普及型：适合常使用云计算等一定计算量的需求。如：并发适中的 App 或普通数据处理。
- 专业型：适用于并发要求较高的应用及适合对云服务器网络及计算性能有一定要求的应用场景。如：企业运营活动、批量处理、分布式分析与视频和图片存储访问较大的网站。

若推荐的配置不能满足您的需求，您可以在[【更多机型】](https://buy.qcloud.com/cvm)中根据实际需要比较各配置方案。当然您也可以在购买云服务器之后，根据您的需求随时进行 [配置升级](http://www.qcloud.com/doc/product/213/%E8%B0%83%E6%95%B4CVM%E5%AE%9E%E4%BE%8B%E9%85%8D%E7%BD%AE#1.-配置升级) 或 [配置降级](http://www.qcloud.com/doc/product/213/%E8%B0%83%E6%95%B4CVM%E5%AE%9E%E4%BE%8B%E9%85%8D%E7%BD%AE#2.-配置降级) 。

### 确定付费方式
腾讯云提供 包年包月 和 按量付费 两种付费模式。详见 [计费模式说明](https://www.qcloud.com/document/product/213/2180) 。
若您选择按量付费，则需先完成 [资质认证](https://console.qcloud.com/developer/infomation) 。

## 步骤二：创建 Windows云服务器
 1\. 登录腾讯云官网，选择【云产品】-【计算与网络】-【云服务器】，点击【立即选购】按钮，进入 [云服务器购买页面](https://buy.qcloud.com/buy/cvm)。

### 选择地域与机型
![](//mc.qcloudimg.com/static/img/babdcee1af6a70057257f0403c11de9f/image.png)
2\. 选择计费模式：包年包月或按量付费（无法购买按量付费云服务器的用户请先进行 [资质认证](https://console.qcloud.com/developer/infomation) ）。计费模式更多信息请看 [这里](http://www.qcloud.com/doc/product/213/%E8%AE%A1%E8%B4%B9%E6%A8%A1%E5%BC%8F%E8%AF%B4%E6%98%8E)。

3\. 选择地域和可用区。当您需要多台云服务器时推荐分别选择不同可用区以达到容灾效果。

4\. 选择机型和配置。
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;根据底层硬件的不同，腾讯云目前提供了 *系列 1* 和 *系列 2* （下文也称为 *上一代实例* 和 *当前一代实例* ）两种不同的实例系列，不同的实例系列提供如下实例类型：
  - 上一代实例类型：标准型S1，高IO型I1，内存型M1
  - 当前一代实例类型：[标准型S2](https://www.qcloud.com/doc/product/213/7154)，[高IO型I2](https://www.qcloud.com/doc/product/213/7155)，[内存型M2](https://www.qcloud.com/doc/product/213/7156)，[计算型C2](https://www.qcloud.com/doc/product/213/7157)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为获得最佳性能，我们建议您在新建实例时使用当前一代实例类型。实例类型详细说明，请参见 [实例类型概述](https://www.qcloud.com/document/product/213/7153) 。

>注释：不同的地域与可用区下的系列、机型会有所不同。

点击【下一步：选择镜像】按钮，进入选择镜像页面。

### 选择镜像
![](//mc.qcloudimg.com/static/img/3a347761dad2fdac7962b09f656efa01/image.png)
5\. 选择镜像提供方。
对于刚开始使用腾讯云的用户，推荐选择公共镜像，其中包含了正版 Windows 操作系统，后续运行环境自行搭建。

6\. 选择操作系统：选择 Windows Server 。
 
7\. 选择系统版本。
 - 系统内含正版激活，无需额外付费（北美地域除外）。 
 - 适合于运行 Windows 下开发的程序，如.NET。 
 - 支持 SQL Server 和其他更多数据库（需自行安装）。 

点击【下一步：选择存储与网络】按钮，进入选择存储与网络页面。

### 选择存储与网络
![](//mc.qcloudimg.com/static/img/3f826b7b8f925c8a7c2b5d2ab5182773/image.png)
8\. 选择硬盘类型和数据盘大小。
腾讯云提供云硬盘和本地硬盘两种类型。（均默认50GB系统盘，系统盘大小任选）
- 云硬盘：采用一盘三备的分布式存储方式，数据可靠性高
- 本地硬盘：处在云服务器所在的物理机上的存储设备，可以获得较低的时延，但存在单点丢失风险。具体对比可以参考 [这里](https://www.qcloud.com/document/product/362/2353#.E5.90.84.E7.A7.8D.E5.9D.97.E5.AD.98.E5.82.A8.E8.AE.BE.E5.A4.87.E7.9A.84.E5.AF.B9.E6.AF.94) 。

9\. 选择网络类型。
腾讯云提供 基础网络  或  私有网络  两种可选。
- 基础网络：适合新手用户，同一用户的云服务器内网互通。
- 私有网络：适合更高阶的用户，不同私有网络间逻辑隔离。

>**注意：**
>Windows云服务器无法作为 [公网网关](http://www.qcloud.com/doc/product/215/%E7%BD%91%E5%85%B3#1.-公网网关) 使用，需要公网网关的用户请参考 Linux 云服务器快速入门。

10\. 选择公网带宽。
腾讯云提供  按带宽计费  或  按使用流量计费  两种可选。
- 按带宽计费：选择固定带宽，超过本带宽时将丢包。适合网络波动较小的场景。
- 按使用流量计费：按实际使用流量收费。可限制峰值带宽避免意外流量带来的费用，当瞬时带宽超过该值时将丢包。适合网络波动较大的场景。

11\. 选择服务器数量。

12\. 选择购买时长与续费方式（仅限包年包月云服务器）。

点击【下一步：设置信息】按钮，进入设置信息页面。

### 设置信息
![](//mc.qcloudimg.com/static/img/6eb79dd99d8e93655684382b79af68dd/image.png)
13\. 命名主机：您可选择创建后命名，也可立即命名。

14\. 登录信息设置：您可设置密码，也可自动生成。设置的密码可在创建后修改，自动生成的密码将会以站内信方式发送。

15\. 选择安全组（<font color="red">确保登录端口3389开放</font>，更多信息见 [安全组](http://www.qcloud.com/doc/product/213/%E5%AE%89%E5%85%A8%E7%BB%84)） 。

点击【立即购买】按钮，完成支付后即可进入 [控制台](https://console.qcloud.com/cvm) 查收您的云服务器。

云服务器创建好后将会收到站内信，内容包括实例名称、公网 IP 地址、内网 IP 地址、登录名、初始登录密码等信息。您可以使用这些信息登录和管理实例，也请尽快更改您的 Windows 登录密码保障主机安全性。

查看站内信请见下一步骤。

## 步骤三：登录Windows云服务器
本部分操作介绍登录 Windows 云服务器的常用方法，不同情况下可以使用不同的登录方式，此处介绍控制台登录，更多登录方式请见   [登录 Windows 实例](https://www.qcloud.com/document/product/213/5435) 。

### 前提条件
登录到云服务器时，需要使用管理员帐号和对应的密码。

 * 管理员账号：对于 Windows 类型的实例，管理员帐号统一为 Administrator
 * 密码：
   * 若用户在创建实例时选择【自动生成密码】，则初始密码由系统随机分配。能可以在下一环节（查看站内信及云服务器信息）中，获得信息。
   * 若用户在创建实例时选择【自定义密码】，则密码为用户指定的密码。
   * 有关密码的更多内容请参考 [登录密码](/doc/product/213/6093) 。
   
### 查看站内信及云服务器信息
完成云服务器的购买和创建后，云服务器的实例名称、公网 IP 地址、内网 IP 地址、登录名、初始登录密码等信息都将以站内信的方式发送到账户上。
![](//mc.qcloudimg.com/static/img/e25aadddb94d210c4f196eded9c460a3/image.png)

 1. 登录 [云服务器控制台](https://console.qcloud.com/cvm) 。登录后即可看到公网 IP 地址、内网 IP 地址等信息。

 2. 点击右上角【站内信】。

 3. 站内信页面即可查看新创建的云服务器，及登录名与密码等信息。


### 控制台登录云服务器
 1. 在云服务器列表的操作列，点击【登录】按钮即可通过VNC连接至Windows云服务器：
	![](//mccdn.qcloud.com/img56b1a6cb7b3e8.png)

 2. 通过在左上角发送Ctrl+Alt+Del命令进入系统登录界面：
	![](//mc.qcloudimg.com/static/img/e4dbc02ca9ae2a7cb9ada5316effd31a/image.png)
	
 3. 输入帐号（Administrator）和站内信中的初始密码（或您修改后的密码）即可登录。

>**注意：**
>该终端为独享，即同一时间只有一个用户可以使用控制台登录。

## 步骤四：格式化数据盘

这里以 Windows 2012 R2 为例进行格式化说明。

### 前提条件
 - 购买了数据盘的用户，需要格式化才可使用。未购买数据盘的用户可以跳过此步骤。
 - 请确保您已完成步骤三操作，登录到云服务器。

### 格式化数据盘

 1. 通过步骤三介绍的方法登录 Windows 云服务器。

 2. 点击【开始】-【服务器管理器】-【工具】-【计算机管理】-【存储】-【磁盘管理】。

 3. 在磁盘1上右键点击，选择【联机】：
	![](//mc.qcloudimg.com/static/img/1217193557509925a622dcdb81aa2e35/image.png)

 4. 右键点击，选择【初始化磁盘】：
	![](//mc.qcloudimg.com/static/img/94ab92867d77ea69bc803a0b20f2b941/image.png)

 5. 根据分区方式的不同，选择【GPT】或【MBR】，点击【确定】按钮：
 > **注意：**
 > 磁盘大于2TB，一定要选择GPT分区形式。
 
	![](//mc.qcloudimg.com/static/img/1f7b0f72767193cfa662e188c86cf31b/image.png)

### 磁盘分区（可选）

 1. 在未分配的空间处右击，选择【新建简单卷】：
	![](//mc.qcloudimg.com/static/img/a6ca720af2082d7a470ece17a8e13f5d/image.png)

 2. 在弹出的“新建简单卷向导”窗口中，点击【下一步】：
	![](//mc.qcloudimg.com/static/img/10fdcd70b510a57919c6a40cf43452a7/image.png)

 3. 输入分区所需磁盘大小，点击【下一步】：
	![](//mc.qcloudimg.com/static/img/05c8d1425a0208597b1d2c75a9c811b6/image.png)

 4. 输入驱动器号，点击【下一步】：
	![](//mc.qcloudimg.com/static/img/737ed569049ad617715efb06fe44e7b2/image.png)

 5. 选择文件系统，格式化分区，点击【下一步】：
	![](//mc.qcloudimg.com/static/img/896cb3f2705fb9fcd04c236b8fb9ec59/image.png)

 6. 完成新建简单卷，点击【完成】：
	![](//mc.qcloudimg.com/static/img/1e257b9c76d80f30b34f612496b8007b/image.png)

 7. 在【开始】中打开【这台电脑】，查看新分区：
	![](//mc.qcloudimg.com/static/img/1cbb4ad1c3c01852a00a1415526a3e12/image.png)

