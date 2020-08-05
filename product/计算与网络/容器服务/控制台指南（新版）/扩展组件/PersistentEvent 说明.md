## 简介

### 组件介绍

Kubernetes Events 包括了 Kubernetes 集群的运行和各类资源的调度情况，对维护人员日常观察资源的变更以及定位问题均有帮助。TKE 支持为您的所有集群配置事件持久化功能，开启本功能后，会将您的集群事件实时导出到配置的存储端。TKE 还支持使用腾讯云提供的 PAAS 服务或开源软件对事件流水进行检索。


### 部署在集群内的 Kubernetes 对象

在集群内部署 PersistentEvent Add-on , 将在集群内部署以下 Kubernetes 对象：

| Kubernetes 对象名称       | 类型         | 默认占用资源          | 所属 Namespaces|
| -------------------- | ---------- | --------------- | ------------ |
| tke-persistent-event | deployment | 0.2核 CPU，100MB内存 | kube-system  |

## 使用场景

Kubernetes 事件是集群内部资源生命周期、资源调度、异常告警等情况产生的记录，可以通过事件深入了解集群内部发生的事情，例如调度程序做出的决策或者分析某些 Pod 从节点中被逐出的原因。

Kubernetes 默认仅提供保留一个小时的 Kubernetes 事件。而 PersistentEvent 提供了将 Kubernetes 事件持久化存储的前置功能，允许您通过 PersistentEvent 将集群内事件导出到您自有的存储端。

## 限制条件
- 安装 PersistentEvent 将占用集群0.2核 CPU 以及100MB内存的资源。
- 支持 1.8 版本以上的 Kubernetes 集群。

## 使用方法

### 安装并设置存储端
1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)，选择左侧导航栏中的【扩展组件】。
2. 在“扩展组件”管理页面上方，选择需安装 PersistentEvent 地域下的集群，并单击【新建】。如下图所示：
![](https://main.qcloudimg.com/raw/d087e46c782e0fe391bb0abd7d2af71d.png)
3. 在“新建扩展组件”页面，选择【PersistentEvent 组件】并配置事件持久化存储端，单击【完成】即可安装成功。
PersistentEvent 支持 [Elasticsearch](https://cloud.tencent.com/document/product/845/16478) 及 [日志服务 CLS](https://cloud.tencent.com/document/product/614/11254) 两种存储端选择，推荐使用日志服务 CLS。您可根据实际情况进行选择，本文以日志服务 CLS 为例。




### 更新存储端
1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)，选择左侧导航栏中的【扩展组件】。
2. 在“扩展组件”页面上方选择需更新地域下 PersistentEvent 的集群，并单击组件所在行右侧的【更新配置】。如下图所示：
![](https://main.qcloudimg.com/raw/d8bd0a3193ae8b30be7222f4cec42b7a.png)
3. 在“更新事件持久化组件”页面，调整事件持久化存储端后单击【完成】即可完成更新。

### 在 CLS 控制台检索事件
1. 登录日志服务控制台，选择左侧导航栏中的【[日志集管理](https://console.cloud.tencent.com/cls/logset)】。
2. 在“日志集管理”页面上方，选择 PersistentEvent 所配置日志集所在地域。
3. 在日志集列表中单击 PersistentEvent 所配置日志集名称，进入该日志集详情页。如下图所示：
![](https://main.qcloudimg.com/raw/adb6166a495c78580a1a2eacf42353cf.png)
4. 单击 PersistentEvent 所配置的日志集主题所在行右侧的【管理】，进入“日志主题”详情页。
5. 选择【索引配置】页签，在页面中开启索引配置并单击【保存】，打开日志检索功能。如下图所示：
![](https://main.qcloudimg.com/raw/a804577fd5e6d638cd4921f2ce255579.png)
6. 选择左侧导航栏中的【[日志检索](https://console.cloud.tencent.com/cls/search)】，并在“日志集”和“日志主题”下拉框中选择 PersistentEvent 所配置的日志服务，以及期望检索日志的时间段，单击【查询分析】即可查看事件数据。如下图所示：
![](https://main.qcloudimg.com/raw/7b30875bb8f4e7bf057291d210dc0d0c.png)



