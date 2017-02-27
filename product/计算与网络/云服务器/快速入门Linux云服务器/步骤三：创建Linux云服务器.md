1) 登录腾讯云官网，选择【云产品】-【计算与网络】-【云服务器】，点击【立即选购】按钮，进入[云服务器购买页面](https://buy.qcloud.com/buy/cvm)

2) 选择计费模式：包年包月或按量付费（无法购买按量付费云服务器的用户请先进行[资质认证](https://console.qcloud.com/developer/infomation)）。两种付费模式一个按整月计算一个按实际使用的秒数计算。更多信息请看[这里](http://www.qcloud.com/doc/product/213/%E8%AE%A1%E8%B4%B9%E6%A8%A1%E5%BC%8F%E8%AF%B4%E6%98%8E)。
![](//mccdn.qcloud.com/static/img/2116de97fc48aa340e08d3ebb982bbde/image.png)

3) 选择地域和可用区。当您需要多台云服务器时推荐分别选择不同可用区以达到容灾效果。

4) 选择机型和配置。
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;根据底层硬件的不同，腾讯云目前提供了 *系列 1* 和 *系列 2* （下文也称为 *上一代实例* 和 *当前一代实例* ）两种不同的实例系列，不同的实例系列提供如下实例类型：

**当前一代实例类型**：[标准型S2](https://www.qcloud.com/doc/product/213/7154)，[高IO型I2](https://www.qcloud.com/doc/product/213/7155)，[内存型M2](https://www.qcloud.com/doc/product/213/7156)，[计算型C2](https://www.qcloud.com/doc/product/213/7157)
**上一代实例类型**：标准型S1，高IO型I1，内存型M1

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为获得最佳性能，我们建议您在新建实例时使用当前一代实例类型。实例类型详细说明，请参见[实例类型概述](https://www.qcloud.com/document/product/213/7153)。


根据第二步确定的配置选择实例规格。
![](//mccdn.qcloud.com/static/img/0a506ce5c9c271ee09ea237ce1d34944/image.png)

5) 对于刚开始使用腾讯云的用户可选择公共镜像，腾讯云提供了包括但不限于CentOS、Ubuntu、Debian、SUSE、OpenSUSE、FreeBSD等操作系统，后续运行环境请您自行搭建。

操作系统选择任意Linux系统，并根据需要挑选版本。
![](//mccdn.qcloud.com/static/img/fe36402379bbc70d9e17591568a6e1f6/image.png)

- Linux为开源系统，支持各种主流编程语言，支持 MySQL 等数据库（需自行安装)。 

6) 选择硬盘类型和数据盘大小。
腾讯云提供云硬盘和本地硬盘两种类型。
- 云硬盘：采用一盘三备的分布式存储方式，数据可靠性高
- 本地硬盘：处在云服务器所在的物理机上的存储设备，可以获得较低的时延，但存在单点丢失风险。具体对比可以参考[这里](https://www.qcloud.com/document/product/362/2353#.E5.90.84.E7.A7.8D.E5.9D.97.E5.AD.98.E5.82.A8.E8.AE.BE.E5.A4.87.E7.9A.84.E5.AF.B9.E6.AF.94)。

不管选择那种硬盘类型，Linux云服务器都默认赠送20GB系统盘，且选择云硬盘时允许您通过付费方式调整至50GB大小。数据盘大小可由您自行选购。
![](//mccdn.qcloud.com/static/img/ef73fc3a1b4d6d1579b322d92d536ac1/image.png)
![](//mccdn.qcloud.com/static/img/72eb6b4c7c89b332394c0e10b0d39ab8/image.png)

7) 选择网络类型（基础网络或私有网络）及公网带宽（固定带宽计费或流量计费）。
- 基础网络：适合新手用户，同一用户的云服务器内网互通。
- 私有网络：适合更高阶的用户，不同私有网络间逻辑隔离。
>公网网关是私有网络与公网的一种接口，可转发私有网络中不同子网内无外网IP的云服务器请求。更多详情请见[公网网关](http://www.qcloud.com/doc/product/215/%E7%BD%91%E5%85%B3#1.-公网网关)
- 固定带宽计费：选择固定带宽，超过本带宽时将丢包。适合网络波动较小的场景。
- 流量计费：按实际使用流量收费。可限制峰值带宽避免意外流量带来的费用，当瞬时带宽超过该值时将丢包。适合网络波动较大的场景。
![](//mccdn.qcloud.com/static/img/3a09b6af11caeb074282dd23006dd818/image.png)

8) 确定服务器数量、购买时长（仅限包年包月云服务器）。

9) 选择登录方式。
- 密码登录：系统自动生成初始密码并通过站内信发送给您。获取初始密码后即可通过默认用户名及密码登录Linux云服务器。
- 密钥登录：安全性高于普通密码登录，要求您先[创建一对密钥](http://www.qcloud.com/doc/product/213/%E5%AF%86%E9%92%A5%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97#1.-创建密钥)。

10) 选择安全组（确保登录端口22开放，更多信息见[安全组](http://www.qcloud.com/doc/product/213/%E5%AE%89%E5%85%A8%E7%BB%84)），点击【立即购买】按钮，完成支付后即可进入[控制台](https://console.qcloud.com/cvm)查收您的云服务器。

云服务器创建好后用户将会会收到站内信，内容包括实例名称、公网 IP 地址、内网 IP 地址、登录名、初始登录密码（选择密码登录时）等信息。您可以使用这些信息登录和管理实例，也请尽快更改您的Linux登录密码保障主机安全性。

