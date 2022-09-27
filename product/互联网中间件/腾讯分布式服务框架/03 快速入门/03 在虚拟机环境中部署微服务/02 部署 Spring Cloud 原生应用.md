## 操作场景

原生 Spring Cloud 应用0代码改造即可接入 TSF，支持服务发现、服务治理、应用性能监控能力。如果您想了解如何实现微服务应用的相关功能，请参见 [Spring Cloud 原生应用开发](#building)。

为了帮助您快速体验如何在 TSF 中部署微服务应用，TSF 提供了一对应用 Demo，包含一个 provider 应用和一个 consumer 应用。本文以一个示例介绍如何在虚拟机环境中部署 Spring Cloud 原生应用，并实现简单的服务调用。

## 前提条件

已参见 [快速创建一个虚拟机集群](https://cloud.tencent.com/document/product/649/55498) 创建好一个虚拟机集群并导入可用的云主机。

[](id:building)
## 部署应用

1. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf/index)。
2. 在左侧导航栏，单击**应用管理**，选择好地域后，在应用列表上方单击**新建应用**。
3. 设置应用信息，单击**提交**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/3c9664a3ad8e09ee60fbe46dcfcc340c.png)
   - **应用名**：填写 **consul-provider**。
   - **部署方式**：选择 **虚拟机部署**。
   - **业务类型**：选择 **业务应用**。
   - **开发语言**：选择 **JAVA**。
   - **开发框架**：选择 **SpringCloud**。
   - **应用类型**：选择 **原生应用**。
   - **标签**：用于分类管理资源，可不选。详情参见 [标签](https://cloud.tencent.com/document/product/649/53869)。
   - **数据集**：选择“无”。用户可以通过数据集管理配置不同的子账号和协作者使用不同资源的权限，详情参阅 [数据集管理](https://cloud.tencent.com/document/product/649/38326)。
   - **备注**：选填，可留空。
4. 在弹出的提醒弹窗中选择**使用官方Demo新建部署组**，进入新建部署组页面。
   ![](https://qcloudimg.tencent-cloud.cn/raw/397a105521f6d0cad136e7054b914c8c.png)
5. 在新建部署组页面，填写部署组信息。
   - **组名**：部署组的名称，不超过60个字符。
   - **集群**：选择提前创建好的集群。
   - **命名空间**：选择集群关联的默认命名空间。
   - **日志配置项**：应用的日志配置项用于指定 TSF 采集应用的日志路径。此处可选择**无**。参见 [日志服务](https://cloud.tencent.com/document/product/649/13697)。
   - **日志投递**：用于日志转储，此处可选择**无**。关于日志投递的详情说明可参见 [日志投递](https://cloud.tencent.com/document/product/649/43510)。
   - **标签**：用于分类管理资源，可不选。详情参见 [标签](https://cloud.tencent.com/document/product/649/53869)。
   - **备注**：选填，可留空。
6. 单击**保存&下一步**，从关联集群的可用云主机列表勾选用于部署的云主机。
7. 单击**部署应用**，设置部署信息。
   ![](https://qcloudimg.tencent-cloud.cn/raw/2b68e2409d34b0ad72b958bd44c7e770.png)
   - 软件仓库：选择**官网Demo（公共仓库）**。
   - 程序包类型：选择 **jar**。
   - JDK 版本：选择 **KONA JDK8**。
   - 程序包类型：选择名称为`consul-provider-0.1.1-SNAPSHOT.jar `的程序包。
   - 启动参数：选填。
   - 更新方式：选择立即更新。
   - 健康检查：可选。详情参见 [健康检查](https://cloud.tencent.com/document/product/649/15525)。
   - 描述：可选。
8. 单击**完成**，应用部署成功后，部署组中**已启动/总机器数**的数值发生变化。
![](https://qcloudimg.tencent-cloud.cn/raw/c216e554c443f4aae755b880c8e85196.png)
9. 在服务治理页面，选择地域和应用关联的命名空间后，可以看到服务实例显示在线状态，表示服务注册成功。
![](https://qcloudimg.tencent-cloud.cn/raw/77ddb2ba28aa37fc440ce3b8d1b9b1f8.png)
10. 在服务列表页单击服务的“ID”，进入服务详情页，单击**接口列表**标签页，可以查看上报的 API 定义。

## 验证服务调用

使用与 [部署应用 Demo]() 相同的流程在同一个集群和命名空间下部署一个 consul-consumer 服务，可以通过以下两种方式访问触发  consul-consumer 服务调用  consul-provider 服务。

### 方式1：使用公网访问验证服务间调用

1. 在集群云主机列表页面，获取 consumer 服务所在云服务器的公网 IP。
![](https://qcloudimg.tencent-cloud.cn/raw/595b537823a3ec75324d51ee52b9e577.png)
2. 使用浏览器访问 consumer 应用的 URL 并调用 provider 服务，格式为`http://<云服务器实例公网IP>:8001/ping-provider`，返回结果如下：
   ![](https://qcloudimg.tencent-cloud.cn/raw/1db530654c9c8b62846758cbd30ab2dc.png)





### 方式2：登录云服务器验证服务间调用

1. 在集群云主机列表页面，单击 consul-consumer 服务所在云服务器操作栏的**登录**，输入登录密码，登录云服务器。
![](https://qcloudimg.tencent-cloud.cn/raw/950b6624b5f64cb55e1dc4a8af38b185.png)
2. 执行 curl 命令调用 provider 服务。
   ```
   curl localhost:8001/ping-provider
   ```
   调用结果如下：
   ![](https://qcloudimg.tencent-cloud.cn/raw/89f6a261ac71778e42c9ad531a4aa11e.png)

   

### 在 TSF 控制台查看服务依赖拓扑图

1. 在 [服务治理](https://console.cloud.tencent.com/tsf/service) 页面，选择创建集群和命名空间后，可以看到 provider 和 consumer 服务的运行状况。服务状态为**单点在线**，表示服务被代理注册成功。服务提供者的请求量大于0，请求成功率为100%，表示服务提供者被服务消费者请求成功。
![](https://qcloudimg.tencent-cloud.cn/raw/bf5677ec7b6bdfe9e394a9e743493bc2.png)
2. 在服务治理页面，单击 consumer 服务的“ID”，进入服务详情页面，可以看到两个服务的依赖关系。
   ![](https://qcloudimg.tencent-cloud.cn/raw/c3336914dfca7be6bddbd18476241750.png)
   在选中时间范围内，consul-consumer 调用了 consul-provider 服务，调用成功比例为 100% （绿色部分）。其中平均每次调用耗时7.77ms，请求频率为每分钟0.03次。




