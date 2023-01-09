## 操作场景

Dubbo 应用使用 TSF Atom-SDK 框架接入，支持 TSF 全栈服务治理、应用配置管理能力。如果您想了解如何实现微服务应用的相关功能，请参见 [Dubbo 应用开发](#building)。

为了帮助您快速体验如何在 TSF 中部署微服务应用，TSF 提供了一对应用 Demo，包含一个 provider 应用和一个 consumer 应用。本文以一个示例介绍如何在虚拟机环境中部署 Dubbo 应用。



## 前提条件

已参见 [快速创建一个虚拟机集群](https://cloud.tencent.com/document/product/649/55498) 创建好一个虚拟机集群并导入两个可用的云主机。


[](id:building)
## 部署应用

1. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf/index)。
2. 在左侧导航栏，单击**应用管理**，选择好地域后，在应用列表上方单击**新建应用**。
3. 设置应用信息，单击**提交**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/4954798135f1d2576d1ef6945428a991.png)
   - **应用名**：填写 provider。
   - **部署方式**：选择 **虚拟机部署**。
   - **业务类型**：选择 **业务应用**。
   - **开发语言**：选择 **JAVA**。
   - **开发框架**：选择 **Dubbo**。
   - **应用类型**：选择 **普通应用**。
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
   ![](https://qcloudimg.tencent-cloud.cn/raw/cde49251f43165ac7e4a218648ceffde.png)
   - 软件仓库：选择**官网Demo（公共仓库）**。
   - 程序包类型：选择 **jar**。
   - JDK 版本：选择**KONA JDK8**。
   - 程序包类型：选择程序包名称为`atom-example-apache-dubbo-provider-1.0.1-RELEASE.jar`的程序包。
   - 启动参数：选填。
   - 更新方式：选择立即更新。
   - 健康检查：可选。详情参见 [健康检查](https://cloud.tencent.com/document/product/649/15525)。
   - 描述：可选。
8. 单击**完成**，应用部署成功后，部署组中**已启动/总机器数**的数值发生变化。
![](https://qcloudimg.tencent-cloud.cn/raw/bda38a3164d322af7661bb55058c6149.png)
9. 在服务治理页面，选择地域和应用关联的命名空间后，可以看到服务实例显示在线状态，表示服务注册成功。
   ![](https://qcloudimg.tencent-cloud.cn/raw/95093bb2cb33cd68a524930fc794bd42.png)





