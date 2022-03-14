本文为您介绍如何运行 PyTorch 训练任务。


## 前提条件

- AI 环境中已安装 [PyTorch Operator](https://cloud.tencent.com/document/product/457/62633)。
- AI 环境中有 GPU 资源。

## 操作步骤

以下操作指南参考 `PyTorch-Operator` 官方提供的分布式训练 [案例](https://github.com/kubeflow/pytorch-operator/tree/master/examples/mnist)。

### 准备训练代码

本示例使用 Kubeflow 官方提供的示例代码 [mnist.py](https://raw.githubusercontent.com/kubeflow/pytorch-operator/master/examples/mnist/mnist.py)。

### 制作训练镜像

训练镜像的制作过程较简单，只需基于一个 PyTorch 1.0 的官方镜像，将代码复制到镜像内，并配置好 `entrypoint` 即可。（如果不配置 entrypoint，用户也可以在提交 PyTorchJob 时配置启动命令。）

> ! 训练代码基于 PyTorch 1.0 构建，由于 PyTorch 在版本间可能存在 API 不兼容的问题，上述训练代码在其他版本的 PyTorch 环境下可能需要自行调整代码。

### 任务提交

1. 准备一个 PyTorchJob 的 [YAML 文件](https://raw.githubusercontent.com/kubeflow/pytorch-operator/master/examples/mnist/v1/pytorch_job_mnist_nccl.yaml)，定义1个 Master Worker 和1个 Worker。
<dx-alert infotype="notice" title="">
- 用户需要用上传后的训练镜像地址替换  `<训练镜像>` 所在占位。
- 由于在资源配置中设置了 GPU 资源，在 `args` 为训练配置的 `backend` 为 `"nccl"`；在未使用 （Nvidia）GPU 的任务中，请使用其他（例如 gloo）backend。
</dx-alert>
```yaml
apiVersion: "kubeflow.org/v1"
kind: "PyTorchJob"
metadata:
  name: "pytorch-dist-mnist-nccl"
spec:
  pytorchReplicaSpecs:
    Master:
      replicas: 1
      restartPolicy: OnFailure
      template:
        metadata:
          annotations:
            sidecar.istio.io/inject: "false"
        spec:
          containers:
            - name: pytorch
              image: <训练镜像>
              args: ["--backend", "nccl"]
              resources: 
                limits:
                  nvidia.com/gpu: 1
    Worker:
      replicas: 1
      restartPolicy: OnFailure
      template:
        metadata:
          annotations:
            sidecar.istio.io/inject: "false"
        spec:
          containers: 
            - name: pytorch
              image: <训练镜像>
              args: ["--backend", "nccl"]
              resources: 
                limits:
                  nvidia.com/gpu: 1
```
2. 执行以下命令，通过 `kubectl` 提交该 PyTorch Job：
```shell
kubectl create -f ./pytorch_job_mnist_nccl.yaml
```
3. 执行以下命令，查看该 PyTorch Job：
```shell
kubectl get -o yaml pytorchjobs pytorch-dist-mnist-nccl
```
4. 执行以下命令，查看 PyTorch 任务创建的相关 Pod：
```shell
kubectl get pods -l pytorch_job_name=pytorch-dist-mnist-nccl  
```

