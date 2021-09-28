## 简介


<dx-alert infotype="alarm" title="">
该组件目前已不再维护，若需要使用事件存储能力，请参考 [事件存储](https://cloud.tencent.com/document/product/457/32091) 文档。日志服务 CLS 新版事件存储提供免费服务，并预置可视化 [事件仪表盘](https://cloud.tencent.com/document/product/457/50512)。
</dx-alert>




### 组件介绍

Kubernetes Events 包括了 Kubernetes 集群的运行和各类资源的调度情况，对维护人员日常观察资源的变更以及定位问题均有帮助。TKE 支持为您的所有集群配置事件持久化功能，开启本功能后，会将您的集群事件实时导出到配置的存储端。TKE 还支持使用腾讯云提供的 PAAS 服务或开源软件对事件流水进行检索。


### 部署在集群内的 Kubernetes 对象


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
1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)，选择左侧导航栏中的**集群**。
2. 在“集群管理”页面上方选择目标集群所在地域下的集群 ID，进入集群详情页。
3. 选择左侧菜单栏中的**组件管理**，进入“组件列表”页面。
4. 在“组件列表”页面中选择**新建**，并在“新建组件”页面中勾选 PersistentEvent，并配置事件持久化存储端，单击**完成**即可安装成功。
主要参数信息如下：
 - **存储端选择**：您可以选择将事件存储到 **[Elasticsearch](https://cloud.tencent.com/document/product/845/16478)**或 **[日志服务 CLS](https://cloud.tencent.com/document/product/614/11254)**。
 - **参数详情**：
	 - 事件存储至**Elasticsearch**需要提供 Elasticsearch 地址和索引。
	 - 事件存储至**日志服务CLS**需要提供日志服务实例，若当前无合适的实例，您可以 [新建日志主题](https://console.cloud.tencent.com/cls/topic?region=ap-guangzhou)。



### 在日志服务控制台检索事件
登录日志服务控制台，选择左侧导航栏中的 **[检索分析](https://console.cloud.tencent.com/cls/search)**，并在“日志集”和“日志主题”下拉框中选择 PersistentEvent 所配置的日志服务，以及期望检索日志的时间段，单击**查询分析**即可查看事件数据。如下图所示：
![](https://main.qcloudimg.com/raw/7b30875bb8f4e7bf057291d210dc0d0c.png)



>!日志主题需要开启全文索引，才可检索日志。

