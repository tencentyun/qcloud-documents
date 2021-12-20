
## Request 智能推荐
>? Request 智能推荐功能目前处于内部邀请使用阶段，如需使用可 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请。
>
### 介绍

Kubernetes 可以有效的提升业务编排能力和资源利用率，但如果没有额外的能力支撑，提升的能力十分有限，根据 TKE 团队之前统计的数据：[Kubernetes 降本增效标准指南 | 容器化计算资源利用率现象剖析](https://mp.weixin.qq.com/s/8sHsI1pVm-1RX5w1F3uWPg)，TKE 节点的资源平均利用率也只有14%左右。如下图所示：
![](https://main.qcloudimg.com/raw/b0a71f06a0aba33be0df9fc2a7e772bf.png)


为什么 Kubernetes 集群的资源利用率依旧不高？主要是因为 Kubernetes 的资源调度逻辑，在创建 Kubernetes 工作负载的时候，通常需要为工作负载配置合适的资源 Request 和 Limit，表示对资源的占用和限制，其中对利用率影响最大的是 Request。为防止自己的工作负载所用的资源被别的工作负载所占用，或者是为了应对高峰流量时的资源消耗诉求，用户一般都习惯将 Request 设置得较大，这样 Request 和实际使用之间的差值，就造成了浪费，而且这个差值的资源，是不能被其它工作负载所使用的。Request 数值不合理的过大，是造成 Kubernetes 集群资源利用率低一个很普遍的现象。

Request 智能推荐可以为 Kubernetes 的 Workload 推荐容器级别资源的 Request/Limit 数值，减少资源浪费。

### 部署在集群内的资源对象

开启集群的 Request 智能推荐 , 将在集群内部署以下 Kubernetes 对象：

| Kubernetes 对象名称           | 类型               | 默认占用资源          | 所属 Namespaces |
| ----------------------------- | ------------------ | --------------------- | --------------- |
| v1beta1.recommendation.tke.io | APIService         | -                    | -               |
| recommendation-server         | ClusterRole        | -                     |-              |
| recommendation-server         | ClusterRoleBinding |-                     | -               |
| recommendation-server         | Service            | -                    | kube-system     |
| recommendation-server         | ServiceAccount     | -                     | kube-system     |
| recommendation-server         | Deployment         | CPU: 250m; Mem: 512Mi | kube-system     |


## 功能说明

  - 支持为 Deployment、StatefulSet、DaemonSet 中的每一个 Container 智能推荐合适的资源 Request/Limit。
  - 支持一键更新：使用推荐值一键更新 Workload 中 Container 的资源值。
  - 支持维持 Request/Limit 比例：推荐的 Request/Limit 会维持初始 Workload 中 Container 设置的 Reqeust/Limit 之间的比例，若 Limit 在创建 Workload 时没有设置，则不会推荐 Limit。



## 注意事项

#### 环境要求

Kubernetes 版本： 1.10+


#### 节点要求
X86，不支持 ARM 机型

#### 被控资源要求

- 支持 Deployment、StatefulSet、DaemonSet。
- 不支持 Job、CronJob，不支持不是由 Workload 管理的 Pod。

#### 推荐阈值

推荐最小值：单个 Pod 推荐的 CPU 最小值是0.025核，即25m；内存的最小值是100Mi。

>!若一个 Pod 中存在多个 Container，则会出现单个 Container 的 CPU 推荐值小于0.025，但该 Pod 的推荐最小值依然是0.025，内存同样如此。



## 操作步骤

### 开启/关闭 Request 智能推荐

1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)。
2. 进入到某一集群后，在左侧导航栏中，单击**基本信息**，进入集群基本信息页面。
3. 找到 **Request智能推荐**，单击打开右侧的开关。
![](https://main.qcloudimg.com/raw/d793072559e2f8f4f6ce60b93c58930e.png)

### 使用 Request 智能推荐

开启 Request 智能推荐后，在**工作负载**的 Deployment、StatefulSet、DaemonSet 的列表里，**推荐 Request** 该列，会出现数值，如下图的1所示。
>!
> - 开启后非立即生效，为准确计算推荐值，需要分析该 Workload 的历史资源使用数据。
> - 不同的 Workload 的计算时间长度可能不太一样，集群中不同的 Workload 之间互相可能会有影响。
> - 开启该功能后，对至少运行一天的 Workload 产生推荐数据。
> - 对于开启功能后新建的 Workload，一般情况下，也需要一天的时间才会产生 Workload 的推荐数据。

如果当平台发现当前工作负载的 Request 设置过于不合理时，会出现红色感叹号的提示，提醒用户需要手动调整 Request，如下图的2所示：
![](https://main.qcloudimg.com/raw/dac27eba9816bf851fb26ee66365b70e.jpg)

如上图所示，对于配置很不合理的 Request，当鼠标悬浮到红色感叹号的提示图标上后，可以单击查看推荐的 Request，以及比较现有 Request 和推荐 Request 之间的差距：
![](https://main.qcloudimg.com/raw/e48e7c3b3b9ba811ff52af9469a9f90f.png)

>!更新会使用新的 Request 数值对工作负载进行滚动更新，会重建 Pod。

您二次确定后，点击下图红色方框里的“更新”按钮，就可以一键使用推荐的 Request 数值更新原有工作负载里的 Request 数值。

![](https://main.qcloudimg.com/raw/185aca2412fa89c60204a2c9141801af.png)

### 通过 Kubectl 获取工作负载 Request 智能推荐值

在开启 Request 智能推荐后，支持用户后台通过 Kubectl 参看工作负载 Request 智能推荐值，配置 Kubectl 可以请参见 [连接集群](https://cloud.tencent.com/document/product/457/32191)。

命令示例：
```shell
kubectl get --raw "/apis/recommendation.tke.io/v1beta1/namespaces/default/deployments/<name>"
```

例如：
在开启 Request 智能推荐后，若您需要访问 kube-system 命名空间下名为 kube-proxy 的 daemonset 的资源推荐值：
![](https://main.qcloudimg.com/raw/504e5341c7f95319c1615034fabe6664.png)
