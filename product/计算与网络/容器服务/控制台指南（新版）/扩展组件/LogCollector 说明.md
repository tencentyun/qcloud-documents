## 简介
### 组件介绍

日志收集功能是 TKE 为用户提供的集群内日志收集工具，可以将集群内服务或集群节点特定路径文件的日志发送至 Kafka 的指定 Topic 或者日志服务 CLS 的指定日志主题。

日志收集功能需要在每个集群中手动开启。功能开启后，日志收集 Agent 会在集群内以 Daemonset 的形式运行。用户可以通过日志收集规则配置日志的采集源和消费端，日志收集 Agent 会从用户配置的采集源进行日志收集，并将日志内容发送至用户指定的消费端。需要注意的是，使用日志收集功能需确保 Kubernetes 集群内节点能够访问日志消费端。

### 部署在集群内的 Kubernetes 对象

在集群内部署 LogCollector Add-on，将在集群内部署以下 Kubernetes 对象：

| Kubernetes 对象名称 | 类型        | 默认占用资源              | 所属 Namespaces |
| -------------- | --------- | ------------------- | ------------ |
| log-collector  | DaemonSet | 每节点0.3核 CPU，250MB内存 | kube-system  |

## 使用场景

日志收集功能适用于需要对 Kubernetes 集群内服务日志进行存储和分析的用户。用户可以通过配置日志收集规则进行集群内日志的收集，并将收集到的日志发送至 Kafka 的指定 Topic 或日志服务 CLS 的指定日志主题，以供用户的其它基础设施进行消费。

##  限制条件
- 安装 LogCollector 之后，将在集群内所有节点（包括后续新增节点）创建日志采集服务。
- 安装 LogCollector 将占用每个节点0.3核 CPU，250M内存的资源。

## 使用方法

### 组件安装
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的【扩展组件】。
2. 在“扩展组件”管理页面上方，选择地域及需安装 LogCollector 的集群，并单击【新建】。如下图所示：
![](https://main.qcloudimg.com/raw/887d95fb6d298edbb4e9a329440c22c1.png)
2. 在“新建扩展组件”页面，选择【LogCollector 组件】后，单击【完成】即可安装成功。

### 设置日志采集规则
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的【日志采集】。
2. 在“日志采集”管理页面上方，选择地域及已安装 LogCollector 的集群，并单击【新建】创建日志采集规则。如下图所示：
![](https://main.qcloudimg.com/raw/7285a504bcef8d1370e3f9e0abab1d0c.png)
3. 在“新建日志采集规则”页面，参考 [日志采集](https://cloud.tencent.com/document/product/457/36771) 创建规则后开始使用。


