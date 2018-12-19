## 准备工作
1. 下载 TSF 提供的 Demo。该步骤预计耗时 1 min。
2. 在 TSF 控制台上已创建容器集群并添加节点，参考 [集群](https://cloud.tencent.com/document/product/649/13684)。对于未创建容器集群和添加节点的用户，该步骤预计耗时 10 min。
3. 用户的开发机上已安装 `docker` 环境（用于推送镜像到镜像仓库）。对于本地无 docker 环境的用户，该步骤预计耗时 20 min。

## 一、创建并部署 Mesh 应用
### 1. 创建应用
1.1 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf)。
1.2 单击左侧导航【[应用管理](https://console.cloud.tencent.com/tsf/app)】。
1.3 单击【新建应用】，并填写以下信息：
   - 应用名：填写应用名称
   - 部署方式：选择 **容器部署**  
   - 应用类型：选择 **Mesh 应用**

1.4 单击【提交】按钮，完成应用创建。


### 2. 将镜像推送到仓库

2.1  单击【[镜像仓库](https://console.cloud.tencent.com/tsf/image)】标签页。首次使用时，需要设置镜像仓库密码（该密码与腾讯云官网账号密码独立）。
2.2 单击【[应用管理](https://console.cloud.tencent.com/tsf/app)】>【ID/应用名】>【使用指引】，根据指引中的命令将 Python demo 应用的镜像推送到镜像仓库中（详请参见 [镜像仓库使用指引](https://cloud.tencent.com/document/product/649/16695)）。
   ![](https://main.qcloudimg.com/raw/bbf54724e4294e6c16c0d892499db3e0/WX20181119-174858@2x.png)


### 3. 创建部署组
在 TSF 平台上，使用部署组来部署应用，用户需要先创建部署组，然后执行部署应用操作。
3.1 在应用详情页内，单击【部署组】标签页。
3.2 新建部署组： 
   - 部署组名：填写部署组名称。
   - 集群：选择应用将部署的集群
   - 命名空间：选择命名空间属性
   - 实例资源限制：参考下图
	 ![](https://main.qcloudimg.com/raw/3d833120463680f3f5cbe9a187130c55.png)
3.3 访问设置、更新方式、日志配置项。
 ![](https://main.qcloudimg.com/raw/989f250a54c31559929ccee79d1f8740.png)
3.4 单击【提交】按钮。



### 4. 部署应用
4.1 单击部署组左侧的【部署应用】。
4.2 部署相关信息，使用 [步骤 2](https://cloud.tencent.com/document/product/649/17930#2.-.E5.B0.86.E9.95.9C.E5.83.8F.E6.8E.A8.E9.80.81.E5.88.B0.E4.BB.93.E5.BA.93) 中仓库中的镜像。各字段含义可参考 [容器应用部署组-部署应用](https://cloud.tencent.com/document/product/649/15525#.E9.83.A8.E7.BD.B2.E5.BA.94.E7.94.A8)。
  ![](https://main.qcloudimg.com/raw/1d32f732730f081aa9b9740bc4ec64a2.png)
4.3  单击【提交】按钮，如果部署组状态变为运行中，表示应用部署成功。


## 二、查看服务是否注册成功

1. 单击左侧导航栏【[服务治理](https://console.cloud.tencent.com/tsf/service)】，查看服务是否注册成功。如果注册成功，服务显示在线状态。
   ![](https://main.qcloudimg.com/raw/c9c264621141bdd7e1005ab8e6c2fe50/WX20181119-183239@2x.png)
2. 单击服务 ID，进入服务详情页。单击【API 列表】标签页，可以查看上报的 API 定义。
   ![](https://main.qcloudimg.com/raw/fcc4e95eb51c75d0e3442e5b940a1dbc/WX20181119-180443@2x.png)


## 三、验证服务调用

### 1. 触发 user 服务调用 shop 和 promotion 服务 
user、shop、promotion 三个服务的接口间调用关系如下：

user (`/api/v6/user/account/query` )  => shop (`/api/v6/shop/order`) => promotion (`/api/v6/promotion/query`)

为了验证 user 服务能通过服务名来调用 shop 服务，需要用户通过以下三种方式来触发 user 服务的接口调用：


- **负载均衡 IP + 服务端口**：如果部署组在部署时，选择了公网访问方式，可以通过 **负载均衡 IP + 服务端口** 来访问 `user` 服务的 `/api/v6/user/account/query` 接口。

- **节点IP + NodePort**： 如果部署组在部署时，选择了 NodePort 访问方式，可以通过 **节点IP + NodePort** 来访问 `user` 服务的 `/api/v6/user/account/query` 接口。其中 `节点IP` 为集群中任一节点的内网IP，`NodePort` 可以在部署组的基本信息页面查看。用户首先登录到集群所在 VPC 的机器，然后执行如下命令：

```
	shell
	curl -XGET <节点IP>:<NodePort>/api/v6/user/account/query
```

- **API 网关**：用户可以通过在 API 网关配置微服务 API 来调用 user 服务的接口。关于如何配置微服务 API 网关，可参考文档 [API 网关作为请求入口](https://cloud.tencent.com/document/product/649/17644)。

### 2. 在控制台验证服务间是否调用
可以通过以下两种方式验证服务是否成功被 Sidecar 代理注册到注册中心，同时验证服务之间是否成功地进行了调用。

- **服务治理** 界面：选择集群和命名空间后，如果服务列表中的服务状态为 **在线** 或 **单点在线**，表示服务被代理注册成功。如果服务提供者的请求量大于 0，表示服务提供者被服务消费者请求成功。
  ![](https://main.qcloudimg.com/raw/c9c264621141bdd7e1005ab8e6c2fe50/WX20181119-183239@2x.png)

- **依赖拓扑** 界面：选择集群和命名空间后，调整时间范围覆盖服务运行期间的时间范围，正常情况下，将出现服务之间相互依赖的界面。
  ![](https://main.qcloudimg.com/raw/e8bdc3acfcb2f5a2c55bdc344f060163/WX20181119-181613@2x.png)
