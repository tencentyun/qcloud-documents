## 操作场景

Mesh 应用支持 Go/Python/C++ 等不同编程语言，通过 Service Mesh 技术接入 TSF，无需修改代码，支持全套 TSF 服务治理能力。如果您想了解如何实现微服务应用的相关功能，请参见 [Mesh 应用开发](#building)。

为了帮助您快速体验如何在 TSF 中部署微服务应用，TSF 提供了一组 Mesh 应用 Demo，包含 user、shop 和 promotion 三个应用。本文以一个示例介绍如何在虚拟机环境中部署 Service Mesh 应用，并实现简单的服务调用。



## 前提条件

已参见 [快速创建一个虚拟机集群](https://cloud.tencent.com/document/product/649/55498) 创建好一个虚拟机集群并导入可用的云主机。


[](id:building)
## 部署应用

1. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf/index)。
2. 在左侧导航栏，单击**应用管理**，选择好地域后，在应用列表上方单击**新建应用**。
3. 设置应用信息，单击**提交**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/b889004d802e004231c5394ffbd4eb06.png)
   - **应用名**：填写 **user**。
   - **部署方式**：选择 **虚拟机部署**。
   - **业务类型**：选择 **业务应用**。
   - **开发语言**：选择 **其他语言**。
   - **开发框架**：选择 **其他框架**。
   - **应用类型**：选择 **Mesh 应用**。
   - **服务配置：**选择使用**使用本地Spec.yaml**。
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
   ![](https://qcloudimg.tencent-cloud.cn/raw/d47807985e4190de4172524ed9953113.png)
   - 软件仓库：选择**官网Demo（公共仓库）**。
   - 程序包类型：选择 **zip/tar.gz**。
   - JDK 版本：选择**KONA JDK8**。
   - 程序包类型：选择程序包名称为`userService.tar.gz`的程序包。
   - 启动参数：选填。
   - 更新方式：选择立即更新。
   - 健康检查：可选。详情参见 [健康检查](https://cloud.tencent.com/document/product/649/15525)。
   - 描述：可选。
8. 单击**完成**，应用部署成功后，部署组中**已启动/总机器数**的数值发生变化。
![](https://qcloudimg.tencent-cloud.cn/raw/4159482c90ce7f47c6419369d0c44cea.png)
9. 在 [服务治理](https://console.cloud.tencent.com/tsf/service) 页面，选择地域和应用关联的命名空间后，可以看到服务实例显示**单点在线**状态，表示服务注册成功。
![](https://qcloudimg.tencent-cloud.cn/raw/62d31369da188cc58c7988481fc69cc9.png)
10. 在服务列表页单击服务的“ID”，进入服务详情页，单击**接口列表**标签页，可以查看上报的 API 定义。

## 验证服务调用

使用同样的步骤在同一个集群和命名空间中部署 user、shop 和 promotion 三个应用。user、shop、promotion 三个服务的接口间调用关系如下：
![img](https://main.qcloudimg.com/raw/4b4cfb3f587dcca35f975db0c924542a.png)

对应的服务名和应用监听端口为：user （8089），shop （8090）和 promotion （8091）。

用户可以登录虚拟机集群 VPC 下的任一机器，然后通过`curl`命令验证 user 服务是否健康，以及触发 user 服务调用 shop 和 promotion 服务。



### 方式1：使用公网访问验证服务调用

1. 在集群云主机列表页面，获取 user 服务所在云服务器的公网IP。
![](https://qcloudimg.tencent-cloud.cn/raw/56870be67dea0cfb1bb60ad2af760a10.png)
2. 使用浏览器访问 consumer 应用的 URL 并触发 user 服务调用 shop 和 promotion 服务。格式为`http://<云服务器实例公网IP>:8089/api/v6/user/account/query`，返回结果如下：
   ![](https://qcloudimg.tencent-cloud.cn/raw/8fbb1b5a6ad3a21c4df555e48959c54a.png)





### 方式2：登录云服务器验证服务间调用

1. 在集群云主机列表页面，单击 user 服务所在云服务器操作栏的**登录**，输入登录密码，登录云服务器。
![](https://qcloudimg.tencent-cloud.cn/raw/618c8c4fb0c4c2f69d5a8f30ccad9238.png)
2. 执行 curl 命令调用 user 服务接口。
   ```
   curl localhost:<user端口>/api/v6/user/account/query
   ```
   调用结果如下：
   ![](https://qcloudimg.tencent-cloud.cn/raw/44a70545c9428768b97eab2d40164ceb.png)
   或者执行 curl 命令调用 shop 服务接口（注意使用服务名来调用）。
   ``` 
   curl shop:<shop端口>/api/v6/shop/order
   ```
   调用结果如下
   ![](https://qcloudimg.tencent-cloud.cn/raw/ff882a1122232aa00733ecacb0ceae14.png)

   


### 在 TSF 控制台查看服务依赖拓扑图

1. 在 [服务治理](https://console.cloud.tencent.com/tsf/service) 页面，选择创建集群和命名空间后，可以看到 user、shop 和 promotion 服务的运行状况。服务状态为**单点在线**，表示服务被代理注册成功。服务提供者的请求量大于0，请求成功率为100%，表示服务提供者被服务消费者请求成功。
![](https://qcloudimg.tencent-cloud.cn/raw/0dda165bf035aa146b5679f5bdbbd506.png)
2. 在服务治理页面，单击 shop 服务的“ID”，进入服务详情页面，可以看到三个服务的依赖关系。
   ![](https://qcloudimg.tencent-cloud.cn/raw/d1c6821c4658746c527ea469d01f1c8a.png)

   




