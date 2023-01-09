


## 简介


### 组件介绍

Kubernetes 可以有效的提升业务编排能力和资源利用率，但如果没有额外的能力支撑，提升的能力十分有限，根据 TKE 团队之前统计的数据：[Kubernetes 降本增效标准指南 | 容器化计算资源利用率现象剖析](https://mp.weixin.qq.com/s/8sHsI1pVm-1RX5w1F3uWPg)，TKE 节点的资源平均利用率也只有14%左右。如下图所示：
![](https://main.qcloudimg.com/raw/b0a71f06a0aba33be0df9fc2a7e772bf.png)


Kubernetes 集群的资源利用率不高的主要原因是根据 Kubernetes 的资源调度逻辑，在创建 Kubernetes 工作负载时，通常需要为工作负载配置合适的资源 Request 和 Limit，表示对资源的占用和限制，其中对利用率影响最大的是 Request。为防止自己的工作负载所用的资源被别的工作负载所占用，或者是为了应对高峰流量时的资源消耗诉求，用户习惯于为 Request 设置较大的数值，Request 和实际使用资源之间的差值，是不能被其它工作负载所使用的，因此造成了浪费。Request 数值设置不合理，造成了 Kubernetes 集群资源利用率低。

容器服务 TKE 支持在集群中安装 **Request 智能推荐**组件。Request 智能推荐可以为 Kubernetes 的 Workload 推荐容器级别资源的 Request/Limit 数值，减少资源浪费。

### 部署在集群内的资源对象

开启集群的 Request 智能推荐 , 将在集群内部署以下 Kubernetes 对象：

| Kubernetes 对象名称               | 类型                     | 默认占用资源 | 所属 Namespaces |
| --------------------------------- | ------------------------ | ------------ | --------------- |
| analytics.analysis.crane.io       | CustomResourceDefinition | -            | -               |
| recommendations.analysis.crane.io | CustomResourceDefinition | -            | -               |
| crane-system                      | Namespace                | -            | -               |
| housekeeper-default               | Analytics                | -            | crane-system    |
| recommendation-config             | ConfigMap                | -            | crane-system    |
| craned                            | ClusterRole              | -            | -               |
| craned                            | ClusterRoleBinding       | -            | -               |
| craned                            | Service                  | -            | crane-system    |
| craned                            | ServiceAccount           | -            | crane-system    |
| craned                            | Deployment               | -            | crane-system    |


## 功能说明

  - 支持为 Deployment、StatefulSet、DaemonSet 中的每一个 Container 智能推荐合适的资源 Request/Limit。
  - 支持一键更新：使用推荐值一键更新 Workload 中 Container 的资源值。
  - 支持维持 Request/Limit 比例：推荐的 Request/Limit 会维持初始 Workload 中 Container 设置的 Reqeust/Limit 之间的比例，若 Limit 在创建 Workload 时没有设置，则不会推荐 Limit。
  - 控制台的 Request 推荐一键更新能力会默认给工作负载加上 nodeSelector 的属性，Workload 在更新时， Pod 将只能调度到原生节点上，若原生节点资源不足，会引发 Pod 的 Pending。

## Request 推荐原理

- 组件在 crane-system 命名空间下创建 Analytics CR 对象，覆盖所有集群中的所有 Kubernetes 原生工作负载（Deployment、DaemonSet、StatefulSet），会分析工作负载最长 14 天的监控数据数据，10 分钟更新一次推荐值。
- 然后根据 Analytics 生成集群内每个工作负载的 Recommendation CR 对象，用于存储推荐的数据。
- Recommendation CR 如果产生了推荐数据，就会把推荐数据写入到对应工作负载的 Annotation 里。

![](https://qcloudimg.tencent-cloud.cn/raw/814d0d52c0adec6dac7c0b5e6278bd6a.png)

## 注意事项

#### 环境要求

Kubernetes 版本：1.10+


#### 节点要求
容器服务控制台中**一键更新 Workload Request** 功能会将工作负载迁移至 [原生节点](https://cloud.tencent.com/document/product/457/78197)，若您的集群原生节点上资源不足，会导致 Pod 发生 Pending。

#### 被控资源要求

- 支持 Deployment、StatefulSet、DaemonSet。
- 不支持 Job、CronJob，不支持不是由 Workload 管理的 Pod。

#### 推荐阈值

推荐最小值：单个容器推荐的 CPU 最小值是0.125核，即125m；内存的最小值是125Mi。

## 使用说明

### 安装组件


1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2/cluster?rid=8)。
2. 在左侧选择**云原生资产管理 > Node Map**。
>? 您也可以在**云原生资产管理 > Workload Map** 中进行安装。
>
3. 在“Node Map”页面中，鼠标悬浮到页面下方某一个 Node 上，单击“详情”。
4. 在该 Node 的详情页的右上角，打开“Request 推荐”开关，进行调度器的参数配置。
![](https://qcloudimg.tencent-cloud.cn/raw/a1e1dd9a7904168a41d07e61d311039d.png)
>!
>- 该功能是集群级别的全局开关，开启后，会自动分析工作负载历史的监控数据，推荐合适的 Request 数值。
>- 开启后非立即生效，为准确计算推荐值，需要分析该 Workload 的历史资源使用数据。
>- 不同的 Workload 的计算时间长度可能不一致，集群中不同的 Workload 之间互相可能会有影响。
>- 开启该功能后，对至少运行一天的 Workload 产生推荐数据。
>- 对于开启功能后新建的 Workload，一般情况下，也需要一天的时间才会产生 Workload 的推荐数据。
>- 建议工作负载稳定运行一段时间之后，再使用推荐值更新 Workload。

### 使用组件

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2/cluster?rid=8)。
2. 在左侧选择**云原生资产管理 > Workload Map**。
>? Workload Map 主要通过可视化的页面展示工作负载的各项状态和指标，帮助用户了解当前工作负载的配置量和实际使用情况，辅助用户分析工作负载可能存在的问题。更多可参考文档 [Workload Map](https://cloud.tencent.com/document/product/457/78330)。
>
3. 在 Workload Map 页面，鼠标悬浮到页面下方某一个 Workload 上，单击**推荐**。
![](https://qcloudimg.tencent-cloud.cn/raw/3bb6d58e856269fe3a701a1d52625cf3.png)
4. 在弹窗中，单击**确认**，即可使用推荐的 Request 数值更新原始 Workload 里面的数值。
>? 容器服务控制台中**一键更新 Workload Request** 功能会将工作负载迁移至 [原生节点](https://cloud.tencent.com/document/product/457/78197)，若您的集群原生节点上资源不足，会导致 Pod 发生 Pending。

### 后台获取推荐数值

Request 智能推荐组件会将每个工作负载的推荐值保存在该工作负载的 YAML 里，您可以通过标准的 Kuberentes API 获取每个工作负载的推荐值，然后集成到业务的发布系统中。如下所示查看工作负载下每个容器的 Request 推荐量：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  annotations:
    analysis.crane.io/resource-recommendation: |
      containers:
      # 若一个 Pod 里有多个容器，每个容器都有 CPU 和 Memory 的 Request 的推荐值
      - containerName: nginx
        target:
          cpu: 125m
          memory: 125Mi
  ```
  
>! 组件本身不会推荐 Limit，在控制台使用 Request 推荐值更新 Workload 时，会维持该 Workload Request 和 Limit 的比值以保证 QoS 不会发生变化。您如果在后台获取到 Request 推荐值，可以作为参考更新原始 Workload 的资源配置量。



