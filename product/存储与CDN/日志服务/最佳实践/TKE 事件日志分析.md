## 概述

集群内的状况层出不穷，变化莫测，如节点状态异常，Pod 重启等，如果无法第一时间感知状况，会错过最佳的问题处理时间，待问题扩大，影响到业务时才发现往往已经为时已晚。
而事件日志（Event）记录了全面的集群状态变更信息，不仅可以帮助用户第一时间发现问题，也是排查问题的最佳帮手。

## 什么是事件日志

Event 是 Kubernetes 中众多资源对象中的一员，通常用来记录集群内发生的状态变更，大到集群节点异常，小到 Pod 启动、调度成功等等。我们常用的`kubectl describe`命令就可以查看相关资源的事件信息。

## 事件日志字段说明

![img](https://main.qcloudimg.com/raw/6d6dabec677912952415964e6d525966.png)

- 级别（Type）： 目前仅有 “Normal” 和 “Warning”，但是如果需要，可以使用自定义类型。
- 资源类型/对象（Involved Object）：事件所涉及的对象，例如 Pod，Deployment，Node 等。
- 事件源（Source）：报告此事件的组件；例如 Scheduler、Kubelet等。
- 内容（Reason）：当前发生事件的简短描述，一般为枚举值，主要在程序内部使用。
- 详细描述（Message）：当前发生事件的详细描述信息。
- 出现次数（Count）：事件发生的次数。

## 如何使用事件日志去排查问题

日志服务（Cloud Log Service，CLS）提供针对 kubernetes 事件日志的一站式服务，包含采集，存储，检索分析能力。用户仅需一键开启集群事件日志功能，即可获取开箱即用的事件日志可视化分析仪表盘。通过可视化的图表，用户可以轻松通过控制台解决大多数常见的运维问题。

### 前提条件

已购买容器服务（Tencent Kubernetes Engine，TKE），并开启集群事件日志，详情请参考 [操作指南](https://cloud.tencent.com/document/product/457/32091)。

### 场景1：一台 Node 节点出现异常，定位原因

1. 登录 [TKE 控制台](https://console.cloud.tencent.com/tke2/cluster?rid=1)。
2. 在左侧导航栏中，单击**集群运维** > **事件检索**。
3. 在事件检索页面，选择**事件总览**页签，并在过滤项中输入异常节点名称。
![img](https://main.qcloudimg.com/raw/b61b2b0ba24676d1d70b725e7819dbf9.png)
查询结果显示，有一条`节点磁盘空间不足`的事件记录查询结果如下图：
![img](https://main.qcloudimg.com/raw/c4f38491b71725467dd6a78a8ae7f775.png)
进一步查看异常事件趋势和异常 Top 事件：
![img](https://main.qcloudimg.com/raw/cfd8dd18d2a1c4040eec73ea7c916fb8.png)
![img](https://main.qcloudimg.com/raw/d70b834365064f1362814121174dcfbf.png)
可以发现，`2020-11-25`号开始，节点`172.16.18.13`由于磁盘空间不足导致节点异常，此后 kubelet 开始尝试驱逐节点上的 pod 以回收节点磁盘空间。

### 场景2：节点触发扩容了，用户需要对扩容过程进行回溯，以确定具体原因

开启 [节点池](https://cloud.tencent.com/document/product/457/43719)「弹性伸缩」的集群，CA（cluster-autoscler）组件会根据负载状况自动对集群中节点数量进行增减。如果集群中的节点发生了自动扩（缩）容，用户可通过事件检索对整个扩（缩）容过程进行回溯。
1. 登录 [TKE 控制台](https://console.cloud.tencent.com/tke2/cluster?rid=1)。
2. 在左侧导航栏中，单击**集群运维** > **事件检索**。
3. 在事件检索页面，单击**全局检索**页签，并输入以下检索命令：
```
event.source.component : "cluster-autoscaler"
```
4. 在左侧隐藏字段中，选择`event.reason`、`event.message`、`event.involvedObject.name`、`event.involvedObject.name`进行显示，将查询结果按照`日志时间`倒序排列。结果如下图所示：
![img](https://main.qcloudimg.com/raw/7d4057c00b780a99bbcac25004d84d0c.png)
通过上图的事件流水，可以看到节点扩容操作在`2020-11-25 20:35:45`左右，分别由三个 nginx Pod(nginx-5dbf784b68-tq8rd、nginx-5dbf784b68-fpvbx、nginx-5dbf784b68-v9jv5) 触发，最终扩增了3个节点，后续的扩容由于达到节点池的最大节点数没有再次触发。


