## 操作场景

容器服务 TKE 支持安装 Nginx-ingress 扩展组件，可通过 Nginx-ingress 接入 Ingress 流量。关于 Nginx-ingress 组件的更多介绍，请参见 [Nginx-ingress 说明](https://cloud.tencent.com/document/product/457/51260)。本文将为您介绍 Nginx-ingress 组件常见最佳实践操作指引。


## 前提条件

已安装 [Nginx-ingress](https://cloud.tencent.com/document/product/457/50503) 扩展组件。


## 操作步骤

### 为集群暴露多个 Nginx Ingress 流量入口

Nginx-ingress 扩展组件安装后，在 `kube-system` 下会有 Nginx-ingress 的 operator 组件，通过该组件可以创建多个 Nginx Ingress 实例，每个 Nginx Ingress 实例都使用不同的 IngressClass，且使用不同的 CLB 作为流量入口，从而实现不同的 Ingress 绑定到不同流量入口。可以根据实际需求，为集群创建多个 Nginx Ingress 实例。


1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的**集群**。
2. 在集群管理页面单击目标集群 ID，进入集群详情页面。
3. 选择左侧菜单栏中的**组件管理**，进入组件列表页面。
4. 单击已安装好的 Nginx-ingress 扩展组件，进入组件页面。
5. 单击**新增Nginx Ingress实例**，根据需求配置 Nginx Ingress 实例，为每个实例指定不同的 IngressClass 名称。
>?创建 Nginx Ingress 实例详细步骤，请参见 [安装 Nginx-ingress 实例](https://cloud.tencent.com/document/product/457/50503)。
6. 创建 Ingress 时可指定具体的 IngressClass 将 Ingress 绑定到具体的 Nginx Ingress 实例上。您可通过控制台或 YAML 创建 Ingress：
<dx-tabs>
::: 通过控制台创建\sIngress
参考控制台 [创建 Ingress](https://cloud.tencent.com/document/product/457/31711#.E5.88.9B.E5.BB.BA-ingress) 步骤创建 Ingress。其中：
- **Ingress类型**：选择**Nginx均衡负载器**。
- **Class**：选择上述步骤创建的 Nginx Ingress 实例。
![](https://main.qcloudimg.com/raw/4e502599789facceddf448642d19d525.jpg)
:::
::: 通过\sYAML\s创建\sIngress
参考 YAML [创建 Ingress](https://cloud.tencent.com/document/product/457/31711#.E5.88.9B.E5.BB.BA-ingress2) 步骤创建 Ingress，并指定 ingressClass 的 annotation（`kubernetes.io/ingress.class`）。如下图所示：
![](https://main.qcloudimg.com/raw/e4ee61dd452ccc512ba8fc5b85ab5714.png)
:::
</dx-tabs>





### 性能优化

#### LB 直通 Pod

集群网络模式为 Global Router 时，默认未开启 LB 直通 Pod，建议您按照以下步骤开启 LB 直通 Pod：

1. 为集群启用 [VPC-CNI](https://cloud.tencent.com/document/product/457/50355)。
2. 创建 Nginx Ingress 实例时，勾选**使用CLB直连Pod模式**，可以使流量绕过 NodePort 直达 Pod，以此来提升性能。如下图所示：
![](https://main.qcloudimg.com/raw/b920ef483e80e83d2080910471f7de4c.png)
>? 创建 Nginx Ingress 实例详细步骤，请参见 [安装 Nginx-ingress 实例](https://cloud.tencent.com/document/product/457/50503)。





#### 提升 LB 带宽上限

LB 作为流量入口，如需较高的并发或吞吐，在创建 Nginx Ingress 实例时，可根据实际需求规划带宽上限，为 Nginx Ingress 分配更高的带宽。如下图所示：
![](https://main.qcloudimg.com/raw/0a59544d930800c1bebf734da4d1ba6b.png)

若账号为非带宽上移类型（可参见 [区分账户类型](https://cloud.tencent.com/document/product/684/39903) 文档进行区分），带宽上限取决于节点带宽，可根据以下情况调整节点的带宽上限：

- 若启用 LB 直通 Pod，LB 总带宽为 Nginx Ingress 实例 Pod 所在节点的带宽之和，建议专门规划一些高外网带宽节点部署 Nginx Ingress 实例（指定节点池 DaemonSet 部署）。
- 若未使用 LB 直通 Pod，LB 总带宽为所有节点的外网带宽之和。



#### 优化 Nginx Ingress 参数

Nginx Ingress 实例已默认为内核参数与 Nginx Ingress 自身的配置进行优化，详情请参见 [Nginx Ingress 高并发实践](https://cloud.tencent.com/document/product/457/48142)。如需自定义，可参考下文介绍自行修改：

<dx-tabs>
::: 修改内核参数
编辑部署好的 nginx-ingress-conntroller 的 Daemonset 或 Deployment（取决于实例部署选项），修改 initContainers（使用 Kubectl 进行修改，控制台禁止修改 kube-system 下的资源）。如下图所示：
![](https://main.qcloudimg.com/raw/821faeb4970ddebe190577d1ca213b84.png)
:::
::: 修改\sNginx\sIngress\s自身配置
在**Nginx配置**中选中对应的实例，单击**编辑YAML**可修改 Nginx Ingress 实例的 ConfigMap 配置。如下图所示：
![](https://main.qcloudimg.com/raw/a6cd6034f4d29ef24b3410bd0dd4f698.jpg)
>? ConfigMap 配置详细介绍请参见 [官方文档](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/)。
:::
</dx-tabs>






### 提升 Nginx Ingress 可观测性

#### 开启监控与日志

创建 Nginx Ingress 实例后，在**日志/监控**里可以为实例开启日志与监控，方便查看实例各项状态指标与问题排查。如下图所示：
![](https://main.qcloudimg.com/raw/03dfb8e728cf3cfe042780147762a63e.jpg)
- 监控依赖 [云原生监控](https://cloud.tencent.com/document/product/457/49889)，如何开启请参见 [Nginx-ingress 监控配置](https://cloud.tencent.com/document/product/457/50506)。
- 日志依赖 [日志服务](https://cloud.tencent.com/document/product/614)，如何开启请参见 [Nginx-ingress 日志配置](https://cloud.tencent.com/document/product/457/50505)。

>?强烈建议为 Nginx Ingress 实例都开启监控和日志。

#### 查看监控大盘

1. 开启监控后，单击实例的**前往Prometheus查看监控**跳转到云原生监控。如下图所示：
![](https://main.qcloudimg.com/raw/381854d2de233984d36510c3b55773d0.png)
2. 进入 Grafana 面板，切换到**NGINX Ingress controller**数据大盘，即可查看监控视图。如下图所示：
![](https://main.qcloudimg.com/raw/82ae23289f21bdd5d0bc9cdf3a8b8ed7.png)

#### 日志检索与日志仪表盘

开启日志配置后，在 Nginx Ingress 列表页可单击实例右侧**操作**项下的**更多**，在弹出的菜单中选择对应功能进行日志检索或查看日志仪表盘。如下图所示：
![](https://main.qcloudimg.com/raw/afaf75d46cdb5eed936a039c7888cb61.jpg)
- 单击**前往CLS查看访问日志**跳转到日志服务，在**检索分析**中选中实例对应的日志集与主题，即可查看 Nginx Ingress 的访问与错误日志。
- 单击**查看访问日志仪表盘**可以直接跳转到根据 Nginx Ingress 日志数据来展示统计信息的仪表盘。

