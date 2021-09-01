>?
>- IPv6 负载均衡内测中，如需使用，请提 [工单申请](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=163&source=0&data_title=%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%20LB&step=1)。
>- 目前仅支持如下地域开通 IPv6 负载均衡：广州、深圳金融、上海、上海金融、南京、北京、成都、香港、新加坡、弗吉尼亚。其中，针对地域为**深圳金融**、**上海金融**的金融行业监管要求定制的合规专区，需提交 [工单申请](https://console.cloud.tencent.com/workorder/category) 使用专区。
>- IPv6 负载均衡不支持传统型负载均衡。
>- IPv6 负载均衡支持获取客户端 IPv6 源地址。四层 IPv6 负载均衡支持直接获取客户端 IPv6 源地址，七层 IPv6 负载均衡支持通过 HTTP 的 X-Forwarded-For 头域获取客户端 IPv6 源地址。
>- 当前 IPv6 负载均衡是纯公网负载均衡，相同 VPC 的客户端无法通过内网访问该 IPv6 负载均衡。
>- 互联网 IPv6 网络大环境还处于建设初期，如出现线路访问不通的情况，请 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=163&source=0&data_title=%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%20LB&step=1) 反馈，另外在内测期间，不提供 SLA 保障。
>


## 概述
IPv6 负载均衡是基于 IPv6 单栈技术实现的负载均衡，和 IPv4 负载均衡协同工作，实现 IPv6/IPv4 双栈通信。IPv6 负载均衡绑定的是云服务器的 IPv6 地址，并对外提供 IPv6 VIP 地址。

### IPv6 负载均衡优势
腾讯云 IPv6 负载均衡在助力业务快速接入 IPv6 时具有如下优势：
- 快速接入：秒级接入 IPv6，随买随用快速上线。
- 易于使用：IPv6负载均衡兼容原 IPv4 负载均衡的操作流程，零学习成本，低门槛使用。
- 端到端的 IPv6 通信：IPv6 负载均衡和云服务器之间通过 IPv6 通信，可以帮助部署在云服务器的应用快速进行 IPv6 改造，并实现端到端的 IPv6 通信。

### IPv6 负载均衡架构
负载均衡支持创建 IPv6 负载均衡（下文中也叫 IPv6 CLB）实例，腾讯云会给 IPv6 CLB 实例分配一个 IPv6 公网地址（即 IPv6 版的 VIP），该 VIP 会将来自 IPv6 客户端的请求转发给后端的 IPv6 云服务器。

IPv6 CLB 实例不但可以快速接入 IPv6 公网用户访问，且通过 IPv6 协议和后端云服务器进行通信，能够帮助云上的应用快速改造 IPv6，并实现端到端的 IPv6 通信。

IPv6 负载均衡的架构如下图所示：
![](https://main.qcloudimg.com/raw/ca444992408e16390a46a3e2d9239bf5.svg)


## 操作指南
### 步骤1：创建 IPv6 负载均衡实例
1. 登录腾讯云官网，进入 [负载均衡购买页](https://buy.cloud.tencent.com/lb)。
2. 请正确选择如下参数：
 - 计费模式：仅支持按量计费。
 - 地域：选择目标地域。
 - IP 版本：IPv6。
 - 运营商类型：BGP。
 - 网络：请务必选择已获取 IPv6 CIDR 的私有网络和子网。
3. 在购买页选择各项配置后，单击**立即购买**，返回至 [负载均衡实例列表页](https://console.cloud.tencent.com/loadbalance/index?rid=1&forward=1)，即可查看已购的 IPv6 负载均衡。


### 步骤2：创建 IPv6 负载均衡监听器
1. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb/index?rid=1&type=2%2C3)，单击 IPv6 负载均衡实例 ID，进入详情页。
2. 选择**监听器管理**标签页，单击**新建**，如创建一个 TCP 监听器。
>?支持创建四层 IPv6 负载均衡监听器（TCP/UDP/TCP SSL）和七层 IPv6 负载均衡监听器（HTTP/HTTPS），详情请参见 [负载均衡监听器概述](https://cloud.tencent.com/document/product/214/6151)。
>
3. 在“基本配置”中配置名称、监听协议端口和均衡方式，单击**下一步**。
![](https://main.qcloudimg.com/raw/815c00aa93b5f23408bd78791ea5b7c3.png)
4. 配置健康检查，单击**下一步**。
![](https://main.qcloudimg.com/raw/19fbf68edcb9d4f06102ae61c2228b67.png)
5. 配置会话保持，单击**提交**。
![](https://main.qcloudimg.com/raw/9743537a93828dc8c0c10e6c943f7673.png)
6. 监听器创建完成后，选中该监听器，在右侧单击**绑定**。
>?绑定云服务器前，请确定该云服务器已获取 IPv6 地址。
>
![](https://main.qcloudimg.com/raw/edf72af61361da4f833f2424a548040e.png)
7. 在弹出框中，选择需要通信的 IPv6 云服务器，并配置服务端口和权重，单击**确定**即可。
![](https://main.qcloudimg.com/raw/7eb363ea3170bbe7a881762be7968210.png)
