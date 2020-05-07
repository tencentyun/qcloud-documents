## 操作场景
本文指导您搭建一个具有 IPv6 CIDR 的云服务器，并为弹性网卡开启 IPv6，实现 IPv6 的内外网通信。
>? 目前弹性公网 IPv6 处于内测中，如有需求，[请提交申请](https://cloud.tencent.com/apply/p/c28sebss8v)。
>

## 操作须知

1. 在开始使用腾讯云产品前，您需要先 [注册腾讯云账号](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F)。
2. 目前支持 IPv6 的地域为北京、上海、广州、上海金融云、深圳金融云，请在这些地域部署 IPv6 服务。
3. IPv6 地址为 GUA 地址，每个 VPC 分配1个`/56`的 IPv6 CIDR，每个子网分配1个`/64`的 IPv6 CIDR，每个弹性网卡分配1个 IPv6 地址。
4. 主网卡、辅助网卡均支持申请 IPv6 地址。想要了解更多云服务器和弹性网卡的关系，请参见 [弹性网卡](https://cloud.tencent.com/document/product/576) 产品文档。

## 操作流程
![](https://main.qcloudimg.com/raw/8ffaec34d26b62c1e3e2430143e5b8f0.jpg)

## 操作步骤

### 步骤1：快速搭建 IPv6 私有网络

#### VPC 分配 IPv6 CIDR

1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在需要开启 IPv6 的 VPC 所在行的操作栏下，单击【编辑 CIDR】。
3. 在弹框中的 “IPv6 CIDR” 单击【获取】并确认操作。如下图所示：
系统将为 VPC 分配一个`/56`的 IPv6 地址段，您可以在列表里看到 IPv6 地址段的详细信息。
![1575385168032](https://main.qcloudimg.com/raw/06cc0c14dc28e511492d5f1b5cb01f32.png)

#### 为子网分配 IPv6 CIDR

1. 单击刚才设置 IPv6 CIDR 的私有网络 ID，进入该私有网络的详情页面。
2. 在网络资源中，单击【子网】，进入子网管理页面。如下图所示：
![1575385318324](https://main.qcloudimg.com/raw/eb2ea423d6382bd2d557aba62f3e8f27.png)
3. 在需要开启 IPv6 的子网所在行的操作栏下，单击【获取 IPv6 CIDR】并确认操作。如下图所示：
系统将从 VPC 的`/56` IPv6 CIDR 分配一个`/64`的 IPv6 CIDR。
![1575385402233](https://main.qcloudimg.com/raw/d3d8fcaa9c336dac11485d5f7ed95a92.png)

#### 弹性网卡获取 IPv6 地址

1. 在左侧导航栏中，选择【IP 与网卡】>【弹性网卡】，单击需要获取 IPv6 地址的弹性网卡 ID，进入详情页。
2. 选择【IPv6 地址管理】标签页，单击【分配 IP】。如下图所示：
![img](https://main.qcloudimg.com/raw/3988ff4d36229c8ce99a9276875204a9.png)
3. 在弹窗中，单击【确定】。如下图所示：
![img](https://main.qcloudimg.com/raw/737f2b30db0766ebf09ce99f2bdc4e01.png)
4. 系统将会为弹性网卡分配一个 IPv6 地址。如下图所示：
![img](https://main.qcloudimg.com/raw/309e8e9d70b69ddb4c70a0ead71f7862.png)

#### 为弹性网卡的 IPv6 地址开通公网

>?
> - 当运营商类型为 BGP 时，弹性公网 IPv6 地址即为弹性网卡获取到的 IPv6 地址。因此，请确保弹性网卡已获取到 IPv6 地址。
> - 单次操作可支持最多100个 IPv6 地址同时开通公网，如果超过100个 IPv6 地址需要开通公网，请分多次操作。
> - 弹性公网 IPv6 只对公网带宽流量计费，弹性公网 IPv6 地址不收取费用。
> 
1. 在左侧导航栏中，选择【IP 与网卡】>【弹性公网 IPv6】。
2. 选择需要开通 IPv6 公网的地域，如“广州”，单击【申请】，进入管理页面。
3. 勾选需要开通 IPv6 公网的 IPv6 地址、设置目标带宽上限，单击【提交】即可。
![](https://main.qcloudimg.com/raw/f66f01c4b1a0791f956663188e2b702b.png)

#### 配置 IPv6 的安全组规则

>? 出入方向的安全组规则支持配置来源为单个 IPv6 地址或者 IPv6 CIDR，其中`::/0`代表所有的 IPv6 源地址。
>
1. 在左侧导航栏中，选择【安全】>【安全组】，进入安全组管理页面。
2. 在安全组列表中，单击云服务器需要绑定的安全组 ID，进入详情页。
2. 选择【入站规则】并单击【添加规则】，添加 IPv6 的入方向安全组规则，单击【完成】。
![img](https://main.qcloudimg.com/raw/73ff04af93a1f13eef92d4f74ac30fc2.png)
3. 选择【出站规则】并单击【添加规则】，添加 IPv6 的出方向安全组规则，单击【完成】。
![img](https://main.qcloudimg.com/raw/c0d255728fa6b48292f425c5ffb6559f.png)

### 步骤2：购买云服务器 CVM

>? 由于 IPv6 正在公测中，默认不会为云服务器实例配置 IPv6 地址。如需开启 IPv6 功能，请进行手动配置。
> 
1. 登录 [腾讯云购买页](http://manage.qcloud.com/shoppingcart/shop.php?tab=cvm&_ga=1.87370846.770173325.1571651505)。
2. 选择机型时，选择支持 IPv6 的地域、网络。
3. 设置主机时，选择支持 IPv6 的安全组，并勾选【免费分配 IPv6 地址】。
4. 核对购买的云服务器信息，并完成支付。

### 步骤3：云服务器配置 IPv6 地址

不同操作系统的云服务器配置 IPv6 地址具有差异性，详情请参见 [Linux 云服务器开启 IPv6](https://cloud.tencent.com/document/product/215/37946#CentOS6.8) 和 [Windows 云服务器开启 IPv6](https://cloud.tencent.com/document/product/215/37946#Windows2012)。





