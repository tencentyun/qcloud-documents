##  托管简单网站
您可以像使用普通网络一样使用私有网络，部署简单的web应用，如博客、网站和日志系统等。通过[安全组](https://cloud.tencent.com/doc/product/213/500)和[网络ACL](https://cloud.tencent.com/doc/product/215/5132)等防火墙，您可以使web应用响应HTTP等请求，但拒绝web应用访问Internet，从而保证web应用的安全。在流量突增时，您还可以在VPC的中启用[负载均衡](https://cloud.tencent.com/doc/product/214/524)轻松应对。
![](//mccdn.qcloud.com/static/img/23729e8b1f865148f8851e82db3cfff5/image.png)
>相关产品：[云服务器（CVM）](https://cloud.tencent.com/doc/product/213/495)、[云数据库](https://cloud.tencent.com/doc/product/236)、[负载均衡](https://cloud.tencent.com/doc/product/214/524)

##  托管多层 Web 应用
您可以在私有网络内创建不同子网，整个web层放在一个子网，通过配置[弹性IP](https://cloud.tencent.com/doc/product/213/1941)/[公网网关](https://cloud.tencent.com/doc/product/215/4972)/[NAT网关](https://cloud.tencent.com/doc/product/215/4975)对外通信，逻辑层单独放在一个子网，只能和web层及数据层通信，数据层放在另外一个子网，只和逻辑层通信，子网和子网之间的流量通过[网络ACL](https://cloud.tencent.com/doc/product/215/5132)进行控制。腾讯云私有网络可以在给您的应用提供Internet服务的同时，又保障数据库服务器的安全，您可以安全灵活地在腾讯云VPC中托管多层Web应用程序。
![](//mccdn.qcloud.com/static/img/64ac36b8359811995205cba91f788c85/image.png)
>相关产品：[云服务器（CVM）](https://cloud.tencent.com/doc/product/213/495)、[云数据库](https://cloud.tencent.com/doc/product/236/3188)、[弹性IP](https://cloud.tencent.com/doc/product/213/1941)、[NAT网关](https://cloud.tencent.com/doc/product/215/4975)、[公网网关](https://cloud.tencent.com/doc/product/215/4972)

##  弹性混合云部署
您可以在私有网络内部署您的应用程序，在您的企业数据中心部署数据库服务器。腾讯云私有网络提供稳定安全的[IPsec VPN](https://cloud.tencent.com/doc/product/215/4956)/[专线](https://cloud.tencent.com/doc/product/215/4976)帮您打通企业数据中心与云端资源。您可使用[弹性伸缩](https://cloud.tencent.com/doc/product/377/3154)服务实现根据业务量弹性扩展应用程序的云服务器等资源，既降低了企业IT运维成本，又不用担心企业核心数据的扩散，轻松实现弹性混合云部署。
![](//mccdn.qcloud.com/static/img/23ac09921e7876e6d33d75704dc7f6db/image.png)
>相关产品：[云服务器（CVM）](https://cloud.tencent.com/doc/product/213/495)、[云硬盘（CBS）](https://cloud.tencent.com/doc/product/362/2345)、[弹性伸缩（AS）](https://cloud.tencent.com/doc/product/377/3154)、[专线接入](https://cloud.tencent.com/doc/product/215/4976)、[VPN连接](https://cloud.tencent.com/doc/product/215/4956)
