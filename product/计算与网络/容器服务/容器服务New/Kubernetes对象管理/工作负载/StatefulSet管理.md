## StatefulSet 管理
### StatefulSet 简介
StatefulSet主要用于管理有状态的应用，与Kubernetes不同的，StatefulSet创建的Pod拥有一定规范创建的持久的标识符，Pod迁移或销毁重启后标识符会保留。 在需要持久化存储时，可以通过标识符对存储卷进行一一对应。如果应用程序不需要持久的标识符，建议使用Deployment来部署应用程序。

### StatefulSet 控制台操作指引
#### 创建 StatefulSet
1. 点击需要部署创建 StatefulSet 的集群ID，进入集群详情页面。
2. 点击创建 StatefulSet 选项，选择新建创建 StatefulSet。
3. 根据指引设置创建 StatefulSet 参数，完成创建。
4. 可通过事件查看 StatefulSet 创建过程。

![][createStatefulSet]

**说明**
1. 您可以为StatefulSet的一个Pod设置多个不同的容器
2. CPU和内存限制建议填写，Request和Limit恰当的设置可以提供业务的健壮性，详细信息可查看[Kubenretes资源限制](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/)。
3. 您可以通过容器的高级设置定制`工作目录`，`运行命令`，`运行参数`，`容器健康检查`，`特权级`等参数。


#### 更新 StatefulSet
**Yaml更新**
1. 点击需要部署的 StatefulSet 的集群ID，进入集群详情页面。
2. 选择需要更新的 StatefulSet 进入StatefulSet 详情页，点击Yaml tab, 可编辑Yaml直接更新

**更新镜像**

1. 点击需要部署的 StatefulSet 的集群ID，进入集群详情页面。
2. 选择需要更新的 StatefulSet, 点击更新镜像操作。


### kubectl 操作 StatefulSet指引
#### Yaml示例
```Yaml
apiVersion: v1
kind: Service  ## 创建一个Headless Service，用于控制网络域
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
- kind: 标识该资源是 StatefulSet 类型
- metadata：该 StatefulSet 的名称、Label等基本信息
- metadata.annotations: 对 StatefulSet 的额外说明，腾讯云TKE额外增强能力可以通过该参数设置。
- spec.template:  该 StatefulSet 管理的Pod的详细模板配置
- spec.volumeClaimTemplates: 提供创建PVC&PV的模板
- 更多可查看[kubernetes StatefulSet官方文档](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)

#### 创建 StatefulSet
1. 准备 StatefulSet Yaml文件， 例如上述文件为web.yaml
2. kubectl安装完成，并且已连接上集群（可直接登录集群节点使用kubectl）
3. 执行命令创建：
```shell
kubectl create -f web.yaml
```
4. 执行命令验证创建情况：
```shell
kubectl get StatefulSet
```

#### 更新 StatefulSet
StatefulSet 有两种更新策略类型（可通过`kubectl get ds/<daemonset-name> -o go-template='{{.spec.updateStrategy.type}}{{"\n"}}'`查看）：

- OnDelete：这是向后兼容性的默认更新策略。使用 OnDelete更新策略，在更新 StatefulSet 后，只有在手动删除旧的StatefulSet Pod时才会创建新的StatefulSet Pod。
- RollingUpdate：使用RollingUpdate更新策略，在更新 StatefulSet 模板后，旧的StatefulSet Pod将被终止，并且将以滚动方式创建新的 StatefulSet Pod（Kubernetes 1.7或更高版本）



**方法一**：直接通过`kubectl edit StatefulSet/[name]`更新
适用与简单调试验证，不建议直接在生产环境使用，可以通过该方法更新任意的StatefulSet参数。

**方法二**：通过`kubectl patch statefulset <NAME> --type='json' -p='[{"op": "replace", "path": "/spec/template/spec/containers/0/image", "value":"<newImage>"}]'
`更新指定容器的镜像， 保证 StatefulSet 的其他参数不变，业务更新时仅更新容器镜像.

如果是滚动更新的更新策略， 那么还可以通过`kubectl rollout status sts/<StatefulSet-name>`命令查看更新状态。

#### 删除 StatefulSet

1. 执行命令`kubectl delete  StatefulSet [NAME] --cascade=false`
  --cascade=false参数告诉Kubernetes仅删除StatefulSet，并且不删除任何Pod。 不设置该参数则关联删除Pod.


更多StatefulSet相关操作可查看[Kubernetes官方指引](https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/#scaling-a-statefulset)。

[createStatefulSet]:https://main.qcloudimg.com/raw/eabcc20b3b1439970f914fd63c458468.png
[updateStatefulSet]:
