
## 简介

### 组件介绍

OLM（Operator Lifecycle Manager）作为 Operator Framework 的一部分，可以帮助用户进行 Operator 的自动安装，升级及生命周期的管理。同时 OLM 自身以 Operator 的形式进行安装部署，其工作方式是以 Operators 来管理 Operators，且面向 Operator 提供的声明式（declarative）自动化管理能力完全符合 Kubernetes 交互的设计理念。

### 组件原理

OLM 由两个 Operator 构成：OLM Operator 和 Catalog Operator，其分别管理以下几个基础 CRD 模型：

| 资名称                | 简称   | 所属 Operator | 描述                                                         |
| --------------------- | ------ | ------------- | ------------------------------------------------------------ |
| ClusterServiceVersion | csv    | OLM           | 业务应用元数据，包括应用名称、版本、图标、依赖资源、安装方式等。 |
| InstallPlan           | ip     | Catalog       | 计算自动安装或升级 CSV 过程中需要创建的资源集。              |
| CatalogSource         | catsrc | Catalog       | 用于定义应用的 CSVs、CRDs、安装包的仓库。                    |
| Subscription          | sub    | Catalog       | 通过跟踪安装包中的 channel 保证 CSVs 的版本更新。            |
| OperatorGroup         | og     | OLM           | 用于 Operators 安装过程中的多租户配置，可以定义一组目标 namespaces 指定创建Operators 所需的 RBAC 等资源配置。 |

- 在 Operator 安装管理生命周期中的 Deployment、Serviceaccount、RBAC 相关的角色和角色绑定通过 OLM operator 创建。Catalog Operator 负责 CRDs 和 CSVs 等资源的创建。
- OLM Operator 的工作基于 ClusterServiceVersion，一旦 CSV 中声明的依赖资源在目标集群中注册成功，OLM Operator 将负责安装这些资源对应的应用实例。
- Catalog Operator 主要负责解析 CSV 中声明的依赖资源定义，同时通过监听 catalog 中安装包对应 channels 的版本定义完成 CSV 对应的版本更新。


### 部署在集群内的 Kubernetes 对象

| Kubernetes 对象名称                             | 类型                     | 请求资源                                  | 所属 Namespace             |
| ----------------------------------------------- | ------------------------ | ----------------------------------------- | -------------------------- |
| catalogsources.operators.coreos.com             | CustomResourceDefinition | -                                         | -                          |
| clusterserviceversions.operators.coreos.com     | CustomResourceDefinition | -                                         | -                          |
| installplans.operators.coreos.com               | CustomResourceDefinition | -                                         | -                          |
| operatorgroups.operators.coreos.com             | CustomResourceDefinition | -                                         | -                          |
| operators.operators.coreos.com                  | CustomResourceDefinition | -                                         | -                          |
| subscriptions.operators.coreos.com              | CustomResourceDefinition | -                                         | -                          |
| olm-operator                                    | Deployment               | cpu request: 10m<br>memory request: 160Mi | operator-lifecycle-manager |
| catalog-operator                                | Deployment               | cpu request: 10m<br>memory request: 80Mi  | operator-lifecycle-manager |
| system:controller:operator-lifecycle-manager    | ClusterRole              | -                                         | -                          |
| aggregate-olm-view                              | ClusterRole              | -                                         | -                          |
| aggregate-olm-edit                              | ClusterRole              | -                                         | -                          |
| olm-operator-binding-operator-lifecycle-manager | ClusterRoleBinding       | -                                         | -                          |
| olm-operator                                    | ServiceAccount           | -                                         | operator-lifecycle-manager |
| operators                                       | Namespace                | -                                         | -                          |
| operator-lifecycle-manager                      | Namespace                | -                                         | -                          |
| packageserver                                   | ClusterServiceVersion    | -                                         | operator-lifecycle-manager |
| olm-operators                                   | OperatorGroup            | -                                         | operator-lifecycle-manager |
| global-operators                                | OperatorGroup            | -                                         | operators                  |

## 使用场景

OLM 可以帮助用户安装、更新和管理所有 Operator 的生命周期。

## 风险控制

OLM 组件卸载后，为了保证用户的业务不会被影响，通过 OLM 部署的 Operator 不会被清理，并且该组件相关的 CRD 资源也不会被清理，此类 CRD 资源可以通过手动方式进行删除。

## 限制条件
<dx-alert infotype="explain" title="">
您在创建集群时选择1.12.4以上版本集群，无需修改任何参数，开箱可用。
</dx-alert>

- 仅支持1.12版本以上的 kubernetes。
- 需设置 kube-apiserver 的启动参数：`--feature-gates=CustomResourceSubresources=true`



## 操作步骤


1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)，在左侧导航栏中选择**集群**。
2. 在“集群管理”页面单击目标集群 ID，进入集群详情页。
3. 选择左侧菜单栏中的**组件管理**，进入 “组件列表” 页面。
4. 在“组件列表”页面中选择**新建**，并在“新建组件”页面中勾选 OLM。
5. 单击**完成**即可创建组件。
