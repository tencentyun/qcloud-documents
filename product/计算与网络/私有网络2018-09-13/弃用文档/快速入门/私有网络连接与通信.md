私有网络是您的一个逻辑独立的网络空间，它各个子网内的资源默认内网互通，但与其它的私有网络、Internet 等均默认不互通。如果您需要将您某个私有网络内的资源与其他资源互通，我们为您提供了多种的连接方式，如下图所示：
![](https://main.qcloudimg.com/raw/dbb768c0bae33a5797df9151faea4cda.png)

## 与 VPC 内资源通信
同一个私有网络内的所有资源默认内网互通，每个路由表中都会有一条 [Local,Local,Local] 的默认路由，表示该私有网络内云服务器（也包括云数据库、云存储等）资源都互通。
![](https://main.qcloudimg.com/raw/54acb50cd3f3d5ba9774aa12890f2612.png)

## 与其它 VPC 通信
不同私有网络间默认内网隔离，您可以通过以下方式实现连接其它 VPC（同账号/跨账号）内的服务资源：
- [对等连接](https://cloud.tencent.com/document/product/553)：可以使两个私有网络内资源内网互通，但要求两端 VPC 的网段不重叠。
- [云联网](https://cloud.tencent.com/document/product/877)：可以使两个或多个私有网络内资源内网互通，要求互通子网的网段不重叠。

## 与 Internet 通信
私有网络需要借助网关或 IP 才能访问 Internet，您可以通过以下方式实现与 Internet 的通信：
- [NAT 网关](https://cloud.tencent.com/document/product/552)：通过绑定弹性 IP，可以使子网内的云服务器安全地访问 Internet 和被访问。
- [弹性公网 IP](https://cloud.tencent.com/document/product/215/20080)：可以绑定在 NAT 网关或云服务器上，实现访问 Internet 的功能。
- [负载均衡](https://cloud.tencent.com/document/product/214)：提供安全快捷的流量分配服务，可以无缝提供分配应用程序流量所需的负载均衡容量。
- [公网网关](https://cloud.tencent.com/document/product/215/20078)：实质是有公网 IP 且具有转发功能的云服务器，可以为位于不同子网内的无公网 IP 云服务提供访问 Internet 的功能。

## 与基础网络通信
区别于私有网络逻辑隔离的网络结构，基础网络是腾讯云上所有用户公共网络资源池。所有云服务器的内网 IP 地址都由腾讯云统一分配，虽然简易但无法自定义。
腾讯云提供了基础网络和私有网络互联的方式：
- [基础网络互通](https://cloud.tencent.com/document/product/215/20083)：提供基础网络内云服务器和私有网络内云服务器、云数据库等资源的互联服务，但对私有网络网段等有一定限制，详情请参见 [使用限制](https://cloud.tencent.com/document/product/215/20083#.E4.BD.BF.E7.94.A8.E7.BA.A6.E6.9D.9F)。

## 通信安全性
私有网络在与外部资源建立连接时，内部资源会有一定安全风险，腾讯云提供不同维度的网络防火墙，保障您的网络安全：
- [安全组](https://cloud.tencent.com/document/product/215/20089)：实例级别（云服务器、云数据库等）的网络访问控制，只有被关联到指定云服务器时才会被应用。
- [网络 ACL](https://cloud.tencent.com/document/product/215/20088) ：子网级别的网络访问控制，会被应用于一个子网内的所有云服务器。
