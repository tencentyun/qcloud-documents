## 操作场景
腾讯云容器镜像服务（Tencent Container Registry，TCR）企业版面向具有严格数据安全及合规性要求、业务分布在多个地域、集群规模庞大的企业级容器客户，提供企业级的独享镜像安全托管服务。相较于个人版服务，企业版支持容器镜像安全扫描、跨地域自动同步、Helm Chart 托管、网络访问控制等特性，详情请参见 [容器镜像服务](https://cloud.tencent.com/document/product/1141)。
本文介绍如何在物联网边缘计算平台中，使用容器镜像服务 TCR 内托管的私有镜像进行应用部署。
更多关于腾讯云容器镜像服务的介绍请参见 [容器镜像服务](https://cloud.tencent.com/document/product/1141)。
本文介绍如何在边缘计算平台IECP 中，使用容器镜像服务 TCR 内托管的私有镜像进行应用部署。

## 前提条件
在使用 TCR 内托管的私有镜像进行应用部署前，您需要完成以下准备工作：
-	已在 [容器镜像服务](https://console.cloud.tencent.com/tcr) 创建企业版实例。如尚未创建，请参考 [创建企业版实例](https://cloud.tencent.com/document/product/1141/40716) 完成创建。
-	如果使用子账号进行操作，请参考 [企业版授权方案示例](https://cloud.tencent.com/document/product/1141/41417) 提前为子账号授予对应实例的操作权限。

## 操作步骤

### 步骤1：准备容器镜像
#### 创建命名空间
新建的 TCR 企业版实例内无默认命名空间，且无法通过推送镜像自动创建。请参考 [创建命名空间](https://cloud.tencent.com/document/product/1141/41803#.E5.88.9B.E5.BB.BA.E5.91.BD.E5.90.8D.E7.A9.BA.E9.97.B4) 按需完成创建。
建议命名空间名使用项目或团队名，本文以 docker 为例。创建成功后如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/418e0ec0434e8ab2ad15301c8cbd900a.png)

#### 创建镜像仓库（可选）
容器镜像托管在具体的镜像仓库内，请参考 [创建镜像仓库](https://cloud.tencent.com/document/product/1141/41811#.E5.88.9B.E5.BB.BA.E9.95.9C.E5.83.8F.E4.BB.93.E5.BA.93) 按需完成创建。镜像仓库名称请设置为期望部署的容器镜像名称，本文以 getting-started 为例。创建成功后如下图所示：
>? 通过 dockercli 或其他镜像工具，例如 Jenkins 推送镜像至企业版实例内时，若镜像仓库不存在，将会自动创建，无需提前手动创建。
>
![](https://qcloudimg.tencent-cloud.cn/raw/d39bdcfa85efbcdddf454e06747fc61e.png)

#### 推送容器镜像
您可通过 docker cli 或其他镜像构建工具，例如 jenkins 推送镜像至指定镜像仓库内，本文以 docker cli 为例。此步骤需要您使用一台安装有 Docker 的云服务器或物理机，并确保访问的客户端已在 [配置网络访问策略](https://cloud.tencent.com/document/product/1141/41836) 定义的公网或内网允许访问范围内。
1.	参考 [获取实例访问凭证](https://cloud.tencent.com/document/product/1141/41829) 获取登录指令，并进行 Docker Login。
2.	登录成功后，您可在本地构建新的容器镜像或从 DockerHub 上获取一个公开镜像用于  测试。
本文以 DockerHub 官方的 Nginx 最新镜像为例，在命令行工具中依次执行以下指  令，即可推送该镜像。请将 demo-tcr、docker 及 getting-started 依次替换为您实际创建的实例名称、命名空间名称及镜像仓库名。
```
docker tag getting-started:latest demo-tcr.tencentcloudcr.com/docker/getting-started:latest
```
```
docker push demo-tcr.tencentcloudcr.com/docker/getting-started:latest
```
推送成功后，即可前往控制台的 “[镜像仓库](https://console.cloud.tencent.com/tcr/repository)” 页面，选择仓库名进入详情页面查看。

### 步骤2：配置 TKE 集群访问 TCR 实例
TCR 企业版实例支持网络访问控制，默认拒绝全部来源的外部访问。您可根据 TKE 集群的网络配置，选择通过公网或内网访问指定实例，拉取容器镜像。若 TKE 集群与 TCR 实例部署在同一地域，建议通过内网访问方式拉取容器镜像，可提升拉取速度，并节约公网流量成本。
#### 配置内网访问及访问凭证
1. 配置内网访问
参考 [内网访问控制](https://cloud.tencent.com/document/product/1141/41838)，配置 TCR 实例与 TKE 集群所在私有网络 VPC 的内网链路，并开启自动解析。
2.	如当前 TCR 实例所在地域暂不支持开启自动解析，可在 TKE 集群中直接配置 TCR 实例的域名解析。请根据您的实际情况，选择以下方案：
**创建集群时配置节点 Host**
在创建 TKE 集群的“云服务器配置”步骤中，选择高级设置并在“节点启动配置”中输入如下内容：
```
echo  '172.21.17.69  demo.tencentcloudcr. com' >> /etc/hosts
```
**为已有集群配置节点 Host**
登录集群各个节点，并执行以下命令：
```
echo 172.21.17.69 demo. tencentcloudcr.com' >> /etc/hosts
```
 `172.21.17.69` 及 `demo.tencentcloudcr.com` 请替换为您实际使用的内网解析 IP 及 TCR 实例域名。

### 步骤3：使用 TCR 实例内容器镜像创建工作负载
1. 已登录 [边缘计算平台](https://console.cloud.tencent.com/iecp)。单击左侧导航栏中**边缘单元**，进入“边缘单元”页面。
2. 单击需要安装节点的单元**管理**，进入该单元详情页。
3. 选择页面左侧**应用管理** > **工作负载**/**Grid 应用**，进入工作负载/Grid应用列表页面，单击**新建应用**
	a. 主要参数信息如下，其他参数请按需设置：命名空间：选择已下发访问凭证的命名空间。
	b. 实例内容器：镜像：单击选择镜像，并在弹出的“选择镜像”窗口中，选择 容器镜像服务 企业版，再根据需要选择地域、实例和镜像仓库。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/c268b072042c9470947f9fd369bf0ffa.png)
	i.	镜像版本：选择好镜像后，单击选择镜像版本，在弹出的“选择镜像版本”窗口中，根据需要选择该镜像仓库的某个版本。若不选择则默认为latest。
4.	完成其他参数设置后，单击确认即可完成工作负载/Grid应用的创建
