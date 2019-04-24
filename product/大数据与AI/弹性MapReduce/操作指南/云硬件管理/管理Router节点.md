

通常情况下，Hive、Hue、Spark等进程默认部署在Master节点，任务都在Master节点上部署和提交。当集群规模较大或者部署了太多应用程序时，Master节点可能出现内存不足等情况，这个时候，可以通过扩展一台或者多台Router节点，将主节点部分进程分担到其他Router节点上，和在Master节点一样的方式使用它们，来分担主节点的压力。
Router节点可以当提交机使用，可以在router节点上向集群正常提交计算Yarn、Hive、Spark等计算任务。
点击【新增Router节点】添加Router节点，并可以选择在Router节点上部署【必选组件】和【可选组件】，可选组件可根据业务需要进行选择，选择后，点击【下一步】进行硬盘规格，磁盘类型、数量等选择， Router节点可新增多个。
![](https://main.qcloudimg.com/raw/26f6a30c44ca9e84c3e905294db7d583.png)
![](https://main.qcloudimg.com/raw/7867eaba487ac9cf703186c98af09874.png)

