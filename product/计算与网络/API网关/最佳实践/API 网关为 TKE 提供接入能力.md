## TKE 介绍

腾讯云容器服务（Tencent Kubernetes Engine，TKE）是基于原生 Kubernetes 提供以容器为核心的、高度可扩展的高性能容器管理服务。相较于用户自建容器服务，TKE 具备简单易用、灵活拓展、安全可靠、高效、低成本等核心优势。详细介绍请参考 [容器服务文档](https://cloud.tencent.com/document/product/457)。

## 操作场景

Kubernetes 作为自动化容器操作的开源平台，已经成为开发者的主流选择。但 Kubernetes 集群没有足够的接入能力，在面对大型应用时，这一点显得尤为突出。将 API 网关作为 Kubernetes 的接入层，能大幅提高 Kubernetes 集群的接入能力，并为 Kubernetes 集群带来 API 网关的高级能力，满足更多用户的更多场景。以下是本场景的架构图：
![](https://main.qcloudimg.com/raw/5a7a5514e002aabf475958127b499e0c.svg)

## 前提条件

配置过程中需要用到 API网关、容器服务 TKE、负载均衡 CLB、私有网络 VPC、云服务器 CVM 等云产品，请确保您已开通这些云产品并且拥有配置权限。

## 操作步骤

<span id="1"></span>
### 步骤1：创建 VPC
1. 登录 [私有网络 VPC 控制台](https://console.cloud.tencent.com/vpc)。
2. 在左侧导航栏中单击【私有网络】，进入私有网络列表。
3. 单击【+新建】，在弹出的对话框中填写内容，创建一个私有网络 VPC。
详细操作请参考 [管理私有网络](https://cloud.tencent.com/document/product/215/36515)。
 <img src="https://main.qcloudimg.com/raw/960e423558a59a055d6995929fd3ae6c.png" width="80%" height="80%">


<span id="2"></span>
### 步骤2：创建 CVM
1. 登录 [云服务器 CVM 控制台](https://console.cloud.tencent.com/cvm)。
2. 在左侧导航栏中单击【实例】，进入实例列表。
3. 单击【新建】，打开 CVM 购买页。
4. 参考 [创建实例](https://cloud.tencent.com/document/product/213/4855) 文档，根据步骤操作，创建一个云服务器 CVM。
>?CVM 的网络需要选择 [步骤1](#1) 中创建的 VPC 和子网，其余配置项均采用默认配置即可。本文中创建了一个标准型 S5 的 CVM 实例。

  <img src="https://main.qcloudimg.com/raw/5eb612c02a613a82cfd48ea701d23db2.png" width="80%" height="80%">
 
<span id="3"></span>
### 步骤3：在同一 VPC 下创建 TKE
1. 登录 [容器服务 TKE 控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中单击【集群】，进入集群列表。
3. 单击集群列表上方的【新建】，参考 [创建集群](https://cloud.tencent.com/document/product/457/32189) 文档创建一个 TKE 容器集群。
 >!
>- 第1步-集群信息中，【集群网络】需选择步骤一中创建的 VPC。
>- 第2步-选择机型中，【节点来源】选择已有节点；【Master 节点】选择平台托管，【Worker 配置】选择 [步骤2](#2) 中创建的 CVM。
>- 其余配置项均采用默认配置即可。
 
 ![](https://main.qcloudimg.com/raw/861608f37d306d90dd1f9173ad17203e.png)

### 步骤4：在 TKE 上创建 Nginx 服务
1. 在 [容器服务 TKE 控制台](https://console.cloud.tencent.com/tke2) 左侧导航栏中单击【集群】，进入集群列表。
2. 在集群列表中，单击 [步骤3](#3) 中创建集群的 ID，进入集群详情页面。
3. 在左侧导航栏中单击【工作负载】>【Deployment】，进入 Deployment 列表。
4. 单击 Deployment 列表上方的【新建】，进入新建 Workload 页面。
5. 参考 [创建 Nginx 服务](https://cloud.tencent.com/document/product/457/7851) 文档，在新建 Workload 页面填写内容。
 >!
 >- 使用 DockerHub 的 Nginx 镜像
 >- 服务访问方式：VPC 内网访问
 >- 负载均衡器：自动创建
 >- 端口映射：协议为 TCP，从容器端口80到服务端口80
6. 单击【创建 Workload】，完成 WorkLoad 的创建，TKE 会自动创建对应的 Deployment 和 Service 。
	![](https://main.qcloudimg.com/raw/ce157e5765aeb4b392841ffca279656c.png)

### 步骤5：在 API 网关中创建服务
1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway)。
2. 在左侧导航栏中点击【服务】，进入服务列表。
3. 单击服务列表上方的【新建】，参考 [创建服务](https://cloud.tencent.com/document/product/628/11787)文档创建一个 API 网关服务。

### 步骤6：在 API 网关服务中创建 API
1. 在 [API 网关控制台](https://console.cloud.tencent.com/apigateway) 左侧导航栏中单击【服务】，进入服务列表。
2. 在服务列表中单击服务名称，进入服务详情页。
3. 在服务详情页单击【管理API】，在管理 API 页单击【新建】，进入 API 创建页面。
4. 在 API 创建页面依次填写前端配置、后端配置、响应配置后单击【完成】，完成 API 的创建。
>!填写后端配置时，后端类型选择“HTTP”，VPC 信息选择步骤一所创建的 VPC，VPC 内资源选择“CLB”，后端路径填“/”即可。

  <img src="https://main.qcloudimg.com/raw/b6879ebde2cafabc3d5056240480e9f2.png" width="60%" height="60%">

<span id="7"></span>
### 步骤7：放通 API 网关内网网段
1. 登录 [云服务器 CVM 控制台](https://console.cloud.tencent.com/cvm)，在左侧导航栏单击【安全组】，进入安全组列表。
2. 选择地域后，单击【+新建】，在弹出的对话框中填写内容，创建一个安全组。
	 ![](https://main.qcloudimg.com/raw/35199dc68b141f07774cee082bb03a78.png)
3. 单击【确定】后进入安全组详情页面，依次选择【安全组规则】>【入站规则】，即可到达入站规则列表。
4. 单击【添加规则】，在弹出的对话框中依次添加9.0.0.0/8、10.0.0.0/8、100.64.0.0/10、11.0.0.0/8、30.0.0.0/8五个API网关的内网网段，协议端口均填写“ALL”，策略均配置为“允许”。单击【完成】，添加五条入站规则。
	 ![](https://main.qcloudimg.com/raw/f74cbe54686520228b4f4cc08bc00f9d.png)
5. 返回安全组详情页面，依次选择【关联实例】>【云服务器】>【新增关联】，将刚刚创建好的安全组关联到 [步骤2](#2) 中创建的 CVM 上，即可实现放通 API 网关内网网段。

### 步骤8：发布 API 网关服务并测试
1. 在 [API 网关控制台](https://console.cloud.tencent.com/apigateway) 左侧导航栏中单击【服务】，进入服务列表。
2. 在服务列表中单击服务名称，进入服务详情页。
3. 在服务详情页的【基本配置】Tab 页中，单击页面右上角的【发布】，将服务发布至“发布”环境。
4. 请求 [步骤6](#6) 中创建的 API，可以看到 Nginx 页面即代表访问成功。

<img src="https://main.qcloudimg.com/raw/7c2d94c0bfc199305a68df3f0eb0001c.png" width="60%" height="60%">
