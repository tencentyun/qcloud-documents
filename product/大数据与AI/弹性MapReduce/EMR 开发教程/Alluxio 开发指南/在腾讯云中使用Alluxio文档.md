## 概述
在腾讯云 EMR 上提供了开箱可用的 Alluxio 服务，以帮助腾讯云客户可以快速实现分布式内存级缓存加速、简化数据管理等。同时还可以通过腾讯云 EMR 控制台或 API 接口，使用配置下发功能，快速配置多层级缓存和元数据管理等，获取一站式监控告警等功能。

## 准备
- 腾讯云 EMR 的 Hadoop 标准版本2.1.0版本及以上
- 腾讯云 EMR 的 Hadoop 天穹版本1.0版本及以上

有关 EMR 中版本中支持具体的 Alluxio 的版本支持可参考 [组件版本](https://cloud.tencent.com/document/product/589/20279)。

## 创建基于 Alluxio 的 EMR 集群
本节主要说明如何在腾讯云 EMR 上创建开箱即用的 Alluxio 集群。EMR 创建集群提供了购买页创建和 API 创建两种方式。

### 购买页创建集群
您需要登录腾讯云 EMR [购买页](https://buy.cloud.tencent.com/emapreduce/)，在购买页选择支持的 Alluxio 发布版本，并且在可选组件列表中勾选 Alluxio 组件。
![](https://main.qcloudimg.com/raw/32d5f013d14def8a396951cd751e1352.png)
其他的选项可根据业务具体业务场景，进行个性化配置，创建过程中的具体选项可参考 [创建 EMR 集群](https://cloud.tencent.com/document/product/589/10981)。

### API 创建集群
腾讯云 EMR 还提供了 API 方式构建基于 Alluxio 的大数据集群。具体可参考 [查询硬件节点信息](https://cloud.tencent.com/document/product/589/41707)。

## 基础配置
创建一个带 Alluxio 组件的腾讯云 EMR 集群，默认会把 HDFS 挂载到 Alluxio 上，并使用内存作为单层 level0 存储。如果有需要更改更符合业务特性的多级存储，或者其他对应优化项，可以使用配置下发功能来完成相关配置。
![](https://main.qcloudimg.com/raw/268372154def37a8ddd15c4befbeb7f0.png)
在配置下发后，部分配置需要重启 Alluxio 服务才能生效。
![](https://main.qcloudimg.com/raw/f1ac6f77833348998871f2eadbab489e.png)
更多配置下发和重启策略细节，可参考 [配置下发](https://cloud.tencent.com/document/product/589/14628) 和 [重启组件](https://cloud.tencent.com/document/product/589/32823)。

### 基于 Alluxio 加速计算存储分离
腾讯云 EMR 基于腾讯云对象存储（COS）提供了计算存储分离能力，默认直接访问对象存储中的数据时，应用程序没有节点级数据本地性或跨应用程序缓存。使用 Alluxio 加速将缓解这些问题。

在腾讯云 EMR 集群上默认已部署使用 COS 作为 UFS 的依赖 jar 包，只需授予访问 COS 的权限，并把 COS mount 到 Alluxio 上即可使用。

### 授权
若当前集群未开启对象存储，可在【[访问管理控制台-角色](https://console.cloud.tencent.com/cam/role)】中进行授权，授权后 EMR 中节点可以通过临时密钥访问 COS 中数据。
![](https://main.qcloudimg.com/raw/12fa4b6008bdfaa3643517cc7de0eac1.png)

### Mount
登录到 EMR 任意一台机器，挂载 COS 到 Alluxio。
```
bin/alluxio fs mount <alluxio-path> <source-path>
//TODO,
```
更多在腾讯云 EMR 中使用 Alluxio 开发细节，可查阅 [Alluxio 开发文档](https://cloud.tencent.com/document/product/589/35281)。
