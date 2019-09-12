
如果您是首次购买和使用云服务器实例的个人用户，腾讯云推荐您按照本文档进行配置、购买和连接实例。本文档主要介绍如何快速使用 Windows 系统的云服务器实例的相关功能，引导您快速了解腾讯云云服务器的创建和配置。

## 快速入门流程
![](https://main.qcloudimg.com/raw/1eb3c146a5908f03397ef4ee88fed390.png)

>? 腾讯云提供**快速配置**和**自定义配置**两种方式。本文档以快速配置为例进行说明。若快速配置不能满足您的需求，您可参考 [自定义配置 Windows 云服务器](https://cloud.tencent.com/doc/product/213/10516) 文档进行配置。

## 步骤一：准备工作
在使用云服务器之前，您需要完成以下准备工作：
1. 注册腾讯云账号，并完成实名认证。
新用户需在腾讯云官网进行 [注册](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F)，具体操作可参考 [注册腾讯云](https://cloud.tencent.com/doc/product/378/9603)。
2. 访问 [腾讯云云服务器介绍页面](https://cloud.tencent.com/product/cvm)，单击【立即选购】。

## 步骤二：配置选型

>! 对于初次购买的账户，默认进入【快速配置】页面。对于已购买过云服务器的用户，默认进入【自定义配置】页面。若您已购买过云服务器，请选择【快速配置】进行快速配置操作。
>
![](https://main.qcloudimg.com/raw/1ec1a6e1071c7fa52f7c733ba1b0cf6b.png)

### 选择云服务器所在地域及可用区

请根据以下原则，选择地域，例如华北地区。可用区默认随机分配。
- 靠近用户原则
  请根据您的用户所在地理位置选择云服务器地域。云服务器越靠近访问用户，越能获得较小的访问时延和较高的访问速度。
- 内网通信同地域原则
详情请参见 [私有网络连接与通信](https://cloud.tencent.com/document/product/215/30717)。

### 选择云服务器机型

| 类型 | 实例规格 | 云硬盘 | 适用场景 |
|---------|---------|---------|---------|
| 入门配置 | 系列2：标准型1核 CPU、1G内存 | 50G高性能云硬盘 | 适用于起步阶段的个人网站，例如个人博客等小型网站。对于个人用户，腾讯云推荐您使用**入门配置**。 |
| 基础配置 | 系列2：标准型1核 CPU、2G内存 | 50G高性能云硬盘 | 适用于有一定访问量的网站或 APP，例如较大型企业官网、小型电商网站。 |
| 普及配置 | 系列2：标准型2核 CPU、4G内存 | 50G高性能云硬盘 | 适用于并发适中的 APP 或普通数据处理，例如门户网站、SaaS 软件、小型 APP。 |
| 专业配置 | 系列2：标准型4核 CPU、8G内存 | 50G高性能云硬盘 | 适用于并发要求较高的应用及适合对云服务器网络及计算性能有一定要求的应用场景，例如大型门户、电商网站、游戏 APP。 |

如果您需要了解更多云服务器的规格信息，如云服务器类型、使用场景、使用须知，请参见 [实例规格](https://cloud.tencent.com/document/product/213/11518)。


### 选择镜像

本文介绍 Windows 实例的购买及登录，请选择 Windows 提供镜像。
![](https://main.qcloudimg.com/raw/f26a5d9f1b0d2c8f1f04975c19c2aff4.png)
>! Windows 云服务器无法作为 [公网网关](https://cloud.tencent.com/document/product/215/20078) 使用，需要公网网关的用户请参考 [快速入门 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。
>


### 配置网络

腾讯云云提供了默认安全组，自动免费公网 IP 给云服务器。


### 选择购买数量和时长

根据实际需求，选择购买实例的数量，以及购买时长。

### 核对信息并购买

核对购买的云服务器信息，并完成支付。
>! 快速配置的用户，腾讯云只提供**包年包月**的付费方式。
> 完成购买后，云服务器的实例名称、公网 IP 地址、内网 IP 地址、登录名、初始登录密码等信息将以 [站内信](https://console.cloud.tencent.com/message) 的方式发送到账户上。
> 

## 步骤三：登录云服务器实例

1. 在 [云服务器控制台](https://console.cloud.tencent.com/cvm/index) 的实例管理页面，选择待登录的云服务器实例，单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/96689027b98d8fc6bfb00036de7a87f8.png)
2. 根据实际需求，选择相应的登录方式。
 - [使用 RDP 文件登录 Windows 实例（推荐）](https://cloud.tencent.com/document/product/213/5435)
 - [使用远程桌面连接登录 Windows 实例](https://cloud.tencent.com/document/product/213/35703)
 - [使用 VNC 登录 Windows 实例](https://cloud.tencent.com/document/product/213/35704)

## 步骤四：格式化与分区数据盘（可选）
>! 对于购买了数据盘的用户，需要在登录实例后对数据盘进行格式化和分区。**若您未购买数据盘，可跳过此操作步骤。**
> 使用快速配置购买的云服务器，默认不购买数据盘，无需执行此操作步骤。
> 
参考 [Windows 实例数据盘分区及格式化](https://cloud.tencent.com/document/product/213/10516#.E6.A0.BC.E5.BC.8F.E5.8C.96.E4.B8.8E.E5.88.86.E5.8C.BA.E6.95.B0.E6.8D.AE.E7.9B.98)，对 Windows 实例进行数据盘分区及格式化。

