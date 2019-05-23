
如果您是首次购买和使用云服务器实例的个人用户，腾讯云推荐您按照以下流程快速配置、购买和连接实例。
![](https://main.qcloudimg.com/raw/37ade775b8f369f5bf673dd4e69090cf.png)
本文档主要介绍如何快速使用 Linux 系统的云服务器实例的相关功能，引导您快速了解腾讯云云服务器的创建和配置。
>? 腾讯云提供**快速配置**和**自定义配置**两种方式。本文档以快速配置为例进行说明。若快速配置不能满足您的需求，您可参考 [自定义配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/10517) 文档进行配置。

## 1. 注册账号与选型

新用户需在腾讯云官网进行 [注册](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F)。注册指引可参考 [如何注册腾讯云](https://cloud.tencent.com/doc/product/378/9603) 。
![](https://main.qcloudimg.com/raw/1ec1a6e1071c7fa52f7c733ba1b0cf6b.png)

### 确定付费方式

腾讯云提供**包年包月**和**按量付费**两种付费模式，对于选择快速配置的用户，腾讯云只提供**包年包月**的付费方式。

## 2. 快速配置及购买 CVM 实例

### 确定云服务器所在地域及可用区

地域选择原则：
- 靠近用户原则
  请根据您的用户所在地理位置选择云服务器地域。云服务器越靠近访问客户，越能获得较小的访问时延和较高的访问速度。
- 内网通信同地域原则
  详情请参见 [私有网络连接与通信](https://cloud.tencent.com/document/product/215/30717)。

### 确定云服务器配置方案

对于个人用户，腾讯云推荐您使用**入门配置**。
- **入门配置**：适用于起步阶段的个人网站。例如个人博客等小型网站。

或者根据需求您可以选择：
- **基础配置**：适合有一定访问量的网站或应用。例如较大型企业官网、小型电商网站。
- **普及配置**：适合常使用云计算等一定计算量的需求。例如门户网站、SaaS 软件、小型 App 。
- **专业配置**：适用于并发要求较高的应用及适合对云服务器网络及计算性能有一定要求的应用场景。例如大型门户、电商网站、游戏 App 。

若推荐的配置不能满足您的需求，您可以在 [更多机型](https://buy.cloud.tencent.com/cvm?tabIndex=1) 中根据实际需要比较各配置方案。当然您也可以在购买云服务器之后，根据您的需求随时进行 [配置升级](https://cloud.tencent.com/doc/product/213/%E8%B0%83%E6%95%B4CVM%E5%AE%9E%E4%BE%8B%E9%85%8D%E7%BD%AE#1.-%E9%85%8D%E7%BD%AE%E5%8D%87%E7%BA%A7) 或 [配置降级](https://cloud.tencent.com/doc/product/213/%E8%B0%83%E6%95%B4CVM%E5%AE%9E%E4%BE%8B%E9%85%8D%E7%BD%AE#2.-%E9%85%8D%E7%BD%AE%E9%99%8D%E7%BA%A7) 。

### 选择镜像
本文介绍 Linux 实例的购买及登录，请选择 Linux（CentOS 或 Ubuntu）提供镜像。
![](https://main.qcloudimg.com/raw/e7dabdf30f673cfd33548788f8816319.png)
完成云服务器的购买和创建后，云服务器的实例名称、公网 IP 地址、内网 IP 地址、登录名、初始登录密码等信息都将以 [站内信](https://console.cloud.tencent.com/message) 的方式发送到账户上。
![](https://main.qcloudimg.com/raw/3e9630ea483d4154d58187091d51cecf.png)

## 3. 登录及连接 CVM 实例

配置及购买实例后，您购买的实例会显示在控制台的实例列表中，选择您需要登录的实例，单击右侧【登录】。
![](https://main.qcloudimg.com/raw/96689027b98d8fc6bfb00036de7a87f8.png)
根据您实例的类型，可以参考 [连接及登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)，选择相应的连接与登录方式进行远程登录 CVM 实例。

## 4. 格数据盘分区及格式化（可选）
对于购买了数据盘的用户，需要在登录实例后对数据盘进行格式化和分区。**未购买数据盘的用户可以跳过此步骤。**
>! 使用快速配置购买的云服务器默认没有购买数据盘，不需要执行此步骤操作。
>
具体操作请参考 [ Linux 实例数据盘分区及格式化](https://cloud.tencent.com/document/product/213/10517#.E6.95.B0.E6.8D.AE.E7.9B.98.E5.88.86.E5.8C.BA.E5.8F.8A.E6.A0.BC.E5.BC.8F.E5.8C.96) 对 Linux 实例进行数据盘分区及格式化。

