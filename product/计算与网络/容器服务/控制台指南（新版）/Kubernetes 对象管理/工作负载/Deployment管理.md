## 简介

Deployment 声明了 Pod 的模板和控制 Pod 的运行策略，适用于部署无状态的应用程序。您可以根据业务需求，对 Deployment 中运行的 Pod 的副本数、调度策略、更新策略等进行声明。

## Deployment 控制台操作指引

[](id:creatDeployment)
### 创建 Deployment
1. 登录容器服务控制台，选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2/cluster)**。
2. 单击需要创建 Deployment 的集群 ID，进入待创建 Deployment 的集群管理页面。如下图所示：
![](https://main.qcloudimg.com/raw/869f07b2d3f54c9b6abbb389b2da8690.png)
3. 单击**新建**，进入 “新建Workload” 页面。
根据实际需求，设置 Deployment 参数。关键参数信息如下：
 - **工作负载名**：输入自定义名称。
 - **标签**：一个键 - 值对（Key-Value），用于对资源进行分类管理。
 - **命名空间**：根据实际需求进行选择。
 - **类型**：选择**Deployment（可扩展的部署 Pod）**。
 - **数据卷（选填）**：为容器提供存储，目前支持临时路径、主机路径、云硬盘数据卷、文件存储 NFS、配置文件、PVC，还需挂载到容器的指定路径中。
 - **实例内容器**：根据实际需求，为 Deployment 的一个 Pod 设置一个或多个不同的容器。
    - **名称**：自定义。
    - **镜像**：根据实际需求进行选择。
    - **镜像版本（Tag）**：根据实际需求进行填写。
    - **镜像拉取策略**：提供以下3种策略，请按需选择。
       若不设置镜像拉取策略，当镜像版本为空或 `latest` 时，使用 Always 策略，否则使用 IfNotPresent 策略。
         - **Always**：总是从远程拉取该镜像。
         - **IfNotPresent**：默认使用本地镜像，若本地无该镜像则远程拉取该镜像。
         - **Never**：只使用本地镜像，若本地没有该镜像将报异常。
    - **CPU/内存限制**：可根据 [Kubernetes 资源限制](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/) 进行设置 CPU 和内存的限制范围，提高业务的健壮性。
    - **GPU 资源**：配置该工作负载使用的最少 GPU 资源。
    - **高级设置**：可设置 “**工作目录**”、“**运行命令**”、“**运行参数**”、“**容器健康检查**”和“**特权级**”等参数。
 - **镜像访问凭证**：容器镜像默认私有，在创建工作负载时，需选择实例对应的镜像访问凭证。
 - **实例数量**：根据实际需求选择调节方式，设置实例数量。
     - **手动调节**：设定实例数量，可单击“+”或“-”控制实例数量。
     - **自动调节**：满足任一设定条件，则自动调节实例（pod）数目。详情请参见 [自动伸缩](https://cloud.tencent.com/document/product/457/14209)。  
4. 单击**创建Workload**，完成创建。如下图所示：
当运行数量=期望数量时，即表示 Deployment 下的所有 Pod 已创建完成。
![](https://main.qcloudimg.com/raw/1ea9f4fe6d49a1651f5d0f0d9594d709.png)

### 更新 Deployment

#### 更新 YAML
1. 登录容器服务控制台，选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2/cluster)**。
2. 单击需要更新 Deployment 的集群 ID，进入待更新 Deployment 的集群管理页面。如下图所示：
![](https://main.qcloudimg.com/raw/91af8781e51bc79ba7f8ab011edc22c9.png)
3. 在需要更新 YAML 的 Deployment 行中，单击**更多** > **编辑YAML**，进入更新 Deployment 页面。
5. 在 “更新Deployment” 页面，编辑 YAML，单击**完成**，即可更新 YAML。如下图所示：
![更新YAML](https://main.qcloudimg.com/raw/ddc23ea3fc49bdb05e35c59b67a577ac.png)

#### 更新 Pod 配置

1. 在集群管理页面，单击需要更新 Pod 配置的 Deployment 的集群 ID，进入待更新 Pod 配置的 Deployment 的集群管理页面。
2. 在需要更新 Pod 配置的 Deployment 行中，单击**更新Pod配置**。如下图所示：
![](https://main.qcloudimg.com/raw/d5f72a2bd47684b7729c40c94121c199.png)
3. 在 “更新Pod配置” 页面，根据实际需求修改更新方式，设置参数。如下图所示：
![](https://main.qcloudimg.com/raw/c9ba21f10f36bf6bb8c55cd787fb632a.png)
4. 单击**完成**，即可更新 Pod 配置。

### 回滚 Deployment
1. 登录容器服务控制台，选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2/cluster)**。
2. 单击需要回滚 Deployment 的集群 ID，进入待回滚 Deployment 的集群管理页面。如下图所示：
![](https://main.qcloudimg.com/raw/91af8781e51bc79ba7f8ab011edc22c9.png)
4. 单击需要回滚的 Deployment 名称，进入 Deployment 信息页面。
5. 选择**修订历史**页签，在需要回滚的版本行中，单击**回滚**。如下图所示：
![](https://main.qcloudimg.com/raw/205acd0beec1c55638d0c4aee2bf195a.png)
6. 在弹出的 “回滚资源” 提示框中，单击**确定**即可完成回滚。

### 调整 Pod 数量
1. 登录容器服务控制台，选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2/cluster)**。
2. 单击需要调整 Pod 数量的 Deployment 的集群 ID，进入待调整 Pod 数量的 Deployment 的集群管理页面。如下图所示：
![](https://main.qcloudimg.com/raw/91af8781e51bc79ba7f8ab011edc22c9.png)
4. 在需要调整 Pod 数量的 Deployment 行中，单击**更新Pod数量**，进入更新 Pod 数量页面。如下图所示：
![](https://main.qcloudimg.com/raw/9d2aec78fe094ef5ea6230e7507b23af.png)
5. 根据实际需求调整 Pod 数量，单击**更新实例数目**即可完成调整。

## Kubectl 操作 Deployment 指引

### YAML 示例[](id:YAMLSample)
```Yaml
apiVersion: apps/v1beta2
kind: Deployment
metadata:
  name: nginx-deployment
  namespace: default
  labels:
    app: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx-deployment
  template:
    metadata:
      labels:
        app: nginx-deployment
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
```
- **kind**：标识 Deployment 资源类型。
- **metadata**：Deployment 的名称、Namespace、Label 等基本信息。
- **metadata.annotations**：对 Deployment 的额外说明，可通过该参数设置腾讯云 TKE 的额外增强能力。
- **spec.replicas**：Deployment 管理的 Pod 数量。
- **spec.selector**：Deployment 管理 Seletor 选中的 Pod 的 Label。
- **spec.template**：Deployment 管理的 Pod 的详细模板配置。

更多参数详情可查看 [Kubernetes Deployment 官方文档](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)。

### Kubectl 创建 Deployment

1. 参考 [YAML 示例](#YAMLSample)，准备 Deployment YAML 文件。
2. 安装 Kubectl，并连接集群。操作详情请参考 [通过 Kubectl 连接集群](https://cloud.tencent.com/document/product/457/8438)。
3. 执行以下命令，创建 Deployment YAML 文件。
```shell
kubectl create -f Deployment YAML 文件名称
```
例如，创建一个文件名为 nginx.Yaml 的 Deployment YAML 文件，则执行以下命令：
```shell
kubectl create -f nginx.yaml
```
4. 执行以下命令，验证创建是否成功。
```shell
kubectl get deployments
```
返回类似以下信息，即表示创建成功。
```
NAME             DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
first-workload   1         1         1            0           6h
ng               1         1         1            1           42m
```

### Kubectl 更新 Deployment

通过 Kubectl 更新 Deployment 有以下三种方法。其中，[方法一](#Method1) 和 [方法二](#Method2) 均支持 **Recreate** 和 **RollingUpdate** 两种更新策略。
- Recreate 更新策略为先销毁全部 Pod，再重新创建 Deployment。
- RollingUpdate 更新策略为滚动更新策略，逐个更新 Deployment 的 Pod。RollingUpdate 还支持暂停、设置更新时间间隔等。

<dx-tabs>
::: 方法一[](id:Method2)
执行以下命令，更新 Deployment。
```
kubectl edit  deployment/[name]
```
此方法适用于简单的调试验证，不建议在生产环境中直接使用。您可以通过此方法更新任意的 Deployment 参数。

:::
::: 方法二[](id:Method2)
执行以下命令，更新指定容器的镜像。
```
kubectl set image deployment/[name] [containerName]=[image:tag]
```
建议保持 Deployment 的其他参数不变，业务更新时，仅更新容器镜像。
:::
::: 方法三[](id:Method3)
执行以下命令，滚动更新指定资源。
```
kubectl rolling-update [NAME] -f FILE
```
:::
</dx-tabs>



### Kubectl 回滚 Deployment

1. 执行以下命令，查看 Deployment 的更新历史。
```
kubectl rollout history deployment/[name]
```
2. 执行以下命令，查看指定版本详情。
```
kubectl rollout history deployment/[name] --revision=[REVISION]
```
3. 执行以下命令，回滚到前一个版本。
```
kubectl rollout undo deployment/[name]
```
如需指定回滚版本号，可执行以下命令。
```
kubectl rollout undo deployment/[name] --to-revision=[REVISION]
```

### Kubectl 调整 Pod 数量
<dx-tabs>
::: 手动更新 Pod 数量
执行以下命令，手动更新 Pod 数量。
```
kubectl scale deployment [NAME] --replicas=[NUMBER]
```
:::
::: 自动更新 Pod 数量
**前提条件**

开启集群中的 HPA 功能。TKE 创建的集群默认开启 HPA 功能。

**操作步骤**

执行以下命令，设置 Deployment 的自动扩缩容。
```
kubectl autoscale deployment [NAME] --min=10 --max=15 --cpu-percent=80
```
:::
</dx-tabs>



### Kubectl 删除 Deployment

执行以下命令，删除 Deployment。
```
kubectl delete deployment [NAME]
```



