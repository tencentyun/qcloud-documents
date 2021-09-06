## 功能介绍
Yarn 资源调度器提供界面化的集群资源管理能力，帮助用户提高集群资源的利用率；目前支持 Fair Scheduler 和 Capacity Scheduler 两种类型的配置。
- Fair Scheduler 即公平调度器，公平调度器能将资源公平的分配到 yarn 上的各个作业，权重可以用来调整资源的分配。
- Capacity Scheduler 即容量调度器，容量调度器以分层的方式组织资源，设计了多层级别的资源限制条件以更好的让多用户共享集群资源。

>!
- 资源调度器默认使用公平调度器，配置管理 YARN 组件 fair-scheduler.xml 配置文件中的相关配置项参数保持与资源调度页一致；切换调度器为容量调度器，配置管理 YARN 组件 capacity-scheduler.xml 配置文件中的相关配置参数也保持与资源调度页一致。
- 资源调度页设置策略后需单击**刷新动态资源池**让其配置管理中配置文件及配置参数保持一致，执行**刷新动态资源池**会进行对应策略得配置下发；删除资源池后，用户需要手动重启 ResoureManager。
- 切换调度器类型后需要单击**部署生效**才能生效，该操作会重启 ResourceManager。

## 配置 Fair Scheduler
1. 登录 [EMR 控制台](https://console.cloud.tencent.com/emr)，在集群列表中选择对应的 Hadoop 集群单击**详情**进入集群详情页。
2. 在集群详情页中选择**集群服务 > Yarn** 组件卡页右上角**操作 > 资源调度**进入资源调度页面。
![](https://main.qcloudimg.com/raw/808aa5b1c5b928c5eb6d7d19c54deb5c.png)
3. 单击**资源调度器开关**，打开后开关后即可进行相关调度器配置。
![](https://main.qcloudimg.com/raw/dd4ba878146a5f2b837b67700dd03b0c.png)
4. 新建 Fair Scheduler 资源池
调度器类型选择 Fair Scheduler 即可进行 Fair Scheduler 策略设置页面；单击**新建资源池**即可新建资源池；可对已有资源池进行编辑、新建子池、克隆、删除等操作。
![](https://main.qcloudimg.com/raw/ee6f82b6ae2fb26d494a107c2585773b.png)

**字段与配置项对照表**

| **字段名称**                | **对应参数名称**             | **参数含义**                                                 |
| --------------------------- | ---------------------------- | ------------------------------------------------------------ |
| 资源池名称                  | name                         | 资源池的名称或队列的名称。                                   |
| 父池     | type 的值为 parent   | 表示该资源池虽然底下没有子池，但它也不是叶子结点，在 hadoop 2.8 及以后父池不能有子池。 |
| 配置集                      | 无                           | yarn没有此参数，表示定时任务的集合。                         |
| 权重                        | weight                       | 在父池中的资源占比，权重越大分配的资源越多。                 |
| 最小资源量    | minResources  | 最少资源保证量，当一个队列的最少资源保证量未满足时，它将优先于其他同级队列获得资源。 |
| 最大资源量                  | maxResources                 | 最多可以使用的资源量，每个队列可使用的资源量不会超过该值。   |
| 最高可同时处于运行的 App 数量 | maxRunningApps               | 最多同时运行的应用程序数目，该限制可以防止超量 Map Task 同时运行时产生的中间输出结果撑爆磁盘。 |
| App Master 最大份额          | maxAMShare  | 限制队列用于运行 Application Master 的资源比例。这个属性只能用于叶子队列。 |
| 调度策略                 | schedulingPolicy             | 任一队列都可以设置调度策略，取值为 Fifo、Fair、Drf，其中 Fifo、Fair 在资源分配时只考虑内存，Drf 考虑内存和核数。 |
| 抢占模式   | allowPreemptionFrom | 在 hadoop 3.x 之后才生效，2.x只能由全局配置 yarn.scheduler.fair.preemption 控制。 |
| 公平份额抢占阈值            | fairSharePreemptionThreshold | 队列的公平共享抢占阈值。如果队列等待 fairSharePreemptionTimeout之后没有接收到 fairSharePreemptionThreshold\*fairShare 的资源，它被允许从其他队列抢占资源。如果不设置，队列将会从其父队列继承这个值。 |
| 公平份额抢占超时时间        | fairSharePreemptionTimeout   | 队列处在最小公平共享阈值之下，在尝试抢占其他队列的资源之前的秒数。如果不设置，队列将会从其父队列继承这个值。 |
| 最小共享优先权超时时间      | minSharePreemptionTimeout    | 队列处在最小共享之下，在尝试抢占其他队列的资源之前的秒数。如果不设置，队列将会从其父队列继承这个值。 |
| 提交访问控制                | aclSubmitApps                | 可以提交 apps 到队列的用户的列表。                             |
| 管理访问控制                | aclAdministerApps            | 可以管理队列的用户的列表。                                   |


5. 配置计划模式
单击策略设置中的**计划模式**即可进入计划模式页面，单击**新建计划模式**即可进行计划模式的新建。
![](https://main.qcloudimg.com/raw/d3b6d2018e00e7392ae234fbb8bbb09d.png)![](https://main.qcloudimg.com/raw/d753179694e4a2b60ec9bcfdb22a295d.png)
6. 配置放置规则
单击策略设置中的**放置规则**即可进入放置规则页面，单击**新建放置规则**即可进行放置规则的新建。
![](https://main.qcloudimg.com/raw/10f31cdd7ced8cf8453b2f25b2f2ae94.png)![](https://main.qcloudimg.com/raw/8b8e63b6702651fca4c977079e53a341.png)
7. 配置用户限制
单击策略设置中的**用户限制**即可进入用户限制页面，单击**新建用户限制**即可进行用户限制的新建。
![](https://main.qcloudimg.com/raw/0c914e1474e5e5ae65913d6cc39d011b.png)![](https://main.qcloudimg.com/raw/419db80fe7e655bda0d1f7b8d3c40023.png)

 
