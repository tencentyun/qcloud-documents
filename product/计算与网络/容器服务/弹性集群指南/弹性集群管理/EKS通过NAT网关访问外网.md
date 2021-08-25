## 操作场景
弹性容器服务（Elastic Kubernetes Service，EKS）支持通过配置 [NAT 网关](https://cloud.tencent.com/document/product/215/4975) 和 [路由表](https://cloud.tencent.com/document/product/215/4954) 来实现集群内服务访问外网，您可参考本文进行配置。

## 操作步骤



### 创建 NAT 网关[](id:createNAT)
1. 登录腾讯云私有网络控制台，选择左侧导航栏中的 **[NAT 网关](https://console.cloud.tencent.com/vpc/nat)**。
2. 在 “NAT网关”页面中，单击**+新建**。
3. 在弹出的“新建NAT网关”窗口中参考 [创建 NAT 网关](https://cloud.tencent.com/document/product/552/18186#.E6.AD.A5.E9.AA.A41.EF.BC.9A.E5.88.9B.E5.BB.BA-nat-.E7.BD.91.E5.85.B3)，创建与 EKS 集群同地域、同私有网络 VPC 的 NAT 网关。

### 创建指向 NAT 网关的路由表[](id:createRouting)
1. 选择左侧导航栏中的 **[路由表](https://console.cloud.tencent.com/vpc/route)**，进入“路由表”管理页面。
2. 在“路由表”管理页面，单击**+新建**。
3. 在弹出的“新建路由表”窗口中，参考以下信息创建与 EKS 集群同地域、同 VPC 的路由表。如下图所示：
![](https://main.qcloudimg.com/raw/34967197070bfbacc3a93c8ac92b234d.png)
主要参数信息如下：
 - **目的端**：选择需访问的外网 IP 地址，支持配置 CIDR。例如，填写 `0.0.0.0/0` 会转发所有流量到 NAT 网关。
 - **下一跳类型**：选择“NAT 网关”。
 - **下一跳**：选择在 [创建 NAT 网关](#createNAT) 步骤中已创建的 NAT 网关。
4. 单击**创建**即可。

### 关联子网至路由表
完成配置路由后，需选择子网关联到该路由表，被选择子网内的访问 Internet 的流量将指向 NAT 网关。步骤如下：
1. 在“路由表”页面中，选择 [创建指向 NAT 网关的路由表](#createRouting) 步骤中已创建路由表所在行右侧的**关联子网**。
2. 在弹出的“关联子网”窗口中，勾选需关联子网并单击**确定**即可。
<dx-alert infotype="explain" title="">
此子网为容器网络，并非 Service CIDR。
</dx-alert>
完成路由表关联子网后，同 VPC 的资源即可以通过 NAT 网关的外网 IP 访问 Internet。

## 验证配置
1. 在“弹性集群”列表页面，单击集群 ID 进入该集群的管理页面。
2. 选择需登录容器所在行右侧的**远程登录**，并执行 ping 命令验证该 Pod 是否可访问外网。返回结果如下所示，则表明已成功访问外网。
![](https://main.qcloudimg.com/raw/35fec47afacbe6d9407f61be565bbb24.png)
