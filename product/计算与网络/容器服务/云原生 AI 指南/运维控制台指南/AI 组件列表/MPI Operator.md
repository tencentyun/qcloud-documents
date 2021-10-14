## 简介

[MPI-Operator](https://github.com/kubeflow/mpi-operator) 是 [Kubeflow](https://www.kubeflow.org) 社区开发，用于支持以 [Horovod](https://horovod.ai) 为代表的数据并行分布式训练在 Kubernetes 集群上部署运行的组件。

在部署完成之后，用户可以创建、查看、删除 [MPIJob](https://github.com/kubeflow/mpi-operator/blob/master/pkg/apis/kubeflow/v1/types.go)。


## 前置依赖

Kubernetes 集群（version >= 1.16）

## 部署

在通过 Helm 部署的过程中，所有的配置项都集中于 `values.yaml`。

以下是部分较为可能需要自定义的字段：

| 参数               | 描述                                   | 默认值                                               |
| ------------------ | -------------------------------------- | ---------------------------------------------------- |
| `image.repository` | MPI-Operator 镜像所在仓库              | `ccr.ccs.tencentyun.com/kubeflow-oteam/mpi-operator` |
| `image.tag`        | MPI-Operator 镜像的版本                | `"latest"`                                           |
| `namespace.create` | 是否为 MPI-Operator 创建独立的命名空间 | `true`                                               |
| `namespace.name`   | 部署 MPI-Operator 的命名空间           | `"mpi-operator"`                                     |

## 最佳实践

请参见 [运行弹性训练任务](https://cloud.tencent.com/document/product/457/62638)。
