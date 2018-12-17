## DaemonSet 管理
### DaemonSet 简介
DaemonSet会保证所有（或部分）节点上均运行有指定的Pod， 新节点添加到集群内也会有自动部署Pod, 节点被移除集群后，Pod将自动回收。
主要用于部署常驻集群内的后台程序，如节点的日志采集。
### DaemonSet调度说明
若配置了Pod的nodeSelector或affinity参数， DaemonSet管理的Pod按照指定的调度规则调度， 若未设置上述参数，将在所有的节点上部署Pod。
### DaemonSet 控制台操作指引
#### 创建DaemonSet
1. 点击需要部署创建DaemonSet的集群ID，进入集群详情页面。
2. 点击创建DaemonSet选项，选择新建创建DaemonSet。
3. 根据指引设置创建DaemonSet参数，完成创建。
4. 可通过事件查看DaemonSet创建过程。
![][createDaemonSet]

**说明**
1. 您可以为DaemonSet的一个Pod设置多个不同的容器
2. CPU和内存限制建议填写，Request和Limit恰当的设置可以提供业务的健壮性，详细信息可查看[Kubenretes资源限制](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/)。
3. 您可以通过容器的高级设置定制`工作目录`，`运行命令`，`运行参数`，`容器健康检查`，`特权级`等参数。


#### 更新DaemonSet
**Yaml更新**
1. 点击需要部署的DaemonSet的集群ID，进入集群详情页面。
2. 选择需要更新的DaemonSet, 进入DaemonSet详情页，点击Yaml tab, 可编辑Yaml直接更新

**更新镜像**
仅在Kubernetes 1.6或更高版本中支持DaemonSet滚动更新功能
1. 点击需要部署的DaemonSet的集群ID，进入集群详情页面。
2. 选择需要更新的DaemonSet, 点击更新镜像操作。


### kubectl 操作 DaemonSet 指引
#### Yaml示例
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
>注：以上YAML示例引用于 https://kubernetes.io/docs/concepts/workloads/controllers/daemonset， 创建时可能存在容器镜像拉取不成功的情况，仅供于本文介绍DaemonSet的组成。

- kind: 标识该资源是DaemonSet类型
- metadata：该DaemonSet的名称、Label等基本信息
- metadata.annotations: 对DaemonSet的额外说明，腾讯云TKE额外增强能力可以通过该参数设置。
- spec.template:  该DaemonSet管理的Pod的详细模板配置
- 更多可查看[kubernetes DaemonSet官方文档](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)

#### kubectl 创建DaemonSet

1. 准备DaemonSet Yaml文件， 例如上述文件为fluentd-elasticsearch.Yaml
2. kubectl安装完成，并且已连接上集群（可直接登录集群节点使用kubectl）
3. 执行命令创建：
```shell
kubectl create -f fluentd-elasticsearch.yaml
```
4. 执行命令验证创建情况：
```shell
kubectl get DaemonSet
```

#### kubectl 更新DaemonSet
DaemonSet有两种更新策略类型（可通过`kubectl get ds/<daemonset-name> -o go-template='{{.spec.updateStrategy.type}}{{"\n"}}'`查看）：

- OnDelete：这是向后兼容性的默认更新策略。使用 OnDelete更新策略，在更新DaemonSet后，只有在手动删除旧的DaemonSet Pod时才会创建新的DaemonSet Pod。
- RollingUpdate：使用RollingUpdate更新策略，在更新DaemonSet模板后，旧的DaemonSet Pod将被终止，并且将以滚动方式创建新的DaemonSet Pod（Kubernetes 1.6或更高版本）



**方法一**：直接通过`kubectl edit DaemonSet/[name]`更新
适用与简单调试验证，不建议直接在生产环境使用，可以通过该方法更新任意的DaemonSet参数。

**方法二**：通过`kubectl set image ds/[daemonset-name][container-name]=[container-new-image] `更新指定容器的镜像， 保证DaemonSet的其他参数不变，业务更新时仅更新容器镜像.

如果是滚动更新的更新策略， 那么还可以通过`kubectl rollout status ds/<daemonset-name>`命令查看更新状态。

#### kubectl 回滚 DaemonSet
1. 通过`kubectl rollout history daemonset /[name]` 查看daemonset 的更新历史。
2. 通过`kubectl rollout history daemonset /[name] --revision=[REVISION]` ,查看指定版本详情。
3. 可通过`kubectl rollout undo daemonset /[name] --to-revision=[REVISION]`, 回滚到指定的版本号。不指定`--to-revision=[REVISION]`默认回滚到前一个版本。
4.
#### kubectl删除 DaemonSet
1. 执行命令`kubectl delete  DaemonSet [NAME]`


[createDaemonSet]:https://main.qcloudimg.com/raw/746fff6232ad98317d05d841889eed1f.png
