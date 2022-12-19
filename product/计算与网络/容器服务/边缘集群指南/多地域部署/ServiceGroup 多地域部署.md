
##  功能特点

- 边缘计算场景中，往往会在同一个集群中管理多个边缘站点，每个边缘站点内有一个或多个计算节点。
- 同时希望在每个站点中都运行一组有业务逻辑联系的服务，每个站点内的服务是一套完整的功能，可以为用户提供服务。
- 由于受到网络限制，有业务联系的服务之间不希望或者不能跨站点访问。

由于以上边缘计算的 3 个特点，腾讯云边缘容器专门设计了一套 ServiceGroup 的自定义资源逻辑，来解决边缘容器在多地域场景下遇到的应用分发和服务治理的问题。


## 操作场景

ServiceGroup 可以便捷地在共属同一个集群的不同机房或区域中各自部署一组服务，并且使得各个服务间的请求在本机房或本地域内部即可完成，避免服务跨地域访问。

原生 Kubernetes 无法控制 Deployment 的 Pod 创建的具体节点位置，需要通过统筹规划节点的亲和性来间接完成。当边缘站点数量以及需要部署的服务数量过多时，管理和部署方面的极为复杂，甚至仅存在理论上的可能性。与此同时，为了将服务间的相互调用限制在一定范围，业务方需要为各个 Deployment 分别创建专属的 Service，管理方面的工作量巨大且极容易出错并引起线上业务异常。

ServiceGroup 针对此场景设计，用户仅需使用 ServiceGroup 提供的 DeploymentGrid 和 ServiceGrid 两种 TKE Edge 自研 Kubernetes 资源，即可方便地将服务分别部署到这些节点组中，并进行服务流量管控，同时还可保证各区域服务数量及容灾。

本文仅以一个实现案例，来说明 ServiceGroup 的使用方式，如果需要探究深入的细节，请参考文档 [ServiceGroup 深入详解](https://cloud.tencent.com/document/product/457/83217)。

## 关键概念

### 整体架构

<div align="left">
  <img src="https://qcloudimg.tencent-cloud.cn/raw/3630448a967c07e0d09ccf3fd84e60c6.jpg" width=80% title="service-group">
</div>

### 基本概念

ServiceGroup 需要和 NodeUnit 以及 NodeGroup 结合使用，概念详情如下：

#### NodeUnit（边缘节点池）



- NodeUnit 通常是位于同一边缘站点内的一个或多个计算资源实例，需要保证同一 NodeUnit 中的节点内网是通的。
- ServiceGroup 组中的服务运行在一个 NodeUnit 之内。
- ServiceGroup 允许用户设置服务在一个 NodeUnit 中运行的 pod 数量。
- ServiceGroup 能够把服务之间的调用限制在本 NodeUnit 内。
更多内容可参考 [边缘节点池](https://cloud.tencent.com/document/product/457/72680)。

#### NodeGroup（边缘节点池分类）

- NodeGroup 包含一个或者多个 NodeUnit。
- 保证在集合中每个 NodeUnit 上均部署 ServiceGroup 中的服务。
- 集群中增加 NodeUnit 时自动将 ServiceGroup 中的服务部署到新增 NodeUnit。
更多内容可参考 [节点池分类](https://cloud.tencent.com/document/product/457/72684)。

#### ServiceGroup
ServiceGroup 并不是一个实体的资源定义，是集中 Kubernetes 自定义资源的集合。ServiceGroup 是一种抽象资源，一个集群中可以创建多个 ServiceGroup。

ServiceGroup 包含一个或者多个业务服务。适用场景如下：
- 业务需要打包部署。
- 业务需要在每一个 NodeUnit 中运行起来并且保证 pod 数量。
- 业务需要将服务之间的调用控制在同一个 NodeUnit 中，不能将流量转发到其他 NodeUnit。
 
ServiceGroup 涉及的资源类型包括如下三类：
<dx-tabs>
:::  DeploymentGrid

DeploymentGrid 的格式与 Deployment 类似，<deployment-template>字段就是原先 deployment 的 template 字段，比较特殊的是 gridUniqKey 字段，该字段指明了节点分组的 label 的 key 值：

```yaml
apiVersion: superedge.io/v1
kind: DeploymentGrid
metadata:
  name:
  namespace:
spec:
  gridUniqKey: <NodeLabel Key>
  <deployment-template>
```
:::
::: StatefulSetGrid

StatefulSetGrid 的格式与 StatefulSet 类似，<statefulset-template>字段就是原先 statefulset 的 template 字段，比较特殊的是 gridUniqKey 字段，该字段指明了节点分组的 label 的 key 值：

```yaml
apiVersion: superedge.io/v1
kind: StatefulSetGrid
metadata:
  name:
  namespace:
spec:
  gridUniqKey: <NodeLabel Key>
  <statefulset-template>
```
:::
::: ServiceGrid

ServiceGrid 的格式与 Service 类似，<service-template>字段就是原先 service 的 template 字段，比较特殊的是 gridUniqKey 字段，该字段指明了节点分组的 label 的 key 值：

```yaml
apiVersion: superedge.io/v1
kind: ServiceGrid
metadata:
  name:
  namespace:
spec:
  gridUniqKey: <NodeLabel Key>
  <service-template>
```
:::
</dx-tabs>


##  操作步骤

以在边缘部署 Nginx 服务为例，我们希望在多个节点池内分别一套完整的 Nginx 服务，需要如下操作：


### 将边缘节点分组

我们以一个边缘集群为例，将集群中的节点添加到**边缘节点池**以及**节点池分类**中。

- 此集群包含 5 个边缘节点，分别位于 `beijing` `guangzhou` 2 个地域，节点名为`bj-1`、`bj-2`、`gz-1`、`gz-2`、`gz-3`。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/6d891bdd009188e331bf8ca934c206ed.jpg)

- 分别创建 2 个 NodeUnit（边缘节点池）：`beijing`、`guangzhou`，分别将相应的节点加入对应的 NodeUnit（边缘节点池）中，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/02066248b66aeb71959bbfcca0ad0c85.jpg)
 
- 创建名称为 `location` 的 NodeGroup（边缘节点池分类），将`beijing`、`guangzhou` 这两个边缘节点池划分到`location`这个分类中，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/04879e4f0917b56ddcb7342ae3cb35e8.png)
 
进行上述操作后，每个节点上会被打上相应的标签，节点 gz-2 的标签如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/66a28a98c5c92b70dc23dce6b070b922.jpg)
 
>?
>- label 的 key 就是 NodeGroup 的名字，value 是 NodeUnit 的名字，value 相同的节点表示属于同一个 NodeUnit。
>- 如果同一个集群中有多个 NodeGroup 请创建不同的 NodeGroup 名字作为唯一标记，部署 ServiceGroup 相关资源的时候会通过 NodeGroup 的名字这个唯一标记来绑定指定的 NodeGroup 进行部署。

### 无状态 ServiceGroup

#### 部署 DeploymentGrid
1. 选择**ServiceGroup**->**DeploymentGrid**，进入列表页。
![](https://qcloudimg.tencent-cloud.cn/raw/2e25e98f738cf1ee4bde042ec343edea.jpg)
2. 单击**新建**，创建名称为`Nginx`的**DeploymentGrid**。
![](https://qcloudimg.tencent-cloud.cn/raw/dcdea0ddca3791ae8e9d604d5b48ef5d.jpg)
  - **NodeGroup**： 这里选择需要批量部署 Nginx 服务的 NodeGroup 分组；这里选择 location，意味着将会在`beijing`和`guangzhou`两个 NodeUnit 下分别部署相应的 Deployment
  - **其余参数**：其余参数和 TKE 部署应用的方式完全一致，这里不再详述；这里作为示例，实例数量设置为了3。
3. 单击**创建 DeploymentGrid**，等待部署完成。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/9364f5a27789525aebc759636d372b34.jpg)
4. 单击**nginx**链接，进入详情页，可以查看具体创建的**Deployment 详情**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/c576b1f551ca182ea9e725b56c201d46.jpg)
>? 平台在 NodeGroup 包含的每个 NodeUnit 下都分别创建了一个 Kubernetes 标准的 Deployment，名字为**DeploymentGrid-NodeUnit**。
> 根据示例，此处示例名分别为`nginx-beijing`和`nginx-guangzhou`。

#### 部署 ServiceGrid

1. 选择**ServiceGroup**->**ServiceGrid**，单击**新建**，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/2a3fbcd8b5951437ed9b6485f7922aca.jpg)
  - **NodeGroup**：选择需要的 NodeGroup，和上面的 DeploymentGrid 选择一样的 NodeGroup。
  - **设置访问**：标准 Kubernetes 的 Sevice 配置信息，选择需要的端口，这里 nginx 服务默认是 80。
  - **Workload 绑定**：选择 Service 通过 Seletor 选择需要的 Pod，可以手动输入添加；也可以选择`引用 Workload`添加已部署的 DeploymentGrid > nginx。
2. 单击**创建 ServiceGrid**，创建成功，显示事件详情页。
3. 在**服务** > **Service**中查看具体创建出来的`Service`信息，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/1752a699d98c5576707c81db88dbddf9.jpg)
4. 通过使用`nginx-svc`这个 Service，能够实现下面的目的：
   - 从`beijing`地域的 Pod 中访问此 svc，后端只会访问到`beijing`地域的 3 个 pod 中。
   - 从`guangzhou`地域的 Pod 中访问此 svc，后端只会访问到`guangzhou`地域的 3 个 pod 中。
  每个地域访问这个Service 都会被限制在本 NodeUnit 范围内

>? 此文档仅简单描述 `ServiceGroup` 的使用方式，如果想要了解详情，请参考文档 [ServiceGroup 深入详解](https://cloud.tencent.com/document/product/457/83217)。
