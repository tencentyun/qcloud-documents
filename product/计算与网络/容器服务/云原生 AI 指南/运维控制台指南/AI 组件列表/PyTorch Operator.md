## 简介

[PyTorch-Operator](https://github.com/kubeflow/pytorch-operator) 是 [Kubeflow](https://www.kubeflow.org) 社区开发，用于支持在 Kubernetes 上执行 [PyTorch](https://pytorch.org) DDP（[distributed data parallel](https://pytorch.org/tutorials/intermediate/ddp_tutorial.html)）模式分布式训练任务的组件。

在部署完成之后，用户可以创建、查看、删除 [PyTorchJob](https://www.kubeflow.org/docs/reference/pytorchjob/v1/pytorch/)。

## 前置依赖

 Kubernetes 集群（version >= 1.16）

## 部署

在通过 Helm 部署的过程中，所有的配置项都集中于 `values.yaml`。

以下是部分较为可能需要自定义的字段：

| 参数               | 描述                                       | 默认值                                                   |
| ------------------ | ------------------------------------------ | -------------------------------------------------------- |
| `image.repository` | PyTorch-Operator 镜像所在仓库              | `ccr.ccs.tencentyun.com/kubeflow-oteam/pytorch-operator` |
| `image.tag`        | PyTorch-Operator 镜像的版本                | `"latest"`                                               |
| `namespace.create` | 是否为 PyTorch-Operator 创建独立的命名空间 | `true`                                                   |
| `namespace.name`   | 部署 PyTorch-Operator 的命名空间           | `"pytorch-operator"`                                     |

## 最佳实践

请参见 [运行 Pytorch 训练任务](https://cloud.tencent.com/document/product/457/62637)。

