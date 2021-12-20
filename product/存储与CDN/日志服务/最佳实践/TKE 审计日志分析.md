## 概述
以前，排查这些问题，对用户来说并不容易。生产环境中的 Kubernetes 集群通常是一个相当复杂的系统，底层是各种异构的主机、网络、存储等云基础设施，上层承载着大量的应用负载，中间运行着各种原生（例如：Scheduler、Kubelet）和第三方（例如：各种 Operator）的组件,负责对基础设施和应用进行管理和调度； 此外不同角色的人员频繁地在集群上进行部署应用、添加节点等各种操作。因此在集群运维场景中， 用户常见的问题有：
- 集群中的某个应用被删除了，谁干的？
- Apiserver 的负载突然变高，大量访问失败，集群中到底发生了什么？
- 集群节点被封锁了，是谁在什么时候操作的？

当前日志服务（Cloud Log Service，CLS）与 [容器服务（Tencent Kubernetes Engine，TKE）](https://console.cloud.tencent.com/tke2/overview) 已实现打通。 其中，Kubernetes 审计日志（Audit）将是可以帮助用户快速解决以上这些问题的重要工具。

## 什么是审计日志

在 Kubernetes 中，所有对集群状态的查询和修改都是通过向 Apiserver 发送请求，而审计日志是 Kube-apiserver 产生的可配置策略的结构化日志，记录了对 Apiserver 的访问事件。通过查看、分析审计日志，可以追溯对集群状态的变更；了解集群的运行状况；排查异常；发现集群潜在的安全、性能风险等等。

## 审计日志字段说明

每一条审计日志都是一个 JSON 格式的结构化记录，包括元数据（metadata）、请求内容（requestObject）和响应内容（responseObject）3个部分。其中元数据一定会存在，请求和响应内容是否存在取决于审计级别。元数据包含了请求的上下文信息，例如谁发起的请求，从哪里发起的，访问的 URI 等等。
![img](https://main.qcloudimg.com/raw/38ba2499da67d3bfd5219e395083f073.png)

## 如何使用审计日志去排查问题

CLS 提供针对 kubernetes 审计日志的一站式服务，包含采集，存储，检索分析能力。用户仅需一键开启集群审计日志功能，即可获取开箱即用的审计日志可视化分析仪表盘。通过可视化的图表，用户可以轻松通过控制台解决大多数常见的运维问题。

### 前提条件

已购买 TKE，并开启集群审计日志，详情请参考[操作指南](https://cloud.tencent.com/document/product/457/48346)。

### 场景1：集群中的某个应用被删除了，谁操作的？

1. 登录 [TKE 控制台](https://console.cloud.tencent.com/tke2/cluster?rid=1)。
2. 在左侧导航栏中，单击**集群运维** > **审计检索**。
3. 在审计检索页面，单击**K8S对象操作概览**标签，指定操作类型为 delete 和资源对象 nginx。
![img](https://main.qcloudimg.com/raw/0948e4538dc02116432bf016826680dd.png)
查询结果如下图所示：
![img](https://main.qcloudimg.com/raw/dcb4952282eda70f2072904f0eff5ce8.png)
由图可见，是 `10001****7138` 这个账号，对应用「nginx」进行了删除。可根据账号 ID 在**访问管理** > **用户列表**中找到关于此账号的详细信息。

### 场景2：Apiserver 的负载突然变高，大量访问失败，集群中到底发生了什么？

1. 登录 [TKE 控制台](https://console.cloud.tencent.com/tke2/cluster?rid=1)。
2. 在左侧导航栏中，单击**集群运维** > **审计检索**。
3. 在审计检索页面，单击**聚合检索**标签，该页签提供了从用户、操作类型、返回状态码等多个维度对于 Apiserver 访问聚合趋势图。
![img](https://main.qcloudimg.com/raw/ff01a47ec1ece54d658c9d24e68e326b.png)
![img](https://main.qcloudimg.com/raw/82eafe331d2246a2330d96c5ff055c4c.png)
![img](https://main.qcloudimg.com/raw/7118ab856c2fb1cec34ba9cbcb821211.png)
通过以上图表得知，用户`tke-kube-state-metrics`的访问量远高于其他用户，并且在“操作类型分布趋势”图中可以看出大多数都是 list 操作，在“状态码分布趋势”图中可以看出，状态码大多数为403，根据`tke-kube-state-metrics`关键词，检索日志。
![image-20210824111626888](https://main.qcloudimg.com/raw/b4c356fb5fb7549da57132bedf8f6328.png)
结合业务日志可知，由于 RBAC 鉴权问题导致`tke-kube-state-metrics`组件不停的请求 Apiserver 重试，导致 Apiserver 访问剧增。


### 场景3：集群节点被封锁了，是谁在什么时候操作的？

1. 登录 [TKE 控制台](https://console.cloud.tencent.com/tke2/cluster?rid=1)。
2. 在左侧导航栏中，单击**集群运维** > **审计检索**。
3. 在审计检索页面，单击**节点操作概览**标签，填写被封锁的节点名。
![img](https://main.qcloudimg.com/raw/e5eb3310ed5a03fc759ca682b08866f1.png)
查询结果如下图所示：
![img](https://main.qcloudimg.com/raw/eafe73fdcb9dfbbd09f325f4b89feba6.png)
由图可见，是`10001****7138`这个账号在`2020-11-30T06:22:18`时对`172.16.18.13`这台节点进行了封锁操作。




