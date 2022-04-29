## 操作场景

TSF 支持 K8S 原生部署方案，当您通过 K8S 部署业务后，使用该功能，您可以实现仅通过页面简单配置或 K8S yaml 的少量修改，将您的应用快速接入 TSF，保留原有 K8S 部署发布全流程，并且您可以使用 TSF 的服务注册发现、服务治理、可观测性等一系列能力。



### 步骤1：在 TKE 控制台创建集群

参考 [创建集群](https://cloud.tencent.com/document/product/457/32189) 和 [Deployment 管理](https://cloud.tencent.com/document/product/457/31705) 在容器服务 TKE 控制台创建集群和 Deployment 并正常运行。

### 步骤2：导入容器服务集群到 TSF

1. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf/index)。
2. 在左侧导航栏中，单击 **[集群](https://console.cloud.tencent.com/tsf/cluster)**。
3. 在集群列表页的左上方，单击**新建集群**。
4. 设置集群的基本信息。
   - 集群类型：选择**容器集群**。
   - **集群名称**：集群名称，不超过60个字符。
   - **新建类型：**选择**导入容器服务 TKE 集群**。
   - **所在可用区**：选择容器服务集群所在的可用区。
   - **选择集群：**选择要导入的容器集群服务。
   - **标签**：用于分类管理资源，可不选。详情参见 [标签](https://cloud.tencent.com/document/product/649/53869)。
   - **备注**：集群的描述，不超过200个字符。
   - **数据集**：将新建的集群添加到已有数据集中。非必填字段。数据集使用，请参见 [数据集管理](https://cloud.tencent.com/document/product/649/38326)。
     ![](https://qcloudimg.tencent-cloud.cn/raw/4e4faa5ccf3ead6b2acafb2e7e912e20.png)
5. 单击**提交**，在弹窗中选择**导入云主机**前往导入云主机页面。
6. 从集群所在 VPC 的云主机列表中，选择需要添加到集群的云主机。
7. 选择导入方式，并根据页面提示完成操作。
   - 重装系统：该方式会使用 root 用户安装 agent。
   - 安装 Agent（仅适用于虚拟机集群）： 该方式支持使用 root 用户和非 root 用户安装 agent。

   

### 步骤3：应用改造

参考开发指南对您的应用进行改造:

- [应用使用 TSF SDK接入](https://cloud.tencent.com/document/product/649/36285)
- [原生 Spring Cloud 应用](https://cloud.tencent.com/document/product/649/54147)
- [Service Mesh 应用接入](https://cloud.tencent.com/document/product/649/17928)



### 步骤4：导入 Deployment 到 TSF

> ? 
>
> 单击开启后，我们将对您的集群进行组件安装，期间不影响集群正常运行，安装组件最少需要64MB内存 和0.1核 CPU。
>
> 当您单击导入 TSF 时，我们将**为您重启 Deployment**，请选择业务低谷期进行操作。
> 
1. 在集群列表页面，单击的集群的“ID”，进入云主机列表页面。
2. 在页面上方选择 **K8S 原生部署**页签，单击**开始使用**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/12492b601ca814b8cfc6fbc4a567faeb.png)
3. 在 Deployment 列表页面，选择好命名空间，单击您要导入的 Deployment 操作列的**导入 TSF**。
4. 在弹窗中填写导入的应用信息。
   - 导入后应用名称：填写导入后的应用名称，不超过60字符。
   - 应用类型：选择导入应用类型
     - 应用使用 TSF SDK接入：使用 TSF SDK 接入，支持 TSF 全栈服务治理、应用性能监控、应用配置管理能力。
     - 原生 Spring Cloud 应用：原生 Spring Cloud 应用0代码改造即可接入，支持服务发现、服务治理、应用性能监控能力。
     - Service Mesh 应用接入：使用 Service Mesh 技术支持全套 TSF 服务治理能力，无需修改代码。
   - TSF Agent：我们将为您在集群中安装 TSF Agent 以使⽤平台提供的服务治理、配置管理、可观测性等能⼒。将在您⼯作负载重启后⽣效。
   - Agent 占⽤资源：
     - request 用于预分配资源，当集群中的节点没有 request 所要求的资源数量时，会导致无法创建容器。
     - limit 用于设置容器使用资源的最大上限，避免异常情况下节点资源消耗过多。
   ![](https://qcloudimg.tencent-cloud.cn/raw/e3fbc1ae8545ef74a29a1031a1ccce39.png)
5. 单击**提交**，等待导入完成。
<dx-alert infotype="explain" title="">
- 导入完成后，会自动给用户创建好应用和部署组，重启应用后应用会注册到 TSF 注册中心。
- 通过 K8S 原生部署导入 Deployment 后， 不支持在 TSF 自动创建的部署组页面进行增删改操作，建议继续在TKE 页面进行操作。
- 对于在 TKE 页面创建的命名空间，开启 K8S 原生部署后，也不支持在该命名空间下新建部署组。
</dx-alert>



   
