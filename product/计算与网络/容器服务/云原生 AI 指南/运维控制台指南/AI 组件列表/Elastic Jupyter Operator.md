## 简介

[elastic-jupyter-operator](https://github.com/tkestack/elastic-jupyter-operator) 是 Kubernetes 原生的弹性 Jupyter 服务。为用户按需提供弹性的 Jupyter Notebook 服务。elastic-jupyter-operator 提供以下特性：

- GPU 空闲时自动释放资源到 Kubernetes 集群。
- 资源延迟申请，在使用时按需申请对应 CPU/内存/GPU 资源。
- 多 Jupyter 共享资源池，提高资源利用率。


## 部署

在通过 Helm 部署过程中，所有的配置项都集中于 `values.yaml`。

以下是部分较为可能需要自定义的字段：

| 参数               | 描述         | 默认值                                                       |
| ------------------ | ------------ | ------------------------------------------------------------ |
| `image.repository` | 镜像所在仓库 | `ccr.ccs.tencentyun.com/kubeflow-oteam/elastic-jupyter-operator` |
| `image.tag`        | 镜像的版本   | `"v0.1.1"`                                                   |
| `namespace.name`   | 命名空间     | `"enterprise-gateway"`                                       |

## 使用

>?更多详细说明，请参见 [使用文档](https://github.com/tkestack/elastic-jupyter-operator/blob/master/README.md)。

1. 执行以下命令，创建一个 Jupyter Gateway CR：
```bash
kubectl apply -f ./config/samples/kubeflow.tkestack.io_v1alpha1_jupytergateway.yaml
```
YAML 文件内容如下：
```yaml
apiVersion: kubeflow.tkestack.io/v1alpha1
kind: JupyterGateway
metadata:
  name: jupytergateway-sample
spec:
  cullIdleTimeout: 3600
```
其中 `cullIdleTimeout` 是一个配置项，在 Kernel 空闲指定 `cullIdleTimeout` 秒内，会由 Gateway 回收对应 Kernel 以释放资源。
2. 执行以下命令，创建一个 Jupyter Notebook CR 实例，并且指定对应的 Gateway CR：
```bash
kubectl apply -f ./config/samples/kubeflow.tkestack.io_v1alpha1_jupyternotebook.yaml
```
YAML 文件内容如下：
```yaml
apiVersion: kubeflow.tkestack.io/v1alpha1
kind: JupyterNotebook
metadata:
  name: jupyternotebook-sample
spec:
  gateway:
    name: jupytergateway-sample
    namespace: default
```
3. 集群上所有资源如下所示：
```shell
NAME                                          READY   STATUS    RESTARTS   AGE
pod/jupytergateway-sample-6d5d97949c-p8bj6    1/1     Running   2          11d
pod/jupyternotebook-sample-5bf7d9d9fb-nq9b8   1/1     Running   2          11d

NAME                            TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/jupytergateway-sample   ClusterIP   10.96.138.111   <none>        8888/TCP   11d
service/kubernetes              ClusterIP   10.96.0.1       <none>        443/TCP    31d

NAME                                     READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/jupytergateway-sample    1/1     1            1           11d
deployment.apps/jupyternotebook-sample   1/1     1            1           11d

NAME                                                DESIRED   CURRENT   READY   AGE
replicaset.apps/jupytergateway-sample-6d5d97949c    1         1         1       11d
replicaset.apps/jupyternotebook-sample-5bf7d9d9fb   1         1         1       11d
```
4. 通过 NodePort、`kubectl port-forward`、ingress 等方式将 Notebook CR 对外暴露提供服务，这里以 `kubectl port-forward` 为例，执行命令如下：
```shell
kubectl port-forward jupyternotebook-sample-5bf7d9d9fb-nq9b8 8888
```

## API 文档

请参见 [API 文档](https://github.com/tkestack/elastic-jupyter-operator/blob/master/docs/api/generated.asciidoc)。
