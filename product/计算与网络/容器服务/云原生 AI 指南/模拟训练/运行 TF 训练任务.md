本文为您介绍如何运行 TF 训练任务。


## 前提条件

- AI 环境中已安装 [TF Operator](https://cloud.tencent.com/document/product/457/62632)。
- AI 环境中有 GPU 资源。

## 操作步骤

以下操作指南参考 `TF-Operator` 官方提供的 PS/Worker 模式的 [分布式训练案例](https://github.com/kubeflow/training-operator/tree/master/examples/tensorflow/dist-mnist)。

### 准备训练代码

本示例中使用 Kubeflow 官方提供的示例代码 [dist_mnist.py](https://raw.githubusercontent.com/kubeflow/training-operator/master/examples/tensorflow/dist-mnist/dist_mnist.py)。

### 制作训练镜像

镜像的制作过程较简单，只需基于一个 TensorFlow 1.5.0 的官方镜像，并将代码复制到镜像内，并配置好 `entrypoint` 即可。

> ? 如果不配置 entrypoint，也可以在提交 TFJob 时配置容器的启动命令。


### 任务提交

1. 准备一个 TFJob 的 [YAML 文件](https://raw.githubusercontent.com/kubeflow/training-operator/master/examples/tensorflow/dist-mnist/tf_job_mnist.yaml)，定义2个 PS 和4个 Worker。
<dx-alert infotype="notice" title="">
用户需要用上传后的训练镜像地址替换 `<训练镜像>` 所在占位。
</dx-alert>
```yaml
apiVersion: "kubeflow.org/v1"
kind: "TFJob"
metadata:
  name: "dist-mnist-for-e2e-test"
spec:
  tfReplicaSpecs:
    PS:
      replicas: 2
      restartPolicy: Never
      template:
        spec:
          containers:
            - name: tensorflow
              image: <训练镜像>
    Worker:
      replicas: 4
      restartPolicy: Never
      template:
        spec:
          containers:
            - name: tensorflow
              image: <训练镜像>
```
2. 执行以下命令，通过 `kubectl` 提交该 TFJob：
```shell
kubectl create -f ./tf_job_mnist.yaml
```
3. 执行以下命令，查看任务状态：
```shell
kubectl get tfjob dist-mnist-for-e2e-test -o yaml
kubectl get pods -l pytorch_job_name=pytorch-tcp-dist-mnist 
```

