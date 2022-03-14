## 操作场景

本文介绍如何在 [弹性容器服务 EKS](https://cloud.tencent.com/document/product/457/57338) 中拉取 TCR 企业版实例内的容器镜像，并创建工作负载。


## 前提条件


在使用容器镜像服务 TCR 企业版内托管的私有镜像进行应用部署前，您需要完成以下准备工作：

- 已成功 [购买企业版实例](https://cloud.tencent.com/document/product/1141/51110)。
- 已成功 [创建 EKS 集群](https://cloud.tencent.com/document/product/457/39813)。
- 如使用子账号进行操作，请参见 [企业版授权方案示例](https://cloud.tencent.com/document/product/1141/41417) 提前为子账号授予对应实例的操作权限。



## 操作步骤

### 准备容器镜像


#### 步骤1：创建命名空间

新建的 TCR 企业版实例内无默认命名空间，且无法通过推送镜像自动创建。请参见 [创建命名空间](https://cloud.tencent.com/document/product/1141/41803#.E5.88.9B.E5.BB.BA.E5.91.BD.E5.90.8D.E7.A9.BA.E9.97.B4) 按需完成创建。


建议命名空间名使用项目或团队名，本文以 `docker` 为例。创建成功后如下图所示：
![](https://main.qcloudimg.com/raw/9fc8509e27ae62915804070f725f75fa.png)        



#### 步骤2：创建镜像仓库（可选）


容器镜像托管在具体的镜像仓库内，请参见 [创建镜像仓库](https://cloud.tencent.com/document/product/1141/41811#.E5.88.9B.E5.BB.BA.E9.95.9C.E5.83.8F.E4.BB.93.E5.BA.93) 按需完成创建。镜像仓库名称请设置为期望部署的容器镜像名称，本文以 `getting-started` 为例。创建成功后如下图所示：
![](https://main.qcloudimg.com/raw/663965fe8382ce2bf900d10318c16e56.png)       
>? 通过 `docker cli` 或其他镜像工具，例如 jenkins 推送镜像至企业版实例内时，若镜像仓库不存在，将会自动创建，无需提前手动创建。



#### 步骤3：推送容器镜像



1. 您可通过 `docker cli` 或其他镜像构建工具（例如 jenkins）推送镜像至指定镜像仓库内，本文以 `docker cli` 为例。此步骤需要您使用一台安装有 Docker 的云服务器或物理机，并确保访问的客户端已在 [配置网络访问策略](https://cloud.tencent.com/document/product/1141/41836) 定义的公网或内网允许访问范围内。
2. 参考 [获取实例访问凭证](https://cloud.tencent.com/document/product/1141/41829) 获取登录指令，并进行 Docker Login。
3. 登录成功后，您可在本地构建新的容器镜像或从 DockerHub 上获取一个公开镜像用于测试。
本文以 DockerHub 官方的 Nginx 最新镜像为例，在命令行工具中依次执行以下指令，即可推送该镜像。请将 demo-tcr、docker 及 getting-started 依次替换为您实际创建的实例名称、命名空间名称及镜像仓库名。
<dx-codeblock>
:::  sh
docker tag getting-started:latest demo-tcr.tencentcloudcr.com/docker/getting-started:latest
:::
</dx-codeblock>
<dx-codeblock>
:::  sh
docker push demo-tcr.tencentcloudcr.com/docker/getting-started:latest
:::
</dx-codeblock>
4. 推送成功后，即可前往控制台的 [镜像仓库](https://console.cloud.tencent.com/tcr/repository) 页面，选择仓库名并进入详情页面查看。






### 配置 EKS 集群访问 TCR 实例



为保护您的数据安全，TCR 和 EKS 初始默认拒绝全部公网及内网访问。在准备将 TCR 的镜像部署至 EKS 之前，请先进行网络访问策略配置。



TCR 企业版实例支持网络访问控制，您可根据 EKS 集群的网络配置，选择通过公网或内网访问指定实例，拉取容器镜像。若 EKS 集群与 TCR 实例部署在同一地域，建议通过内网访问方式拉取容器镜像，该方式可提升拉取速度，并节约公网流量成本。

下文将介绍通过内网访问的方式，若要通过外网访问，请参见 [通过 NAT 网关访问外网](https://cloud.tencent.com/document/product/457/48710)。






#### 步骤1：在 TCR 实例中关联集群 VPC



为保障用户数据安全，新建的 TCR 实例默认拒绝全部来源的访问。为允许指定 EKS 集群可访问 TCR 实例拉取镜像，需将集群所在的 VPC 关联至 TCR 实例，并配置相应的内网域名解析。



1. [新建内网访问链路](https://cloud.tencent.com/document/product/1141/41838#.E6.96.B0.E5.BB.BA.E8.AE.BF.E9.97.AE.E9.93.BE.E8.B7.AF)。
2. [配置域名内网解析](https://cloud.tencent.com/document/product/1141/41838#.E7.AE.A1.E7.90.86.E5.86.85.E7.BD.91.E8.A7.A3.E6.9E.90)。





#### 步骤2：获取 TCR 实例访问凭证[](id:step2)



从 TCR 实例中拉取容器镜像需要首先使用凭证信息登录至实例。请参见 [获取实例访问凭证](https://cloud.tencent.com/document/product/1141/41829)，保存该实例的长期访问凭证，用于之后配置部署 TCR 镜像。





### 使用 TCR 实例内容器镜像创建工作负载



1. 登录容器服务控制台，选择左侧导航栏中的**[弹性容器-弹性集群](https://console.cloud.tencent.com/tke2/ecluster?rid=19)**。
2. 选择需要创建工作负载的集群 ID，进入集群详情页。
3. 在集群详情页面，选择左侧**工作负载** > **Deployment**。
4. 进入“Deployment” 页面，并单击**新建**。
5. 进入“新建Workload” 页面，参考以下主要的参数信息，创建工作负载。
	- **命名空间**：根据需要选择集群的命名空间。
	- **实例内容器**：
		- **镜像**：单击**选择镜像**，并在弹出的“选择镜像”窗口中，选择**容器镜像服务 企业版**，再根据需要选择地域、实例和镜像仓库。如下图所示：
	![](https://main.qcloudimg.com/raw/4aa3e009714aba2521e0a889cac71a47.png)    
	- **镜像版本**：选择镜像后，单击**选择镜像版本**，在弹出的“选择镜像版本”窗口中，根据需要选择该镜像仓库的某个版本。若不选择则默认为 latest。
	- **镜像访问凭证**：单击**添加镜像访问凭证**，下拉框中选择**使用新的访问凭证**。如下图所示：
	![](https://main.qcloudimg.com/raw/14f917f3e79b80822605f7f40be93c94.png)      
	单击**设置访问凭证信息**，在弹出的“新建镜像访问凭证”窗口中，正确填写该镜像的仓库域名、用户名和密码。
	- **仓库域名**：登录 [容器镜像服务](https://console.cloud.tencent.com/tcr) 控制台，选择左侧导航栏中的**镜像仓库**，即可获得所需镜像的仓库地址。
	- **用户名**：前往 [账号信息](https://console.cloud.tencent.com/developer) 获取账号 ID，账号 ID 即为用户名。
	- **密码**：在上述 [步骤2](#step2)：获取 TCR 实例访问凭证中获取的访问凭证即为密码。
	- **访问设置（Service）**：用户在 Kubernetes 中可以部署各种容器，其中一部分是通过 HTTP、HTTPS 协议对外提供七层网络服务，另一部分是通过 TCP、UDP 协议提供四层网络服务。而 Kubernetes 定义的 Service 资源可用于管理集群中四层网络的服务访问。参考以下主要的参数信息，完成访问设置。
		- **Service**：勾选**启用**。
		- **服务访问方式**：选择**VPC内网访问**。
6. 完成其他参数设置后，单击**创建Workload**，查看该工作负载的部署进度。
部署成功后，可在 “Deployment” 页面查看该工作负载的“运行/期望Pod数量”为“1/1”。如下图所示：
![](https://main.qcloudimg.com/raw/c2508150d4243cf4de8415d3a6ecc190.png)   
