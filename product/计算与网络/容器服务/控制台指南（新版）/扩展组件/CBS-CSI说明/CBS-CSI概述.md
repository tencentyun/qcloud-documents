## 操作场景

[CBS-CSI 组件](https://github.com/TencentCloud/kubernetes-csi-tencentcloud/blob/master/docs/README_CBS.md) 支持 TKE 集群通过控制台快捷选择存储类型，并创建对应块存储云硬盘类型的 PV 和 PVC。本文提供 CBS-CSI 组件功能特性等说明并介绍几种常见示例用法。


## 功能特性

| 功能                          | 说明                                                         |
| ----------------------------- | ------------------------------------------------------------ |
| 静态数据卷                    | 支持手动创建 Volume、PV 对象及 PVC 对象                      |
| 动态数据卷                    | 支持通过 StorageClass 配置、创建和删除 Volume 及 PV 对象     |
| 存储拓扑感知                  | 云硬盘不支持跨可用区挂载，在多可用区集群中，CBS-CSI 组件将先调度 Pod，后调度 Node 的 zone 创建 Volume |
| 调度器感知节点 maxAttachLimit | 腾讯云单个云服务器上默认最多挂载20块云硬盘，调度器调度 Pod 时将过滤超过最大可挂载云硬盘数量的节点 |
| 卷在线扩容                    | 支持通过修改 PVC 容量字段，实现在线扩容（仅支持云硬盘类型）  |
| 卷快照和恢复                  | 支持通过快照创建数据卷                                       |


## 组件说明

CBS-CSI 组件在集群内部署后，包含以下组件：

- DaemonSet：每个 Node 提供一个 DaemonSet，简称为 NodePlugin。由 CBS-CSI Driver 和 node-driver-registrar 两个容器组成，负责向节点注册 Driver，并提供挂载能力。
- StatefulSet 和 Deployment：简称为 Controller。由 Driver 和多个 Sidecar（external-provisioner、external-attacher、external-resizer、external-snapshotter、snapshot-controller）一起构成，提供创删卷、attach、detach、扩容、快照等能力。

![](https://main.qcloudimg.com/raw/f469674c69e02fc912b65d0babc001bd.png)



## 限制条件

- TKE 集群版本 ≥ 1.14
- 使用 CBS-CSI 组件后，才可在 TKE 集群中为云硬盘在线扩容和创建快照。
- 已经使用 QcloudCbs（In-Tree 插件）的 TKE 集群，可以继续正常使用。（后续将通过 Volume Migration 统一到 CBS CSI）



## 使用示例

- [通过 CBS-CSI 避免云硬盘跨可用区挂载](https://cloud.tencent.com/document/product/457/67078)
- [在线扩容云硬盘](https://cloud.tencent.com/document/product/457/67079)
- [创建快照和使用快照来恢复卷](https://cloud.tencent.com/document/product/457/67080)

