弹性 MapReduce（EMR）容器版提供了开源大数据组件完全基于容器服务部署的新体验。可以将 Spark 组件部署到云原生的弹性容器服务上，借助容器应用管理优势，可减少资源层的运维投入，快速构建起集群运行大数据作业。适用于需要突发运行 Spark 任务或作业级别调整 Spark 版本，便于快速尝试新特性，以满足不同业务对版本的需求。

## 原理介绍
EMR 容器集群在创建时，会在当前所选地域自动创建一个隐藏的 EMR 专用 EKS 集群，由 EMR 管控系统在 EKS 集群自动创建 EMR 容器集群资源。
当 EMR 容器集群提交 Spark 作业时，SparkOperator 会根据作业需求自动创建 Driver 和 Executor POD 资源，作业结束后释放相关 POD 资源。
![](https://qcloudimg.tencent-cloud.cn/raw/49a1c52271d128484ec17101f03d6278.png)
