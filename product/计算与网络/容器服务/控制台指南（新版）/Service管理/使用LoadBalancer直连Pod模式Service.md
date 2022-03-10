## 操作场景

原生 LoadBalancer 模式 Servcie 可自动创建负载均衡 CLB，并通过集群的 Nodeport 转发至集群内，再通过 iptable 或 ipvs 进行二次转发。该模式下的 Service 能满足大部分使用场景，但在以下场景中更推荐使用**直连 Pod 模式 Service**：

- 有获取来源 IP 需求时（非直连模式必须另外开启 Local 转发）。
- 要求具备更高转发性能时（非直连模式下 CLB 和 Service 本身存在两层 CLB，性能有一定损失）。
- 需使用完整的健康检查和会话保持到 Pod 层级时（非直连模式下 CLB 和 Service 本身存在两层 CLB，健康检查及会话保持功能较难配置）。



> ? 当前 GlobalRouter 和 VPC-CNI 容器网络模式均支持直连 Pod 模式，您可以在 [集群列表](https://console.cloud.tencent.com/tke2/cluster?rid=1) 中单击集群 ID 进入集群详情页面，在集群的“基本信息”页面中查看当前集群使用的网络插件。
>


## 容器网络模式为 VPC-CNI

### 使用限制

- 集群 Kubernetes 版本需要高于 1.12。
- 集群网络模式必须开启 VPC-CNI 弹性网卡模式。
- 直连模式 Service 使用的工作负载需使用 VPC-CNI 弹性网卡模式。
- 默认 CLB 的后端数量限制是200个，如果您绑定的工作负载的副本数超过200时，可通过 [在线咨询](https://cloud.tencent.com/online-service?from=doc_457) 提升负载均衡 CLB 的配额。
- 满足 CLB 本身绑定弹性网卡的功能限制，详情请参见 [绑定弹性网卡](https://cloud.tencent.com/document/product/214/36538)。
- 开启直连 Pod 模式的工作负载更新时，将会根据 CLB 的健康检查状态进行滚动更新，会对更新速度造成一定影响。
- 不支持 HostNetwork 类型的工作负载。

### 操作步骤

<dx-tabs>
::: 控制台操作指引
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 参考 [控制台创建 Service](https://cloud.tencent.com/document/product/457/45489#.E5.88.9B.E5.BB.BA-service) 步骤，进入 “新建Service” 页面，根据实际需求设置 Service 参数。
    其中，部分关键参数信息需进行如下设置，如下图所示：
![](https://main.qcloudimg.com/raw/5190f97b699f9d0d856aeb0412a9428f.png)
 - **服务访问方式**：选择为**公网LB访问**或**内网LB访问**。
 - **网络模式**：勾选**采用负载均衡直连Pod模式**。
 - **Workload绑定**：选择**引用Workload**。
3. 单击**创建服务**，完成创建。 
		
:::
::: YAML\s操作指引
直连 Pod 模式 Service 的 YAML 配置与普通 Service YAML 配置相同，示例中的 annotation 即代表是否开启直连 Pod 模式。

```
kind: Service
apiVersion: v1
metadata:
  annotations:
    service.cloud.tencent.com/direct-access: "true" ##开启直连 Pod 模式
  name: my-service
spec:
  selector:
    app: MyApp
  ports:
  - protocol: TCP
    port: 80
    targetPort: 9376
  type: LoadBalancer
```

####  annotation 扩展

负载均衡 CLB 的相关配置可参见 [TkeServiceConfig 介绍](https://cloud.tencent.com/document/product/457/41895)。其中相关 annotation 配置如下：

```
service.cloud.tencent.com/tke-service-config: [tke-service-configName]
```

:::
</dx-tabs>














### 注意事项

#### 如何保证滚动更新时的可用性保证

Kubernetes 官方提供的一个特性 ReadinessGate，主要是用来控制 Pod 的状态，集群版本需高于1.12。默认情况下，Pod 有以下 Condition：PodScheduled、Initialized、ContainersReady，当这几个状态都 Ready 的时候，Pod Ready 的 Condition 就通过了。但是在云原生场景下，Pod 的状态可能需要参考其他状态。ReadinessGate 提供了这样一个机制，允许为 Pod 的状态判断添加一个栅栏，由第三方来进行判断与控制。这样 Pod 的状态就和第三方关联起来了。


#### 直连模式滚动更新的变化

当用户开始为应用做滚动更新的时候，Kubernetes 会根据更新策略进行滚动更新。但其判断一批 Pod 启动的标识仅包括 Pod 自身的状态，并不会考虑该 Pod 在负载均衡上是否配置健康检查且通过。如在接入层组件高负载时，不能及时对此类 Pod 进行及时调度，则滚动更新成功的 Pod 可能并没有正在对外提供服务，从而导致服务的中断。
为了关联滚动更新和负载均衡的后端状态，TKE 接入层组件引入了 Kubernetes 1.12中引入的新特性 `ReadinessGate`。TKE 接入层组件仅在确认后端绑定成功并且健康检查通过时，通过配置 `ReadinessGate `的状态来使 Pod 达到 Ready 的状态，从而推动整个工作负载的滚动更新。

#### 在集群中使用 ReadinessGate 


Kubernetes 集群提供了服务注册的机制，只需要将您的服务以 `MutatingWebhookConfigurations` 资源的形式注册至集群即可。集群会在 Pod 创建的时候按照配置的回调路径进行通知，此时可对 Pod 进行创建前的操作，即给 Pod 加上 `ReadinessGate`。需注意此回调过程必须是 HTTPS，即需要在 `MutatingWebhookConfigurations` 中配置签发请求的 CA，并在服务端配置该 CA 签发的证书。

#### ReadinessGate 机制的灾难恢复

用户集群中的服务注册或证书有可能被用户删除，虽然这些系统组件资源不应该被用户修改或破坏。在用户对集群的探索或是误操作下，这类问题会不可避免的出现。因此接入层组件在启动时会检查以上资源的完整性，在完整性受到破坏时会重建以上资源，加强系统的鲁棒性。详情可参见 [Kubernetes Pods ReadinessGate 特性](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-readiness-gate)。














## 容器网络模式为 GlobalRouter 

### 使用限制

- 单个工作负载仅能运行在一种网络模式下，您可选择弹性网卡直连或 GlobalRoute 直连。
- 仅支持带宽上移账号，如若当前账户是传统账号类型（带宽非上移），可参见 [账户类型升级说明](https://cloud.tencent.com/document/product/1199/49090)。
- 默认 CLB 的后端数量限制是 200 个，如果您绑定的工作负载的副本数超过 200 时，可通过 [在线咨询](https://cloud.tencent.com/online-service?from=doc_457) 提升负载均衡 CLB 的配额。
- 使用 CLB 直连 Pod，需注意网络链路受云服务器的安全组限制，确认安全组配置是否放开对应的协议和端口，**需要开启 CVM 上工作负载对应的端口**。
- 开启直连后，默认将启用 [ReadinessGate](https://cloud.tencent.com/document/product/457/48768#.E5.BC.95.E5.85.A5-readinessgate) 就绪检查，将会在 Pod 滚动更新时检查来自负载均衡的流量是否正常，需要为业务方配置正确的健康检查配置，详情可参见 [TkeServiceConfig 介绍](https://cloud.tencent.com/document/product/457/41895)。
- 直连 Globalrouter 模式下的 Pod 为内测功能，您可通过以下两种方式进行使用：
 - **通过 [云联网](https://cloud.tencent.com/document/product/877) 使用。**推荐使用该方式，云联网可以校验绑定的 IP 地址，防止出现绑定出错、地址回环等 IP 绑定常见问题。操作步骤如下：
   1. 创建云联网实例。详情可参见 [新建云联网实例](https://cloud.tencent.com/document/product/877/18752)。
   2. 将集群所在 VPC 添加至已创建的云联网实例中。
   3. 将容器网段注册到云联网，在集群的“基本信息”页面中开启云联网。
![](https://main.qcloudimg.com/raw/e9c44e7cb6ba38bc1ab34ea1f4d91cef.png)
 - **您可通过 [在线咨询](https://cloud.tencent.com/online-service?from=doc_457) 进行申请。**此方式缺少云联网的 IP 校验功能，不推荐使用。


### 操作步骤

<dx-tabs>
::: 控制台操作指引
**前置使用条件**
<li>在 `kube-system/tke-service-controller-config` ConfigMap 中新增 `GlobalRouteDirectAccess: "true"` 以开启 GlobalRoute 直连能力。</li>
<li>该功能需要开通 CLB SNAT Pro 的白名单，您可通过 <a href="https://cloud.tencent.com/online-service?from=doc_457">在线咨询</a> 进行申请。</li>
<br>

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 参考 [控制台创建 Service](https://cloud.tencent.com/document/product/457/45489#.E5.88.9B.E5.BB.BA-service) 步骤，进入 “新建Service” 页面，根据实际需求设置 Service 参数。
    其中，部分关键参数信息需进行如下设置，如下图所示：
![](https://main.qcloudimg.com/raw/5190f97b699f9d0d856aeb0412a9428f.png)
 - **服务访问方式**：选择为**公网LB访问**或**内网LB访问**。
 - **网络模式**：勾选**采用负载均衡直连Pod模式**。
 - **Workload绑定**：选择**引用Workload**。
3. 单击**创建服务**，完成创建。 
:::
::: YAML\s操作指引
直连 Pod 模式 Service 的 YAML 配置与普通 Service YAML 配置相同，示例中的 annotation 即代表是否开启直连 Pod 模式。

**前置使用条件**
<li>在 `kube-system/tke-service-controller-config` ConfigMap 中新增 `GlobalRouteDirectAccess: "true"` 以开启 GlobalRoute 直连能力。</li>
<li>该功能需要开通 CLB SNAT Pro 的白名单，您可通过 <a href="https://cloud.tencent.com/online-service?from=doc_457">在线咨询</a> 进行申请。</li>
<br>

**在 Service YAML 里开启直连模式**

```
kind: Service
apiVersion: v1
metadata:
  annotations:
    service.cloud.tencent.com/direct-access: "true" ##开启直连 Pod 模式
  name: my-service
spec:
  selector:
    app: MyApp
  ports:
  - protocol: TCP
    port: 80
    targetPort: 9376
  type: LoadBalancer
```

####  annotation 扩展


负载均衡 CLB 的相关配置可参见 [TkeServiceConfig 介绍](https://cloud.tencent.com/document/product/457/41895)。其中相关 annotation 配置如下：

```
service.cloud.tencent.com/tke-service-config: [tke-service-configName]
```



:::
</dx-tabs>


