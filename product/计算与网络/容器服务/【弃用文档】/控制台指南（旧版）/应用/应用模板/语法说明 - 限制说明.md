出于功能稳定闭环的考虑，容器平台对 kubernetes 的编排语法做了一定的限制。本文档将介绍这些限制的内容和原因。

## yaml 字节数配额限制

应用编排 yaml 字节数配额限制51200。

## 支持的资源类型限制

Kubernetes 包含多种不同资源类型。容器服务根据用户的需求，在 UI 界面上暂时只开放了`Deployment`和`Service`这两种最常用资源。（在创建`Deployment`会自动创建`Pod`资源和`replicaset`）。

所有在容器服务的应用编排中，暂时只支持`Deployment`和`Service`这两种资源。

## 资源名称限制

应用模板的每个服务内，`Deployment`和`Service`资源名称必须和服务名称保持一致。

## 命名空间限制

1. 应用模板中所有资源必须在一个命名空间内。

2. `kube-system`命名空间暂时不支持创建服务，所以在应用模板中暂时不支持命名空间为`kube-system`。

## Label 标签限制
1. 在应用模板中，可以使用 Label 标签对服务中的资源进行标记。在容器服务中，`Service`通过 `Select Label`标签去寻找对应的`Pod`，从而实现与`Deployment`的关联。`Deployment`关联`Pod`使用的是`Deployment`自身的`Select Label`。所以为了实现`Deployment`和`Service`的管理，增加了`Deployment`和`Service`的`Select Label`必须一致的限制。

2. 在应用模板中默认为每一个服务提供`qcloud-app`进行标识，提供`qcloud-application-label`标签标记属于哪个应用。这两个标签暂时不支持修改。

## Cbs 盘使用限制

1. 由于 cbs 只能同时被一个容器实例挂载，所有在使用了 cbs 盘的服务，实例数最大为1。

2. 使用了 cbs 盘的服务，更新操作只能使用重新创建更新，暂时不支持滚动更新。












