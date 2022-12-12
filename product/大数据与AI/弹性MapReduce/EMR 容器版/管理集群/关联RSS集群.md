## 功能介绍
Spark 容器集群支持关联 RSS 集群，RSS 能够帮助解决大数据量 Spark 作业的磁盘写满、网络不稳定和随机 IO 等运行稳定性问题，同时可以提升大数据量 Shuffle 的性能，提高计算任务的运行速度和质量。
>! 当 RSS 集群被销毁时，需要在 Spark 容器集群手动解除关联。

## 操作步骤
1. 登录 [EMR 容器版控制台](https://console.cloud.tencent.com/emr/static/containerdeploy)，在集群列表中单击对应的 Spark 集群 **ID/名称**进入集群详情页。或登录 EMR 容器版控制台，在集群列表操作中选择**详情**。
2. 进入实例信息后，在**基础信息 > 关联 RSS 集群** 右侧单击**关联**。
![](https://qcloudimg.tencent-cloud.cn/raw/8f8378361273132fca52e7b3fb8ff726.png)
3. 根据需要选择 RSS 集群，确认无误后，单击**确定**，即完成关联 RSS 集群。
![](https://qcloudimg.tencent-cloud.cn/raw/602aa1e674c4a0c6b380175e9c9acd69.png)
4. 若您的 Spark 集群不再需要关联 RSS 集群，您可单击**解除关联**，确认无误后，单击**确定**，即解除关联 RSS 集群。
