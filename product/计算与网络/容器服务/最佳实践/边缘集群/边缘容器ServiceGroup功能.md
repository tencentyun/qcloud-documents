边缘计算场景下，往往需要在同一个集群中管理多个边缘站点，每个边缘站点内有一个或多个计算节点；同时希望在每个站点中都运行一组有业务逻辑联系的服务，每个站点内的服务是一套完整的功能，可以为用户提供服务。但是，由于受到网络限制，有业务联系的服务之间不希望或者不能跨站点访问。

目前，已有 [常规方案](#step1) 应对上述问题，但是仍有痛点无法解决。为此，[边缘容器服务](https://cloud.tencent.com/document/product/457/42876) 提供 ServiceGroup 特性，只需两个 yaml 文件即可轻松实现即使上百地域的服务部署，且无需应用适配或改造。

## ServiceGroup 概述

ServiceGroup 可以便捷地在共属同一个集群的不同机房或区域中各自部署一组服务，并且使得各个服务间的请求在本机房或本地域内部即可完成，避免服务跨地域访问。

原生 Kubernetes 无法控制 Deployment 的 Pod 创建的具体节点位置，需要通过统筹规划节点的亲和性来间接完成，当边缘站点数量以及需要部署的服务数量过多时，管理和部署方面的极为复杂，乃至仅存在理论上的可能性；与此同时，为了将服务间的相互调用限制在一定范围，业务方需要为各个 Deployment 分别创建专属的 Service，管理方面的工作量巨大且极容易出错并引起线上业务异常。

ServiceGroup 就是为这种场景设计的，客户只需要使用 ServiceGroup 提供的 DeploymentGrid 和 ServiceGrid 这两种 TKE Edge 自研的 Kubernetes 资源，即可方便地将服务分别部署到这些节点组中，并进行服务流量管控。另外，还能保证各区域服务数量及容灾。

### 1. 整体架构<span id="OverallStructure"></span>

![img](https://main.qcloudimg.com/raw/63a72957d094f247f694f9e3f3c69034.png)

#### ServiceGroup

- ServiceGroup 包含一个或者多个业务服务。
- 适用场景
  - 业务需要打包部署。
  - 业务需要在每一个 NodeUnit 中均运行起来并且保证pod数量。
  - 业务需要将服务之间的调用控制在同一个 NodeUnit 中，不能将流量转发到其他 NodeUnit。

> ! ServiceGroup 是一种抽象资源，一个集群中可以创建多个 ServiceGroup。

#### NodeUnit

- NodeUnit 通常是位于同一边缘站点内的一个或多个计算资源实例，需要保证同一 NodeUnit 中的节点内网是通的。
- ServiceGroup 组中的服务运行在一个 NodeUnit 之内。
- TKE Edge 允许用户设置服务在一个 NodeUnit 中运行的 Pod 数量。
- TKE Edge 能够把服务之间的调用限制在本 NodeUnit 内。

#### NodeGroup

- NodeGroup 包含一个或者多个 NodeUnit。
- 保证在集合中每个 NodeUnit 上均部署 ServiceGroup 中的服务。
- 集群中增加 NodeUnit 时自动将 ServiceGroup 中的服务部署到新增 NodeUnit。

### 2. 涉及的资源类型

#### DepolymentGrid

DeploymentGrid 的格式与 Deployment 类似，`deployment-template` 字段为原先 Deployment 的 `template` 字段，比较特殊的是 `gridUniqKey` 字段，该字段指明了节点分组的 label 的 key 值。示例如下：

```
apiVersion: tkeedge.io/v1
kind: DeploymentGrid
metadata:
  name:
  namespace:
spec:
  gridUniqKey: <NodeLabel Key>
  <deployment-template>
```

#### ServiceGrid

ServiceGrid 的格式与 Service 类似，`service-template` 字段为原先 Service 的 `template` 字段，比较特殊的是 `gridUniqKey` 字段，该字段指明了节点分组的 label 的 key 值。示例如下：

```
apiVersion: tkeedge.io/v1
kind: ServiceGrid
metadata:
  name:
  namespace:
spec:
  gridUniqKey: <NodeLabel Key>
  <service-template>
```

### 3. 操作步骤

以在边缘部署 nginx 为例。若您希望在多个节点组内分别部署 nginx 服务，需依次执行以下步骤：

#### 1. 确定 ServiceGroup 唯一标识

这一步是逻辑规划，不需要做任何实际操作。边缘容器将目前要创建的 ServiceGroup 逻辑标记使用的 UniqKey 设置为：zone。

#### 2. 通过 Label 将边缘节点分组<span id="Step2"></span>

该步骤需要通过 TKE Edge 控制台或者 kubectl 对边缘节点打 Label。其中，TKE Edge 控制台操作步骤如下：

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的【边缘集群】。

2. 单击需要编辑标签的节点所在的集群 ID，进入该集群管理页面。

3. 单击【节点管理】>【节点】，进入节点列表页，如下图所示：
   ![](https://main.qcloudimg.com/raw/712450952968557eefd23e4833deaa5f.png)

4. 单击需要编辑标签的节点所在行最右侧的“更多”，在展开的下拉菜单选择“编辑标签”。

5. 在弹出的“编辑标签”窗口，按需新增 Label，如下图所示：
   ![](https://main.qcloudimg.com/raw/09c92b66ba8b36aa763c54c75fa07c76.png)
   
   - 借鉴 [整体架构](#OverallStructure) 章节中的图，我们选定 Node12、Node14，编辑 Label：`zone=nodeunit1`；Node21、Node23 编辑 Label：`zone=nodeunit2`。
   - 上条中 Label 的 key 需与 ServiceGroup 的 UniqKey 一致，value 是 NodeUnit 的唯一key，value 相同的节点表示属于同一个 NodeUnit。
   - 如果同一个集群中有多个 ServiceGroup，请为每一个 ServiceGroup 分配不同的 Uniqkey。
   
6. 单击【确定】即可。

#### 部署 DeploymentGrid

```
apiVersion: tkeedge.io/v1
kind: DeploymentGrid
metadata:
  name: deploymentgrid-demo
  namespace: default
spec:
  gridUniqKey: zone
  template:
    selector:
      matchLabels:
        appGrid: nginx
    replicas: 2
    template:
      metadata:
        labels:
          appGrid: nginx
      spec:
        containers:
        - name: nginx
          image: nginx:1.7.9
          ports:
          - containerPort: 80
```

#### 部署 ServiceGrid

```
apiVersion: tkeedge.io/v1
kind: ServiceGrid
metadata:
  name: servicegrid-demo
  namespace: default
spec:
  gridUniqKey: zone
  template:
    selector:
      appGrid: nginx
    ports:
    - protocol: TCP
      port: 80
      targetPort: 80
```

可以看到此处 gridUniqKey 字段设置为了 zone，因此对应到 [通过 Label 将边缘节点分组](#Step2) 步骤中对节点进行分组时 Label 的 key 也应设置为 zone。如果有三组节点，分别为他们添加 `zone: zone-0`，`zone: zone-1 `，`zone: zone-2 `的 Label 即可。

这时，每组节点内都有了 nginx 的 Deployment 和对应的 Pod，在节点内访问统一的 service-name 也只会将请求发向本组的节点。验证方式如下：

```
[root@VM_1_34_centos ~]# kubectl get deploy
NAME                         READY   UP-TO-DATE   AVAILABLE   AGE
deploymentgrid-demo-zone-0   2/2     2            2           85s
deploymentgrid-demo-zone-1   2/2     2            2           85s
deploymentgrid-demo-zone-2   2/2     2            2           85s
 
[root@VM_1_34_centos ~]# kubectl get svc
NAME                   TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
kubernetes             ClusterIP   172.19.0.1     <none>        443/TCP   87m
servicegrid-demo-svc   ClusterIP   172.19.0.177   <none>        80/TCP    80s
```

另外，对于部署了 DeploymentGrid 和 ServiceGrid 后才添加进集群的节点组，该功能会在新的节点组内自动创建指定的 Deployment 和 Service。

## 常规方案<span id="step1"></span>

### 1. 将服务限制在一个节点内
![img](https://main.qcloudimg.com/raw/fd24574574aff2e247684a755038bb5b.jpg)

该方案具备以下特点：

- 服务以 DaemonSet 方式部署，以便每个边缘节点上均有所有服务的 Pod 副本。如上图所示，集群内有 A、B 两个服务，以 DaemonSet 方式部署后每个边缘节点上均有一个 Pod-A 和 Pod-B。
- 服务通过 localhost 访问，以便将调用链锁定在同一个节点内。如上图所示，Pod-A 和 Pod-B 之间以 localhost 访问。

> !
> - 由于 DaemonSet 工作机制所限，每个服务在同一个节点内只能有一个 Pod。对于需要在同一节点上运行多个 Pod 的服务极为不便。
> - Pod 需要使用 hostnetWork 模式，以便 Pod 之间可以通过 localhost+port 访问。这意味着用户需要很好地管理服务对资源使用，以避免出现资源竞争，如端口竞争。

### 2. 相同服务在不同站点设置不同名字

![img](https://main.qcloudimg.com/raw/402199fd8502b09387ec3879c873a4e2.jpg)

该方案具备以下特点：

- 相同服务在不同站点设置为不同的名字，以便将服务间的访问锁定在同一个站点内。如上图所示，集群内有 A、B 两个服务，在 site-1中分别命名为 Svr-A-1、Svc-B-1，在 site-2中分别命名为 Svr-A-2、Svc-B-2。

> ! 服务在不同站点名字不同，因而服务之间不能简单地通过服务名 A 和 B 来调用，而是在 site-1中用 Svc-A-1、Svc-B-1，在 site-2中用 Svc-A-2、Svc-B-2。对于借助 Kubernetes DNS 实现微服务的业务极为不友好。

### 3. 方案痛点

**1. Kubernetes 本身并不支持直接针对这种场景提供方案**

- 众多地域部署问题。通常，一个边缘集群会管理许多个边缘站点（每个边缘站点内有一个或多个计算资源），中心云场景往往是一些大地域的中心机房，边缘地域相对中心云场景地域更多，也许一个小城市就有一个边缘机房，地域数量可能会非常多；在原生 Kubernetes 中，Pod 的创建很难指定，除非使用节点亲和性针对每个地域进行部署，但是如果地域数量有十几个甚至几十个，以需要每个地域部署多个服务的 Deployment 为例，需要各个 Deployment 的名称和 selector 各不相同，几十个地域，意味着需要上百个对应的不同name，selector，pod labels 以及亲和性的部署 yaml，单单是编写这些yaml工作量就非常巨大。
- Services 服务需要与地域关联。例如音视频服务中的转码和合成服务，要在所属地域内完成接入的音视频服务，用户希望服务之间的相互调用能限制在本地域内，而不是跨地域访问。这同样需要用户同样准备上百个不同 selector 和 name 的本地域 Deployment 专属的 Service 的部署 yaml。
- 如果用户程序中服务之间的相互访问使用了 Service 名，那么当前环境下，由于 Service 的名称各个地域都不相同，对于用户而言，原来的应用甚至都无法工作，需要针对每个地域单独适配，复杂度太高。

**2. 使用方为了让容器化的业务在调度方案上与之前运行在虚拟机或者物理机上的业务保持一致，他们很自然就想到为每个 Pod 分配一个公网 IP，然而公网 IP 数量明显是不够用的。**

综上所述，原生 Kubernetes 虽然可以变相满足需求1，但是实际方案非常复杂，对于需求2则没有好的解决方案。因此为解决上述痛点，TKE Edge 开创性地提出和实现了 serviceGroup 特性，两个 yaml 文件即可轻松实现即使上百地域的服务部署，且无需应用适配或改造。
