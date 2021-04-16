## 准备工作

1. 本地安装 java 和 maven 环境。
2. 下载 TSF 提供的 Demo (参考 [TSF 原生应用 Demo 介绍](https://cloud.tencent.com/document/product/649/54148))。
3. 解压 Demo 压缩包，按 README.md 提示执行命令 `make build`。
4. 在 TSF 控制台上已创虚拟机集群并添加节点，参考 [集群](https://cloud.tencent.com/document/product/649/13684)。

## 操作步骤

### 步骤1：创建并部署原生应用

#### 1. 创建应用

1. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf)。
2. 在左侧导航栏单击【应用管理】，进入应用管理列表页。
3. 单击【新建应用】，并填写以下信息：
   - 应用名：填写应用名称
   - 部署方式：选择**虚拟机部署**
   - 应用类型：选择 **原生应用**
   - 标签（可选）：可选择已有标签或者点击标签管理去新建标签。
4. 单击【提交】，完成应用创建，在弹出的窗口中选择【确认】，前往上传程序包并部署应用。

#### 2. 上传程序包

1. 上传程序包页面，单击【上传程序包】，选择程序包（如`consul-provider/target/consul-provider-*.jar`），填写程序包相关信息。
2. 单击【提交】，完成上传。

#### 3. 创建部署组

详细操作请参考 [虚拟机应用部署组](https://cloud.tencent.com/document/product/649/15524) 中关于**创建部署组**的内容。

#### 4. 部署应用

详细操作请参考 [虚拟机应用部署组](https://cloud.tencent.com/document/product/649/15524) 中关于**部署应用**的内容。部署应用后部署组状态变为运行中。

![](https://main.qcloudimg.com/raw/9f6267360bdc9216d45f2be2ed03c445.png)

### 步骤2：查看服务是否注册成功

1. 在左侧导航栏单击 【[服务治理](https://console.cloud.tencent.com/tsf/service)】，进入服务列表页，查看服务是否注册成功。如果成功，服务显示在线状态。

   ![](https://main.qcloudimg.com/raw/39452614a27038d9d055ed7389ed91ce.png)

2. 在服务列表页单击服务 ID，进入服务详情页，查看具体信息。

### 步骤3：验证服务调用

使用与之前相同的流程部署一组 consumer 和 provider（如 consul-consumer 和 consul-provider）。

![](https://main.qcloudimg.com/raw/bfe411679daabf171d94a0e4553b010f.png)


#### 1. 登录服务器验证服务间调用

为了验证 consumer 服务能通过服务名来调用 provider 服务，需要用户通过以下方式来请求 provider 服务的调用（以 consul 为例）：

- 登录 consul-consumer 所在云服务器，执行如下 `curl` 命令调用 provider 服务接口。
```
curl localhost:8001/ping-provider
```

- 登录 consul-consumer 所在云服务器，执行如下 `curl` 命令调用 provider 服务接口。
```
curl consul-provider:8002/ping
```

- **API 网关**：用户可以通过在 API 网关配置微服务 API 来调用 consumer 服务的接口。关于如何配置微服务 API 网关，请参考文档 [API 网关作为请求入口](https://cloud.tencent.com/document/product/649/17644)。

#### 2. 在控制台验证服务之间是否调用

可以验证服务是否成功被注册，同时验证服务之间是否成功地进行了调用。

在**服务治理**界面：选择集群和命名空间后，如果服务列表中的服务状态为**在线**或**单点在线**，表示服务被代理注册成功。如果服务提供者的请求量大于0，表示 provider 被 consumer 请求成功。

![](https://main.qcloudimg.com/raw/913e1b92a99b80f51735e93e2dcfc9c3.png)

在**依赖拓扑**界面：调整时间范围，使其覆盖服务运行期间的时间范围，正常情况下，将出现服务之间相互依赖的界面。

![](https://main.qcloudimg.com/raw/26aab83740bd04a28f20ae347214a943.png)
