## 准备工作

1. 下载 TSF 提供的 Demo (参考 [TSF 原生应用 Demo 介绍](https://cloud.tencent.com/document/product/649/54148))。
2. 解压 Demo 压缩包，按 README 提示执行命令 `make docker-build`。
3. 在 TSF 控制台上已创建容器集群并添加节点，详情参考 [集群](https://cloud.tencent.com/document/product/649/13684)。

## 操作步骤

### 步骤1：创建并部署原生应用

#### 1. 创建应用

1. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf)。
2. 在左侧导航，单击【应用管理】，进入应用列表页。
3. 在应用列表页，单击【新建应用】，并填写以下信息：
   - 应用名：填写应用名称
   - 部署方式：选择**容器部署**
   - 应用类型：选择 **原生应用**
   - 标签（可选）：可选择已有标签或者点击标签管理去新建标签。
4. 单击【提交】，完成应用创建。

#### 2. 将镜像推送到仓库

1. 在左侧导航拦，单击【镜像仓库】，进入镜像列表页。首次使用时，您需要设置镜像仓库密码（该密码与腾讯云官网账号密码独立）。
2. 在镜像列表页，单击【应用管理】>【ID/应用名】>【镜像】，单击【使用指引】，根据指引中的命令将 Demo 应用的镜像（参考 [准备工作](#zb) 中的第2步）推送到镜像仓库中（详请参见 [镜像仓库使用指引](https://cloud.tencent.com/document/product/649/16695)）。

#### 3. 创建部署组

详细操作请参考 [容器应用部署组](https://cloud.tencent.com/document/product/649/15525) 中关于**创建部署组**的内容。

#### 4. 部署应用

详细操作请参考 [容器应用部署组](https://cloud.tencent.com/document/product/649/15525) 中关于**部署应用**的内容。部署应用后部署组状态变为运行中。

![](https://main.qcloudimg.com/raw/9f6267360bdc9216d45f2be2ed03c445.png)

### 步骤2：查看服务是否注册成功

1. 在左侧导航栏，单击【[服务治理](https://console.cloud.tencent.com/tsf/service)】进入服务列表页，选择正确的地域和命名口行家，查看服务是否注册成功。如果注册成功，服务显示在线状态。
   ![](https://main.qcloudimg.com/raw/39452614a27038d9d055ed7389ed91ce.png)
2. 在服务列表页，单击服务 ID，进入服务详情页，查看具体信息。

### 步骤3：验证服务调用

使用与之前相同的流程部署一组 consumer 和 provider（如 consul-consumer 和 consul-provider）。

![](https://main.qcloudimg.com/raw/bfe411679daabf171d94a0e4553b010f.png)

#### 1. 请求 consumer 来调用 provider

有3种方式可以从公网请求 consumer：

- **云主机 IP + NodePort**： 如果部署组在部署时，选择了 NodePort 访问方式，可以通过**云主机 IP + NodePort**来访问`consumer`服务的`/ping-provider`接口。其中`云主机 IP`为集群中任一云主机的 IP，`NodePort`可以在部署组的基本信息页面被查看。
```
curl <云主机 IP>:<NodePort>/ping-provider
```

- **负载均衡 IP + 服务端口**：如果部署组在部署时，选择了公网访问方式，可以通过**负载均衡 IP + 服务端口**来访问`consumer`服务的`/ping-provider`接口。

- **API 网关**：用户可以通过在 API 网关配置微服务 API 来调用 user 服务的接口。关于如何配置微服务 API 网关，可参考文档 [API 网关作为请求入口](https://cloud.tencent.com/document/product/649/17644)。


也可以在容器内通过服务名和服务端口请求 consumer。先通过 kubectl 等方式进入 容器，然后调用：

```
wget -O- consul-consumer:8001/ping-provider
wget -O- eureka-consumer:8003/ping-provider
```

#### 2. 在控制台验证服务之间是否调用

可以验证服务是否成功被注册，同时验证服务之间是否成功地进行了调用。

在**服务治理**界面：选择集群和命名空间后，如果服务列表中的服务状态为**在线**或**单点在线**，表示服务被代理注册成功。如果服务提供者的请求量大于0，表示 provider 被 consumer 请求成功。

![](https://main.qcloudimg.com/raw/913e1b92a99b80f51735e93e2dcfc9c3.png)

在**依赖拓扑**界面：调整时间范围，使其覆盖服务运行期间的时间范围，正常情况下，将出现服务之间相互依赖的界面。

![](https://main.qcloudimg.com/raw/26aab83740bd04a28f20ae347214a943.png)
