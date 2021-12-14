
## 操作场景

本文将实践如何使用负载均衡 CLB 作为 Serverless 服务的访问入口，配合 SCF 快速部署 Web 服务。拓展 Serverless 服务低成本、免运维等优势，为开发者平滑迁移应用上云提供参考。

## 操作步骤

### 创建私有网络 VPC[](id:createVPC) 
登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)，创建私有网络与子网。详情可参见 [快速搭建私有网络](https://cloud.tencent.com/document/product/215/30716)。

<dx-alert infotype="notice" title="">
私有网络 VPC 需要与负载均衡 CLB 和云函数 SCF 网页部署在相同地区，本案例以 “上海” 为例。
</dx-alert>




### 创建 CLB 实例[](id:createCLB)

1. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb/instance?rid=4&pid=0&type=OPEN)，创建负载均衡实例。详情可参见 [创建负载均衡实例](https://cloud.tencent.com/document/product/214/8975#.E6.AD.A5.E9.AA.A4.E4.B8.80.EF.BC.9A.E8.B4.AD.E4.B9.B0.E8.B4.9F.E8.BD.BD.E5.9D.87.E8.A1.A1.E5.AE.9E.E4.BE.8B)。
![](https://main.qcloudimg.com/raw/6422b8dda3b985825a93a74ecfcc06ce.png)
本案例以 “上海” 地域为例，私有网络选择 [上一步](#createVPC) 中已创建的 VPC。
2. 创建完成后，在“实例管理”页面中，找到目标负载均衡实例，为实例配置监听器。配置监听器详情可参见 监听器详情可参见 [配置 HTTP 监听器](https://cloud.tencent.com/document/product/214/36384)。
本案例以监听器名称为`clb-scf-web`，监听协议端口为`81`为例。 



### 创建云函数服务
1. 登录云函数控制台，选择左侧导航栏中的 **[函数服务](https://console.cloud.tencent.com/scf/list)**。
2. 在“函数服务”页面上方选择**上海**地域，并单击**新建**进入新建函数页面。
  设置以下参数信息，并单击**下一步**。如下图所示：
 - **创建方式**：选择**模板创建**。
 - **模糊搜索**：输入 “Web 静态页面托管”“Python3.6”，并进行搜索。
 单击模板中的**查看详情**，即可在弹出的“模板详情”窗口中查看相关信息，支持下载操作。
![](https://main.qcloudimg.com/raw/847f64a37bb760cfae6660bae0426e2e.png)
3. 在**基础配置**中，填写**函数名称**，选择**函数地域**。
   - 函数名称：例如 `clb-scf-web`。
   - 地域：需要与 CLB 地域相同，例如 “上海”。
4. 在**触发器配置**中，选择“自定义创建”，使用触发器绑定 CLB 至 SCF。
   - 触发版本：选择“默认流量”。
   - 触发方式：选择“CLB触发”。
   - 实例ID：选择 [上一步](#createCLB) 中已创建的 CLB 实例，例如 `clb_serverless_web`。
   - 监听器：选择已配置的监听器，在本案例中监听器监听了端口`81`。
   - 域名/主机：选择“新建规则”。
   - 新增域名：将 CLB 实例中的 “VIP” 填入新增域名。
   <dx-alert infotype="explain" title="">
VIP 即负载均衡向客户端提供服务的 IP 地址。
   </dx-alert>
   - URL路径：以 `/` 为开头添加本网站 URL 路径，例如 `/demo`。
5. 单击**完成**，跳转到**部署日志**中查看函数和触发器创建进度。

### 测试负载均衡入口
1. 登录云函数控制台，选择左侧导航栏中的 **[函数服务](https://console.cloud.tencent.com/scf/list)**。
2. 在“函数服务”页面上方单击已创建的函数 `clb-scf-web`。
3. 在该函数的详情页面，选择**触发管理**。
4. 在“触发管理”页中获取 API 网关触发器访问路径，查看 Web 页面。如下图所示：
![](https://main.qcloudimg.com/raw/579a6edd4c4f610c7783e84d1fa5bcc7.png)



