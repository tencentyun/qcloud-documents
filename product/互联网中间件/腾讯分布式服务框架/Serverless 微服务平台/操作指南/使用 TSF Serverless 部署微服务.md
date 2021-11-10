## 操作场景

本文指导您通过 TSF 控制台，完成 TSF Serverless 部署微服务的整体操作流程。

## 操作步骤

### 步骤1：创建 Serverless 集群

首先您需要创建 Serverless 集群。集群是实例、Serverless 等云资源的集合。

1. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf/index)。
2. 在左侧导航栏中，单击**集群**，进入集群列表页。
3. 在集群列表页，单击**新建集群**。
4. 设置集群的基本信息。
	- **集群类型**：选择 **Serverless 集群**。
	- **集群名称**：集群名称，不超过60个字符。
	- **集群网络**：为集群内主机分配在云服务器网络地址范围内的 IP 地址。参阅 [私有网络和子网](https://cloud.tencent.com/document/product/215/20046)。
	- **集群描述**：集群的描述，不超过200个字符。

### 步骤2：创建 Serverless 应用

1. 在左侧导航栏，单击 **[应用管理](https://console.cloud.tencent.com/tsf/app?rid=1)**，进入应用列表。
2. 在应用列表上方单击**新建应用**。
3. 设置应用信息后，单击**提交**。
   - 部署方式：选择 **Serverless 部署**
   - 运行环境：选择 **Java8**（目前仅 Java8 支持微服务应用）

### 步骤3：上传程序包

1. 在 [应用管理列表](https://console.cloud.tencent.com/tsf/app) 页 ，单击目标应用的 **ID/应用名**，进入应用详情页。
2. 在应用详情页的上方，单击**程序包管理**标签页，单击**上传程序包**。
![](https://qcloudimg.tencent-cloud.cn/raw/d8187fa2694a5d9cae70ee27bd47aec4.png)
3. 在**上传程序包**对话框中填写相关参数。
	- 上传程序包：单击**选择文件**，选择编译为 jar 格式的程序包
	- 程序包版本：填写版本号，或单击**用时间戳作为版本号**
	- 备注：填写备注  
4. 单击**提交**，程序包上传成功后出现在程序包列表中。

### 步骤4：创建部署组

1. 在 [应用管理列表](https://console.cloud.tencent.com/tsf/app) 页 ，单击目标应用的 **ID/应用名**，进入应用详情页。
2. 单击**新建部署组**，设置部署组相关信息：
	- 部署组名称：部署组的名称，不超过60个字符。
	- 集群：选择**步骤1**中创建的集群。
	- 命名空间：选择集群关联的系统命名空间。
	- 日志配置项：应用的日志配置项用于指定 TSF 采集应用的日志路径。参考 [日志服务](https://cloud.tencent.com/document/product/649/13697)。
3. 单击**提交**。

### 步骤5：部署应用

1. 在上步操作中单击**下一步**即可完成部署，如部署失败，可在部署组列表页的右侧，单击**部署应用**重试。
   ![](https://main.qcloudimg.com/raw/ee0e779344c6f058fd181fb24c8582bc.png)
2. 选择**步骤3**中已上传成功的程序包后，单击**提交**。
3. 应用部署成功后，部署组中**运行实例数**的数值发生变化。
	 ![](https://qcloudimg.tencent-cloud.cn/raw/8274f8534512232fc47c3a5093d3ffb8.png)

## 相关文档

您可参考以下文档，使用 TSF Serverles 相关功能：

- [TSF Serverless 使用须知](https://cloud.tencent.com/document/product/649/38960)
- [Spring Cloud 概述](https://cloud.tencent.com/document/product/649/36285)
- [Spring Cloud 快速入门](https://cloud.tencent.com/document/product/649/20261)
