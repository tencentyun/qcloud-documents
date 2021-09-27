## 功能介绍
YARN 资源调度提供了交互式的 YARN 资源队列调度管理能力，较文件式配置管理操作更便捷，目前支持 Fair Scheduler 和 Capacity Scheduler 两种类型的调度配置。
- Fair Scheduler 是公平调度器，公平调度器将资源公平的分配给 yarn 上的各个作业，通过权重来调整资源的分配。
- Capacity Scheduler 是容量调度器，容量调度器以分层的方式组织资源,可通过多层级的资源限制条件让多用户共享集群资源。

>!
- 资源调度器默认使用公平调度器，配置管理 YARN 组件 fair-scheduler.xml 配置文件中的相关配置项参数保持与资源调度页一致。切换调度器为容量调度器，配置管理 YARN 组件 capacity-scheduler.xml 配置文件中的相关配置参数也保持与资源调度页一致。
- 资源调度页设置策略后需单击**刷新动态资源池**让其配置管理中配置文件及配置参数保持一致，执行**刷新动态资源池**会进行对应策略得配置下发。删除资源池后，用户需要手动重启 ResoureManager。删除资源池后，用户可以单击**部署生效**或者手动重启 ResoureManager。
- 切换调度器类型后需要单击**部署生效**才能生效，该操作会重启 ResourceManager。

## 配置 Fair Scheduler
1. 登录 [EMR 控制台](https://console.cloud.tencent.com/emr)，在集群列表中选择对应的 Hadoop 集群单击**详情**进入集群详情页。
2. 在集群详情页中选择**集群服务 > Yarn 组件卡**页右上角**操作 > 资源调度**进入资源调度页面。
![](https://main.qcloudimg.com/raw/808aa5b1c5b928c5eb6d7d19c54deb5c.png)
3. 单击**资源调度器开关**，打开开关后即可进行相关调度器配置。
![](https://main.qcloudimg.com/raw/dd4ba878146a5f2b837b67700dd03b0c.png)
4. 新建 Fair Scheduler 资源池
调度器类型选择 Fair Scheduler 即可进行 Fair Scheduler 策略设置页面，单击**新建资源池**即可新建资源池，可对已有资源池进行编辑、新建子池、克隆、删除等操作。
![](https://main.qcloudimg.com/raw/ee6f82b6ae2fb26d494a107c2585773b.png)
**字段与配置项对照表**
<table>
<thead>
<tr>
<th><strong>字段名称</strong></th>
<th><strong>对应参数名称</strong></th>
<th><strong>参数含义</strong></th>
</tr>
</thead>
<tbody><tr>
<td>资源池名称</td>
<td>name</td>
<td>资源池的名称或队列的名称。</td>
</tr>
<tr>
<td>父池</td>
<td>type 的值为 parent</td>
<td>表示该资源池虽然底下没有子池，但它也不是叶子结点，在 hadoop 2.8 及以后父池不能有子池。</td>
</tr>
<tr>
<td>配置集</td>
<td>无</td>
<td>yarn没有此参数，表示定时任务的集合。</td>
</tr>
<tr>
<td>权重</td>
<td>weight</td>
<td>在父池中的资源占比，权重越大分配的资源越多。</td>
</tr>
<tr>
<td>最小资源量</td>
<td>minResources</td>
<td>最少资源保证量，当一个队列的最少资源保证量未满足时，它将优先于其他同级队列获得资源。</td>
</tr>
<tr>
<td>最大资源量</td>
<td>maxResources</td>
<td>最多可以使用的资源量，每个队列可使用的资源量不会超过该值。</td>
</tr>
<tr>
<td>最高可同时处于运行的 App 数量</td>
<td>maxRunningApps</td>
<td>最多同时运行的应用程序数目，该限制可以防止超量 Map Task 同时运行时产生的中间输出结果撑爆磁盘。</td>
</tr>
<tr>
<td>App Master 最大份额</td>
<td>maxAMShare</td>
<td>限制队列用于运行 Application Master 的资源比例。这个属性只能用于叶子队列。</td>
</tr>
<tr>
<td>调度策略</td>
<td>schedulingPolicy</td>
<td>任一队列都可以设置调度策略，取值为 Fifo、Fair、Drf，其中 Fifo、Fair 在资源分配时只考虑内存，Drf 考虑内存和核数。</td>
</tr>
<tr>
<td>抢占模式</td>
<td>allowPreemptionFrom</td>
<td>在 hadoop 3.x 之后才生效，2.x只能由全局配置 yarn.scheduler.fair.preemption 控制。</td>
</tr>
<tr>
<td>公平份额抢占阈值</td>
<td>fairSharePreemptionThreshold</td>
<td>队列的公平共享抢占阈值。如果队列等待 fairSharePreemptionTimeout 之后没有接收到 fairSharePreemptionThreshold*fairShare 的资源，它被允许从其他队列抢占资源。如果不设置，队列将会从其父队列继承这个值。</td>
</tr>
<tr>
<td>公平份额抢占超时时间</td>
<td>fairSharePreemptionTimeout</td>
<td>队列处在最小公平共享阈值之下，在尝试抢占其他队列的资源之前的秒数。如果不设置，队列将会从其父队列继承这个值。</td>
</tr>
<tr>
<td>最小共享优先权超时时间</td>
<td>minSharePreemptionTimeout</td>
<td>队列处在最小共享之下，在尝试抢占其他队列的资源之前的秒数。如果不设置，队列将会从其父队列继承这个值。</td>
</tr>
<tr>
<td>提交访问控制</td>
<td>aclSubmitApps</td>
<td>可以提交 apps 到队列的用户的列表。</td>
</tr>
<tr>
<td>管理访问控制</td>
<td>aclAdministerApps</td>
<td>可以管理队列的用户的列表。</td>
</tr>
</tbody></table>
5. 配置计划模式
单击策略设置中的**计划模式**即可进入计划模式页面，单击**新建计划模式**即可进行计划模式的新建。
![](https://main.qcloudimg.com/raw/d3b6d2018e00e7392ae234fbb8bbb09d.png)![](https://main.qcloudimg.com/raw/d753179694e4a2b60ec9bcfdb22a295d.png)
6. 配置放置规则
单击策略设置中的**放置规则**即可进入放置规则页面，单击**新建放置规则**即可进行放置规则的新建。
![](https://main.qcloudimg.com/raw/10f31cdd7ced8cf8453b2f25b2f2ae94.png)![](https://main.qcloudimg.com/raw/8b8e63b6702651fca4c977079e53a341.png)
7. 配置用户限制
单击策略设置中的**用户限制**即可进入用户限制页面，单击**新建用户限制**即可进行用户限制的新建。
![](https://main.qcloudimg.com/raw/0c914e1474e5e5ae65913d6cc39d011b.png)![](https://main.qcloudimg.com/raw/419db80fe7e655bda0d1f7b8d3c40023.png)

## 配置 Capacity Scheduler
1. 登录 [EMR 控制台](https://console.cloud.tencent.com/emr)，在集群列表中选择对应的 Hadoop 集群单击**详情**进入集群详情页。
2. 在集群详情页中选择**集群服务 > Yarn 组件**卡页右上角**操作 > 资源调度**进入资源调度页面。
![](https://main.qcloudimg.com/raw/068cbd684c9f615f1d6d6d690d9782f9.png)
3. 单击**资源调度器开关**，打开开关后即可进行相关调度器配置。
4. 新建 Capacity Scheduler
调度策略类型选择 Capacity Scheduler 即可进入 Capacity Scheduler 的配置页面，单击**新增资源池**即可新建资源池，可对已有资源池进行编辑、新建子池、克隆等操作。
![](https://main.qcloudimg.com/raw/d4e9fdfbe1550dba3b896aa0522ff09a.png)![](https://main.qcloudimg.com/raw/f7e4335375f03c2762d9e0953ee02011.png)
**字段与配置项对照表**
<table>
<thead>
<tr>
<th><strong>字段名称</strong></th>
<th><strong>对应参数名称</strong></th>
<th><strong>参数含义</strong></th>
</tr>
</thead>
<tbody><tr>
<td>资源池名称</td>
<td><code>yarn.scheduler.capacity.&lt;queue-path&gt;.queues</code></td>
<td>资源池的名称或队列的名称。</td>
</tr>
<tr>
<td>容量</td>
<td><code>yarn.scheduler.capacity.&lt;queue-path&gt;.capacity</code></td>
<td>表示该队列占用整个集群资源的比例，所有队列资源的总和等于100%。如果该队列需要比这个比例更高的资源，而其他队列又有空闲资源的话，可以占用比这个比例更高的资源。</td>
</tr>
<tr>
<td>最大容量</td>
<td><code>yarn.scheduler.capacity.&lt;queue-path&gt;.maximum-capacity</code></td>
<td>队列的资源使用上限（百分比）。由于存在资源共享，因此一个队列使用的资源量可能超过其容量，而最多使用资源量可通过该参数限制。</td>
</tr>
<tr>
<td>用户最小容量</td>
<td><code>yarn.scheduler.capacity.&lt;queue-path&gt;.minimum-user-limit-percent</code></td>
<td>每个用户最低资源保障（百分比）。任何时刻，一个队列中每个用户可使用的资源量均有一定的限制。当一个队列中同时运行多个用户的应用程序时中，每个用户的使用资源量在一个最小值和最大值之间浮动，其中，最小值取决于正在运行的应用程序数目，而最大值则由 minimum-user-limit-percent 决定。</td>
</tr>
<tr>
<td>用户资源因子</td>
<td><code>yarn.scheduler.capacity.&lt;queue-path&gt;.user-limit-factor</code></td>
<td>每个用户最多可使用的资源量（百分比）。例如，假设该值为30，则任何时刻，每个用户使用的资源量不能超过该队列容量的30%。</td>
</tr>
<tr>
<td>分配 Container 最大内存数量</td>
<td><code>yarn.scheduler.capacity.&lt;queue-path&gt;.maximum-allocation-mb</code></td>
<td>每个 container 的最大内存值，这个配置会覆盖 yarn.scheduler.maximum-allocation-mb 值，但是该值必须小于等于系统的 yarn.scheduler.maximum-allocation-mb 的值。</td>
</tr>
<tr>
<td>Container 最大 vCore 数量</td>
<td>-</td>
<td>资源池状态为 STOPPED 状态，任何任务都无法提交到该资源池以及子池中。</td>
</tr>
<tr>
<td>资源池状态</td>
<td><code>yarn.scheduler.capacity.&lt;queue-path&gt;.state</code></td>
<td>队列的状态。可以是正在运行或已停止。如果队列处于停止状态，则无法向其自身或其任何子队列提交新的应用程序。</td>
</tr>
<tr>
<td>最大应用数 Max-Applications</td>
<td><code>yarn.scheduler.capacity.&lt;queue-path&gt;.maximum-applications</code></td>
<td>系统中可同时处于活动状态（正在运行和挂起）的最大应用程序数。</td>
</tr>
<tr>
<td>最大 AM 比例</td>
<td><code>yarn.scheduler.capacity.&lt;queue-path&gt;.maximum-am-resource-percent</code></td>
<td>群集中可用于运行应用程序主机的最大资源百分比-控制并发活动应用程序的数量。</td>
</tr>
<tr>
<td>提交访问控制</td>
<td><code>yarn.scheduler.capacity.root.&lt;queue-path&gt;.acl_submit_applications</code></td>
<td>可以提交 apps 到队列的用户的列表。</td>
</tr>
<tr>
<td>管理访问控制</td>
<td><code>yarn.scheduler.capacity.root.&lt;queue-path&gt;.acl_administer_queue</code></td>
<td>可以管理队列的用户的列表。</td>
</tr>
</tbody></table>
5. 配置资源池映射
单击策略设置中的**资源池映射**即可进入资源池映射页面，单击**新建资源池映射**即可进行新建资源池映射。
![](https://main.qcloudimg.com/raw/b3e089a06b25d0621eef90880fb6cc53.png)![](https://main.qcloudimg.com/raw/e6e413fcfdd530a6861f98165e5cc8cb.png)
6. 是否覆盖用户指定队列
默认关闭，假如用户在资源池映射中定义了映射的队列，且用户在提交任务时指定了队列，但是该队列与映射队列不同时：当用户指定的队列为 default 或者开启了覆盖，则会使用映射队列，否则使用用户指定的队列。
![](https://main.qcloudimg.com/raw/df4add0e67c84e3a7dad8e171372bb3e.png)
 
