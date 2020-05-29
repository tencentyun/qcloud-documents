在 JAR 作业方式下，是用户自己基于 Flink 的 API 来开发业务逻辑，形成 JAR 包，然后提交到云端流计算集群上运行。这种方式适用于熟悉 Flink 开发的开发人员，支持他们通过更自由的开发实现，去应对复杂度更高的需求场景。

## 前提条件
- 需要根据业务需求情况，基于 Flink 的 API 开发好自己的 JAR 包。
- 需要先创建好自己的独享集群，请参见 [创建和管理集群](https://cloud.tencent.com/document/product/849/38380)。
- 需要准备好上下游数据，具体请参见 [上下游数据一览](https://cloud.tencent.com/document/product/849/38374)。

## 操作步骤

### 1. 创建 JAR 作业

登录 [流计算 Oceanus 控制台](https://console.cloud.tencent.com/oceanus)，单击左侧菜单栏【流计算】下的【作业管理】，进入作业管理页面。单击【新建JAR作业】，进入【新建作业】，选择您的独享集群，单击【下一步】。
> ? 如果这一步您没有可选的独享集群，请参见 [创建和管理集群](https://cloud.tencent.com/document/product/849/38380) 创建独享集群。

![新建JAR作业步骤1](https://main.qcloudimg.com/raw/97acd63eec13dcb9f12a3835263df950.png)
输入相关信息后单击【完成创建】，即可在【作业管理】页面看到新创建的作业。
![新建JAR作业步骤2](https://main.qcloudimg.com/raw/76dd4c6e105aedd9bb7f4e2f3b13a28e.png)
相关信息如下：

| 参数           | 说明                                           |
| -------------- | ---------------------------------------------- |
| 作业名称       | 给作业取一个名字                               |
| 作业运行的集群 | 您在上一步选择的自己创建的独享集群             |
| 算子默认并行度 | 请参见 [作业并行度设置](https://cloud.tencent.com/document/product/849/38377) |

### 2. 流计算服务委托授权
在【作业管理】页面单击某个作业名称打开【作业详情】页，单击【分析开发】，在未授权时，弹出访问授权对话框如下。单击【前往授权】，授权流计算作业访问您的 CKafka、TencentDB 等资源。
![角色授权弹框](https://main.qcloudimg.com/raw/0810024f6f10d6fb8a4ce689a274537f.png)

> ? 此授权的详细说明参见 [流计算服务委托授权](https://cloud.tencent.com/document/product/849/38290)。

### 3. JAR 作业开发和发布

在【作业管理】页面单击某个作业名称打开【作业详情】页，单击【分析开发】，进入作业开发页面。上传准备好的 JAR 包，输入配置信息，单击【保存并发布运行】，提交作业。
![JAR作业开发页面](https://main.qcloudimg.com/raw/39594fab8e4137dc2fa8a5b5209f7d4f.png)

相关信息如下：

| 参数      | 说明                       |
| --------- | -------------------------- |
| MainClass | JAR 包运行时的主类         |
| 主类入参  | JAR 包运行时主类的输入参数 |



