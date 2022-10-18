
## 概述
TKE IPv4/IPv6 双栈基于集群维度，即需要先创建一个 TKE IPv4/IPv6 双栈集群。已创建的双栈集群，其 Pod 会自动分配 IPv4/IPv6 双栈地址，其 Servcie 也支持 IPv4/IPv6 双栈。
>? 
>- TKE IPv4/IPv6 双栈目前正在内测中，如需使用可 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=350&source=14&data_title=%E5%AE%B9%E5%99%A8%E6%9C%8D%E5%8A%A1%20TKE&step=1) 申请。
>- TKE IPv4/IPv6 双栈依赖于 IPv4/IPv6 双栈 VPC 和 IPv6 CLB，当前 IPv4/IPv6 双栈 VPC 和 IPv6 CLB 都在内测中，因此开通 TKE IPv4/IPv6 双栈将同时开通 IPv4/IPv6 双栈 VPC 和 IPv6  CLB。
>

## 前提条件
1. 创建 IPv4/IPv6 双栈类型的 VPC，具体方式为先创建 IPv4 类型 VPC，然后再开启 IPv6，操作详情见 [搭建 IPv6 私有网络](https://cloud.tencent.com/document/product/215/47557)。
2. 在 IPv4/IPv6 双栈类型的 VPC 中创建 IPv4/IPv6 双栈类型子网，具体方式先创建 IPv4 类型子网，然后再开启 IPv6，操作详情见 [搭建 IPv6 私有网络](https://cloud.tencent.com/document/product/215/47557)。

## 相关约束
- 目前支持地域为北京、上海、广州、上海金融、深圳金融、北京金融、成都、重庆、南京、中国香港、新加坡、弗吉尼亚。
- 目前仅支持 IPv4/IPv6 双栈类型 Service，暂不支持 IPv4/IPv6 双栈类型 Ingress。

## 操作步骤
### 步骤一：创建 TKE IPv4/IPv6 双栈集群
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 选择新建标准集群，选择 **IPv4/IPv6 双栈**集群 IP 类型。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/a81da34b4a70c6c5b3370bbce1c5455c.png)
>? 
>- 集群 IP 类型选项，IPv4 或 IPv4/IPv6 双栈，只能二选一。
>- IPv4/IPv6 双栈，其 Kubernetes 版本必须是 1.22 版本及以上。
>- 使用 IPv4/IPv6 双栈必须 VPC 和 CLB 支持 IPv6，以上展示地域为 VPC 和 CLB IPv6 支持地域。
>- IPv4/IPv6 双栈只支持 VPC-CNI 共享网卡模式，不支持固定 Pod IP，在选择集群网络、容器子网时，必须选 IPv4/IPv6 双栈 VPC 和子网。
>- 操作系统支持类型为 ubuntu18、ubuntu20、centos7.6、TencentOS Server 3.1 (TK4) 即 tlinux3.1(TK4)、TencentOS Server 2.6 (TK4) 即 tlinux2.6(TK4）。

### 步骤二：双栈集群创建完成后节点/节点池管理
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，单击集群 ID，进入详情页。
2. 选择**节点管理 > 节点**，单击**新建节点**。参考如下信息进行设置：
![](https://qcloudimg.tencent-cloud.cn/raw/042f859dc5f22bb994863fd28d4c4343.png)
 - **操作系统**：选择操作系统支持类型为 ubuntu18、ubuntu20、centos7.6、TencentOS Server 3.1 (TK4) 即 tlinux3.1(TK4)、TencentOS Server 2.6 (TK4) 即 tlinux2.6(TK4）。
 - **集群网络**：集群网络选择 IPv4/IPv6 双栈子网。
3. 选择**节点管理 > 节点池**，单击**新建节点池**。参考如下信息进行设置：
![](https://qcloudimg.tencent-cloud.cn/raw/3d3c0562da21f76f6c0b117b2e2cb575.png)
 - **操作系统**：选择操作系统支持类型为 ubuntu18、ubuntu20、centos7.6、TencentOS Server 3.1 (TK4) 即 tlinux3.1(TK4)、TencentOS Server 2.6 (TK4) 即 tlinux2.6(TK4）。
 - **集群网络**：集群网络选择 IPv4/IPv6 双栈子网。

### 步骤三：双栈集群创建完成后集群信息展示
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，单击集群 ID，进入详情页。
2. 在基本信息标签页查看集群 IP 类型和 Service CIDR（IPv4）、Service CIDR（IPv6）。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/1e490c770c69950bb4faef4e8f1039ef.png)
 

### 步骤四：创建 IPv4/IPv6 双栈 Service
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，单击集群 ID，进入详情页。
2. 选择**服务与路由 > Service**，进入 “Service” 管理页面。
3. 单击**新建**。根据实际需求，设置 Service 参数。
<dx-tabs>
::: ClusterIP 类型

针对 ClusterIP 类型，您需进行如下设置：
![](https://qcloudimg.tencent-cloud.cn/raw/0a12b096cbd40be6155f44f187c6e5ac.png)
- 对 Service 中 ipFamilyPolicy 进行展示。
- 实现对 Service 中 ipFamilies 进行配置。
:::
::: NodePort 类型
针对 NodePort 类型，您需进行如下设置：
![](https://qcloudimg.tencent-cloud.cn/raw/f5437c8027b75fef664e4ce5689f8230.png)
>? 
- 对 Service 中 ipFamilyPolicy 进行展示。
- 实现对 Service 中 ipFamilies 进行配置。
:::
::: 公网 LoadBalance 类型
针对公网 LoadBalance 类型，您需进行如下设置：
当前 CLB 只支持公网 IPv6 和 IPv4 单栈，同时 TKE 中单个 Servcie 只能绑定一个 CLB，如果需要使用 IPv4/IPv6 双栈，您必须新建两个公网 LoadBalance 类型 Servcie，一个绑定 IPv4 CLB，一个绑定 IPv6 CLB。

**新建 IPv4 公网 LoadBalance 类型 Servcie：**
![](https://qcloudimg.tencent-cloud.cn/raw/2587f7c37ff5a0bedc9d76e9ff63fd1f.png)
- 对 Service 中 ipFamilyPolicy 进行展示。
- IP 版本必须选择 IPv4。

<br>
		
**新建 IPv6 公网 LoadBalance 类型 Servcie：**
![](https://qcloudimg.tencent-cloud.cn/raw/c8b0eb5fea197e2998d5eb2bdcb7723e.png)
- 对 Service 中 ipFamilyPolicy 进行展示。
- IP 版本必须选择 IPv6。
- 选择相应的双栈子网。
- IPv6 公网 LoadBalance 运营商类型只有 BGP，网络计费模式只有按使用流量、共享带宽包。
- 负载均衡器使用已有选项，只能选择 IPv6 CLB。
:::
::: 内网 LoadBalance 类型
针对内网 LoadBalance 类型，您需进行如下设置：
当前 CLB 不支持内网 IPv6，因此 TKE Servcie 内网 LoadBalance 类型也只能支持 IPv4 单栈方式。
![](https://qcloudimg.tencent-cloud.cn/raw/2e58bcc2aa816201740f6add186bf623.png)
- 对 Service 中 ipFamilyPolicy 进行展示。
- 对 Service 中 ipFamilies 进行展示。
:::
</dx-tabs>
4. 单击**创建Service**，完成创建。您可在 Service 管理页面进行查看。








