



## 概述

Kubernetes Pod 水平自动扩缩（Horizontal Pod Autoscaler，以下简称 HPA）可以基于 CPU 利用率、内存利用率和其他自定义的度量指标自动扩缩 Pod 的副本数量，以使得工作负载服务的整体度量水平与用户所设定的目标值匹配。本文将介绍和使用腾讯云容器服务 TKE 的 HPA 功能实现 Pod 自动水平扩缩容。

## 使用场景

HPA 自动伸缩特性使容器服务具有非常灵活的自适应能力，能够在用户设定内快速扩容多个 Pod 副本来应对业务负载的急剧飙升，也可以在业务负载变小的情况下根据实际情况适当缩容来节省计算资源给其他的服务，整个过程自动化无须人为干预，适合服务波动较大、服务数量多且需要频繁扩缩容的业务场景，例如：电商服务、线上教育、金融服务等。

## 原理概述

Pod 水平自动扩缩特性由 Kubernetes API 资源和控制器实现。资源利用指标决定控制器的行为，控制器会周期性的根据 Pod 资源利用情况调整服务 Pod 的副本数量，以使得工作负载的度量水平与用户所设定的目标值匹配。其扩缩容流程如下图所示：
>! Pod 自动水平扩缩不适用于无法扩缩的对象，例如 DaemonSet 资源。
>
![hpa](https://main.qcloudimg.com/raw/0d5a5ba9445f1f74abcf8f4acf2d89f8.jpg)
重点内容说明：
- **HPA Controller**：控制 HPA 扩缩逻辑的控制组件。
- **Metrics Aggeregator**：度量指标聚合器。通常情况下，控制器将从一系列的聚合 API（`metrics.k8s.io`、`custom.metrics.k8s.io` 和 `external.metrics.k8s.io`）中获取度量值。`metrics.k8s.io` API 通常由 Metrics 服务器提供，社区版可提供基本的 CPU、内存度量类型。相比于社区版，TKE 使用自定义 Metrics Server 采集可支持更广泛的 HPA 的度量指标触发类型，提供包括 CPU 、内存、硬盘、网络和 GPU 相关指标，了解更多详细内容请参见 [TKE 自动伸缩指标说明]( https://cloud.tencent.com/document/product/457/38929)。
>? 控制器也可从 Heapster 获取指标。但自 Kubernetes 1.11 版本起，从 Heapster 获取指标特性的方式已废弃。
>
- **HPA 计算目标副本数算法**：TKE HPA 扩缩容算法请参见 [工作原理](https://cloud.tencent.com/document/product/457/37384#.E5.B7.A5.E4.BD.9C.E5.8E.9F.E7.90.86)，更多详细算法请参见 [算法细节](https://kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale/#algorithm-details)。

## 前提条件

- 已 [注册腾讯云账户](https://cloud.tencent.com/register)。
- 已登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/tke2)。
- 已创建 TKE 集群。关于创建集群，详情请参见 [创建集群](https://cloud.tencent.com/document/product/457/32189)。

## 操作步骤
### 部署测试工作负载

以 Deployment 资源类型的工作负载为例，创建一个单副本数，服务类型为  Web 服务的 “hpa-test” 工作负载。在容器服务控制台创建Deployment 类型工作负载方法请参见 [Deployment 管理](https://cloud.tencent.com/document/product/457/31705)。
本示例创建结果如下图所示： 
![image-20201105173748658](https://main.qcloudimg.com/raw/8f66b02ddfe9b5d5062c1f9e0e1e5333.png)

### 配置 HPA 

在容器服务控制台为测试工作负载绑定一个 HPA 配置，关于如何绑定配置 HPA 请参见 [HPA 操作步骤](https://cloud.tencent.com/document/product/457/37384#.E6.93.8D.E4.BD.9C.E6.AD.A5.E9.AA.A4)，本文以配置当网络出带宽达到0.15Mbps（150Kbps）时触发扩容的策略为例。如下图所示：
![image-20201106155539282](https://main.qcloudimg.com/raw/c4f4e6e08382e71f087da5b49852a5fe.png)

### 功能验证
#### 模拟扩容过程
执行以下命令，在集群中启动一个临时 Pod 对配置的 HPA 功能进行测试（模拟客户端）：
```bash
kubectl run -it --image alpine hpa-test --restart=Never --rm /bin/sh
```
在临时 Pod 中执行以下命令，模拟在短时间内用大量请求访问 "hpa-test" 服务使出口流量带宽增大：
```bash
# hpa-test.default.svc.cluster.local 为服务在集群中的域名，当需要停止脚本时按 Ctrl+C 即可
while true; do wget -q -O - hpa-test.default.svc.cluster.local; done   
```
在测试 Pod 中执行模拟请求命令后，通过观察工作负载的 Pod 数量监控，发现在16:21分时工作负载扩容副本数量至2个，由此可推断出已经触发了 HPA 的扩容事件。如下图所示：
![image-20201106164540791](https://main.qcloudimg.com/raw/54c7fb16668fcf0404ee45d3722d0b84.png)
再通过工作负载的网络出口带宽监控可以观察到在16:21时网络出口带宽增至大概196Kbps，已经超过 HPA 设定的网络出口带宽目标值，进一步证明此时触发 HPA  [扩缩容算法](https://cloud.tencent.com/document/product/457/37384#.E5.B7.A5.E4.BD.9C.E5.8E.9F.E7.90.86)，扩容了一个副本数来满足设定的目标值，故工作负载的副本数量变成了2个。如下图所示：
>! HPA [扩缩容算法](https://cloud.tencent.com/document/product/457/37384#.E5.B7.A5.E4.BD.9C.E5.8E.9F.E7.90.86) 不只以公式计算维度去控制扩缩容逻辑，而会多维度去衡量是否需要扩容或缩容，所以在实际情况中可能和预期会稍有偏差，详情可参见 [算法细节](https://kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale/#algorithm-details)。
>
![image-20201106165107310](https://main.qcloudimg.com/raw/7451abe924d06df2a71832354c0ae572.png)

 #### 模拟缩容过程

模拟缩容过程时，在16:24左右手动停止执行模拟请求的命令，从监控可以观察到此时网络出口带宽值下降到扩容前位置，按照 HPA 的逻辑，此时已经满足工作负载缩容的条件。如下图所示：
![image-20201106165205910](https://main.qcloudimg.com/raw/19acc1b78c28863e1857836294d64310.png)
但从下图工作负载的 Pod 数量监控可以看出，工作负载在16:30分时才触发了 HPA 的缩容，原因是触发 HPA 缩容后有默认5分钟容忍的时间算法，以防止度量指标短时间波动导致的频繁的扩缩容，详情请参见 [冷却 / 延迟支持](https://kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale/#%E5%86%B7%E5%8D%B4-%E5%BB%B6%E8%BF%9F%E6%94%AF%E6%8C%81)。从下图可以看出工作负载副本数在停止命令5分钟后按照 HPA [扩缩容算法](https://cloud.tencent.com/document/product/457/37384#.E5.B7.A5.E4.BD.9C.E5.8E.9F.E7.90.86) 缩容到了最初设定的1个副本数。如下图所示：
![image-20201106164648921](https://main.qcloudimg.com/raw/58a538f52c3601759036dc9a0ee455cb.png)
当 TKE 发生 HPA 扩缩容事件时，会在对应的 HPA 实例的事件列表展示。需要注意的是事件通知列表的时间分为 “首次出现时间” 和 “最后出现时间”，“首次出现时间” 表示相同事件第一次出现的时间，“最后出现时间” 为相同事件出现的最新时间，所以从下图事件列表 “最后出现时间” 字段可以看到本示例扩容事件时间点是16:21:03，缩容事件时间是16.29:42，时间点与工作负载监控看到的时间点相吻合。如下图所示：
![image-20201106164245358](https://main.qcloudimg.com/raw/2d1bc7a10640ae779130ca2d35a85498.png)
此外，工作负载事件列表也会记录 HPA 发生时工作负载的增删副本数事件，从下图可以看出工作负载扩缩容时间点与 HPA 事件列表的时间点也是吻合的，增加副本数时间点是16:21:03，减少副本数时间点是16:29:42。
![image-20201106164329173](https://main.qcloudimg.com/raw/956d37b12ec4246945c75bfd482251af.png)



## 总结

在本示例中主要演示了 TKE 的 HPA 功能，即使用 TKE 自定义的网络出口带宽度量类型作为工作负载 HPA 的扩缩容度量指标：
 - 当工作负载实际度量值超过 HPA 配置的度量目标值时，HPA 根据扩容算法计算出合适的副本数实现水平扩容，保证工作负载的度量指标满足预期及工作负载健康稳定运行。
 - 当实际度量值远低于 HPA 配置的度量目标值时，HPA 会在容忍时间后计算合适的副本数实现水平缩容，适当释放闲置资源，达到提升资源利用率的目的，并且整个过程在 HPA 和工作负载事件列表都会有相应的事件记录，使整个工作负载水平扩缩容全程可追溯。
