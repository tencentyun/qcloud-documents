## 简介

[Fluid](https://github.com/fluid-cloudnative/fluid) 是一个开源的 Kubernetes 原生分布式数据集编排和加速引擎，目前它由云原生计算基金会 [CNCF](https://www.cncf.io/sandbox-projects/) 作为 Sandbox 项目托管。主要服务于云原生场景下的数据密集型应用，例如大数据应用、AI 应用等。通过定义数据集资源的抽象，实现如下功能：

- **数据集抽象原生支持**：将数据密集型应用所需基础支撑能力功能化，实现数据高效访问并降低多维管理成本。
- **云上数据预热与加速**：Fluid 通过使用分布式缓存引擎（GooseFS/Alluxio）为云上应用提供数据预热与加速，同时可以保障缓存数据的可观测性、可迁移性和自动化的水平扩展。
- **数据应用协同编排**：在云上调度应用和数据时，同时考虑两者特性与位置，实现协同编排，提升性能。
- **多命名空间管理支持**：用户可以创建和管理不同 namespace 的数据集。
- **异构数据源管理**：一次性统一访问不同来源的底层数据（对象存储 COS，HDFS 和 Ceph 等存储)，适用于混合云场景。

## 重要概念

**Dataset**：数据集是逻辑上相关的一组数据的集合，会被运算引擎使用，例如大数据的 Spark，AI 场景的 TensorFlow。而这些数据智能的应用会创造工业界的核心价值。Dataset 的管理实际上也有多个维度，例如安全性，版本管理和数据加速。我们希望从数据加速出发，对于数据集的管理提供支持。

**Runtime**：实现数据集安全性，版本管理和数据加速等能力的执行引擎，定义了一系列生命周期的接口。可以通过实现这些接口，支持数据集的管理和加速。

**GooseFSRuntime**：来源于腾讯云 COS 团队 GooseFS，基于 Java 实现的支撑 Dataset 数据管理和缓存的执行引擎实现，支持对象存储 COS。GooseFS 为腾讯云产品，有专门的产品级支持，但是代码不开源。Fluid 通过管理和调度 GooseFS Runtime 实现数据集的可见性，弹性伸缩， 数据迁移。

**AlluxioRuntime**：来源于 Alluixo 社区，是支撑 Dataset 数据管理和缓存的执行引擎实现，支持 PVC，Ceph，CPFS 计算，有效支持混合云场景。但是 Alluxio 为开源社区方案，对于数据缓存的稳定性和性能优化，腾讯云会和社区一起推动，但是时效性和响应会有延时。Fluid 通过管理和调度 Alluxio Runtime 实现数据集的可见性，弹性伸缩， 数据迁移。

|    -          | Alluxio                       | GooseFS                                 |
| ------------ | ----------------------------- | --------------------------------------- |
| 底层存储类型 | PVC，Ceph，HDFS，CPFS，NFS... | OSS，EMR，PVC，Ceph，HDFS，CPFS，NFS... |
| 支持方式     | 开源社区                      | 腾讯云产品                              |

## 组件安装

### 前置依赖

- Kubernetes 集群（version >= 1.14）
- 集群支持 CSI 功能

### 参数配置

在通过 Helm 部署的过程中，所有的配置项都集中于 `values.yaml`。
以下是部分较为可能需要自定义的字段：

| 参数     | 描述     | 默认值     |
| ------- | -------- | --------- |
| `workdir` | 缓存引擎备份元数据地址 | `/tmp`
| `dataset.controller.image.repository` | Dataset Controller 镜像所在仓库  | `ccr.ccs.tencentyun.com/fluid/dataset-controller` |
| `dataset.controller.image.tag`        | Dataset Controller 镜像的版本    | `"v0.6.0-0bfc552"` |
| `csi.registrar.image.repository`   | CSI registrar 镜像所在仓库 | `"ccr.ccs.tencentyun.com/fluid/csi-node-driver-registrar"` |
| `csi.registrar.image.tag`   | CSI registrar 镜像的版本 | `"v1.2.0"` |
| `csi.plugins.image.repository`   | CSI plugins 镜像所在仓库 | `"ccr.ccs.tencentyun.com/fluid/fluid-csi"` |
| `csi.plugins.image.tag`   | CSI plugins 镜像的版本 | `"v0.6.0-def5316"` |
| `csi.kubelet.rootDir`   | kubelet root 文件夹 | `"/var/lib/kubelet"` |
| `runtime.mountRoot`   | 缓存引擎 fuse mount 点的 Root 地址 | `"/var/lib/kubelet"` |
| `runtime.goosefs.enable`   | 开启 GooseFS 缓存引擎支持 | `"true"` |
| `runtime.goosefs.init.image.repository`   | GooseFS 缓存引擎初始化镜像所在仓库 | `"ccr.ccs.tencentyun.com/fluid/init-users"` |
| `runtime.goosefs.init.image.tag`   | GooseFS 缓存引擎初始化镜像的版本 | `"v0.6.0-0cd802e"` |
| `runtime.goosefs.controller.image.repository`   | GooseFS 缓存引擎控制器镜像所在仓库 | `"ccr.ccs.tencentyun.com/fluid/goosefsruntime-controller"` |
| `runtime.goosefs.controller.image.tag`   | GooseFS 缓存引擎控制器镜像的版本 | `"v0.6.0-bbf4ea0"` |
| `runtime.goosefs.runtime.image.repository`   | GooseFS 缓存引擎镜像所在仓库 | `"ccr.ccs.tencentyun.com/fluid/goosefs"` |
| `runtime.goosefs.runtime.image.tag`   | GooseFS 缓存引擎镜像的版本 | `"v1.1.10"` |
| `runtime.goosefs.fuse.image.repository`   | GooseFS 缓存引擎 Fuse 组件镜像所在仓库 | `"ccr.ccs.tencentyun.com/fluid/goosefs-fuse"` |
| `runtime.goosefs.fuse.image.tag`   | GooseFS 缓存引擎 Fuse 组件镜像的版本 | `"v1.1.10"` |
| `runtime.alluxio.runtimeWorkers`   | Alluxio 缓存引擎控制器最大并发 worker 数量 | `"3"` |
| `runtime.alluxio.portRange`   | Alluxio 缓存引擎组件端口占用分配段 | `"20000-26000"` |
| `runtime.alluxio.enable`   | 开启 Alluxio 缓存引擎支持 | `"true"` |
| `runtime.alluxio.init.image.repository`   | Alluxio 缓存引擎初始化镜像所在仓库 | `"ccr.ccs.tencentyun.com/fluid/init-users"` |
| `runtime.alluxio.init.image.tag`   | Alluxio 缓存引擎初始化镜像的版本 | `"v0.6.0-def5316"` |
| `runtime.alluxio.controller.image.repository`   | Alluxio 缓存引擎控制器镜像所在仓库 | `"ccr.ccs.tencentyun.com/fluid/alluxioruntime-controller"` |
| `runtime.alluxio.controller.image.tag`   | Alluxio 缓存引擎控制器镜像的版本 | `"v0.6.0-0cd802e"` |
| `runtime.alluxio.runtime.image.repository`   | Alluxio 缓存引擎镜像所在仓库 | `"ccr.ccs.tencentyun.com/alluxio/alluxio"` |
| `runtime.alluxio.runtime.image.tag`   | Alluxio 缓存引擎镜像的版本 | `"release-2.5.0-2-SNAPSHOT-a05eadcff1"` |
| `runtime.alluxio.fuse.image.repository`   | Alluxio 缓存引擎 Fuse 组件镜像所在仓库 | `"ccr.ccs.tencentyun.com/alluxio/alluxio-fuse"` |
| `runtime.alluxio.fuse.image.tag`   | Alluxio 缓存引擎 Fuse 组件镜像的版本 | `"release-2.5.0-2-SNAPSHOT-a05eadcff1"` |

## 最佳实践

请参见 Alluxio [使用文档](https://github.com/fluid-cloudnative/fluid/blob/master/docs/zh/TOC.md)。
