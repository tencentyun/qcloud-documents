本文为您详细介绍如何使用 CODING 持续部署进行蓝绿部署。

## 进入项目

1. 登录 [CODING 控制台](https://console.cloud.tencent.com/coding)，单击团队域名进入 CODING 使用页面。
2. 单击页面右上角的 <img src ="https://main.qcloudimg.com/raw/d94a8e60dd3a41d0af07d72ae0e9d70e.png" style ="margin:0">，进入项目列表页面，单击项目图标进入目标项目。
3. 选择左侧菜单【持续部署】。

## 前言

软件世界的迭代进化比以往任何事物的变化都更快。为了保持市场竞争力，需要尽快推出新的软件版本，并且中间还不能够中断活跃用户的访问，影响用户体验。越来越多企业已将其应用迁移到 Kubernetes，使用持续部署的方式在变化中迭代。

在 Kubernetes 中有几种不同的方式发布应用，所以为了让应用在升级期间依然平稳提供服务，选择一个正确的发布策略就非常重要了，本篇文章将讲解如何在 Kubernetes 使用蓝绿的方式更新镜像。

## 原理

蓝绿发布是版本 1 与版本 2 会同时存在，通过控制 Service 来决定使用具体哪一个版本，也称为红黑部署。蓝绿发布与滚动更新不同，版本 2 （`绿`） 与版本 1（`蓝`）一起部署，在测试新版本满足要求后，然后更新 Service 对象，通过替换 label selector 中的版本标签来将流量发送到新版本，更新过程如下图所示：

![](https://help-assets.codehub.cn/enterprise/20200727153823.png)

下面将会演示如何使用 Kubernetes 原生方式来升级应用。

## 快速入门

### 准备

image

```shell
bebullish/demo:v1
bebullish/demo:v2
```

deployment-v1

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: demo-dp-v1
spec:
  selector:
    matchLabels:
      app: demo
      version: v1
  replicas: 3
  template:
    metadata:
      labels:
        app: demo
        version: v1
    spec: 
      containers:
      - name: demo
        image: bebullish/demo:v1
        ports:
        - containerPort: 8080
```

deployment-v2

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: demo-dp-v2
spec:
  selector:
    matchLabels:
      app: demo
      version: v2
  replicas: 3
  template:
    metadata:
      labels:
        app: demo
        version: v2
    spec: 
      containers:
      - name: demo
        image: bebullish/demo:v2
        ports:
        - containerPort: 8080
```

service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: demo-service
spec:
  selector:
    app: demo
    version: v1                              # 通过更改 version 来控制流量走向
  type: LoadBalancer
  ports:
  - port: 80
    targetPort: 8080
    protocol: TCP
```

将上述  `deployment-v1` 以及 `service` 保存为 yaml 文件，使用 `kubectl apply -f` 命令创建 yaml 资源，等待创建成功后，使用 `kubectl get svc` 获取 EXTERNAL-IP。

### 测试

如果使用浏览器测试的话，你会发现每次调用都会返回同一个 pod 的名字，那是因为浏览器发出的请求包含 keepAlive，所以需要使用 curl 来保证每次发出的请求都是重新创建的。

```sh
curl -X GET http://${EXTERNAL-IP}
```

![](https://help-assets.codehub.cn/enterprise/20200727154446.png)

### 升级

将上述 `deployment-v2` 保存为 yaml 文件，使用 `kubectl apply -f` 命令创建 yaml 资源，切换流量之前先执行命令，以便查看镜像更新过程。

```sh
while true; do curl -X GET http://49.232.125.218 ; done
```

等待 `deployment-v2` 创建成功后，通过将 service 的 version 值改为 v2 来切换流量。

```sh
kubectl edit service demo-service
```

### 查看日志

![](https://help-assets.codehub.cn/enterprise/20200727154459.png)

### 请求流量

![](https://help-assets.codehub.cn/enterprise/20200727154516.png)

### 结论

首先可以发现在更新过程中，程序保持一直可用的状态，v2 版本部署成功之后，所有请求还是 v1 版本，当流量切换后，立刻出现 v2 版本的日志，并且不会出现 v1 版本的日志，说明流量是一次性切换的，如果需要回滚只需要将流量切回 v1 版本即可。

## 使用 CODING CD 方式升级应用

### 创建服务

![](https://help-assets.codehub.cn/enterprise/20200727154531.png)

service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: demo-service
spec:
  selector:
    createBy: demo-service       # 这里填写的标签，会被添加到对应的 ReplicaSet 中
  type: LoadBalancer
  ports:
  - port: 80
    targetPort: 8080
    protocol: TCP
```

这里注意，service 创建之后应不会匹配到任何资源，即 endpoint 为空，而在后面执行部署流程时会为 ReplicaSet 添加 label `createBy: demo-service` ，从而决定流量走向。

![](https://help-assets.codehub.cn/enterprise/20200727154547.png)

部署成功之后可以看到 `demo-service`。

### 配置制品

![](https://help-assets.codehub.cn/enterprise/20200727154606.png)

使用 docker 官方镜像需要以 `docker.io` 开头。

### 配置 yaml 及绑定制品

![](https://help-assets.codehub.cn/enterprise/20200727154619.png)

replicaSet

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: demo-rs
spec:
  replicas: 3
  selector:
    matchLabels:
      app: demo
  template:
    metadata:
      labels:
        app: demo
    spec:
      containers:
        - image: docker.io/bebullish/demo
          name: demo
          ports:
            - containerPort: 8080
```

阶段中选择 `部署（Manifest）` ，输入上述 yaml 文件（目前发布策略选项仅支持 ReplicaSet），这里需要把镜像的版本删除掉，在需要绑定的制品选择之前配置的制品。这样配置之后，每次执行的时候版本是动态传入的。

### 蓝绿（红黑）发布配置

![](https://help-assets.codehub.cn/enterprise/20200727154637.png)

在下方勾选让 CODING 部署控制台管理入口流量，然后选择 `demo-service` 所在的命名空间（我这里是在 `marlon` 这个命名空间下），然后选择 `demo-service` ，策略选择 Red/Black（Blue/Green），保存即可。

### 发布制品

![](https://help-assets.codehub.cn/enterprise/20200727154657.png)

选择应用和部署流程，输入版本 v1。

### 查看结果

![](https://help-assets.codehub.cn/enterprise/20200727154714.png)

等待一小段时间后，就可以在部署控制台中看到发布的资源了。

### 更新镜像版本

![](https://help-assets.codehub.cn/enterprise/20200727154738.png)

再次执行发布，版本输入 v2。

### 更新原理

![](https://help-assets.codehub.cn/enterprise/20200727154755.png)

基于 CODING CD 的蓝绿发布和一般的蓝绿发布略有不同，一旦 v2 版本的 pod 处于就绪状态后，他就会立即获得流量，而当所有的 v2 版本的 pod 处于就绪状态后，会禁用 v1 版本的 pod，此时所有流量会打到 v2 版本上，从而完成更新。

> 注意：基于 CODING CD 的蓝绿发布会出现 v1 版本和 v2 版本同时获得流量的情况，具体取决于 pod 的就绪探针，v2 版本的 pod 一旦就绪，那么它就会获得流量，所以需要合理设计就绪探针，尽量减少 v1 版本和 v2 版本同时存在的时间差。

## 总结

使用 Kubernetes 原生方式实现蓝绿更新步骤较多，但也容易出错，推荐使用 CODING 所提供的 CD 功能，配置一次，永久使用。不仅降低了人工成本，提高容错率，还提供了更加丰富的持续部署功能。

## 参考文章

[TrafficManagement](https://spinnaker.io/guides/user/kubernetes-v2/traffic-management/)

[RolloutStrategies](https://spinnaker.io/guides/user/kubernetes-v2/rollout-strategies/)

[CODING 持续部署](/docs/cd/overview.html)