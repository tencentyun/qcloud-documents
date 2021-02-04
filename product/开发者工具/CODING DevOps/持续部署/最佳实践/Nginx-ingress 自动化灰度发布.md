本文为您详细介绍如何使用 Nginx-ingress 实现自动化灰度发布。

## 进入项目

1. 登录 [CODING 控制台](https://console.cloud.tencent.com/coding)，单击团队域名进入 CODING 使用页面。
2. 单击页面右上角的 <img src ="https://main.qcloudimg.com/raw/d94a8e60dd3a41d0af07d72ae0e9d70e.png" style ="margin:0">，进入项目列表页面，单击项目图标进入目标项目。
3. 选择左侧菜单【持续部署】。

在 Kubernetes 上的应用实现灰度发布，最简单的方案是引入官方的 `Nginx-ingress` 来实现。

我们通过部署两套 deployment 和 services，分别代表灰度环境和生产环境，通过负载均衡算法，实现对两套环境的按照灰度比例进行分流，进而实现灰度发布。

通常的做法是当项目打包新镜像后，通过修改 `yaml` 文件的镜像版本，执行 `kubectl apply` 的方式来更新服务。如果发布流程还需要进行灰度发布，那么可以通过调整两套服务的配置文件权重来控制灰度发布，这种方式离不开人工执行。如果项目数量多，灰度的时间跨度过长，人为误操作的概率将大大增加，过于依赖于人工执行，这对于 `DevOps` 工程实践是不能忍受的。

那么，有没有一种方式能够实现无需人工干预的自动化灰度呢？例如在代码更新后，自动发布到预发布和灰度环境，并在一天的时间内自动将灰度比例从 10% 权重提高到 100%，且能够随时终止，灰度通过后自动发布到生产环境？

答案是肯定的，利用 `CODING DevOps` 就能够满足此类需求。

## Nginx-ingress 架构和原理

迅速回顾一下 `Nginx-ingress` 的架构和实现原理：

![](https://help-assets.codehub.cn/enterprise/20200727162517.png)

`Nginx-ingress` 通过前置的 `Loadbalancer` 类型的 `Service` 接收集群流量，将流量转发至 `Nginx-ingress` Pod 内并对配置的策略进行检查，再转发至目标 `Service`，最终将流量转发至业务容器。

传统的 `Nginx` 需要我们配置 `conf` 文件策略。但 `Nginx-ingress` 通过实现 `Nginx-ingress-Controller` 将原生 `conf` 配置文件和 `yaml` 配置文件进行了转化，当我们配置 `yaml` 文件的策略后，`Nginx-ingress-Controller` 将对其进行转化，并且动态更新策略，动态 Reload `Nginx Pod`，实现自动管理。

那么 `Nginx-ingress-Controller` 如何能够动态感知集群的策略变化呢？方法有很多种，可以通过 webhook admission 拦截器，也可以通过 ServiceAccount 与 Kubernetes Api 进行交互，动态获取。`Nginx-ingress-Controller` 使用后者来实现。所以在部署 `Nginx-ingress` 我们会发现 `Deployment` 内指定了 Pod 的 ServiceAccount，以及实现了 RoleBinding ，最终达到 Pod 与 Kubernetes Api 交互的目标。

## 实现方案预览

为了实现以上目标，我们设计了以下持续部署流水线。

![](https://help-assets.codehub.cn/enterprise/20200727162539.png)

此持续部署流水线主要实现了以下几个步骤：

1.  自动部署到预发布环境
2.  是否进行 A/B 测试
3.  自动灰度发布（自动进行 3 次逐渐提升灰度比例）
4.  发布到生产环境

同时，本文案例还演示了从 Git 提交代码到自动触发持续集成的步骤：

1.  提交代码后触发持续集成，自动构建镜像
2.  镜像构建完成后，自动推送镜像到制品库
3.  触发持续部署



1.  提交代码后触发持续集成，自动构建镜像并推送到制品库

![](https://help-assets.codehub.cn/enterprise/20200727163104.gif)

2.  触发持续部署，并发布到预发布环境

![](https://help-assets.codehub.cn/enterprise/20200727163147.gif)

3.  人工确认：进行 A/B 测试（或跳过直接进入自动灰度）
    
![](https://help-assets.codehub.cn/enterprise/20200727163228.gif)

> 进行 A/B 测试时，只有 Header 包含 location=shenzhen 可以访问新版本，其他用户访问生产环境仍然为旧版本。

4.  人工确认：是否自动灰度发布（自动进行 3 轮逐渐提升灰度比例，每轮间隔 30S）

第一次灰度：新版本 30% 的灰度比例，此时访问生产环境大约有 30% 的流量进入新版本灰度环境：

![](https://help-assets.codehub.cn/enterprise/20200727163307.gif)

30S 后自动进行第二轮灰度：新版本 60% 的灰度比例：

![](https://help-assets.codehub.cn/enterprise/20200727163412.gif)

60S 后自动进行第三轮灰度：新版本 90% 的灰度比例：

![](https://help-assets.codehub.cn/enterprise/20200727163438.gif)

本案例中，我们配置了自动化灰度发布将会以 3 次渐进式进行，每次提高 30% 的比例，每次持续 30S 后自动进入下一个灰度阶段。在不同的灰度阶段，会发现请求新版本出现的概率越来越高。渐进式的灰度可根据业务需要进行任意配置，例如持续 1 天时间分 10 次自动进行灰度，直至发布到生产环境而无需人工值守。

5.  灰度完成，30S 后发布到生产环境

![](https://help-assets.codehub.cn/enterprise/20200727163501.gif)

## 项目源码和原理分析

点击访问项目[源码](https://wangweicoding.coding.net/public/nginx-ingress-gray/nginx-ingress-gray/git)。

```sh
├── Jenkinsfile  # 持续集成脚本
├── deployment
│   ├── canary
│   │   └── deploy.yaml   # 灰度发布部署文件
│   ├── dev
│   │   └── deploy.yaml   # 预发布部署文件
│   └── pro
│       └── deploy.yaml   # 生产部署文件
├── docker
│   ├── Dockerfile
│   └── html
│       └── index.html
├── nginx-ingress-init
│   ├── nginx-ingress-deployment  # nginx-ingress 部署文件
│   │   ├── ClusterRoleBinding.yaml
│   │   ├── RoleBinding.yaml
│   │   ├── clusterRole.yaml
│   │   ├── defaultBackendService.yaml
│   │   ├── defaultBackendServiceaccount.yaml
│   │   ├── deployment.yaml
│   │   ├── nginxDefaultBackendDeploy.yaml
│   │   ├── roles.yaml
│   │   ├── service.yaml
│   │   └── serviceAccount.yaml
│   └── nginx-ingress-helm   # nginx-ingress Helm 包
│       └── nginx-ingress-1.36.3.tgz
└── pipeline   # 持续部署流水线模板
    ├── gray-deploy.json  # 灰度发布流水线
    ├── gray-init.json    # 灰度发布初始化（首次运行）
    └── nginx-ingress-init.json  # nginx-ingress 初始化（首次运行）
```

灰度环境和生产环境主要由 `deployment/canary/deploy.yaml` 和 `deployment/pro/deploy.yaml` 来实现，主要是实现了两套环境的：
*   Deployment
*   Service
*   Ingress

A/B 测试和灰度由配置的 `Ingress` 进行控制：

```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  annotations:
    kubernetes.io/ingress.class: nginx  # nginx=nginx-ingress| qcloud=CLB ingress
    nginx.ingress.kubernetes.io/canary: "true"  # 开启灰度
    nginx.ingress.kubernetes.io/canary-by-header: "location"  # A/B 测试用例 Header key
    nginx.ingress.kubernetes.io/canary-by-header-value: "shenzhen"  # A/B 测试用例 Header value
  name: my-ingress
  namespace: pro
spec:
  rules:
  - host: nginx-ingress.coding.pro
    http:
      paths:
      - backend:
          serviceName: nginx-canary
          servicePort: 80
        path: /
```

A/B 测试主要由注解 `nginx.ingress.kubernetes.io/canary-by-header` 和 `nginx.ingress.kubernetes.io/canary-by-header-value` 进行控制，来匹配请求 Header 的 Key 和 Value。

```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  annotations:
    kubernetes.io/ingress.class: nginx  # nginx=nginx-ingress| qcloud=CLB ingress
    nginx.ingress.kubernetes.io/canary: "true"
    nginx.ingress.kubernetes.io/canary-weight: 30
  name: my-ingress
  namespace: pro
spec:
  rules:
  - host: nginx-ingress.coding.pro
    http:
      paths:
      - backend:
          serviceName: nginx-canary
          servicePort: 80
        path: /
```

而灰度则由注解 `nginx.ingress.kubernetes.io/canary-weight` 控制，值范围可以是 `0-100`，对应灰度权重比例。在 `Nginx-ingress` ，负载均衡算法主要由`加权轮询`的算法来实现分流。

整体架构图如所示：

![](https://help-assets.codehub.cn/enterprise/20200727163900.png)

## 环境准备

1.  K8S 集群，推荐使用腾讯云[容器服务](https://cloud.tencent.com/product/tke)；

2.  开通 [CODING DevOps](https://coding.net/products/cd)，提供镜像构建和流水线的部署能力；

## 实践步骤

1.  克隆源码并推送至自己的 CODING Git 仓库

```sh
$ git clone https://e.coding.net/wangweicoding/nginx-ingress-gray/nginx-ingress-gray.git
$ git remote set-url origin https://you coding git
$ git add .
$ git commit -a -m 'first commit'
$ git push -u origin master
```

注意，推送前请将 `deployment/dev`、`deployment/canary`、`deployment/pro` 文件夹的 `deploy.yaml`、`image` 修改为自己的制品库镜像地址。 

2.  创建持续集成流水线

使用“自定义构建过程”创建构建计划，并选择使用代码仓库的 `Jenkinsfile`。

![](https://help-assets.codehub.cn/enterprise/20200727164052.png)

3.  新增云账号并创建持续部署流水线，复制项目的 pipeline Json 模板到创建的流水线内（3 个）

![](https://help-assets.codehub.cn/enterprise/20200727164028.png)
    
为了便于使用模板，创建持续部署流水线应用名为：nginx-ingress

![](https://help-assets.codehub.cn/enterprise/20200727164109.png)

创建继续创建空白部署流程，复制 Json 模板到持续部署流水线中，一共创建三条流水线：

*   nginx-ingress-init - 用于初始化 nginx-ingress
*   gray-init - 用于首次初始化环境
*   gray-deploy - 用于演示灰度发布

注意：请将以上流水线的云账号选择为自己的云账号，另外 gray-deploy 流水线中，请重新配置“启动所需制品”和“触发器”。

![](https://help-assets.codehub.cn/enterprise/20200727164130.png)

4.  初始化 nginx-ingress（首次运行）
    
    首次运行 `nginx-ingress` 流水线将自动为您部署 `nginx-ingress`。部署成功后，运行 `kubectl get svc | grep nginx-ingress-controller`获取 `Ningx-ingress` 的 `EXTERNAL-IP`，此 IP 为集群请求入口 IP 。并为本机配置 `Host` ，便于访问。

5.  初始化灰度发布（首次运行）

    首次运行 `gray-init` 流水线将自动部署一套完整的环境，否则自动化灰度流水线将会失败。

6.  自动触发灰度发布
    
    现在，您可以尝试修改项目 `docker/html/index.html` 文件，推送后将自动触发构建和持续部署，触发后，进入“持续部署”页面，查看部署详情和流程。

## 总结

我们主要利用了 `CODING 持续部署`的`等待`阶段，通过对不同灰度比例的阶段设定等待时间，自动化逐一运行灰度阶段，最终实现无人工值守的自动化灰度发布。

利用`等待`阶段，可以实现平滑的发布流程，只有当发布出现问题，才需要人工介入。配合持续部署通知功能，可以很方便的将当前发布状态推送到企业微信、钉钉等协作工具。

为了方便展示，案例中对灰度比例和等待时间进行了硬编码，你也可以使用阶段的“自定义参数”来实现对灰度比例和等待实现进行动态控制，针对当前的发布等级动态输入灰度比例和流程控制，使得发布更加灵活。

## 生产建议

本文的 `Nginx-ingress` 采用 `deployment` 的部署方式来实现。`Nginx-ingress` 作为 `Kubernetes` 集群的边缘网关，承担着所有入口流量，其高可用性直接决定了 `Kubernetes` 集群的高可用性。

在生产环境，部署 `Nginx-ingress` 建议遵循以下几点：
*   推荐使用 DaemonSet 的方式部署，避免节点故障。
*   通过标签选择器，将 `Nginx-ingress-controller` 部署在独立的 Node 节点（如高主频、高网络、高 IO 节点）或者低负载的节点。
*   如果采用 `Deployment` 的方式部署，可以为 `Nginx-ingress` 配置 HPA 水平伸缩。