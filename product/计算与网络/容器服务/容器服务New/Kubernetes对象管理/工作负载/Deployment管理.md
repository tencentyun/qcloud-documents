## Deployment 管理
### Deployment 简介
Deployment声明了Pod的模板和控制Pod的运行策略，适用于部署无状态的应用程序，可以根据业务需求声明Deployment下运行的Pod的副本数、调度策略、更新策略等。
### Deployment 控制台操作指引
#### 创建Deployment

1. 点击需要部署Deployment的集群ID，进入集群详情页面。
2. 点击Deployment选项，选择新建Deployment。
3. 根据指引设置Deployment参数，完成创建。
![][createdeploymet]
4. 可通过事件查看Deployment创建过程，当运行数量=期望数量时表示Deployment下的所有Pod已创建完成。

**说明**
1. 您可以为Deployment的一个Pod设置多个不同的容器
2. CPU和内存限制建议填写，Request和Limit恰当的设置可以提供业务的健壮性，详细信息可查看[Kubenretes资源限制](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/)。
3. 您可以通过容器的高级设置定制`工作目录`，`运行命令`，`运行参数`，`容器健康检查`，`特权级`等参数。

#### 设置Deployment亲和性调度
1. 创建Deployment时点击高级设置。
2. 根据业务需要配置调度规则。
3. 完成。


#### 更新Deployment
**Yaml更新**
1. 点击需要部署的Deployment的集群ID，进入集群详情页面。
2. 选择需要更新的Deployment, 进入Deployment详情页，点击Yaml tab, 可编辑Yaml直接更新

**更新镜像**
1. 点击需要部署的Deployment的集群ID，进入集群详情页面。
2. 选择需要更新的Deployment, 点击更新镜像操作。
    - 支持滚动更新（默认更新策略，推荐）
    - 支持快速更新

![][updatedeploymet]
#### 回滚Deployment
1. 点击需要回滚的Deployment的集群ID，进入集群详情页面。
2. 选择需要回滚的Deployment, 点击回滚操作。
3. 选择需要回滚的版本，执行回滚。

![][rolloutdeploymet]

#### 调整Deployment下Pod数量
1. 点击需要调整Pod数量的Deployment的集群ID，进入集群详情页面。
2. 选择需要调整Pod数量的Deployment, 点击调整Pod数量操作。
3. 设置需要调整Pod数量，完成。


![][scaledeploymet]


###kubectl 操作 Deployment 指引
#### Yaml示例
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

- kind: 标识该资源是Deployment类型
- metadata：该deployment的名称、Namespace、Label等基本信息
- metadata.annotations: 对Deployment的额外说明，腾讯云TKE额外增强能力可以通过该参数设置。
- spec.replicas： 该deployment管理的Pod数量
- spec.selector： 该deployment管理Seletor选中的Pod的label
- spec.template:  该deployment管理的Pod的详细模板配置
- 更多可查看[kubernetes Deployment官方文档](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)


#### kubectl创建Deployment

1. 准备Deployment Yaml文件， 例如上述文件为nginx.Yaml
2. kubectl安装完成，并且已连接上集群（可直接登录集群节点使用kubectl）
3. 执行命令创建：
```shell
kubectl create -f nginx.yaml
```
4. 执行命令验证创建情况：
```shell
kubectl get deployments
```

#### kubectl更新Deployment
**方法一**：直接通过`kubectl edit  deployment/[name]`更新
适用与简单调试验证，不建议直接在生产环境使用，可以通过该方法更新任意的deployment参数。
**方法二**：通过`kubectl set image deployment/[name] [containerName]=[image:tag] `更新指定容器的镜像， 尽量保证deployment的其他参数不变，业务更新时仅更新容器镜像。

 上述两种方法均支持`Recreate`和`RollingUpdate` 两种更新策略。Recreate表示先销毁全部Pod，然后重新创建；RollingUpdate为滚动更新策略，逐个更新Deployment的Pod，支持暂停、设置更新时间间隔等。

**方法三**：通过`kubectl rolling-update [NAME] -f FILE` 滚动更新指定资源, 查看更多[滚动更新说明](https://kubernetes.io/cn/docs/tasks/run-application/rolling-update-replication-controller/)。

#### kubectl回滚Deployment
1. 通过`kubectl rollout history deployment/[name]` 查看deployment的更新历史。
2. 通过`kubectl rollout history deployment/[name] --revision=[REVISION]` ,查看指定版本详情。
3. 可通过`kubectl rollout undo deployment/[name] --to-revision=[REVISION]`, 回滚到指定的版本号。不指定`--to-revision=[REVISION]`默认回滚到前一个版本。

#### kubectl调整Deployment下Pod数量
1. 手动更新Pod数量
   通过`kubectl scale deployment [NAME] --replicas=[NUMBER]`更新Pod数量。
2. 自动更新Pod数量
   前提：需要集群集群内开启HPA功能，TKE集群默认开启。
   通过`kubectl autoscale deployment [NAME] --min=10 --max=15 --cpu-percent=80` 设置deployment的自动扩缩容。

#### kubectl删除Deployment
1. 执行命令`kubectl delete deployment [NAME]`

[createdeploymet]:https://main.qcloudimg.com/raw/d1263f63c666250b39876b55015d313d.png
[scaledeploymet]:https://main.qcloudimg.com/raw/cf84d73219bce23e4c2574ba1b517168.
[updatedeploymet]:https://main.qcloudimg.com/raw/32bd1e1f320fa9d55e7d4940f44b2466.png
[rolloutdeploymet]:https://main.qcloudimg.com/raw/1b6745b956291cf9febcc1351f9da45e.png
