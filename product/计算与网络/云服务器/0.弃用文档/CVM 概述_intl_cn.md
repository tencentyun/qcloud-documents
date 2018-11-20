## 简介
腾讯云云服务器 (Cloud Virtual Machine，CVM) 是在云中提供可扩展的计算服务，避免了使用传统服务器时需要预估资源用量及前期投入的情况。通过使用腾讯云 CVM ，您可以在短时间内快速启动任意数量的云服务器并即时部署应用程序。腾讯云 CVM 支持用户自定义一切资源：CPU、内存、硬盘、网络、安全等等，并可在访问量和负载等需求发生变化时轻松地调整它们。

## 相关概念
了解腾讯云 CVM 时，通常会涉及到以下概念：

- [**实例**](/doc/product/213/4939)：云上的虚拟计算资源。

- [**实例类型**](/doc/product/213/7153)：实例在CPU、内存、存储和网络等配置上的不同搭配。

- [**镜像**](/doc/product/213/4940)：实例预置模版，包含服务器的预配置环境（操作系统和其他已安装的软件）。

- [**本地盘**](/doc/product/213/5798)：与实例处于同一台物理服务器上的，可被实例用作持久存储的设备。

- [**云硬盘**](/doc/product/213/4953)：提供的分布式持久块存储设备，可以用作实例的系统盘或可扩展数据盘使用。


- [**私有网络**](/doc/product/215/4927)：自定义的虚拟网络空间，与其他资源逻辑隔离。

- **IP 地址**：实例对内和对外的服务地址，也即 [内网 IP 地址](/doc/product/213/5225) 和 [公网 IP 地址](/doc/product/213/5224) 。

- [**弹性 IP**](/doc/product/215/5733)：专为动态网络设计的静态公网 IP，满足快速排障需求。

- [**安全组**](/doc/product/213/5221)：对实例进行安全的访问控制，指定进出实例的IP、协议及端口规则。

- **登录方式**：安全性高的 [SSH 密钥对](/doc/product/213/6092) 和普通密码的 [登录密码](/doc/product/213/6093) 。

- [**地域和可用区**](/doc/product/213/6091)：实例和其他资源的启动位置。

- [**腾讯云控制台**](https://console.cloud.tencent.com)：基于 Web 的用户界面。


## 相关服务

- 您可以使用一个预设模版来启动新的云服务器。预设模版可以包含任何您希望在初始化时就包含在云服务器中的环境或应用程序。腾讯云提供大量经审核的第三方预设模版，帮助用户快速搭建环境。更多信息，请参考[服务市场](http://market.cloud.tencent.com/)。

- 您可以使用弹性伸缩定时或根据条件地自动增加及减少服务器集群数量。更多信息，请参考 [弹性伸缩产品文档](https://cloud.tencent.com/doc/product/377)。

- 您可以使用负载均衡横跨多个云服务器实例自动分配来自客户端的请求流量。更多信息，请参考 [负载均衡产品文档](https://cloud.tencent.com/doc/product/214)。

- 您可以使用容器服务管理在一组云服务器的应用生命周期。更多信息，请参考 [容器服务产品文档](https://cloud.tencent.com/doc/product/457)。


- 您可以使用云监控服务监控云服务器实例及其系统盘。更多信息，请参考 [云监控产品文档](https://cloud.tencent.com/doc/product/248)。

- 您可以在云上部署关系数据库，也可以使用腾讯云云数据库。更多信息，请参考[云数据库MySQL](https://cloud.tencent.com/doc/product/236)。

- 您可以编写代码调用腾讯云 API 访问腾讯云云的产品和服务，更多信息，请参考[腾讯云 API 文档](https://cloud.tencent.com/document/api)。


## 使用 CVM

腾讯云 CVM 提供基于 Web 的用户界面，即控制台，如果您已注册腾讯云账户，您可以直接登录 [ CVM 控制台](https://console.cloud.tencent.com/cvm)，对您的 CVM 进行操作。

腾讯云 CVM 也提供了 API 接口方便您管理云服务器 CVM，有关 CVM API 操作的更多信息，请参阅 [API 文档](https://cloud.tencent.com/document/api/213/568)。

您可以使用 SDK（支持 PHP/Python/Java/.NET/Node.js）编程或使用腾讯云命令行工具调用 CVM API，具体请参考：

- [使用 SDK >>](https://cloud.tencent.com/document/developer-resource)

- [使用命令行工具 >>](https://cloud.tencent.com/document/product/440/6317)

## CVM 定价
CVM 支持包年包月和按量付费。更多信息，请参考 [ CVM 实例价格](/doc/product/213/2176) 。

CVM 及相关资源的价格信息，请参考 [定价中心](https://buy.cloud.tencent.com/price/cvm) 。

