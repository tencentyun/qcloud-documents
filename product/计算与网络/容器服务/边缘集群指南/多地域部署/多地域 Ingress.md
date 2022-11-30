



## 场景介绍
在边缘节点区分多个地域的情况下，每个地域都有独立的网络架构，需要在本地域对外提供 Ingress 服务能力，腾讯云边缘容器服务基于 `NodeUnit`的相关概念，在产品上支持在不同地域创建`Nginx-Ingress-Controller`的能力，同时通过`application-grid-wrapper`组件，可以将 Ingress-Controller 对 pod 的访问限制在本地域(NodeUnit 范围)之内，具体架构如下图：

![](https://qcloudimg.tencent-cloud.cn/raw/20e966b99f2a4e29e12060bf96a9a938.jpg)

## 操作步骤
### Nginx-Ingress-Controller 组件安装
1. 登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 单击目标边缘集群 ID，进入集群详情页。
3. 选择页面左侧**组件管理**，进入组件列表页面，点击**新建**，添加 Ingress-Controller 边缘组件，单击**完成**。如下图所示：
<div align="left"><img src="https://qcloudimg.tencent-cloud.cn/raw/0d12e39e5f5dbf6fd0bf43c83bd21da5.jpg" width=100% title="service-group"></div>
4. 等待边缘组件安装完成。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/5c3f00e83ac32292593d878707908391.png)
5. 单击已经部署的组件名称，进入组件详情页面。如下图所示：
<div align="left"><img src="https://qcloudimg.tencent-cloud.cn/raw/ca0bc6fc0e2d2db6946b632ec7c0c830.jpg" width=100% title="service-group"></div>
6. 单击**新增Nginx Ingress 实例**，在指定的地域（NodeUnit）创建 Nginx-Ingress-Controller 实例。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/1571ea7e36748f77bbf875535febae38.jpg)
 - **NginxIngress 名称**：指定相应部署的 Ingress-Ingress-Controller 实例的名称，会创建相应的 daemonset。
 - **命名空间**：现在默认监听所有命名空间下的 Ingress 资源。
 - **部署选项**：现在默认使用 DaemonSet 模式部署，需要用户自行选择 NodeUnit 下的一个或者多个节点提供 Ingress Controller 服务。
 - **节点池**：选择您需要部署的节点池（NodeUnit）进行部署，然后选择需要的节点来部署 Nginx-Ingress-Controller 服务。
>!  选择的节点需要保证 80/443端口未被占用，否则会导致 Nginx-Ingress-Controller 启动失败。
>
 - **Nginx 配置**：配置 Nginx-Ingress-Controller 的资源占用，请根据您业务压力需求合理配置。
7. 单击**完成**后，即可查看创建的 Ingress-Controller 实例。如下图所示：
<div align="left"><img src="https://qcloudimg.tencent-cloud.cn/raw/b094e0d35958dc1fe158e353d1d76885.jpg" width=100% title="service-group"></div>
8. 查看**组件详情**，可以确认当前controller 的部署状态，当运行的 Pod 数达到期望后，就表示已经部署成功。如下图所示：
<div align="left"><img src="https://qcloudimg.tencent-cloud.cn/raw/f6dd8e695d40a0b602b7ea14794f3b7b.jpg" width=100% title="service-group"></div>

### 部署服务并使用 Ingress 访问
1. 这里以 Ningx 服务为例，创建一个 Deployment，这些 Pod 分别会部署到 beijing地域和 guangzhou 地域。如下图所示：
<div align="left"><img src="https://qcloudimg.tencent-cloud.cn/raw/14def85c19f1a2bc5525c36f33c201f3.jpg" width=100% title="service-group"></div>
然后使用同一个 svc 提供内部访问服务
<div align="left"><img src="https://qcloudimg.tencent-cloud.cn/raw/a2db68c400df1aec0f4fc77e2634a42f.jpg" width=75% title="service-group"></div>
这里我们期望从 beijing 地域访问 Ingress 的时候，只会访问到beijing 下的 Pod，即`nginx-deployment-7c97977fd8-2zv87`，而不会访问到 guangzhou 地域的 pod。
2. 创建 Ingress，进入**集群详情页**->**服务**->**Ingress**，单击**新建**。如下图所示：
<div align="left"><img src="https://qcloudimg.tencent-cloud.cn/raw/c305fd9740c9b0442b1413e0da4e6364.jpg" width=100% title="service-group"></div>
3. 输入所需的 Ingress 信息。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/d45346e59055ebe43bdbc33648f47d2d.jpg)
	- **Ingress 名称**：输入需要创建的 Ingress 的名称。
	- **描述**：备注描述信息。
	- **Ingress**类型：当前默认只支持`Nginx Ingress Controller` 类型。
	- **命名空间**：指定命名空间创建此 Ingress。
	- **节点池**：选择此 Ingress 需要绑定的 Ingress-Controller，也就是上面部署的 Nginx-Ingress-Controller 实例。
	- **转发配置**：这里按照服务的具体配置输入。例如这里输入自定义域名`test.k8s.io`，路径为`echo`，后端服务指定为上面创建的svc-`nginx` 。
4. 在相应的地域内访问 ingress 服务。例如在`beijing`地域内，访问`http://test.k8s.io/echo`，如下图所示：
<div align="left"><img src="https://qcloudimg.tencent-cloud.cn/raw/abcaaf48b1b04b9f962f8600e46d5828.jpg" width=40% title="service-group"></div>
 可以进行多次访问测试，会发现所有的访问都会被限制在`beijing`地域的 Pod 中，不会访问到`guangzhou`地域中。
