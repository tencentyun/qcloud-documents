## 功能介绍
Fair Scheduler 是公平调度器，公平调度器将资源公平的分配给 yarn 上的各个作业，通过权重来调整资源的分配。
## 名词解释
- 配置集：定义在给定时间内处于活动状态的资源池之间的资源分配。
- 计划模式：定义配置集何时处于活动状态。
- 放置规则：通过放置规则将不同的用户提交的作业自动分配到指定的资源池中。
- 用户限制：定义用户可以同时提交的最多应用程序数量。

## 操作步骤
### 新建资源池
1. 登录 [EMR 控制台](https://console.cloud.tencent.com/emr)，在集群列表中选择对应的 Hadoop 集群单击**详情**进入集群详情页。
2. 在集群详情页中选择**集群服务 > Yarn 组件卡页**右上角**操作 > 资源调度**进入资源调度页面。
![](https://qcloudimg.tencent-cloud.cn/raw/16320db2e3a68ebf6ff3733c26201bc9.png)
3. 单击**资源调度器开关**，打开开关后即可进行相关调度器配置。
![](https://qcloudimg.tencent-cloud.cn/raw/da6a4c4cb0f1b09a1a11f87877c302cd.png)
4. 新建 Fair Scheduler 资源池
调度器类型选择 Fair Scheduler 即可进入 Fair Scheduler 策略设置页面，单击**新建资源池**即可新建资源池，可对已有资源池进行编辑、新建子池、克隆、删除等操作。
![](https://qcloudimg.tencent-cloud.cn/raw/4598532c402c263efc3552d77151401a.png)
**字段与配置项对照表：**
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
<td>name</td>
<td>资源池的名称或队列的名称。资源池名称只能由含数字、字母，-或_组成，不能以-或_开头。</td>
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


### 配置计划模式
1. 单击策略设置中的**计划模式**即可进入计划模式页面，单击**新建计划模式**即可进行计划模式的新建。
**配置集状态**用于标记计划模式是否开启，默认为开启状态，若不需要使用自定义计划模式但仍想保留配置集，可将**配置集状态**设置为关闭。
2. 在新建计划模式中选择/填写配置集、名称和计划有效时间。
![](https://qcloudimg.tencent-cloud.cn/raw/40906d8b180daba5705f1f925d2e527d.png)

### 示例配置集
1. 登录 [EMR 控制台](https://console.cloud.tencent.com/emr)，在集群列表中选择对应的 Hadoop 集群单击**详情**进入集群详情页。
2. 在集群详情页中选择**集群服务 > Yarn 组件卡页**右上角**操作 > 资源调度**进入资源调度页面。
3. 单击**资源调度器开关**，调度器类型选择 Fair Scheduler 。
4. 单击**新建资源池**，根据实际需求进行配置。
![](https://qcloudimg.tencent-cloud.cn/raw/085278739c837cd8b8953a8d93d0ecd4.png)
5. 在资源调度页中选择**计划模式>新建计划模式**，根据业务需要调整计划有效时间。
>? 如果 EMR 集群配置了定时扩容，建议将计划模式的计划有效时间设置在定时扩容之后。
>
![](https://qcloudimg.tencent-cloud.cn/raw/7ae0572347df707c7389d85ff74ce488.png)
![](https://qcloudimg.tencent-cloud.cn/raw/89318116a64fcfadca1aca35ff2b9745.png)
6. 在资源调度页中选择**资源池**，在**配置集**下拉选项中，选择一个配置集。
>? 资源池在不同配置集中的资源量限制相互独立，即可以按照业务分别进行配置，相互不影响。
>
![](https://qcloudimg.tencent-cloud.cn/raw/37b2ecb065c0df19d39e92a9eb360f5a.png)
7. 在**配置集**下选择之前创建的资源池，按照业务进⾏资源量限制的调整。
![](https://qcloudimg.tencent-cloud.cn/raw/f96f07a7b414bb5b0ca842bc62c5e3fe.png)
![](https://qcloudimg.tencent-cloud.cn/raw/c5a4ccb6eabee693c2539b9fa78d8e7d.png)
![](https://qcloudimg.tencent-cloud.cn/raw/0bdf077e98540416cb104b78a647a559.png)
8. 资源池调整完后，单击**部署生效**，即可使设置生效。


### 配置放置规则
单击策略设置中的**放置规则**即可进入放置规则页面，单击**新建放置规则**即可进行放置规则的新建。
![](https://qcloudimg.tencent-cloud.cn/raw/cd120385fa49067e50cae7c8d0b959a2.png)
填写放置类型和池名称。
![](https://qcloudimg.tencent-cloud.cn/raw/d3cdc014b72b1490cfdf9ec63af822f7.png)
**配置规则类型说明：**
**root.[pool name]**：该规则始终满足，在其它规则不匹配的情况下使用，因此该规则默认要放置在所有匹配规则之后。
**root.[pool name].[username]**：该放置规则会判断资源池中是否存在相应的pool name，存在则在该资源池下创建与用户名相同的资源池（勾选池不存在时创建池的情况下）。
**root.[primary group]**：该规则使用与该用户主要组匹配的资源池。Linux中用户默认的主要组与用户名一致，匹配时会通过用户的主要组与资源池名称比对。
**root.[primary group].[username]**：该放置规则会优先使用用户的主要组匹配的资源池，然后使用与该用户名匹配的子池，如果勾选池不存在时创建池则会在该池下创建一个与用户名一致的子池。
**root.[secondarygroup]**：该放置规则用于匹配用户的次要组，使用与次要组之一匹配的资源池。
**root.[secondarygroup].[username]**：该放置规则首先匹配用户的次要组，然后使用与该用户名匹配的资源池。
**root.[username]**：该放置规则用于匹配与用户名一致的资源池。（不推荐使用）
已在运行时指定：该放置规则主要使用在运行时指定的资源池。
放置规则的判断方式，根据放置规则的顺序1、2、3…进行判断，判断到满足条件的放置规则后，后续的规则不再进行匹配。

### 配置用户限制
单击策略设置中的**用户限制**即可进入用户限制页面，单击**新建用户限制**即可进行用户限制的新建。
![](https://qcloudimg.tencent-cloud.cn/raw/4b79b6bc1fa307e127efb51cef890dbb.png)
填写用户名称和同时运行应用程序上限：
![](https://qcloudimg.tencent-cloud.cn/raw/ecc5ee92ec96ca534635bbbc8d289c02.png)
