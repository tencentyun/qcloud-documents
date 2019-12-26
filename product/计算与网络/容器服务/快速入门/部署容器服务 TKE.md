## 操作场景
腾讯云容器服务（Tencent Kubernetes Engine，TKE）是高度可扩展的高性能容器管理服务，您可以在托管的云服务器实例集群上轻松运行应用程序。在本教程中，您将了解如何使用容器服务快速创建和管理容器集群，并在集群内快速、弹性地部署您的服务。

## 操作步骤
### 创建集群
首先您需要创建集群。集群是指容器运行所需云资源的集合，包含了若干台云服务器、负载均衡器等腾讯云资源。
1. 登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/tke2)，单击左侧导航栏中的【集群】。
2. 在“集群管理”页面中，单击集群列表页上方的【新建】。如下图所示：
![](https://main.qcloudimg.com/raw/2030c77934c3420929e96949a58b941d.png)
3. 在“创建集群”页面，设置集群的基本信息，并单击【下一步】。如下图所示：
 - **集群名称**：输入要创建的集群的名称，不超过60个字符。
 - **新增资源所属项目**：根据实际需求进行选择，新增的资源将会自动分配到该项目下。
 - **Kubernetes版本**：提供多个 Kubernetes 版本选择，前往 [Supported Versions of the Kubernetes Documentation](https://kubernetes.io/docs/home/supported-doc-versions/) 查看各版本特性对比。
 - **运行时组件**：提供 “docker” 和 “containerd” 两种选择，详情请参见 [如何选择 Containerd 和 Docker](https://cloud.tencent.com/document/product/457/35747)。
 - **所在地域**：建议您根据所在地理位置选择靠近的地域。可降低访问延迟，提高下载速度。
 - **集群网络**：为集群内主机分配在节点网络地址范围内的 IP 地址。具体操作请参阅 [容器及节点网络设置](https://cloud.tencent.com/document/product/457/9083)。
 - **容器网络**：为集群内容器分配在容器网络地址范围内的 IP 地址。具体操作请参阅 [容器及节点网络设置](https://cloud.tencent.com/document/product/457/9083)。
 - **镜像提供方**：根据实际需求进行选择。
 - **操作系统**：根据实际需求进行选择。
 - **集群描述**：填写集群的相关信息，该信息将显示在**集群信息**页面。
 - **高级设置**：可设置 ipvs。
 ipvs 适用于将在集群中运行大规模服务的场景，开启后不能关闭。具体操作请参阅 [集群启用 IPVS](https://cloud.tencent.com/document/product/457/32193)。
![](https://main.qcloudimg.com/raw/22730e294cc4c6db7f0ff5e2fb914b5f.png)
4. 选择机型，并单击【下一步】。如下图所示：
 - **创建集群**：根据实际需求进行选择。
 - **Master**：Master 的部署方法决定了您集群的管理模式，我们提供“托管”和“独立部署”两种集群模式选择，详情请参见 [集群类型](https://cloud.tencent.com/document/product/457/32187#.E9.9B.86.E7.BE.A4.E7.B1.BB.E5.9E.8B)。
 - **Node**：Node 配置的是集群运行服务真正使用的工作节点。您可以在创建集群时购置云服务器作为 Node 节点，也可以在集群创建完成后再添加 Node 节点。
 - **计费模式**：提供按量计费和包年包月两种计费模式，详情请参见 [计费模式](https://cloud.tencent.com/document/product/213/2180)。
 - **Node机型**：当 “**Node**” 选择为“**新增**”时可选。您可以选择已有的云服务器作为 Node 节点，也可以在集群创建完成后再添加 Node 节点。
![](https://main.qcloudimg.com/raw/d8ab3e98f9ac97bcccf2cee7bf3a9215.png)
5. 填写云服务器配置，并单击 【下一步】。如下图所示：
 - **数据盘挂载**：请根据您的实际需求进行勾选。勾选后，会进行以下操作：
    - 会将数据盘自动挂载到您指定的挂载点，并自动格式化为 ext4 文件系统格式。
    - 会将容器存储到挂载点的容器目录。
    - 此选项仅对拥有一块数据盘的节点生效。
 - **安全组**：安全组具有防火墙的功能，用于设置云服务器的网络访问控制。详情请参见  [容器服务安全组设置](https://cloud.tencent.com/document/product/457/9084) 。
 - **登录方式**：提供三种登录方式。
    - **设置密码**：请根据提示设置对应密码。
    - **立即关联密钥**：密钥对是通过算法生成的一对参数，是一种比常规密码更安全的登录云服务器的方式。详情请参见  [SSH 密钥](https://cloud.tencent.com/document/product/213/6092)。
    - **自动生成密码**：自动生成的密码将通过站内信发送给您。
 - **自动调节**：可自动创建最大节点数为2的伸缩组。
![](https://main.qcloudimg.com/raw/df4c4bf407f1d01cdc81850b84c9adfe.png)
6. 确认配置信息，并单击【完成】，即可完成集群创建。如下图所示：
![](https://main.qcloudimg.com/raw/eb8bbe8cc2073b14f6a979309bb091c4.png)
7. 创建完成的集群将出现在集群列表中。
![](https://main.qcloudimg.com/raw/2ed7cbabf7dbb4bc3ecc23b0c102c1d5.png)

### 创建服务
您现已创建了集群，接下来就是创建服务。服务是由多个相同配置的容器和访问这些容器的规则组成的微服务。
1. 单击需要创建服务的集群 ID，进入工作负载 Deployment 详情页，单击【新建】。如下图所示：
![](https://main.qcloudimg.com/raw/c1ab530a5629036aa235e2b178cda652.png)
2. 设置工作负载基本信息。如下图所示：
 - **工作负载名**：要创建的工作负载的名称。
 - **描述**：填写工作负载的相关信息。
 - **标签**：key = value 键值对，本例中标签默认值为 k8s-app = 工作负载名 。
 - **命名空间**：根据实际需求进行选择。
 - **类型**：根据实际需求进行选择。
![](https://main.qcloudimg.com/raw/e28e621a11ff5e99aa7ad2349634f57b.png)
3. （可选）设置数据卷，要指定容器挂载至指定路径时，单击【添加数据卷】，详情查看 [Volume 管理](https://cloud.tencent.com/document/product/457/31713)。如下图所示：
>!源路径不指定时将默认分配临时路径。
> 
 - 类型：支持使用临时目录、主机路径、NFS盘、已有VPC、腾讯云硬盘、ConfigMap、Secret七种类型的数据卷。相关详细介绍请参阅 [Volume 管理](https://cloud.tencent.com/document/product/457/31713)。
 - 名称：数据卷的名称。
![](https://main.qcloudimg.com/raw/7d69d00f2b00b4d0d3a12c49fbbabaa7.png)
4. 设置**实例內容器**。如下图所示：
 - **名称**：输入要创建容器的名称。
 - **镜像**：单击【选择镜像】，可在我的镜像、我的收藏、TencentHub 镜像、DockerHub 镜像和其他镜像下选择。
 - **镜像版本（Tag）**：容器服务默认选择版本。如果您需要使用镜像的其它版本，单击版本显示框选择。
 - **CPU/内存限制**：Request 用于预分配资源，当集群中的节点没有 request 所要求的资源数量时，容器会创建失败。Limit 用于设置容器使用资源的最大上限，避免异常情况下节点资源消耗过多。
 - **GPU限制**：根据实际需要设置。
 - **环境变量**：变量名只能包含大小写字母、数字及下划线，并且不能以数字开头。
![](https://main.qcloudimg.com/raw/bb379e8f502bb81375cd3b1fcb5649d9.png)
5. 设置**实例数量**。如下图所示：
 - 手动调节：设定实例数量，本文实例数量设置为1。可单击“+”或“-”控制实例数量。
 - 自动调节：满足任一设定条件，则自动调节实例（pod）数目。详情请参见 [服务自动扩缩容]()。
![](https://main.qcloudimg.com/raw/43ec0d5015d4ed9a73741d67194fc523.png)
6. 进行访问设置。如下图所示：
 - **Service**：勾选“启用”。
 - **服务访问方式**：服务的访问方式决定了这个服务的网络属性，不同访问方式的服务可以提供不同网络能力。提供的四种访问方式详细介绍请参阅 [服务访问方式设置](https://cloud.tencent.com/document/product/457/9098)。
 - **负载均衡器**：根据实际需求进行选择。
 - **端口映射**：选择**协议**，填写**容器端口**和**服务端口**。
![](https://main.qcloudimg.com/raw/9108be0e87972cace70db6f2d88ada35.png)
7. 单击【创建Workload】，完成服务的创建。创建完成的服务将出现在服务列表中。

#### 查看资源
在上述步骤中，您创建了集群、服务。在此步骤中，您将查看您所创建的资源。
#### 查看集群
1. 单击左侧导航栏中的【集群】，选择集群列表页集群的 ID。如下图所示：
![](https://main.qcloudimg.com/raw/6538c2c2b3d0317aa6565b0252af1d01.png)
2. 单击后显示以下内容，其中界面默认显示 Deployment 详情页。如下图所示：
 - **基本信息**：显示了集群的基本信息。
 - **节点管理**：节点是一台已注册到集群内的云服务器。可以进行新建节点、添加已有节点、新建伸缩等的操作。
 - **命名空间**：命名空间是对一组资源和对象的抽象集合。可以对命名空间进行新建和删除操作。
 - **工作负载**、**服务**、**配置管理**、**存储**：Kubernetes 常用资源对象，详情请参见 [对象分类](https://cloud.tencent.com/document/product/457/31700#.E5.AF.B9.E8.B1.A1.E5.88.86.E7.B1.BB)。
 - **日志**：显示相关日志信息。
 - **事件**: 创建服务时会跳转至此页面，显示服务创建时流水事件。
![](https://main.qcloudimg.com/raw/7935bbbde94b7792d49f6f0891d03624.png)

### 查看服务
1. 单击左侧导航栏中【集群】，进入“集群管理”页面。
2. 单击已创建服务所在的集群 ID，选择【服务】>【Service】。如下图所示：
![](https://main.qcloudimg.com/raw/a99b77041c76ebb1cfefc346f2474d16.png)
3. 单击 ”Service“ 列表页中的服务名称，进入服务详情页。如下图所示：
 - **详情**：显示 Service 基本信息、高级设置信息。
 - **事件**：显示 Service 最近1小时内发生的事件信息。
 - **YAML**:可通过编辑 YAML 以更新 Service 。
![](https://main.qcloudimg.com/raw/a3e561c8d6c26482fa70d3712e950c50.png)

### 删除资源
在本教程中，启动了两种资源：集群和服务。在此步骤中，您将清除所有的资源以免产生不必要的费用。
#### 删除集群
1. 单击左侧导航栏中的【集群】，选择需删除集群列表右侧【更多】>【删除】。如下图所示：
![](https://main.qcloudimg.com/raw/6b8048359485601d8625d3a477c7872a.png)
2. 在弹出框中确认信息后，单击【确定】即可删除集群。如下图所示：
>!
>- 集群在删除期间，无法对外提供服务，请提前做好准备，以免造成影响。
>- 删除集群，则该集群内的 Service 也随即被删除。
>
![](https://main.qcloudimg.com/raw/5545bd2fa5728b7cdcfbe780c5fecc46.png)


#### 删除服务
1. 单击左侧导航栏中【集群】，进入集群管理页面。
2. 单击需要删除的 Service 所在的集群 ID，进入该集群详情页。
3. 选择【服务】>【Service】，进入 Service 信息页面。
4. 单击 Service 列表右侧的【删除】。如下图所示：
![](https://main.qcloudimg.com/raw/ed65f1fa96dc1506472d9adb986071d9.png)
5. 在弹出框中单击【确定】，即可删除服务。

### 更多
通过本教程，您已经了解如何在腾讯云容器服务 TKE 中配置、部署和删除服务。使用腾讯云容器服务 TKE，您将无需安装、运维、扩展您的集群管理基础设施，只需进行简单的 API 调用，便可启动和停止 Docker 应用程序，查询集群的完整状态，以及使用各种云服务。

您可进入下一个教程，了解 [负载均衡](https://cloud.tencent.com/document/product/457/9110) 和 [镜像仓库](https://cloud.tencent.com/document/product/457/9118) 的基本概念和操作，通过 [入门示例](https://cloud.tencent.com/document/product/457/11138) 快速构建服务。

                                          
