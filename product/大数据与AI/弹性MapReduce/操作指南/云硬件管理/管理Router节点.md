## 操作场景
通常情况下，Hive、Hue、Spark 等进程默认部署在 Master 节点，任务都在 Master 节点上部署和提交。当集群规模较大或者部署了太多应用程序时，Master 节点可能出现内存不足等情况，此时，可通过扩展一台或者多台 Router 节点，将主节点部分进程分担到其他 Router 节点上，和在 Master 节点一样的方式使用它们，来分担主节点的压力。

Router 节点可以当提交机使用，可以在 Router 节点上向集群正常提交计算 Yarn、Hive、Spark 等计算任务。

## 操作步骤
1. 登录 [EMR 控制台](https://console.cloud.tencent.com/emr)，在左侧栏选择【云硬件管理】页。
2. 在云硬件列表页，单击【新增router节点】。
3. 在新增 Router 页，可以选择在 Router 节点上部署【必选组件】和【可选组件】，可选组件可根据业务需要进行选择。
![](https://main.qcloudimg.com/raw/b129228c544f8995f0910ccfd7aecb78.png)
4. 单击【下一步】进行付费类型、磁盘类型、数量等选择， Router 节点可同时新增多个。
![](https://main.qcloudimg.com/raw/86613fe61cac1f197330abf9f0567322.png)
5. 确认无误后，单击【购买】，完成支付后，可返回控制台列表查看新增的 Router 节点。
