## 简介

### 组件介绍

Helm 是管理 Kubernetes 应用程序的打包工具，详情请参见 [Helm 官网文档](https://helm.sh/)。TKE 集成 Helm 相关功能，提供了 Helm Chart 在指定集群内图形化的增删改查功能。

### 部署在集群内的 Kubernetes 对象

在集群内部署 Helm Add-on，将在集群内部署以下 Kubernetes 对象：

| Kubernetes 对象名称 | 类型         | 默认占用资源           | 所属 Namespaces |
| -------------- | ---------- | ---------------- | ------------ |
| swift          | deployment | 0.03核 CPU，20MiB内存 | kube-system  |
| tiller-deploy  | deployment | 0.15核 CPU，80MiB内存 | kube-system  |


## 限制条件
- 支持 1.8 版本以上的 Kubernetes 集群。
- 将占用集群0.28核 CPU 以及180MiB内存的资源。

## 使用方法
 详情请参见 [Helm 应用管理](https://cloud.tencent.com/document/product/457/32730)。


