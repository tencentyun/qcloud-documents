
[边缘容器 ServiceGroup 功能](https://cloud.tencent.com/document/product/457/46923) 介绍了 ServiceGroup 设计思想，以及如何 [通过 yaml](https://cloud.tencent.com/document/product/457/50417) 管理资源，本文将介绍如何通过控制台管理 ServiceGroup 资源。

 


## 通过控制台使用 ServiceGroup 功能
### 新建 DeploymentGrid 资源[](id:step1)
1. 登录容器服务控制台，选择左侧导航栏中的 **[边缘集群](https://console.cloud.tencent.com/tke2/edge?rid=1)**。
2. 在“边缘集群”页面单击需要创建 DeploymentGrid 资源的集群 ID，进入边缘集群管理页面。
3. 选择边缘集群左侧菜单中的**ServiceGroup** > **DeploymentGrid**，进入 “DeploymentGrid” 管理页面。
4. 单击**新建**，进入 “新建DeploymentGrid” 页面。如下图所示：
![](https://main.qcloudimg.com/raw/d8ea1886b686a835cb4241b9c1943b37.png)
  根据实际需求，设置 DeploymentGrid 参数。关键参数信息如下：
 - **工作负载名**：DeploymentGrid 资源名。
 - **NodeGroup**：新建资源绑定的 NodeGroup。填写已有的 NodeGroup 将会自动产生关联，否则将新建一个 NodeGroup。
 - **实例内容器**：需输入 Container 相关信息。
5. 单击**创建DeploymentGrid**，完成创建。
6. 创建成功后，在 “DeploymentGrid” 管理页面即可查看已新建的 DeploymentGrid 对象。在 “NodeGroup” 管理页面即可查看创建 DeploymentGrid 时填写的 NodeGroup 对象。

 
### 管理 NodeGroup[](id:step2)
1. 登录容器服务控制台，选择左侧导航栏中的 **[边缘集群](https://console.cloud.tencent.com/tke2/edge?rid=1)**。
2. 单击需要管理 NodeGroup 的集群 ID，进入该集群详情页。
3. 选择边缘集群左侧菜单中的**ServiceGroup** > **NodeGroup**，进入 “NodeGroup” 管理页面。
4. 选择需要管理 NodeGroup 的名称，进入 NodeUnit 列表页面，单击**新建NodeUnit**。
5. 在弹出的**添加NodeUnit**窗口中，按需选择 NodeUnit 的名称和节点。如下图所示：
![](https://main.qcloudimg.com/raw/bac9249de8649aded5e3071ff70ef9a1.png)
 - **名称**：自定义 NodeUnit 的名称。
 - **节点**：向自定义 NodeUnit 中添加节点。
 >! 一个 NodeGroup 下可以有多个 NodeUnit，通常同一个 NodeUnit 中的节点位于相同的内网，ServiceGrid 资源中的服务组会将流量限定在同一个 NodeUnit 所绑定的节点中。
6. 单击**确定**，完成创建 NodeUnit。创建成功后，即可在 NodeUnit 列表页面进行查看。


### 新建 ServiceGrid 资源[](id:step3)
1. 登录容器服务控制台，选择左侧导航栏中的 **[边缘集群](https://console.cloud.tencent.com/tke2/edge?rid=1)**。
2. 单击需要新建 ServiceGrid 资源的集群 ID，进入该集群详情页。
3. 选择边缘集群左侧菜单中的**ServiceGroup** > **ServiceGrid**，进入 “ServiceGrid” 管理页面。
4. 单击**新建**，进入 “新建ServiceGrid” 页面。如下图所示：
![](https://main.qcloudimg.com/raw/aad8ffe4689da6efcdf97c4de1ba2d68.png)
主要参数信息如下：
 - **NodeGroup**：新建 ServiceGrid 对象将与选中的 NodeGroup 建立关联关系。
 - **DeploymentGrid绑定（选填）**：新建 ServiceGrid 对象将与选中的 DeploymentGrid 绑定。推荐使用 “引用DeploymentGrid”。
 >! 在弹出的“引用DeploymentGrid” 窗口中，需根据 NodeGroup 值进行人工筛选，以确保与绑定的 DeploymentGrid 关联相同的 NodeGroup。
5. 单击**创建ServiceGrid**，完成创建。
  创建成功后，在 “ServiceGrid” 管理页面即可查看已新建的 ServiceGrid 对象，也可通过**编辑YAML**对 ServiceGrid 资源进行修改。
>!  目前只支持修改 ”GridUniqKey“ 字段和 ”Ports“ 字段。”GridUniqKey“ 即创建 ServiceGroup 时的 NodeGroup 值。




## 测试验证
该步骤验证 ServiceGroup 功能是否具备编排调度与流量闭环的能力。


### 编排调度
1. 参考 [新建 DeploymentGrid 资源](#step1)，创建对象 `ngx`。
2. 参考 [管理 NodeGroup](#step2)，创建对象 `zone1`，并与 DeploymentGrid 资源 `ngx` 关联。
3. 在 `zone1` 中创建两个 NodeUnit，分别为 `sc`、`xj`。在 `sc` 中绑定2个节点，在 `xj` 中绑定1个节点。

完成以上操作后进入**工作负载** > **Deployment**页面，“Deployment” 管理页面将出现 `ngx-sc`、`ngx-xj`。如下图所示：
![](https://main.qcloudimg.com/raw/edea6b5a4844703c89fd4c335de5b50a.png)

单击 `ngx-sc` 进入 “Pod 管理页面” 后可看到，`ngx-sc` 的 Pod 全部运行在 `sc` 的2个节点上。同理，`ngx-xj` 的 Pod 全部运行在 `xj` 的1个节点上。

- 如果在 NodeGroup 中增加 NodeUnit 命名为 `abc`，则 Deployment 管理页中将新增 `ngx-abc`，并且 `ngx-abc` 的 Pod 也会全部运行在 `abc` 绑定的节点上。
- 如果在 NodeGroup 中修改 `abc` 绑定的节点，例如增加、删除节点，则可以看到 `ngx-abc` 的 Pod 有可能触发调度，最终一定会保证运行在 `abc` 绑定的节点上。
- 如果在 NodeGroup 中删除 `abc`，则在 Deployment 管理页中 `ngx-abc` 自动消失。





### 流量闭环
在 [新建 ServiceGrid 资源](#step3) 中，创建 ServiceGrid 对象 `ngx`。该对象也与名为 `zone1` 的 NodeGroup 相关联。

完成以上操作后进入**服务** > **Service**页面，“Service” 管理页面将出现 `ngx-svc`。如下图所示：
![](https://main.qcloudimg.com/raw/f66fab3f7014b90cca685c35e576de1b.png)

这表明名为 `ngx-svc` 的流量会限制在每个 NodeUnit 内部。例如，在 NodeUnit `sc` 的绑定节点上任意找一个 Pod，在 Pod 中请求 `ngx-svc`，所有的请求将均落在 Deployment `ngx-sc` 对应的 Pod 上。同理，在 `xj` 进行相同操作，可查看请求全部落在 `ngx-xj` 对应的 Pod 上。

ServiceGroup 的流量闭环能力将微服务之间的调用闭环在同一个 NodeUnit 中。在以下场景中适用：
在一个边缘集群中经常需要管理多个机房的节点，同一个机房内的节点网络可达，机房之间不可达，需将微服务之间的调用控制在同一个机房内。为了使 ServiceGroup 功能更加通用，可将流量控制在一个 NodeUnit 内。

 
## 使用示例 
### 使用 ServiceGroup 部署边缘微服务

1. 假设微服务有 svc-a、svc-b、svc-c，服务间存在调用关系或服务需要一起部署，对应的是 deployment-a、deployment-b、deployment-c。
2. 分别创建 deploymentGrid-a、deploymentGrid-b、deploymentGrid-c，并且关联相同的 NodeGroup，假设名为 service-group-1。
3. 创建 serviceGrid-a、serviceGrid-b、serviceGrid-c，关联 service-group-1，分别绑定 deploymentGrid-a、deploymentGrid-b、deploymentGrid-c。
4. 在 service-group-1 中管理 NodeUnit 及各 NodeUnit 下的机器节点。

完成上述操作后，即可实现每个 NodeUnit 中的 a、b、c 的调用流量在本 NodeUnit 中闭环。
>! 服务间的调用不能使用原来的 svc-a、svc-b、svc-c，而是使用 svc-a-svc、svc-b-svc、svc-c-svc，需在原来的 servicename 后面增加 `-svc` 字符串。

 
