## 简介

DaemonSet 主要用于部署常驻集群内的后台程序，例如节点的日志采集。DaemonSet 保证在所有或部分节点上均运行指定的 Pod。 新节点添加到集群内时，也会有自动部署 Pod；节点被移除集群后，Pod 将自动回收。

## 调度说明

若配置了 Pod 的 nodeSelector 或 affinity 参数，DaemonSet 管理的 Pod 将按照指定的调度规则调度。若未配置 Pod 的 nodeSelector 或 affinity 参数，则将在所有的节点上部署 Pod。

## DaemonSet 控制台操作指引

### 创建 DaemonSet
1. 登录容器服务控制台，选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2/cluster)**。
2. 单击需要创建 DaemonSet 的集群 ID，进入待创建 DaemonSet 的集群管理页面。
3. 选择**工作负载** > **DaemonSet**，进入 DaemonSet 信息页面。如下图所示：
![](https://main.qcloudimg.com/raw/4c9a1a9e7115d341c4426833a76077c0.png)
4. 单击**新建**，进入 “新建Workload” 页面。
根据实际需求，设置 DaemonSet 参数。关键参数信息如下：
 - **工作负载名**：输入自定义名称。
 - **标签**：一个键 - 值对（Key-Value），用于对资源进行分类管理。
 - **命名空间**：根据实际需求进行选择。
 - **类型**：选择**DaemonSet（在每个主机上运行Pod）**。
 - **数据卷（选填）**：为容器提供存储，目前支持临时路径、主机路径、云硬盘数据卷、文件存储 NFS、配置文件、PVC，还需挂载到容器的指定路径中。
 - **实例内容器**：根据实际需求，为 DaemonSet 的一个 Pod 设置一个或多个不同的容器。
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
    - 高级设置：可设置 “**工作目录**”，“**运行命令**”，“**运行参数**”，“**容器健康检查**”，“**特权级**”等参数。
 - **镜像访问凭证**：容器镜像默认私有，在创建工作负载时，需选择实例对应的镜像访问凭证。
 - **节点调度策略**：可根据调度规则，将 Pod 调度到符合预期的 Label 的节点中。
5. 单击**创建Workload**，完成创建。

### 更新 DaemonSet

#### 更新 YAML
1. 登录容器服务控制台，选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2/cluster)**。
2. 单击需要更新 YAML 的集群 ID，进入待更新 YAML 的集群管理页面。
4. 选择**工作负载** > **DaemonSet**，进入 DaemonSet 信息页面。如下图所示：
![](https://main.qcloudimg.com/raw/292064b549bd53d5e6f24bfa2a44b141.png)
5. 在需要更新 YAML 的 DaemonSet 行中，选择**更多** > **编辑YAML**，进入更新 DaemonSet 页面。
6. 在 “更新DaemonSet” 页面编辑 YAML，单击**完成**即可更新 YAML。

#### 更新 Pod 配置
>? 仅在 Kubernetes 1.6或更高版本中支持 DaemonSet 滚动更新功能。
>
1. 在集群管理页面，单击需要更新 Pod 配置的 DaemonSet 的集群 ID，进入待更新 Pod 配置的 DaemonSet 的集群管理页面。
2. 在需要更新 Pod 配置的 DaemonSet 行中，单击**更新Pod配置**。如下图所示：
![](https://main.qcloudimg.com/raw/22a518ea2069ff209ea9b3175bcbb248.png)
3. 在 “更新Pod配置” 页面，根据实际需求修改更新方式，设置参数。如下图所示：
![](https://main.qcloudimg.com/raw/3205e96b04d94c693af9f8fb28614cff.png)
4. 单击**完成**，即可更新 Pod 配置。

## Kubectl 操作 DaemonSet 指引


### YAML 示例[](id:YAMLSample)
```Yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluentd-elasticsearch
  namespace: kube-system
  labels:
    k8s-app: fluentd-logging
spec:
  selector:
    matchLabels:
      name: fluentd-elasticsearch
  template:
    metadata:
      labels:
        name: fluentd-elasticsearch
    spec:
      tolerations:
      - key: node-role.kubernetes.io/master
        effect: NoSchedule
      containers:
      - name: fluentd-elasticsearch
        image: k8s.gcr.io/fluentd-elasticsearch:1.20
        resources:
          limits:
            memory: 200Mi
          requests:
            cpu: 100m
            memory: 200Mi
        volumeMounts:
        - name: varlog
          mountPath: /var/log
        - name: varlibdockercontainers
          mountPath: /var/lib/docker/containers
          readOnly: true
      terminationGracePeriodSeconds: 30
      volumes:
      - name: varlog
        hostPath:
          path: /var/log
      - name: varlibdockercontainers
        hostPath:
          path: /var/lib/docker/containers
```
>!以上 YAML 示例引用于 `https://kubernetes.io/docs/concepts/workloads/controllers/daemonset`， 创建时可能存在容器镜像拉取不成功的情况，仅用于本文介绍 DaemonSet 的组成。

- **kind**：标识 DaemonSet 资源类型。
- **metadata**：DaemonSet 的名称、Label等基本信息。
- **metadata.annotations**：DaemonSet 的额外说明，可通过该参数设置腾讯云 TKE 的额外增强能力。
- **spec.template**：DaemonSet 管理的 Pod 的详细模板配置。

更多可查看 [Kubernetes DaemonSet 官方文档](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)。

### Kubectl 创建 DaemonSet

1. 参考 [YAML 示例](#YAMLSample)，准备 StatefulSet YAML 文件。
2. 安装 Kubectl，并连接集群。操作详情请参考 [通过 Kubectl 连接集群](https://cloud.tencent.com/document/product/457/8438)。
3. 执行以下命令，创建 DaemonSet YAML 文件。
```shell
kubectl create -f DaemonSet YAML 文件名称
```
例如，创建一个文件名为 fluentd-elasticsearch.yaml 的 StatefulSet YAML 文件，则执行以下命令：
```shell
kubectl create -f fluentd-elasticsearch.yaml
```
4. 执行以下命令，验证创建是否成功。
```shell
kubectl get DaemonSet
```
返回类似以下信息，即表示创建成功。
```
NAME       DESIRED   CURRENT   READY     UP-TO-DATE   AVAILABLE   NODE SELECTOR       AGE
frontend   0         0         0         0            0           app=frontend-node   16d
```

### Kubectl 更新 DaemonSet

执行以下命令，查看 DaemonSet 的更新策略类型。
```
kubectl get ds/<daemonset-name> -o go-template='{{.spec.updateStrategy.type}}{{"\n"}}'
```
DaemonSet 有以下两种更新策略类型：
- OnDelete：默认更新策略。该更新策略在更新 DaemonSet 后，需手动删除旧的 DaemonSet Pod 才会创建新的DaemonSet Pod。
- RollingUpdate：支持 Kubernetes 1.6或更高版本。该更新策略在更新 DaemonSet 模板后，旧的 DaemonSet Pod 将被终止，并且以滚动更新方式创建新的 DaemonSet Pod。

#### 方法一

执行以下命令，更新 DaemonSet。
```
kubectl edit DaemonSet/[name]
```
此方法适用于简单的调试验证，不建议在生产环境中直接使用。您可以通过此方法更新任意的 DaemonSet 参数。

#### 方法二

执行以下命令，更新指定容器的镜像。
```
kubectl set image ds/[daemonset-name][container-name]=[container-new-image]
```
建议保持 DaemonSet 的其他参数不变，业务更新时，仅更新容器镜像。

### Kubectl 回滚 DaemonSet

1. 执行以下命令，查看 DaemonSet 的更新历史。
```
kubectl rollout history daemonset /[name]
```
2. 执行以下命令，查看指定版本详情。
```
kubectl rollout history daemonset /[name] --revision=[REVISION]
```
3. 执行以下命令，回滚到前一个版本。
```
kubectl rollout undo daemonset /[name]
```
如需指定回滚版本号，可执行以下命令。
```
kubectl rollout undo daemonset /[name] --to-revision=[REVISION]
```

### Kubectl 删除 DaemonSet
执行以下命令，删除 DaemonSet。
```
kubectl delete  DaemonSet [NAME]
```


