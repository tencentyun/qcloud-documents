与快速配置云服务器相比，自定义配置提供您更丰富的镜像平台，以及存储、带宽以及安全组等高级设置，您可根据需求选择合适的配置。本文档以自定义配置为例进行介绍。
若您需要通过快速配置进行创建云服务器，可参考 [快速配置 Windows 云服务器](https://cloud.tencent.com/document/product/213/2764) 文档进行配置。

## 注册及认证

在使用云服务器之前，您需要完成以下准备工作：
1. 注册腾讯云账号，并完成实名认证。
新用户需在腾讯云官网进行 [注册](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F)，具体操作可参考 [注册腾讯云](https://cloud.tencent.com/doc/product/378/9603)。
2. 访问 [腾讯云云服务器介绍页面](https://cloud.tencent.com/product/cvm)，单击【立即选购】。

## 选择地域与机型
>! 对于初次购买的账户，默认进入【快速配置】页面。对于已购买过云服务器的用户，默认进入【自定义配置】页面。若您未购买过云服务器，请选择【自定义配置】进行自定义配置操作。
>
![选择地域与机型](https://main.qcloudimg.com/raw/7f8aae3cd95da2af33e2be807d6a1fd0.png)
1. **选择计费模式**：选择【包年包月】或【按量付费】。
无法购买按量付费云服务器的用户请先进行 [实名认证](https://console.cloud.tencent.com/developer/infomation)。更多信息请参见 [计费模式说明](https://cloud.tencent.com/document/product/213/2180)。
2. **选择地域和可用区**：当您需要多台云服务器时，选择不同可用区可实现容灾效果。
3. **选择网络类型**：腾讯云提供【基础网络】或【私有网络】两种网络类型可选。
  - 基础网络：同一用户同地域下的服务器默认内网互通，不同地域内网不通。
  - 私有网络：适合更高阶的用户，不同私有网络间逻辑隔离。
>! Windows 云服务器无法作为 [公网网关](https://cloud.tencent.com/document/product/215/20078) 使用，需要公网网关的用户请参见 [自定义配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/10517)。
>
4. **选择机型和配置**
根据底层硬件的不同，腾讯云目前提供了**系列1**和**系列 2**（下文也称为**上一代实例**和**当前一代实例**）两种不同的实例系列，不同的实例系列提供如下实例类型：
 - 上一代实例类型：标准型 S1，高 IO 型 I1，内存型 M1
 - 当前一代实例类型：[标准型 S2](https://cloud.tencent.com/document/product/213/11518#S2)，[高 IO 型 I2](https://cloud.tencent.com/document/product/213/11518#I2)，[内存型 M2](https://cloud.tencent.com/document/product/213/11518#M2)，[计算型 C2](https://cloud.tencent.com/document/product/213/11518#C2)，[GPU 型 G2](https://cloud.tencent.com/document/product/560/11625)，[FPGA 型 FX2](https://cloud.tencent.com/document/product/565/10417) 
为获得最佳性能，我们建议您在新建实例时使用当前一代实例类型。实例类型详细说明，请参见 [实例规格](https://cloud.tencent.com/document/product/213/11518)。
>! 不同的地域与可用区下的系列、机型会有所不同。
>
5. 单击【下一步：选择镜像】，进入选择镜像页面。

## 选择镜像
![](https://main.qcloudimg.com/raw/d85131c0a58d21c86fa7d2eacae317d9.png)
1. **选择镜像提供方**：腾讯云提供公共镜像、自定义镜像、共享镜像、服务市场，您可参考 [镜像类型](https://cloud.tencent.com/document/product/213/4941) 进行选择。
对于刚开始使用腾讯云的用户，推荐选择公共镜像，其中包含了正版 Windows 操作系统，后续运行环境自行搭建。
2. **选择操作系统**：选择【Windows】。
3. **选择镜像版本**
  -  系统内含正版激活，无需额外付费（北美地域除外）。 
  -  适合于运行 Windows 下开发的程序，如 .NET。 
  -  支持 SQL Server 和其他更多数据库（需自行安装）。 
4. 单击【下一步：选择存储与带宽】，进入选择存储与带宽页面。

## 选择存储与带宽

![存储与带宽](https://main.qcloudimg.com/raw/f98d0da08960cc495258247bcc2c588f.png)
1. **选择硬盘类型和数据盘大小**：腾讯云提供云硬盘和本地硬盘两种类型（均默认50GB系统盘，系统盘大小任选）。
 - [云硬盘](https://cloud.tencent.com/document/product/362/2353)：采用一盘三备的分布式存储方式，数据可靠性高
 - 本地硬盘：处在云服务器所在的物理机上的存储设备，可以获得较低的时延，但存在单点丢失风险
2. **选择公网带宽**：腾讯云提供【按带宽计费】或【按使用流量】两种计费方式可选。
  - 按带宽计费：选择固定带宽，超过本带宽时将丢包。适合网络波动较小的场景。
  - 按使用流量计费：按实际使用流量收费。可限制峰值带宽避免意外流量带来的费用，当瞬时带宽超过该值时将丢包。适合网络波动较大的场景。
3. 单击【下一步：设置安全组和主机】，进入设置安全组和主机页面。

## 设置安全组和主机
![安全组和主机](https://main.qcloudimg.com/raw/b3e41aa8064a5e181d20b37b56861136.png)
1. **选择安全组**：**须确保登录端口3389开放**，更多信息请参见 [安全组](https://cloud.tencent.com/document/product/213/12452)。
2. **自定义实例名称**：您可选择创建后命名，也可立即命名。
3. **设置实例的登录密码**：您可设置密码，也可自动生成。设置的密码可在创建后修改，自动生成的密码将会以站内信方式发送。
4. 选择【高级设置】：对实例做更多配置。
![高级设置](https://main.qcloudimg.com/raw/ea9fa0376071c0167038cb02dbf7df4f.png)
 - 主机名：用户可以自定义设置云服务器操作系统内部的计算机名，云服务器成功生产后可以通过登录云服务器内部查看。
 - 置放群组：根据需要可以将实例添加到置放群组中，提高业务的可用性。具体可参考 [置放群组](https://cloud.tencent.com/document/product/213/15486) 进行设置。
 - 标签：设置标签之后可以对云服务器实现资源的分类管理。具体可参考 [标签](https://cloud.tencent.com/document/product/213/19548) 进行设置。
 - 自定义数据：指定自定义数据来配置实例，既当实例启动的时候运行配置的脚本，如果一次购买多台云服务器，自定义数据会在所有的云服务器上运行。Linux 操作系统支持 Shell 格式，Windows 操作系统支持 PowerShell 格式，最大支持 16KB 原始数据。具体可参考 [自定义数据](https://cloud.tencent.com/document/product/213/17525)。
 >! 此项配置仅支持 Windows 公有镜像，具体可参考 [cloudbase-init](https://cloud.tencent.com/document/product/213/19670#cloudbase-init)。
 >
5. 单击【下一步：确认配置信息】，进入确认配置信息页面。

## 确认配置信息

1. 核对购买的云服务器信息。
2. 根据实际需求，选择购买实例的数量，以及购买时长与续费方式（购买时长与续费方式仅限包年包月云服务器）。
7. 单击【立即购买】，完成支付。当您付款完成后，即可进入 [云服务器控制台](https://console.cloud.tencent.com/cvm) 查收您的云服务器。
云服务器的实例名称、公网 IP 地址、内网 IP 地址、登录名、初始登录密码等信息将以 [站内信](https://console.cloud.tencent.com/message) 的方式发送到账户上。您可以使用这些信息登录和管理实例，也请尽快更改您的 Windows 登录密码保障主机安全性。

## 登录及连接实例

当您完成云服务器操作后，您可以尝试通过腾讯云控制台登录您的云服务器，并根据您的实际需求，进行建站等操作。
关于如何通过腾讯云控制台登录云服务器，请根据实际需求，选择相应的登录方式：
- [使用 RDP 文件登录 Windows 实例（推荐）](https://cloud.tencent.com/document/product/213/5435)
- [使用远程桌面连接登录 Windows 实例](https://cloud.tencent.com/document/product/213/35703)

## 格式化与分区数据盘

对于购买了数据盘的用户，需要在登录实例后对数据盘进行格式化和分区。**如果您未购买数据盘，可以跳过此步骤。**
对数据盘进行格式化、分区及创建文件系统等初始化操作，请根据您实际使用场景选择初始化方式：
- 若整块硬盘只呈现为一个独立的分区（即不存在多个逻辑盘，如 D盘和E盘 ），推荐您不使用分区，直接在裸设备上构建文件系统。
- 若整块硬盘需要呈现为多个逻辑分区（即存在多个逻辑盘），则您需要先进行分区操作，再在分区上构建文件系统。

常用的磁盘分区形式有主启动记录分区（Main Boot Record，MBR）和全局分区表（Guid Partition Table，GPT），磁盘投入使用后再切换磁盘分区形式，磁盘上的原有数据将会清除，因此请根据实际需求合理选择分区形式。两种分区形式的简介如下表所示：

| 分区形式 | 支持最大磁盘容量 | 支持分区数量 | 分区工具 |
|---------|---------|---------|---------|
|MBR | 2TB |<li>4个主分区</li><li>3个主分区和1个扩展分区</li>|Windows 操作系统：磁盘管理</br> |
|GPT | 18EB</br>目前云硬盘支持的最大容量为16TB | 不限制分区数量|Windows 操作系统：磁盘管理</br>|

请根据磁盘容量大小、云服务器操作系统类型选择合适的操作指引：
- 磁盘容量小于2TB时：
 - [初始化云硬盘（Windows）](https://cloud.tencent.com/document/product/362/6734#Windows2008)
- 磁盘容量大于等于2TB时：
 - [初始化云硬盘（Windows）](https://cloud.tencent.com/document/product/362/6735#2TBWindows2012)
