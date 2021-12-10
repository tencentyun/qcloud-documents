## 操作场景

运行在 TEM 上的应用，由于业务需求等原因，通常会有访问公网的需求。同时，小程序等场景中通常会有访问白名单的需求，此时要求访问公网的应用有固定的公网 IP。

基于上述需求，本文档将会详细介绍部署在 TEM 上的应用访问公网的方法。

#### 整体思路：
TEM 中的应用部署在用户的环境中，环境和用户的 VPC 关联，即 TEM 中的应用本质上是部署在用户的 VPC 内。可通过为 VPC 配置 NAT 网关，并为 NAT Gateway 关联 EIP，实现 VPC 内的应用访问公网。


#### 操作流程：
<dx-steps>
- [部署 TEM 应用](#step1)
- [创建 NAT 网关实例](#step2)
- [在 VPC 控制台中配置 NAT 网关信息](#step3)
- [验证公网访问](#step4)
- [(可选)查询访问公网的 IP](#step5)
</dx-steps>



## 操作步骤

### 步骤1：部署 TEM 应用[](id:step1)

参考 [创建环境]( https://cloud.tencent.com/document/product/1371/53293) 和 [创建应用]( https://cloud.tencent.com/document/product/1371/53294) 在 TEM 控制台中部署应用。



### 步骤2：创建 NAT 网关实例[](id:step2)

登录 [NAT 网关控制台](https://console.cloud.tencent.com/vpc/nat?rid=4)，在左侧导航栏选择**NAT网关**，选择 TEM 应用所在的地域，单击**新建**购买 NAT 网关实例。
<img src="https://main.qcloudimg.com/raw/dbdc9cc093cd253f17b0a3d9ae08dafc.png" width="600px">
- **所属网络**：与 TEM 应用所在环境的 VPC 保持一致。
- **弹性IP**：若没有可用的公网弹性 IP (EIP)，一键跳转进行购买，购买后在 NAT 网关购买页面中刷新即可查到。



### 步骤3：在 VPC 控制台中配置 NAT 网关信息[](id:step3)

1. 在 TEM 控制台 [**环境**](https://console.cloud.tencent.com/tem/env) 页面单击 TEM 应用所在的环境卡片，进入环境基本信息页面。
2. 在集群网络处单击 VPC，跳转至 VPC 网络基本信息页面。
	<img src="https://main.qcloudimg.com/raw/bcaabe271f748c1632c20d4d18f241be.png" width="450px">
3. 单击**路由表**模块，进入路由表配置页面。
4. 在路由表页面，单击**新建**，配置路由表。
   ![](https://main.qcloudimg.com/raw/d8e0c1143cbe31013011a01debb61b26.png)
   - **目的端**：选择需访问的外网 IP 地址，支持配置 CIDR，例如，填写 0.0.0.0/0 会转发所有流量到 NAT 网关
   - **下一跳类型**：选择**NAT 网关**。
   - **下一跳**：选择**步骤2**中创建的 NAT 网关。

   详细配置参考 [自定义路由表](https://cloud.tencent.com/document/product/215/36682)。
5. 在创建好的路由表操作栏单击**更多** > **关联子网**，在关联的子网中选择 TEM 应用所在环境关联的子网
![](https://main.qcloudimg.com/raw/e1a0128b08128ac0c8ea394eef96195e.png)


### 步骤4：验证公网访问[](id:step4)

1. 在 TEM 控制台的 [**应用管理**](https://console.cloud.tencent.com/tem/application?rid=4) 页面单击 TEM 应用的“ID”，进入应用实例列表页面。
2. 单击应用实例操作栏的**Webshell**，进入到 Webshell 中。
   ![](https://main.qcloudimg.com/raw/fc3adda3cc164fe7d9597fc24f223901.png)
3. 验证是否可以访问公网。
	![](https://main.qcloudimg.com/raw/74eaf5884506d3880dcf0529df16ea15.png)



###  步骤5：(可选)查询访问公网的 IP[](id:step5)

1. 在 TEM 控制台 [**环境**](https://console.cloud.tencent.com/tem/env) 页面单击 TEM 应用所在的环境卡片，进入环境基本信息页面。
2. 在集群网络处单击 VPC，跳转至 VPC 网络基本信息页面。
	<img src="https://main.qcloudimg.com/raw/bcaabe271f748c1632c20d4d18f241be.png" width="450px">
3. 单击**NAT 网关**模块，进入NAT 网关列表页面。
4. 单击目标NAT网关的“ID”，进入NAT网关基本信息页面，选择**关联弹性IP**页签，可获取访问公网的 IP。
	<img src="https://main.qcloudimg.com/raw/c29b3c7ffce4f7b745a534a9a1474459.png" width="600px">


## 额外费用

使用 [NAT 网关](https://cloud.tencent.com/product/nat) 和 [EIP](https://cloud.tencent.com/product/eip) 产生额外费用，定价详情参见：

- [NAT 网关定价](https://cloud.tencent.com/document/product/552/18172)
- [EIP 定价](https://cloud.tencent.com/document/product/1199/41692)
