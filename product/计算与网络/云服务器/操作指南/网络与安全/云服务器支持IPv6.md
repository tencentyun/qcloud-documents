## 操作场景
本文指导您搭建一个具有 IPv6 CIDR 的云服务器，并为弹性网卡开启 IPv6，实现 IPv6 的内外网通信。
>? 目前弹性公网 IPv6 处于内测中，如有需求，[请提交申请](https://cloud.tencent.com/apply/p/a9k0gialqhj)。
>


## 操作须知

1. 在开始使用腾讯云产品前，您需要先 [注册腾讯云账号](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F)。
2. 目前仅支持如下地域开通弹性公网 IPv6、IPv6 负载均衡、IPv6 私有网络：
广州、深圳金融、上海、上海金融、南京、北京、成都、香港、新加坡、弗吉尼亚。如需使用，请提交 [内测申请](https://cloud.tencent.com/apply/p/c28sebss8v)。
3. IPv6 地址为 GUA 地址，每个 VPC 分配1个`/56`的 IPv6 CIDR，每个子网分配1个`/64`的 IPv6 CIDR，每个弹性网卡分配1个 IPv6 地址。
4. 主网卡、辅助网卡均支持申请 IPv6 地址。想要了解更多云服务器和弹性网卡的关系，请参见 [弹性网卡](https://cloud.tencent.com/document/product/576) 产品文档。
5. 黑石物理服务器2.0不支持在创建实例时配置 IPv6 地址。如需在黑石物理服务器2.0配置此功能，请在创建黑石物理服务器2.0实例后，前往弹性网卡 IPv6 控制台进行开通。详情请参见 [管理 IPv6 公网](https://cloud.tencent.com/document/product/1142/38141)。

## 操作步骤
>? 由于 IPv6 正在内测中，默认不会为云服务器实例配置 IPv6 地址。如果您的云服务器需要开启 IPv6 功能，请先进行手动配置，详情请参考 [快速搭建 IPv6 私有网络](https://cloud.tencent.com/document/product/215/37946)。
> 

### 步骤1：购买云服务器（可选）

>? 如果您已经购买了云服务器，可跳过此步骤。
> 
1. 登录 [腾讯云购买页](http://manage.qcloud.com/shoppingcart/shop.php?tab=cvm&_ga=1.87370846.770173325.1571651505)。
2. 选择机型时，选择支持 IPv6 的地域、网络。
3. 设置主机时，选择支持 IPv6 的安全组，并勾选【免费分配 IPv6 地址】。
>! 如果您所选的网络或安全组未支持 IPv6，请参考 [快速搭建 IPv6 私有网络](https://cloud.tencent.com/document/product/215/37946) 创建满足需求的私有网络和安全组。
>
4. 核对购买的云服务器信息，并完成支付。

<span id="step2_configIPv6"></span>
### 步骤2：云服务器配置 IPv6 地址

不同操作系统的云服务器配置 IPv6 地址具有差异性，详情请参见私有网络提供的如下文档：
-  [Linux 云服务器配置 IPv6](https://cloud.tencent.com/document/product/215/47556)
-  [Windows 云服务器配置 IPv6](https://cloud.tencent.com/document/product/215/47558) 
