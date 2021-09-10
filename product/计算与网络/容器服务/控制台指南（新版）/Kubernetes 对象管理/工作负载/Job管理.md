## 简介

Job 控制器会创建 1-N 个 Pod，这些 Pod 按照运行规则运行，直至运行结束。Job 可用于批量计算、数据分析等场景。通过设置重复执行次数、并行度、重启策略等满足业务诉求。
Job 执行完成后，不再创建新的 Pod，也不会删除 Pod，您可在 “日志” 中查看已完成的 Pod 的日志。如果您删除了 Job，Job 创建的 Pod 也会同时被删除，将无法查看该 Job 创建的 Pod 的日志。

## Job 控制台操作指引

### 创建 Job

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中，单击**集群**，进入集群管理页面。
3. 单击需要创建 Job 的集群 ID，进入待创建 Job 的集群管理页面。
4. 选择 **工作负载** > **Job**，进入 Job 信息页面。如下图所示：
![](https://main.qcloudimg.com/raw/ca53820e24a5092811efb96cf07b399d.png)
5. 单击**新建**，进入 “新建Workload” 页面。如下图所示：
6. 根据实际需求，设置 Job 参数。关键参数信息如下：
 - **工作负载名**：自定义。
 - **标签**：一个键 - 值对（Key-Value），用于对资源进行分类管理。
 - **命名空间**：根据实际需求进行选择。
 - **类型**：选择 “Job（单次任务）”。
 - **Job设置**：根据实际需求，为 Job 的一个 Pod 设置一个或多个不同的容器。
    - **重复次数**：设置 Job 管理的 Pod 需要重复执行的次数。
    - **并行度**：设置 Job 并行执行的 Pod 数量。
    - **失败重启策略**：设置 Pod 下容器异常退出后的重启策略。
       - **选择 Never**：不重启容器，直至 Pod 下所有容器退出。
       - **选择 OnFailure**：Pod 继续运行，容器将重新启动。
 - **数据卷（选填）**：为容器提供存储，目前支持临时路径、主机路径、云硬盘数据卷、文件存储 NFS、配置文件、PVC，还需挂载到容器的指定路径中。      
 - **实例内容器**：根据实际需求，为 Job 的一个 Pod 设置一个或多个不同的容器。
    - **名称**：自定义。
    - **镜像**：根据实际需求进行选择。
    - **镜像版本**：根据实际需求进行填写。
    - **CPU/内存限制**：可根据 [Kubernetes 资源限制](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/) 进行设置 CPU 和内存的限制范围，提高业务的健壮性。
    - **GPU 资源**：配置该工作负载使用的最少 GPU 资源。
    - **高级设置**：可设置 “工作目录”，“运行命令”，“运行参数”，“容器健康检查”，“特权级”等参数。
 - **镜像访问凭证**：容器镜像默认私有，在创建工作负载时，需选择实例对应的镜像访问凭证。
 - **节点调度策略**：可根据调度规则，将 Pod 调度到符合预期的 Label 的节点中。
7. 单击**创建Workload**，完成创建。

### 查看 Job 状态

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中，单击**集群**，进入集群管理页面。
3. 单击需要查看 Job 状态的集群 ID，进入待查看 Job 状态的集群管理页面。
4. 选择 “工作负载” > “Job”，进入 Job 信息页面。如下图所示：
![Job](https://main.qcloudimg.com/raw/0fa661e68d83d9cbb1f3228ad4988061.png)
5. 单击需要查看状态的 Job 名称，即可查看 Job 详情。

### 删除 Job

Job 执行完成后，不再创建新的 Pod，也不会删除 Pod，您可在 “日志” 中查看已完成的 Pod 的日志。如果您删除了 Job，Job 创建的 Pod 也会同时被删除，将查看不到该 Job 创建的 Pod 的日志。

## Kubectl 操作 Job 指引

[](id:YAMLSample)
### YAML 示例

```Yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: pi
spec:
  completions: 2
  parallelism: 2
  template:
    spec:
      containers:
      - name: pi
        image: perl
        command: ["perl",  "-Mbignum=bpi", "-wle", "print bpi(2000)"]
      restartPolicy: Never
  backoffLimit: 4
```
- kind：标识 Job 资源类型。
- metadata：Job 的名称、Label等基本信息。
- metadata.annotations：Job 的额外说明，可通过该参数设置腾讯云 TKE 的额外增强能力。
- spec.completions：Job 管理的 Pod 重复执行次数。
- spec.parallelism：Job 并行执行的 Pod 数。
- spec.template：Job 管理的 Pod 的详细模板配置。

### 创建 Job

1. 参考 [YAML 示例](#YAMLSample)，准备 Job YAML 文件。
2. 安装 Kubectl，并连接集群。操作详情请参考 [通过 Kubectl 连接集群](https://cloud.tencent.com/document/product/457/8438)。
3. 创建 Job YAML 文件。
```
kubectl create -f Job YAML 文件名称
```
例如，创建一个文件名为 pi.yaml 的 Job YAML 文件，则执行以下命令：
```shell
kubectl create -f pi.yaml
```
4. 执行以下命令，验证创建是否成功。
```shell
kubectl get job
```
返回类似以下信息，即表示创建成功。
```
NAME      DESIRED   SUCCESSFUL   AGE
job       1         0            1m
```

### 删除 Job
执行以下命令，删除 Job。
```
kubectl delete job [NAME]
```



