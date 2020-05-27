腾讯云为您提供了丰富接入公网的方式，您可以通过普通公网 IP、弹性公网 IP、NAT 网关、负载均衡等访问公网（Internet）。您可通过如下视频了解 VPC 连接 Internet 的相关信息。
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/2354-35383?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

## 普通公网 IP
创建云服务器实例时，您可以选择为实例分配普通公网 IP，系统会为您的云服务器分配一个 IP 地址，使其可以访问公网和被公网访问。 
普通公网 IP 不能与 CVM 等资源动态解绑和绑定，但您可以将普通公网 IP 转换为弹性公网 IP，详细操作请参见 [普通公网 IP 转 EIP](https://cloud.tencent.com/document/product/1199/41706) 。
![](https://main.qcloudimg.com/raw/bf56f0daee011ea0ecbce39bce58a44a.png)

## 弹性公网 IP
弹性公网 IP 是一种可以独立拥有的 IP 资源。相较于公网 IP 仅可跟随云服务器一起申请释放，弹性公网 IP 可以与云服务器的生命周期解耦，作为云资源单独进行操作。 
弹性公网 IP 的申请、绑定、释放操作请参见 [弹性公网 IP-操作指南](https://cloud.tencent.com/document/product/1199/41698)。 
弹性公网 IP 具有如下优势： 
- 独立持有的资源 
弹性公网 IP 可以作为您账户的独立资源，无需与云服务器等绑定购买，可以作为云资源单独操作。 
- 弹性绑定和解绑资源 
弹性公网 IP 可以与云服务器等资源随时绑定、解绑，灵活高可用。 

## NAT 网关
如果您有多台云服务器需要通过一个公网 IP 访问公网，NAT 网关可以满足您的需求。NAT 网关能够为私有网络内的云服务器提供 SNAT 和 DNAT 功能，轻松搭建公网出口、提供服务。 
NAT 网关的相关配置操作，请参见 [NAT 网关-操作总览](https://cloud.tencent.com/document/product/552/12958)。
NAT 网关具有如下优势： 
- 安全的公网访问 
NAT 网关可以为您提供 SNAT 和 DNAT 功能，在满足与公网通信功能的同时，隐藏 VPC 内主机的 IP，有安全保障。 
- 高可用 
NAT 网关双机热备、自动热切换，支持最大5Gbps的转发功能，可以为您大规模公网应用提供支撑。 
- 配置灵活 
您可以根据需求，随时修改 NAT 网关的规格，灵活配置。 

## 负载均衡
负载均衡（Cloud Load Balancer，CLB）是对多台云服务器进行流量分发的服务。负载均衡可以通过流量分发扩展应用系统对外的服务能力，通过消除单点故障提升应用系统的可用性。
负载均衡的购买、配置操作请参见 [负载均衡快速入门](https://cloud.tencent.com/document/product/214/8975 )。
负载均衡具有如下优势： 
- 单集群高性能 
一组 CLB 集群由多台物理服务器组成，可用性高达99.95%。同时集群系统具备剔除故障实例、筛选健康实例的功能，确保后端服务器业务正常运行。
- 安全稳定
CLB 依靠大禹分布式防御系统能够防御绝大多数网络攻击（如 DDoS 等），针对流量攻击实现秒级清洗，极大避免 IP 被封、带宽被占满等情况发生。

## 公网网关
公网网关是开启了转发功能的云服务器。私有网络内没有外网 IP 的云服务器，可通过位于不同子网的公网网关访问 Internet。公网网关服务器将对公网流量进行源地址转换，其它所有云服务器访问 Internet 的流量经过公网网关后，IP 都被转换为公网网关服务器的 IP 地址。
公网网关的相关配置操作，请参见 [配置公网网关](https://cloud.tencent.com/document/product/215/38616)。
