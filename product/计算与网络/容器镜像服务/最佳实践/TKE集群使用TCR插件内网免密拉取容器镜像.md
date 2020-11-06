## 操作场景
本文介绍如何在 [容器服务 TKE](https://cloud.tencent.com/document/product/457/6759) 中，通过使用 TCR 插件，实现内网免密拉取企业版实例内容器镜像，并创建工作负载。

## 前提条件
在使用容器镜像服务 TCR 企业版内托管的私有镜像进行应用部署前，您需要完成以下准备工作：
- 已成功 [创建企业版实例](https://cloud.tencent.com/document/product/1141/40716)。
- 已成功 [创建 TKE 集群](https://cloud.tencent.com/document/product/457/32189)。
- 如使用子账号进行操作，请参考 [企业版授权方案示例](https://cloud.tencent.com/document/product/1141/41417) 提前为子账号授予对应实例的操作权限。
- 如使用已有 TKE 集群，请确认操作子账号具有集群相关权限，请参考 [TKE 集群权限管理](https://cloud.tencent.com/document/product/457/11542)。


## 操作步骤

### 准备容器镜像
#### 步骤1：创建命名空间
新建的 TCR 企业版实例内无默认命名空间，且无法通过推送镜像自动创建。请参考 [创建命名空间](https://cloud.tencent.com/document/product/1141/41803#.E5.88.9B.E5.BB.BA.E5.91.BD.E5.90.8D.E7.A9.BA.E9.97.B4) 按需完成创建。
建议命名空间名使用项目或团队名，本文以 `docker` 为例。创建成功后如下图所示：
![](https://main.qcloudimg.com/raw/0863439831b93c49a243dccaeb0a9806.png)

#### 步骤2：创建镜像仓库（可选）
容器镜像托管在具体的镜像仓库内，请参考 [创建镜像仓库](https://cloud.tencent.com/document/product/1141/41811#.E5.88.9B.E5.BB.BA.E9.95.9C.E5.83.8F.E4.BB.93.E5.BA.93) 按需完成创建。镜像仓库名称请设置为期望部署的容器镜像名称，本文以 `getting-started` 为例。创建成功后如下图所示：
>?通过 docker cli 或其他镜像工具，例如 jenkins 推送镜像至企业版实例内时，若镜像仓库不存在，将会自动创建，无需提前手动创建。
>
![](https://main.qcloudimg.com/raw/e2af4a28cdfe97f47bd54a24a61af88d.png)

#### 步骤3：推送容器镜像
您可通过 docker cli 或其他镜像构建工具（例如 jenkins）推送镜像至指定镜像仓库内，本文以 docker cli 为例。此步骤需要您使用一台安装有 Docker 的云服务器或物理机，并确保访问的客户端已在 [配置网络访问策略](https://cloud.tencent.com/document/product/1141/41836) 定义的公网或内网允许访问范围内。
1. 参考 [获取实例访问凭证](https://cloud.tencent.com/document/product/1141/41829) 获取登录指令，并进行 Docker Login。
2. 登录成功后，您可在本地构建新的容器镜像或从 DockerHub 上获取一个公开镜像用于测试。
本文以 DockerHub 官方的 Nginx 最新镜像为例，在命令行工具中依次执行以下指令，即可推送该镜像。请将 demo-tcr、docker 及 getting-started 依次替换为您实际创建的实例名称、命名空间名称及镜像仓库名。
```
docker tag getting-started:latest demo-tcr.tencentcloudcr.com/docker/getting-started:latest
```
```
docker push demo-tcr.tencentcloudcr.com/docker/getting-started:latest
```
推送成功后，即可前往控制台的 “[镜像仓库](https://console.cloud.tencent.com/tcr/repository)” 页面，选择仓库名并进入详情页面查看。

### 配置 TKE 集群访问 TCR 实例<span id="deployTKE"></span>
TCR 企业版实例支持网络访问控制，默认拒绝全部来源的外部访问。您可根据 TKE 集群的网络配置，选择通过公网或内网访问指定实例，拉取容器镜像。若 TKE 集群与 TCR 实例部署在同一地域，建议通过内网访问方式拉取容器镜像，该方式可提升拉取速度，并节约公网流量成本。
1. 登录容器服务控制台，选择左侧导航栏中的【[集群](https://console.cloud.tencent.com/tke2/cluster)】。
2. 在“集群管理”页面，选择集群 ID，进入集群详情页。 
3. 在集群详情页面，选择左侧【组件管理】，进入“组件管理”页面，并单击【新建】。
4. 在“新建扩展组件”页面，选择 “TCR” 组件。如下图所示：
    >? 当前 TCR 组件暂只支持 K8S 版本为1.14、1.16、1.18的集群，如集群版本暂不支持，请采用手动配置方式。
	>
   ![](https://main.qcloudimg.com/raw/ac01c58b0e50f2c2001f0abe50a361e3.png)
  - 单击【查看详情】了解组件功能及配置说明。
  - 单击【参数配置】开始配置组件。
5. 在“TCR组件参数设置”页面，参考【查看详情】中介绍的组件配置方式，配置相关参数。如下图所示：
![](https://main.qcloudimg.com/raw/34fa53f8b3a3b6c04f7470ea84613d7b.png)
    - **关联实例**：选择与集群同地域的 TCR 实例。
    - **免密拉取配置**：可采用默认配置。
    - **内网访问配置**：当内网访问链路中未展示为“链路正常”，请参考 [内网访问控制](https://cloud.tencent.com/document/product/1141/41838)，配置 TCR 实例与 TKE 集群所在私有网络 VPC 的内网链路。
6. 单击【确定】返回组件选择界面。
7. 在组件选择界面单击【完成】，开始为集群安装 TCR 扩展组件。
8. 组件安装完成后，集群将具备内网免密拉取该关联实例内镜像的能力，无需额外配置。如下图所示：
![](https://main.qcloudimg.com/raw/9a63dbecc51517f3c54e5872d23e6a2f.png)

### 使用 TCR 实例内容器镜像创建工作负载
1. 在集群详情页面，选择左侧【工作负载】>【Deployment】。
2. 进入“Deployment” 页面，并单击【新建】。
3. 进入“新建Workload” 页面，参考以下信息创建工作负载。
主要参数信息如下，其他参数请按需设置：
 - **命名空间**：选择已下发访问凭证的命名空间。
 - **实例内容器**：
    - **镜像**：单击【选择镜像】，并在弹出的“选择镜像”窗口中，选择 TCR 实例内容器镜像。如下图所示：
![](https://main.qcloudimg.com/raw/c4a4840a1ea80e82684f32153345cb55.png)
 - **镜像访问凭证**：如集群已安装 TCR 扩展组件，无需显式配置。
4. 完成其他参数设置后，单击【创建workload】，查看该工作负载的部署进度。
部署成功后，可在 “Deployment” 页面查看该工作负载的“运行/期望Pod数量”为“1/1”。如下图所示：
![](https://main.qcloudimg.com/raw/cc69105f8d20f2d6ed33e3a90c5d0c9f.png)

