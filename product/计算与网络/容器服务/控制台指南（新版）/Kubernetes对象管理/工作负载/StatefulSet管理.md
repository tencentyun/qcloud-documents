## 简介

StatefulSet 主要用于管理有状态的应用，创建的 Pod 拥有根据规范创建的持久型标识符。Pod 迁移或销毁重启后，标识符仍会保留。 在需要持久化存储时，您可以通过标识符对存储卷进行一一对应。如果应用程序不需要持久的标识符，建议您使用 Deployment 部署应用程序。

## StatefulSet 控制台操作指引

<span id="createStatefulSet"></span>
### 创建 StatefulSet

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中，单击【集群】，进入集群管理页面。
3. 单击需要创建 StatefulSet 的集群 ID，进入待创建 StatefulSet 的集群管理页面。
4. 选择 “工作负载” > “StatefulSet”，进入 StatefulSet 信息页面。如下图所示：
![StatefulSet](https://main.qcloudimg.com/raw/7d6d1ddb1b1580f34519dc62d6bab3d8.png)
5. 单击【新建】，进入 “新建Workload” 页面。如下图所示：
![新建Workload](https://main.qcloudimg.com/raw/9c53cf0e24719da48ce4905603c4e4d3.png)
6. 根据实际需求，设置 Deployment 参数。关键参数信息如下：
 - 工作负载名：自定义。
 - 命名空间：根据实际需求进行选择。
 - 类型：选择 “StatefulSet（有状态集的运行Pod）”。
 - 实例内容器：根据实际需求，为 StatefulSet 的一个 Pod 设置一个或多个不同的容器。
    - 名称：自定义。
    - 镜像：根据实际需求进行选择。
    - 镜像版本：根据实际需求进行填写。
    - CPU/内存限制：可根据 [Kubernetes 资源限制](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/) 进行设置 CPU 和内存的限制范围，提高业务的健壮性。
    - 高级设置：可设置 “**工作目录**”，“**运行命令**”，“**运行参数**”，“**容器健康检查**”，“**特权级**”等参数。
 - 实例数量：根据实际需求选择调节方式，设置实例数量。
7. 单击【创建Workload】，完成创建。

### 更新 StatefulSet

#### 更新 YAML

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中，单击【集群】，进入集群管理页面。
3. 单击需要更新 YAML 的集群 ID，进入待更新 YAML 的集群管理页面。
4. 选择 “工作负载” > “StatefulSet”，进入 StatefulSet 信息页面。如下图所示：
![StatefulSet](https://main.qcloudimg.com/raw/7d6d1ddb1b1580f34519dc62d6bab3d8.png)
5. 在需要更新 YAML 的 StatefulSet 行中，单击【编辑YAML】，进入更新 StatefulSet 页面。
6. 在 “更新StatefulSet” 页面，编辑 YAML，单击【完成】，即可更新 YAML。

#### 更新镜像

1. 在集群管理页面，单击需要更新镜像的 StatefulSet 的集群 ID，进入待更新镜像的 StatefulSet 的集群管理页面。
2. 在需要更新镜像的 StatefulSet 行中，单击【更新镜像】。如下图所示：
![StatefulSet更新镜像](https://main.qcloudimg.com/raw/208eae0b4970c0f800e16722263d6a00.png)
3. 在 “滚动更新镜像” 页面，根据实际需求修改更新方式，设置参数。如下图所示：
![滚动更新镜像](https://main.qcloudimg.com/raw/2d67ba80dcfe3fff0e572b69aea59068.png)
4. 单击【完成】，即可更新镜像。

## Kubectl 操作 StatefulSet 指引

<span id="YAMLSample"></span>
### YAML 示例

```Yaml
apiVersion: v1
kind: Service  ## 创建一个 Headless Service，用于控制网络域
metadata:
  name: nginx
  namespace: default
  labels:
    app: nginx
spec:
  ports:
  - port: 80
    name: web
  clusterIP: None
  selector:
    app: nginx
---
apiVersion: apps/v1
kind: StatefulSet ### 创建一个 Nginx的StatefulSet
metadata:
  name: web
  namespace: default
spec:
  selector:
    matchLabels:
      app: nginx
  serviceName: "nginx"
  replicas: 3 # by default is 1
  template:
    metadata:
      labels:
        app: nginx
    spec:
      terminationGracePeriodSeconds: 10
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
          name: web
        volumeMounts:
        - name: www
          mountPath: /usr/share/nginx/html
  volumeClaimTemplates:
  - metadata:
      name: www
    spec:
      accessModes: [ "ReadWriteOnce" ]
      storageClassName: "cbs"
      resources:
        requests:
          storage: 10Gi
```
- kind：标识 StatefulSet 资源类型。
- metadata：StatefulSet 的名称、Label等基本信息。
- metadata.annotations：对 StatefulSet 的额外说明，可通过该参数设置腾讯云 TKE 的额外增强能力。
- spec.template：StatefulSet 管理的 Pod 的详细模板配置。
- spec.volumeClaimTemplates：提供创建 PVC&PV 的模板。

更多参数详情可查看 [Kubernetes StatefulSet 官方文档](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)。

### 创建 StatefulSet

1. 参考 [YAML 示例](#YAMLSample)，准备 StatefulSet YAML 文件。
2. 安装 Kubectl，并连接集群。操作详情请参考 [通过 Kubectl 连接集群](https://cloud.tencent.com/document/product/457/8438)。
3. 执行以下命令，创建 StatefulSet YAML 文件。
```shell
kubectl create -f StatefulSet YAML 文件名称
```
例如，创建一个文件名为 web.yaml 的 StatefulSet YAML 文件，则执行以下命令：
```shell
kubectl create -f web.yaml
```
4. 执行以下命令，验证创建是否成功。
```shell
kubectl get StatefulSet
```
返回类似以下信息，即表示创建成功。
```
NAME      DESIRED   CURRENT   AGE
test      1         1         10s
```

### 更新 StatefulSet

执行以下命令，查看 StatefulSet 的更新策略类型。
```
kubectl get ds/<daemonset-name> -o go-template='{{.spec.updateStrategy.type}}{{"\n"}}'
```
StatefulSet 有以下两种更新策略类型：
- OnDelete：默认更新策略。该更新策略在更新 StatefulSet 后，需手动删除旧的 StatefulSet Pod 才会创建新的 StatefulSet Pod。
- RollingUpdate：支持 Kubernetes 1.7或更高版本。该更新策略在更新 StatefulSet 模板后，旧的 StatefulSet Pod 将被终止，并且以滚动更新方式创建新的 StatefulSet Pod（Kubernetes 1.7或更高版本）。

#### 方法一

执行以下命令，更新 StatefulSet。
```
kubectl edit StatefulSet/[name]
```
此方法适用于简单的调试验证，不建议在生产环境中直接使用。您可以通过此方法更新任意的 StatefulSet 参数。

#### 方法二

执行以下命令，更新指定容器的镜像。
```
kubectl patch statefulset <NAME> --type='json' -p='[{"op": "replace", "path": "/spec/template/spec/containers/0/image", "value":"<newImage>"}]'
```
建议保持 StatefulSet 的其他参数不变，业务更新时，仅更新容器镜像。

如果更新的 StatefulSet 是滚动更新方式的策略，可执行以下命令查看更新状态：
```
kubectl rollout status sts/<StatefulSet-name>
```

### 删除 StatefulSet

执行以下命令，删除 StatefulSet。
```
kubectl delete  StatefulSet [NAME] --cascade=false
```
--cascade=false 参数表示 Kubernetes 仅删除 StatefulSet，且不删除任何 Pod。如需删除 Pod，则执行以下命令：
```
kubectl delete  StatefulSet [NAME]
```
更多 StatefulSet 相关操作可查看 [Kubernetes官方指引](https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/#scaling-a-statefulset)。

