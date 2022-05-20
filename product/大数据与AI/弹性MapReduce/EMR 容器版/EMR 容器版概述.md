弹性 MapReduce（EMR）容器版提供了开源大数据组件完全基于容器服务部署的新体验。可以将 Spark 组件部署到云原生的弹性容器服务上，借助容器应用管理优势，可减少资源层的运维投入，快速构建起集群运行大数据作业。适用于需要突发运行 Spark 任务或作业级别调整 Spark 版本，便于快速尝试新特性，以满足不同业务对版本的需求。

>! 当前 EMR 容器版为白名单开放，如需要可 [联系工单](https://console.cloud.tencent.com/workorder/category) 开通。

## 原理介绍
EMR 集群的主要运维操作，如集群创建、销毁等，通过 k8s 的 operator 进行。在创建过程中，通过 K8S API Server 调度各项资源，如 pod、configmap、secret、pvc、pv 等。提交任务到集群进行计算，EKS 定时推送集群资源使用量（cpu、mem）到 emrcc，由 emrcc 进⾏处理，调⽤计费平台服务进行相关费用的结算。
![](https://qcloudimg.tencent-cloud.cn/raw/92ca7888ce0f98feb8d188f94c4333e0.png)
