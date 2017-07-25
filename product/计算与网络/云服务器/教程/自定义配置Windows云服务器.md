本文档介绍 Windows 云服务器的自定义配置方法。
不同于快速配置，自定义配置选项齐全，较少使用默认选项，您可根据需求选择合适的配置。

## 前提条件

 1. 开始自定义配置前，您需完成[【快速入门 Windows 云服务器】](https://www.qcloud.com/document/product/213/10071?!preview=&lang=cn)文档中的步骤一。
 2. 登录腾讯云官网，选择【云产品】-【计算与网络】-【云服务器】，单击【立即选购】按钮，进入 [云服务器购买页面](https://buy.qcloud.com/buy/cvm) 。
 3. 单击【自定义配置】，进入自定义配置界面。

## 选择地域与机型
![](//mc.qcloudimg.com/static/img/3ed8bab8cce3dde578a6e3fb14267ea5/image.png)
 1. 选择计费模式：包年包月或按量付费（无法购买按量付费云服务器的用户请先进行 [资质认证](https://console.qcloud.com/developer/infomation) ）。计费模式更多信息请看 [这里](http://www.qcloud.com/doc/product/213/%E8%AE%A1%E8%B4%B9%E6%A8%A1%E5%BC%8F%E8%AF%B4%E6%98%8E) 。

 2. 选择地域和可用区。当您需要多台云服务器时推荐分别选择不同可用区以达到容灾效果。

 3. 选择机型和配置。
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;根据底层硬件的不同，腾讯云目前提供了 *系列 1* 和 *系列 2* （下文也称为 *上一代实例* 和 *当前一代实例* ）两种不同的实例系列，不同的实例系列提供如下实例类型：
 
- 上一代实例类型：标准型S1，高IO型I1，内存型M1
- 当前一代实例类型：[标准型S2](https://www.qcloud.com/doc/product/213/7154)，[高IO型I2](https://www.qcloud.com/doc/product/213/7155)，[内存型M2](https://www.qcloud.com/doc/product/213/7156)，[计算型C2](https://www.qcloud.com/doc/product/213/7157)，[GPU型G2](https://www.qcloud.com/document/product/560)，[FPGA型FX2](https://www.qcloud.com/document/product/565) 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为获得最佳性能，我们建议您在新建实例时使用当前一代实例类型。实例类型详细说明，请参见 [实例类型概述](https://www.qcloud.com/document/product/213/7153) 。

>注意：
>不同的地域与可用区下的系列、机型会有所不同。

单击【下一步：选择镜像】按钮，进入选择镜像页面。

## 选择镜像
![](//mc.qcloudimg.com/static/img/be83f1c6052ad0f3aaf31b45203fa551/image.png)
 1. 选择镜像提供方。
对于刚开始使用腾讯云的用户，推荐选择公共镜像，其中包含了正版 Windows 操作系统，后续运行环境自行搭建。

 2. 选择操作系统：选择 Windows Server 。
 
 3. 选择系统版本。
-  系统内含正版激活，无需额外付费（北美地域除外）。 
-  适合于运行 Windows 下开发的程序，如.NET。 
-  支持 SQL Server 和其他更多数据库（需自行安装）。 

单击【下一步：选择存储与网络】按钮，进入选择存储与网络页面。

## 选择存储与网络
![](//mc.qcloudimg.com/static/img/e95a5bf7bf47c60f43dd0ee62946b67a/image.png)
 1. 选择硬盘类型和数据盘大小。
腾讯云提供云硬盘和本地硬盘两种类型。（均默认50GB系统盘，系统盘大小任选）
- 云硬盘：采用一盘三备的分布式存储方式，数据可靠性高
- 本地硬盘：处在云服务器所在的物理机上的存储设备，可以获得较低的时延，但存在单点丢失风险。具体对比可以参考 [这里](https://www.qcloud.com/document/product/362/2353#.E5.90.84.E7.A7.8D.E5.9D.97.E5.AD.98.E5.82.A8.E8.AE.BE.E5.A4.87.E7.9A.84.E5.AF.B9.E6.AF.94) 。

 2. 选择网络类型。
腾讯云提供 基础网络 或 私有网络 两种可选。
- 基础网络：适合新手用户，同一用户的云服务器内网互通。
- 私有网络：适合更高阶的用户，不同私有网络间逻辑隔离。

	>**注意：**
	> Windows 云服务器无法作为 [公网网关](http://www.qcloud.com/doc/product/215/%E7%BD%91%E5%85%B3#1.-公网网关) 使用，需要公网网关的用户请参考 [Linux 云服务器快速入门](https://www.qcloud.com/document/product/213/10133?!preview=&lang=cn)。

 3. 选择公网带宽。
腾讯云提供  按带宽计费  或  按使用流量计费  两种可选。
- 按带宽计费：选择固定带宽，超过本带宽时将丢包。适合网络波动较小的场景。
- 按使用流量计费：按实际使用流量收费。可限制峰值带宽避免意外流量带来的费用，当瞬时带宽超过该值时将丢包。适合网络波动较大的场景。

 4. 选择服务器数量。

 5. 选择购买时长与续费方式（仅限包年包月云服务器）。

单击【下一步：设置信息】按钮，进入设置信息页面。

## 设置信息
![](//mc.qcloudimg.com/static/img/fbc4230b5e6a19ef6ec60ffebfc62aaa/image.png)
 1. 命名主机：您可选择创建后命名，也可立即命名。

 2. 登录信息设置：您可设置密码，也可自动生成。设置的密码可在创建后修改，自动生成的密码将会以站内信方式发送。

 3. 选择安全组（<font color="red">确保登录端口3389开放</font>，更多信息见 [安全组](http://www.qcloud.com/doc/product/213/%E5%AE%89%E5%85%A8%E7%BB%84)） 。

单击【立即购买】按钮，完成支付后即可进入 [控制台](https://console.qcloud.com/cvm) 查收您的云服务器。

云服务器创建好后将会收到站内信，内容包括实例名称、公网 IP 地址、内网 IP 地址、登录名、初始登录密码等信息。您可以使用这些信息登录和管理实例，也请尽快更改您的 Windows 登录密码保障主机安全性。

单击 [这里](https://www.qcloud.com/document/product/213/10071?!preview=&lang=cn/#continue-page) ，继续 Windows 云服务器的后续配置。
