## 功能介绍
Capacity Scheduler 是容量调度器，容量调度器以分层的方式组织资源，可通过多层级的资源限制条件让多用户共享集群资源。
## 操作步骤
### 新建资源池
1. 登录 [EMR 控制台](https://console.cloud.tencent.com/emr)，在集群列表中选择对应的 Hadoop 集群单击**详情**进入集群详情页。
2. 在集群详情页中选择**集群服务 > Yarn 组件卡页**右上角**操作 > 资源调度**进入资源调度页面。
![](https://qcloudimg.tencent-cloud.cn/raw/78a4bccadd9d4742136b7218990f4c67.png)
3. 单击**资源调度器开关**，打开开关后即可进行相关调度器配置。
4. 新建 Capacity Scheduler
调度策略类型选择 Capacity Scheduler 即可进入 Capacity Scheduler 的配置页面，单击**新增资源池**即可新建资源池。可对已有资源池进行编辑、新建子池、克隆等操作；也可单击**默认设置**进行设置容量调度的延迟调度次数。
![](https://qcloudimg.tencent-cloud.cn/raw/ebd586bfaf076ad20371fd51f36cfd8a.png)
![](https://qcloudimg.tencent-cloud.cn/raw/bcac9b4049798553d81831ac70787549.png)
**字段与配置项对照表**：
<table>
<thead>
<tr>
<th>字段名称</th>
<th>对应参数名称</th>
<th>参数含义</th>
</tr>
</thead>
<tbody><tr>
<td>资源池名称</td>
<td>yarn.scheduler.capacity.&lt;queue-path>.queues&lt;/queue-path></td>
<td>资源池的名称或队列的名称。</td>
</tr>
<tr>
<td>标签设置</td>
<td>无</td>
<td>设置队列可以访问的特定标签。</td>
</tr>
<tr>
<td>容量</td>
<td>yarn.scheduler.capacity.&lt;queue-path>.capacity&lt;/queue-path></td>
<td>可以使用的资源大小，同一父资源池的子池容量总和为100，能使用的资源=父资源池*容量%。如果该队列需要比这个比例更高的资源，而其他队列又有空闲资源的话，可以占用比这个比例更高的资源。</td>
</tr>
<tr>
<td>最大容量</td>
<td>yarn.scheduler.capacity.&lt;queue-path>.maximum-capacity&lt;/queue-path></td>
<td>队列的资源使用上限（百分比）。由于存在资源共享，因此一个队列使用的资源量可能超过其容量，而最多使用资源量可通过该参数限制。</td>
</tr>
<tr>
<td>默认标签表达式</td>
<td>yarn.scheduler.capacity.&lt;queue-path>.default-node-label-expression&lt;/queue-path></td>
<td>当资源请求未指定节点标签时，应用将被提交到该值对应的分区。默认情况下，该值为空，即应用程序将被分配没有标签的节点上的容器。</td>
</tr>
<tr>
<td>用户最小容量</td>
<td>yarn.scheduler.capacity.&lt;queue-path>.minimum-user-limit-percent&lt;/queue-path></td>
<td>每个用户最低资源保障（百分比）。任何时刻，一个队列中每个用户可使用的资源量均有一定的限制。当一个队列中同时运行多个用户的应用程序时，每个用户的使用资源量在一个最小值和最大值之间浮动，其中，最小值取决于正在运行的应用程序数目，而最大值则由 minimum-user-limit-percent 决定。</td>
</tr>
<tr>
<td>用户资源因子</td>
<td>yarn.scheduler.capacity.&lt;queue-path>.user-limit-factor&lt;/queue-path></td>
<td>每个用户最多可使用的资源量（百分比）。例如，假设该值为30，则任何时刻，每个用户使用的资源量不能超过该队列容量的30%。</td>
</tr>
<tr>
<td>分配 Container 最大内存数量</td>
<td>yarn.scheduler.capacity.&lt;queue-path>.maximum-allocation-mb&lt;/queue-path></td>
<td>每个 container 的最大内存值，这个配置会覆盖 yarn.scheduler.maximum-allocation-mb 值，但是该值必须小于等于系统的 yarn.scheduler.maximum-allocation-mb 的值。</td>
</tr>
<tr>
<td>Container 最大 vCore 数量</td>
<td>yarn.scheduler.capacity.&lt;queue-path>.maximum-allocation-vcores&lt;/queue-path></td>
<td>每个 container 的最大核数，这个配置会覆盖 yarn.scheduler.maximum-allocation-vcores 值，但是该值必须小于等于系统的 yarn.scheduler.maximum-allocation-vcores 的值。</td>
</tr>
<tr>
<td>资源池状态</td>
<td>yarn.scheduler.capacity.&lt;queue-path>.state&lt;/queue-path></td>
<td>队列的状态。可以是正在运行或已停止。如果队列处于停止状态，则无法向其自身或其任何子队列提交新的应用程序。</td>
</tr>
<tr>
<td>最大应用数 Max-Applications</td>
<td>yarn.scheduler.capacity.&lt;queue-path>.maximum-applications&lt;/queue-path></td>
<td>系统中可同时处于活动状态（正在运行和挂起）的最大应用程序数。</td>
</tr>
<tr>
<td>最大 AM 比例</td>
<td>yarn.scheduler.capacity.&lt;queue-path>.maximum-am-resource-percent&lt;/queue-path></td>
<td>群集中可用于运行应用程序主机的最大资源百分比-控制并发活动应用程序的数量。</td>
</tr>
<tr>
<td>资源池优先级</td>
<td>yarn.scheduler.capacity.root.&lt;leaf-queue-path>.default-application-priority&lt;/leaf-queue-path></td>
<td>配置资源队列的优先级，默认为0，设置值越大，优先级越高。</td>
</tr>
<tr>
<td>提交访问控制</td>
<td>yarn.scheduler.capacity.root.&lt;queue-path>.acl_submit_applications</queue-path></td>
<td>可以提交 apps 到队列的用户的列表。</td>
</tr>
<tr>
<td>管理访问控制</td>
<td>yarn.scheduler.capacity.root.&lt;queue-path>.acl_administer_queue</queue-path></td>
<td>可以管理队列的用户的列表。</td>
</tr>
<tr>
<td>延迟调度</td>
<td>yarn.scheduler.capacity.node-locality-delay</td>
<td>保证任务本地化执行，可以延迟调度的次数。如果值为 -1，将禁用延迟调度。</td>
</tr>
</tbody></table>

### 配置资源池映射
1. 单击策略设置中的**资源池映射**即可进入资源池映射页面，单击**新建资源池映射**即可进行新建资源池映射。
![](https://qcloudimg.tencent-cloud.cn/raw/2172b90ec5546dd91972272fe43f7de6.png)
![](https://qcloudimg.tencent-cloud.cn/raw/39a7e01320e839a9639d764213c3a8fe.png)
2. 是否覆盖用户指定队列
默认关闭，假如用户在资源池映射中定义了映射的队列，且用户在提交任务时指定了队列，但是该队列与映射队列不同时：当用户指定的队列为 default 或者开启了覆盖，则会使用映射队列，否则使用用户指定的队列。

### 示例标签调度
1. 登录 [EMR 控制台](https://console.cloud.tencent.com/emr)，在集群列表中选择对应的 Hadoop 集群单击**详情**进入集群详情页。
2. 在集群详情页中选择**集群服务 > Yarn 组件卡页**右上角**操作 > 资源调度**进入资源调度页面。
3. 单击**资源调度器开关**，调度器类型选择 Capacity Scheduler。
4. 单击**标签调度开关**，打开标签调度后单击**标签管理**，进入标签管理页。
![](https://qcloudimg.tencent-cloud.cn/raw/ac2a25756122de0bb31e116f834af698.png)
5. 单击**新建标签**，填写标签名称，并根据需要设置标签类型和该标签绑定的节点。
![](https://qcloudimg.tencent-cloud.cn/raw/6b4ecde10e7bd5f234b468b9d75a96f2.png)
6. 标签设置完成后，单击**指令生效**，即可在资源池中编辑查看该标签的资源队列。
![](https://qcloudimg.tencent-cloud.cn/raw/abe05a0a956e0b28f5bac068c773c56a.png)
7. 在资源调度页中单击**新建资源池**，根据业务需要选择标签、容量、最大容量等。
>? 资源池在不同标签中的容量、最大容量相互独立，即可以按照业务分别进行配置，相互不影响。
>
![](https://qcloudimg.tencent-cloud.cn/raw/5082f7e272f21277b4c24e5e7342cad8.png)
![](https://qcloudimg.tencent-cloud.cn/raw/a675647042f975483f2b3acb8ef364d8.png)
8. 资源池设置完后，单击**部署生效**，即向后台提交了部署生效任务。
>! 由于 ResourceManager 重启属于高危操作，单击**部署生效**时如果提示会重启 ResourceManager，请在**调度历史中**查看操作是否成功，并在**角色管理**中查看 ResourceManager 健康状态是否良好。
