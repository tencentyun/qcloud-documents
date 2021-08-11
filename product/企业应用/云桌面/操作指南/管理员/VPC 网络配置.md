云桌面创建前需要选择 [私有网络VPC](https://cloud.tencent.com/document/product/215)，将云桌面资源放置在您的专属云上网络空间中，以提升云上云桌面资源的安全性，并满足不同的应用场景需求。
基于 VPC 配置云桌面的网络，可以实现云桌面与其他业务或者云产品互访、云桌面的公网访问和云桌面跨 VPC 访问。
## VPC 网络创建

云桌面需要结合VPC使用，请提前准备满足需求的腾讯云 VPC 网络，您可以参见 [私有网络创建指南](https://cloud.tencent.com/document/product/215/36515) 新建您的私有网络。云桌面创建完成后所属私有网络/子网无法变更。

## 云桌面访问其他 VPC 资源
### 对等链接
您可以通过 [对等链接](https://cloud.tencent.com/document/product/553)（Peering Connection）实现云桌面访问另**一个 VPC**，对等连接支持同账号 VPC 互通和跨账号 VPC 互通，可以参见以下链接为您的云桌面创建对等连接。
- [同账号创建对等连接通信](https://cloud.tencent.com/document/product/877/30804)
- [跨账号创建对等连接通信](https://cloud.tencent.com/document/product/553/18837)

### 云联网
您可以通过 [云联网](https://cloud.tencent.com/document/product/877)（Cloud Connect Network，CCN）实现云桌面访问**两个及以上的 VPC**，云联网支持同账号 VPC 互通和跨账号 VPC 互通，可以参见以下链接为您的云桌面实施云联网。
- [同账号网络实例互通](https://cloud.tencent.com/document/product/877/30804)
- [跨账号网络实例互通](https://cloud.tencent.com/document/product/877/30805)

## 云桌面通过 NAT 网关访问互联网
[NAT 网关](https://cloud.tencent.com/document/product/552) 是一种 IP 地址转换服务，可以绑定 [弹性公网 IP（EIP）](https://cloud.tencent.com/document/product/1199)为私有网络（VPC）内的云桌面提供安全、高性能的 Internet 访问服务。
>?NAT 网关的创建请正确选择所属VPC，关联配置路由规则，将子网流量指向 NAT 网关。

关于NAT 网关的配置指南，请参见：
- [NAT 网关快速入门](https://cloud.tencent.com/document/product/552/18186)
- [修改 NAT 网关配置](https://cloud.tencent.com/document/product/552/18179)
- [管理 NAT 网关的弹性 IP](https://cloud.tencent.com/document/product/552/18180)
- [管理 SNAT 规则](https://cloud.tencent.com/document/product/552/52323)
- [管理端口转发规则](https://cloud.tencent.com/document/product/552/53621)
- [配置指向 NAT 网关的路由](https://cloud.tencent.com/document/product/552/19697)
