本文指导您通过专线接入 + 私有 NAT 网关的 SNAT 和 DNAT 功能，实现本地数据中心 IDC（Internet Data Center）与云上地址的资源访问。
>?
>- NAT 型专线网关 V3R2 版本目前处于内测中，如有需要，请联系 [在线支持](https://cloud.tencent.com/online-service?from=sales&source=PRESALE)。
>- 私网 NAT 网关功能目前处于内测中，如有需要，请联系 [在线支持](https://cloud.tencent.com/online-service?from=sales&source=PRESALE)。
>

## 业务场景
用户使用专线打通腾讯云和客户 IDC 实现资源访问，同时期望指定访问 IP 地址并无 IP 冲突，可以通过私网 NAT + 专线方案来实现。
![](https://qcloudimg.tencent-cloud.cn/raw/eed46c83d8dcb6747d2a2bc26f85168c.png)

## 前提条件
- 已完成物理专线建设，详情可参见 [申请接入物理专线](https://cloud.tencent.com/document/product/216/48586)。
- 已 [创建 VPC](https://cloud.tencent.com/document/product/215/36515)。

## 注意事项
- 私网 NAT 网关需要配置网络地址映射关系，不配业务将不通。
- 在私网 NAT 中配置的 SNAT 本端三层、SNAT 本端四层和 DNAT 对端四层会自动产生映射关系；对端三层不会产生 NAT 映射关系。同时由于默认不发布 VPC CIDR，因此如果单独使用对端三层规则，需要在 IDC 侧手动配置 VPC CIDR 路由才能通，推荐和本端搭配使用。

## 操作步骤
### 步骤一：创建私网 NAT 网关[](id:step1)
1. 登录 [NAT 网关控制台](https://console.cloud.tencent.com/vpc/nat?rid=1)。
2. 在左侧导航栏单击 **NAT 网关** > **私网 NAT 网关**，选择地域和所在私有网络，单击**新建**。
3. 填写如下配置信息，单击**立即开通**。
![](https://qcloudimg.tencent-cloud.cn/raw/bb4407161c72e3af956979d7d367e633.png)
>?更多详细配置可参考 [NAT 网关](https://cloud.tencent.com/document/product/552)。
>


### 步骤二：创建 NAT 型专线网关
1. 登录 [专线网关控制台](https://console.cloud.tencent.com/vpc/dcgw?rid=8)。
2. 在**新建专线网关**页面填写**网关名称**、**可用区**、**关联网络**选择 NAT 网络，并关联相应的 NAT 实例。
3. 勾选清理冗余网关协议，单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/886d7c8e6ea89653094194a622684de6.png)
>?更多详细配置，请参见 [创建专线网关](https://cloud.tencent.com/document/product/216/19256)。
>

### 步骤三：创建专用通道
物理专线接入方式不同，则在其上创建的通道不同。可按实际需求选择创建如下一种专用通道：
- 使用自主独占型物理专线创建的通道为独占型专用通道，即独占专用通道，适用于大带宽接入、业务独享等场景，创建详情请参见 [独享专用通道](https://cloud.tencent.com/document/product/216/74769)。
- 使用合作伙伴与腾讯预连接的物理专线创建的专用通道为共享型专用通道，即共享专用通道，适用于无大带宽入云需求、上云时间要求较短的场景，创建详情请参见 [共享专用通道](https://cloud.tencent.com/document/product/216/74570)。

### [](id:step4)步骤四：配置私网 NAT 网关 SNAT 和 DNAT 条目
1. 登录 [NAT 网关控制台](https://console.cloud.tencent.com/vpc/nat?rid=1)，在左侧导航栏选择私网 NAT 网关，单击已创建私网 NAT 网关 ID。
2. 在**私网 NAT 网关详情**页面，在 **SNAT** 和 **DNAT** 页签配置 SNAT 和 DNAT 规则，本例以 SNAT 为例。
![](https://qcloudimg.tencent-cloud.cn/raw/9d532a6c65e50eb32963e3ad07141d6c.png)
3. 在 SNAT 页签，单击**新建**，在**添加 SNAT 规则**页面**映射类型**选择**三层**，原 IP 配置为云上 IP，**映射 IP/映射 IP 池**选择您需要指定的 IP 地址或者 IP 池。
![](https://qcloudimg.tencent-cloud.cn/raw/3bed158a74652637fb0de397888e27de.png)
如果一次需要配置多条 SNAT 规则，可单击**新增一行**进行添加。
4. 单击**确定**。
>?更多详细配置请参见 [操作总览](https://cloud.tencent.com/document/product/552/12958)。
>

### [](id:step5)步骤五：配置 VPC 路由表路由策略
1. 登录 [路由表控制台](https://console.cloud.tencent.com/vpc/route?rid=1)。
2. 在**路由表**页面找到您 VPC 对应的路由表，进入路由表详情页面。
![](https://qcloudimg.tencent-cloud.cn/raw/ca39e93e4bbe5460e83b431752627ecf.png)
3. 单击**新增路由策略**并进行路由策略配置。
**目的端**为您本地 IDC 网段，**下一跳类型**为**私网 NAT 网关**，**下一条**为 [步骤一](#step1) 创建的私网 NAT 网关。
![](https://qcloudimg.tencent-cloud.cn/raw/e82b1ab022bc7a5379cd2cfe4410c1c8.png)
>?更多私有网络策略，请参考 [管理路由策略](https://cloud.tencent.com/document/product/215/53587)。
>


### 步骤六：配置本地 IDC
通道创建最后一步时，请单击下载配置指引：下载 CPE 配置指引文件，按照文件中提供的几款通用厂商的配置方法进行配置。
>?更多详细配置请参考 [独享专用通道](https://cloud.tencent.com/document/product/216/74769#step4)。
>

### 步骤七：测试联通性
测试云上 CVM 实例是否与本地 IDC 互访。
1. 登录您 VPC 内的 CVM。
2. 使用 ping 命令 ping 您本地 IDC 内服务器 IP 地址，如果能收到 icmp 回包，则说明 CVM 与 IDC 已连通。
   在您本地 IDC 服务器执行抓包命令，可以查看报文源 IP 为 SNAT 后指定的 IP 地址。
>?如果没有收到回包，排查意见如下：
>- 检查 vpc 路由表，是否配置了下一跳指向“私网 NAT 网关”的路由，详情可参见 [步骤五](#step5)。
>- 检查私网 NAT 网关是否配置了 SNAT 或者 DNAT 规则，如果均没有配置，则默认不通。配置详情可参见 [步骤四](#step4)。
>- 检查专用通道状态，连接状态必须为**已连接**。2.0的通道 BGP 状态必须为 **established**。
>- 如果以上情况都不是，请联系腾讯云 [在线支持](https://cloud.tencent.com/online-service)。
>
3. 登录您本地 IDC 服务器地址，执行 `ssh root@NAT IP` 命令。
   如果能接收到回复报文，则表示连接成功。
