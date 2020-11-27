## 背景知识

前文介绍了ServiceGroup设计思想（[最佳实践：边缘容器 serviceGroup 功能](https://cloud.tencent.com/document/product/457/46923)），以及如何通过yaml管理资源，本文将介绍如何通过控制台管理serviceGroup资源.

 


## 创建 DeploymentGrid 资源
### 新建 DeploymentGrid
1. 登录容器服务控制台，选择左侧导航栏中的【[边缘集群](https://console.cloud.tencent.com/tke2/edge?rid=1)】。
2. 在“边缘集群”页面单击需要创建 DeploymentGrid 资源的集群 ID，进入待创建 DeploymentGrid 的边缘集群管理页面。
3. 选择【ServiceGroup】>【DeploymentGrid】，进入 “DeploymentGrid” 管理页面。
4. 单击【新建】，进入 “新建DeploymentGrid” 页面。如下图所示：
![](https://main.qcloudimg.com/raw/d8ea1886b686a835cb4241b9c1943b37.png)
  根据实际需求，设置 DeploymentGrid 参数。关键参数信息如下：
 - 工作负载名：DeploymentGrid 资源名。
 - NodeGroup：新建资源绑定的 NodeGroup。填写已有的 NodeGroup 将会自动产生关联，否则将新建一个 NodeGroup。
 - 实例内容器：需输入 Container 相关信息。
5. 单击【创建DeploymentGrid】，完成创建。


第三步，查看资源

![图形用户界面, 应用程序  描述已自动生成](file:///C:/Users/V_XIXI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image006.png)

DeploymentGrid 列表中出现刚才创建的名为ngx的对象

 

![图形用户界面, 应用程序  描述已自动生成](file:///C:/Users/V_XIXI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image008.png)

NodeGroup 列表中出现创建 ngx 时填写的 zone1

 

**管理** **NodeGroup**

第一步，点击 ”zone1“，进入NodeGroup管理页面

![图形用户界面, 应用程序  描述已自动生成](file:///C:/Users/V_XIXI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image009.png)

 

第二步，在名为 zone1 的NodeGroup下添加NodeUnit

![图形用户界面, 应用程序  描述已自动生成](file:///C:/Users/V_XIXI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image011.png)

第一个红框，指定NodeUnit名字，如图中的 sc

第二个红框，往sc中绑定节点

 

注意，一个NodeGroup下可以有多个NodeUnit，通常同一个NodeUnit中的节点位于相同的内网，因为serviceGrid资源中的服务组会将流量限定在同一个NodeUnit所绑定的节点中

 

第三步，管理NodeUnit

![图形用户界面, 应用程序  描述已自动生成](file:///C:/Users/V_XIXI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image013.png)

 

**创建** **serviceGrid****资源**

第一步，入口

![图形用户界面, 应用程序  描述已自动生成](file:///C:/Users/V_XIXI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image015.png)

 

第二步，新建 serviceGrid

![图形用户界面, 文本, 应用程序, 电子邮件  描述已自动生成](file:///C:/Users/V_XIXI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image017.png)

第一个红框，说明这个 serviceGrid 对象将会与 zone1 这个 nodeGroup 建立关联关系

第二个红框，这个serviceGrid将与哪个DeploymentGrid绑定，推荐大家使用 ”引用DeploymentGrid“方式。

目前点击 ”引用DeploymentGrid“时展示出来的可选DeploymentGrid尚未根据 NodeGroup 值做筛选，请务必人工筛选一下，确保绑定的DeploymentGrid也是关联相同的NodeGroup。

 

第三步，查看资源

![图形用户界面, 应用程序  描述已自动生成](file:///C:/Users/V_XIXI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image019.png)

也可以修改 ngx 的设置



![图形用户界面, 应用程序  描述已自动生成](file:///C:/Users/V_XIXI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image021.png)

 

请务必注意，目前只支持修改 ”GridUniqKey“ 和 "Ports" 两个字段。GridUniqKey亦即创建serviceGroup时的 NodeGroup 值

![文本  描述已自动生成](file:///C:/Users/V_XIXI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image023.png)

操作解读

**编排和调度**

我们创建了ngx这种deploymentGrid资源对象，该对象与名为zone1的NodeGroup关联在一起。然后在zone1下面创建了sc、xj两个NodeUnit，并且分别在sc中绑定了2个节点，在xj中绑定了1个节点。做完这些操作后进入 ”工作负载-Deployment“列表页，我们可以看到出现了两个deployment，分别为 ngx-sc、ngx-xj

![图形用户界面, 应用程序  描述已自动生成](file:///C:/Users/V_XIXI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image024.png)

 

点击进入 ngx-sc后还可以看到，ngx-sc的pod全部运行在sc的2个节点上，ngx-xj的pod全部运行在xj的1个节点上。

如果在NodeGroup中增加一个NodeUnit名为abc，我们可以看到在会自定新增一个名为ngx-abc的deployment，并且ngx-abc的pod也会全部运行在abc绑定的节点上

如果在NodeGroup中修改NodeUnit名为abc中绑定的节点，比如增加、删除节点，我们可以看到 ngx-abc的pod 有可能触发调度，最终一定会保证运行在abc绑定的节点上

如果在NodeGroup中删除名为abc的NodeUnit，我们可以看到 ngx-abc这个deployment自动消失了

这就是serviceGroup的第一个能力

**流量闭环**

我们还创建了 ngx这种serviceGrid资源对象，该对象也与名为zone1的NodeGroup关联在一起。做完这个操作我们进入 ”服务-Service“列表页可以看到出现一个名为ngx-svc的Service对象

![图形用户界面, 应用程序  描述已自动生成](file:///C:/Users/V_XIXI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image026.png)

这意味着名为 ngx-svc 这个svc的流量会限制在每个 NodeUnit 内部，为了更直观地理解这一点，我们可以尝试在名为sc的NodeUnit所绑定的节点上随意找一个pod，在pod中请求ngx-svc。我们将发现，所有的请求均落在ngx-sc这个deployment对应的pod上。我们再在

xj做同样的操作，同样可以看到请求全部会落在 ngx-xj对应的pod上。

这是serviceGroup的另一个能力，将微服务之间的调用闭环在同一个NodeUnit中。设计这个能力的原因是，在一个边缘集群中经常需要管理多个机房的节点，同一个机房内的节点网络可达，机房之间不可达，因此必须将微服务之间的调用控制在同一个机房内。为了更加通用，我们将流量控制在一个 NodeUnit内。

 

如何借助serviceGroup部署边缘微服务

1、假设我们的微服务有 svc-a、svc-b、svc-c，服务间存在调用关系或服务需要一起部署，对应的是deployment-a、deployment-b、deployment-c。

2、分别创建deploymentGrid-a、deploymentGrid-b、deploymentGrid-c，并且关联相同的 NodeGroup，假设名为 service-group-1

3、创建serviceGrid-a、serviceGrid-b、serviceGrid-c，关联service-group-1，分别绑定deploymentGrid-a、deploymentGrid-b、deploymentGrid-c

4、在service-group-1中管理NodeUnit及各NodeUnit下的机器节点。

做完上述操作后，我们就实现每个 NodeUnit 中的a、b、c的调用流量在本 NodeUnit中闭环的效果。

值得注意的是，服务间的调用不能使用原来的svc-a、svc-b、svc-c，而是使用 svc-a-svc、svc-b-svc、svc-c-svc，在原来的servicename后面增加了 '-svc' 字符串

 
