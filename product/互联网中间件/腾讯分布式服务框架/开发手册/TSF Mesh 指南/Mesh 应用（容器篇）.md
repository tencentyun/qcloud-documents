## 准备工作

前提条件：

1. 下载 TSF 提供的 Demo。该步骤预计耗时 1 min。
2. 在 TSF 控制台上已创建容器集群并添加节点，参考 [集群](https://cloud.tencent.com/document/product/649/13684)。对于未创建容器集群和添加节点的用户，该步骤预计耗时 10 min。
3. 用户的开发机上已安装 `docker` 环境（用于推送镜像到镜像仓库）。对于本地无 docker 环境的用户，该步骤预计耗时 20 min。



**Demo for Python**

- [Demo for Python](https://main.qcloudimg.com/raw/beac5a25054beae556e93bafa64bdd9d/tsf_mesh_demo_python.tar.gz)：提供了 3 个 Python 应用及 Dockerfile。三个应用对应的服务名分别是：
  - user
  - shop
  - promotion

三个应用之间的调用关系是：

```
user => shop => promotion
```



**控制台操作步骤**

快速体验 TSF Mesh 应用（通过容器部署），涉及到 3 个步骤：

1. 创建并部署 Mesh 应用
2. 创建服务并与 Mesh 应用关联
3. 验证服务调用



## 一、创建并部署 Mesh 应用

### 1. 创建应用
1.1 登录 TSF 控制台。
1.2 单击左侧导航【应用管理】。
1.3 新建应用：
   - 应用名：填写应用名称

   - 部署方式：选择 **容器部署**  

   - 应用类型：选择 **Mesh 应用**

     ![](https://main.qcloudimg.com/raw/dc0c301e3b3829f486cff4ce580ab6f0.png)
1.4 单击【提交】按钮。



### 2. 将镜像推送到仓库

2.1 单击【镜像】标签页。如果是首次使用，需要设置镜像仓库密码（该密码与腾讯云官网账号密码独立）。
2.2 单击【使用指引】，根据指引中的命令将 Python demo 应用的镜像推送到镜像仓库中。关于如何将镜像推送到仓库的操作方法参考 [镜像仓库使用指引](https://cloud.tencent.com/document/product/649/16695)。
  ![](https://main.qcloudimg.com/raw/c5fd709b9d3acbc6fc25f1c8bd8ebd5d.png)



### 3. 创建部署组

在 TSF 平台上，使用部署组来部署应用，用户首先需要创建部署组，然后执行部署应用操作。

3.1 在应用详情页内，单击【部署组】标签页。
3.2 新建部署组：
   - 部署组名：填写部署组名称。
   - 集群：选择应用将部署的集群
   - 命名空间：选择命名空间属性
   - 其他设置：参考下图
     ![](https://main.qcloudimg.com/raw/3a79f0f83dc6e538e6ab5534a8e1302d.png)

3.3 单击【提交】按钮。



### 4. 部署应用

4.1 部署组左侧的【部署应用】。
4.2 部署相关信息，使用 **步骤二** 中仓库中的镜像。各字段含义可参考 [容器应用部署组-部署应用](https://cloud.tencent.com/document/product/649/15525#.E9.83.A8.E7.BD.B2.E5.BA.94.E7.94.A8)。

![](https://main.qcloudimg.com/raw/230b0a45fdb27f15bfe0b4fcfefafc4b/image.png)

4.3 单击【提交】按钮，，如果部署组状态变为运行中，表示应用部署成功。



## 二、创建服务并关联应用


1. 在 TSF 控制台上，单击左侧导航栏 【服务治理】。
2. 在页面顶部选择集群和命名空间。确保选中的集群和命名空间和 **步骤三** 中部署组的集群和命名空间属性相同。
3. 新建服务：
   - 服务名：填写服务名称 user。
   - 关联应用：选择 Mesh 应用，在应用列表中选择在 **步骤一** 中创建的应用。
   - 服务监听端口：协议选择 HTTP，端口可填写 9080。
   - 健康检查 URL：填写应用的健康检查 URL，用于检查应用是否正常运行。

     ![](https://main.qcloudimg.com/raw/b08bb4be98bd700806aa37180b8f670b.png)
4. 单击【提交】按钮。


## 三、验证服务调用

使用同样的步骤一和步骤二部署 `user`、`shop` 和 `promotion` 三个应用，并创建服务与应用关联。注意在创建3个服务时的端口号：

- `user` 端口号：9080

- `shop` 端口号：9080

- `promotion` 端口号：9080



用户可以登录容器集群 VPC 下任一机器，然后通过 `curl` 命令验证 `user` 服务是否健康，以及触发 `user` 服务调用 `shop` 和 `promotion` 服务。



#### 1. 触发 user 服务调用 shop 和 promotion 服务 

user, shop, promotion 三个服务的接口间调用关系如下：

user (`/api/v6/user/account/query` )  => shop (`/api/v6/shop/order`) => promotion (`/api/v6/promotion/query`)

为了验证 `user` 服务能通过服务名来调用 `shop` 服务，需要用户通过以下几种方式来触发 `user` 服务的接口调用：



- **负载均衡 IP + 服务端口**：如果部署组在部署时，选择了公网访问方式，可以通过 **负载均衡 IP + 服务端口** （在上面的截图例子中服务端口是  9080）来访问 `user` 服务的 `/api/v6/user/account/query` 接口。

- **节点IP + NodePort**： 如果部署组在部署时，选择了 NodePort 访问方式，可以通过 **节点IP + NodePort** 来访问 `user` 服务的 `/api/v6/user/account/query` 接口。其中 `节点IP` 为集群中任一节点的内网IP，`NodePort` 可以在部署组的基本信息页面查看。用户首先登录到集群所在 VPC 的机器，然后执行如下命令：

 ```
	shell
	curl -XGET <节点IP>:<NodePort>/api/v6/user/account/query
 ```

- **API 网关**：用户可以通过在 API 网关配置微服务 API 来调用 `user` 服务的接口。关于如何配置微服务 API 网关，可参考文档 [API 网关作为请求入口](https://cloud.tencent.com/document/product/649/17644)。



#### 2. 在控制台验证服务间是否调用

完成 **1** 和 **2** 之后，可以通过几种方式验证服务是否成功被 sidecar 代理注册到注册中心，同时服务之间是否成功地进行了调用。

- **服务治理** 界面：选择集群和命名空间后，如果服务列表中的服务状态为 **在线** 或 **单点在线**，表示服务被代理注册成功。如果服务提供者的请求量大于 0，表示服务提供者被服务消费者请求成功。
  ![](https://main.qcloudimg.com/raw/89040e8ddf377a1a9a972cac02b65037.png)

- **依赖拓扑** 界面：选择集群和命名空间后，调整时间范围覆盖服务运行期间的时间范围，正常情况下，将出现服务之间相互依赖的界面。
  ![](https://main.qcloudimg.com/raw/95c0a6e134664254b23e2c70e5f25671.png)
