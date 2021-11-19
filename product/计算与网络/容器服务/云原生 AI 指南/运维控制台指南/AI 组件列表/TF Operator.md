## 简介

[TF-Operator](https://github.com/kubeflow/tf-operator) 是 [Kubeflow](https://www.kubeflow.org) 社区开发，用以支持在 Kubernetes 上部署执行 [TensorFlow](https://www.tensorflow.org) 分布式训练任务的组件。

在部署完成之后，用户可以创建、查看、删除 [TFJob](https://www.kubeflow.org/docs/components/training/tftraining/)。

## 前置依赖

 Kubernetes 集群（version >= 1.16）

## 部署

在通过 Helm 部署的过程中，所有的配置项都集中于 `values.yaml`。

以下是部分较为可能需要自定义的字段：

| 参数               | 描述                                  | 默认值                                              |
| ------------------ | ------------------------------------- | --------------------------------------------------- |
| `image.repository` | TF-Operator 镜像所在仓库              | `ccr.ccs.tencentyun.com/kubeflow-oteam/tf-operator` |
| `image.tag`        | TF-Operator 镜像的版本                | `"latest"`                                          |
| `namespace.create` | 是否为 TF-Operator 创建独立的命名空间 | `true`                                              |
| `namespace.name`   | 部署 TF-Operator 的命名空间           | `"tf-operator"`                                     |

## 最佳实践

请参见 [运行 TF 训练任务](https://cloud.tencent.com/document/product/457/62636)。
