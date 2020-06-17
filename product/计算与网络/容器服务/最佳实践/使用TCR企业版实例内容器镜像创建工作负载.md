## 操作场景
腾讯云容器镜像服务（Tencent Container Registry，TCR）企业版面向具有严格数据安全及合规性要求、业务分布在多个地域、集群规模庞大的企业级容器客户，提供企业级的独享镜像安全托管服务。相较于个人版服务，企业版支持容器镜像安全扫描、跨地域自动同步、Helm Chart 托管、网络访问控制等特性，详情请参见 [容器镜像服务](https://cloud.tencent.com/document/product/1141)。

本文介绍如何在容器服务 TKE 中，使用容器镜像服务 TCR 内托管的私有镜像进行应用部署。

## 前提条件
在使用 TCR 内托管的私有镜像进行应用部署前，您需要完成以下准备工作：
- 已在 [容器镜像服务](https://console.cloud.tencent.com/tcr) 创建企业版实例。如尚未创建，请参考 [创建企业版实例](https://cloud.tencent.com/document/product/1141/40716) 完成创建。
- 如果使用子账号进行操作，请参考 [企业版授权方案示例](https://cloud.tencent.com/document/product/1141/41417) 提前为子账号授予对应实例的操作权限。


## 操作步骤
### 搭建容器镜像
#### 创建命名空间
新建的 TCR 企业版实例内无默认命名空间，且无法通过推送镜像自动创建。请参考 [创建命名空间](https://cloud.tencent.com/document/product/1141/41803#.E5.88.9B.E5.BB.BA.E5.91.BD.E5.90.8D.E7.A9.BA.E9.97.B4) 按需完成创建。
建议命名空间名使用项目或团队名，本文以 `test-tcr` 为例。创建成功后如下图所示：
![](https://main.qcloudimg.com/raw/a018496ebe9ab02ee9282107cc3cac90.png)

#### 创建镜像仓库（可选）
容器镜像托管在具体的镜像仓库内，请参考 [创建镜像仓库](https://cloud.tencent.com/document/product/1141/41811#.E5.88.9B.E5.BB.BA.E9.95.9C.E5.83.8F.E4.BB.93.E5.BA.93) 按需完成创建。镜像仓库名称请设置为期望部署的容器镜像名称，本文以 `nginx` 为例。创建成功后如下图所示：
>?通过 docker cli 或其他镜像工具，例如 jenkins 推送镜像至企业版实例内时，若镜像仓库不存在，将会自动创建，无需提前手动创建。
>
![](https://main.qcloudimg.com/raw/65e3728533122fb77940e3b2b7dc15e1.png)

#### 推送容器镜像
您可通过 docker cli 或其他镜像构建工具，例如 jenkins 推送镜像至指定镜像仓库内，本文以 docker cli 为例。此步骤需要您使用一台安装有 Docker 的云服务器或物理机，并确保访问的客户端已在 [配置网络访问策略]() 定义的公网或内网允许访问范围内。
1. 参考 [获取实例访问凭证](https://cloud.tencent.com/document/product/1141/41829) 获取登录指令，并进行 Docker Login。
2. 登录成功后，您可在本地构建新的容器镜像或从 DockerHub 上获取一个公开镜像用于测试。
本文以 DockerHub 官方的 Nginx 最新镜像为例，在命令行工具中依次执行以下指令，即可推送该镜像。请将 demo-tcr、test-tcr 及 nginx 依次替换为您实际创建的实例名称、命名空间名称及镜像仓库名。
```
docker tag nginx:latest demo-tcr.tencentcloudcr.com/project-a/nginx:latest
```
```
docker push demo-tcr.tencentcloudcr.com/project-a/nginx:latest
```
推送成功后，即可前往控制台的 “[镜像仓库](https://console.cloud.tencent.com/tcr/repository)” 页面，选择仓库名进入详情页面查看。如下图所示： 
![](https://main.qcloudimg.com/raw/f1eb1852825f857ed66d8404ddbc9c1d.png)

### 配置 TKE 集群访问 TCR 实例<span id="deployTKE"></span>
TCR 企业版实例支持网络访问控制，默认拒绝全部来源的外部访问。您可根据 TKE 集群的网络配置，选择通过公网或内网访问指定实例，拉取容器镜像。

#### 公网访问
当集群节点具备公网访问能力时，可配置 TKE 集群通过公网拉取容器镜像。
1. 参考 [开启公网入口](https://cloud.tencent.com/document/product/1141/41837#.E5.BC.80.E5.90.AF.E5.85.AC.E7.BD.91.E8.AE.BF.E9.97.AE.E5.85.A5.E5.8F.A3)，开通指定实例的公网访问入口。
2. 参考 [配置访问策略](https://cloud.tencent.com/document/product/1141/41837#.E9.85.8D.E7.BD.AE.E8.AE.BF.E9.97.AE.E7.AD.96.E7.95.A5) 配置公网访问白名单，可将集群节点的公网 IP 加入至白名单内。如不确认集群节点的公网 IP，可通过配置 `0.0.0.0/0` 放通全部公网来源的访问。
3. 完成以上配置后，登录集群节点并执行以下命令，验证集群节点是否可以正常访问该实例。
```
docker login xxxxxx.tencentcloudcr.com
```
请将 `xxxxx` 替换为您实际使用的 TCR 实例名称。

#### 内网访问
如果 TKE 集群与 TCR 实例部署在同一地域，建议通过内网访问方式拉取容器镜像，可提升拉取速度，并节约公网流量成本。
1. 参考 [内网访问控制](https://cloud.tencent.com/document/product/1141/41838)，配置 TCR 实例与 TKE 集群所在私有网络 VPC 的内网链路。
2. 建立 TCR 实例与 TKE 集群所在私有网络的内网链路后，还需要在 TKE 集群中配置 TCR 实例的域名解析。请根据您的实际情况，选择以下方案：
 - **创建集群时配置节点 Host**
 在创建 TKE 集群的“云服务器配置”步骤中，选择【高级设置】并在“节点启动配置”中输入如下内容：
```
echo '172.21.17.69 demo.tencentcloudcr.com' >> /etc/hosts
```
 - **为已有集群配置节点 Host**
登录集群各个节点，并执行以下命令：
```
echo '172.21.17.69 demo.tencentcloudcr.com' >> /etc/hosts
```
>?`172.21.17.69` 及 `demo.tencentcloudcr.com` 请替换为您实际使用的内网解析 IP 及 TCR 实例域名。
>


### 下发 TCR 实例的访问凭证<span id="issued"></span>
在 TKE 集群内的节点上拉取 TCR 实例内的容器镜像时，需通过 TCR 实例的访问凭证访问该实例。请根据您的实际情况，选择以下方案，在集群的命名空间内下发 TCR 实例的访问凭证。

#### 新建命名空间并下发访问凭证
1. 登录容器服务控制台，选择左侧导航栏中的【[集群](https://console.cloud.tencent.com/tke2/cluster)】。
2. 在“集群管理”页面，选择集群 ID，进入集群详情页。
3. 选择左侧的【命名空间】，进入 “Namespace” 页面并单击【新建】。
4. 进入“新建Namespace” 页面，勾选“自动下发容器镜像服务企业版访问凭证”，并选择该集群需访问的 TCR 实例。如下图所示：
![](https://main.qcloudimg.com/raw/d4c21b05217a1b2d715fd3632e77a241.png)
5. 单击【创建Namespace】进行创建。
创建完成后，该实例的访问凭证将自动下发至该命名空间。可选择左侧的【配置管理】>【Secret】，进入 “Secret” 页面即可查看该访问凭证。例如 `1000090225xx-tcr-m3ut3qxx-dockercfg`。其中，`1000090225xx` 为创建命名空间的子账号 uin，`tcr-m3ut3qxx` 为所选实例的实例 ID。


#### 向已有命名空间下发访问凭证
1. <span id="loginInfo"></span>参考 [获取实例访问凭证](https://cloud.tencent.com/document/product/1141/41829)，获取用户名及密码。
2. 在集群详情页，选择左侧的【配置管理】>【Secret】，进入 “Secret” 页面。
3. 在 “Secret” 页面单击【新建】进入“新建Secret” 页面，参考以下信息下发访问凭证。如下图所示：
![](https://main.qcloudimg.com/raw/3521ba5ef8437b52586411eb505d344a.png)
主要参数信息如下：
 - **Secret类型**：选择【Dockercfg】。
 - **生效范围**：勾选需下发凭证的命名空间。
 - **仓库域名**：填写 TCR 实例的访问域名。
 - **用户名、密码**：填写 [步骤1](#loginInfo) 已获取的用户名及密码。
4. 单击【创建Secret】即可完成下发。

### 使用 TCR 实例内容器镜像创建工作负载
1. 在集群详情页面，选择左侧【工作负载】>【Deployment】。
2. 进入 “Deployment” 页面，并单击【新建】。
3. 进入“新建Workload” 页面，参考以下信息创建工作负载。
主要参数信息如下，其他参数请按需设置：
 - **命名空间**：选择已下发访问凭证的命名空间。
 - **实例内容器**：
    - **镜像**：单击【选择镜像】，并在弹出的“选择镜像”窗口中，选择 TCR 实例内容器镜像。如下图所示：
    ![](https://main.qcloudimg.com/raw/20018062f1498872191eb75e0a70e5ac.png)
 - **镜像访问凭证**：选择【添加镜像访问凭证】，并选择 [下发 TCR 实例的访问凭证](#issued) 步骤中已下发的访问凭证。如下图所示：
![](https://main.qcloudimg.com/raw/788c33fe1f2a6042f06c0daded949494.png)
4. 完成其他参数设置后，单击【创建workload】后查看该工作负载的部署进度。
部署成功后，可在 “Deployment” 页面查看该工作负载的“运行/期望Pod数量”为“1/1”。如下图所示：
![](https://main.qcloudimg.com/raw/0223f408f2a3434f8a61389f4b6d8d87.png)
如果出现镜像无法拉取等问题，请确认 [配置 TKE 集群访问 TCR 实例](#deployTKE) 及 [下发 TCR 实例的访问凭证](#issued) 步骤是否已完成。


