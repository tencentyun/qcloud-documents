## 操作场景

原生 Spring Cloud 应用0代码改造即可接入，支持服务发现、服务治理、应用性能监控能力。如果您想了解如何实现微服务应用的相关功能，请参见 [Spring Cloud 原生应用开发](#building)。

为了帮助您快速体验如何在 TSF 中部署微服务应用，TSF 提供了一对应用 Demo，包含一个 provider 应用和一个 consumer 应用。本文以一个示例介绍如何在容器环境中部署 Spring Cloud 原生应用，并实现简单的服务调用。

## 前提条件

- 已参见 [快速创建一个容器集群](https://cloud.tencent.com/document/product/649/55505) 创建好一个容器集群并导入可用的云主机。
- 已下载并解压 [应用 Demo](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91/%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8/tsf-native-app-demo.zip) 。



[](id:building)
## 操作步骤

[](id:step1)
### 步骤1：新建应用

1. 在左侧导航栏，单击**应用管理**，进入应用列表页。
2. 在应用列表上方单击**新建应用**。
3. 设置应用信息，单击**提交**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/0f6178e9a64295021a81b3319cfb1301.png)
   - **应用名**：填写 consul-provider。
   - **部署方式**：选择 **容器部署**。
   - **业务类型**：选择 **业务应用**。
   - **开发语言**：选择 **JAVA**。
   - **开发框架**：选择 **SpringCloud**。
   - **应用类型**：选择 **原生应用**。
   - **标签**：用于分类管理资源，可不选。详情参见 [标签](https://cloud.tencent.com/document/product/649/53869)。
   - **数据集**：选择“无”。用户可以通过数据集管理配置不同的子账号和协作者使用不同资源的权限，详情参阅 [数据集管理](https://cloud.tencent.com/document/product/649/38326)。
   - **备注**：选填，可留空。
4. 在弹出的弹窗中单击**确认**，前往上传镜像并部署应用。
   ![](https://main.qcloudimg.com/raw/761b87560d72e3a9e4b00a0d3b05a3b3.png)




[](id:step2)
### 步骤2：上传镜像

1. 在镜像标签页面，单击**上传程序包/镜像**。
2. 在个人仓库上传程序包页面，上传程序包。
   - 文件上传方式：选择**JAR包部署**。
   - 上传程序包：单击**选择文件**，选择提前准备好的 Demo 中的`consul-provider-0.1.1-SNAPSHOT` 的 jar 程序包。
   - 程序包版本：填写版本号，或单击**用时间戳作为版本号**。
   - 备注：填写备注。
3. 单击**上传程序包并制作镜像**，我们将自动为您制作镜像并上传到镜像仓库，右上角将出现任务进行的状态。
4. 任务完成后，在镜像标签页的镜像列表中将看到上传好的镜像。
   ![](https://qcloudimg.tencent-cloud.cn/raw/9cf71fbd34591f129d6aec5187e1ec2c.png)



### 步骤3：部署应用

1. 在应用列表中，单击在 [步骤1. 新建应用]() 中创建的应用的 “ID”。
2. 在部署组页面，单击**新建部署组**，设置部署组相关信息。
   - **组名**：填写 **consumer**。
   - **集群**：选择提前创建好的集群。
   - **命名空间**：选择集群关联的默认命名空间。
   - **日志配置项**：用于采集应用的业务日志数据，此处可选择**无**。关于日志配置项的使用说明可参见 [日志配置项](https://cloud.tencent.com/document/product/649/13697)。
   - **日志投递**：用于日志转储，此处可选择**无**。关于日志投递的详情说明可参见 [日志投递](https://cloud.tencent.com/document/product/649/43510)。
   - **标签**：用于分类管理资源，可不选。详情参见 [标签](https://cloud.tencent.com/document/product/649/53869)。
   - **备注**：选填，可留空。
3. 单击**保存&下一步**，进入部署应用页面。
4. 设置部署相关信息。![](https://qcloudimg.tencent-cloud.cn/raw/02fb4dca525aeebb28881605979bdf6a.png)
   ![](https://qcloudimg.tencent-cloud.cn/raw/4be95528fb0e3abc94fbce0952ddfef8.png)
   - **选择镜像**：选择 [步骤2：上传镜像](#step2) 中推送到镜像仓库的镜像版本。
   - **启动参数**（选填）：设置 Java 应用的启动参数。
   - **资源配置**：应用容器的 CPU 和内存限制使用默认值即可，实例数设置为1。
   - **访问配置**： 
     - 网络访问方式决定了部署组内应用的网络属性，不同访问方式的应用可以提供不同网络能力。此处设置**主机端口访问**。
     - 端口映射中选择 TCP 协议，容器端口和服务端口设置为8002。
5. 单击**提交**，完成应用部署。应用部署成功后，部署组中**运行中/预期服务实例数**的数值发生变化。
![](https://qcloudimg.tencent-cloud.cn/raw/132fff28e0b96a4c6336a0dc4a44fde3.png)
6. 在服务治理页面，选择地域和应用关联的命名空间后，可以看到服务实例显示在线状态，表示服务注册成功。
![](https://qcloudimg.tencent-cloud.cn/raw/717ba963c88dafa06c515b1974c02a79.png)
7. 在服务列表页单击服务的“ID”，进入服务详情页，单击**接口列表**标签页，可以查看上报的 API 定义。



### 步骤4：验证服务调用

使用与之前相同的流程部署一组 consumer 和 provider（如 consul-consumer 和 consul-provider）。

![](https://qcloudimg.tencent-cloud.cn/raw/a3c34fd757772d91ed481b3c22c60a1c.png)

#### 请求 consumer 来调用 provider
 
1. 在 [部署组](https://console.cloud.tencent.com/tsf/group) 列表页面，单击 consumer 部署组的“ID”，进入服务实例列表页面。
2. 在页面上方选择“基本信息”页签，在**服务访问**模块获取**主机端口（NodePort）**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/cd18036b18fbfeed6cfcdf074302a3c9.png)
3. 在集群 [云主机列表](https://console.cloud.tencent.com/tsf/cluster-detai) 页面，获取集群中任一云主机的 IP的公网IP。
   ![](https://qcloudimg.tencent-cloud.cn/raw/d4b04af6d50cbb6ee952db72227469a5.png)
4. 单击云主机操作栏的**登录**，输入登录密码，登录云服务器。
5. 执行 curl 命令调用 provider 服务，其中`<云主机 IP> `和 `<NodePort> `为上述步骤获取的主机端口（NodePort）和云主机公网 IP。
   ```
   curl <云主机 IP>:<NodePort>/ping-provider
   ```
   调用结果如下：
   ![](https://qcloudimg.tencent-cloud.cn/raw/3c923e211320e782c7b1a51923dbe627.png)

   

#### 在 TSF 控制台查看服务依赖拓扑图

1. 在 [服务治理](https://console.cloud.tencent.com/tsf/service) 页面，选择创建集群和命名空间后，可以看到 consul-provider 和 consul-consumer 服务的运行状况。服务状态为**在线**或**单点在线**，表示服务被代理注册成功。如果服务提供者的请求量大于0，请求成功率为100%，表示服务提供者被服务消费者请求成功。
![](https://qcloudimg.tencent-cloud.cn/raw/1863ea23c6afb8fc0156b0f16f9ccd84.png)
2. 在服务治理页面，单击 consul-consumer 服务的“ID”，进入服务详情页面，可以看到两个服务的依赖关系。
   ![](https://qcloudimg.tencent-cloud.cn/raw/3ae53795483ce0bebe227a461a4825f9.png)
   在选中时间范围内，consul-consumer 调用了 consul-provider 服务，调用成功比例为 100% （绿色部分）。


